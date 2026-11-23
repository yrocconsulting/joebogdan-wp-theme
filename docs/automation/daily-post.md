# Daily Insights post (weekdays, auto-published)

A scheduled task runs this procedure Monday-Friday at about 10 AM Central and
publishes one new article to https://josephbogdan.com/insights/ under Joseph
Bogdan's name. There is no human review before it goes live, so every rule
below is mandatory. If a rule cannot be met, do not publish that day.

Repository: `yrocconsulting/joebogdan-wp-theme`, branch
`claude/wordpress-custom-theme-k0hq9k`. Facts about Joseph, approved wording
and CTAs: `docs/claude-project/2-site-facts.md`. Already-published topics:
`docs/claude-project/3-published-articles.md` and `tools/daily/`.

## 1. Pick today's topic

Weekday focus (Central Time date):

| Day | Focus | Category slug(s) |
|---|---|---|
| Monday | North Texas / Texas housing and mortgage-market trends | `texas-housing-market`, `mortgage-strategy` |
| Tuesday | Home buyers: first-time, move-up, FHA, VA, down payment assistance, buying before selling | `home-buying` |
| Wednesday | Builders and new construction (priority audience) | `builders-new-construction` |
| Thursday | Rotate: self-employed and business owners, investors and DSCR, luxury and jumbo | `business-owners`, `real-estate-investing`, `luxury-jumbo` |
| Friday | Rotate: construction and land loans, refinance and home equity | `construction-land`, `mortgage-strategy` |

Then research what is happening **now**: run several WebSearch queries (mode
"standard"; "extended" only if results are thin) for news and data from the
last 14 days on that focus, for example housing starts, builder sentiment,
existing-home sales and inventory, Texas and DFW market reports, rate
direction, FHFA/HUD/VA/CFPB rule or limit changes, property tax and insurance
news in Texas. Prefer primary sources: Freddie Mac, Fannie Mae ESR, MBA, NAR,
NAHB, U.S. Census Bureau, FHFA, HUD, VA, CFPB, Texas A&M Texas Real Estate
Research Center, Texas Comptroller, Texas Department of Insurance, HAR/NTREIS
market reports and major news outlets.

Choose a topic that:
- ties a current development to a practical question a reader in North Texas
  would actually ask, and answers it;
- is **not** already covered by a published title (check the list and the
  slugs in `tools/daily/`). A new angle on a covered subject is fine only if
  the news makes it genuinely new; then link to the older article;
- fits programs Joseph offers in Texas (see site facts). Do not write about
  products not listed there (for example reverse mortgages, USDA, commercial
  loans, HELOC specifics) unless the site facts list them.

## 2. Write the article

Create `tools/daily/YYYY-MM-DD-<slug>.py` (today's Central date). It calls
`post()` once, exactly like the articles in `tools/posts.py`:

```python
post(
    "<slug>",                      # lowercase-hyphenated, unique, no date in it
    "<Title as a question or clear promise>",
    "<category-slug>",
    "<excerpt / meta description: 110-165 characters, answers the question>",
    "<SEO title: 30-65 characters>",
    "<image file from theme/joe-bogdan-mlo/assets/images>",
    body(
        lead("<2-4 sentence direct answer, with the month and year for anything time-sensitive>"),
        takeaways([...4-5 bullets...]),
        h("<question-style H2>"),
        p("..."),
        ...,
        <the category's CTA constant, placed mid-article>,
        ...,
        p("Related: <a href=\"/existing-url/\">...</a> ..."),
        faq([(q, a), (q, a), (q, a)]),
        sources([("Publisher: report or article title", "https://...")]),
    ),
)
```

Helpers available: `lead, takeaways, h, p, ul, ol, faq, cta, body, sources`
and the CTA constants `BUYING_POWER_CTA`, `BUILDER_CTA`, `BUILDER_SCENARIO_CTA`,
`CONSTRUCTION_CTA`, `FORWARD_CTA` (or build one with `cta(...)` pointing at a
URL from the site facts).

Images: use one that suits the audience and was not used by the previous
three daily posts. Builder or construction topics: `feat-joseph-model-home-a/b/c.webp`,
`feat-joseph-national-mall.webp`. Buyers: `buyers.webp`. Business owners:
`business-owners.webp`. Luxury: `luxury.webp`. Market and strategy: `strategy.webp`.

Quality bar (Google and AI assistants reward this; thin daily content hurts the site):
- 700-1,100 words of original writing. Explain what changed, why it matters in
  North Texas, and what the reader should do. No filler or generic intros.
- Every statistic or claim about the news is attributed in the text
  ("according to the Census Bureau's October report") and listed in Sources
  with a working link. Never invent numbers, quotes, studies or sources.
- Plain language, short paragraphs, question-style H2s, a takeaways box, and
  an FAQ with 3 questions (emits FAQPage schema).
- At least two internal links to existing pages or articles that exist in
  `content/manifest.json`.
- Use "Joseph" (never "Joe" in body copy). Joseph is a loan officer only: no
  real-estate advice, no legal or tax advice beyond "talk with your CPA or
  attorney". No first-person claims, anecdotes, client stories or quotes
  attributed to Joseph. Only the approved background wording.

## 3. Compliance (mandatory; `tools/build.py` enforces part of it)

- No interest rates, APRs, payment amounts, down-payment amounts or
  percentages, or "no down payment" claims, even as market averages. Describe
  direction instead ("average 30-year rates eased this week, according to
  Freddie Mac"). Home-price, sales, inventory, starts and similar non-credit
  statistics are fine with attribution.
- No guarantees, "lowest/best rates", approval-speed promises, or statements
  that anyone will qualify. Use "may", "often", "depending on the program".
- Programs are "subject to credit approval" and eligibility; say so when
  describing a program.
- Never mention or link joebogdan.com. Do not mention competitors by name.
- No em dashes (use a hyphen or rewrite).
- Fair lending: nothing that targets or discourages any group by a
  protected characteristic.

## 4. Build, check and publish

1. `python3 tools/build.py` must print `wrote N pages, M posts` with no
   errors. If a compliance or length check fails, fix the copy. Never edit
   the checks to get a pass.
2. Re-read the generated `content/posts/<slug>.html` once, adversarially,
   against sections 2 and 3. Check every internal link exists in the
   manifest and every source URL was actually found in today's research.
3. Add a row to the table in `docs/claude-project/3-published-articles.md`.
4. Commit (`Daily post: <title>`) and push to the branch. The push deploys to
   staging automatically.
5. Run the `deploy-production.yml` workflow on the same branch with inputs
   `search_visibility=on`, `indexnow_all=false`, `force=` (empty). The deploy
   publishes the post and submits it to IndexNow.
6. Confirm `https://josephbogdan.com/<slug>/` returns 200 (allow a few
   minutes). If the deploy fails, read its log and fix only what this post
   caused; never force-overwrite (`force`) anything.
7. End with a short summary: title, URL, category, the news it was based
   on, and sources.

If anything blocks publishing (no defensible topic, research tools failing,
checks you cannot satisfy, deploy failing for reasons outside this post), do
not publish a weaker article. Commit nothing, and explain what blocked it in
the final summary.
