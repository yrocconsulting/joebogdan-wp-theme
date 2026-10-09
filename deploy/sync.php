<?php
/**
 * Content sync, run on the server by the deploy workflow:
 *
 *   wp eval-file ../jb-sync/deploy/sync.php
 *
 * Creates/updates pages, menus, categories and site options from
 * content/manifest.json. It never overwrites a page or menu that someone has
 * edited in WordPress since the last sync, unless that page's slug is listed
 * in JB_FORCE (comma separated, or "all").
 *
 * Env: JB_ENV (staging|production), JB_FORCE, JB_LEAD_EMAIL.
 */

if ( ! defined( 'WP_CLI' ) ) {
	exit( 1 );
}

$base     = dirname( __DIR__ );
$manifest = json_decode( file_get_contents( $base . '/content/manifest.json' ), true );
$env      = getenv( 'JB_ENV' ) ?: 'staging';
$force    = array_filter( array_map( 'trim', explode( ',', (string) getenv( 'JB_FORCE' ) ) ) );
$force_all = in_array( 'all', $force, true );

// Content is trusted repo content; don't let kses strip block markup.
kses_remove_filters();

function jb_sync_log( $msg ) {
	WP_CLI::log( $msg );
}

/* ---------------------------------------------------------------- theme */
if ( 'joe-bogdan-mlo' !== get_stylesheet() ) {
	switch_theme( 'joe-bogdan-mlo' );
	jb_sync_log( 'Activated theme joe-bogdan-mlo' );
}

/* -------------------------------------------------------------- options */
update_option( 'permalink_structure', '/%postname%/' );
update_option( 'blogname', 'Joseph Bogdan' );
update_option( 'blogdescription', 'Senior Loan Officer · NMLS #2795320' );
update_option( 'timezone_string', 'America/Chicago' );
update_option( 'default_comment_status', 'closed' );
update_option( 'default_ping_status', 'closed' );
// Production is indexable unless JB_INDEX=0 (e.g. a soft launch before compliance sign-off).
$indexable = 'production' === $env && '0' !== getenv( 'JB_INDEX' );
update_option( 'blog_public', $indexable ? '1' : '0' );
jb_sync_log( 'Search engine visibility: ' . ( $indexable ? 'ON' : 'OFF' ) );

// Lead routing from the workflow. A value the deploy wrote earlier is updated;
// a value someone changed in Appearance → Joseph Bogdan Settings is kept.
$settings = (array) get_option( 'jb_settings', array() );
$managed  = (array) get_option( 'jb_settings_managed', array() );
foreach ( array( 'lead_email' => 'JB_LEAD_EMAIL', 'lead_bcc' => 'JB_LEAD_BCC' ) as $key => $var ) {
	$want = getenv( $var );
	if ( false === $want ) {
		continue;
	}
	$current = $settings[ $key ] ?? '';
	$ours    = '' === $current || ( isset( $managed[ $key ] ) && $managed[ $key ] === $current )
		// Earlier deploys wrote this address before routing was tracked.
		|| ( ! isset( $managed[ $key ] ) && 'bradley@yrocconsulting.com' === $current );
	if ( $force_all || in_array( 'settings', $force, true ) ) {
		$ours = true; // JB_FORCE=settings: the workflow's values win.
	}
	if ( $ours && $current !== $want ) {
		$settings[ $key ] = $want;
		$managed[ $key ]  = $want;
		jb_sync_log( "Setting $key: " . ( '' === $want ? '(cleared)' : $want ) );
	} elseif ( ! $ours ) {
		jb_sync_log( "Keeping $key set in WordPress: $current" );
	} else {
		$managed[ $key ] = $want;
	}
}
update_option( 'jb_settings', $settings );
update_option( 'jb_settings_managed', $managed );

/* -------------------------------------------------- default WP content */
foreach ( array( array( 'hello-world', 'post' ), array( 'sample-page', 'page' ) ) as $default ) {
	$found = get_page_by_path( $default[0], OBJECT, $default[1] );
	if ( $found && ! get_post_meta( $found->ID, '_jb_sync_hash', true ) ) {
		wp_delete_post( $found->ID, true );
		jb_sync_log( "Removed default {$default[1]} {$default[0]}" );
	}
}

/* ----------------------------------------------------------- categories */
foreach ( $manifest['categories'] as $cat ) {
	$term = get_term_by( 'slug', $cat['slug'], 'category' );
	if ( ! $term ) {
		wp_insert_term( $cat['name'], 'category', array( 'slug' => $cat['slug'], 'description' => $cat['description'] ) );
		jb_sync_log( "Created category {$cat['slug']}" );
	} elseif ( $term->description !== $cat['description'] ) {
		wp_update_term( $term->term_id, 'category', array( 'description' => $cat['description'] ) );
		jb_sync_log( "Updated category description {$cat['slug']}" );
	}
}
$default_cat = get_term_by( 'slug', $manifest['categories'][0]['slug'], 'category' );
if ( $default_cat ) {
	update_option( 'default_category', $default_cat->term_id );
	$uncat = get_term_by( 'slug', 'uncategorized', 'category' );
	if ( $uncat && 0 === (int) $uncat->count ) {
		wp_delete_term( $uncat->term_id, 'category' );
	}
}

/* ---------------------------------------------------------------- pages */
$ids = array();
foreach ( $manifest['pages'] as $spec ) {
	$slug    = $spec['slug'];
	$content = file_get_contents( $base . '/content/' . $spec['file'] );
	$parent  = $spec['parent'] ? ( $ids[ $spec['parent'] ] ?? 0 ) : 0;
	$path    = $spec['parent'] ? $spec['parent'] . '/' . $slug : $slug;

	$existing = get_page_by_path( $path, OBJECT, 'page' );
	$renamed  = false;
	foreach ( (array) ( $spec['old_slugs'] ?? array() ) as $old_slug ) {
		if ( ! $existing ) {
			$existing = get_page_by_path( $old_slug, OBJECT, 'page' );
			if ( $existing ) {
				jb_sync_log( "Renaming $old_slug -> $slug" );
				$renamed = true;
			}
		}
	}
	if ( ! $existing ) {
		$q = get_posts( array( 'post_type' => 'page', 'name' => $slug, 'post_status' => array( 'publish', 'draft', 'private', 'pending' ), 'numberposts' => 1 ) );
		$existing = $q ? $q[0] : null;
	}

	$postarr = array(
		'post_type'    => 'page',
		'post_status'  => 'publish',
		'post_title'   => $spec['title'],
		'post_name'    => $slug,
		'post_content' => $content,
		'post_parent'  => $parent,
		'menu_order'   => (int) $spec['menu_order'],
		'post_excerpt' => $spec['excerpt'],
	);

	if ( $existing ) {
		$stored  = get_post_meta( $existing->ID, '_jb_sync_hash', true );
		$current = md5( $existing->post_content );
		$edited  = $stored ? $stored !== $current : ( '' !== trim( $existing->post_content ) && 'publish' === $existing->post_status );
		if ( $edited && ! $force_all && ! in_array( $slug, $force, true ) ) {
			if ( $renamed ) {
				// Keep their edits but still move the page to its new address.
				wp_update_post( array( 'ID' => $existing->ID, 'post_name' => $slug ) );
			}
			jb_sync_log( "SKIP $path (edited in WordPress; add to JB_FORCE to overwrite)" );
			$ids[ $slug ] = $existing->ID;
			continue;
		}
		if ( ! $renamed && $stored === md5( $content ) && $existing->post_status === 'publish' && (int) $existing->post_parent === $parent ) {
			$ids[ $slug ] = $existing->ID;
			jb_sync_log( "ok   $path (unchanged)" );
		} else {
			$postarr['ID'] = $existing->ID;
			wp_update_post( wp_slash( $postarr ) );
			$ids[ $slug ] = $existing->ID;
			jb_sync_log( "UPD  $path" );
		}
	} else {
		$ids[ $slug ] = wp_insert_post( wp_slash( $postarr ) );
		jb_sync_log( "NEW  $path" );
	}

	$id = $ids[ $slug ];
	// Hash of what WordPress actually stored, so later human edits are detectable.
	update_post_meta( $id, '_jb_sync_hash', md5( get_post_field( 'post_content', $id ) ) );
	update_post_meta( $id, '_wp_page_template', $spec['template'] ? $spec['template'] : 'default' );
	update_post_meta( $id, '_jb_seo_title', $spec['seo_title'] );
	update_post_meta( $id, '_jb_seo_description', $spec['seo_description'] );
	update_post_meta( $id, '_jb_service', $spec['service'] );
	update_post_meta( $id, '_jb_audience', $spec['audience'] ?? '' );
}

update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $ids[ $manifest['front_page'] ] );
update_option( 'page_for_posts', $ids[ $manifest['posts_page'] ] );
update_option( 'wp_page_for_privacy_policy', $ids['privacy-policy'] ?? 0 );

/* ---------------------------------------------------------------- posts */
/**
 * Import a theme image into the media library once and reuse it.
 */
function jb_sync_theme_image( $file ) {
	// Stock photos are shared across articles, so they are marked decorative
	// (empty alt) until article-specific photography replaces them.
	$alts = array();
	$existing = get_posts( array( 'post_type' => 'attachment', 'meta_key' => '_jb_source_file', 'meta_value' => $file, 'numberposts' => 1, 'fields' => 'ids' ) );
	if ( $existing ) {
		update_post_meta( $existing[0], '_wp_attachment_image_alt', $alts[ $file ] ?? '' );
		return $existing[0];
	}
	$src = get_theme_root() . '/joe-bogdan-mlo/assets/images/' . $file;
	if ( ! file_exists( $src ) ) {
		return 0;
	}
	$upload = wp_upload_bits( $file, null, file_get_contents( $src ) );
	if ( ! empty( $upload['error'] ) ) {
		jb_sync_log( "Image upload failed for $file: {$upload['error']}" );
		return 0;
	}
	require_once ABSPATH . 'wp-admin/includes/image.php';
	$id = wp_insert_attachment( array(
		'post_mime_type' => wp_check_filetype( $upload['file'] )['type'],
		'post_title'     => sanitize_title( pathinfo( $file, PATHINFO_FILENAME ) ),
		'post_status'    => 'inherit',
	), $upload['file'] );
	wp_update_attachment_metadata( $id, wp_generate_attachment_metadata( $id, $upload['file'] ) );
	update_post_meta( $id, '_jb_source_file', $file );
	update_post_meta( $id, '_wp_attachment_image_alt', $alts[ $file ] ?? '' );
	jb_sync_log( "Imported image $file" );
	return $id;
}

// Articles are authored by a "Joseph Bogdan" account (never the admin login).
$joseph = get_user_by( 'login', 'joseph-bogdan' );
if ( ! $joseph ) {
	$uid = wp_insert_user( array(
		'user_login'   => 'joseph-bogdan',
		'user_pass'    => wp_generate_password( 32, true, true ),
		'user_email'   => '',
		'display_name' => 'Joseph Bogdan',
		'nickname'     => 'Joseph Bogdan',
		'first_name'   => 'Joseph',
		'last_name'    => 'Bogdan',
		'role'         => 'author',
	) );
	$joseph = is_wp_error( $uid ) ? null : get_user_by( 'id', $uid );
	jb_sync_log( $joseph ? 'Created author account Joseph Bogdan' : 'Could not create author account: ' . $uid->get_error_message() );
}
$author = $joseph ? array( $joseph->ID ) : get_users( array( 'role' => 'administrator', 'number' => 1, 'fields' => 'ID' ) );
foreach ( $manifest['posts'] ?? array() as $spec ) {
	$slug     = $spec['slug'];
	$content  = file_get_contents( $base . '/content/' . $spec['file'] );
	$existing = get_page_by_path( $slug, OBJECT, 'post' );
	$cat      = get_term_by( 'slug', $spec['category'], 'category' );
	$postarr  = array(
		'post_type'     => 'post',
		'post_status'   => 'publish',
		'post_title'    => $spec['title'],
		'post_name'     => $slug,
		'post_content'  => $content,
		'post_excerpt'  => $spec['excerpt'],
		'post_category' => $cat ? array( $cat->term_id ) : array(),
		'post_author'   => $author ? (int) $author[0] : 1,
	);

	if ( $existing ) {
		$stored = get_post_meta( $existing->ID, '_jb_sync_hash', true );
		$edited = $stored && $stored !== md5( $existing->post_content );
		if ( $edited && ! $force_all && ! in_array( $slug, $force, true ) ) {
			jb_sync_log( "SKIP post $slug (edited in WordPress; add to JB_FORCE to overwrite)" );
			continue;
		}
		if ( $stored === md5( $content ) && $existing->post_excerpt === $spec['excerpt'] ) {
			$id = $existing->ID;
			jb_sync_log( "ok   post $slug (unchanged)" );
		} else {
			$postarr['ID'] = $existing->ID;
			unset( $postarr['post_author'] );
			wp_update_post( wp_slash( $postarr ) );
			$id = $existing->ID;
			jb_sync_log( "UPD  post $slug" );
		}
	} else {
		$id = wp_insert_post( wp_slash( $postarr ) );
		jb_sync_log( "NEW  post $slug" );
	}

	if ( $joseph && (int) get_post_field( 'post_author', $id ) !== (int) $joseph->ID ) {
		wp_update_post( array( 'ID' => $id, 'post_author' => $joseph->ID ) );
		jb_sync_log( "     post $slug now authored by Joseph Bogdan" );
	}
	update_post_meta( $id, '_jb_sync_hash', md5( get_post_field( 'post_content', $id ) ) );
	update_post_meta( $id, '_jb_seo_title', $spec['seo_title'] );
	update_post_meta( $id, '_jb_seo_description', $spec['seo_description'] );
	if ( ! empty( $spec['image'] ) ) {
		$img = jb_sync_theme_image( $spec['image'] );
		if ( $img && ! has_post_thumbnail( $id ) ) {
			set_post_thumbnail( $id, $img );
		}
	}
}

/* ---------------------------------------------------------------- menus */
function jb_menu_signature( $menu_id ) {
	$items = wp_get_nav_menu_items( $menu_id ) ?: array();
	return md5( wp_json_encode( array_map( function ( $i ) {
		// post_title is the stored label (empty when it follows the page title),
		// so renaming a page doesn't look like a hand edit to the menu.
		return array( $i->post_title, (int) $i->object_id, (int) $i->menu_item_parent ? 1 : 0, (int) $i->menu_order );
	}, $items ) ) );
}

$names     = array( 'primary' => 'Primary', 'footer' => 'Footer', 'legal' => 'Legal' );
$locations = get_theme_mod( 'nav_menu_locations', array() );
$state     = (array) get_option( 'jb_menu_state', array() );

foreach ( $manifest['menus'] as $location => $items ) {
	$spec_hash = md5( wp_json_encode( $items ) );
	$menu_id   = $locations[ $location ] ?? 0;
	$menu      = $menu_id ? wp_get_nav_menu_object( $menu_id ) : null;

	if ( $menu ) {
		$known = $state[ $location ] ?? array();
		$human = empty( $known['sig'] ) || jb_menu_signature( $menu->term_id ) !== $known['sig'];
		if ( $human && ! empty( $known['sig'] ) ) {
			// Signatures saved by an earlier version used display titles.
			$legacy = md5( wp_json_encode( array_map( function ( $i ) {
				return array( $i->title, (int) $i->object_id, (int) $i->menu_item_parent ? 1 : 0, (int) $i->menu_order );
			}, wp_get_nav_menu_items( $menu->term_id ) ?: array() ) ) );
			$human = $legacy !== $known['sig'];
		}
		if ( $human && ! $force_all && ! in_array( 'menu-' . $location, $force, true ) ) {
			jb_sync_log( "SKIP menu $location (edited in WordPress; add menu-$location to JB_FORCE to rebuild)" );
			continue;
		}
		if ( ! $human && ( $known['spec'] ?? '' ) === $spec_hash ) {
			jb_sync_log( "ok   menu $location (unchanged)" );
			continue;
		}
		foreach ( wp_get_nav_menu_items( $menu->term_id ) ?: array() as $old ) {
			wp_delete_post( $old->ID, true );
		}
		$menu_id = $menu->term_id;
	} else {
		$existing = wp_get_nav_menu_object( $names[ $location ] );
		$menu_id  = $existing ? $existing->term_id : wp_create_nav_menu( $names[ $location ] );
	}

	$order = 1;
	foreach ( $items as $item ) {
		$parent_item = wp_update_nav_menu_item( $menu_id, 0, array(
			'menu-item-title'     => $item['title'],
			'menu-item-object'    => 'page',
			'menu-item-object-id' => $ids[ $item['page'] ],
			'menu-item-type'      => 'post_type',
			'menu-item-status'    => 'publish',
			'menu-item-position'  => $order++,
		) );
		foreach ( $item['children'] as $child ) {
			wp_update_nav_menu_item( $menu_id, 0, array(
				'menu-item-title'     => $child['title'],
				'menu-item-object'    => 'page',
				'menu-item-object-id' => $ids[ $child['page'] ],
				'menu-item-type'      => 'post_type',
				'menu-item-status'    => 'publish',
				'menu-item-parent-id' => $parent_item,
				'menu-item-position'  => $order++,
			) );
		}
	}
	$locations[ $location ] = $menu_id;
	$state[ $location ]     = array( 'sig' => jb_menu_signature( $menu_id ), 'spec' => $spec_hash );
	jb_sync_log( "MENU $location rebuilt" );
}
set_theme_mod( 'nav_menu_locations', $locations );
update_option( 'jb_menu_state', $state );

/* ------------------------------------------------ launch: IndexNow */
if ( '1' === (string) get_option( 'blog_public' ) && function_exists( 'jb_indexnow_submit' ) && ! get_option( 'jb_indexnow_launch' ) ) {
	$urls = array( home_url( '/' ) );
	foreach ( get_posts( array( 'post_type' => array( 'page', 'post' ), 'post_status' => 'publish', 'numberposts' => 200 ) ) as $item ) {
		$urls[] = get_permalink( $item );
	}
	foreach ( get_categories( array( 'hide_empty' => true ) ) as $cat ) {
		$urls[] = get_category_link( $cat );
	}
	$res = jb_indexnow_submit( array_values( array_unique( $urls ) ), true );
	$code = is_wp_error( $res ) ? $res->get_error_message() : wp_remote_retrieve_response_code( $res );
	jb_sync_log( sprintf( 'IndexNow launch submission: %d URLs, response %s', count( $urls ), $code ) );
	if ( ! is_wp_error( $res ) && in_array( (int) $code, array( 200, 202 ), true ) ) {
		update_option( 'jb_indexnow_launch', gmdate( 'c' ) );
	}
}

jb_sync_log( 'Sync complete.' );
