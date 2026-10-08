<?php
/**
 * Section shortcodes used inside page content. Each one renders a designed
 * component while keeping its words editable from the page editor.
 */

defined( 'ABSPATH' ) || exit;

/**
 * [jb_hero eyebrow="" title="" accent="" lede="" cta="" cta_url="" image="joe-headshot.webp" variant="home|page" form=""]
 *
 * "accent" is appended to the title in gold italics. When "form" is set the
 * right column shows that lead form instead of a photo.
 */
add_shortcode( 'jb_hero', function ( $atts ) {
	$a = shortcode_atts( array(
		'eyebrow'   => '',
		'title'     => '',
		'accent'    => '',
		'lede'      => '',
		'cta'       => 'Discover Your Buying Power',
		'cta_url'   => '/get-pre-approved/',
		'secondary' => 'yes',
		'image'     => '',
		'variant'   => 'page',
		'form'         => '',
		'form_heading' => '',
		'note'         => '',
		'builder'      => '',
	), $atts );

	$url = 0 === strpos( $a['cta_url'], 'http' ) || 0 === strpos( $a['cta_url'], '#' ) ? $a['cta_url'] : home_url( $a['cta_url'] );
	ob_start();
	?>
	<section class="hero hero-<?php echo esc_attr( $a['variant'] ); ?><?php echo $a['form'] ? ' hero-has-form' : ''; ?>">
		<div class="wrap hero-grid">
			<div class="hero-copy">
				<?php if ( 'home' !== $a['variant'] ) : ?>
					<?php jb_breadcrumbs(); ?>
				<?php endif; ?>
				<?php if ( $a['eyebrow'] ) : ?>
					<p class="hero-badge"><?php echo esc_html( $a['eyebrow'] ); ?></p>
				<?php endif; ?>
				<h1 class="hero-title"><?php echo esc_html( $a['title'] ); ?><?php if ( $a['accent'] ) : ?> <em><?php echo esc_html( $a['accent'] ); ?></em><?php endif; ?></h1>
				<?php if ( $a['lede'] ) : ?>
					<p class="hero-lede"><?php echo esc_html( $a['lede'] ); ?></p>
				<?php endif; ?>
				<div class="hero-actions">
					<?php if ( $a['cta'] ) : ?>
						<a class="btn btn-gold btn-lg" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $a['cta'] ); ?> <?php echo jb_icon( 'arrow' ); ?></a>
					<?php endif; ?>
					<?php if ( 'yes' === $a['secondary'] ) : ?>
						<div class="hero-talk">
							<span>Prefer to talk?</span>
							<a href="tel:<?php echo esc_attr( jb_tel() ); ?>"><?php echo jb_icon( 'phone' ); ?> Call</a>
							<a href="sms:<?php echo esc_attr( jb_tel( 'sms' ) ); ?>"><?php echo jb_icon( 'message' ); ?> Text Joseph</a>
						</div>
					<?php endif; ?>
				</div>
				<?php if ( $a['note'] ) : ?>
					<p class="hero-note"><?php echo esc_html( $a['note'] ); ?></p>
				<?php endif; ?>
				<?php if ( $a['builder'] ) : ?>
					<a class="hero-builder" href="<?php echo esc_url( home_url( '/builders-developers/' ) ); ?>"><?php echo jb_icon( 'building' ); ?><span><strong>Builder or developer?</strong> Become a preferred lending partner</span><?php echo jb_icon( 'arrow' ); ?></a>
				<?php endif; ?>
			</div>
			<?php if ( $a['form'] ) : ?>
				<div class="hero-form" id="start"><?php echo do_shortcode( '[jb_form type="' . esc_attr( $a['form'] ) . '" heading="' . esc_attr( $a['form_heading'] ) . '"]' ); ?></div>
			<?php elseif ( $a['image'] ) : ?>
				<div class="hero-media">
					<img src="<?php echo jb_img( $a['image'] ); ?>" alt="<?php echo esc_attr( jb_opt( 'name' ) . ', ' . jb_opt( 'title' ) ); ?>" width="819" height="1024" fetchpriority="high">
					<div class="hero-card">
						<strong><?php echo esc_html( jb_opt( 'name' ) ); ?></strong>
						<span><?php echo esc_html( jb_opt( 'title' ) ); ?> · NMLS #<?php echo esc_html( jb_opt( 'nmls' ) ); ?></span>
					</div>
				</div>
			<?php endif; ?>
		</div>
	</section>
	<?php
	return ob_get_clean();
} );

/**
 * [jb_intent] - "How can Joseph help?" problem-first routing cards.
 */
add_shortcode( 'jb_intent', function ( $atts ) {
	$a = shortcode_atts( array(
		'eyebrow' => 'How Can Joseph Help?',
		'title'   => 'Start With Your Situation, Not a Loan Program.',
	), $atts );
	$cards = array(
		array( 'home', 'Buy a Home', 'How much can I afford? Can I buy before I sell?', '/loan-programs/home-purchase/', 'Plan my purchase' ),
		array( 'refresh', 'Refinance or Use Equity', 'Can I lower my payment, take cash out or drop mortgage insurance?', '/loan-programs/refinance/', 'Analyze my loan' ),
		array( 'diamond', 'Luxury & Jumbo', 'How do I finance a high-value home, ranch or second home well?', '/loan-programs/jumbo-luxury-financing/', 'Explore jumbo strategy' ),
		array( 'briefcase', 'Business Owners & Investors', 'Can I qualify if I’m self-employed? What are my investment-property options?', '/loan-programs/self-employed-business-owners/', 'See my options' ),
	);
	ob_start();
	?>
	<section class="section section-ivory intent" id="how-joe-helps">
		<div class="wrap">
			<div class="section-head">
				<p class="eyebrow"><?php echo esc_html( $a['eyebrow'] ); ?></p>
				<h2 class="section-title"><?php echo esc_html( $a['title'] ); ?></h2>
			</div>
			<div class="intent-grid">
				<?php foreach ( $cards as $card ) : ?>
					<a class="intent-card" href="<?php echo esc_url( home_url( $card[3] ) ); ?>">
						<span class="intent-icon"><?php echo jb_icon( $card[0] ); ?></span>
						<h3><?php echo esc_html( $card[1] ); ?></h3>
						<p><?php echo esc_html( $card[2] ); ?></p>
						<span class="text-link"><?php echo esc_html( $card[4] ); ?> <?php echo jb_icon( 'arrow' ); ?></span>
					</a>
				<?php endforeach; ?>
			</div>
			<p class="intent-partners">Real estate professional? <a href="<?php echo esc_url( home_url( '/realtor-partners/' ) ); ?>">Realtor partners</a> · <a href="<?php echo esc_url( home_url( '/builders-developers/' ) ); ?>">Builders &amp; developers</a></p>
		</div>
	</section>
	<?php
	return ob_get_clean();
} );

/**
 * [jb_trust] - verifiable credibility strip (no manufactured stats).
 */
add_shortcode( 'jb_trust', function () {
	$items = array(
		array( '30+ Years', 'Business & executive leadership' ),
		array( 'Former CEO', 'Built and operated multiple companies' ),
		array( 'NMLS #' . jb_opt( 'nmls' ), 'Texas-licensed mortgage loan originator', 'https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/' . rawurlencode( jb_opt( 'nmls' ) ) ),
		array( 'CrossCountry Mortgage', 'National lender, local relationship' ),
	);
	ob_start();
	?>
	<section class="trust-bar" aria-label="Credentials">
		<div class="wrap trust-grid">
			<?php foreach ( $items as $item ) : ?>
				<div class="trust-item">
					<?php if ( ! empty( $item[2] ) ) : ?>
						<a href="<?php echo esc_url( $item[2] ); ?>" target="_blank" rel="noopener"><strong><?php echo esc_html( $item[0] ); ?></strong></a>
					<?php else : ?>
						<strong><?php echo esc_html( $item[0] ); ?></strong>
					<?php endif; ?>
					<span><?php echo esc_html( $item[1] ); ?></span>
				</div>
			<?php endforeach; ?>
		</div>
	</section>
	<?php
	return ob_get_clean();
} );

/**
 * [jb_process] - Conversation → Strategy → Approval → Closing.
 */
add_shortcode( 'jb_process', function ( $atts ) {
	$a = shortcode_atts( array(
		'title' => 'Four Steps. No Guesswork.',
		'cta'   => 'Start With a Conversation',
		'url'   => '/contact/',
	), $atts );
	$steps = array(
		array( 'Conversation', 'You share your goals, timing and financial picture - in plain language.' ),
		array( 'Strategy', 'Joseph compares the realistic options and builds a plan around your priorities.' ),
		array( 'Approval', 'A strong, documented pre-approval so you can move with confidence.' ),
		array( 'Closing', 'Proactive updates to you and your agent all the way to the closing table.' ),
	);
	ob_start();
	?>
	<section class="section section-white process">
		<div class="wrap">
			<div class="section-head">
				<p class="eyebrow">How It Works</p>
				<h2 class="section-title"><?php echo esc_html( $a['title'] ); ?></h2>
			</div>
			<ol class="process-steps">
				<?php foreach ( $steps as $i => $step ) : ?>
					<li>
						<span class="process-num"><?php echo esc_html( sprintf( '%02d', $i + 1 ) ); ?></span>
						<h3><?php echo esc_html( $step[0] ); ?></h3>
						<p><?php echo esc_html( $step[1] ); ?></p>
					</li>
				<?php endforeach; ?>
			</ol>
			<?php if ( $a['cta'] ) : ?>
				<div class="process-cta">
					<a class="btn btn-gold" href="<?php echo esc_url( home_url( $a['url'] ) ); ?>"><?php echo esc_html( $a['cta'] ); ?> <?php echo jb_icon( 'arrow' ); ?></a>
				</div>
			<?php endif; ?>
		</div>
	</section>
	<?php
	return ob_get_clean();
} );

/**
 * [jb_faq title=""][jb_q q="Question?"]Answer[/jb_q][/jb_faq]
 * Questions are collected for FAQPage structured data.
 */
$GLOBALS['jb_faq_items'] = array();

add_shortcode( 'jb_faq', function ( $atts, $content = '' ) {
	$a = shortcode_atts( array( 'title' => 'Straight Answers', 'eyebrow' => 'Frequently Asked Questions', 'inline' => '' ), $atts );
	if ( $a['inline'] ) {
		// Compact version for use inside an article.
		return '<div class="faq faq-inline"><h2>' . esc_html( $a['title'] ) . '</h2><div class="faq-list">' . do_shortcode( shortcode_unautop( trim( $content ) ) ) . '</div></div>';
	}
	ob_start();
	?>
	<section class="section section-ivory faq">
		<div class="wrap wrap-narrow">
			<div class="section-head">
				<p class="eyebrow"><?php echo esc_html( $a['eyebrow'] ); ?></p>
				<h2 class="section-title"><?php echo esc_html( $a['title'] ); ?></h2>
			</div>
			<div class="faq-list">
				<?php echo do_shortcode( shortcode_unautop( trim( $content ) ) ); // phpcs:ignore ?>
			</div>
		</div>
	</section>
	<?php
	return ob_get_clean();
} );

add_shortcode( 'jb_q', function ( $atts, $content = '' ) {
	$a      = shortcode_atts( array( 'q' => '' ), $atts );
	$answer = wpautop( trim( $content ) );
	$GLOBALS['jb_faq_items'][] = array( 'q' => $a['q'], 'a' => wp_strip_all_tags( $answer ) );
	return sprintf(
		'<details class="faq-item"><summary><h3>%s</h3>%s</summary><div class="faq-answer">%s</div></details>',
		esc_html( $a['q'] ),
		jb_icon( 'chevron', 'faq-chevron' ),
		wp_kses_post( $answer )
	);
} );

/**
 * [jb_video title=""] - Joseph's intro video. Renders nothing publicly until a
 * video URL is set in Appearance → Joseph Bogdan Settings.
 */
add_shortcode( 'jb_video', function ( $atts ) {
	$a     = shortcode_atts( array( 'title' => 'Meet Joseph in 90 Seconds' ), $atts );
	$video = jb_video_data();
	if ( ! $video ) {
		return jb_editor_note( 'Intro video slot: add a 60-90 second video URL in Appearance → Joseph Bogdan Settings and it will appear here.' );
	}
	$GLOBALS['jb_video_on_page'] = true;
	$html = sprintf(
		'<div class="video-embed" data-embed="%1$s"><img src="%2$s" alt="" loading="lazy"><button type="button" class="video-play">%3$s<span>%4$s</span></button></div>',
		esc_url( $video['embed'] . ( false === strpos( $video['embed'], '?' ) ? '?' : '&' ) . 'autoplay=1' ),
		esc_url( $video['thumb'] ),
		jb_icon( 'play' ),
		esc_html( $a['title'] )
	);
	if ( $video['transcript'] ) {
		$html .= '<details class="video-transcript"><summary>Read the transcript</summary>' . wpautop( esc_html( $video['transcript'] ) ) . '</details>';
	}
	return $html;
} );

/**
 * Intro video details from settings (also used for VideoObject schema).
 */
function jb_video_data() {
	$url = jb_opt( 'video_url' );
	if ( ! $url ) {
		return null;
	}
	if ( preg_match( '~(?:youtu\.be/|v=|embed/|shorts/)([\w-]{11})~', $url, $m ) ) {
		$embed = 'https://www.youtube-nocookie.com/embed/' . $m[1] . '?rel=0';
		$thumb = 'https://i.ytimg.com/vi/' . $m[1] . '/hqdefault.jpg';
	} elseif ( preg_match( '~vimeo\.com/(\d+)~', $url, $m ) ) {
		$embed = 'https://player.vimeo.com/video/' . $m[1];
		$thumb = jb_img( 'joe-headshot.webp' );
	} else {
		return null;
	}
	return array(
		'url'         => $url,
		'embed'       => $embed,
		'thumb'       => $thumb,
		'title'       => jb_opt( 'video_title' ),
		'description' => jb_opt( 'video_description' ),
		'date'        => jb_opt( 'video_date' ),
		'transcript'  => jb_opt( 'video_transcript' ),
	);
}

/**
 * [jb_contact_options] - call / text / email cards.
 */
add_shortcode( 'jb_contact_options', function () {
	$options = array(
		array( 'phone', 'Call Joseph', jb_opt( 'phone' ), 'tel:' . jb_tel() ),
		array( 'message', 'Text Joseph', jb_opt( 'sms' ), 'sms:' . jb_tel( 'sms' ) ),
		array( 'mail', 'Email Joseph', jb_opt( 'email' ), 'mailto:' . jb_opt( 'email' ) ),
	);
	if ( jb_opt( 'calendar_url' ) ) {
		$options[] = array( 'clock', 'Book a Time', 'Pick a time that works for you', jb_opt( 'calendar_url' ) );
	}
	$out = '<div class="contact-options">';
	foreach ( $options as $o ) {
		$out .= sprintf(
			'<a class="contact-option" href="%s"><span class="contact-option-icon">%s</span><span><strong>%s</strong><small>%s</small></span></a>',
			esc_url( $o[3], array( 'tel', 'sms', 'mailto', 'http', 'https' ) ),
			jb_icon( $o[0] ),
			esc_html( $o[1] ),
			esc_html( $o[2] )
		);
	}
	return $out . '</div>';
} );

/**
 * [jb_latest count="3" category=""] - latest Insights.
 */
add_shortcode( 'jb_latest', function ( $atts ) {
	$a = shortcode_atts( array( 'count' => 3, 'category' => '', 'title' => 'Straight Answers to Common Questions' ), $atts );
	$q = new WP_Query( array(
		'posts_per_page'      => (int) $a['count'],
		'category_name'       => $a['category'],
		'ignore_sticky_posts' => true,
	) );
	if ( ! $q->have_posts() ) {
		return '';
	}
	ob_start();
	?>
	<section class="section section-ivory">
		<div class="wrap">
			<div class="section-head section-head-split">
				<div>
					<p class="eyebrow">Insights</p>
					<h2 class="section-title"><?php echo esc_html( $a['title'] ); ?></h2>
				</div>
				<a class="text-link" href="<?php echo esc_url( home_url( '/insights/' ) ); ?>">All insights <?php echo jb_icon( 'arrow' ); ?></a>
			</div>
			<div class="post-grid">
				<?php
				while ( $q->have_posts() ) {
					$q->the_post();
					jb_post_card();
				}
				wp_reset_postdata();
				?>
			</div>
		</div>
	</section>
	<?php
	return ob_get_clean();
} );

/**
 * [jb_cta title="" text="" url="" label="" tone="navy|gold"]
 */
add_shortcode( 'jb_cta', function ( $atts ) {
	$a = shortcode_atts( array(
		'title' => 'Know your number before you shop.',
		'text'  => 'A personalized buying-power analysis from Joseph - not a generic calculator result.',
		'url'   => '/get-pre-approved/',
		'label' => 'Discover Your Buying Power',
		'tone'  => 'navy',
	), $atts );
	ob_start();
	jb_cta_band( array( $a['title'], $a['text'], $a['url'], $a['label'] ), $a['tone'] );
	return ob_get_clean();
} );

/** [jb_opt key="nmls"] - print a setting inline (legal pages). */
add_shortcode( 'jb_opt', function ( $atts ) {
	$a = shortcode_atts( array( 'key' => '' ), $atts );
	return esc_html( jb_opt( $a['key'] ) );
} );

/** [jb_texas_notice] - Texas complaint / recovery fund notice. */
add_shortcode( 'jb_texas_notice', 'jb_texas_notice' );

/** [jb_disclosure] - full lender disclosure paragraph. */
add_shortcode( 'jb_disclosure', function () {
	return '<p class="fine-print">' . jb_disclosure() . '</p>';
} );

/** [jb_todo]Note[/jb_todo] - visible only to logged-in editors. */
add_shortcode( 'jb_todo', function ( $atts, $content = '' ) {
	return jb_editor_note( $content );
} );

function jb_editor_note( $text ) {
	if ( ! current_user_can( 'edit_pages' ) ) {
		return '';
	}
	return '<div class="editor-note" role="note"><strong>Editor note (hidden from visitors):</strong> ' . esc_html( $text ) . '</div>';
}


/** [jb_photo file="strategy.webp" alt="" class=""] - theme image that survives domain changes. */
add_shortcode( 'jb_photo', function ( $atts ) {
	$a = shortcode_atts( array( 'file' => 'joe-headshot.webp', 'alt' => '', 'class' => '' ), $atts );
	$path = JB_DIR . '/assets/images/' . basename( $a['file'] );
	$size = file_exists( $path ) ? @getimagesize( $path ) : false; // phpcs:ignore
	return sprintf(
		'<figure class="photo %s"><img src="%s" alt="%s"%s loading="lazy" decoding="async"></figure>',
		esc_attr( $a['class'] ),
		jb_img( basename( $a['file'] ) ),
		esc_attr( $a['alt'] ),
		$size ? sprintf( ' width="%d" height="%d"', $size[0], $size[1] ) : ''
	);
} );

/**
 * [jb_inline_cta title="" text="" url="" label=""] - offer box inside an article.
 */
add_shortcode( 'jb_inline_cta', function ( $atts ) {
	$a = shortcode_atts( array(
		'title' => 'Know your number before you shop.',
		'text'  => 'Get a free, personalized buying-power analysis from Joseph. No credit pull.',
		'url'   => '/get-pre-approved/',
		'label' => 'Discover Your Buying Power',
	), $atts );
	$url = 0 === strpos( $a['url'], 'http' ) ? $a['url'] : home_url( $a['url'] );
	return sprintf(
		'<aside class="inline-cta"><div><p class="inline-cta-title">%s</p><p>%s</p></div><div class="inline-cta-actions"><a class="btn btn-gold" href="%s">%s %s</a><a class="inline-cta-text" href="sms:%s">%s Or text Joseph</a></div></aside>',
		esc_html( $a['title'] ),
		esc_html( $a['text'] ),
		esc_url( $url ),
		esc_html( $a['label'] ),
		jb_icon( 'arrow' ),
		esc_attr( jb_tel( 'sms' ) ),
		jb_icon( 'message' )
	);
} );
