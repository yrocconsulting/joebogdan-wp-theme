/**
 * Joseph Bogdan MLO - front-end behavior.
 * Navigation, multi-step lead forms with instant estimates, lazy video.
 */
(function () {
	'use strict';

	var cfg = window.JB || {};
	var doc = document;
	var root = doc.documentElement;

	/* ---------------------------------------------------------------
	 * Header: shadow on scroll
	 * ------------------------------------------------------------- */
	var header = doc.getElementById('site-header');
	if (header) {
		var onScroll = function () {
			header.classList.toggle('is-scrolled', window.scrollY > 8);
		};
		window.addEventListener('scroll', onScroll, { passive: true });
		onScroll();
	}

	/* ---------------------------------------------------------------
	 * Mobile navigation + submenus
	 * ------------------------------------------------------------- */
	var toggle = doc.querySelector('.nav-toggle');
	var nav = doc.getElementById('primary-nav');

	function setNav(open) {
		doc.body.classList.toggle('nav-open', open);
		if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
	}
	if (toggle && nav) {
		toggle.addEventListener('click', function () {
			setNav(!doc.body.classList.contains('nav-open'));
		});
		doc.addEventListener('keydown', function (e) {
			if (e.key === 'Escape' && doc.body.classList.contains('nav-open')) {
				setNav(false);
				toggle.focus();
			}
		});
		doc.addEventListener('click', function (e) {
			if (doc.body.classList.contains('nav-open') && !nav.contains(e.target) && !toggle.contains(e.target)) {
				setNav(false);
			}
		});
	}

	// Add a toggle button to every parent menu item (works for both
	// assigned menus and the fallback menu).
	doc.querySelectorAll('.primary-nav .menu-item-has-children').forEach(function (item) {
		var link = item.querySelector(':scope > a');
		var sub = item.querySelector(':scope > .sub-menu');
		if (!link || !sub) return;
		var btn = doc.createElement('button');
		btn.type = 'button';
		btn.className = 'submenu-toggle';
		btn.setAttribute('aria-expanded', 'false');
		btn.setAttribute('aria-label', 'Show ' + link.textContent.trim() + ' menu');
		btn.innerHTML = '<svg class="icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>';
		link.after(btn);
		btn.addEventListener('click', function () {
			var open = !item.classList.contains('is-open');
			item.classList.toggle('is-open', open);
			btn.setAttribute('aria-expanded', open ? 'true' : 'false');
		});
		item.addEventListener('keydown', function (e) {
			if (e.key === 'Escape' && item.classList.contains('is-open')) {
				item.classList.remove('is-open');
				btn.setAttribute('aria-expanded', 'false');
				btn.focus();
			}
		});
	});

	/* ---------------------------------------------------------------
	 * Campaign attribution (first touch, per session)
	 * ------------------------------------------------------------- */
	var utm = '';
	try {
		var params = new URLSearchParams(window.location.search);
		var keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid'];
		var found = keys.filter(function (k) { return params.get(k); }).map(function (k) { return k + '=' + params.get(k); });
		if (found.length) sessionStorage.setItem('jb_utm', found.join('&'));
		if (!sessionStorage.getItem('jb_ref') && doc.referrer && doc.referrer.indexOf(location.host) === -1) {
			sessionStorage.setItem('jb_ref', doc.referrer);
		}
		utm = [sessionStorage.getItem('jb_utm'), sessionStorage.getItem('jb_ref') ? 'ref=' + sessionStorage.getItem('jb_ref') : '']
			.filter(Boolean).join(' | ');
	} catch (e) { /* storage unavailable */ }

	/* ---------------------------------------------------------------
	 * Lead forms
	 * ------------------------------------------------------------- */
	var money = function (n) {
		return '$' + Math.round(n).toLocaleString('en-US');
	};
	var num = function (v) {
		return parseFloat(String(v || '').replace(/[^0-9.]/g, '')) || 0;
	};

	// Mirrors jb_lead_estimate() in inc/leads.php.
	function estimate(type, data) {
		if (type === 'buying-power') {
			var income = num(data.income) / 12;
			var debts = num(data.debts);
			var down = num(data.down_payment);
			if (income <= 0) return null;
			var r = (cfg.rate || 6.75) / 100 / 12;
			var factor = r > 0 ? r / (1 - Math.pow(1 + r, -360)) : 1 / 360;
			var tax = (cfg.taxIns || 2.4) / 100 / 12;
			var price = function (ratio) {
				var payment = Math.min(income * (ratio - 0.08), income * ratio - debts);
				if (payment <= 0) return { price: 0, payment: 0 };
				return { price: Math.max(0, (payment + down * factor) / (factor + tax)), payment: payment };
			};
			var low = price(0.36), high = price(0.45);
			var round = function (n) { return Math.round(n / 5000) * 5000; };
			if (high.price <= 0) {
				return '<span class="result-label">Your next step</span><p class="result-sub">Based on what you entered, Joseph will want to talk through options with you directly. He’ll reach out shortly.</p>';
			}
			return '<span class="result-label">Estimated price range</span>' +
				'<span class="result-figure">' + money(round(low.price)) + ' - ' + money(round(high.price)) + '</span>' +
				'<p class="result-sub">Joseph will review your answers and follow up with the programs and options that fit your situation.</p>' +
				'<p class="result-note">General estimate based on your answers and typical assumptions for interest rates, Texas property taxes and insurance. It is not a loan offer, pre-approval or commitment to lend; actual terms depend on credit approval, underwriting and program availability.</p>';
		}
		if (type === 'refinance') {
			var equity = Math.max(0, num(data.home_value) * 0.8 - num(data.balance));
			return '<span class="result-label">Estimated accessible equity</span>' +
				'<span class="result-figure">Up to ' + money(Math.round(equity / 1000) * 1000) + '</span>' +
				'<p class="result-sub">Based on borrowing up to 80% of your estimated home value.</p>' +
				'<p class="result-note">General estimate only. Texas homestead cash-out rules, your credit, the appraised value and program availability determine actual options. Not a loan offer or commitment to lend.</p>';
		}
		return null;
	}

	function fieldWrap(el) {
		return el.closest('.field');
	}

	function clearError(wrap) {
		if (!wrap) return;
		wrap.classList.remove('has-error');
		var msg = wrap.querySelector('.field-error');
		if (msg) msg.remove();
		wrap.querySelectorAll('[aria-invalid]').forEach(function (i) { i.removeAttribute('aria-invalid'); });
	}

	function showError(wrap, text) {
		if (!wrap || wrap.classList.contains('has-error')) return;
		wrap.classList.add('has-error');
		var msg = doc.createElement('span');
		msg.className = 'field-error';
		msg.textContent = text;
		wrap.appendChild(msg);
		wrap.querySelectorAll('input, select, textarea').forEach(function (i) { i.setAttribute('aria-invalid', 'true'); });
	}

	function validateStep(step) {
		var firstBad = null;
		step.querySelectorAll('.field').forEach(clearError);
		step.querySelectorAll('[required]').forEach(function (input) {
			var wrap = fieldWrap(input);
			var ok;
			if (input.type === 'radio') {
				ok = !!step.querySelector('input[name="' + input.name + '"]:checked');
			} else if (input.type === 'email') {
				ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value.trim());
			} else if (input.type === 'tel') {
				ok = input.value.replace(/\D/g, '').length >= 10;
			} else {
				ok = input.value.trim() !== '';
			}
			if (!ok) {
				var label = wrap && wrap.querySelector('.field-label');
				var name = label ? label.textContent.replace('*', '').trim() : 'This field';
				showError(wrap, input.type === 'email' ? 'Please enter a valid email.' : input.type === 'tel' ? 'Please enter a 10-digit mobile number.' : name + ' is required.');
				if (!firstBad) firstBad = input;
			}
		});
		if (firstBad) {
			firstBad.focus({ preventScroll: true });
			firstBad.closest('.field').scrollIntoView({ behavior: 'smooth', block: 'center' });
			return false;
		}
		return true;
	}

	doc.querySelectorAll('.lead-form').forEach(function (box) {
		var form = box.querySelector('form');
		var steps = Array.prototype.slice.call(form.querySelectorAll('.lead-step'));
		var bars = box.querySelectorAll('.lead-progress span');
		var errorBox = form.querySelector('.lead-error');
		var success = box.querySelector('.lead-success');
		var type = box.getAttribute('data-form');
		var current = 0;

		var source = form.querySelector('[name="source_url"]');
		if (source) source.value = location.href.split('#')[0];
		var utmField = form.querySelector('[name="utm"]');
		if (utmField) utmField.value = utm;

		function go(index) {
			steps[current].hidden = true;
			current = index;
			steps[current].hidden = false;
			bars.forEach(function (bar, i) {
				bar.classList.toggle('is-active', i === current);
				bar.classList.toggle('is-done', i < current);
			});
			var title = steps[current].querySelector('.lead-step-title');
			var top = box.getBoundingClientRect().top;
			if (top < 0 || top > window.innerHeight * 0.6) {
				box.scrollIntoView({ behavior: 'smooth', block: 'start' });
			}
			var focusTarget = steps[current].querySelector('input:not([type=hidden]), select, textarea');
			if (focusTarget) focusTarget.focus({ preventScroll: true });
			else if (title) title.focus();
		}

		form.addEventListener('click', function (e) {
			if (e.target.closest('[data-next]')) {
				if (validateStep(steps[current])) go(current + 1);
			} else if (e.target.closest('[data-prev]')) {
				go(current - 1);
			}
		});

		form.addEventListener('change', function (e) {
			clearError(fieldWrap(e.target));
		});
		form.addEventListener('input', function (e) {
			var wrap = fieldWrap(e.target);
			if (wrap && wrap.classList.contains('has-error')) clearError(wrap);
			if (e.target.hasAttribute('data-currency')) {
				var digits = e.target.value.replace(/[^0-9]/g, '');
				e.target.value = digits ? parseInt(digits, 10).toLocaleString('en-US') : '';
			}
		});

		// Enter key advances instead of submitting early.
		form.addEventListener('keydown', function (e) {
			if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA' && current < steps.length - 1) {
				e.preventDefault();
				if (validateStep(steps[current])) go(current + 1);
			}
		});

		form.addEventListener('submit', function (e) {
			e.preventDefault();
			if (!validateStep(steps[current])) return;
			if (!window.fetch || !cfg.leadEndpoint) {
				form.submit();
				return;
			}
			var submit = form.querySelector('[type="submit"]');
			var label = submit.innerHTML;
			submit.disabled = true;
			submit.textContent = 'Sending…';
			errorBox.hidden = true;

			var data = new FormData(form);
			var plain = {};
			data.forEach(function (v, k) { plain[k] = v; });

			fetch(cfg.leadEndpoint, { method: 'POST', body: data, credentials: 'omit' })
				.then(function (res) {
					return res.json().then(function (body) { return { ok: res.ok, body: body }; });
				})
				.then(function (r) {
					if (!r.ok || !r.body || !r.body.ok) {
						throw new Error((r.body && r.body.message) || 'Something went wrong. Please call or text Joseph directly.');
					}
					var result = estimate(type, plain);
					if (result) success.querySelector('.lead-result').innerHTML = result;
					form.hidden = true;
					success.hidden = false;
					success.focus();
					box.scrollIntoView({ behavior: 'smooth', block: 'start' });
					if (window.dataLayer) window.dataLayer.push({ event: 'generate_lead', form_type: type });
					if (window.gtag) window.gtag('event', 'generate_lead', { form_type: type });
				})
				.catch(function (err) {
					errorBox.textContent = err.message;
					errorBox.hidden = false;
					submit.disabled = false;
					submit.innerHTML = label;
				});
		});
	});

	/* ---------------------------------------------------------------
	 * Lazy video (loads the player only on click)
	 * ------------------------------------------------------------- */
	doc.querySelectorAll('.video-embed').forEach(function (box) {
		var btn = box.querySelector('.video-play');
		if (!btn) return;
		btn.addEventListener('click', function () {
			var iframe = doc.createElement('iframe');
			iframe.src = box.getAttribute('data-embed');
			iframe.title = btn.textContent.trim() || 'Video';
			iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
			iframe.allowFullscreen = true;
			box.innerHTML = '';
			box.appendChild(iframe);
		});
	});

	root.classList.add('js');
})();
