<?php
defined( 'ABSPATH' ) || exit;
get_header();
while ( have_posts() ) :
	the_post();
	$cats = get_the_category();
	?>
	<article class="article">
		<header class="page-hero article-hero">
			<div class="wrap wrap-narrow">
				<?php jb_breadcrumbs(); ?>
				<?php if ( $cats ) : ?>
					<span class="eyebrow eyebrow-light"><?php echo esc_html( $cats[0]->name ); ?></span>
				<?php endif; ?>
				<h1><?php the_title(); ?></h1>
				<?php if ( has_excerpt() ) : ?>
					<p class="page-hero-lede"><?php echo esc_html( get_the_excerpt() ); ?></p>
				<?php endif; ?>
				<p class="article-meta">
					By <a href="<?php echo esc_url( home_url( '/about-joseph/' ) ); ?>"><?php echo esc_html( jb_opt( 'name' ) ); ?></a>, <?php echo esc_html( jb_opt( 'title' ) ); ?>, NMLS #<?php echo esc_html( jb_opt( 'nmls' ) ); ?>
					· Updated <time datetime="<?php echo esc_attr( get_the_modified_date( 'c' ) ); ?>"><?php echo esc_html( get_the_modified_date() ); ?></time>
				</p>
			</div>
		</header>

		<div class="section section-ivory">
			<div class="wrap wrap-narrow prose">
				<?php if ( has_post_thumbnail() ) : ?>
					<figure class="article-image"><?php the_post_thumbnail( 'jb-wide' ); ?></figure>
				<?php endif; ?>
				<?php the_content(); ?>

				<aside class="author-box" aria-label="About the author">
					<img src="<?php echo jb_img( 'joe-headshot-sm.webp' ); ?>" alt="<?php echo esc_attr( jb_opt( 'name' ) ); ?>" width="96" height="120" loading="lazy">
					<div>
						<p class="author-name"><?php echo esc_html( jb_opt( 'name' ) ); ?></p>
						<p><?php echo esc_html( jb_opt( 'title' ) ); ?> with <?php echo esc_html( jb_opt( 'company' ) ); ?> (NMLS #<?php echo esc_html( jb_opt( 'nmls' ) ); ?>). After 30+ years building and running companies, Joseph helps buyers, business owners and investors structure mortgage financing strategically.</p>
						<a class="text-link" href="<?php echo esc_url( home_url( '/about-joseph/' ) ); ?>">More about Joseph <?php echo jb_icon( 'arrow' ); ?></a>
						<?php if ( jb_opt( 'linkedin' ) ) : ?>
							<a class="text-link" href="<?php echo esc_url( jb_opt( 'linkedin' ) ); ?>" target="_blank" rel="noopener me">LinkedIn <?php echo jb_icon( 'arrow' ); ?></a>
						<?php endif; ?>
					</div>
				</aside>
				<p class="fine-print">This article is for general education and is not a commitment to lend or an offer of credit. Program availability, rates and terms depend on your full financial picture and are subject to change.</p>
			</div>
		</div>
	</article>
	<?php
	jb_cta_band( jb_post_cta() );

	$related = new WP_Query( array(
		'posts_per_page'      => 3,
		'post__not_in'        => array( get_the_ID() ),
		'category__in'        => wp_list_pluck( $cats, 'term_id' ),
		'ignore_sticky_posts' => true,
	) );
	if ( $related->have_posts() ) :
		?>
		<section class="section section-ivory">
			<div class="wrap">
				<h2 class="section-title">Keep Reading</h2>
				<div class="post-grid">
					<?php
					while ( $related->have_posts() ) :
						$related->the_post();
						jb_post_card();
					endwhile;
					wp_reset_postdata();
					?>
				</div>
			</div>
		</section>
		<?php
	endif;
endwhile;
get_footer();
