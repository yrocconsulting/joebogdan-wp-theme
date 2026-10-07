<?php
/**
 * Template Name: Landing (full width)
 * Template Post Type: page
 *
 * For conversion pages whose content supplies its own hero and sections.
 */
defined( 'ABSPATH' ) || exit;
get_header();
while ( have_posts() ) :
	the_post();
	?>
	<div class="landing-content">
		<?php the_content(); ?>
	</div>
	<?php
endwhile;
get_footer();
