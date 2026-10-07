<?php
/**
 * Homepage: renders the page assigned as the static front page.
 * Sections are built from blocks/shortcodes so copy stays editable in WordPress.
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
