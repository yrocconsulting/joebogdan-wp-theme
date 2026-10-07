<?php
/**
 * Lead funnels: form definitions, rendering, submission handling,
 * storage (private "Leads" post type) and email delivery.
 *
 * Usage in content: [jb_form type="buying-power"]
 */

defined( 'ABSPATH' ) || exit;

/* ---------------------------------------------------------------------------
 * Form definitions
 * ------------------------------------------------------------------------ */

function jb_credit_options() {
	return array( 'Excellent (740+)', 'Good (680–739)', 'Fair (620–679)', 'Below 620', 'Not sure' );
}

function jb_contact_step( $title = 'Where should Joe send it?' ) {
	return array(
		'title'  => $title,
		'fields' => array(
			array( 'first_name', 'First name', 'text', null, true, 'half', 'given-name' ),
			array( 'last_name', 'Last name', 'text', null, true, 'half', 'family-name' ),
			array( 'phone', 'Mobile number', 'tel', null, true, 'half', 'tel' ),
			array( 'email', 'Email', 'email', null, true, 'half', 'email' ),
			array( 'contact_pref', 'Best way to reach you', 'chips', array( 'Text', 'Call', 'Email' ), false ),
		),
	);
}

/**
 * Each field: [ name, label, type, options, required, width, autocomplete, help ].
 */
function jb_forms() {
	return array(
		'buying-power'      => array(
			'label'   => 'Buying Power Analysis',
			'heading' => 'Discover Your Buying Power',
			'submit'  => 'Get My Buying-Power Analysis',
			'steps'   => array(
				array(
					'title'  => 'Tell Joe about your move',
					'fields' => array(
						array( 'goal', 'What are you planning?', 'cards', array( 'Buy my first home', 'Buy my next home', 'Buy a second home', 'Buy an investment property' ), true ),
						array( 'timeline', 'When would you like to buy?', 'chips', array( '0–3 months', '3–6 months', '6–12 months', 'Just exploring' ), true ),
						array( 'own_home', 'Do you currently own a home?', 'chips', array( 'No', 'Yes — I need to sell it', 'Yes — I’m keeping it' ), true ),
						array( 'area', 'Where are you looking?', 'text', null, false, 'half', 'address-level2', 'City or area, e.g. Flower Mound' ),
						array( 'price_target', 'Price range in mind (optional)', 'currency', null, false, 'half' ),
					),
				),
				array(
					'title'  => 'A quick look at the numbers',
					'note'   => 'Estimates are fine. This never affects your credit.',
					'fields' => array(
						array( 'employment', 'How are you paid?', 'chips', array( 'W-2 / salary', 'Self-employed / business owner', 'Commission or bonus', 'Retired / fixed income', 'A mix' ), true ),
						array( 'income', 'Gross household income (yearly)', 'currency', null, true, 'half' ),
						array( 'debts', 'Monthly debt payments', 'currency', null, true, 'half', null, 'Car, student loans, minimum card payments. Not rent.' ),
						array( 'down_payment', 'Cash available for down payment', 'currency', null, true, 'half' ),
						array( 'credit', 'Credit estimate', 'select', jb_credit_options(), true, 'half' ),
						array( 'veteran', 'Have you served in the military?', 'chips', array( 'No', 'Yes' ), false ),
					),
				),
				jb_contact_step( 'Where should Joe send your analysis?' ),
			),
		),
		'self-employed'     => array(
			'label'   => 'Self-Employed Mortgage Strategy Review',
			'heading' => 'Request Your Self-Employed Strategy Review',
			'submit'  => 'Request My Strategy Review',
			'steps'   => array(
				array(
					'title'  => 'Your business',
					'fields' => array(
						array( 'business_type', 'How is your income structured?', 'chips', array( 'Sole proprietor', 'LLC', 'S-Corp', 'Partnership', '1099 contractor', 'Not sure' ), true ),
						array( 'years', 'Years self-employed', 'chips', array( 'Less than 2', '2–5', '5–10', '10+' ), true ),
						array( 'goal', 'What are you trying to do?', 'chips', array( 'Buy a home', 'Refinance', 'Buy an investment property' ), true ),
						array( 'price_target', 'Approximate price or loan amount', 'currency', null, false, 'half' ),
						array( 'credit', 'Credit estimate', 'select', jb_credit_options(), false, 'half' ),
						array( 'concern', 'What worries you most about qualifying?', 'textarea', null, false, null, null, 'e.g. write-offs lower my taxable income, income varies year to year' ),
					),
				),
				jb_contact_step( 'Where should Joe reach you?' ),
			),
		),
		'jumbo'             => array(
			'label'   => 'Jumbo Financing Consultation',
			'heading' => 'Request a Private Jumbo Financing Consultation',
			'submit'  => 'Request My Consultation',
			'steps'   => array(
				array(
					'title'  => 'The property',
					'fields' => array(
						array( 'goal', 'Purchase or refinance?', 'chips', array( 'Purchase', 'Refinance', 'Cash-out refinance' ), true ),
						array( 'price_band', 'Price range', 'chips', array( '$800K–$1.5M', '$1.5M–$3M', '$3M+' ), true ),
						array( 'property_type', 'Property type', 'chips', array( 'Primary residence', 'Second home', 'Ranch / acreage', 'New construction' ), true ),
						array( 'timeline', 'Timeline', 'chips', array( 'Under contract', '0–3 months', '3–12 months', 'Planning ahead' ), true ),
						array( 'notes', 'Anything Joe should know?', 'textarea', null, false, null, null, 'e.g. complex income, assets in a trust, buying before selling' ),
					),
				),
				jb_contact_step( 'Where should Joe reach you?' ),
			),
		),
		'refinance'         => array(
			'label'   => 'Refinance & Equity Analysis',
			'heading' => 'Get Your Refinance & Equity Analysis',
			'submit'  => 'Get My Analysis',
			'steps'   => array(
				array(
					'title'  => 'Your current loan',
					'fields' => array(
						array( 'goal', 'What would you like to accomplish?', 'cards', array( 'Lower my payment', 'Take cash out', 'Consolidate debt', 'Remove mortgage insurance', 'Pay off faster', 'Not sure yet' ), true ),
						array( 'home_value', 'Estimated home value', 'currency', null, true, 'half' ),
						array( 'balance', 'Current loan balance', 'currency', null, true, 'half' ),
						array( 'current_rate', 'Current interest rate (%)', 'number', null, false, 'half', null, 'e.g. 7.25' ),
						array( 'credit', 'Credit estimate', 'select', jb_credit_options(), false, 'half' ),
					),
				),
				jb_contact_step( 'Where should Joe send your analysis?' ),
			),
		),
		'investor'          => array(
			'label'   => 'Investor Financing Scenario',
			'heading' => 'Run an Investor Financing Scenario',
			'submit'  => 'Send My Scenario',
			'steps'   => array(
				array(
					'title'  => 'The deal',
					'fields' => array(
						array( 'property_type', 'Property type', 'chips', array( 'Single-family rental', '2–4 units', 'Short-term rental', 'Fix & hold', 'Portfolio / multiple' ), true ),
						array( 'goal', 'Purchase or refinance?', 'chips', array( 'Purchase', 'Rate/term refinance', 'Cash-out refinance' ), true ),
						array( 'price_target', 'Price or value', 'currency', null, true, 'half' ),
						array( 'rent', 'Expected monthly rent', 'currency', null, false, 'half' ),
						array( 'down_payment', 'Cash available', 'currency', null, false, 'half' ),
						array( 'experience', 'Properties you own today', 'select', array( 'None yet', '1–2', '3–9', '10+' ), false, 'half' ),
						array( 'notes', 'Anything else?', 'textarea', null, false ),
					),
				),
				jb_contact_step( 'Where should Joe send your options?' ),
			),
		),
		'realtor-scenario'  => array(
			'label'   => 'Realtor Client Scenario',
			'heading' => 'Run a Financing Scenario for My Client',
			'submit'  => 'Send the Scenario to Joe',
			'steps'   => array(
				array(
					'title'  => 'Your client’s scenario',
					'note'   => 'No client names needed. Joe will reach out to you first.',
					'fields' => array(
						array( 'urgency', 'How soon do you need an answer?', 'chips', array( 'Writing an offer today', 'This week', 'Planning ahead' ), true ),
						array( 'price_target', 'Target price', 'currency', null, true, 'half' ),
						array( 'down_payment', 'Down payment available', 'currency', null, false, 'half' ),
						array( 'employment', 'Client income type', 'chips', array( 'W-2', 'Self-employed', 'Commission / bonus', 'Retired', 'Mixed / complex' ), true ),
						array( 'credit', 'Credit estimate', 'select', jb_credit_options(), false, 'half' ),
						array( 'own_home', 'Does the client need to sell first?', 'select', array( 'No', 'Yes', 'Not sure' ), false, 'half' ),
						array( 'notes', 'What’s the challenge?', 'textarea', null, false, null, null, 'e.g. recent job change, needs to buy before selling, jumbo, credit event' ),
					),
				),
				array(
					'title'  => 'Your details',
					'fields' => array(
						array( 'first_name', 'First name', 'text', null, true, 'half', 'given-name' ),
						array( 'last_name', 'Last name', 'text', null, true, 'half', 'family-name' ),
						array( 'phone', 'Mobile number', 'tel', null, true, 'half', 'tel' ),
						array( 'email', 'Email', 'email', null, true, 'half', 'email' ),
						array( 'brokerage', 'Brokerage', 'text', null, false, 'half', 'organization' ),
						array( 'contact_pref', 'Best way to reach you', 'chips', array( 'Text', 'Call', 'Email' ), false ),
					),
				),
			),
		),
		'builder'           => array(
			'label'   => 'Builder / Developer Partnership',
			'heading' => 'Become a Preferred Lending Partner',
			'submit'  => 'Start the Conversation',
			'steps'   => array(
				array(
					'title'  => 'Your communities',
					'fields' => array(
						array( 'company', 'Company', 'text', null, true, 'half', 'organization' ),
						array( 'role', 'Your role', 'text', null, false, 'half', 'organization-title' ),
						array( 'volume', 'Homes closed per year', 'chips', array( 'Under 10', '10–50', '50–150', '150+' ), false ),
						array( 'price_band', 'Typical price range', 'chips', array( 'Under $400K', '$400K–$750K', '$750K–$1.5M', '$1.5M+' ), false ),
						array( 'notes', 'Communities and what you need from a lender', 'textarea', null, false, null, null, 'e.g. faster pre-approvals for model-home traffic, fewer fall-throughs, better buyer communication' ),
					),
				),
				array(
					'title'  => 'Your details',
					'fields' => array(
						array( 'first_name', 'First name', 'text', null, true, 'half', 'given-name' ),
						array( 'last_name', 'Last name', 'text', null, true, 'half', 'family-name' ),
						array( 'phone', 'Mobile number', 'tel', null, true, 'half', 'tel' ),
						array( 'email', 'Email', 'email', null, true, 'half', 'email' ),
					),
				),
			),
		),
		'ask-joe'           => array(
			'label'   => 'Ask Joe',
			'heading' => 'Ask Joe About Your Scenario',
			'submit'  => 'Send to Joe',
			'steps'   => array(
				array(
					'title'  => 'Your question',
					'fields' => array(
						array( 'topic', 'I’m asking about…', 'select', array( 'Buying a home', 'Refinancing or using equity', 'Jumbo / luxury financing', 'Self-employed or business owner', 'Investment property', 'I’m a Realtor', 'I’m a builder / developer', 'Something else' ), true ),
						array( 'notes', 'Your scenario or question', 'textarea', null, true ),
						array( 'first_name', 'First name', 'text', null, true, 'half', 'given-name' ),
						array( 'last_name', 'Last name', 'text', null, true, 'half', 'family-name' ),
						array( 'phone', 'Mobile number', 'tel', null, true, 'half', 'tel' ),
						array( 'email', 'Email', 'email', null, true, 'half', 'email' ),
						array( 'contact_pref', 'Best way to reach you', 'chips', array( 'Text', 'Call', 'Email' ), false ),
					),
				),
			),
		),
	);
}

/* ---------------------------------------------------------------------------
 * Rendering
 * ------------------------------------------------------------------------ */

add_shortcode( 'jb_form', function ( $atts ) {
	$atts  = shortcode_atts( array( 'type' => 'ask-joe', 'heading' => '' ), $atts );
	$forms = jb_forms();
	if ( ! isset( $forms[ $atts['type'] ] ) ) {
		return '';
	}
	$form    = $forms[ $atts['type'] ];
	$steps   = $form['steps'];
	$count   = count( $steps );
	$uid     = 'jbf-' . wp_unique_id();
	$heading = $atts['heading'] ? $atts['heading'] : $form['heading'];

	ob_start();
	?>
	<div class="lead-form" data-form="<?php echo esc_attr( $atts['type'] ); ?>">
		<form class="lead-form-inner" method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" novalidate aria-labelledby="<?php echo esc_attr( $uid ); ?>-title">
			<div class="lead-form-head">
				<h3 class="lead-form-title" id="<?php echo esc_attr( $uid ); ?>-title"><?php echo esc_html( $heading ); ?></h3>
				<?php if ( $count > 1 ) : ?>
					<div class="lead-progress" aria-hidden="true">
						<?php for ( $i = 0; $i < $count; $i++ ) : ?>
							<span class="<?php echo 0 === $i ? 'is-active' : ''; ?>"></span>
						<?php endfor; ?>
					</div>
				<?php endif; ?>
			</div>

			<input type="hidden" name="action" value="jb_lead">
			<input type="hidden" name="form_type" value="<?php echo esc_attr( $atts['type'] ); ?>">
			<input type="hidden" name="jb_ts" value="<?php echo esc_attr( base64_encode( (string) time() ) ); ?>">
			<input type="hidden" name="source_url" value="">
			<input type="hidden" name="utm" value="">
			<div class="hp-field" aria-hidden="true">
				<label for="<?php echo esc_attr( $uid ); ?>-website">Website</label>
				<input type="text" id="<?php echo esc_attr( $uid ); ?>-website" name="website" tabindex="-1" autocomplete="off">
			</div>

			<?php foreach ( $steps as $s => $step ) : ?>
				<fieldset class="lead-step" data-step="<?php echo (int) $s; ?>" <?php echo $s > 0 ? 'hidden' : ''; ?>>
					<legend class="lead-step-title">
						<?php if ( $count > 1 ) : ?>
							<span class="lead-step-count">Step <?php echo (int) $s + 1; ?> of <?php echo (int) $count; ?></span>
						<?php endif; ?>
						<?php echo esc_html( $step['title'] ); ?>
					</legend>
					<?php if ( ! empty( $step['note'] ) ) : ?>
						<p class="lead-step-note"><?php echo esc_html( $step['note'] ); ?></p>
					<?php endif; ?>
					<div class="lead-fields">
						<?php
						foreach ( $step['fields'] as $field ) {
							echo jb_render_field( $field, $uid ); // phpcs:ignore WordPress.Security.EscapeOutput
						}
						?>
					</div>

					<?php if ( $s === $count - 1 ) : ?>
						<div class="lead-consent">
							<label class="check">
								<input type="checkbox" name="sms_consent" value="yes">
								<span>Optional: I agree to receive text messages from <?php echo esc_html( jb_opt( 'name' ) ); ?> and <?php echo esc_html( jb_opt( 'company' ) ); ?> about my inquiry at the mobile number above, which may be sent using automated technology. Message frequency varies; message and data rates may apply. Reply STOP to opt out or HELP for help. Consent is not a condition of any purchase or loan. <a href="<?php echo esc_url( home_url( '/sms-terms/' ) ); ?>">Text terms</a></span>
							</label>
							<p class="fine-print">By submitting, you agree that <?php echo esc_html( jb_opt( 'name' ) ); ?> and <?php echo esc_html( jb_opt( 'company' ) ); ?> may contact you by phone or email about your inquiry. Submitting this form is not a loan application, does not lock a rate, is not a commitment to lend and does not affect your credit. See our <a href="<?php echo esc_url( home_url( '/privacy-policy/' ) ); ?>">Privacy Policy</a> and <a href="<?php echo esc_url( home_url( '/terms-of-use/' ) ); ?>">Terms of Use</a>. NMLS #<?php echo esc_html( jb_opt( 'nmls' ) ); ?> · <?php echo esc_html( jb_opt( 'company' ) ); ?> NMLS #<?php echo esc_html( jb_opt( 'company_nmls' ) ); ?> · Equal Housing Opportunity Lender.</p>
						</div>
					<?php endif; ?>

					<div class="lead-nav">
						<?php if ( $s > 0 ) : ?>
							<button type="button" class="btn btn-ghost" data-prev>Back</button>
						<?php endif; ?>
						<?php if ( $s < $count - 1 ) : ?>
							<button type="button" class="btn btn-gold" data-next>Continue <?php echo jb_icon( 'arrow' ); ?></button>
						<?php else : ?>
							<button type="submit" class="btn btn-gold"><?php echo esc_html( $form['submit'] ); ?> <?php echo jb_icon( 'arrow' ); ?></button>
						<?php endif; ?>
					</div>
				</fieldset>
			<?php endforeach; ?>

			<p class="lead-error" role="alert" hidden></p>
		</form>

		<div class="lead-success" hidden tabindex="-1">
			<div class="lead-success-icon"><?php echo jb_icon( 'check' ); ?></div>
			<h3>Thanks — Joe has your details.</h3>
			<div class="lead-result" aria-live="polite"></div>
			<p>Joe personally reviews every request and will follow up with you directly. Prefer to talk now?</p>
			<div class="btn-row">
				<a class="btn btn-gold" href="tel:<?php echo esc_attr( jb_tel() ); ?>"><?php echo jb_icon( 'phone' ); ?> Call <?php echo esc_html( jb_opt( 'phone' ) ); ?></a>
				<a class="btn btn-ghost" href="sms:<?php echo esc_attr( jb_tel( 'sms' ) ); ?>"><?php echo jb_icon( 'message' ); ?> Text Joe</a>
			</div>
		</div>
	</div>
	<?php
	return ob_get_clean();
} );

function jb_render_field( $field, $uid ) {
	$field = array_pad( $field, 8, null );
	list( $name, $label, $type, $options, $required, $width, $autocomplete, $help ) = $field;
	$id    = $uid . '-' . $name;
	$req   = $required ? ' required' : '';
	$class = 'field field-' . $type . ( 'half' === $width ? ' field-half' : '' );
	$star  = $required ? ' <span class="req" aria-hidden="true">*</span>' : '';
	$help_id = $help ? $id . '-help' : '';
	$described = $help ? ' aria-describedby="' . esc_attr( $help_id ) . '"' : '';
	$help_html = $help ? '<span class="field-help" id="' . esc_attr( $help_id ) . '">' . esc_html( $help ) . '</span>' : '';

	ob_start();
	if ( in_array( $type, array( 'chips', 'cards' ), true ) ) {
		printf( '<fieldset class="%s"><legend class="field-label">%s%s</legend><div class="choice-group">', esc_attr( $class ), esc_html( $label ), $star );
		foreach ( (array) $options as $i => $opt ) {
			printf(
				'<label class="choice"><input type="radio" name="%s" value="%s"%s><span>%s</span></label>',
				esc_attr( $name ),
				esc_attr( $opt ),
				0 === $i ? $req : '',
				esc_html( $opt )
			);
		}
		echo '</div>' . $help_html . '</fieldset>'; // phpcs:ignore
		return ob_get_clean();
	}

	printf( '<div class="%s"><label class="field-label" for="%s">%s%s</label>', esc_attr( $class ), esc_attr( $id ), esc_html( $label ), $star );
	$ac = $autocomplete ? ' autocomplete="' . esc_attr( $autocomplete ) . '"' : '';
	switch ( $type ) {
		case 'select':
			printf( '<select id="%s" name="%s"%s%s><option value="">Select…</option>', esc_attr( $id ), esc_attr( $name ), $req, $described );
			foreach ( (array) $options as $opt ) {
				printf( '<option>%s</option>', esc_html( $opt ) );
			}
			echo '</select>';
			break;
		case 'textarea':
			printf( '<textarea id="%s" name="%s" rows="3"%s%s placeholder="%s"></textarea>', esc_attr( $id ), esc_attr( $name ), $req, $described, esc_attr( (string) $help ) );
			$help_html = '';
			break;
		case 'currency':
			printf( '<span class="input-prefix"><span aria-hidden="true">$</span><input id="%s" name="%s" type="text" inputmode="numeric" data-currency%s%s></span>', esc_attr( $id ), esc_attr( $name ), $req, $described );
			break;
		case 'number':
			printf( '<input id="%s" name="%s" type="text" inputmode="decimal"%s%s>', esc_attr( $id ), esc_attr( $name ), $req, $described );
			break;
		default:
			printf( '<input id="%s" name="%s" type="%s"%s%s%s>', esc_attr( $id ), esc_attr( $name ), esc_attr( $type ), $req, $ac, $described );
	}
	echo $help_html . '</div>'; // phpcs:ignore
	return ob_get_clean();
}

/* ---------------------------------------------------------------------------
 * Storage
 * ------------------------------------------------------------------------ */

add_action( 'init', function () {
	register_post_type( 'jb_lead', array(
		'labels'          => array(
			'name'          => 'Leads',
			'singular_name' => 'Lead',
			'menu_name'     => 'Leads',
			'all_items'     => 'All Leads',
		),
		'public'          => false,
		'show_ui'         => true,
		'show_in_menu'    => true,
		'show_in_rest'    => false,
		'menu_icon'       => 'dashicons-groups',
		'menu_position'   => 3,
		'supports'        => array( 'title' ),
		'capability_type' => 'post',
		'capabilities'    => array( 'create_posts' => 'do_not_allow' ),
		'map_meta_cap'    => true,
	) );
} );

// Show the submitted details read-only on the lead screen.
add_action( 'add_meta_boxes_jb_lead', function () {
	add_meta_box( 'jb-lead-details', 'Lead details', function ( $post ) {
		echo wp_kses_post( get_post_meta( $post->ID, '_jb_lead_html', true ) );
	}, 'jb_lead', 'normal', 'high' );
} );

add_filter( 'manage_jb_lead_posts_columns', function ( $cols ) {
	return array(
		'cb'      => $cols['cb'],
		'title'   => 'Lead',
		'jb_form' => 'Funnel',
		'jb_contact' => 'Contact',
		'date'    => 'Received',
	);
} );

add_action( 'manage_jb_lead_posts_custom_column', function ( $col, $post_id ) {
	$data = (array) get_post_meta( $post_id, '_jb_lead', true );
	if ( 'jb_form' === $col ) {
		echo esc_html( get_post_meta( $post_id, '_jb_form_label', true ) );
	} elseif ( 'jb_contact' === $col ) {
		echo esc_html( trim( ( $data['phone'] ?? '' ) . ' · ' . ( $data['email'] ?? '' ), ' ·' ) );
	}
}, 10, 2 );

/* ---------------------------------------------------------------------------
 * Submission
 * ------------------------------------------------------------------------ */

add_action( 'rest_api_init', function () {
	register_rest_route( 'jb/v1', '/lead', array(
		'methods'             => 'POST',
		'permission_callback' => '__return_true',
		'callback'            => function ( WP_REST_Request $request ) {
			$result = jb_process_lead( $request->get_body_params() ?: $request->get_json_params() );
			if ( is_wp_error( $result ) ) {
				return new WP_REST_Response( array( 'ok' => false, 'message' => $result->get_error_message() ), 400 );
			}
			return new WP_REST_Response( array( 'ok' => true, 'result' => $result ), 200 );
		},
	) );
} );

// No-JS fallback.
add_action( 'admin_post_nopriv_jb_lead', 'jb_lead_fallback' );
add_action( 'admin_post_jb_lead', 'jb_lead_fallback' );
function jb_lead_fallback() {
	$result = jb_process_lead( wp_unslash( $_POST ) ); // phpcs:ignore WordPress.Security.NonceVerification
	$back   = wp_get_referer() ? wp_get_referer() : home_url( '/' );
	wp_safe_redirect( add_query_arg( 'lead', is_wp_error( $result ) ? 'error' : 'thanks', $back ) );
	exit;
}

/**
 * Validate, store and email a lead. Returns the computed estimate (if any).
 *
 * @return array|WP_Error
 */
function jb_process_lead( $raw ) {
	$raw   = (array) $raw;
	$forms = jb_forms();
	$type  = isset( $raw['form_type'] ) ? sanitize_key( $raw['form_type'] ) : '';
	if ( ! isset( $forms[ $type ] ) ) {
		return new WP_Error( 'jb_form', 'Unknown form.' );
	}

	// Spam checks: honeypot, minimum fill time, per-IP rate limit.
	if ( ! empty( $raw['website'] ) ) {
		return array();
	}
	$ts = isset( $raw['jb_ts'] ) ? (int) base64_decode( (string) $raw['jb_ts'] ) : 0;
	if ( $ts && time() - $ts < 3 ) {
		return new WP_Error( 'jb_fast', 'Please take a moment to review your details and try again.' );
	}
	$ip_key = 'jb_rl_' . md5( $_SERVER['REMOTE_ADDR'] ?? '' );
	$hits   = (int) get_transient( $ip_key );
	if ( $hits >= 8 ) {
		return new WP_Error( 'jb_rate', 'We received several requests from you already. Please call or text Joe directly.' );
	}
	set_transient( $ip_key, $hits + 1, 15 * MINUTE_IN_SECONDS );

	// Collect only defined fields.
	$form   = $forms[ $type ];
	$data   = array();
	$labels = array();
	foreach ( $form['steps'] as $step ) {
		foreach ( $step['fields'] as $field ) {
			$name  = $field[0];
			$value = isset( $raw[ $name ] ) ? (string) $raw[ $name ] : '';
			$value = 'textarea' === $field[2] ? sanitize_textarea_field( $value ) : sanitize_text_field( $value );
			if ( 'email' === $field[2] ) {
				$value = sanitize_email( $value );
			}
			if ( ! empty( $field[4] ) && '' === $value ) {
				return new WP_Error( 'jb_required', sprintf( 'Please complete: %s', $field[1] ) );
			}
			$data[ $name ]   = $value;
			$labels[ $name ] = $field[1];
		}
	}
	if ( isset( $data['email'] ) && ! is_email( $data['email'] ) ) {
		return new WP_Error( 'jb_email', 'Please enter a valid email address.' );
	}
	if ( isset( $data['phone'] ) && strlen( preg_replace( '/\D/', '', $data['phone'] ) ) < 10 ) {
		return new WP_Error( 'jb_phone', 'Please enter a valid mobile number.' );
	}

	$data['sms_consent'] = ! empty( $raw['sms_consent'] ) ? 'Yes' : 'No';
	$labels['sms_consent'] = 'Text-message consent';
	$meta = array(
		'source_url' => esc_url_raw( (string) ( $raw['source_url'] ?? '' ) ),
		'utm'        => sanitize_text_field( (string) ( $raw['utm'] ?? '' ) ),
		'ip'         => sanitize_text_field( $_SERVER['REMOTE_ADDR'] ?? '' ),
		'user_agent' => sanitize_text_field( $_SERVER['HTTP_USER_AGENT'] ?? '' ),
		'submitted'  => current_time( 'mysql' ),
	);

	$result = jb_lead_estimate( $type, $data );
	$name   = trim( ( $data['first_name'] ?? '' ) . ' ' . ( $data['last_name'] ?? '' ) );

	// Readable summary used in the email and the admin screen.
	$rows = '';
	foreach ( $data as $key => $value ) {
		if ( '' === $value ) {
			continue;
		}
		$rows .= sprintf( '<tr><th style="text-align:left;padding:6px 12px 6px 0;vertical-align:top;color:#4a5568">%s</th><td style="padding:6px 0">%s</td></tr>', esc_html( $labels[ $key ] ?? $key ), nl2br( esc_html( $value ) ) );
	}
	if ( ! empty( $result['summary'] ) ) {
		$rows .= sprintf( '<tr><th style="text-align:left;padding:6px 12px 6px 0;color:#4a5568">Estimate shown to visitor</th><td style="padding:6px 0">%s</td></tr>', esc_html( $result['summary'] ) );
	}
	foreach ( array( 'source_url' => 'Submitted from', 'utm' => 'Campaign', 'submitted' => 'Received' ) as $key => $label ) {
		if ( $meta[ $key ] ) {
			$rows .= sprintf( '<tr><th style="text-align:left;padding:6px 12px 6px 0;color:#4a5568">%s</th><td style="padding:6px 0">%s</td></tr>', esc_html( $label ), esc_html( $meta[ $key ] ) );
		}
	}
	$html = '<table style="border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px">' . $rows . '</table>';

	$post_id = wp_insert_post( array(
		'post_type'   => 'jb_lead',
		'post_status' => 'private',
		'post_title'  => sprintf( '%s — %s', $form['label'], $name ? $name : 'Unknown' ),
	) );
	if ( $post_id && ! is_wp_error( $post_id ) ) {
		update_post_meta( $post_id, '_jb_lead', $data );
		update_post_meta( $post_id, '_jb_lead_meta', $meta );
		update_post_meta( $post_id, '_jb_lead_html', $html );
		update_post_meta( $post_id, '_jb_form_label', $form['label'] );
	}

	$to = array_filter( array_map( 'trim', explode( ',', jb_opt( 'lead_email' ) ) ), 'is_email' );
	if ( $to ) {
		$headers = array( 'Content-Type: text/html; charset=UTF-8' );
		if ( ! empty( $data['email'] ) ) {
			$headers[] = sprintf( 'Reply-To: %s <%s>', $name, $data['email'] );
		}
		$body  = '<p style="font-family:Arial,sans-serif;font-size:15px"><strong>New ' . esc_html( $form['label'] ) . ' request</strong></p>' . $html;
		$body .= '<p style="font-family:Arial,sans-serif;font-size:12px;color:#888">Stored in WordPress → Leads.</p>';
		wp_mail( $to, sprintf( 'New lead: %s — %s', $form['label'], $name ), $body, $headers );
	}

	return $result;
}

/**
 * Server-side twin of the estimate shown to the visitor (main.js), so the
 * email records exactly what the visitor saw.
 */
function jb_lead_estimate( $type, $data ) {
	$num = function ( $v ) {
		return (float) preg_replace( '/[^0-9.]/', '', (string) $v );
	};
	if ( 'buying-power' === $type ) {
		$income = $num( $data['income'] ?? 0 ) / 12;
		$debts  = $num( $data['debts'] ?? 0 );
		$down   = $num( $data['down_payment'] ?? 0 );
		if ( $income <= 0 ) {
			return array();
		}
		$r       = (float) jb_opt( 'rate_estimate' ) / 100 / 12;
		$factor  = $r > 0 ? $r / ( 1 - pow( 1 + $r, -360 ) ) : 1 / 360;
		$tax     = (float) jb_opt( 'tax_ins_pct' ) / 100 / 12;
		$price   = function ( $ratio ) use ( $income, $debts, $down, $factor, $tax ) {
			$payment = min( $income * ( $ratio - 0.08 ), $income * $ratio - $debts );
			if ( $payment <= 0 ) {
				return 0;
			}
			return max( 0, ( $payment + $down * $factor ) / ( $factor + $tax ) );
		};
		$low  = round( $price( 0.36 ) / 5000 ) * 5000;
		$high = round( $price( 0.45 ) / 5000 ) * 5000;
		return array(
			'low'     => $low,
			'high'    => $high,
			'summary' => sprintf( '$%s – $%s', number_format( $low ), number_format( $high ) ),
		);
	}
	if ( 'refinance' === $type ) {
		$value   = $num( $data['home_value'] ?? 0 );
		$balance = $num( $data['balance'] ?? 0 );
		$equity  = max( 0, $value * 0.8 - $balance );
		return array(
			'equity'  => round( $equity / 1000 ) * 1000,
			'summary' => sprintf( 'Up to ~$%s accessible equity at 80%% LTV', number_format( round( $equity / 1000 ) * 1000 ) ),
		);
	}
	return array();
}
