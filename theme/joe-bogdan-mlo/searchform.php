<?php defined( 'ABSPATH' ) || exit; ?>
<?php $jb_search_id = 's-' . wp_unique_id(); ?>
<form role="search" method="get" class="search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
	<label class="screen-reader-text" for="<?php echo esc_attr( $jb_search_id ); ?>">Search insights</label>
	<input type="search" id="<?php echo esc_attr( $jb_search_id ); ?>" name="s" value="<?php echo esc_attr( get_search_query() ); ?>" placeholder="Search a mortgage question…">
	<button type="submit" class="btn btn-gold">Search</button>
</form>
