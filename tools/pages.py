"""Page copy for joebogdanlo. Run `python3 tools/build.py` to regenerate content/.

Copy rules (from the conversion brief):
- Lead with the visitor's problem; products support the answer.
- Every section builds trust, names a problem, gives value or moves to action.
- Joseph is a Mortgage Loan Originator only: no real-estate representation language.
- No manufactured social proof, no rate promises, no "guaranteed" approvals.
"""
from blocks import (button, buttons, card, cards, faq, form_section, group, h, head, ol, p, page, sc,
                    section, split, ul)

PREAPPROVE = "/get-pre-approved/"
CONTACT = "/contact/"

# ---------------------------------------------------------------------------
# Shared FAQ answers
# ---------------------------------------------------------------------------
FAQ_CREDIT = ("What credit score do I need for a mortgage?",
              "It depends on the program. FHA financing generally allows lower scores than conventional loans, while jumbo loans usually expect stronger credit. Your score is one factor alongside income, assets and debts, so the most useful next step is a quick review of your full picture.")
FAQ_TIMELINE = ("How long does the mortgage process take?",
                "It depends on the loan program, the property and how quickly documents come in. New construction, jumbo and self-employed files often involve extra steps. Joseph maps out a realistic timeline with you up front so there are no surprises.")
FAQ_NMLS = ("Is Joseph Bogdan licensed?",
            "Yes. Joseph Bogdan is a Senior Loan Officer licensed as a mortgage loan originator in Texas (NMLS #2795320) with CrossCountry Mortgage, LLC (NMLS #3029). You can verify his license at nmlsconsumeraccess.org.")
FAQ_REALTOR = ("Is Joseph a real estate agent?",
               "No. Joseph is a mortgage loan originator only. He does not represent buyers or sellers in real estate transactions, so he works alongside your Realtor - never in competition with them.")
FAQ_CREDIT_PULL = ("Will requesting an analysis affect my credit?",
                   "No. The buying-power analysis and scenario reviews on this site do not pull your credit. If you decide to move forward with a full pre-approval, Joseph will explain exactly when and why a credit check happens first.")

# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
home = page(
    sc('[jb_hero variant="home" eyebrow="Joseph Bogdan, NMLS #2795320 · CrossCountry Mortgage" '
       'title="Mortgage Strategy for Your Next" accent="Move." '
       'lede="Buying your first home, stepping up to a luxury property or qualifying with business income? Joseph Bogdan structures the loan around your life - and picks up the phone when it matters." '
       'cta="Discover Your Buying Power" cta_url="/get-pre-approved/" image="joe-headshot.webp" '
       'note="Free personalized analysis · No credit pull · Based in Flower Mound, serving North Texas" builder="yes"]'),
    sc("[jb_trust]"),
    sc("[jb_intent]"),
    section(
        group(
            group(
                p("Builder &amp; Developer Partnerships", "eyebrow"),
                h("The Lending Partner Your Buyers Deserve.", 2, "section-title"),
                p("When your buyers need financing, they need it handled quickly, clearly and by someone who understands your timeline. Joseph works directly with builders and developers to give buyers a responsive path from contract to close - protecting your schedule and your reputation."),
                buttons(button("Become a Preferred Lending Partner", "/builders-developers/#partner"), button("How the Partnership Works", "/builders-developers/", outline=True)),
                cls="split-form-copy",
            ),
            group(
                group(h("Responsive pre-approvals", 3), p("Prompt attention for model-home and walk-in traffic, so buyers stay engaged and your sales team keeps moving."), cls="card card-dark"),
                group(h("Built around construction timelines", 3), p("Rate locks, appraisals and closings planned around your build schedule and contract terms."), cls="card card-dark"),
                group(h("One point of contact, start to finish", 3), p("Your sales team and your buyers have Joseph’s direct line, with proactive updates on every file."), cls="card card-dark"),
                group(h("A business owner’s perspective", 3), p("Joseph ran companies for more than 30 years. He knows why every delayed closing costs you money."), cls="card card-dark"),
                cls="card-grid card-grid-2",
            ),
            cls="split-form",
        ),
        tone="navy",
        id="builders",
    ),
    form_section(
        "Discover Your Buying Power",
        "Know Your Number Before You Fall in Love With a House.",
        "Online calculators guess. Joseph looks at your actual income, savings and goals, then sends a personalized buying-power analysis you can shop with.",
        [
            "A realistic price range - and the monthly payment behind it",
            "The loan programs you are most likely to fit",
            "Options if you need to buy before you sell",
            "What to do now to strengthen your approval",
        ],
        "buying-power",
        id="buying-power",
        tone="ivory",
    ),
    section(
        split(
            [sc('[jb_photo file="joe-headshot.webp" alt="Joseph Bogdan, Senior Loan Officer" class="photo-portrait"]'),
             sc('[jb_video title="Meet Joseph in 90 seconds"]')],
            [p("Meet Joseph Bogdan", "eyebrow"),
             h("A Loan Officer Who Has Sat on Your Side of the Desk.", 2, "section-title"),
             p("Before mortgage lending, Joseph spent more than 30 years building and running companies as a CEO. He has signed payroll, weighed risk on major purchases and financed his own homes and investments along the way."),
             p("That is why he treats a mortgage as a strategic decision - connected to your business, your family and your long-term plans - not just a rate quote. You get straight answers, a clear plan and a loan officer who stays reachable from first call to closing."),
             buttons(button("Read Joseph’s Story", "/about-joseph/"), button("Ask Joseph a Question", CONTACT, outline=True))],
            cls="split-media-left",
        ),
        tone="white",
    ),
    section(
        head("Specialties", "Where Joseph’s Experience Makes the Biggest Difference.",
             "Some loans are simple. These usually aren’t - and they’re where a strategic loan officer earns his keep."),
        group(
            group(
                p("Luxury & Jumbo", "eyebrow eyebrow-light"),
                h("Financing High-Value Homes, Ranches and Second Homes", 3),
                p("Jumbo loans reward preparation: asset documentation, reserve planning and the right structure for how you hold wealth. Joseph brings a CEO’s discipline to large financing decisions."),
                ul(["Jumbo purchase and refinance", "Ranch, acreage and second-home financing", "Strategies for complex assets and income"], "check-list"),
                buttons(button("Explore Jumbo Financing", "/loan-programs/jumbo-luxury-financing/")),
                cls="feature feature-dark",
            ),
            group(
                p("Business Owners & Investors", "eyebrow eyebrow-light"),
                h("Qualifying When Your Tax Return Doesn’t Tell the Whole Story", 3),
                p("Write-offs that save you taxes can shrink your qualifying income. Joseph has run businesses himself and knows how to present self-employed and investor income the right way."),
                ul(["Bank-statement and 1099 programs", "DSCR loans that qualify on the property’s rent", "Portfolio and multi-unit strategy"], "check-list"),
                buttons(button("See Self-Employed Options", "/loan-programs/self-employed-business-owners/"), button("Investment Property Loans", "/loan-programs/investment-property/", outline=True)),
                cls="feature feature-dark",
            ),
            cls="feature-grid",
        ),
        tone="navy",
    ),
    section(
        head("For Real Estate Professionals", "A Lending Partner Who Protects Your Deals.",
             "Joseph is a mortgage loan originator only - he will never compete with you for the client. His job is to make you look good and get your buyers to the closing table."),
        cards(
            card("Realtors", "Prompt scenario reviews when you are writing an offer, strong pre-approval letters and proactive updates so you are never chasing the lender.", ("Partner with Joseph", "/realtor-partners/")),
            card("Builders & Developers", "Responsive pre-approvals for model-home traffic, an understanding of construction timelines and one point of contact from contract to close.", ("Become a preferred lender", "/builders-developers/")),
            cols=2,
        ),
        tone="ivory",
    ),
    sc('[jb_process title="Conversation → Strategy → Approval → Closing" cta="Start With a Conversation" url="/contact/"]'),
    faq("Straight Answers, Before You Ask.", [
        ("How much house can I afford?",
         "It depends on your income, monthly debts, savings, credit and the loan program - plus Texas property taxes and insurance, which matter more here than in many states. Joseph’s free buying-power analysis turns those numbers into a realistic price range and payment."),
        ("Can I qualify for a mortgage if I’m self-employed?",
         "Often, yes. Beyond traditional tax-return loans, there are bank-statement, 1099 and asset-based programs designed for business owners. The right choice depends on how your income is documented, which is exactly what Joseph reviews in a Self-Employed Strategy Review."),
        ("Can I buy a new home before I sell my current one?",
         "Frequently, yes. Depending on your income, equity and reserves, you may qualify carrying both payments, or use options that tap your current home’s equity. Joseph will walk through what fits your situation before you write an offer."),
        FAQ_REALTOR,
        FAQ_NMLS,
        FAQ_CREDIT_PULL,
    ]),
    sc("[jb_latest count=\"3\"]"),
    sc('[jb_cta title="Have a Scenario on Your Mind?" text="Tell Joseph what you are trying to do. You will get a straight answer and a clear next step - not a sales pitch." url="/contact/" label="Ask Joseph About Your Scenario"]'),
)

# ---------------------------------------------------------------------------
# Get Pre-Approved / Discover Your Buying Power
# ---------------------------------------------------------------------------
preapproval = page(
    sc('[jb_hero eyebrow="Two ways to start" title="Get Pre-Approved" accent="With Joseph." '
       'lede="Ready to apply? Start CrossCountry Mortgage’s secure online application, the step that leads to a pre-approval. Not ready yet? Start with a free buying-power analysis from Joseph. It takes about two minutes and does not pull your credit." '
       'cta="Start My Application" cta_url="/apply/" secondary="yes" form="buying-power" form_heading="Or Start With Your Buying Power"]'),
    section(
        head("Choose Your Starting Point", "Apply Now, or Get Your Number First."),
        cards(
            card("Apply online", "CrossCountry Mortgage’s secure application is the official first step toward a pre-approval. With your authorization, your credit, income and assets are reviewed so Joseph can issue a pre-approval letter.", ("Start my application", "/apply/")),
            card("Discover your buying power", "A free, no-credit-pull analysis. Answer a few questions and Joseph follows up with a realistic price range, likely programs and the documents you will need to apply.", ("Get my buying-power analysis", "#start")),
            cols=2,
        ),
        tone="ivory",
    ),
    sc('[jb_process title="From First Conversation to Keys" cta="Questions First? Ask Joseph" url="/contact/"]'),
    faq("Pre-Approval Questions", [
        ("Is the buying-power analysis a loan application?",
         "No. The analysis is a free, no-credit-pull estimate based on what you share, and it does not lock a rate or commit anyone to lend. To get pre-approved, you complete CrossCountry Mortgage’s online application, and Joseph reviews your credit, income and assets."),
        FAQ_CREDIT_PULL,
        ("What is the difference between pre-qualification and pre-approval?",
         "A pre-qualification is an estimate based on what you tell us. A pre-approval goes further: after you apply, your income, assets and credit are reviewed and verified, so sellers and their agents can trust your offer."),
        ("How long is a pre-approval good for?",
         "Pre-approvals are time-limited and depend on the program and how recent your documents are. If your search runs longer, Joseph can update it with fresh documents."),
        FAQ_TIMELINE,
        FAQ_CREDIT,
    ]),
)

# ---------------------------------------------------------------------------
# Loan Programs hub
# ---------------------------------------------------------------------------
programs = page(
    sc('[jb_hero eyebrow="Loan Programs" title="Start With What You’re Trying to" accent="Do." '
       'lede="The right loan depends on your goal, how you earn and what you own. Pick the situation closest to yours and Joseph will take it from there." '
       'cta="Discover Your Buying Power" cta_url="/get-pre-approved/" image="joe-headshot.webp"]'),
    section(
        head("Find Your Scenario", "Which of These Sounds Like You?"),
        cards(
            card("“How much can I afford - and how do I win the house?”", "First-time and move-up buyers, buyers who need to sell first, and new-construction purchases.", ("Home Purchase", "/loan-programs/home-purchase/")),
            card("“Should I refinance or tap my equity?”", "Lower a payment, take cash out, consolidate debt or remove mortgage insurance.", ("Refinance & Equity", "/loan-programs/refinance/")),
            card("“How do I finance a high-value home well?”", "Jumbo purchases and refinances, ranches, acreage and second homes.", ("Jumbo & Luxury Financing", "/loan-programs/jumbo-luxury-financing/")),
            card("“Can I qualify if I’m self-employed?”", "Bank-statement, 1099 and asset-based options for business owners and entrepreneurs.", ("Self-Employed & Business Owners", "/loan-programs/self-employed-business-owners/")),
            card("“What are my options for a rental property?”", "DSCR, conventional investor and multi-unit financing for growing a portfolio.", ("Investment Property", "/loan-programs/investment-property/")),
            card("“Can I finance building a custom home?”", "One-time-close construction loans that cover the lot, the build and your permanent mortgage.", ("Construction Loans", "/loan-programs/construction-loans/")),
            card("“I found a lot. Can I finance it?”", "Lot and land loans for buyers who want to secure land now and build when ready.", ("Lot & Land Loans", "/loan-programs/lot-land-loans/")),
            card("“My situation is complicated.”", "Recent job change, credit event, divorce, trust-held assets - tell Joseph the details and get a straight answer.", ("Ask Joseph About Your Scenario", "/contact/")),
        ),
        tone="ivory",
    ),
    section(
        head("Programs Joseph Works With", "The Tools Behind the Strategy",
             "Products matter, but only after the plan. These are the programs Joseph most often uses to solve the situations above."),
        ul([
            "<strong>Conventional</strong> - a range of down-payment options for qualified buyers",
            "<strong>FHA</strong> - more flexible credit and down-payment guidelines",
            "<strong>VA</strong> - for eligible veterans, service members and surviving spouses",
            "<strong>Jumbo</strong> - loan amounts above conforming limits",
            "<strong>Fixed-rate and adjustable-rate</strong> - matched to how long you plan to keep the home",
            "<strong>Non-QM</strong> - alternative-documentation programs for borrowers outside standard guidelines",
            "<strong>Home equity</strong> - options to access equity without replacing your first mortgage",
            "<strong>Down payment assistance</strong> - programs for eligible buyers, including first-time homebuyers",
            "<strong>Bank-statement &amp; 1099</strong> - qualify using business or personal deposits instead of tax returns",
            "<strong>DSCR</strong> - investor loans that qualify on the property’s rental income",
            "<strong>New construction</strong> - financing coordinated with your builder’s timeline",
            "<strong>Construction-to-permanent</strong> - conventional, FHA and VA one-time-close loans for custom and to-be-built homes",
            "<strong>Lot &amp; land</strong> - financing for residential lots and land you plan to build on",
        ], "check-list check-list-columns"),
        p("Program availability, rates and terms depend on your full financial picture and are subject to credit approval and change.", "fine-print"),
        tone="white",
    ),
    sc('[jb_cta title="Not Sure Which Fits?" text="That is normal. A five-minute conversation with Joseph usually narrows it down." url="/contact/" label="Ask Joseph About Your Scenario"]'),
)

# ---------------------------------------------------------------------------
# Home Purchase
# ---------------------------------------------------------------------------
purchase = page(
    sc('[jb_hero eyebrow="Home Purchase" title="Buy With a Number You Trust and an Offer Sellers" accent="Respect." '
       'lede="Whether it is your first home, your next home or a new build, Joseph helps you understand what you can comfortably afford and makes your offer stronger." '
       'cta="Discover Your Buying Power" cta_url="#buying-power" image="joe-headshot.webp"]'),
    section(
        head("Sound Familiar?", "The Questions Buyers Ask Joseph Every Week."),
        cards(
            card("“How much can I actually afford?”", "Lenders may approve more than you want to spend. Joseph shows the payment behind every price point - taxes and insurance included - so you choose your comfort zone."),
            card("“Can I buy before I sell?”", "Depending on income, equity and reserves, you may be able to carry both homes briefly or use your current equity. Joseph maps the options before you write an offer."),
            card("“How much do I need to put down?”", "It may be less than you think. Conventional, FHA and VA programs each have different down-payment requirements and trade-offs worth understanding."),
            card("“How do I compete with other offers?”", "A fully documented pre-approval and a loan officer who is responsive to the listing agent can help your offer stand out."),
            card("“We’re buying new construction.”", "Joseph coordinates with your builder’s schedule so rate, appraisal and closing timelines line up."),
            card("“Is now a good time to buy?”", "Joseph won’t pressure you. He will help you compare buying now with waiting, using your real numbers."),
        ),
        tone="ivory",
    ),
    form_section(
        "Free Buying-Power Analysis",
        "Get a Personalized Number - Not a Calculator Guess.",
        "Two minutes of questions. Joseph reviews your answers personally and follows up with your price range, likely programs and next steps. No credit pull.",
        ["Realistic price range and monthly payment", "Programs you likely qualify for", "Buy-before-you-sell options if you own today"],
        "buying-power",
        id="buying-power",
    ),
    sc('[jb_process title="Conversation → Strategy → Approval → Closing" cta="Talk Through Your Purchase" url="/contact/"]'),
    faq("Home Purchase Questions", [
        ("What do I need for a pre-approval?",
         "Typically recent pay stubs, W-2s or tax returns, two months of bank statements and a photo ID. Self-employed buyers may use different documentation. Joseph sends a simple checklist based on your situation."),
        ("Can I buy a home with less than 20% down?",
         "Often, yes. Depending on your situation, conventional, FHA or - for eligible veterans - VA financing may allow a smaller down payment. Each option has trade-offs, such as mortgage insurance, which Joseph will walk through with your actual numbers."),
        ("Can I buy before selling my current home?",
         "Often. It depends on whether you can qualify with both payments, how much equity you have and your reserves. Joseph will outline the realistic options before you start touring."),
        FAQ_TIMELINE,
        FAQ_CREDIT,
    ]),
    sc('[jb_cta title="Ready to Shop With Confidence?" text="Start with your personalized buying-power analysis." url="/get-pre-approved/" label="Discover Your Buying Power"]'),
)

# ---------------------------------------------------------------------------
# Refinance
# ---------------------------------------------------------------------------
refinance = page(
    sc('[jb_hero eyebrow="Refinance & Home Equity" title="Make Your Mortgage Work Harder for" accent="You." '
       'lede="Lower your payment, unlock equity, consolidate debt or remove mortgage insurance - but only when the math actually works. Joseph will tell you if it doesn’t." '
       'cta="Get My Refinance Analysis" cta_url="#refinance-analysis" image="joe-headshot.webp"]'),
    section(
        head("What Are You Trying to Do?", "Refinancing Is a Tool. Start With the Goal."),
        cards(
            card("Lower my monthly payment", "Compare a new rate and term against your current loan, including closing costs and your break-even point."),
            card("Take cash out", "Use equity for renovations, a down payment on another property or a business opportunity."),
            card("Consolidate higher-interest debt", "Roll credit cards or other debt into one payment - and understand the long-term trade-off."),
            card("Remove mortgage insurance", "If your home has appreciated, you may be able to drop PMI or FHA mortgage insurance."),
            card("Pay off faster", "Shorten your term to save on interest without stretching your budget."),
            card("Not sure yet", "Joseph will look at your current loan and tell you honestly whether refinancing makes sense now."),
        ),
        tone="ivory",
    ),
    form_section(
        "Refinance & Equity Analysis",
        "See What Your Equity Could Do - In Two Minutes.",
        "Share a few details about your home and current loan. You will see an instant estimate of accessible equity, and Joseph will follow up with a personalized side-by-side comparison.",
        ["Estimated accessible equity", "Break-even point on closing costs", "Whether waiting could be the better move"],
        "refinance",
        id="refinance-analysis",
    ),
    faq("Refinance Questions", [
        ("When does refinancing make sense?",
         "When the savings or benefit outweighs the cost within a time frame that fits your plans. Joseph calculates your break-even point so you can decide with real numbers - and will tell you if waiting is smarter."),
        ("How much equity can I take out?",
         "It depends on your home’s value, your current balance, your credit and the program. Texas has specific rules for cash-out refinancing on a homestead, which Joseph will walk you through."),
        ("Can I remove mortgage insurance without refinancing?",
         "Sometimes. Conventional PMI can often be removed once you reach enough equity. FHA mortgage insurance usually requires a refinance. Joseph will check which applies to you."),
        FAQ_CREDIT_PULL,
    ]),
)

# ---------------------------------------------------------------------------
# Jumbo & Luxury
# ---------------------------------------------------------------------------
jumbo = page(
    sc('[jb_hero eyebrow="Jumbo & Luxury Financing" title="Large Loans Deserve a" accent="Strategy." '
       'lede="High-value homes, ranches and second homes come with different rules - larger reserves, deeper documentation and more structure choices. Joseph brings executive-level judgment to every one." '
       'cta="Request a Private Consultation" cta_url="#consultation" image="joe-headshot.webp"]'),
    section(
        split(
            [p("Why It’s Different", "eyebrow"),
             h("Jumbo Financing Rewards Preparation.", 2, "section-title"),
             p("Above conforming loan limits, lenders look harder at reserves, asset sources and how your income is earned. Small decisions - which accounts to document, how to structure the down payment, whether to keep liquidity - can change your terms and your flexibility after closing."),
             p("Joseph spent three decades making capital decisions as a CEO. He will help you weigh the options the way a CFO would, then manage the file so it moves quietly and on schedule.")],
            [ul([
                "<strong>Jumbo purchase and refinance</strong> for high-value primary homes",
                "<strong>Second homes</strong> and vacation properties",
                "<strong>Ranch and acreage</strong> properties across North Texas",
                "<strong>Complex income</strong>: business owners, executives, commission and bonus earners",
                "<strong>Asset-based strategies</strong> for clients with significant savings or investments",
                "<strong>Discreet, direct communication</strong> with you and your advisors",
            ], "check-list check-list-card")],
        ),
        tone="white",
    ),
    form_section(
        "Private Jumbo Consultation",
        "Talk Through Your Financing Before You Commit.",
        "Share the basics and Joseph will reach out personally to discuss structure, documentation and timing - before you are under contract.",
        ["Down-payment and reserve strategy", "Documentation plan for complex income and assets", "Realistic timeline to close"],
        "jumbo",
        id="consultation",
    ),
    faq("Jumbo & Luxury Questions", [
        ("What is a jumbo loan?",
         "A mortgage larger than the conforming loan limit set each year by the Federal Housing Finance Agency. Because these loans can’t be sold to Fannie Mae or Freddie Mac, lenders set their own credit, reserve and documentation standards."),
        ("How much do I need to put down on a jumbo loan?",
         "It varies by program, loan size and your overall financial profile. Joseph will walk you through the requirements that apply to you and the trade-offs between putting more down and keeping liquidity."),
        ("Can I finance a ranch or acreage property?",
         "Often, yes - though acreage, outbuildings and agricultural use affect which programs fit. Share the property details and Joseph will tell you what is realistic."),
        FAQ_TIMELINE,
    ]),
)

# ---------------------------------------------------------------------------
# Self-Employed & Business Owners
# ---------------------------------------------------------------------------
self_employed = page(
    sc('[jb_hero eyebrow="Self-Employed & Business Owners" title="Your Business Is Strong. Your Tax Return Just Doesn’t" accent="Show It." '
       'lede="Write-offs that lower your taxes can also lower your qualifying income. Joseph has owned and run companies - he knows how to present business income so lenders see the real picture." '
       'cta="Request a Strategy Review" cta_url="#strategy-review" image="joe-headshot.webp"]'),
    section(
        head("Sound Familiar?", "Why Good Businesses Get Bad Mortgage Answers."),
        cards(
            card("“The bank said my income is too low.”", "Tax-return income after deductions can understate what you actually earn. Other documentation paths may fit better."),
            card("“My income changes year to year.”", "Lenders often average income. Timing your application - or choosing a different program - can matter."),
            card("“I just switched from W-2 to my own company.”", "Recent business owners have options, especially with prior experience in the same field."),
            card("“My money is in the business.”", "How business funds are used for down payment and reserves needs a plan before you apply."),
        ),
        tone="ivory",
    ),
    section(
        head("Options for Business Owners", "More Than One Way to Qualify."),
        cards(
            card("Full-documentation loans", "Conventional, FHA or jumbo financing using tax returns - often the most straightforward path when your returns support it."),
            card("Bank-statement loans", "Qualify using business or personal bank deposits instead of tax returns."),
            card("1099 programs", "For contractors and commission earners paid on 1099s."),
            card("Asset-based loans", "Qualify using significant liquid assets rather than monthly income."),
        ),
        p("Non-traditional programs can carry different rates, down-payment and reserve requirements. Joseph will compare them side by side with conventional options.", "fine-print"),
        tone="white",
    ),
    form_section(
        "Self-Employed Mortgage Strategy Review",
        "Get a Plan Before You Apply Anywhere.",
        "Tell Joseph how your business is structured and what you are trying to do. He will outline which documentation path fits, what lenders will look for and how to position your file.",
        ["Which programs you likely qualify for", "How lenders will calculate your income", "What to prepare - and what to avoid - before applying"],
        "self-employed",
        id="strategy-review",
    ),
    faq("Self-Employed Mortgage Questions", [
        ("Can I get a mortgage with less than two years self-employed?",
         "Sometimes. If you have a strong history in the same line of work, some programs will consider a shorter self-employment period. Joseph will review your timeline."),
        ("What is a bank-statement loan?",
         "A program that calculates income from bank deposits instead of tax returns. It is designed for business owners whose deductions reduce taxable income. Pricing and requirements typically differ from conventional loans, and Joseph will compare them side by side."),
        ("Do I need to stop taking write-offs to qualify?",
         "Not necessarily. Talk to Joseph - and your CPA - before changing your tax strategy. There may be a program that fits how you already file."),
        ("Investment property instead?", "If you are buying rentals, a DSCR loan may qualify you on the property’s rent rather than your personal income. See <a href=\"/loan-programs/investment-property/\">investment property financing</a>."),
    ]),
)

# ---------------------------------------------------------------------------
# Investment Property
# ---------------------------------------------------------------------------
investment = page(
    sc('[jb_hero eyebrow="Investment Property" title="Financing That Helps Your Portfolio" accent="Grow." '
       'lede="Single-family rentals, 2-4 units or short-term rentals - Joseph helps investors choose financing that fits the deal and keeps the next deal possible." '
       'cta="Run an Investor Scenario" cta_url="#investor-scenario" image="joe-headshot.webp"]'),
    section(
        head("Investor Questions", "What Investors Ask Joseph."),
        cards(
            card("“Can I qualify on the property’s rent?”", "DSCR loans qualify primarily on the property’s rental income compared with its payment - not your personal tax returns."),
            card("“How much do I need down?”", "Investment properties often have different down-payment and reserve requirements than a primary home. Joseph will compare programs so you keep enough cash for reserves and the next opportunity."),
            card("“Can I pull equity from my rentals?”", "A cash-out refinance can fund your next purchase. Joseph will check whether the numbers still cash-flow afterward."),
            card("“Should I buy in an LLC?”", "Some programs allow LLC vesting. Joseph will explain the options; talk with your attorney and CPA about the legal and tax side."),
        ),
        tone="ivory",
    ),
    form_section(
        "Investor Scenario",
        "Send Joseph the Deal. Get Your Financing Options.",
        "Price, rent and cash available are enough to start. Joseph will reply with the programs that fit and how each affects your cash flow.",
        ["DSCR vs. conventional comparison", "Cash needed to close and reserves", "Cash-out and portfolio strategy"],
        "investor",
        id="investor-scenario",
    ),
    faq("Investment Property Questions", [
        ("What is a DSCR loan?",
         "DSCR stands for debt-service coverage ratio. These loans compare a property’s rental income with its mortgage payment, taxes and insurance, so qualification relies more on the property than on your personal income."),
        ("Can I use a VA or FHA loan for an investment property?",
         "Not for a pure investment property. However, you may be able to buy a 2-4 unit home, live in one unit and rent the others. Joseph can walk you through the requirements."),
        FAQ_CREDIT_PULL,
    ]),
)

# ---------------------------------------------------------------------------
# Builders & Developers
# ---------------------------------------------------------------------------
builders = page(
    sc('[jb_hero eyebrow="Builder & Developer Partnerships" title="The Lending Partner Your Buyers" accent="Deserve." '
       'lede="Responsive pre-approvals for model-home traffic, proactive communication and a loan officer who understands construction timelines - so your schedule and your reputation are in good hands." '
       'cta="Become a Preferred Lending Partner" cta_url="#partner" image="photo-joseph-model-home.webp" image_alt="Joseph Bogdan touring a model home at the Innovative Housing Showcase in Washington, D.C."]'),
    section(
        head("Why Builders Work With Joseph", "Built Around Your Sales and Construction Schedule."),
        cards(
            card("Responsive pre-approvals", "Prompt attention for walk-in and model-home traffic so buyers stay engaged and your sales team can keep moving."),
            card("Timeline-aware financing", "Rate locks, appraisals and closings planned around construction milestones - not the other way around."),
            card("One point of contact", "Your sales team and your buyers have Joseph’s direct line, from contract to closing."),
            card("Proactive status updates", "You hear about issues early, with a plan, instead of the week of closing."),
            card("Business-owner perspective", "Joseph ran companies for 30 years. He understands margins, carrying costs and why every delayed closing matters."),
            card("Difficult-buyer strategy", "Self-employed, jumbo and move-up buyers who need to sell first get a real plan instead of a quick “no.”"),
        ),
        tone="ivory",
    ),
    section(
        split(
            [sc('[jb_photo file="photo-joseph-national-mall.webp" alt="Joseph Bogdan on the National Mall at the Innovative Housing Showcase, with the U.S. Capitol behind him" class="photo-landscape" caption="Joseph at the Innovative Housing Showcase on the National Mall in Washington, D.C."]')],
            [p("On the Ground", "eyebrow"),
             h("Staying Ahead of How Homes Get Built.", 2, "section-title"),
             p("Joseph spends time where the housing industry is heading. At the Innovative Housing Showcase on the National Mall in Washington, D.C., he toured new home designs and building approaches and talked with builders and manufacturers about what is changing in how homes are built, sold and financed."),
             p("That perspective shapes how he works with builders: financing planned around the way you actually build, from your sales team's first buyer conversation to closing day."),
             buttons(button("Talk With Joseph About Your Communities", "#partner"))],
            cls="split-media-left",
        ),
        tone="white",
    ),
    section(
        split(
            [p("How It Works", "eyebrow"),
             h("A Simple Partnership.", 2, "section-title"),
             p("Joseph meets with your sales team, learns your communities and process, and sets expectations for communication. From there, your buyers get a responsive, consistent experience - and you get visibility into every file.")],
            [ul([
                "<strong>Kickoff</strong> - learn your communities, incentives and timelines",
                "<strong>Buyer intake</strong> - a simple way for your team to send buyers to Joseph",
                "<strong>Weekly visibility</strong> - status on every buyer in your pipeline",
                "<strong>Closing coordination</strong> - aligned with your construction and title teams",
            ], "check-list check-list-card")],
        ),
        tone="white",
    ),
    form_section(
        "Preferred Lending Partnership",
        "Let’s Talk About Your Communities.",
        "Share a little about your business and Joseph will set up a short call with you and your sales team.",
        None,
        "builder",
        id="partner",
    ),
    section(
        head("Builder Resources", "Free Guides for Builders and Sales Teams",
             "Practical tools your team can use with every buyer, written by Joseph."),
        cards(
            card("Builder Financing FAQ", "Straight answers to the questions builders and sales teams ask most: incentives, concessions, rate locks, appraisals and closing on time.", ("Read the FAQ", "/builders-developers/builder-financing-faq/")),
            card("Buyer Pre-Approval Checklist", "What to verify before you take a home off the market, plus the red flags that predict a contract that won't close.", ("Use the checklist", "/builders-developers/buyer-pre-approval-checklist/")),
            card("Contract-to-Close Timeline", "Every financing milestone from contract to keys, mapped to the construction schedule, so nothing surprises your team.", ("See the timeline", "/builders-developers/contract-to-close-timeline/")),
        ),
        tone="ivory",
    ),
    section(
        head("Financing Programs for Builders and Developers", "More Ways to Help Your Buyers Close",
             "Beyond responsive buyer financing, Joseph helps builders and developers use rate programs, construction loans and rental strategies."),
        cards(
            card("Forward Commitments", "Reserve a rate for buyers closing in a set window and give payment-sensitive buyers a reason to choose new construction.", ("How forward commitments work", "/builders-developers/forward-commitments/")),
            card("Construction-to-Permanent Loans", "For buyers building on their own lot or a lot in your community: one approval and one closing, with draws coordinated with your team.", ("Construction loans", "/loan-programs/construction-loans/")),
            card("Developer &amp; Build-to-Rent", "Lot financing, end-buyer plans by phase and DSCR loans for completed homes you keep as rentals.", ("Developer financing", "/builders-developers/developer-financing/")),
        ),
        tone="white",
    ),
    sc('[jb_latest count="3" category="builders-new-construction" title="Insights for Builders"]'),
    faq("Questions From Builders", [
        ("Do our buyers have to use Joseph as their lender?",
         "No. Buyers are always free to choose their own lender. Joseph’s goal is to be the lender your buyers want to use, because the process is responsive and predictable."),
        ("How do you handle long construction timelines?",
         "Joseph plans financing around your build schedule from the start: when to apply, when to lock and when updated documents will be needed. Lock options depend on the program and are discussed with each buyer."),
        ("Can you help buyers who need to sell their current home first?",
         "Often, yes. Depending on income, equity and reserves, there may be ways to qualify carrying both homes or to use the current home’s equity. Joseph reviews each buyer’s options early so contracts stay on track."),
        ("What does your sales team need to do?",
         "Very little. Joseph sets up a simple way for your team to introduce buyers, then keeps your team updated on every file through closing."),
    ], eyebrow="For Builders"),
    p("Builders and lenders must comply with RESPA. Buyers are always free to choose their own lender.", "fine-print section-fine-print"),
)

# ---------------------------------------------------------------------------
# Realtor Partners
# ---------------------------------------------------------------------------
realtors = page(
    sc('[jb_hero eyebrow="For Realtors" title="Your Client. Your Deal. Joseph Just Makes It" accent="Close." '
       'lede="Joseph is a mortgage loan originator only - he does not list, sell or represent buyers. That means he is entirely focused on getting your clients approved, protecting your relationship and keeping your deals on schedule." '
       'cta="Run a Scenario for My Client" cta_url="#client-scenario" image="joe-headshot.webp"]'),
    section(
        head("What You Can Count On", "Built for Agents Who Can’t Afford Surprises."),
        cards(
            card("Prompt scenario reviews", "Text Joseph the basics while you are writing an offer and get a realistic read on your client’s options."),
            card("Strong pre-approvals", "Documented, reviewed pre-approvals - and a call to the listing agent when it helps your offer stand out."),
            card("Proactive communication", "You hear status updates before you have to ask, from application to clear-to-close."),
            card("Difficult-borrower strategy", "Self-employed, jumbo, investor and buy-before-you-sell clients get a plan, not a quick “no.”"),
            card("Honest answers early", "If a scenario has a problem, you hear about it before the offer - not the week of closing."),
            card("Your relationship stays yours", "Joseph never competes for your client and always keeps you in the loop."),
        ),
        tone="ivory",
    ),
    form_section(
        "Run a Financing Scenario for My Client",
        "Get a Read on Your Client - Before You Write the Offer.",
        "No client names needed. Share the scenario and Joseph will reply directly to you with options and any red flags.",
        ["Realistic price range and down-payment options", "Program fit for complex income", "Buy-before-you-sell strategies"],
        "realtor-scenario",
        id="client-scenario",
    ),
    section(
        split(
            [p("Why It Matters", "eyebrow"),
             h("No More Conflicted Lenders.", 2, "section-title"),
             p("Some loan officers also sell real estate, which can make referring clients uncomfortable. Joseph has chosen to focus exclusively on mortgage lending. Every client you send stays your client - and Joseph’s job is to make you look good.")],
            [sc("[jb_contact_options]")],
        ),
        tone="white",
    ),
    faq("Questions From Agents", [
        FAQ_REALTOR,
        ("How quickly can Joseph review a scenario?",
         "Text or submit the scenario and Joseph will respond as quickly as he can. Let him know when an offer is being written so he can prioritize it."),
        ("Can Joseph help clients who need to sell before they buy?",
         "Often. Depending on income, equity and reserves, there may be ways to qualify carrying both homes or to use the current home’s equity. Send the scenario and Joseph will outline options."),
        FAQ_NMLS,
    ], eyebrow="For Agents"),
)

# ---------------------------------------------------------------------------
# About Joseph
# ---------------------------------------------------------------------------
about = page(
    sc('[jb_hero eyebrow="About Joseph Bogdan" title="A CEO’s Judgment. A Loan Officer’s" accent="Focus." '
       'lede="Joseph Bogdan spent more than 30 years building and running companies before becoming a mortgage loan originator. Today he brings that same strategic thinking to the biggest financial decision most people make." '
       'cta="Ask Joseph About Your Scenario" cta_url="/contact/" image="joe-headshot.webp"]'),
    section(
        split(
            [sc('[jb_photo file="photo-joseph-model-home-2.webp" alt="Joseph Bogdan in a model home at the Innovative Housing Showcase" class="photo-tall" caption="Joseph touring new home designs at the Innovative Housing Showcase in Washington, D.C."]'),
             sc('[jb_video title="Meet Joseph in 90 seconds"]')],
            [p("The Business Background", "eyebrow"),
             h("Three Decades of Decisions That Prepared Him for Yours.", 2, "section-title"),
             p("As a CEO, Joseph built and operated multiple companies - including more than two decades building successful medical businesses focused on outpatient diagnostic services. He managed payroll, negotiated with lenders, evaluated risk and lived with the consequences of every major financial commitment."),
             p("Along the way he bought, financed and invested in homes and ranch properties of his own. He learned firsthand how much the structure of a loan - not just its rate - affects flexibility, cash flow and peace of mind.")],
            cls="split-media-left",
        ),
        tone="white",
    ),
    section(
        p("Why Mortgage Lending", "eyebrow"),
        h("Why Joseph Became a Loan Officer.", 2, "section-title"),
        p("Joseph joined the mortgage industry to serve his community by providing innovative mortgage solutions that make homeownership more accessible and affordable. After years of leading client-focused businesses, he moved into lending to put that leadership and service experience to work for buyers and homeowners."), p("He saw how often buyers - especially business owners and families making big moves - got generic answers to situations that deserved real strategy. Joseph’s goal is to give every client the kind of advice he always wanted: direct, informed and focused on the long term."),
        tone="ivory",
        narrow=True,
    ),
    section(
        head("How Joseph Works", "What Clients and Agents Can Expect."),
        cards(
            card("Strategy before product", "Joseph starts with your goals and timeline, then chooses the loan - not the other way around."),
            card("Plain-language answers", "No jargon, no pressure. If something is not in your best interest, he will tell you."),
            card("Reachable", "Call or text Joseph directly. You will not be handed off to a call center."),
            card("Focused on lending only", "Joseph does not sell real estate, so his advice - and his relationship with your agent - stays clean."),
            cols=2,
        ),
        tone="white",
    ),
    section(
        head("Credentials", "Licensed, Verifiable and Backed by a National Lender."),
        ul([
            "Senior Loan Officer, CrossCountry Mortgage, LLC (company NMLS #3029)",
            "Individual NMLS #2795320 - <a href=\"https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/2795320\" target=\"_blank\" rel=\"noopener\">verify on NMLS Consumer Access</a>",
            "Licensed as a mortgage loan originator in Texas; CrossCountry Mortgage, LLC is licensed in all 50 states",
            "Based in Flower Mound, serving the Dallas-Fort Worth Metroplex and North Texas",
            "30+ years of business ownership and executive leadership",
        ], "check-list"),
        tone="white",
        narrow=True,
    ),
    sc('[jb_cta title="Let’s Talk About Your Next Move." text="Start with a question, a scenario or a buying-power analysis." url="/get-pre-approved/" label="Discover Your Buying Power"]'),
)

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
contact = page(
    sc('[jb_hero eyebrow="Contact Joseph" title="Ask Joseph About Your" accent="Scenario." '
       'lede="A question, a complicated situation or a deal on a deadline - tell Joseph what is going on and you will get a straight answer from him directly." '
       'cta="" form="ask-joe" form_heading="Send Joseph Your Question"]'),
    section(
        split(
            [p("Prefer to Talk?", "eyebrow"),
             h("Call or Text Joseph Directly.", 2, "section-title"),
             p("Texting is often fastest for quick questions. For bigger decisions, a short call helps Joseph understand the full picture."),
             sc("[jb_contact_options]")],
            [p("Office", "eyebrow"),
             h("Flower Mound, Texas", 3),
             p("2201 Spinks Road, Suite 236<br>Flower Mound, TX 75022"),
             p("Serving Dallas, Fort Worth, Southlake, Plano, Frisco, McKinney, Denton, Argyle, Granbury and communities across North Texas."),
             sc("[jb_disclosure]")],
        ),
        tone="white",
    ),
)

# ---------------------------------------------------------------------------
# Legal
# ---------------------------------------------------------------------------

privacy = page(
    p("<em>Last updated: October 2026</em>"),
    p("This Privacy Policy explains how information is collected and used when you visit this website, operated by [jb_opt key=\"name\"], [jb_opt key=\"title\"] (NMLS #[jb_opt key=\"nmls\"]), with [jb_opt key=\"company\"] (Company NMLS #[jb_opt key=\"company_nmls\"])."),
    h("Information we collect"),
    ul([
        "<strong>Information you provide</strong> - such as your name, phone number, email address and the details you share in our forms about your home-financing goals.",
        "<strong>Automatically collected information</strong> - such as your browser type, pages visited, referring site and approximate location, collected through cookies and similar technologies.",
    ]),
    h("How we use information"),
    ul([
        "To respond to your inquiry and provide the analysis or consultation you requested",
        "To contact you by phone, email or - with your consent - text message about your inquiry",
        "To improve this website and understand which content is helpful",
        "To comply with legal and regulatory obligations",
    ]),
    h("How information is shared"),
    p("We do not sell your personal information. Information you submit may be shared with [jb_opt key=\"company\"] and its service providers to respond to your request, and as required by law. Mobile numbers and text-messaging consent are not shared with third parties for their marketing purposes."),
    h("Your choices"),
    p("You may opt out of text messages at any time by replying STOP. To request access to or deletion of your information, contact [jb_opt key=\"email\"]."),
    h("Lender privacy notice"),
    p("If you apply for a loan, your information is also governed by <a href=\"https://crosscountrymortgage.com/mortgage/privacy-policy/\" target=\"_blank\" rel=\"noopener\">[jb_opt key=\"company\"]’s Privacy Policy</a> and the privacy notice provided with your application."),
    h("Changes to this policy"),
    p("We may update this policy from time to time. The date at the top shows when it was last revised."),
)

terms = page(
    p("<em>Last updated: October 2026</em>"),
    p("By using this website you agree to these terms. If you do not agree, please do not use the site."),
    h("Educational information only"),
    p("Content on this site is for general educational purposes and is not a commitment to lend, an offer of credit or financial, legal or tax advice. Estimates produced by our tools are illustrations based on the information you enter and on assumptions that may not apply to you."),
    h("Loan terms"),
    p("All loans are subject to credit approval, underwriting guidelines and program availability. Rates, terms and programs are subject to change without notice. Not all applicants will qualify."),
    h("Third-party links"),
    p("Links to other websites are provided for convenience. We are not responsible for their content or practices."),
    h("No warranties"),
    p("This website and its content are provided “as is” and “as available,” without warranties of any kind, express or implied, including accuracy, completeness or fitness for a particular purpose."),
    h("Limitation of liability"),
    p("To the fullest extent permitted by law, [jb_opt key=\"name\"] and [jb_opt key=\"company\"] are not liable for any indirect, incidental, consequential or other damages arising from your use of, or inability to use, this website or any information on it."),
    h("Governing law"),
    p("These terms are governed by the laws of the State of Texas, without regard to its conflict-of-law rules. Any dispute relating to this website will be brought in the state or federal courts located in Denton County, Texas."),
    h("Changes to these terms"),
    p("We may update these terms at any time. Continued use of the website after changes are posted means you accept the updated terms."),
    h("Contact"),
    p("Questions about these terms? Email [jb_opt key=\"email\"] or call [jb_opt key=\"phone\"]."),
    h("Licensing"),
    sc("[jb_disclosure]"),
)

sms = page(
    p("<em>Last updated: October 2026</em>"),
    p("By checking the text-message consent box on this site, you agree to receive text messages from [jb_opt key=\"name\"] and/or [jb_opt key=\"company\"] about your inquiry, which may be sent using automated technology. Consent is not required as a condition of obtaining any loan, product or service."),
    ul([
        "Message and data rates may apply.",
        "Message frequency varies based on your inquiry and ongoing conversation.",
        "Reply <strong>STOP</strong> at any time to opt out, or <strong>HELP</strong> for assistance.",
        "Your mobile number and consent will not be shared with third parties for their marketing purposes.",
    ]),
    p("See our <a href=\"/privacy-policy/\">Privacy Policy</a> for more on how your information is handled."),
)

accessibility = page(
    p("We want everyone to be able to use this website. It is designed to conform with the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA, including keyboard navigation, readable color contrast, descriptive labels and support for screen readers."),
    p("If you have difficulty using any part of this site, please call [jb_opt key=\"phone\"] or email [jb_opt key=\"email\"] and we will provide the information you need in another way and work to fix the issue."),
)

licensing = page(
    h("Licensing"),
    sc("[jb_disclosure]"),
    ul([
        "[jb_opt key=\"legal_name\"] is licensed as a residential mortgage loan originator in Texas - <a href=\"https://www.nmlsconsumeraccess.org/EntityDetails.aspx/INDIVIDUAL/2795320\" target=\"_blank\" rel=\"noopener\">verify NMLS #[jb_opt key=\"nmls\"]</a>.",
        "[jb_opt key=\"company\"] (NMLS #[jb_opt key=\"company_nmls\"]) is licensed in all 50 states - <a href=\"https://www.nmlsconsumeraccess.org/EntityDetails.aspx/COMPANY/3029\" target=\"_blank\" rel=\"noopener\">verify on NMLS Consumer Access</a> and see <a href=\"https://crosscountrymortgage.com/mortgage/licensing-and-disclosures/\" target=\"_blank\" rel=\"noopener\">CrossCountry Mortgage licensing and disclosures</a>.",
        "Branch NMLS #[jb_opt key=\"branch_nmls\"] (Flower Mound, TX)",
        "Company website: <a href=\"https://crosscountrymortgage.com/\" target=\"_blank\" rel=\"noopener\">crosscountrymortgage.com</a>",
    ]),
    h("Equal Housing Opportunity Lender"),
    p("[jb_opt key=\"company\"] is an Equal Housing Opportunity Lender. We do business in accordance with the Fair Housing Act and the Equal Credit Opportunity Act."),
    h("Not a commitment to lend"),
    p("Information on this website is not a commitment to lend or an offer of credit. All loans are subject to credit approval, underwriting guidelines and program availability. Programs, rates, terms and conditions are subject to change without notice. Not all applicants will qualify. Estimates produced by tools on this site are general illustrations, not loan offers."),
    h("Mortgage loan originator only"),
    p("[jb_opt key=\"name\"] is a licensed mortgage loan originator and does not provide real estate brokerage services or represent buyers or sellers in real estate transactions."),
    h("Texas Consumer Complaint and Recovery Fund Notice"),
    p("The Texas Department of Savings and Mortgage Lending notice appears at the bottom of every page and on the <a href=\"/texas-consumer-notice/\">Texas Consumer Notice</a> page."),
)

texas = page(
    p("The following notice is provided as required for Texas mortgage bankers and residential mortgage loan originators. It matches the notice published by <a href=\"https://crosscountrymortgage.com/mortgage/licensing-and-disclosures/\" target=\"_blank\" rel=\"noopener\">CrossCountry Mortgage, LLC</a>."),
    sc("[jb_texas_notice]"),
)

# ---------------------------------------------------------------------------
# Builder resources (children of Builders & Developers)
# ---------------------------------------------------------------------------
BUILDER_PARTNER_CTA = sc('[jb_cta title="Make Joseph Your Preferred Lender" text="A short kickoff with your sales team, then responsive buyer follow-up and proactive updates through closing." url="/builders-developers/#partner" label="Become a Preferred Lending Partner"]')

builder_faq = page(
    sc('[jb_hero eyebrow="Builder Resources" title="Builder Financing" accent="FAQ." '
       'lede="Straight answers to the questions North Texas builders and their sales teams ask Joseph most about buyer financing, incentives and closing on time." '
       'cta="Become a Preferred Lending Partner" cta_url="/builders-developers/#partner" image="joe-headshot.webp"]'),
    faq("Buyers and Pre-Approvals", [
        ("What should a builder verify before accepting a buyer's pre-approval?", "Confirm that the buyer's income, assets and credit were actually reviewed, which loan program they are approved for, whether the approval covers your price and incentives, and whether they need to sell another home. Joseph's <a href=\"/builders-developers/buyer-pre-approval-checklist/\">Buyer Pre-Approval Checklist</a> walks through each item."),
        ("Can a builder require buyers to use a preferred lender?", "No. Buyers are always free to choose their lender. Builders can offer a preferred lender and incentives within program limits, and arrangements must comply with RESPA."),
        ("How should we handle buyers who need to sell their current home?", "Find out at the first meeting. If the buyer qualifies carrying both payments, they can sign without a sale contingency. Otherwise options include using existing equity, timing the sale to the build or a realistic contingency."),
        ("What if a buyer's situation changes during construction?", "New debt, a job change or large deposits can affect approval. Coach buyers to call their lender before making changes, and ask the lender to update the file before completion."),
    ], eyebrow="Builder FAQ"),
    faq("Incentives and Concessions", [
        ("Is a rate buydown better than a price cut?", "Often for payment-sensitive buyers, because the same dollars usually lower the monthly payment more, and a buydown protects your comparable sales. A price cut can be better when the buyer needs a lower loan amount. See <a href=\"/price-cut-or-rate-buydown-builder-incentives/\">price cut or rate buydown</a>."),
        ("How much can a builder contribute toward a buyer's costs?", "It depends on the loan program, the buyer's down payment and occupancy. Conventional limits range from 3% to 9% for a primary residence, FHA generally allows up to 6%, and VA limits certain concessions to 4%. See <a href=\"/builder-incentive-limits-seller-concessions/\">seller-concession limits by loan type</a>."),
        ("Can builder incentives be paid to the buyer as cash?", "Generally no. Contributions are applied to allowable costs such as closing costs, prepaid items and rate buydowns."),
        ("Can we advertise a rate or monthly payment on our homes?", "You can promote financing incentives, but quoting a specific rate or payment triggers federal disclosure requirements. Have your lender review rate-based advertising before it runs."),
    ], eyebrow="Builder FAQ"),
    faq("Construction Timelines and Closing", [
        ("When should a buyer lock their rate on new construction?", "It depends on the build schedule and the program. Extended locks are available on many programs, usually at extra cost, or the buyer can lock closer to completion. Joseph explains the trade-offs to each buyer."),
        ("Can a buyer close before the home is complete?", "With a standard purchase loan, generally no: the home must be complete, with final inspection or occupancy approval. With a <a href=\"/loan-programs/construction-loans/\">construction-to-permanent loan</a>, the buyer closes before construction and the builder is paid in draws."),
        ("What is a forward commitment?", "A builder pays a fee to reserve a pool of mortgage money at a set rate for buyers who close within a window. See <a href=\"/builders-developers/forward-commitments/\">forward commitments for builders</a>."),
        ("Why do new-construction closings get delayed?", "The usual causes are expired documents, rate locks that run out, late completion paperwork, appraisal questions and buyer changes during the build. See <a href=\"/why-new-construction-closings-slip/\">why closings slip</a>."),
        ("How do appraisals work on new construction?", "Appraisers compare recent sales of similar homes, often in your community, and consider upgrades and concessions. Appraisals can be done from plans with a completion inspection later."),
        ("Can builders finance completed homes they keep as rentals?", "Often, with DSCR loans that qualify on the home's rent rather than personal tax returns. See <a href=\"/build-to-rent-holding-completed-homes-dscr/\">build to sell or hold</a>."),
    ], eyebrow="Builder FAQ"),
    BUILDER_PARTNER_CTA,
)

builder_checklist = page(
    sc('[jb_hero eyebrow="Builder Resources" title="Buyer Pre-Approval" accent="Checklist." '
       'lede="What your sales team should verify before taking a home off the market, and the red flags that predict a contract that will not close." '
       'cta="Talk to Joseph About a Buyer" cta_url="/builders-developers/#partner" image="joe-headshot.webp"]'),
    section(
        head("Before the Contract", "Verify These Seven Things", center=False),
        ol([
            "<strong>Reviewed, not stated.</strong> The lender reviewed income documents, bank statements and a credit report.",
            "<strong>The right program.</strong> The loan program fits the price, the home and how the buyer will use it.",
            "<strong>Price and incentives covered.</strong> The approval reflects your contract price, and incentives fit the program's contribution limits.",
            "<strong>Current home addressed.</strong> You know whether the buyer must sell or rent another home, and how that is planned.",
            "<strong>Cash to close confirmed.</strong> Down payment and remaining costs are documented, including what incentives will not cover.",
            "<strong>Timeline fit.</strong> The lender has a rate-lock and document-update plan for your expected completion date.",
            "<strong>A reachable lender.</strong> A named loan officer with an NMLS number who answers your team's questions.",
        ], "check-list"),
        tone="white",
        narrow=True,
    ),
    section(
        head("Red Flags", "Signs a Contract May Not Close", center=False),
        ul([
            "A letter with no lender contact or license number",
            "Vague answers about whether documents were reviewed",
            "A buyer who needs to sell, while the approval assumes they do not",
            "Recent job changes, new debt or large unexplained deposits with no plan",
            "Incentives promised beyond the program's contribution limits",
            "A lender who is hard to reach before the contract is signed",
        ], "check-list"),
        p("Questions you can ask the buyer's lender: which documents did you review, which program is this, does the approval cover this price and these incentives, and how will you keep our team updated?"),
        tone="ivory",
        narrow=True,
    ),
    BUILDER_PARTNER_CTA,
)

builder_timeline = page(
    sc('[jb_hero eyebrow="Builder Resources" title="Contract-to-Close" accent="Timeline." '
       'lede="Every financing milestone from signed contract to keys, mapped to the construction schedule, so your team and your buyers know what happens next." '
       'cta="Become a Preferred Lending Partner" cta_url="/builders-developers/#partner" image="joe-headshot.webp"]'),
    section(
        head("Milestones", "From Contract to Keys", center=False),
        ol([
            "<strong>Contract.</strong> Fully reviewed approval, program confirmed, incentives checked against limits, current-home plan in place.",
            "<strong>Application and disclosures.</strong> The buyer completes the application and receives initial loan disclosures.",
            "<strong>Rate-lock decision.</strong> Lock now with a longer lock, or float and lock closer to completion, based on the build schedule.",
            "<strong>During construction.</strong> Monthly completion-date updates shared with the lender; buyer coached to avoid new credit, job changes and large money moves.",
            "<strong>Appraisal.</strong> Ordered by the lender, from plans or near completion, depending on the program.",
            "<strong>Before completion.</strong> Updated pay stubs, bank statements and credit as needed; conditions cleared.",
            "<strong>Completion.</strong> Final inspection or certificate of occupancy, completion inspection if required, final walk-through.",
            "<strong>Clear to close.</strong> Closing disclosure delivered to the buyer, closing scheduled with title.",
            "<strong>Closing and keys.</strong> Documents signed, loan funded, keys delivered.",
        ], "check-list"),
        tone="white",
        narrow=True,
    ),
    section(
        head("Keep It on Schedule", "What Builders Can Do", center=False),
        ul([
            "Share realistic completion dates and update them as the build moves",
            "Ask the lender to schedule document updates before completion, not after",
            "Coordinate the walk-through, inspection and closing date in one shared plan",
            "Use a lender who sends proactive updates on every buyer in your pipeline",
        ], "check-list"),
        p("Read more: <a href=\"/why-new-construction-closings-slip/\">why new-construction closings slip</a> and <a href=\"/financing-on-a-construction-timeline/\">financing on a construction timeline</a>."),
        tone="ivory",
        narrow=True,
    ),
    BUILDER_PARTNER_CTA,
)

# ---------------------------------------------------------------------------
# Construction, land, forward commitments and developer financing
# ---------------------------------------------------------------------------
CONSTRUCTION_FORM = "/loan-programs/construction-loans/#construction-scenario"

construction = page(
    sc('[jb_hero eyebrow="Construction Loans" title="Build the Home, Close" accent="Once." '
       'lede="Planning a custom home in North Texas? A one-time-close construction loan finances the land, the build and your permanent mortgage with one application and one closing - and Joseph keeps the lender, builder and title company moving on the same schedule." '
       'cta="Start My Construction Scenario" cta_url="#construction-scenario" image="photo-joseph-model-home-2.webp" image_alt="Joseph Bogdan inside a new model home"]'),
    section(
        head("Before You Break Ground", "The Questions Every Custom-Home Buyer Asks."),
        cards(
            card("“Can I finance the land and the build together?”", "Often, yes. A construction-to-permanent loan can cover buying the lot, building the home and the long-term mortgage in a single loan."),
            card("“What if I already own my lot?”", "Equity in land you own can often count toward your down payment, which can reduce the cash you need at closing."),
            card("“Do I have to qualify twice?”", "Not with a one-time close. You qualify and close once, before construction starts, instead of re-qualifying when the home is finished."),
            card("“How does my builder get paid?”", "Funds are released in stages, called draws, as construction milestones are inspected and approved."),
            card("“Can I build with an FHA or VA loan?”", "Yes. CrossCountry Mortgage offers FHA and VA one-time-close construction loans for eligible buyers building a primary residence.", ("FHA &amp; VA construction loans", "/loan-programs/fha-va-construction-loans/")),
            card("“Can I use any builder?”", "Your builder has to be reviewed and approved by the lender. Joseph starts that review early so it never holds up your closing."),
        ),
        tone="ivory",
    ),
    section(
        split(
            [p("How It Works", "eyebrow"),
             h("One Loan From Lot to Keys.", 2, "section-title"),
             p("A one-time-close loan (also called construction-to-permanent) combines short-term construction financing and your long-term mortgage. You sign once. During construction, the loan pays your builder in draws. When the home is complete, the loan becomes your regular mortgage without a second closing."),
             p("Read the full guide: <a href=\"/one-time-close-construction-loans-explained/\">one-time-close construction loans explained</a>.")],
            [ol([
                "<strong>Plan</strong> - budget, land, builder and timeline reviewed with Joseph",
                "<strong>Approve the builder</strong> - the lender reviews your builder's experience, insurance and references",
                "<strong>Plans and appraisal</strong> - the home is appraised from plans and specifications, as if complete",
                "<strong>Close once</strong> - before construction starts, including the lot purchase if needed",
                "<strong>Build with draws</strong> - funds released after inspections at each stage",
                "<strong>Complete and convert</strong> - final inspection, then the loan becomes your permanent mortgage",
            ], "check-list check-list-card")],
        ),
        tone="white",
    ),
    section(
        head("Choosing a Path", "One-Time Close or Two-Time Close?", center=False),
        p("A <strong>one-time close</strong> means one approval, one set of closing costs and no re-qualifying at the end. A <strong>two-time close</strong> uses a separate short-term construction loan and then a new mortgage when the home is finished: two closings and two approvals, but more flexibility to shop the permanent loan. The right choice depends on your timeline, your cash and how stable your income will be through the build."),
        p("Compare them side by side: <a href=\"/one-time-close-vs-two-time-close-construction-loans/\">one-time close vs. two-time close</a>. Building on land you already own? See <a href=\"/building-a-home-on-land-you-already-own/\">building on your own lot</a>."),
        tone="ivory",
        narrow=True,
    ),
    form_section(
        "Construction Scenario",
        "Tell Joseph About Your Build.",
        "Land, budget and timeline are enough to start. Joseph will reply with the financing paths that fit and what each one needs from you and your builder. No credit pull to start.",
        ["One-time vs. two-time close comparison", "How your land equity can be used", "Builder approval and draw planning"],
        "construction",
        id="construction-scenario",
    ),
    faq("Construction Loan Questions", [
        ("What is a one-time-close construction loan?",
         "It is a single loan that funds construction of a new home and then converts to a permanent mortgage when the home is complete. You apply, qualify and close once, before construction begins."),
        ("Do I make payments during construction?",
         "CrossCountry Mortgage offers interest-only payments during the construction phase, based on the amount drawn so far, so payments start small and grow as the build progresses. Joseph will walk you through how it works for your program before you commit."),
        ("Which loan programs offer a one-time close?",
         "Conventional, FHA and VA one-time-close construction loans are available through CrossCountry Mortgage. FHA and VA are for primary residences; see <a href=\"/loan-programs/fha-va-construction-loans/\">FHA and VA construction loans</a>."),
        ("Can the loan include the cost of the lot?",
         "Often, yes. If you are buying the lot, it can typically be purchased at the same closing. If you already own it, your equity in the land may count toward the down payment."),
        ("What happens if the build runs over budget?",
         "Budgets include a contingency for a reason. Overruns are typically covered first by the contingency and then by the borrower, so Joseph helps you plan for them before you close."),
        ("Does Texas have special rules for building a home?",
         "Texas has specific requirements for construction contracts and liens, especially when the property is or will be your homestead. The lender and title company handle these requirements, which is one reason to work with a loan officer experienced with Texas construction."),
        ("How long can construction take?",
         "Programs set a maximum construction period, typically up to about a year. Joseph will confirm the window for your program and plan it against your builder's realistic schedule, with room for weather and inspections."),
        FAQ_CREDIT_PULL,
    ]),
    p("Construction financing is subject to credit approval, builder approval, property eligibility and program guidelines. Terms and availability may change.", "fine-print section-fine-print"),
)

fha_va_construction = page(
    sc('[jb_hero eyebrow="FHA & VA Construction Loans" title="Build New With FHA or VA" accent="Financing." '
       'lede="You do not have to choose between a new custom home and the benefits of an FHA or VA loan. With a one-time-close construction loan through CrossCountry Mortgage, eligible buyers can finance the lot, the build and the permanent mortgage with one closing." '
       'cta="Start My Construction Scenario" cta_url="#construction-scenario" image="photo-joseph-model-home-2.webp" image_alt="Joseph Bogdan inside a new model home"]'),
    section(
        head("Two Government-Backed Paths", "Which One Fits You?"),
        cards(
            card("FHA one-time close", "For buyers who want the more flexible credit and down-payment guidelines of an FHA loan on a home they will live in. FHA loan limits by county and FHA mortgage insurance apply."),
            card("VA one-time close", "For eligible veterans, service members and surviving spouses who want to use their VA home loan benefit to build. There is no monthly mortgage insurance; a VA funding fee applies unless you are exempt."),
            card("Conventional one-time close", "For buyers who do not need or qualify for FHA or VA, or who are building a home that will not be their primary residence.", ("Construction loans", "/loan-programs/construction-loans/")),
        ),
        tone="ivory",
    ),
    section(
        split(
            [p("How It Works", "eyebrow"),
             h("The Same One-Time Close, With Your Program’s Benefits.", 2, "section-title"),
             p("FHA and VA construction-to-permanent loans work like any one-time close: you qualify and close once, the builder is paid in draws as work is inspected, and the loan converts to a permanent 15- or 30-year FHA or VA mortgage when the home is finished. CrossCountry Mortgage offers interest-only payments during the construction phase."),
             p("Compare them in detail: <a href=\"/fha-vs-va-one-time-close-construction-loans/\">FHA vs. VA one-time-close construction loans</a>.")],
            [ul([
                "<strong>Primary residence</strong> - FHA and VA construction loans are for a home you will live in",
                "<strong>Land and build together</strong> - buy the lot and fund construction in one loan",
                "<strong>Eligible builder</strong> - your builder must meet the program's requirements; VA requires a builder with a VA builder ID",
                "<strong>Appraisal from plans</strong> - the home is valued as if complete, to program standards",
                "<strong>Set construction window</strong> - typically up to about a year to complete the home",
            ], "check-list check-list-card")],
        ),
        tone="white",
    ),
    form_section(
        "Construction Scenario",
        "Ask Joseph Whether FHA or VA Fits Your Build.",
        "Tell Joseph about your land, budget and timeline. If you are a veteran, let him know; he will check how your VA benefit applies. No credit pull to start.",
        ["FHA vs. VA vs. conventional comparison", "Builder eligibility check", "How the lot and build fit one loan"],
        "construction",
        id="construction-scenario",
    ),
    faq("FHA and VA Construction Loan Questions", [
        ("Can I use an FHA loan to build a house?",
         "Yes. An FHA one-time-close construction loan can finance the land purchase, construction and permanent mortgage in a single loan for a home you will live in. FHA loan limits, mortgage insurance and property standards apply."),
        ("Can I use my VA loan to build a home?",
         "Yes. Eligible veterans, service members and surviving spouses can use a VA one-time-close construction loan to build a primary residence. The builder must be eligible under VA requirements, including having a VA builder ID."),
        ("Does CrossCountry Mortgage offer FHA and VA construction loans in Texas?",
         "Yes. CrossCountry Mortgage offers FHA and VA one-time-close construction loans, and Joseph Bogdan originates them for North Texas buyers. Availability depends on the borrower, builder and property."),
        ("What do I pay while the home is being built?",
         "CrossCountry Mortgage offers interest-only payments during the construction phase, so payments are based on what has been drawn. Joseph will walk you through how payments work for your program before you commit."),
        ("Can I build a second home or rental with FHA or VA?",
         "No. FHA and VA construction loans are for primary residences. A conventional one-time-close loan may work for other types of property."),
        FAQ_CREDIT_PULL,
    ]),
    p("FHA and VA financing is subject to credit approval, program eligibility, builder and property eligibility and program guidelines. VA eligibility is determined by the U.S. Department of Veterans Affairs. Terms and availability may change.", "fine-print section-fine-print"),
)

lot_land = page(
    sc('[jb_hero eyebrow="Lot & Land Loans" title="Buy the Land Now. Build When You’re" accent="Ready." '
       'lede="Whether it is a lot in a new community or acreage outside town, land financing works differently from a home loan. Joseph helps you understand what lenders look for before you sign a contract on land." '
       'cta="Ask About a Lot or Land Purchase" cta_url="#construction-scenario" image="photo-joseph-national-mall.webp" image_alt="Joseph Bogdan at the Innovative Housing Showcase in Washington, D.C."]'),
    section(
        head("What Lenders Look At", "Not All Land Is Financed the Same Way."),
        cards(
            card("Improved vs. raw land", "A lot with road access and utilities in place is generally easier to finance than raw land without them."),
            card("Utilities and access", "Water or well, sewer or septic, electricity and legal road access all affect whether and how land can be financed."),
            card("Survey, flood and restrictions", "Surveys, flood zones, zoning, deed restrictions and HOA rules can limit what you can build, so they are checked early."),
            card("Your build plans", "Buying a lot you plan to build on soon can open different options than land you plan to hold for years."),
            card("Texas taxes on land", "MUD, PID and county taxes on land, and what they become once a home is built, belong in your budget from day one."),
            card("Down payment and terms", "Land loans usually require more money down and have different terms than a home mortgage. Joseph will show you what applies to your purchase."),
        ),
        tone="ivory",
    ),
    section(
        split(
            [p("Two Ways to Approach It", "eyebrow"),
             h("Buy the Lot First, or Finance It With the Build?", 2, "section-title")],
            [ul([
                "<strong>Lot loan now, construction loan later</strong> - secure the land you want, then use your equity in it toward the construction loan when you are ready to build",
                "<strong>Lot and build together</strong> - a construction-to-permanent loan can include the lot purchase at the same closing, so there is only one loan",
                "<strong>Cash for the lot</strong> - some buyers pay cash for land and use its value toward the construction loan's down payment",
            ], "check-list check-list-card"),
             p("Related: <a href=\"/loan-programs/construction-loans/\">construction loans</a> and <a href=\"/lot-and-land-loans-texas-what-to-know/\">lot and land loans in Texas: what to know first</a>.")],
        ),
        tone="white",
    ),
    form_section(
        "Lot &amp; Land Scenario",
        "Found a Lot or Acreage? Send Joseph the Details.",
        "Share the price, location and what you plan to build. Joseph will tell you what the lender will need to see and which path fits.",
        ["Whether the land is likely financeable as-is", "Lot loan vs. lot-plus-construction", "What to check before you sign"],
        "construction",
        id="construction-scenario",
    ),
    faq("Lot and Land Loan Questions", [
        ("Can I get a loan to buy a residential lot?",
         "Often, yes. Lot loans are available for many residential lots, especially improved lots with utilities and road access. Eligibility depends on the property, your credit and your plans for building."),
        ("Is it harder to finance raw land?",
         "Usually. Raw land without utilities or access carries more risk for a lender, so options are more limited and requirements are stricter. Joseph will tell you plainly what is realistic."),
        ("Can I use my land as a down payment on a construction loan?",
         "In many cases, equity in land you own can be applied toward the down payment on a construction-to-permanent loan. How much counts depends on the land's appraised value and what you owe on it."),
        ("What should I check before buying land in Texas?",
         "Confirm utilities, road access, the survey, flood zone, deed restrictions, HOA rules and the full tax picture, including any MUD or PID. A title commitment will show easements and other issues."),
        FAQ_CREDIT_PULL,
    ]),
    p("Lot and land financing is subject to credit approval, property eligibility and program guidelines. Terms and availability may change.", "fine-print section-fine-print"),
)

forward_commitments = page(
    sc('[jb_hero eyebrow="Builder Rate Programs" title="Forward Commitments That Move" accent="Inventory." '
       'lede="A forward commitment lets a builder reserve mortgage money at a set rate for buyers who close within a window. Used well, it can do more for payment-sensitive buyers than the same dollars spent on price cuts." '
       'cta="Plan a Forward Commitment" cta_url="#partner" image="photo-joseph-model-home.webp" image_alt="Joseph Bogdan touring a model home at the Innovative Housing Showcase in Washington, D.C."]'),
    section(
        head("How It Works", "Reserve the Rate Once, Use It for Many Buyers."),
        cards(
            card("1. Size the pool", "Estimate how many homes will close in the window and the total loan volume you want to cover."),
            card("2. Pay the commitment fee", "The builder pays a fee to reserve that pool of money at an agreed rate for a set period."),
            card("3. Buyers qualify and close", "Eligible buyers who qualify and close within the window receive the committed rate."),
            card("4. Track usage", "Joseph tracks which buyers are using the commitment so your team knows what remains and when it expires."),
        ),
        tone="ivory",
    ),
    section(
        split(
            [p("When It Fits", "eyebrow"),
             h("Is a Forward Commitment Right for Your Communities?", 2, "section-title"),
             p("Forward commitments work best when you have homes completing on a predictable schedule and buyers who care most about the monthly payment. They are less useful when completion dates are uncertain or when only one or two homes need help.")],
            [ul([
                "<strong>Good fit:</strong> a steady pipeline of homes completing in the same window",
                "<strong>Good fit:</strong> payment-sensitive buyers comparing new homes with resale",
                "<strong>Plan carefully:</strong> long or uncertain build schedules that may miss the window",
                "<strong>Compare first:</strong> for a single home, a buyer-specific buydown may cost less",
            ], "check-list check-list-card")],
        ),
        tone="white",
    ),
    section(
        head("Know the Trade-Offs", "What Builders Should Ask Before Committing", center=False),
        ul([
            "What happens to the fee if fewer buyers use the commitment than planned?",
            "Which loan programs and occupancy types are eligible?",
            "How is the cost counted against each buyer's seller-concession limit?",
            "Can the commitment be extended if construction runs late, and at what cost?",
            "How will rate-based advertising be reviewed for Truth in Lending compliance?",
        ], "check-list"),
        p("Compare the options: <a href=\"/forward-commitments-explained-for-builders/\">forward commitments explained</a> and <a href=\"/forward-commitment-vs-buydown-vs-price-cut/\">forward commitment vs. buydown vs. price cut</a>. Concession limits by loan type: <a href=\"/builder-incentive-limits-seller-concessions/\">seller-concession limits</a>."),
        tone="ivory",
        narrow=True,
    ),
    form_section(
        "Builder Rate Programs",
        "Let’s Model a Forward Commitment for Your Communities.",
        "Share your pipeline and price range. Joseph will review whether a forward commitment, individual buydowns or another incentive gives your buyers the most for your budget.",
        ["Pool size and timing against your build schedule", "Cost comparison with buydowns and price cuts", "Concession-limit and advertising checks"],
        "builder",
        id="partner",
    ),
    faq("Forward Commitment Questions", [
        ("What is a forward commitment in mortgage lending?",
         "It is an agreement in which a builder pays a fee to reserve a pool of mortgage money at a set interest rate for a period of time. Buyers who qualify and close within that period can use the committed rate."),
        ("Is a forward commitment the same as a rate buydown?",
         "No. A buydown is paid for one buyer's loan. A forward commitment reserves a rate for a group of future loans. Both use builder dollars to lower buyers' rates, but they differ in cost, risk and flexibility."),
        ("Do buyers have to use the builder's lender to get the committed rate?",
         "The committed rate is available through the lender that issued the commitment. Buyers remain free to choose any lender, and arrangements should be reviewed for RESPA compliance."),
        ("Can we advertise the committed rate?",
         "You can, but advertising a rate or payment triggers federal Truth in Lending disclosure requirements. Have rate-based advertising reviewed before it runs."),
    ], eyebrow="For Builders"),
    p("Forward commitment availability, terms and costs depend on market conditions and program guidelines and may change. Buyers are subject to credit approval. Builders and lenders must comply with RESPA; buyers are always free to choose their own lender.", "fine-print section-fine-print"),
)

developer = page(
    sc('[jb_hero eyebrow="Developer Financing" title="Financing Plans for the Whole" accent="Project." '
       'lede="From lots to finished homes to rentals you keep, developers need a lender who thinks about the whole project. Joseph helps developers plan lot financing, end-buyer financing and build-to-rent strategies that support the way the project actually sells." '
       'cta="Review My Project" cta_url="#construction-scenario" image="photo-joseph-national-mall.webp" image_alt="Joseph Bogdan on the National Mall at the Innovative Housing Showcase"]'),
    section(
        head("Where Joseph Helps", "Financing Built Around How the Project Sells."),
        cards(
            card("Lot sales to buyers", "Lot and construction-to-permanent loans help buyers purchase a lot in your community and build with an approved builder.", ("Lot &amp; land loans", "/loan-programs/lot-land-loans/")),
            card("End-buyer financing", "Preferred-lender programs, pre-qualification for interested buyers and a predictable path to closing for every phase.", ("Builder partnerships", "/builders-developers/")),
            card("Forward commitments", "Reserve a rate for buyers closing in a set window to support absorption when rates are working against you.", ("Forward commitments", "/builders-developers/forward-commitments/")),
            card("Build-to-rent and hold", "DSCR loans can finance completed homes you keep as rentals, qualifying on the home's rent instead of tax returns.", ("Build to sell or hold", "/build-to-rent-holding-completed-homes-dscr/")),
            card("Custom builds in your community", "Construction-to-permanent loans let buyers close once and build, with draws coordinated with the builder.", ("Construction loans", "/loan-programs/construction-loans/")),
            card("Larger project financing", "Acquisition, development and multi-home construction credit lines are reviewed project by project. Joseph will tell you plainly what fits."),
        ),
        tone="ivory",
    ),
    section(
        split(
            [p("Plan Early", "eyebrow"),
             h("Financing Questions to Answer Before Phase One.", 2, "section-title"),
             p("The way buyers will finance homes in your project affects pricing, absorption and how quickly you get capital back. Working through those questions early avoids surprises later.")],
            [ul([
                "Which loan programs fit your expected buyers and price points?",
                "Will appraisers find comparable sales for the first phase?",
                "What will MUD, PID and county taxes do to buyers' payments?",
                "Will you sell lots, finished homes, or hold some as rentals?",
                "What incentive budget does each phase need, and in what form?",
            ], "check-list check-list-card"),
             p("Read more: <a href=\"/financing-a-new-community-what-developers-should-plan/\">financing a new community: what developers should plan</a>.")],
        ),
        tone="white",
    ),
    form_section(
        "Developer Project Review",
        "Tell Joseph About Your Project.",
        "Location, lot count, price range and timeline are enough to start. Joseph will review where he can help and what each part of the plan needs.",
        ["End-buyer financing plan by phase", "Lot, construction and build-to-rent options", "Incentive strategy, including forward commitments"],
        "construction",
        id="construction-scenario",
    ),
    faq("Developer Financing Questions", [
        ("Can buyers finance a lot in our community and build later?",
         "Often, yes. Lot loans can finance the purchase now, and equity in the lot can typically be applied toward a construction-to-permanent loan when the buyer is ready to build."),
        ("Can we keep finished homes as rentals?",
         "Many developers and builders do. DSCR loans can qualify on the home's rental income, and some programs allow ownership in an LLC. Talk with your CPA and attorney about structure."),
        ("Do you finance land acquisition and development?",
         "Larger acquisition, development and construction credit facilities are reviewed project by project. Share the details and Joseph will tell you what fits the programs available through CrossCountry Mortgage."),
        ("How early should we involve a lender?",
         "Before pricing and incentives for the first phase are set. Financing affects which buyers can afford the homes and how appraisals will support the prices."),
    ], eyebrow="For Developers"),
    p("All financing is subject to credit approval, property and project eligibility and program guidelines. Terms and availability may change. Builders, developers and lenders must comply with RESPA; buyers are always free to choose their own lender.", "fine-print section-fine-print"),
)

# ---------------------------------------------------------------------------
# Manifest data
# ---------------------------------------------------------------------------
LANDING = "page-templates/landing.php"

PAGES = [
    # slug, title, parent, template, body, seo title, seo description, service, order, excerpt
    ("home", "Home", None, None, home,
     "Joseph Bogdan | Mortgage Loan Officer, Flower Mound & North Texas",
     "Joseph Bogdan, Senior Loan Officer with CrossCountry Mortgage (NMLS #2795320), helps North Texas buyers, business owners and investors finance strategically.",
     None, 0, None),
    ("get-pre-approved", "Get Pre-Approved", None, LANDING, preapproval,
     "Get Pre-Approved: Apply Online or Check Your Buying Power",
     "Apply online with CrossCountry Mortgage to get pre-approved, or start with a free buying-power analysis from Joseph Bogdan. No credit pull to start.",
     "Mortgage pre-approval", 1, None),
    ("loan-programs", "Loan Programs", None, LANDING, programs,
     "Mortgage Loan Programs by Situation | Joseph Bogdan, North Texas",
     "Find the right mortgage by starting with your goal: buying, refinancing, jumbo, self-employed or investment property financing in North Texas.",
     None, 2, None),
    ("home-purchase", "Home Purchase", "loan-programs", LANDING, purchase,
     "Home Purchase Loans & Pre-Approval in North Texas | Joseph Bogdan",
     "How much house can you afford, and can you buy before you sell? Joseph Bogdan helps North Texas buyers get a confident number and a stronger offer.",
     "Home purchase mortgage", 1, None),
    ("refinance", "Refinance & Equity", "loan-programs", LANDING, refinance,
     "Refinance & Home Equity Options in Texas | Joseph Bogdan",
     "Lower your payment, take cash out or remove mortgage insurance - Joseph Bogdan shows whether refinancing makes sense with a free equity analysis.",
     "Mortgage refinance", 2, None),
    ("jumbo-luxury-financing", "Jumbo & Luxury Financing", "loan-programs", LANDING, jumbo,
     "Jumbo & Luxury Home Financing in North Texas | Joseph Bogdan",
     "Strategic jumbo financing for high-value homes, ranches and second homes in North Texas. Request a private consultation with Joseph Bogdan.",
     "Jumbo mortgage", 3, None),
    ("self-employed-business-owners", "Self-Employed & Business Owners", "loan-programs", LANDING, self_employed,
     "Self-Employed Mortgages: Bank-Statement & 1099 | Joseph Bogdan",
     "Can you qualify for a mortgage if you’re self-employed? Joseph Bogdan, a former CEO, helps business owners choose the right documentation path.",
     "Self-employed mortgage", 4, None),
    ("investment-property", "Investment Property", "loan-programs", LANDING, investment,
     "Investment Property & DSCR Loans in Texas | Joseph Bogdan",
     "DSCR, conventional and multi-unit investment property financing. Send Joseph Bogdan your deal and get financing options that fit your portfolio.",
     "Investment property mortgage", 5, None),
    ("builders-developers", "Builders & Developers", None, LANDING, builders,
     "Preferred Lender for DFW Builders & Developers | Joseph Bogdan",
     "Responsive pre-approvals, construction-timeline coordination and one point of contact. Become a preferred lending partner with Joseph Bogdan.",
     "Builder and developer lending partnership", 3, None),
    ("realtor-partners", "Realtor Partners", None, LANDING, realtors,
     "Mortgage Partner for Realtors in DFW | Joseph Bogdan",
     "Prompt scenario reviews, strong pre-approvals and a lender who never competes for your client. Run a financing scenario for your buyer with Joseph Bogdan.",
     "Mortgage lending partnership for Realtors", 4, None),
    ("about-joseph", "About Joseph", None, LANDING, about,
     "About Joseph Bogdan | Former CEO Turned Mortgage Loan Originator",
     "Joseph Bogdan spent 30+ years building and running companies before becoming a Senior Loan Officer with CrossCountry Mortgage. See how he works.",
     None, 5, None),
    ("insights", "Insights", None, None, "",
     "Mortgage Insights & Answers | Joseph Bogdan",
     "Straight answers on home buying, mortgage strategy, jumbo loans, self-employed financing and investing in Texas real estate from Joseph Bogdan.",
     None, 6, None),
    ("contact", "Contact", None, LANDING, contact,
     "Contact Joseph Bogdan | Call, Text or Ask About Your Scenario",
     "Call Joseph Bogdan at (469) 324-4620, text (972) 672-8624, or ask about your mortgage scenario online. Based in Flower Mound, serving North Texas.",
     None, 7, None),
    ("privacy-policy", "Privacy Policy", None, None, privacy, "Privacy Policy | Joseph Bogdan, Senior Loan Officer", "How Joseph Bogdan’s website collects, uses and protects the information you submit, including contact details and text-message consent.", None, 20, None),
    ("terms-of-use", "Terms of Use", None, None, terms, "Terms of Use | Joseph Bogdan, Senior Loan Officer", "Terms for using Joseph Bogdan’s website, including the educational nature of its content and estimates, and lender licensing information.", None, 21, None),
    ("sms-terms", "Text Messaging Terms", None, None, sms, "Text Messaging Terms | Joseph Bogdan, Senior Loan Officer", "Terms for text messages from Joseph Bogdan and CrossCountry Mortgage, LLC, including consent, message frequency, rates and how to opt out.", None, 22, None),
    ("accessibility", "Accessibility", None, None, accessibility, "Accessibility Statement | Joseph Bogdan, Senior Loan Officer", "Joseph Bogdan’s commitment to an accessible website that conforms with WCAG 2.1 AA, and how to get help if any part of the site is hard to use.", None, 23, None),
    ("licensing-disclosures", "Licensing & Disclosures", None, None, licensing, "Licensing & Disclosures | Joseph Bogdan, NMLS #2795320", "Licensing and disclosures for Joseph Bogdan (Texas MLO, NMLS #2795320) and CrossCountry Mortgage, LLC (NMLS #3029), Equal Housing Opportunity Lender.", None, 24, None),
    ("texas-consumer-notice", "Texas Consumer Notice", None, None, texas, "Texas Consumer Complaint & Recovery Fund Notice | Joseph Bogdan", "Texas Department of Savings and Mortgage Lending consumer complaint and recovery fund notice for mortgage bankers and residential mortgage loan originators.", None, 25, None),
    ("builder-financing-faq", "Builder Financing FAQ", "builders-developers", LANDING, builder_faq,
     "Builder Financing FAQ: Incentives, Buyers & Closings",
     "Answers for North Texas builders on buyer pre-approvals, incentives, seller-concession limits, rate locks, appraisals and closing new construction on time.",
     "Builder financing guidance", 1, None),
    ("buyer-pre-approval-checklist", "Buyer Pre-Approval Checklist for Builders", "builders-developers", LANDING, builder_checklist,
     "Buyer Pre-Approval Checklist for Home Builders",
     "Seven things builders should verify before accepting a buyer's pre-approval, plus red flags that predict a new-construction contract that won't close.",
     None, 2, None),
    ("contract-to-close-timeline", "Contract-to-Close Timeline for New Construction", "builders-developers", LANDING, builder_timeline,
     "New Construction Contract-to-Close Timeline for Builders",
     "Every financing milestone from contract to keys on a new-construction home, mapped to the build schedule, with steps builders can take to avoid delays.",
     None, 3, None),
    ("construction-loans", "Construction Loans", "loan-programs", LANDING, construction,
     "One-Time Close Construction Loans in Texas | Joseph Bogdan",
     "Finance the lot, the build and your mortgage with one closing. Joseph Bogdan explains construction-to-permanent loans for North Texas custom homes.",
     "Construction-to-permanent (one-time close) construction loan", 6, None),
    ("fha-va-construction-loans", "FHA & VA Construction Loans", "loan-programs", LANDING, fha_va_construction,
     "FHA & VA One-Time Close Construction Loans in Texas",
     "Build a new home with an FHA or VA one-time-close construction loan through CrossCountry Mortgage. Joseph Bogdan explains eligibility, builders and draws.",
     "FHA and VA one-time-close construction loan", 7, None),
    ("lot-land-loans", "Lot & Land Loans", "loan-programs", LANDING, lot_land,
     "Lot & Land Loans in North Texas | Joseph Bogdan",
     "Buying a residential lot or acreage to build on? Learn how lot and land loans work in Texas and what lenders check before you sign a land contract.",
     "Lot and land loan", 8, None),
    ("forward-commitments", "Forward Commitments for Builders", "builders-developers", LANDING, forward_commitments,
     "Builder Forward Commitments: Rate Programs for Buyers",
     "How builder forward commitments reserve a mortgage rate for buyers closing in a set window, what they cost, and when they beat buydowns or price cuts.",
     "Builder forward commitment rate program", 4, None),
    ("developer-financing", "Developer & Build-to-Rent Financing", "builders-developers", LANDING, developer,
     "Developer & Build-to-Rent Financing in DFW | Joseph Bogdan",
     "Lot, construction, end-buyer and build-to-rent financing plans for North Texas developers. Request a project review with Joseph Bogdan.",
     "Developer and build-to-rent financing", 5, None),
]

MENUS = {
    "primary": [
        ("Builders & Developers", "builders-developers", [
            ("Forward Commitments", "forward-commitments"),
            ("Developer & Build-to-Rent", "developer-financing"),
            ("Builder Financing FAQ", "builder-financing-faq"),
            ("Buyer Pre-Approval Checklist", "buyer-pre-approval-checklist"),
            ("Contract-to-Close Timeline", "contract-to-close-timeline"),
        ]),
        ("Loan Programs", "loan-programs", [
            ("Home Purchase", "home-purchase"),
            ("Refinance & Equity", "refinance"),
            ("Jumbo & Luxury Financing", "jumbo-luxury-financing"),
            ("Self-Employed & Business Owners", "self-employed-business-owners"),
            ("Investment Property", "investment-property"),
            ("Construction Loans", "construction-loans"),
            ("FHA & VA Construction Loans", "fha-va-construction-loans"),
            ("Lot & Land Loans", "lot-land-loans"),
        ]),
        ("Realtor Partners", "realtor-partners", []),
        ("About Joseph", "about-joseph", []),
        ("Insights", "insights", []),
        ("Contact", "contact", []),
    ],
    "footer": [
        ("Get Pre-Approved", "get-pre-approved", []),
        ("Loan Programs", "loan-programs", []),
        ("Builders & Developers", "builders-developers", []),
        ("Realtor Partners", "realtor-partners", []),
        ("About Joseph", "about-joseph", []),
        ("Insights", "insights", []),
        ("Contact", "contact", []),
    ],
    "legal": [
        ("Privacy Policy", "privacy-policy", []),
        ("Terms of Use", "terms-of-use", []),
        ("Text Messaging Terms", "sms-terms", []),
        ("Licensing & Disclosures", "licensing-disclosures", []),
        ("Texas Consumer Notice", "texas-consumer-notice", []),
        ("Accessibility", "accessibility", []),
    ],
}

CATEGORIES = [
    ("home-buying", "Home Buying", "Straight answers for North Texas home buyers on affordability, pre-approval, buying before selling and making offers that sellers take seriously."),
    ("mortgage-strategy", "Mortgage Strategy", "How to structure a mortgage around your goals: refinancing, home equity, loan terms and building a pre-approval that helps you win the home you want."),
    ("texas-housing-market", "Texas Housing & Market", "What North Texas buyers should know about property taxes, insurance, new construction and local market conditions."),
    ("luxury-jumbo", "Luxury & Jumbo", "How jumbo loans work and how to prepare to finance high-value homes, ranches, acreage and second homes in North Texas with confidence."),
    ("business-owners", "Business Owners & Self-Employed", "How self-employed borrowers and business owners qualify for a mortgage, from tax-return income to bank-statement, 1099 and asset-based programs."),
    ("real-estate-investing", "Real Estate Investing", "Financing rental and investment property in Texas: DSCR loans, conventional investor loans, cash-out strategies and growing a portfolio."),
    ("construction-land", "Construction & Land Loans", "How one-time-close construction loans, lot and land loans and draw schedules work for North Texas buyers building a custom home."),
    ("builders-new-construction", "Builders & New Construction", "Mortgage strategy for North Texas home builders and their sales teams: incentives, buyer pre-approvals, closing timelines and new-construction financing."),
]

# Who each service page is for (Service.audience in structured data).
AUDIENCE = {
    "get-pre-approved": "Home buyers",
    "home-purchase": "Home buyers, including first-time and move-up buyers",
    "refinance": "Homeowners",
    "jumbo-luxury-financing": "Luxury and high-value home buyers",
    "self-employed-business-owners": "Self-employed borrowers and business owners",
    "investment-property": "Real estate investors",
    "builders-developers": "Home builders and developers",
    "builder-financing-faq": "Home builders, developers and their sales teams",
    "realtor-partners": "Real estate agents",
    "construction-loans": "Buyers building a custom or new home",
    "fha-va-construction-loans": "FHA borrowers and eligible veterans, service members and surviving spouses building a primary residence",
    "lot-land-loans": "Buyers purchasing a residential lot or land to build on",
    "forward-commitments": "Home builders and their sales teams",
    "developer-financing": "Residential developers and build-to-rent operators",
}

# Pages whose URL changed; the sync renames the existing page instead of creating a duplicate.
OLD_SLUGS = {
    "about-joseph": ["about-joe"],
}
