"""Page copy for joebogdanlo. Run `python3 tools/build.py` to regenerate content/.

Copy rules (from the conversion brief):
- Lead with the visitor's problem; products support the answer.
- Every section builds trust, names a problem, gives value or moves to action.
- Joseph is a Mortgage Loan Originator only: no real-estate representation language.
- No manufactured social proof, no rate promises, no "guaranteed" approvals.
"""
from blocks import (button, buttons, card, cards, faq, form_section, group, h, head, p, page, sc,
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
       'cta="Become a Preferred Lending Partner" cta_url="#partner" image="joe-headshot.webp"]'),
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
            [sc('[jb_photo file="strategy.webp" alt="Reviewing financing strategy" class="photo-landscape"]'),
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
]

MENUS = {
    "primary": [
        ("Builders & Developers", "builders-developers", []),
        ("Loan Programs", "loan-programs", [
            ("Home Purchase", "home-purchase"),
            ("Refinance & Equity", "refinance"),
            ("Jumbo & Luxury Financing", "jumbo-luxury-financing"),
            ("Self-Employed & Business Owners", "self-employed-business-owners"),
            ("Investment Property", "investment-property"),
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
    "realtor-partners": "Real estate agents",
}

# Pages whose URL changed; the sync renames the existing page instead of creating a duplicate.
OLD_SLUGS = {
    "about-joseph": ["about-joe"],
}
