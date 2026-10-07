<?php
defined( 'ABSPATH' ) || exit;
get_header();
while ( have_posts() ) :
	the_post();
	?>
	<header class="page-hero">
		<div class="wrap">
			<?php jb_breadcrumbs(); ?>
			<h1><?php the_title(); ?></h1>
			<?php if ( has_excerpt() ) : ?>
				<p class="page-hero-lede"><?php echo esc_html( get_the_excerpt() ); ?></p>
			<?php endif; ?>
		</div>
	</header>
	<div class="section section-ivory">
		<div class="wrap prose">
			<?php the_content(); ?>
		</div>
	</div>
	<?php
endwhile;
get_footer();
