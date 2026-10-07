<?php
defined( 'ABSPATH' ) || exit;
get_header();
?>
<header class="page-hero">
	<div class="wrap">
		<h1>That page has moved.</h1>
		<p class="page-hero-lede">The page you were looking for isn’t here, but the answer to your mortgage question probably is.</p>
		<div class="btn-row">
			<a class="btn btn-gold" href="<?php echo jb_preapproval_url(); ?>">Discover Your Buying Power</a>
			<a class="btn btn-outline" href="<?php echo esc_url( home_url( '/loan-programs/' ) ); ?>">Find Your Scenario</a>
		</div>
	</div>
</header>
<?php
get_footer();
