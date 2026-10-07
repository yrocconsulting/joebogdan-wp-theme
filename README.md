# Joe Bogdan - Mortgage Loan Originator website

Custom WordPress theme and content for Joe Bogdan, Senior Loan Officer with CrossCountry Mortgage (NMLS #2795320). The site is built to generate leads: every page starts from the visitor's problem and leads to a funnel.

## Layout

| Path | What it is |
|---|---|
| `theme/joe-bogdan-mlo/` | The WordPress theme (classic PHP theme, block-editor content) |
| `tools/pages.py` | All page copy, written with the helpers in `tools/blocks.py` |
| `content/` | Generated block markup + `manifest.json` (pages, menus, categories). Regenerate with `python3 tools/build.py` |
| `deploy/sync.php` | Runs on the server via WP-CLI; creates/updates pages, menus and settings from `content/` |
| `.github/workflows/deploy-staging.yml` | On push: lint, rsync the theme to SiteGround, run the sync, smoke-test |

## Editing content

- **In WordPress** (recommended for day-to-day): edit pages, add pages, images, posts and menu items as usual. The sync never overwrites a page or menu edited in WordPress unless you run the deploy workflow manually with that slug in **force**.
- **In the repo**: edit `tools/pages.py`, run `python3 tools/build.py`, commit and push.

Business details (phone, NMLS, lead email, video URL, rate used for estimates) live in **Appearance → Joe Bogdan Settings**.

## Lead funnels

`[jb_form type="…"]` - `buying-power`, `self-employed`, `jumbo`, `refinance`, `investor`, `realtor-scenario`, `builder`, `ask-joe`.
Leads are emailed to the address in settings and stored under **Leads** in wp-admin.

## Other shortcodes

`[jb_hero]`, `[jb_intent]`, `[jb_trust]`, `[jb_process]`, `[jb_faq][jb_q q="…"]…[/jb_q][/jb_faq]` (emits FAQPage schema), `[jb_video]`, `[jb_contact_options]`, `[jb_latest]`, `[jb_cta]`, `[jb_photo]`, `[jb_disclosure]`, `[jb_opt key="…"]`, `[jb_todo]` (visible to editors only).

Block patterns are available in the editor under **Patterns → Joe Bogdan**.

## SEO / AI search

- JSON-LD graph: Person (with NMLS credential), FinancialService, lender Organization, WebPage + BreadcrumbList, Service (loan pages), Article (posts), FAQPage.
- Per-page search title/description in the editor sidebar ("Search & AI Snippet").
- `/llms.txt` generated from pages and posts, including Joe's external profiles.
- robots.txt explicitly allows search and AI assistant crawlers (when the site is public).
- IndexNow pings Bing and other engines when a page or post is published or updated (production only).
- Intro video: set URL, upload date and transcript in settings to get the player, a visible transcript and VideoObject schema.
- Profiles (LinkedIn, Facebook, Zillow, Experience.com, CrossCountry, Google) live in settings and feed schema `sameAs`.
- Checks: `python3 tools/seo_audit.py URL…` and `python3 tools/schema_validate.py schemaorg-current-https.jsonld URL…`.
- Staging deploys set "Discourage search engines". Production must deploy with `JB_ENV=production`.

## Before launch

- [ ] Compliance review of legal pages and disclosures (marked with editor notes)
- [ ] Joe confirms About-page story and Realtor availability wording
- [ ] Replace stock imagery with real photography; add intro video URL
- [ ] Confirm licensing statement against NMLS Consumer Access
- [ ] Switch lead email to Joe; set up SMTP for reliable delivery
- [ ] Deploy with `JB_ENV=production` so search engines can index
