<?php
/**
 * Small rendering helpers shared by templates and shortcodes.
 */

defined( 'ABSPATH' ) || exit;

/**
 * Inline stroke icon. Decorative by default (aria-hidden).
 */
function jb_icon( $name, $class = '' ) {
	$paths = array(
		'phone'     => '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
		'message'   => '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
		'arrow'     => '<path d="M5 12h14M13 6l6 6-6 6"/>',
		'home'      => '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
		'refresh'   => '<path d="M20 11a8 8 0 0 0-14.9-3M4 4v4h4"/><path d="M4 13a8 8 0 0 0 14.9 3M20 20v-4h-4"/>',
		'diamond'   => '<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18M9 3l3 18 3-18"/>',
		'briefcase' => '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
		'building'  => '<path d="M4 21V5l8-3v19M12 9h8v12M4 21h18"/><path d="M8 8h.01M8 12h.01M8 16h.01M16 13h.01M16 17h.01"/>',
		'handshake' => '<path d="M11 17l2 2a1.4 1.4 0 0 0 2-2"/><path d="M14 14l2.5 2.5a1.4 1.4 0 0 0 2-2L15 11l-3 1-2-2 4-4 7 6"/><path d="M3 9l4-4 3 2M3 9l7 7 1.5 1.5a1.4 1.4 0 0 1-2 2L8 18"/>',
		'check'     => '<path d="M5 12.5l4.5 4.5L19 7"/>',
		'chart'     => '<path d="M4 20V4M4 20h16"/><path d="M8 16l4-5 3 3 5-7"/>',
		'clock'     => '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
		'shield'    => '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
		'play'      => '<path d="M8 5l11 7-11 7z"/>',
		'mail'      => '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
		'pin'       => '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
		'menu'      => '<path d="M4 7h16M4 12h16M4 17h16"/>',
		'close'     => '<path d="M6 6l12 12M18 6L6 18"/>',
		'chevron'   => '<path d="M6 9l6 6 6-6"/>',
		'calc'      => '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15v3M8 18h4"/>',
		'key'       => '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>',
		'linkedin'  => '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
		'users'     => '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
	);
	if ( ! isset( $paths[ $name ] ) ) {
		return '';
	}
	return sprintf(
		'<svg class="icon %s" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>',
		esc_attr( $class ),
		$paths[ $name ]
	);
}

/** URL of a theme image. */
function jb_img( $file ) {
	return esc_url( JB_URI . '/assets/images/' . $file );
}

/** URL of the main conversion page. */
function jb_preapproval_url() {
	return esc_url( home_url( '/get-pre-approved/' ) );
}

/** Lender disclosure used in the footer, on legal pages and near forms. */
function jb_disclosure() {
	$company_url = jb_opt( 'company_url' );
	return sprintf(
		'%1$s, %2$s, NMLS #%3$s. %4$s. %5$s, NMLS #%6$s, <a href="%7$s" rel="noopener" target="_blank">%8$s</a>. %9$s. Equal Housing Opportunity Lender. Verify licensing at <a href="https://www.nmlsconsumeraccess.org/" rel="noopener" target="_blank">www.nmlsconsumeraccess.org</a> and see <a href="%10$s" rel="noopener" target="_blank">CrossCountry Mortgage licensing and disclosures</a>. This is not a commitment to lend. All loans are subject to credit approval, underwriting guidelines and program availability. Programs, rates, terms and conditions are subject to change without notice. Not all applicants will qualify.',
		esc_html( jb_opt( 'legal_name' ) ),
		esc_html( jb_opt( 'title' ) ),
		esc_html( jb_opt( 'nmls' ) ),
		esc_html( jb_opt( 'licensing' ) ),
		esc_html( jb_opt( 'company' ) ),
		esc_html( jb_opt( 'company_nmls' ) ),
		esc_url( $company_url ),
		esc_html( untrailingslashit( preg_replace( '#^https?://(www\.)?#', '', $company_url ) ) ),
		esc_html( jb_opt( 'company_license' ) ),
		esc_url( jb_opt( 'company_licensing_url' ) )
	);
}

/**
 * Texas Consumer Complaint and Recovery Fund Notice (mortgage banker version,
 * matching CrossCountry Mortgage's published notice). Required on the site.
 */
function jb_texas_notice() {
	return '<p>Consumers wishing to file a complaint against a mortgage banker or a licensed mortgage banker residential mortgage loan originator should complete and send a complaint form to the Texas Department of Savings and Mortgage Lending, 2601 N. Lamar, Suite 201, Austin, Texas 78705. Complaint forms and instructions may be obtained from the Department’s website at <a href="https://www.sml.texas.gov" rel="noopener" target="_blank">www.sml.texas.gov</a>. A toll-free consumer hotline is available at 1-877-276-5550.</p>'
		. '<p>The Department maintains a recovery fund to make payments of certain actual out of pocket damages sustained by borrowers caused by acts of licensed mortgage banker residential mortgage loan originators. A written application for reimbursement from the recovery fund must be filed with and investigated by the Department prior to the payment of a claim. For more information about the recovery fund, please consult the Department’s website at <a href="https://www.sml.texas.gov" rel="noopener" target="_blank">www.sml.texas.gov</a>.</p>';
}

/** Equal Housing Opportunity logo (inline SVG). */
function jb_ehl_logo() {
	return '<svg class="ehl" viewBox="0 0 64 64" width="40" height="40" role="img" aria-label="Equal Housing Opportunity Lender"><path fill="currentColor" d="M32 4 2 22v6h4v30h52V28h4v-6zm18 50H14V26l18-11 18 11zM20 32h24v5H20zm0 10h24v5H20z"/></svg>';
}

/**
 * Breadcrumb trail for interior pages (visual; schema is emitted in seo.php).
 */
function jb_breadcrumbs() {
	$trail = jb_breadcrumb_items();
	if ( count( $trail ) < 2 ) {
		return;
	}
	echo '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>';
	$last = count( $trail ) - 1;
	foreach ( $trail as $i => $item ) {
		if ( $i === $last ) {
			printf( '<li aria-current="page">%s</li>', esc_html( $item['name'] ) );
		} else {
			printf( '<li><a href="%s">%s</a></li>', esc_url( $item['url'] ), esc_html( $item['name'] ) );
		}
	}
	echo '</ol></nav>';
}

function jb_breadcrumb_items() {
	$items = array( array( 'name' => 'Home', 'url' => home_url( '/' ) ) );
	if ( is_front_page() ) {
		return $items;
	}
	if ( is_page() ) {
		$id = get_queried_object_id();
		foreach ( array_reverse( get_post_ancestors( $id ) ) as $ancestor ) {
			$items[] = array( 'name' => get_the_title( $ancestor ), 'url' => get_permalink( $ancestor ) );
		}
		$items[] = array( 'name' => get_the_title( $id ), 'url' => get_permalink( $id ) );
	} elseif ( is_singular( 'post' ) || is_home() || is_category() ) {
		$posts_page = (int) get_option( 'page_for_posts' );
		if ( $posts_page ) {
			$items[] = array( 'name' => get_the_title( $posts_page ), 'url' => get_permalink( $posts_page ) );
		}
		if ( is_category() ) {
			$items[] = array( 'name' => single_cat_title( '', false ), 'url' => get_category_link( get_queried_object_id() ) );
		} elseif ( is_singular() ) {
			$cats = get_the_category();
			if ( $cats ) {
				$items[] = array( 'name' => $cats[0]->name, 'url' => get_category_link( $cats[0] ) );
			}
			$items[] = array( 'name' => get_the_title(), 'url' => get_permalink() );
		}
	}
	return $items;
}

/**
 * Fallback primary menu, used until a menu is assigned in Appearance → Menus.
 */
function jb_fallback_menu() {
	$links = array(
		array( 'Loan Programs', '/loan-programs/', array(
			array( 'Home Purchase', '/loan-programs/home-purchase/' ),
			array( 'Refinance & Equity', '/loan-programs/refinance/' ),
			array( 'Jumbo & Luxury Financing', '/loan-programs/jumbo-luxury-financing/' ),
			array( 'Self-Employed & Business Owners', '/loan-programs/self-employed-business-owners/' ),
			array( 'Investment Property', '/loan-programs/investment-property/' ),
		) ),
		array( 'Builders & Developers', '/builders-developers/' ),
		array( 'Realtor Partners', '/realtor-partners/' ),
		array( 'About Joe', '/about-joe/' ),
		array( 'Insights', '/insights/' ),
		array( 'Contact', '/contact/' ),
	);
	echo '<ul id="primary-menu" class="menu">';
	foreach ( $links as $link ) {
		$has_children = ! empty( $link[2] );
		printf( '<li class="menu-item%s"><a href="%s">%s</a>', $has_children ? ' menu-item-has-children' : '', esc_url( home_url( $link[1] ) ), esc_html( $link[0] ) );
		if ( $has_children ) {
			echo '<ul class="sub-menu">';
			foreach ( $link[2] as $child ) {
				printf( '<li class="menu-item"><a href="%s">%s</a></li>', esc_url( home_url( $child[1] ) ), esc_html( $child[0] ) );
			}
			echo '</ul>';
		}
		echo '</li>';
	}
	echo '</ul>';
}

/**
 * Insights content pillars and the next action each one leads to.
 * Keys are category slugs.
 */
function jb_pillars() {
	return array(
		'home-buying'            => array(
			'name' => 'Home Buying',
			'cta'  => array( 'Know your number before you shop.', 'Get a personalized buying-power analysis from Joe — not a generic calculator result.', '/get-pre-approved/', 'Discover Your Buying Power' ),
		),
		'mortgage-strategy'      => array(
			'name' => 'Mortgage Strategy',
			'cta'  => array( 'Want a second set of eyes on your plan?', 'Tell Joe what you are weighing and he will map the options with you.', '/contact/', 'Ask Joe About Your Scenario' ),
		),
		'texas-housing-market'   => array(
			'name' => 'Texas Housing & Market',
			'cta'  => array( 'Buying in North Texas?', 'See what you can comfortably afford in today’s market.', '/get-pre-approved/', 'Discover Your Buying Power' ),
		),
		'luxury-jumbo'           => array(
			'name' => 'Luxury & Jumbo',
			'cta'  => array( 'Financing a high-value home?', 'Book a private jumbo financing consultation with Joe.', '/loan-programs/jumbo-luxury-financing/#consultation', 'Request a Jumbo Consultation' ),
		),
		'business-owners'        => array(
			'name' => 'Business Owners & Self-Employed',
			'cta'  => array( 'Self-employed? Your tax return isn’t the whole story.', 'Get a Self-Employed Mortgage Strategy Review.', '/loan-programs/self-employed-business-owners/#strategy-review', 'Request a Strategy Review' ),
		),
		'real-estate-investing'  => array(
			'name' => 'Real Estate Investing',
			'cta'  => array( 'Running numbers on a property?', 'Send Joe the scenario and get your financing options.', '/loan-programs/investment-property/#investor-scenario', 'Run an Investor Scenario' ),
		),
	);
}

/** CTA tuple for a post, based on its first pillar category. */
function jb_post_cta( $post_id = null ) {
	$pillars = jb_pillars();
	foreach ( get_the_category( $post_id ) as $cat ) {
		if ( isset( $pillars[ $cat->slug ] ) ) {
			return $pillars[ $cat->slug ]['cta'];
		}
	}
	return $pillars['home-buying']['cta'];
}

/** Full-width conversion band. */
function jb_cta_band( $cta, $tone = 'navy' ) {
	list( $title, $text, $path, $label ) = $cta;
	?>
	<section class="cta-band cta-band-<?php echo esc_attr( $tone ); ?>">
		<div class="wrap cta-band-inner">
			<div>
				<h2><?php echo esc_html( $title ); ?></h2>
				<p><?php echo esc_html( $text ); ?></p>
			</div>
			<div class="btn-row">
				<a class="btn btn-gold" href="<?php echo esc_url( home_url( $path ) ); ?>"><?php echo esc_html( $label ); ?></a>
				<a class="btn btn-outline" href="sms:<?php echo esc_attr( jb_tel( 'sms' ) ); ?>"><?php echo jb_icon( 'message' ); ?> Text Joe</a>
			</div>
		</div>
	</section>
	<?php
}

/** Article card used in listings. */
function jb_post_card() {
	$cats = get_the_category();
	?>
	<article class="post-card">
		<a class="post-card-link" href="<?php the_permalink(); ?>">
			<?php if ( has_post_thumbnail() ) : ?>
				<?php the_post_thumbnail( 'jb-card', array( 'loading' => 'lazy', 'class' => 'post-card-img' ) ); ?>
			<?php endif; ?>
			<div class="post-card-body">
				<?php if ( $cats ) : ?>
					<span class="eyebrow"><?php echo esc_html( $cats[0]->name ); ?></span>
				<?php endif; ?>
				<h3><?php the_title(); ?></h3>
				<p><?php echo esc_html( get_the_excerpt() ); ?></p>
				<span class="text-link">Read the answer <?php echo jb_icon( 'arrow' ); ?></span>
			</div>
		</a>
	</article>
	<?php
}
