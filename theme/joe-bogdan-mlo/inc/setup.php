<?php
/**
 * Theme supports, menus, assets and front-end hygiene.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'after_setup_theme', function () {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'responsive-embeds' );
	add_theme_support( 'align-wide' );
	add_theme_support( 'editor-styles' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script', 'navigation-widgets' ) );
	add_theme_support( 'custom-logo', array( 'height' => 88, 'width' => 88, 'flex-width' => true ) );
	remove_theme_support( 'core-block-patterns' );

	add_editor_style( array( 'assets/css/fonts.css', 'assets/css/main.css' ) );

	register_nav_menus( array(
		'primary' => 'Primary navigation',
		'footer'  => 'Footer navigation',
		'legal'   => 'Footer legal links',
	) );

	add_image_size( 'jb-card', 720, 480, true );
	add_image_size( 'jb-wide', 1600, 900, true );
} );

/** Cache-busting version that changes whenever the file is deployed. */
function jb_asset_version( $path ) {
	$file = JB_DIR . '/' . $path;
	return file_exists( $file ) ? (string) filemtime( $file ) : JB_VERSION;
}

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'jb-fonts', JB_URI . '/assets/css/fonts.css', array(), jb_asset_version( 'assets/css/fonts.css' ) );
	wp_enqueue_style( 'jb-main', JB_URI . '/assets/css/main.css', array( 'jb-fonts' ), jb_asset_version( 'assets/css/main.css' ) );
	wp_enqueue_script( 'jb-main', JB_URI . '/assets/js/main.js', array(), jb_asset_version( 'assets/js/main.js' ), array( 'strategy' => 'defer', 'in_footer' => true ) );
	wp_localize_script( 'jb-main', 'JB', array(
		'leadEndpoint' => esc_url_raw( rest_url( 'jb/v1/lead' ) ),
		'rate'         => (float) jb_opt( 'rate_estimate' ),
		'taxIns'       => (float) jb_opt( 'tax_ins_pct' ),
	) );
} );

// Preload the two fonts used above the fold.
add_action( 'wp_head', function () {
	foreach ( array( 'fraunces-latin-opsz-normal.woff2', 'inter-latin-wght-normal.woff2' ) as $font ) {
		printf( '<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n", esc_url( JB_URI . '/assets/fonts/' . $font ) );
	}
}, 1 );

// Front-end hygiene.
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'wp_head', 'wp_generator' );
remove_action( 'wp_head', 'wlwmanifest_link' );
remove_action( 'wp_head', 'rsd_link' );

// Insights are articles, not discussion threads.
add_filter( 'comments_open', '__return_false' );
add_filter( 'pings_open', '__return_false' );

add_filter( 'excerpt_length', function () {
	return 28;
} );
add_filter( 'excerpt_more', function () {
	return '…';
} );

add_filter( 'body_class', function ( $classes ) {
	if ( is_page() ) {
		$classes[] = 'page-' . get_post_field( 'post_name', get_queried_object_id() );
	}
	return $classes;
} );

/**
 * Favicons. A Site Icon chosen in Appearance → Customize → Site Identity
 * takes over automatically; until then the theme's JB icons are used.
 */
function jb_icon_url( $file ) {
	return esc_url( JB_URI . '/assets/icons/' . $file );
}

add_action( 'wp_head', function () {
	if ( has_site_icon() ) {
		return;
	}
	printf( '<link rel="icon" href="%s" sizes="48x48">' . "\n", jb_icon_url( 'favicon.ico' ) );
	printf( '<link rel="icon" type="image/png" sizes="32x32" href="%s">' . "\n", jb_icon_url( 'favicon-32.png' ) );
	printf( '<link rel="icon" type="image/png" sizes="192x192" href="%s">' . "\n", jb_icon_url( 'icon-192.png' ) );
	printf( '<link rel="apple-touch-icon" href="%s">' . "\n", jb_icon_url( 'apple-touch-icon.png' ) );
	printf( '<link rel="manifest" href="%s">' . "\n", jb_icon_url( 'site.webmanifest' ) );
}, 3 );
add_action( 'admin_head', function () {
	if ( ! has_site_icon() ) {
		printf( '<link rel="icon" href="%s">' . "\n", jb_icon_url( 'favicon.ico' ) );
	}
} );

// Browsers request /favicon.ico directly; serve the JB icon instead of WordPress's default.
add_action( 'do_faviconico', function () {
	if ( has_site_icon() ) {
		return;
	}
	wp_safe_redirect( JB_URI . '/assets/icons/favicon.ico', 301 );
	exit;
}, 5 );

/**
 * Google Tag Manager (Appearance → Joseph Bogdan Settings). Only runs when the
 * site is visible to search engines, so staging visits stay out of the stats.
 * Lead forms push a `generate_lead` event (with form_type) to the dataLayer.
 */
function jb_gtm_id() {
	$id = jb_opt( 'gtm_id' );
	return ( preg_match( '/^GTM-[A-Z0-9]+$/', $id ) && '1' === (string) get_option( 'blog_public' ) ) ? $id : '';
}

add_action( 'wp_head', function () {
	$id = jb_gtm_id();
	if ( ! $id ) {
		return;
	}
	?>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','<?php echo esc_js( $id ); ?>');</script>
<!-- End Google Tag Manager -->
	<?php
}, 1 );

add_action( 'wp_body_open', function () {
	$id = jb_gtm_id();
	if ( $id ) {
		printf( '<!-- Google Tag Manager (noscript) --><noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%s" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>' . "\n", esc_attr( $id ) );
	}
}, 1 );

// Google Search Console ownership verification.
add_action( 'wp_head', function () {
	$code = preg_replace( '/[^A-Za-z0-9_-]/', '', jb_opt( 'gsc_verification' ) );
	if ( $code ) {
		printf( '<meta name="google-site-verification" content="%s" />' . "\n", esc_attr( $code ) );
	}
}, 1 );
