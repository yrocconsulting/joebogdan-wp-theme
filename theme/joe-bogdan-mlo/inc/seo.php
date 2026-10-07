<?php
/**
 * Search and AI-search signals: titles, meta descriptions, Open Graph,
 * a connected JSON-LD entity graph, and /llms.txt.
 *
 * If a dedicated SEO plugin is activated later, the meta/OG output steps
 * aside automatically; the entity graph and llms.txt stay.
 */

defined( 'ABSPATH' ) || exit;

function jb_seo_plugin_active() {
	return defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'AIOSEO_VERSION' ) || defined( 'SEOPRESS_VERSION' );
}

/* ---------------------------------------------------------------------------
 * Per-page SEO fields (title + description), editable in the sidebar.
 * ------------------------------------------------------------------------ */

add_action( 'init', function () {
	foreach ( array( 'page', 'post' ) as $type ) {
		foreach ( array( '_jb_seo_title', '_jb_seo_description', '_jb_service', '_jb_audience' ) as $key ) {
			register_post_meta( $type, $key, array(
				'type'          => 'string',
				'single'        => true,
				'show_in_rest'  => true,
				'auth_callback' => function () {
					return current_user_can( 'edit_posts' );
				},
			) );
		}
	}
} );

add_action( 'add_meta_boxes', function () {
	foreach ( array( 'page', 'post' ) as $type ) {
		add_meta_box( 'jb-seo', 'Search & AI Snippet', 'jb_seo_metabox', $type, 'side', 'default' );
	}
} );

function jb_seo_metabox( $post ) {
	wp_nonce_field( 'jb_seo', 'jb_seo_nonce' );
	$title = get_post_meta( $post->ID, '_jb_seo_title', true );
	$desc  = get_post_meta( $post->ID, '_jb_seo_description', true );
	?>
	<p><label for="jb-seo-title"><strong>Search title</strong></label><br>
	<input type="text" id="jb-seo-title" name="jb_seo_title" value="<?php echo esc_attr( $title ); ?>" style="width:100%" placeholder="Defaults to the page title"></p>
	<p><label for="jb-seo-desc"><strong>Meta description</strong></label><br>
	<textarea id="jb-seo-desc" name="jb_seo_description" rows="4" style="width:100%" placeholder="One or two sentences that directly answer what this page helps with."><?php echo esc_textarea( $desc ); ?></textarea></p>
	<p class="description">Aim for 140–160 characters. Lead with the visitor’s problem.</p>
	<?php
}

add_action( 'save_post', function ( $post_id ) {
	if ( ! isset( $_POST['jb_seo_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['jb_seo_nonce'] ), 'jb_seo' ) ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	update_post_meta( $post_id, '_jb_seo_title', sanitize_text_field( wp_unslash( $_POST['jb_seo_title'] ?? '' ) ) );
	update_post_meta( $post_id, '_jb_seo_description', sanitize_textarea_field( wp_unslash( $_POST['jb_seo_description'] ?? '' ) ) );
} );

/* ---------------------------------------------------------------------------
 * Title + description
 * ------------------------------------------------------------------------ */

/** Post/page ID whose SEO fields apply to the current view (posts page included). */
function jb_seo_object_id() {
	if ( is_singular() ) {
		return get_queried_object_id();
	}
	if ( is_home() && get_option( 'page_for_posts' ) ) {
		return (int) get_option( 'page_for_posts' );
	}
	return 0;
}

/** Canonical URL of the current view, including pagination. */
function jb_current_url() {
	if ( is_singular() ) {
		return get_permalink();
	}
	if ( is_home() && get_option( 'page_for_posts' ) ) {
		$url = get_permalink( get_option( 'page_for_posts' ) );
	} elseif ( is_category() ) {
		$url = get_category_link( get_queried_object_id() );
	} else {
		$url = home_url( '/' );
	}
	$paged = (int) get_query_var( 'paged' );
	return $paged > 1 ? trailingslashit( $url ) . 'page/' . $paged . '/' : $url;
}

add_filter( 'document_title_parts', function ( $parts ) {
	if ( jb_seo_plugin_active() ) {
		return $parts;
	}
	$paged = (int) get_query_var( 'paged' );
	$suffix = $paged > 1 ? ' – Page ' . $paged : '';
	$id = jb_seo_object_id();
	if ( $id ) {
		$custom = get_post_meta( $id, '_jb_seo_title', true );
		if ( $custom ) {
			return array( 'title' => $custom . $suffix );
		}
	}
	if ( is_front_page() ) {
		return array( 'title' => sprintf( '%s | Mortgage Loan Officer, Flower Mound & North Texas', jb_opt( 'name' ) ) );
	}
	if ( is_category() ) {
		return array( 'title' => sprintf( '%s Mortgage Insights%s | %s', single_cat_title( '', false ), $suffix, jb_opt( 'name' ) ) );
	}
	$parts['site'] = jb_opt( 'name' );
	unset( $parts['tagline'] );
	return $parts;
} );

add_filter( 'document_title_separator', function () {
	return '|';
} );

function jb_meta_description() {
	$id = jb_seo_object_id();
	if ( $id ) {
		$desc = get_post_meta( $id, '_jb_seo_description', true );
		if ( ! $desc && has_excerpt( $id ) ) {
			$desc = get_the_excerpt( $id );
		}
		if ( ! $desc ) {
			$desc = wp_trim_words( wp_strip_all_tags( strip_shortcodes( get_post_field( 'post_content', $id ) ) ), 26, '…' );
		}
		return trim( preg_replace( '/\s+/', ' ', $desc ) );
	}
	if ( is_category() && category_description() ) {
		return trim( wp_strip_all_tags( category_description() ) );
	}
	return sprintf( '%s, %s with %s (NMLS #%s), helps North Texas buyers, business owners and investors finance strategically.', jb_opt( 'name' ), jb_opt( 'title' ), jb_opt( 'company' ), jb_opt( 'nmls' ) );
}

/** Image used for social sharing and primaryImageOfPage. */
function jb_page_image() {
	if ( is_singular() && has_post_thumbnail() ) {
		$src = wp_get_attachment_image_src( get_post_thumbnail_id(), 'jb-wide' );
		$alt = get_post_meta( get_post_thumbnail_id(), '_wp_attachment_image_alt', true );
		if ( $src ) {
			return array( 'url' => $src[0], 'width' => $src[1], 'height' => $src[2], 'alt' => $alt ? $alt : get_the_title() );
		}
	}
	return array( 'url' => jb_img( 'joe-headshot.webp' ), 'width' => 819, 'height' => 1024, 'alt' => jb_opt( 'name' ) . ', ' . jb_opt( 'title' ) );
}

add_action( 'wp_head', function () {
	if ( jb_seo_plugin_active() ) {
		return;
	}
	$desc  = jb_meta_description();
	$title = wp_get_document_title();
	$url   = jb_current_url();
	$image = jb_page_image();

	// WordPress prints canonicals for single posts/pages; cover listings too.
	if ( ! is_singular() && ( is_home() || is_category() ) ) {
		printf( '<link rel="canonical" href="%s">' . "\n", esc_url( $url ) );
	}
	printf( '<meta name="description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta property="og:locale" content="en_US">' . "\n" );
	printf( '<meta property="og:type" content="%s">' . "\n", is_singular( 'post' ) ? 'article' : 'website' );
	printf( '<meta property="og:site_name" content="%s">' . "\n", esc_attr( jb_opt( 'name' ) . ', ' . jb_opt( 'title' ) ) );
	printf( '<meta property="og:title" content="%s">' . "\n", esc_attr( $title ) );
	printf( '<meta property="og:description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta property="og:url" content="%s">' . "\n", esc_url( $url ) );
	printf( '<meta property="og:image" content="%s">' . "\n", esc_url( $image['url'] ) );
	printf( '<meta property="og:image:width" content="%d">' . "\n", (int) $image['width'] );
	printf( '<meta property="og:image:height" content="%d">' . "\n", (int) $image['height'] );
	printf( '<meta property="og:image:alt" content="%s">' . "\n", esc_attr( $image['alt'] ) );
	if ( is_singular( 'post' ) ) {
		printf( '<meta property="article:published_time" content="%s">' . "\n", esc_attr( get_the_date( 'c' ) ) );
		printf( '<meta property="article:modified_time" content="%s">' . "\n", esc_attr( get_the_modified_date( 'c' ) ) );
		foreach ( get_the_category() as $cat ) {
			printf( '<meta property="article:section" content="%s">' . "\n", esc_attr( $cat->name ) );
		}
	}
	echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
	printf( '<meta name="twitter:title" content="%s">' . "\n", esc_attr( $title ) );
	printf( '<meta name="twitter:description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta name="twitter:image" content="%s">' . "\n", esc_url( $image['url'] ) );
}, 2 );

// Thin pages stay out of the index.
add_filter( 'wp_robots', function ( $robots ) {
	if ( is_search() || is_404() || is_singular( 'jb_lead' ) ) {
		$robots['noindex'] = true;
		$robots['follow']  = true;
	}
	return $robots;
} );

/* ---------------------------------------------------------------------------
 * JSON-LD entity graph (printed in the footer so FAQ items rendered by the
 * page content can be included).
 * ------------------------------------------------------------------------ */

function jb_schema_ids() {
	$home = trailingslashit( home_url() );
	return array(
		'site'     => $home . '#website',
		'person'   => $home . '#joe-bogdan',
		'practice' => $home . '#mortgage-practice',
		'lender'   => $home . '#crosscountry-mortgage',
	);
}

/** Published pages that describe a service (have a _jb_service value). */
function jb_service_pages() {
	return get_posts( array(
		'post_type'   => 'page',
		'numberposts' => 30,
		'meta_key'    => '_jb_service',
		'meta_compare'=> '!=',
		'meta_value'  => '',
		'orderby'     => 'menu_order',
		'order'       => 'ASC',
	) );
}

function jb_schema_graph() {
	$ids   = jb_schema_ids();
	$nmls  = jb_opt( 'nmls' );
	$url   = jb_current_url();
	$areas = array_map( function ( $city ) {
		return array( '@type' => 'City', 'name' => trim( $city ) . ', TX' );
	}, array_filter( explode( ',', jb_opt( 'service_area' ) ) ) );
	$areas[] = array( '@type' => 'State', 'name' => 'Texas' );

	$same_as = array_values( array_filter( array(
		'https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/' . rawurlencode( $nmls ),
		jb_opt( 'linkedin' ),
		jb_opt( 'facebook' ),
		jb_opt( 'instagram' ),
		jb_opt( 'google' ),
		jb_opt( 'ccm_url' ),
	) ) );

	$address = array(
		'@type'           => 'PostalAddress',
		'streetAddress'   => jb_opt( 'street' ),
		'addressLocality' => jb_opt( 'city' ),
		'addressRegion'   => jb_opt( 'region' ),
		'postalCode'      => jb_opt( 'postal' ),
		'addressCountry'  => 'US',
	);

	$contact_points = array(
		array(
			'@type'             => 'ContactPoint',
			'contactType'       => 'customer service',
			'telephone'         => jb_opt( 'phone' ),
			'email'             => jb_opt( 'email' ),
			'areaServed'        => 'US-TX',
			'availableLanguage' => 'English',
		),
		array(
			'@type'             => 'ContactPoint',
			'contactType'       => 'mobile and text messages',
			'telephone'         => jb_opt( 'sms' ),
			'areaServed'        => 'US-TX',
			'availableLanguage' => 'English',
		),
	);

	$knows = array( 'Mortgage pre-approval', 'Home purchase financing', 'Mortgage refinancing', 'Home equity', 'Jumbo loans', 'Luxury home financing', 'Self-employed mortgages', 'Bank statement loans', 'Investment property loans', 'DSCR loans', 'New construction financing', 'FHA loans', 'VA loans', 'Conventional loans', 'Non-QM loans', 'Adjustable-rate mortgages', 'Down payment assistance', 'First-time homebuyers', 'Texas property taxes' );

	$catalog = array();
	foreach ( jb_service_pages() as $svc ) {
		$catalog[] = array(
			'@type'       => 'Offer',
			'itemOffered' => array( '@id' => get_permalink( $svc ) . '#service' ),
		);
	}

	$headshot = array(
		'@type'      => 'ImageObject',
		'@id'        => trailingslashit( home_url() ) . '#joe-headshot',
		'url'        => jb_img( 'joe-headshot.webp' ),
		'width'      => 819,
		'height'     => 1024,
		'caption'    => jb_opt( 'name' ) . ', ' . jb_opt( 'title' ),
	);

	$practice = array(
		'@type'                     => array( 'FinancialService', 'LocalBusiness' ),
		'@id'                       => $ids['practice'],
		'name'                      => jb_opt( 'name' ) . ' — ' . jb_opt( 'title' ) . ', ' . jb_opt( 'company' ),
		'description'               => sprintf( 'Mortgage lending for home buyers, homeowners, self-employed borrowers, real estate investors and luxury buyers in North Texas, plus a lending partnership for Realtors and home builders. %s.', jb_opt( 'licensing' ) ),
		'url'                       => home_url( '/' ),
		'image'                     => array( '@id' => $headshot['@id'] ),
		'telephone'                 => jb_opt( 'phone' ),
		'email'                     => jb_opt( 'email' ),
		'address'                   => $address,
		'areaServed'                => $areas,
		'contactPoint'              => $contact_points,
		'openingHoursSpecification' => array(
			'@type'     => 'OpeningHoursSpecification',
			'dayOfWeek' => array( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' ),
			'opens'     => '08:00',
			'closes'    => '17:00',
		),
		'employee'                  => array( '@id' => $ids['person'] ),
		'parentOrganization'        => array( '@id' => $ids['lender'] ),
		'knowsAbout'                => $knows,
		'sameAs'                    => array_values( array_filter( array( jb_opt( 'google' ) ) ) ),
	);
	if ( $catalog ) {
		$practice['hasOfferCatalog'] = array(
			'@type'           => 'OfferCatalog',
			'name'            => 'Mortgage services',
			'itemListElement' => $catalog,
		);
	}
	if ( ! $practice['sameAs'] ) {
		unset( $practice['sameAs'] );
	}

	$graph = array(
		array(
			'@type'       => 'WebSite',
			'@id'         => $ids['site'],
			'url'         => home_url( '/' ),
			'name'        => jb_opt( 'name' ) . ', ' . jb_opt( 'title' ),
			'description' => 'Mortgage strategy and lending in North Texas from ' . jb_opt( 'name' ) . ', ' . jb_opt( 'title' ) . ' with ' . jb_opt( 'company' ) . '.',
			'publisher'   => array( '@id' => $ids['person'] ),
			'about'       => array( '@id' => $ids['person'] ),
			'inLanguage'  => 'en-US',
		),
		array(
			'@type'       => 'Organization',
			'@id'         => $ids['lender'],
			'name'        => jb_opt( 'company' ),
			'url'         => jb_opt( 'company_url' ),
			'description' => jb_opt( 'company_license' ) . '.',
			'identifier'  => array( '@type' => 'PropertyValue', 'propertyID' => 'NMLS', 'value' => jb_opt( 'company_nmls' ) ),
			'sameAs'      => array( 'https://www.nmlsconsumeraccess.org/EntityDetails.aspx/COMPANY/' . rawurlencode( jb_opt( 'company_nmls' ) ) ),
		),
		$headshot,
		array(
			'@type'          => 'Person',
			'@id'            => $ids['person'],
			'name'           => jb_opt( 'name' ),
			'alternateName'  => jb_opt( 'legal_name' ),
			'givenName'      => 'Joe',
			'familyName'     => 'Bogdan',
			'jobTitle'       => jb_opt( 'title' ),
			'description'    => sprintf( '%s is a %s with %s (NMLS #%s), licensed as a mortgage loan originator in Texas. Before mortgage lending he spent more than 30 years as a business owner and CEO, including over two decades building medical businesses focused on outpatient diagnostic services. He helps home buyers, self-employed borrowers, investors and luxury buyers finance strategically and partners with Realtors and builders across North Texas.', jb_opt( 'name' ), jb_opt( 'title' ), jb_opt( 'company' ), $nmls ),
			'url'            => home_url( '/about-joe/' ),
			'image'          => array( '@id' => $headshot['@id'] ),
			'telephone'      => jb_opt( 'phone' ),
			'email'          => jb_opt( 'email' ),
			'contactPoint'   => $contact_points,
			'worksFor'       => array( '@id' => $ids['lender'] ),
			'workLocation'   => array( '@id' => $ids['practice'] ),
			'identifier'     => array( '@type' => 'PropertyValue', 'propertyID' => 'NMLS', 'value' => $nmls ),
			'hasCredential'  => array(
				'@type'              => 'EducationalOccupationalCredential',
				'credentialCategory' => 'license',
				'name'               => 'Texas Residential Mortgage Loan Originator License (NMLS #' . $nmls . ')',
				'recognizedBy'       => array( '@type' => 'GovernmentOrganization', 'name' => 'Texas Department of Savings and Mortgage Lending', 'url' => 'https://www.sml.texas.gov/' ),
			),
			'hasOccupation'  => array(
				'@type'                 => 'Occupation',
				'name'                  => 'Mortgage Loan Originator',
				'occupationLocation'    => array( '@type' => 'State', 'name' => 'Texas' ),
				'occupationalCategory'  => '13-2072.00',
			),
			'knowsAbout'     => $knows,
			'knowsLanguage'  => 'English',
			'sameAs'         => $same_as,
		),
		$practice,
	);

	// The current page.
	$crumbs = jb_breadcrumb_items();
	$image  = jb_page_image();
	$type   = 'WebPage';
	if ( is_page( 'about-joe' ) ) {
		$type = 'ProfilePage';
	} elseif ( is_page( 'contact' ) ) {
		$type = 'ContactPage';
	} elseif ( is_home() || is_category() || ( is_page() && get_pages( array( 'parent' => get_queried_object_id(), 'number' => 1 ) ) ) ) {
		$type = 'CollectionPage';
	}

	$page = array(
		'@type'              => $type,
		'@id'                => $url . '#webpage',
		'url'                => $url,
		'name'               => wp_get_document_title(),
		'description'        => jb_meta_description(),
		'isPartOf'           => array( '@id' => $ids['site'] ),
		'about'              => array( '@id' => is_page( 'about-joe' ) ? $ids['person'] : $ids['practice'] ),
		'primaryImageOfPage' => array( '@type' => 'ImageObject', 'url' => $image['url'], 'width' => $image['width'], 'height' => $image['height'] ),
		'inLanguage'         => 'en-US',
	);
	if ( is_page( 'about-joe' ) ) {
		$page['mainEntity'] = array( '@id' => $ids['person'] );
	} elseif ( is_page( 'contact' ) ) {
		$page['mainEntity'] = array( '@id' => $ids['practice'] );
	}
	if ( is_singular() ) {
		$page['datePublished'] = get_the_date( 'c' );
		$page['dateModified']  = get_the_modified_date( 'c' );
	}
	if ( count( $crumbs ) > 1 ) {
		$page['breadcrumb'] = array(
			'@type'           => 'BreadcrumbList',
			'@id'             => $url . '#breadcrumb',
			'itemListElement' => array_map( function ( $item, $i ) {
				return array( '@type' => 'ListItem', 'position' => $i + 1, 'name' => $item['name'], 'item' => $item['url'] );
			}, $crumbs, array_keys( $crumbs ) ),
		);
	}

	// Listings: describe the items on the page.
	if ( 'CollectionPage' === $type ) {
		$items = array();
		if ( is_page() ) {
			foreach ( get_pages( array( 'parent' => get_queried_object_id(), 'sort_column' => 'menu_order' ) ) as $child ) {
				$items[] = array( 'url' => get_permalink( $child ), 'name' => $child->post_title );
			}
		} else {
			foreach ( $GLOBALS['wp_query']->posts as $listed ) {
				$items[] = array( 'url' => get_permalink( $listed ), 'name' => get_the_title( $listed ) );
			}
		}
		$page['mainEntity'] = array(
			'@type'           => 'ItemList',
			'numberOfItems'   => count( $items ),
			'itemListElement' => array_map( function ( $item, $i ) {
				return array( '@type' => 'ListItem', 'position' => $i + 1, 'url' => $item['url'], 'name' => $item['name'] );
			}, $items, array_keys( $items ) ),
		);
	}
	$graph[] = $page;

	if ( is_singular( 'post' ) ) {
		$content = get_post_field( 'post_content', get_the_ID() );
		$graph[] = array(
			'@type'            => 'Article',
			'@id'              => $url . '#article',
			'headline'         => get_the_title(),
			'description'      => jb_meta_description(),
			'datePublished'    => get_the_date( 'c' ),
			'dateModified'     => get_the_modified_date( 'c' ),
			'author'           => array( '@id' => $ids['person'] ),
			'publisher'        => array( '@id' => $ids['person'] ),
			'isPartOf'         => array( '@id' => $url . '#webpage' ),
			'mainEntityOfPage' => array( '@id' => $url . '#webpage' ),
			'image'            => array( '@type' => 'ImageObject', 'url' => $image['url'], 'width' => $image['width'], 'height' => $image['height'] ),
			'articleSection'   => wp_list_pluck( get_the_category(), 'name' ),
			'about'            => array( '@id' => $ids['practice'] ),
			'wordCount'        => str_word_count( wp_strip_all_tags( strip_shortcodes( $content ) ) ),
			'inLanguage'       => 'en-US',
		);
	}

	$service = is_page() ? get_post_meta( get_queried_object_id(), '_jb_service', true ) : '';
	if ( $service ) {
		$node = array(
			'@type'            => 'Service',
			'@id'              => $url . '#service',
			'name'             => $service,
			'serviceType'      => $service,
			'category'         => 'Mortgage lending',
			'description'      => jb_meta_description(),
			'provider'         => array( '@id' => $ids['person'] ),
			'areaServed'       => $areas,
			'url'              => $url,
			'availableChannel' => array(
				'@type'        => 'ServiceChannel',
				'serviceUrl'   => $url,
				'servicePhone' => array( '@type' => 'ContactPoint', 'telephone' => jb_opt( 'phone' ), 'contactType' => 'customer service' ),
			),
		);
		$audience = get_post_meta( get_queried_object_id(), '_jb_audience', true );
		if ( $audience ) {
			$node['audience'] = array( '@type' => 'Audience', 'audienceType' => $audience );
		}
		$graph[] = $node;
	}

	if ( ! empty( $GLOBALS['jb_faq_items'] ) ) {
		$graph[] = array(
			'@type'      => 'FAQPage',
			'@id'        => $url . '#faq',
			'isPartOf'   => array( '@id' => $url . '#webpage' ),
			'mainEntity' => array_map( function ( $item ) {
				return array(
					'@type'          => 'Question',
					'name'           => $item['q'],
					'acceptedAnswer' => array( '@type' => 'Answer', 'text' => trim( preg_replace( '/\s+/', ' ', $item['a'] ) ) ),
				);
			}, $GLOBALS['jb_faq_items'] ),
		);
	}

	return array( '@context' => 'https://schema.org', '@graph' => $graph );
}

add_action( 'wp_footer', function () {
	if ( is_404() || is_search() ) {
		return;
	}
	echo '<script type="application/ld+json">' . wp_json_encode( jb_schema_graph(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}, 5 );

/* ---------------------------------------------------------------------------
 * /llms.txt — a plain-language map of the site for AI assistants.
 * ------------------------------------------------------------------------ */

add_action( 'init', function () {
	add_rewrite_rule( '^llms\.txt$', 'index.php?jb_llms=1', 'top' );
} );

add_filter( 'query_vars', function ( $vars ) {
	$vars[] = 'jb_llms';
	return $vars;
} );

add_filter( 'redirect_canonical', function ( $redirect ) {
	return get_query_var( 'jb_llms' ) ? false : $redirect;
} );

add_action( 'template_redirect', function () {
	if ( ! get_query_var( 'jb_llms' ) ) {
		return;
	}
	header( 'Content-Type: text/plain; charset=utf-8' );
	header( 'X-Robots-Tag: noindex' );

	$line = function ( $page ) {
		$desc = get_post_meta( $page->ID, '_jb_seo_description', true );
		return sprintf( '- [%s](%s)%s', $page->post_title, get_permalink( $page ), $desc ? ': ' . $desc : '' );
	};

	$out   = array();
	$out[] = '# ' . jb_opt( 'name' ) . ', ' . jb_opt( 'title' );
	$out[] = '';
	$out[] = sprintf( '> %s is a %s with %s (individual NMLS #%s; company NMLS #%s), based in %s, %s and serving North Texas. %s; %s. He helps home buyers, self-employed borrowers and business owners, real estate investors and luxury/jumbo buyers structure mortgage financing, and partners with Realtors and home builders. He is a mortgage loan originator only and does not provide real estate brokerage services.', jb_opt( 'name' ), jb_opt( 'title' ), jb_opt( 'company' ), jb_opt( 'nmls' ), jb_opt( 'company_nmls' ), jb_opt( 'city' ), jb_opt( 'region' ), jb_opt( 'licensing' ), jb_opt( 'company_license' ) );
	$out[] = '';
	$out[] = sprintf( 'Contact: call %s · text %s · %s · %s, %s, %s %s', jb_opt( 'phone' ), jb_opt( 'sms' ), jb_opt( 'email' ), jb_opt( 'street' ), jb_opt( 'city' ), jb_opt( 'region' ), jb_opt( 'postal' ) );
	$out[] = sprintf( 'Verify license: https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/%s', jb_opt( 'nmls' ) );
	$out[] = '';

	$pages = get_pages( array( 'sort_column' => 'menu_order,post_title' ) );
	$legal = array( 'privacy-policy', 'terms-of-use', 'sms-terms', 'accessibility', 'licensing-disclosures', 'texas-consumer-notice' );
	$out[] = '## Pages';
	foreach ( $pages as $page ) {
		if ( ! in_array( $page->post_name, $legal, true ) ) {
			$out[] = $line( $page );
		}
	}

	$posts = get_posts( array( 'numberposts' => 50 ) );
	if ( $posts ) {
		$out[] = '';
		$out[] = '## Insights';
		foreach ( $posts as $post ) {
			$out[] = sprintf( '- [%s](%s): %s', $post->post_title, get_permalink( $post ), wp_strip_all_tags( get_the_excerpt( $post ) ) );
		}
	}

	$out[] = '';
	$out[] = '## Optional';
	foreach ( $pages as $page ) {
		if ( in_array( $page->post_name, $legal, true ) ) {
			$out[] = $line( $page );
		}
	}

	echo implode( "\n", $out ) . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput
	exit;
} );

// Keep usernames out of the public sitemap.
add_filter( 'wp_sitemaps_add_provider', function ( $provider, $name ) {
	return 'users' === $name ? false : $provider;
}, 10, 2 );
