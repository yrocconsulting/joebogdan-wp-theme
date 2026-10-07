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

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'jb-fonts', JB_URI . '/assets/css/fonts.css', array(), JB_VERSION );
	wp_enqueue_style( 'jb-main', JB_URI . '/assets/css/main.css', array( 'jb-fonts' ), JB_VERSION );
	wp_enqueue_script( 'jb-main', JB_URI . '/assets/js/main.js', array(), JB_VERSION, array( 'strategy' => 'defer', 'in_footer' => true ) );
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
