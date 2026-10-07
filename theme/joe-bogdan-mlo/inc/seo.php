<?php
/**
 * Search and AI-search signals: titles, meta descriptions, Open Graph,
 * a connected JSON-LD entity graph, and /llms.txt.
 *
 * If a dedicated SEO plugin is activated later, the meta/OG output steps
 * aside automatically; the entity graph and llms.txt stay.
 */

defined( 'ABSPATH' ) || exit;

function jb_seo_plugin_active() {
	return defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'AIOSEO_VERSION' ) || defined( 'SEOPRESS_VERSION' );
}

/* ---------------------------------------------------------------------------
 * Per-page SEO fields (title + description), editable in the sidebar.
 * ------------------------------------------------------------------------ */

add_action( 'init', function () {
	foreach ( array( 'page', 'post' ) as $type ) {
		foreach ( array( '_jb_seo_title', '_jb_seo_description', '_jb_service' ) as $key ) {
			register_post_meta( $type, $key, array(
				'type'          => 'string',
				'single'        => true,
				'show_in_rest'  => true,
				'auth_callback' => function () {
					return current_user_can( 'edit_posts' );
				},
			) );
		}
	}
} );

add_action( 'add_meta_boxes', function () {
	foreach ( array( 'page', 'post' ) as $type ) {
		add_meta_box( 'jb-seo', 'Search & AI Snippet', 'jb_seo_metabox', $type, 'side', 'default' );
	}
} );

function jb_seo_metabox( $post ) {
	wp_nonce_field( 'jb_seo', 'jb_seo_nonce' );
	$title = get_post_meta( $post->ID, '_jb_seo_title', true );
	$desc  = get_post_meta( $post->ID, '_jb_seo_description', true );
	?>
	<p><label for="jb-seo-title"><strong>Search title</strong></label><br>
	<input type="text" id="jb-seo-title" name="jb_seo_title" value="<?php echo esc_attr( $title ); ?>" style="width:100%" placeholder="Defaults to the page title"></p>
	<p><label for="jb-seo-desc"><strong>Meta description</strong></label><br>
	<textarea id="jb-seo-desc" name="jb_seo_description" rows="4" style="width:100%" placeholder="One or two sentences that directly answer what this page helps with."><?php echo esc_textarea( $desc ); ?></textarea></p>
	<p class="description">Aim for 140–160 characters. Lead with the visitor’s problem.</p>
	<?php
}

add_action( 'save_post', function ( $post_id ) {
	if ( ! isset( $_POST['jb_seo_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['jb_seo_nonce'] ), 'jb_seo' ) ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	update_post_meta( $post_id, '_jb_seo_title', sanitize_text_field( wp_unslash( $_POST['jb_seo_title'] ?? '' ) ) );
	update_post_meta( $post_id, '_jb_seo_description', sanitize_textarea_field( wp_unslash( $_POST['jb_seo_description'] ?? '' ) ) );
} );

/* ---------------------------------------------------------------------------
 * Title + description
 * ------------------------------------------------------------------------ */

add_filter( 'document_title_parts', function ( $parts ) {
	if ( jb_seo_plugin_active() ) {
		return $parts;
	}
	if ( is_singular() ) {
		$custom = get_post_meta( get_queried_object_id(), '_jb_seo_title', true );
		if ( $custom ) {
			return array( 'title' => $custom );
		}
	}
	if ( is_front_page() ) {
		return array( 'title' => sprintf( '%s | Mortgage Loan Originator in Flower Mound & North Texas', jb_opt( 'name' ) ) );
	}
	$parts['site'] = jb_opt( 'name' ) . ', ' . jb_opt( 'title' );
	unset( $parts['tagline'] );
	return $parts;
} );

add_filter( 'document_title_separator', function () {
	return '|';
} );

function jb_meta_description() {
	if ( is_singular() ) {
		$id   = get_queried_object_id();
		$desc = get_post_meta( $id, '_jb_seo_description', true );
		if ( ! $desc && has_excerpt( $id ) ) {
			$desc = get_the_excerpt( $id );
		}
		if ( ! $desc ) {
			$desc = wp_trim_words( wp_strip_all_tags( strip_shortcodes( get_post_field( 'post_content', $id ) ) ), 30, '…' );
		}
		return $desc;
	}
	if ( is_category() && category_description() ) {
		return wp_strip_all_tags( category_description() );
	}
	return sprintf( '%s is a %s with %s (NMLS #%s) helping North Texas home buyers, business owners, investors and luxury buyers finance strategically.', jb_opt( 'name' ), jb_opt( 'title' ), jb_opt( 'company' ), jb_opt( 'nmls' ) );
}

add_action( 'wp_head', function () {
	if ( jb_seo_plugin_active() ) {
		return;
	}
	$desc  = trim( preg_replace( '/\s+/', ' ', jb_meta_description() ) );
	$title = wp_get_document_title();
	$url   = is_singular() ? get_permalink() : home_url( add_query_arg( array(), $GLOBALS['wp']->request ?? '' ) );
	$image = is_singular() && has_post_thumbnail() ? get_the_post_thumbnail_url( null, 'jb-wide' ) : jb_img( 'joe-headshot.webp' );

	printf( '<meta name="description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta property="og:type" content="%s">' . "\n", is_singular( 'post' ) ? 'article' : 'website' );
	printf( '<meta property="og:site_name" content="%s">' . "\n", esc_attr( jb_opt( 'name' ) . ', ' . jb_opt( 'title' ) ) );
	printf( '<meta property="og:title" content="%s">' . "\n", esc_attr( $title ) );
	printf( '<meta property="og:description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta property="og:url" content="%s">' . "\n", esc_url( $url ) );
	printf( '<meta property="og:image" content="%s">' . "\n", esc_url( $image ) );
	echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
}, 2 );

// Thin pages stay out of the index.
add_filter( 'wp_robots', function ( $robots ) {
	if ( is_search() || is_404() || is_singular( 'jb_lead' ) ) {
		$robots['noindex'] = true;
		$robots['follow']  = true;
	}
	return $robots;
} );

/* ---------------------------------------------------------------------------
 * JSON-LD entity graph (printed in the footer so FAQ items rendered by the
 * page content can be included).
 * ------------------------------------------------------------------------ */

function jb_schema_ids() {
	$home = trailingslashit( home_url() );
	return array(
		'site'     => $home . '#website',
		'person'   => $home . '#joe-bogdan',
		'practice' => $home . '#mortgage-practice',
		'lender'   => $home . '#crosscountry-mortgage',
	);
}

function jb_schema_graph() {
	$ids   = jb_schema_ids();
	$nmls  = jb_opt( 'nmls' );
	$areas = array_map( function ( $city ) {
		return array( '@type' => 'City', 'name' => trim( $city ) . ', TX' );
	}, array_filter( explode( ',', jb_opt( 'service_area' ) ) ) );
	$areas[] = array( '@type' => 'State', 'name' => 'Texas' );

	$same_as = array_values( array_filter( array(
		'https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/' . rawurlencode( $nmls ),
		jb_opt( 'linkedin' ),
		jb_opt( 'facebook' ),
		jb_opt( 'instagram' ),
		jb_opt( 'google' ),
		jb_opt( 'ccm_url' ),
	) ) );

	$address = array(
		'@type'           => 'PostalAddress',
		'streetAddress'   => jb_opt( 'street' ),
		'addressLocality' => jb_opt( 'city' ),
		'addressRegion'   => jb_opt( 'region' ),
		'postalCode'      => jb_opt( 'postal' ),
		'addressCountry'  => 'US',
	);

	$knows = array( 'Mortgage pre-approval', 'Home purchase financing', 'Mortgage refinancing', 'Home equity', 'Jumbo loans', 'Luxury home financing', 'Self-employed mortgages', 'Bank statement loans', 'Investment property loans', 'DSCR loans', 'New construction financing', 'FHA loans', 'VA loans', 'Conventional loans', 'Non-QM loans', 'Adjustable-rate mortgages', 'Down payment assistance', 'First-time homebuyers' );

	$graph = array(
		array(
			'@type'       => 'WebSite',
			'@id'         => $ids['site'],
			'url'         => home_url( '/' ),
			'name'        => jb_opt( 'name' ) . ', ' . jb_opt( 'title' ),
			'publisher'   => array( '@id' => $ids['person'] ),
			'inLanguage'  => 'en-US',
		),
		array(
			'@type'       => 'Organization',
			'@id'         => $ids['lender'],
			'name'        => jb_opt( 'company' ),
			'url'         => jb_opt( 'company_url' ),
			'description' => jb_opt( 'company_license' ) . '.',
			'identifier'  => array( '@type' => 'PropertyValue', 'propertyID' => 'NMLS', 'value' => jb_opt( 'company_nmls' ) ),
		),
		array(
			'@type'            => 'Person',
			'@id'              => $ids['person'],
			'name'             => jb_opt( 'name' ),
			'alternateName'    => jb_opt( 'legal_name' ),
			'jobTitle'         => jb_opt( 'title' ),
			'description'      => sprintf( '%s is a %s with %s (NMLS #%s). Before mortgage lending he spent more than 30 years as a business owner and CEO. He specializes in purchase, jumbo, self-employed and investment-property financing and partners with Realtors and builders across North Texas.', jb_opt( 'name' ), jb_opt( 'title' ), jb_opt( 'company' ), $nmls ),
			'url'              => home_url( '/about-joe/' ),
			'image'            => jb_img( 'joe-headshot.webp' ),
			'telephone'        => jb_opt( 'phone' ),
			'email'            => jb_opt( 'email' ),
			'worksFor'         => array( '@id' => $ids['lender'] ),
			'workLocation'     => array( '@id' => $ids['practice'] ),
			'identifier'       => array( '@type' => 'PropertyValue', 'propertyID' => 'NMLS', 'value' => $nmls ),
			'hasCredential'    => array(
				'@type'              => 'EducationalOccupationalCredential',
				'credentialCategory' => 'license',
				'name'               => 'Texas Residential Mortgage Loan Originator License (NMLS #' . $nmls . ')',
				'recognizedBy'       => array( '@type' => 'GovernmentOrganization', 'name' => 'Texas Department of Savings and Mortgage Lending', 'url' => 'https://www.sml.texas.gov/' ),
			),
			'knowsAbout'       => $knows,
			'areaServed'       => $areas,
			'sameAs'           => $same_as,
		),
		array(
			'@type'              => array( 'FinancialService', 'LocalBusiness' ),
			'@id'                => $ids['practice'],
			'name'               => jb_opt( 'name' ) . ' — ' . jb_opt( 'title' ) . ', ' . jb_opt( 'company' ),
			'url'                => home_url( '/' ),
			'image'              => jb_img( 'joe-headshot.webp' ),
			'telephone'          => jb_opt( 'phone' ),
			'email'              => jb_opt( 'email' ),
			'address'            => $address,
			'areaServed'         => $areas,
			'employee'           => array( '@id' => $ids['person'] ),
			'parentOrganization' => array( '@id' => $ids['lender'] ),
			'knowsAbout'         => $knows,
		),
	);

	// The current page.
	$crumbs = jb_breadcrumb_items();
	$page   = array(
		'@type'      => is_singular( 'post' ) ? 'WebPage' : ( is_page( array( 'about-joe' ) ) ? 'ProfilePage' : ( is_page( 'contact' ) ? 'ContactPage' : 'WebPage' ) ),
		'@id'        => ( is_singular() ? get_permalink() : home_url( '/' ) ) . '#webpage',
		'url'        => is_singular() ? get_permalink() : home_url( '/' ),
		'name'       => wp_get_document_title(),
		'description'=> jb_meta_description(),
		'isPartOf'   => array( '@id' => $ids['site'] ),
		'about'      => array( '@id' => is_page( 'about-joe' ) ? $ids['person'] : $ids['practice'] ),
		'inLanguage' => 'en-US',
	);
	if ( is_page( 'about-joe' ) ) {
		$page['mainEntity'] = array( '@id' => $ids['person'] );
	}
	if ( is_singular() ) {
		$page['dateModified'] = get_the_modified_date( 'c' );
	}
	if ( count( $crumbs ) > 1 ) {
		$page['breadcrumb'] = array(
			'@type'           => 'BreadcrumbList',
			'itemListElement' => array_map( function ( $item, $i ) {
				return array( '@type' => 'ListItem', 'position' => $i + 1, 'name' => $item['name'], 'item' => $item['url'] );
			}, $crumbs, array_keys( $crumbs ) ),
		);
	}
	$graph[] = $page;

	if ( is_singular( 'post' ) ) {
		$graph[] = array(
			'@type'            => 'Article',
			'@id'              => get_permalink() . '#article',
			'headline'         => get_the_title(),
			'description'      => jb_meta_description(),
			'datePublished'    => get_the_date( 'c' ),
			'dateModified'     => get_the_modified_date( 'c' ),
			'author'           => array( '@id' => $ids['person'] ),
			'publisher'        => array( '@id' => $ids['person'] ),
			'mainEntityOfPage' => array( '@id' => get_permalink() . '#webpage' ),
			'image'            => has_post_thumbnail() ? get_the_post_thumbnail_url( null, 'jb-wide' ) : jb_img( 'joe-headshot.webp' ),
			'articleSection'   => wp_list_pluck( get_the_category(), 'name' ),
		);
	}

	$service = is_page() ? get_post_meta( get_queried_object_id(), '_jb_service', true ) : '';
	if ( $service ) {
		$graph[] = array(
			'@type'       => 'Service',
			'@id'         => get_permalink() . '#service',
			'name'        => $service,
			'serviceType' => 'Mortgage lending',
			'description' => jb_meta_description(),
			'provider'    => array( '@id' => $ids['person'] ),
			'areaServed'  => $areas,
			'url'         => get_permalink(),
		);
	}

	if ( ! empty( $GLOBALS['jb_faq_items'] ) ) {
		$graph[] = array(
			'@type'      => 'FAQPage',
			'@id'        => ( is_singular() ? get_permalink() : home_url( '/' ) ) . '#faq',
			'mainEntity' => array_map( function ( $item ) {
				return array(
					'@type'          => 'Question',
					'name'           => $item['q'],
					'acceptedAnswer' => array( '@type' => 'Answer', 'text' => trim( preg_replace( '/\s+/', ' ', $item['a'] ) ) ),
				);
			}, $GLOBALS['jb_faq_items'] ),
		);
	}

	return array( '@context' => 'https://schema.org', '@graph' => $graph );
}

add_action( 'wp_footer', function () {
	if ( is_404() || is_search() ) {
		return;
	}
	echo '<script type="application/ld+json">' . wp_json_encode( jb_schema_graph(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}, 5 );

/* ---------------------------------------------------------------------------
 * /llms.txt — a plain-language map of the site for AI assistants.
 * ------------------------------------------------------------------------ */

add_action( 'init', function () {
	add_rewrite_rule( '^llms\.txt$', 'index.php?jb_llms=1', 'top' );
} );

add_filter( 'query_vars', function ( $vars ) {
	$vars[] = 'jb_llms';
	return $vars;
} );

add_filter( 'redirect_canonical', function ( $redirect ) {
	return get_query_var( 'jb_llms' ) ? false : $redirect;
} );

add_action( 'template_redirect', function () {
	if ( ! get_query_var( 'jb_llms' ) ) {
		return;
	}
	header( 'Content-Type: text/plain; charset=utf-8' );
	header( 'X-Robots-Tag: noindex' );

	$line = function ( $page ) {
		$desc = get_post_meta( $page->ID, '_jb_seo_description', true );
		return sprintf( '- [%s](%s)%s', $page->post_title, get_permalink( $page ), $desc ? ': ' . $desc : '' );
	};

	$out   = array();
	$out[] = '# ' . jb_opt( 'name' ) . ', ' . jb_opt( 'title' );
	$out[] = '';
	$out[] = sprintf( '> %s is a %s with %s (individual NMLS #%s; company NMLS #%s), based in %s, %s and serving North Texas. %s; %s. He helps home buyers, self-employed borrowers and business owners, real estate investors and luxury/jumbo buyers structure mortgage financing, and partners with Realtors and home builders. He is a mortgage loan originator only and does not provide real estate brokerage services.', jb_opt( 'name' ), jb_opt( 'title' ), jb_opt( 'company' ), jb_opt( 'nmls' ), jb_opt( 'company_nmls' ), jb_opt( 'city' ), jb_opt( 'region' ), jb_opt( 'licensing' ), jb_opt( 'company_license' ) );
	$out[] = '';
	$out[] = sprintf( 'Contact: call %s · text %s · %s · %s, %s, %s %s', jb_opt( 'phone' ), jb_opt( 'sms' ), jb_opt( 'email' ), jb_opt( 'street' ), jb_opt( 'city' ), jb_opt( 'region' ), jb_opt( 'postal' ) );
	$out[] = sprintf( 'Verify license: https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/%s', jb_opt( 'nmls' ) );
	$out[] = '';

	$pages = get_pages( array( 'sort_column' => 'menu_order,post_title' ) );
	$legal = array( 'privacy-policy', 'terms-of-use', 'sms-terms', 'accessibility', 'licensing-disclosures', 'texas-consumer-notice' );
	$out[] = '## Pages';
	foreach ( $pages as $page ) {
		if ( ! in_array( $page->post_name, $legal, true ) ) {
			$out[] = $line( $page );
		}
	}

	$posts = get_posts( array( 'numberposts' => 50 ) );
	if ( $posts ) {
		$out[] = '';
		$out[] = '## Insights';
		foreach ( $posts as $post ) {
			$out[] = sprintf( '- [%s](%s): %s', $post->post_title, get_permalink( $post ), wp_strip_all_tags( get_the_excerpt( $post ) ) );
		}
	}

	$out[] = '';
	$out[] = '## Optional';
	foreach ( $pages as $page ) {
		if ( in_array( $page->post_name, $legal, true ) ) {
			$out[] = $line( $page );
		}
	}

	echo implode( "\n", $out ) . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput
	exit;
} );

// Keep usernames out of the public sitemap.
add_filter( 'wp_sitemaps_add_provider', function ( $provider, $name ) {
	return 'users' === $name ? false : $provider;
}, 10, 2 );
