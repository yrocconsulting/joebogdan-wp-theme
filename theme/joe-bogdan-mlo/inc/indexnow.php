<?php
/**
 * IndexNow: tell Bing (which feeds ChatGPT Search and Copilot), Yandex and
 * other participating engines the moment a page or post is published or
 * updated. Only runs when the site is visible to search engines, so
 * staging never pings.
 */

defined( 'ABSPATH' ) || exit;

function jb_indexnow_key() {
	$key = get_option( 'jb_indexnow_key' );
	if ( ! $key ) {
		$key = strtolower( wp_generate_password( 32, false, false ) );
		update_option( 'jb_indexnow_key', $key, true );
	}
	return $key;
}

// Serve the verification file at /{key}.txt.
add_action( 'init', function () {
	add_rewrite_rule( '^([A-Za-z0-9]{32})\.txt$', 'index.php?jb_indexnow=$matches[1]', 'top' );
} );

add_filter( 'query_vars', function ( $vars ) {
	$vars[] = 'jb_indexnow';
	return $vars;
} );

add_action( 'template_redirect', function () {
	$requested = get_query_var( 'jb_indexnow' );
	if ( ! $requested ) {
		return;
	}
	if ( ! hash_equals( jb_indexnow_key(), $requested ) ) {
		status_header( 404 );
		exit;
	}
	header( 'Content-Type: text/plain; charset=utf-8' );
	echo esc_html( $requested );
	exit;
}, 0 );

add_filter( 'redirect_canonical', function ( $redirect ) {
	return get_query_var( 'jb_indexnow' ) ? false : $redirect;
} );

/**
 * Submit URLs (non-blocking). Repeat pings for the same URL within ten
 * minutes are skipped.
 */
function jb_indexnow_submit( array $urls ) {
	if ( '1' !== (string) get_option( 'blog_public' ) || wp_installing() ) {
		return;
	}
	$urls = array_values( array_filter( array_unique( $urls ), function ( $url ) {
		$key = 'jb_inx_' . md5( $url );
		if ( get_transient( $key ) ) {
			return false;
		}
		set_transient( $key, 1, 10 * MINUTE_IN_SECONDS );
		return true;
	} ) );
	if ( ! $urls ) {
		return;
	}
	$key = jb_indexnow_key();
	wp_remote_post( 'https://api.indexnow.org/indexnow', array(
		'blocking' => false,
		'timeout'  => 3,
		'headers'  => array( 'Content-Type' => 'application/json; charset=utf-8' ),
		'body'     => wp_json_encode( array(
			'host'        => wp_parse_url( home_url(), PHP_URL_HOST ),
			'key'         => $key,
			'keyLocation' => home_url( '/' . $key . '.txt' ),
			'urlList'     => $urls,
		) ),
	) );
}

add_action( 'transition_post_status', function ( $new, $old, $post ) {
	if ( ! in_array( $post->post_type, array( 'post', 'page' ), true ) ) {
		return;
	}
	if ( 'publish' === $new || 'publish' === $old ) {
		$urls = array( get_permalink( $post ) );
		if ( 'post' === $post->post_type ) {
			$urls[] = get_permalink( get_option( 'page_for_posts' ) );
		}
		jb_indexnow_submit( array_filter( $urls ) );
	}
}, 10, 3 );
