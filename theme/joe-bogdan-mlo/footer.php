<?php defined( 'ABSPATH' ) || exit; ?>
</main>

<footer class="site-footer">
	<div class="wrap footer-grid">
		<div class="footer-brand">
			<a class="logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<span class="logo-mark" aria-hidden="true">JB</span>
				<span class="logo-text"><?php echo esc_html( jb_opt( 'name' ) ); ?><small><?php echo esc_html( jb_opt( 'title' ) ); ?></small></span>
			</a>
			<p>Strategic mortgage financing for home buyers, business owners, investors and luxury buyers — and a responsive lending partner for the Realtors and builders who serve them.</p>
			<a class="btn btn-gold" href="<?php echo jb_preapproval_url(); ?>">Discover Your Buying Power</a>
		</div>

		<div class="footer-col">
			<h2 class="footer-heading">Navigate</h2>
			<?php
			wp_nav_menu( array(
				'theme_location' => 'footer',
				'container'      => false,
				'depth'          => 1,
				'fallback_cb'    => function () {
					echo '<ul class="menu">';
					foreach ( array(
						'Loan Programs'         => '/loan-programs/',
						'Builders & Developers' => '/builders-developers/',
						'Realtor Partners'      => '/realtor-partners/',
						'About Joe'             => '/about-joe/',
						'Insights'              => '/insights/',
						'Contact'               => '/contact/',
					) as $label => $path ) {
						printf( '<li><a href="%s">%s</a></li>', esc_url( home_url( $path ) ), esc_html( $label ) );
					}
					echo '</ul>';
				},
			) );
			?>
		</div>

		<div class="footer-col">
			<h2 class="footer-heading">Talk to Joe</h2>
			<ul class="footer-contact">
				<li><a href="tel:<?php echo esc_attr( jb_tel() ); ?>"><?php echo jb_icon( 'phone' ); ?>Call <?php echo esc_html( jb_opt( 'phone' ) ); ?></a></li>
				<li><a href="sms:<?php echo esc_attr( jb_tel( 'sms' ) ); ?>"><?php echo jb_icon( 'message' ); ?>Text <?php echo esc_html( jb_opt( 'sms' ) ); ?></a></li>
				<li><a href="mailto:<?php echo esc_attr( jb_opt( 'email' ) ); ?>"><?php echo jb_icon( 'mail' ); ?><?php echo esc_html( jb_opt( 'email' ) ); ?></a></li>
				<?php if ( jb_opt( 'linkedin' ) ) : ?>
					<li><a href="<?php echo esc_url( jb_opt( 'linkedin' ) ); ?>" target="_blank" rel="noopener me"><?php echo jb_icon( 'linkedin' ); ?>Joe on LinkedIn</a></li>
				<?php endif; ?>
				<li><span><?php echo jb_icon( 'pin' ); ?><?php echo esc_html( jb_opt( 'street' ) ); ?><br><?php echo esc_html( jb_opt( 'city' ) . ', ' . jb_opt( 'region' ) . ' ' . jb_opt( 'postal' ) ); ?></span></li>
			</ul>
		</div>
	</div>

	<div class="wrap footer-legal">
		<?php
		wp_nav_menu( array(
			'theme_location' => 'legal',
			'container'      => 'nav',
			'container_aria_label' => 'Legal',
			'menu_class'     => 'legal-menu',
			'depth'          => 1,
			'fallback_cb'    => function () {
				echo '<nav aria-label="Legal"><ul class="legal-menu">';
				foreach ( array(
					'Privacy Policy'          => '/privacy-policy/',
					'Terms of Use'            => '/terms-of-use/',
					'Text Messaging Terms'    => '/sms-terms/',
					'Licensing & Disclosures' => '/licensing-disclosures/',
					'Texas Consumer Notice'   => '/texas-consumer-notice/',
					'Accessibility'           => '/accessibility/',
				) as $label => $path ) {
					printf( '<li><a href="%s">%s</a></li>', esc_url( home_url( $path ) ), esc_html( $label ) );
				}
				echo '</ul></nav>';
			},
		) );
		?>
		<div class="disclosure">
			<?php echo jb_ehl_logo(); ?>
			<p><?php echo jb_disclosure(); ?></p>
		</div>
		<div class="texas-notice">
			<h2 class="footer-heading">Texas Consumer Complaint &amp; Recovery Fund Notice</h2>
			<?php echo jb_texas_notice(); ?>
		</div>
		<p class="copyright">&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php echo esc_html( jb_opt( 'name' ) ); ?>. All rights reserved.</p>
	</div>
</footer>

<nav class="mobile-action-bar" aria-label="Quick actions">
	<a href="tel:<?php echo esc_attr( jb_tel() ); ?>"><?php echo jb_icon( 'phone' ); ?><span>Call</span></a>
	<a href="sms:<?php echo esc_attr( jb_tel( 'sms' ) ); ?>"><?php echo jb_icon( 'message' ); ?><span>Text</span></a>
	<a class="is-primary" href="<?php echo jb_preapproval_url(); ?>"><?php echo jb_icon( 'check' ); ?><span>Get Pre-Approved</span></a>
</nav>

<?php wp_footer(); ?>
</body>
</html>
