<?php
/**
 * Insights listing (posts page, categories, search).
 */
defined( 'ABSPATH' ) || exit;
get_header();

$pillars = jb_pillars();
$current = is_category() ? get_queried_object()->slug : '';
if ( is_category() ) {
	$title = single_cat_title( '', false );
	$lede  = category_description() ? wp_strip_all_tags( category_description() ) : 'Straight answers on ' . $title . ', written by Joseph.';
} elseif ( is_search() ) {
	$title = 'Search: ' . get_search_query();
	$lede  = 'Articles matching your question.';
} else {
	$title = 'Mortgage Insights';
	$lede  = 'Straight answers to the questions buyers, business owners, investors and agents ask Joseph every week.';
}
?>
<header class="page-hero">
	<div class="wrap">
		<?php jb_breadcrumbs(); ?>
		<span class="eyebrow eyebrow-light">Insights &amp; Resources</span>
		<h1><?php echo esc_html( $title ); ?></h1>
		<p class="page-hero-lede"><?php echo esc_html( $lede ); ?></p>
		<?php get_search_form(); ?>
	</div>
</header>

<section class="section section-ivory">
	<div class="wrap">
		<nav class="pillar-nav" aria-label="Topics">
			<a href="<?php echo esc_url( get_permalink( get_option( 'page_for_posts' ) ) ?: home_url( '/insights/' ) ); ?>" <?php echo $current ? '' : 'aria-current="page"'; ?>>All</a>
			<?php foreach ( $pillars as $slug => $pillar ) : ?>
				<?php $term = get_category_by_slug( $slug ); ?>
				<?php if ( $term ) : ?>
					<a href="<?php echo esc_url( get_category_link( $term ) ); ?>" <?php echo $current === $slug ? 'aria-current="page"' : ''; ?>><?php echo esc_html( $pillar['name'] ); ?></a>
				<?php endif; ?>
			<?php endforeach; ?>
		</nav>

		<?php if ( have_posts() ) : ?>
			<div class="post-grid">
				<?php
				while ( have_posts() ) :
					the_post();
					jb_post_card( 'h2' );
				endwhile;
				?>
			</div>
			<?php the_posts_pagination( array( 'mid_size' => 1 ) ); ?>
		<?php else : ?>
			<div class="empty-state">
				<h2>New articles are on the way.</h2>
				<p>In the meantime, the fastest answer to your question is a quick conversation with Joseph.</p>
				<a class="btn btn-gold" href="<?php echo esc_url( home_url( '/contact/' ) ); ?>">Ask Joseph About Your Scenario</a>
			</div>
		<?php endif; ?>
	</div>
</section>
<?php
jb_cta_band( $current && isset( $pillars[ $current ] ) ? $pillars[ $current ]['cta'] : $pillars['home-buying']['cta'] );
get_footer();
