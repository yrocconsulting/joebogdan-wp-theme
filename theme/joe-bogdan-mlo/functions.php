<?php
/**
 * Joe Bogdan MLO theme bootstrap.
 */

defined( 'ABSPATH' ) || exit;

define( 'JB_VERSION', '1.0.0' );
define( 'JB_DIR', get_template_directory() );
define( 'JB_URI', get_template_directory_uri() );

require JB_DIR . '/inc/settings.php';
require JB_DIR . '/inc/setup.php';
require JB_DIR . '/inc/template-tags.php';
require JB_DIR . '/inc/shortcodes.php';
require JB_DIR . '/inc/leads.php';
require JB_DIR . '/inc/seo.php';
require JB_DIR . '/inc/indexnow.php';
require JB_DIR . '/inc/patterns.php';
