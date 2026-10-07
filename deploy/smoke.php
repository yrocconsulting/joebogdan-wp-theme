<?php
/**
 * Post-deploy checks, run on the server: wp eval-file ../jb-sync/deploy/smoke.php
 */

if ( ! defined( 'WP_CLI' ) ) {
	exit( 1 );
}

$manifest = json_decode( file_get_contents( dirname( __DIR__ ) . '/content/manifest.json' ), true );
$problems = array();

if ( 'joe-bogdan-mlo' !== get_stylesheet() ) {
	$problems[] = 'Theme joe-bogdan-mlo is not active (active: ' . get_stylesheet() . ')';
}
foreach ( $manifest['pages'] as $spec ) {
	$path = $spec['parent'] ? $spec['parent'] . '/' . $spec['slug'] : $spec['slug'];
	$page = get_page_by_path( $path );
	if ( ! $page || 'publish' !== $page->post_status ) {
		$problems[] = "Page missing or unpublished: $path";
	}
}
if ( ! (int) get_option( 'page_on_front' ) ) {
	$problems[] = 'No static front page set';
}
foreach ( array( 'primary', 'footer', 'legal' ) as $location ) {
	if ( ! has_nav_menu( $location ) ) {
		$problems[] = "No menu assigned to $location";
	}
}

if ( $problems ) {
	WP_CLI::error( implode( "\n", $problems ) );
}
WP_CLI::success( sprintf( 'Theme active, %d pages published, menus assigned.', count( $manifest['pages'] ) ) );
