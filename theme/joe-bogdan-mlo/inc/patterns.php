<?php
/**
 * Block patterns for building new pages in the same style
 * (Editor → + → Patterns → "Joseph Bogdan").
 */

defined( 'ABSPATH' ) || exit;

add_action( 'init', function () {
	register_block_pattern_category( 'joe-bogdan', array( 'label' => 'Joseph Bogdan' ) );

	$patterns = array(
		'landing-hero'   => array(
			'Page hero with call to action',
			'<!-- wp:shortcode -->[jb_hero eyebrow="Short label" title="Lead with the visitor’s question" accent="in gold." lede="One or two sentences on how Joseph solves it." cta="Discover Your Buying Power" cta_url="/get-pre-approved/" image="joe-headshot.webp"]<!-- /wp:shortcode -->',
		),
		'problem-cards'  => array(
			'Questions visitors are asking (cards)',
			'<!-- wp:group {"className":"section section-ivory"} --><div class="wp-block-group section section-ivory"><!-- wp:group {"className":"wrap"} --><div class="wp-block-group wrap"><!-- wp:paragraph {"className":"eyebrow"} --><p class="eyebrow">Sound familiar?</p><!-- /wp:paragraph --><!-- wp:heading {"className":"section-title"} --><h2 class="wp-block-heading section-title">Section heading</h2><!-- /wp:heading --><!-- wp:group {"className":"card-grid"} --><div class="wp-block-group card-grid"><!-- wp:group {"className":"card"} --><div class="wp-block-group card"><!-- wp:heading {"level":3} --><h3 class="wp-block-heading">A question visitors ask</h3><!-- /wp:heading --><!-- wp:paragraph --><p>How Joseph answers it.</p><!-- /wp:paragraph --></div><!-- /wp:group --><!-- wp:group {"className":"card"} --><div class="wp-block-group card"><!-- wp:heading {"level":3} --><h3 class="wp-block-heading">Another question</h3><!-- /wp:heading --><!-- wp:paragraph --><p>How Joseph answers it.</p><!-- /wp:paragraph --></div><!-- /wp:group --><!-- wp:group {"className":"card"} --><div class="wp-block-group card"><!-- wp:heading {"level":3} --><h3 class="wp-block-heading">A third question</h3><!-- /wp:heading --><!-- wp:paragraph --><p>How Joseph answers it.</p><!-- /wp:paragraph --></div><!-- /wp:group --></div><!-- /wp:group --></div><!-- /wp:group --></div><!-- /wp:group -->',
		),
		'lead-form'      => array(
			'Lead form section',
			'<!-- wp:group {"className":"section section-navy"} --><div class="wp-block-group section section-navy"><!-- wp:group {"className":"wrap split-form"} --><div class="wp-block-group wrap split-form"><!-- wp:group {"className":"split-form-copy"} --><div class="wp-block-group split-form-copy"><!-- wp:heading {"className":"section-title"} --><h2 class="wp-block-heading section-title">Offer headline</h2><!-- /wp:heading --><!-- wp:paragraph --><p>What the visitor gets by filling this out.</p><!-- /wp:paragraph --></div><!-- /wp:group --><!-- wp:shortcode -->[jb_form type="ask-joe"]<!-- /wp:shortcode --></div><!-- /wp:group --></div><!-- /wp:group -->',
		),
		'faq'            => array(
			'FAQ (with FAQ structured data)',
			'<!-- wp:shortcode -->[jb_faq title="Straight Answers"][jb_q q="Question one?"]Answer one.[/jb_q][jb_q q="Question two?"]Answer two.[/jb_q][/jb_faq]<!-- /wp:shortcode -->',
		),
		'cta-band'       => array(
			'Call-to-action band',
			'<!-- wp:shortcode -->[jb_cta title="Know your number before you shop." text="A personalized buying-power analysis from Joseph." url="/get-pre-approved/" label="Discover Your Buying Power"]<!-- /wp:shortcode -->',
		),
		'process'        => array(
			'Four-step process',
			'<!-- wp:shortcode -->[jb_process]<!-- /wp:shortcode -->',
		),
	);

	foreach ( $patterns as $slug => $pattern ) {
		register_block_pattern( 'joe-bogdan/' . $slug, array(
			'title'      => $pattern[0],
			'categories' => array( 'joe-bogdan' ),
			'content'    => $pattern[1],
		) );
	}
} );
