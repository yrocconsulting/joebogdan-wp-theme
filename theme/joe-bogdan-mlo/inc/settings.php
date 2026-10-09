<?php
/**
 * Site-wide business details (Appearance → Joseph Bogdan Settings).
 *
 * Everything that appears in more than one place - phone, NMLS, disclosures,
 * lead routing - lives here so it is edited once.
 */

defined( 'ABSPATH' ) || exit;

function jb_settings_fields() {
	return array(
		'Identity'   => array(
			'name'         => array( 'Display name', 'Joseph Bogdan' ),
			'legal_name'   => array( 'Legal name (disclosures)', 'Joseph Henry Bogdan' ),
			'title'        => array( 'Title', 'Senior Loan Officer' ),
			'nmls'         => array( 'Individual NMLS #', '2795320' ),
			'company'      => array( 'Company', 'CrossCountry Mortgage, LLC' ),
			'company_nmls' => array( 'Company NMLS #', '3029' ),
			'branch_nmls'  => array( 'Branch NMLS #', '2083600' ),
			'licensing'    => array( 'Joseph’s licensing statement', 'Licensed as a mortgage loan originator in Texas' ),
			'company_license' => array( 'Company licensing statement', 'CrossCountry Mortgage, LLC is licensed in all 50 states' ),
			'company_url'  => array( 'Company website URL', 'https://crosscountrymortgage.com/' ),
			'company_licensing_url' => array( 'Company licensing & disclosures URL', 'https://crosscountrymortgage.com/mortgage/licensing-and-disclosures/' ),
		),
		'Contact'    => array(
			'phone'        => array( 'Phone (calls)', '(469) 324-4620' ),
			'sms'          => array( 'Mobile (texts)', '(972) 672-8624' ),
			'email'        => array( 'Public email', 'Joe.Bogdan@ccm.com' ),
			'street'       => array( 'Street address', '2201 Spinks Road, Suite 236' ),
			'city'         => array( 'City', 'Flower Mound' ),
			'region'       => array( 'State', 'TX' ),
			'postal'       => array( 'ZIP', '75022' ),
			'service_area' => array( 'Service area (comma separated)', 'Dallas, Fort Worth, Flower Mound, Southlake, Plano, Frisco, McKinney, Denton, Argyle, Granbury' ),
		),
		'Conversion' => array(
			'lead_email'    => array( 'Send leads to (comma separated)', 'Joe.Bogdan@ccm.com' ),
			'lead_bcc'      => array( 'BCC leads to (comma separated, optional)', '' ),
			'apply_url'     => array( 'CrossCountry online application URL', 'https://app.crosscountrymortgage.com/#/signup?referrerId=joseph.bogdan%40ccm.com' ),
			'calendar_url'  => array( 'Booking / calendar URL (optional)', '' ),
			'video_url'     => array( 'Intro video URL (YouTube/Vimeo, optional)', '' ),
			'video_title'   => array( 'Video title', 'Meet Joseph Bogdan, Senior Loan Officer' ),
			'video_date'    => array( 'Video upload date (YYYY-MM-DD)', '' ),
			'video_description' => array( 'Video description (one or two sentences)', 'Joseph Bogdan explains who he helps, how he approaches mortgage decisions and why buyers, business owners and Realtors call him.' ),
			'video_transcript'  => array( 'Video transcript (helps search and AI assistants)', '' ),
			'review_url'    => array( 'Google review link (optional)', '' ),
			'rate_estimate' => array( 'Rate used for buying-power estimates (%)', '6.75' ),
			'tax_ins_pct'   => array( 'Annual tax + insurance estimate (% of price)', '2.4' ),
		),
		'Profiles'   => array(
			'linkedin'  => array( 'LinkedIn URL', 'https://www.linkedin.com/in/joebogdan-ccm/' ),
			'facebook'  => array( 'Facebook URL', 'https://www.facebook.com/joebogdanCCM/' ),
			'instagram' => array( 'Instagram URL', '' ),
			'google'    => array( 'Google Business Profile URL', '' ),
			'ccm_url'   => array( 'CrossCountry profile URL', 'https://crosscountrymortgage.com/flower-mound-tx-3345/joseph-bogdan/' ),
			'zillow_url'     => array( 'Zillow lender profile URL', 'https://www.zillow.com/lender-profile/jhbogdan/' ),
			'experience_url' => array( 'Experience.com reviews URL', 'https://www.experience.com/reviews/joseph-bogdan-463145' ),
		),
	);
}

/**
 * Read a setting, falling back to the default above.
 */
function jb_opt( $key ) {
	static $saved = null;
	if ( null === $saved ) {
		$saved = (array) get_option( 'jb_settings', array() );
	}
	if ( isset( $saved[ $key ] ) && '' !== $saved[ $key ] ) {
		return $saved[ $key ];
	}
	foreach ( jb_settings_fields() as $fields ) {
		if ( isset( $fields[ $key ] ) ) {
			return $fields[ $key ][1];
		}
	}
	return '';
}

/** Digits-only phone for tel:/sms: links. */
/** E.164 phone number (+1XXXXXXXXXX) for tel:/sms: links. */
function jb_tel( $key = 'phone' ) {
	$digits = preg_replace( '/\D/', '', jb_opt( $key ) );
	if ( 10 === strlen( $digits ) ) {
		$digits = '1' . $digits;
	}
	return '+' . $digits;
}

add_action( 'admin_menu', function () {
	add_theme_page( 'Joseph Bogdan Settings', 'Joseph Bogdan Settings', 'manage_options', 'jb-settings', 'jb_render_settings_page' );
} );

add_action( 'admin_init', function () {
	register_setting( 'jb_settings', 'jb_settings', array(
		'type'              => 'array',
		'sanitize_callback' => function ( $input ) {
			$clean = array();
			foreach ( jb_settings_fields() as $fields ) {
				foreach ( $fields as $key => $def ) {
					$val = isset( $input[ $key ] ) ? trim( wp_unslash( $input[ $key ] ) ) : '';
					if ( 'video_transcript' === $key ) {
						$clean[ $key ] = sanitize_textarea_field( $val );
						continue;
					}
					$clean[ $key ] = preg_match( '/_url$|^(linkedin|facebook|instagram|google)$/', $key ) ? esc_url_raw( $val ) : sanitize_text_field( $val );
				}
			}
			return $clean;
		},
	) );
} );

function jb_render_settings_page() {
	$saved = (array) get_option( 'jb_settings', array() );
	?>
	<div class="wrap">
		<h1>Joseph Bogdan Settings</h1>
		<p>These details feed the header, footer, disclosures, structured data and lead forms. Leave a field blank to use the default shown.</p>
		<form method="post" action="options.php">
			<?php settings_fields( 'jb_settings' ); ?>
			<?php foreach ( jb_settings_fields() as $group => $fields ) : ?>
				<h2><?php echo esc_html( $group ); ?></h2>
				<table class="form-table" role="presentation">
					<?php foreach ( $fields as $key => $def ) : ?>
						<tr>
							<th scope="row"><label for="jb-<?php echo esc_attr( $key ); ?>"><?php echo esc_html( $def[0] ); ?></label></th>
							<td>
								<?php if ( 'video_transcript' === $key ) : ?>
									<textarea class="large-text" rows="6" id="jb-<?php echo esc_attr( $key ); ?>" name="jb_settings[<?php echo esc_attr( $key ); ?>]"><?php echo esc_textarea( $saved[ $key ] ?? '' ); ?></textarea>
								<?php else : ?>
									<input class="regular-text" id="jb-<?php echo esc_attr( $key ); ?>" name="jb_settings[<?php echo esc_attr( $key ); ?>]" value="<?php echo esc_attr( $saved[ $key ] ?? '' ); ?>" placeholder="<?php echo esc_attr( $def[1] ); ?>">
								<?php endif; ?>
							</td>
						</tr>
					<?php endforeach; ?>
				</table>
			<?php endforeach; ?>
			<?php submit_button(); ?>
		</form>
	</div>
	<?php
}
