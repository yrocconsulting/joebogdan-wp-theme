<?php defined( 'ABSPATH' ) || exit; ?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#132238">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="skip-link" href="#main">Skip to content</a>

<div class="utility-bar">
	<div class="wrap utility-inner">
		<p class="utility-tagline"><?php echo esc_html( jb_opt( 'title' ) ); ?> · <?php echo esc_html( jb_opt( 'company' ) ); ?> · NMLS #<?php echo esc_html( jb_opt( 'nmls' ) ); ?></p>
		<p class="utility-contact">
			<a href="tel:<?php echo esc_attr( jb_tel() ); ?>"><?php echo jb_icon( 'phone' ); ?><span>Call <?php echo esc_html( jb_opt( 'phone' ) ); ?></span></a>
			<a href="sms:<?php echo esc_attr( jb_tel( 'sms' ) ); ?>"><?php echo jb_icon( 'message' ); ?><span>Text Joe</span></a>
		</p>
	</div>
</div>

<header class="site-header" id="site-header">
	<div class="wrap header-inner">
		<a class="logo" href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home">
			<?php if ( has_custom_logo() ) : ?>
				<?php echo wp_get_attachment_image( get_theme_mod( 'custom_logo' ), 'full', false, array( 'class' => 'logo-img', 'alt' => '' ) ); ?>
			<?php else : ?>
				<span class="logo-mark" aria-hidden="true">JB</span>
			<?php endif; ?>
			<span class="logo-text"><?php echo esc_html( jb_opt( 'name' ) ); ?><small>Mortgage Loan Originator</small></span>
		</a>

		<nav class="primary-nav" id="primary-nav" aria-label="Primary">
			<?php
			wp_nav_menu( array(
				'theme_location' => 'primary',
				'container'      => false,
				'menu_id'        => 'primary-menu',
				'fallback_cb'    => 'jb_fallback_menu',
				'depth'          => 2,
			) );
			?>
			<div class="nav-mobile-actions">
				<a class="btn btn-gold btn-block" href="<?php echo jb_preapproval_url(); ?>">Get Pre-Approved</a>
				<a class="btn btn-outline btn-block" href="tel:<?php echo esc_attr( jb_tel() ); ?>"><?php echo jb_icon( 'phone' ); ?> Call <?php echo esc_html( jb_opt( 'phone' ) ); ?></a>
			</div>
		</nav>

		<a class="btn btn-gold header-cta" href="<?php echo jb_preapproval_url(); ?>">Get Pre-Approved</a>
		<button class="nav-toggle" aria-controls="primary-nav" aria-expanded="false">
			<span class="nav-toggle-open"><?php echo jb_icon( 'menu' ); ?></span>
			<span class="nav-toggle-close"><?php echo jb_icon( 'close' ); ?></span>
			<span class="screen-reader-text">Menu</span>
		</button>
	</div>
</header>

<main id="main" class="site-main" tabindex="-1">
