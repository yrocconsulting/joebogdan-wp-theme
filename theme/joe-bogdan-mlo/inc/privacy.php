<?php
/**
 * Keep WordPress account names private: no author archives, no public user
 * listing in the REST API, and no usernames in oEmbed data. Articles are
 * presented as written by Joseph (see the author box and Article schema).
 */

defined( 'ABSPATH' ) || exit;

// /author/... and ?author=N go to the About page instead of an archive.
add_action( 'template_redirect', function () {
	if ( is_author() || isset( $_GET['author'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification
		wp_safe_redirect( home_url( '/about-joseph/' ), 301 );
		exit;
	}
}, 1 );

// Author archive links point to the About page too.
add_filter( 'author_link', function () {
	return home_url( '/about-joseph/' );
} );

// Hide the users endpoints from anyone not logged in (the editor still works).
add_filter( 'rest_endpoints', function ( $endpoints ) {
	if ( is_user_logged_in() ) {
		return $endpoints;
	}
	foreach ( array_keys( $endpoints ) as $route ) {
		if ( 0 === strpos( $route, '/wp/v2/users' ) ) {
			unset( $endpoints[ $route ] );
		}
	}
	return $endpoints;
} );

// oEmbed responses name Joseph, not the WordPress account.
add_filter( 'oembed_response_data', function ( $data ) {
	$data['author_name'] = jb_opt( 'name' );
	$data['author_url']  = home_url( '/about-joseph/' );
	return $data;
} );

// The About page moved from /about-joe/ to /about-joseph/.
add_action( 'template_redirect', function () {
	if ( is_404() && preg_match( '#^/about-joe/?$#', wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH ) ) ) {
		wp_safe_redirect( home_url( '/about-joseph/' ), 301 );
		exit;
	}
} );

// /apply/ forwards to Joseph's CrossCountry online application (set in settings).
add_action( 'init', function () {
	add_rewrite_rule( '^apply/?$', 'index.php?jb_apply=1', 'top' );
} );
add_filter( 'query_vars', function ( $vars ) {
	$vars[] = 'jb_apply';
	return $vars;
} );
add_action( 'template_redirect', function () {
	if ( get_query_var( 'jb_apply' ) ) {
		header( 'X-Robots-Tag: noindex' );
		wp_redirect( esc_url_raw( jb_opt( 'apply_url' ) ), 302 ); // phpcs:ignore WordPress.Security.SafeRedirect
		exit;
	}
}, 0 );
