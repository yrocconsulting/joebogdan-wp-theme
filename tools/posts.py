"""Insights articles. Run `python3 tools/build.py` to regenerate content/.

Article rules:
- Answer the question in the first paragraph (what search and AI assistants quote).
- Question-style H2s, a key-takeaways box, an FAQ (emits FAQPage schema).
- One relevant next action mid-article; the theme adds a closing CTA by topic.
- Compliance: no rates, APRs, payment amounts or down-payment figures (Regulation Z
  triggering terms), no guarantees, and only programs Joe offers in Texas.
"""
from blocks import group, h, ol, p, sc, ul


def lead(text):
    return p(text, "lead-answer")


def takeaways(items):
    return group(h("Key takeaways", 2), ul(items, "check-list"), cls="callout")


def cta(title, text, url, label):
    return sc(f'[jb_inline_cta title="{title}" text="{text}" url="{url}" label="{label}"]')


def faq(qas, title="Frequently asked questions"):
    items = "".join(f'[jb_q q="{q}"]{a}[/jb_q]' for q, a in qas)
    return sc(f'[jb_faq inline="yes" title="{title}"]{items}[/jb_faq]')


def body(*blocks):
    return "\n\n".join(blocks) + "\n"


BUYING_POWER_CTA = cta("Want your real number?",
                       "Joe will turn your income, savings and goals into a personalized buying-power analysis. Free, about two minutes, no credit pull.",
                       "/get-pre-approved/", "Discover Your Buying Power")

POSTS = []


def post(slug, title, category, excerpt, seo_title, image, content):
    POSTS.append({
        "slug": slug, "title": title, "category": category, "excerpt": excerpt,
        "seo_title": seo_title, "seo_description": excerpt, "image": image, "content": content,
    })


# ---------------------------------------------------------------------------
post(
    "how-much-house-can-i-afford-north-texas",
    "How Much House Can I Afford in North Texas?",
    "home-buying",
    "What you can afford depends on income, debts, savings, credit and Texas property taxes and insurance. Here is how lenders calculate it and how to find a number you are comfortable with.",
    "How Much House Can I Afford in North Texas? | Joe Bogdan",
    "buyers.webp",
    body(
        lead("How much house you can afford comes down to five things: your gross income, your monthly debts, the cash you have for a down payment and closing costs, your credit, and the full monthly cost of the home — including Texas property taxes and homeowners insurance. Lenders turn those into a maximum. The more useful question is what price keeps your monthly budget comfortable."),
        takeaways([
            "Lenders compare your total monthly debts, including the new house payment, with your gross monthly income.",
            "In Texas, property taxes and insurance are a large share of the monthly payment, so the same price can cost very different amounts in different neighborhoods.",
            "Being approved for a price is not the same as being comfortable at that price.",
            "A personalized analysis based on your real numbers beats an online calculator.",
        ]),
        h("How do lenders decide how much I can borrow?"),
        p("Most lenders start with your <strong>debt-to-income ratio (DTI)</strong>: your monthly debt payments divided by your gross monthly income. Debts include car loans, student loans, minimum credit card payments and the proposed housing payment. Rent you will stop paying once you buy is not counted."),
        p("A common rule of thumb is to keep housing costs around 28% of gross monthly income and total debts around 36%. Many loan programs allow higher ratios for well-qualified borrowers, but just because a program allows more does not mean you should borrow it."),
        p("Lenders also look at credit history, the stability and type of your income, how much you are putting down and how much you will have in reserve after closing."),
        h("Why do Texas property taxes matter so much?"),
        p("Texas has no state income tax, and local property taxes help make up the difference. Your monthly mortgage payment usually includes an escrow for property taxes and homeowners insurance, and in North Texas those two items can be a substantial part of the total."),
        p("Taxes vary by county, city, school district and special districts. Many newer DFW subdivisions sit inside a <strong>Municipal Utility District (MUD)</strong> or <strong>Public Improvement District (PID)</strong>, which add to the tax bill. Two homes at the same price can have very different monthly costs, so it is worth checking the full tax rate for any home you are serious about."),
        BUYING_POWER_CTA,
        h("What else affects my budget?"),
        ul([
            "<strong>Mortgage insurance</strong> — conventional loans with a smaller down payment usually include private mortgage insurance; FHA loans have their own mortgage insurance.",
            "<strong>HOA dues</strong> — common in planned communities and counted in your DTI.",
            "<strong>Closing costs and prepaid items</strong> — set aside cash beyond your down payment, including initial escrow deposits.",
            "<strong>Reserves</strong> — having savings left after closing makes your file stronger and your life less stressful.",
        ]),
        h("Approved amount vs. comfortable amount"),
        p("Start with the monthly payment that fits your life — savings goals, childcare, travel, business swings — then work backward to a price. Joe’s buying-power analysis shows both: what you may qualify for and the range that keeps your monthly budget where you want it."),
        h("How do I get a reliable number?"),
        ol([
            "Gather the basics: income, monthly debts, savings and a rough credit estimate.",
            "Get a personalized analysis instead of relying on a generic calculator.",
            "Turn it into a documented pre-approval before you start making offers.",
        ]),
        faq([
            ("Does Texas have a state income tax?", "No. Texas does not have a state income tax, but local property taxes are relatively high, which affects your monthly mortgage payment through escrow."),
            ("What is a MUD or PID tax?", "Municipal Utility Districts and Public Improvement Districts fund infrastructure in many newer Texas neighborhoods. They add to a home’s property tax rate, so check whether a home is in one before you make an offer."),
            ("Is it better to put more money down?", "Not always. A larger down payment can reduce your loan amount and mortgage insurance, but keeping cash in reserve also has value. Joe can show you the trade-offs with your actual numbers."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "buy-a-new-home-before-selling",
    "Can I Buy a New Home Before Selling My Current One?",
    "home-buying",
    "Often, yes. Depending on your income, equity and reserves you may qualify carrying both homes or use your current home’s equity. Here are the options and the trade-offs.",
    "Can I Buy a Home Before Selling My Current One? | Joe Bogdan",
    "strategy.webp",
    body(
        lead("Often, yes. Whether you can buy before you sell depends on three things: whether your income can support both housing payments for a period of time, how much equity you have in your current home, and how much cash you have in reserve. If you can qualify with both payments, you can make a non-contingent offer. If not, there are other ways to bridge the gap."),
        takeaways([
            "Buying first avoids a double move and lets you make a stronger offer.",
            "The key question is whether you qualify carrying both payments.",
            "Your current home’s equity can help fund the next down payment, but Texas has specific rules for borrowing against a homestead.",
            "Plan the strategy before you start touring, not after you find the house.",
        ]),
        h("Option 1: Qualify with both payments"),
        p("If your income, credit and reserves support your current payment plus the new one, you can buy first and sell afterward. This is usually the cleanest path, and it lets your offer compete without a home-sale contingency. Your savings need to cover the down payment and closing costs on the new home while your equity is still tied up in the old one."),
        h("Option 2: Use the equity in your current home"),
        p("If most of your down payment is tied up in your current home, you may be able to access that equity before you sell. In Texas, home equity loans and lines of credit on a homestead follow specific state rules, including limits on how much you can borrow against the home’s value and required waiting periods, so timing matters. Joe will walk through which options fit your situation and timeline."),
        h("Option 3: Make an offer contingent on selling"),
        p("A home-sale contingency protects you if your current home does not sell, but many sellers see it as a weaker offer. It works best in slower markets, with new construction or when your current home is already under contract."),
        h("Option 4: Sell first and rent back"),
        p("Some sellers negotiate a short leaseback after closing so they can stay in the home while they buy. You get your equity in hand first, but you need a buyer willing to agree to it and you may need short-term housing if timelines slip."),
        cta("Planning a move-up purchase?", "Tell Joe about your current home and your next one. He will outline which buy-before-you-sell options fit.", "/contact/", "Ask Joe About Your Scenario"),
        h("Questions to answer before you start"),
        ul([
            "Can you comfortably carry two payments for a few months if needed?",
            "How much equity do you realistically have after selling costs?",
            "How competitive is the market for the home you want?",
            "Is the next home new construction, with a longer timeline?",
        ]),
        h("Bring your Realtor into the plan"),
        p("Your agent’s offer strategy depends on your financing strategy. When Joe and your Realtor coordinate early, your offer reflects what you can actually do, and there are fewer surprises after you go under contract."),
        faq([
            ("Will my current mortgage count against me when I buy?", "Yes, unless your current home is sold or under contract with conditions satisfied, lenders generally count the existing payment in your debt-to-income ratio."),
            ("Can rental income from my current home help me qualify?", "Sometimes. If you plan to keep and rent your current home, some programs allow a portion of the expected rent to count, with documentation such as a lease. Joe will tell you what applies."),
            ("Is a contingent offer a bad idea?", "Not necessarily. It depends on the market and the seller. In a competitive situation, qualifying without the contingency is usually stronger."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "self-employed-mortgage-how-lenders-calculate-income",
    "Can I Get a Mortgage if I’m Self-Employed? How Lenders Look at Business Income",
    "business-owners",
    "Yes. Lenders usually average two years of self-employed income from tax returns, with add-backs such as depreciation. If write-offs shrink your income, bank-statement and other Non-QM programs may fit.",
    "Self-Employed Mortgage: How Lenders Calculate Business Income | Joe Bogdan",
    "business-owners.webp",
    body(
        lead("Yes, self-employed borrowers qualify for mortgages every day. For most traditional loans, lenders average your income from the last two years of personal and business tax returns, add back certain non-cash deductions like depreciation, and look at whether income is stable or growing. If deductions make your taxable income much lower than what your business really produces, alternative-documentation programs may be a better fit."),
        takeaways([
            "Traditional loans usually use two years of tax returns, averaged.",
            "Some deductions, such as depreciation, can be added back to qualifying income.",
            "Declining income gets extra scrutiny.",
            "Bank-statement and other Non-QM programs qualify you differently, with different pricing and requirements.",
            "Talk to a loan officer before you file your next return.",
        ]),
        h("What documents do lenders ask for?"),
        p("For a traditional (full-documentation) loan, expect to provide personal tax returns, and business returns if you own a significant share of the business, along with schedules such as Schedule C or K-1s. Lenders may also ask for a year-to-date profit and loss statement and business bank statements."),
        h("How is self-employed income calculated?"),
        p("Lenders start with the net income on your returns, then add back certain non-cash or non-recurring items, such as depreciation, depletion and some one-time expenses. The result is usually averaged over two years. If this year’s income is lower than last year’s, the lender may use the lower figure or ask for an explanation."),
        p("This is where many business owners get surprised: deductions that save on taxes also lower qualifying income. That is not a reason to change your tax strategy without your CPA, but it is a reason to plan."),
        h("What if I have been self-employed less than two years?"),
        p("Some programs consider a shorter history if you have previous experience in the same line of work, for example a nurse who opened a practice or a salesperson who became an independent agent. The details matter, so get your scenario reviewed early."),
        cta("Self-employed and planning a purchase?", "Request a Self-Employed Mortgage Strategy Review. Joe will show you which documentation path fits.", "/loan-programs/self-employed-business-owners/#strategy-review", "Request a Strategy Review"),
        h("What are bank-statement loans and other Non-QM options?"),
        p("Non-QM (non-qualified mortgage) programs use alternative documentation. A <strong>bank-statement loan</strong> calculates income from business or personal deposits over a set period instead of tax returns. <strong>Asset-based</strong> programs look at significant liquid assets. These programs exist for borrowers whose finances do not fit standard guidelines, and their pricing and requirements typically differ from conventional loans. Joe will compare them side by side with traditional options."),
        h("How to prepare"),
        ol([
            "Talk to a loan officer before you file, especially if you expect large write-offs.",
            "Keep business and personal accounts separate and clean.",
            "Have a year-to-date profit and loss statement ready.",
            "Document large deposits and transfers.",
            "Loop in your CPA so tax and mortgage strategy work together.",
        ]),
        p("Joe built and ran companies for more than 30 years before becoming a loan officer. He has been on the business-owner side of these conversations and knows how to present your file clearly."),
        faq([
            ("Do I need two years of tax returns to get a mortgage?", "For most traditional loans, yes. Some programs allow a shorter self-employment history with prior experience in the same field, and alternative-documentation programs qualify you differently."),
            ("Can I use business funds for my down payment?", "Often, yes, with documentation. Lenders may want to confirm that withdrawing the funds will not hurt the business. Plan this before you move money."),
            ("Is a bank-statement loan more expensive?", "Non-QM programs typically have different pricing and requirements than conventional loans. Whether one makes sense depends on how much more income it lets you document. Joe will compare the options with you."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "what-makes-a-jumbo-loan-different",
    "What Makes a Jumbo Loan Different — and How to Prepare",
    "luxury-jumbo",
    "Jumbo loans exceed the conforming loan limit, so lenders set their own standards for credit, reserves, documentation and appraisals. Preparation shapes your terms and flexibility.",
    "What Is a Jumbo Loan and How Do I Qualify? | Joe Bogdan",
    "luxury.webp",
    body(
        lead("A jumbo loan is a mortgage larger than the conforming loan limit set each year by the Federal Housing Finance Agency. Because these loans cannot be sold to Fannie Mae or Freddie Mac, lenders set their own standards, which usually means closer review of credit, cash reserves, asset documentation and the appraisal. Strong preparation can improve your options and make the process smoother."),
        takeaways([
            "Jumbo means above the conforming limit, which FHFA updates every year.",
            "Expect more documentation of income and assets, and higher reserve expectations.",
            "How you structure the down payment and how much liquidity you keep are strategic choices.",
            "High-value, unique and acreage properties can make appraisals more complex.",
        ]),
        h("What counts as a jumbo loan?"),
        p("Any loan amount above the conforming loan limit for the county is considered jumbo. The limit changes each year and is higher in some high-cost areas. You can find the current limits on the <a href=\"https://www.fhfa.gov/data/conforming-loan-limit\" target=\"_blank\" rel=\"noopener\">FHFA website</a>, or Joe can confirm whether your loan amount falls into jumbo territory."),
        h("How is qualifying for a jumbo loan different?"),
        ul([
            "<strong>Credit</strong> — lenders typically look for strong credit histories.",
            "<strong>Reserves</strong> — you will usually need several months of payments in savings or investments after closing.",
            "<strong>Asset documentation</strong> — expect to document where your down payment and reserves come from, including brokerage and retirement accounts.",
            "<strong>Income</strong> — complex income from business ownership, bonuses, commissions or investments needs careful presentation.",
            "<strong>Appraisal</strong> — higher-value and unique homes can be harder to value, and some lenders require additional review.",
        ]),
        cta("Considering a high-value purchase?", "Request a private jumbo financing consultation before you go under contract.", "/loan-programs/jumbo-luxury-financing/#consultation", "Request a Consultation"),
        h("Down payment vs. liquidity: a strategic choice"),
        p("With large loans, how much you put down is a real decision. A larger down payment can reduce the loan amount, while keeping more cash or investments can protect flexibility for your business, other properties or opportunities. There is no single right answer. Joe helps you weigh it the way a CFO would."),
        h("Ranches, acreage and second homes"),
        p("North Texas buyers often look at properties with acreage, outbuildings or agricultural use. These features can affect which programs fit and how the property is appraised. Second homes have their own occupancy rules. Share the property details early so the financing plan matches the property."),
        h("How to prepare"),
        ol([
            "Organize two years of income documentation and recent statements for every account you plan to use.",
            "Avoid moving large sums between accounts without a paper trail.",
            "Decide how much liquidity you want to keep after closing.",
            "Get a pre-approval before you shop, especially for competitive listings.",
        ]),
        faq([
            ("Is a jumbo loan harder to get?", "Requirements are usually stricter and documentation is deeper, but well-prepared borrowers qualify regularly. The key is organizing income and asset documentation early."),
            ("Can I get a jumbo loan if I am self-employed?", "Yes, though documentation is especially important. Joe will help you present business income clearly and compare program options."),
            ("Can I use a jumbo loan for a second home?", "Often, yes. Second-home financing has its own occupancy and reserve requirements, which Joe will walk through with you."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "dscr-loans-explained",
    "DSCR Loans Explained: Qualifying for a Rental Property Based on Its Income",
    "real-estate-investing",
    "A DSCR loan qualifies an investment property mainly on whether its rent covers the mortgage payment, taxes, insurance and HOA dues — not on your personal tax returns.",
    "DSCR Loans Explained for Texas Real Estate Investors | Joe Bogdan",
    "strategy.webp",
    body(
        lead("A DSCR (debt-service coverage ratio) loan is an investment-property mortgage that qualifies mainly on the property’s rental income instead of your personal income. The lender divides the property’s monthly rent by its monthly housing expense — principal, interest, taxes, insurance and any HOA dues. If the rent covers the expense, the property supports the loan."),
        takeaways([
            "DSCR = monthly rent ÷ monthly principal, interest, taxes, insurance and HOA.",
            "A ratio of 1.0 means rent exactly covers the payment; above 1.0 means it covers more.",
            "Personal tax returns are usually not the main qualifying factor.",
            "DSCR loans are Non-QM programs, with different pricing and requirements than conventional investor loans.",
        ]),
        h("How is the DSCR calculated?"),
        p("Take the property’s monthly rent, from a current lease or an appraiser’s market-rent estimate, and divide it by the full monthly housing expense. If rent is 25% higher than the expense, the ratio is 1.25. If rent only covers 90% of the expense, the ratio is 0.90. Requirements vary by program, and stronger ratios generally give you more options."),
        h("Who are DSCR loans for?"),
        ul([
            "Investors whose tax returns show low income because of depreciation and write-offs",
            "Self-employed investors with complex income",
            "Investors growing a portfolio who do not want each new property tied to personal DTI",
            "Buyers using an LLC, where the program allows it",
        ]),
        cta("Running numbers on a property?", "Send Joe the price, expected rent and cash available. He will reply with the financing options that fit.", "/loan-programs/investment-property/#investor-scenario", "Run an Investor Scenario"),
        h("DSCR vs. conventional investment loans"),
        p("A conventional investment-property loan uses your personal income, debts and tax returns, much like a home loan. It may have different pricing than a DSCR loan, but it counts against your personal DTI, and it can get harder to use as you add properties. A DSCR loan focuses on the property. Many investors use both at different stages."),
        h("What about Texas property taxes?"),
        p("Taxes and insurance are part of the DSCR calculation, so high-tax areas reduce the ratio. Check the full tax rate, including any MUD or PID, before you run your numbers on a North Texas rental."),
        faq([
            ("Do DSCR loans require tax returns?", "Usually personal income is not the main qualifying factor, though you will still need credit, assets for the down payment and reserves, and documentation on the property."),
            ("Can I use a DSCR loan for a short-term rental?", "Some programs allow it, using short-term rental income data. Requirements vary, so share the property details with Joe."),
            ("Can I close in an LLC?", "Some DSCR programs allow LLC vesting. Talk with your attorney and CPA about the legal and tax implications."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "texas-property-taxes-homestead-exemption-mortgage",
    "Texas Property Taxes, Homestead Exemptions and Your Mortgage Payment",
    "texas-housing-market",
    "Property taxes are a big part of a Texas mortgage payment. Here is how escrow works, why MUD and PID taxes matter, and how the homestead exemption and protests can lower your bill.",
    "Texas Property Taxes & Homestead Exemption: What Buyers Should Know | Joe Bogdan",
    "buyers.webp",
    body(
        lead("In Texas, property taxes are usually one of the largest parts of a monthly mortgage payment. Most lenders collect them through an escrow account along with homeowners insurance. Your bill depends on the home’s appraised value and the combined tax rate of every taxing entity, including any MUD or PID. Filing for your homestead exemption and reviewing your appraisal each year can help keep it in check."),
        takeaways([
            "Your payment usually includes escrow for property taxes and homeowners insurance.",
            "The total tax rate combines county, city, school district and special districts.",
            "MUD and PID taxes are common in newer DFW neighborhoods.",
            "File your homestead exemption with your county appraisal district once the home is your primary residence.",
            "Escrow payments can change each year when taxes or insurance change.",
        ]),
        h("How does escrow work?"),
        p("Each month, part of your payment goes into an escrow account. When property tax and insurance bills come due, your loan servicer pays them. Once a year the servicer reviews the account. If taxes or insurance went up, your monthly payment may rise to cover the shortage. If they went down, it may decrease."),
        h("What makes up a Texas property tax bill?"),
        p("Your bill is the appraised value, minus any exemptions, multiplied by the combined rate of every taxing entity where the home is located: county, city, school district, community college and special districts. In many newer North Texas subdivisions, a <strong>Municipal Utility District (MUD)</strong> or <strong>Public Improvement District (PID)</strong> adds to the rate to pay for roads, water and other infrastructure."),
        BUYING_POWER_CTA,
        h("What is the homestead exemption?"),
        p("A homestead exemption reduces the taxable value of your primary residence for school district and some other taxes, and limits how much the taxable value of a homestead can rise each year. Additional exemptions may apply for homeowners who are 65 or older, disabled, or disabled veterans. You apply through your county appraisal district, such as the Denton, Tarrant, Dallas or Collin Central Appraisal District. Check with your district for current exemption amounts and filing timelines."),
        h("Can I protest my appraisal?"),
        p("Yes. Each spring, appraisal districts send notices of appraised value. If you believe the value is too high, you can file a protest by the deadline on your notice, usually in the spring. Recent sales of comparable homes are the most persuasive evidence."),
        h("What this means when you are house hunting"),
        ul([
            "Ask for the full tax rate, not just the price, on every home you are considering.",
            "Budget based on the purchase price, because the appraised value often resets after a sale.",
            "In new construction, taxes in the first year may be based on the lot only, so expect an increase once the home is assessed.",
        ]),
        faq([
            ("When can I file for a Texas homestead exemption?", "You can generally apply once the home is your principal residence. Check your county appraisal district’s website for current forms and timing."),
            ("Why did my mortgage payment go up if my rate is fixed?", "A fixed rate keeps principal and interest the same, but escrow for taxes and insurance can change each year. Higher taxes or insurance premiums increase the escrow portion of the payment."),
            ("Are taxes higher in new construction neighborhoods?", "Often, because of MUD or PID taxes and because the first-year bill may reflect only the land value. Check the full rate before you buy."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "when-does-refinancing-make-sense",
    "When Does Refinancing Make Sense? How to Find Your Break-Even Point",
    "mortgage-strategy",
    "Refinancing makes sense when the benefit outweighs the cost within the time you plan to keep the loan. Here is how to calculate your break-even point and what Texas cash-out rules mean.",
    "When Does Refinancing Make Sense? Break-Even & Texas Cash-Out Rules | Joe Bogdan",
    "strategy.webp",
    body(
        lead("Refinancing makes sense when what you gain — a lower payment, a shorter term, removing mortgage insurance or accessing equity — is worth more than what it costs, within the time you expect to keep the loan. The simplest test is your break-even point: total closing costs divided by your monthly savings tells you how many months it takes to come out ahead."),
        takeaways([
            "Break-even months = closing costs ÷ monthly savings.",
            "If you will sell or refinance again before the break-even point, it may not be worth it.",
            "Cash-out refinancing on a Texas homestead follows specific state rules.",
            "Sometimes the best advice is to wait. Joe will tell you if that is the case.",
        ]),
        h("How do I calculate the break-even point?"),
        p("Add up the closing costs of the new loan. Then compare your new monthly principal and interest payment with your current one. Divide the costs by the monthly savings. If you plan to stay in the home well beyond that number of months, the refinance may make sense. Also consider the total interest over the life of each loan, not just the monthly payment."),
        h("Common reasons to refinance"),
        ul([
            "<strong>Lower the monthly payment</strong> when market conditions or your credit have improved",
            "<strong>Remove mortgage insurance</strong> after your home has gained value",
            "<strong>Shorten the term</strong> to pay off the home sooner",
            "<strong>Move from an adjustable rate to a fixed rate</strong> for stability",
            "<strong>Access equity</strong> for renovations, debt consolidation or other goals",
        ]),
        cta("Curious what your equity could do?", "Get a free Refinance & Equity Analysis. You will see an estimate of accessible equity right away.", "/loan-programs/refinance/#refinance-analysis", "Get My Analysis"),
        h("What should I know about cash-out refinancing in Texas?"),
        p("Texas has some of the most specific home-equity rules in the country. A cash-out refinance of a homestead is governed by the Texas Constitution, which limits how much of the home’s value can be borrowed against, requires waiting periods before closing, sets rules about where the loan can close and limits how often you can do one. These rules protect homeowners, but they affect timing and options, so plan ahead."),
        p("If you only need a portion of your equity, a home equity loan or line of credit that leaves your first mortgage in place may be worth comparing."),
        h("When waiting is the better choice"),
        p("If you are planning to move soon, if the savings are small relative to costs, or if your credit is about to improve, waiting may serve you better. A good loan officer will say so."),
        faq([
            ("How much does it cost to refinance?", "Costs vary with the loan amount, title and appraisal fees and other factors. Joe will give you an itemized estimate so you can calculate your break-even point accurately."),
            ("Can I remove PMI without refinancing?", "Often, yes, on conventional loans once you reach enough equity based on the original value or a new appraisal. FHA mortgage insurance usually requires a refinance to remove. Joe can check which applies to you."),
            ("How often can I do a cash-out refinance in Texas?", "Texas limits how frequently a homestead can be used for a cash-out loan. Joe will review your loan history and the current rules with you."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "what-makes-a-strong-pre-approval",
    "What Makes a Pre-Approval Letter Strong? A Guide for Buyers and Agents",
    "mortgage-strategy",
    "Not all pre-approvals are equal. A strong one is based on verified income, assets and credit, matches the offer, and comes from a loan officer the listing agent can reach.",
    "What Makes a Strong Mortgage Pre-Approval? | Joe Bogdan",
    "buyers.webp",
    body(
        lead("A strong pre-approval is based on documents that have actually been reviewed — income, assets and credit — not just numbers the buyer typed into a form. It is tailored to the offer, it comes from a loan officer the listing agent can reach, and it has no surprises waiting in underwriting. To sellers and their agents, that combination signals that the buyer can close."),
        takeaways([
            "Pre-qualification is an estimate; pre-approval is based on verified information.",
            "Letters should match the offer price and loan type.",
            "Listing agents value a loan officer who answers questions quickly and clearly.",
            "Issues found before the offer are much easier to solve than issues found after.",
        ]),
        h("Pre-qualification vs. pre-approval"),
        p("A <strong>pre-qualification</strong> is a quick estimate based on what you tell the lender. A <strong>pre-approval</strong> means your credit has been reviewed and your income and asset documents have been checked. A pre-approval takes a little more effort up front, and it is what serious sellers expect."),
        h("What sellers and listing agents look for"),
        ul([
            "A letter from a lender they recognize or can easily verify",
            "A loan amount and program that match the offer",
            "Confidence that income and assets were actually reviewed",
            "A loan officer who will pick up the phone and explain the file",
        ]),
        cta("Ready to shop with a strong letter?", "Start with your buying-power analysis. Joe will turn it into a documented pre-approval.", "/get-pre-approved/", "Discover Your Buying Power"),
        h("For Realtors: what to ask your buyer’s lender"),
        ol([
            "Has the buyer’s income and asset documentation been reviewed, or only stated?",
            "Is there anything in the file that could cause a delay, such as a recent job change, large deposits or a home to sell?",
            "Will you call the listing agent if it helps the offer?",
            "How will you keep me updated through closing?",
        ]),
        p("Joe works exclusively as a mortgage loan originator. He does not sell real estate, so referring your clients to him never puts your relationship at risk. Agents can <a href=\"/realtor-partners/#client-scenario\">send a client scenario</a> before writing an offer."),
        h("What buyers can do to keep a pre-approval strong"),
        ul([
            "Avoid new credit accounts or large purchases before closing.",
            "Do not change jobs without talking to your loan officer first.",
            "Document large deposits and keep funds in the same accounts.",
            "Respond quickly when the lender asks for updated documents.",
        ]),
        faq([
            ("How long is a pre-approval good for?", "Pre-approvals are time-limited, because credit reports and documents age. If your search runs longer, your loan officer can update it with fresh documents."),
            ("Does getting pre-approved hurt my credit?", "A pre-approval typically includes a credit check, which can have a small effect. Joe’s buying-power analysis on this site does not pull credit, and he will tell you before any credit check happens."),
            ("Should the pre-approval show my maximum amount?", "Not necessarily. Many buyers ask for a letter that matches each offer so the seller does not see their ceiling. Joe can issue letters tailored to the offer."),
        ]),
    ),
)

# Search titles/descriptions (excerpts above are the longer card summaries).
SEO = {
    "how-much-house-can-i-afford-north-texas": ("How Much House Can I Afford in North Texas? | Joe Bogdan",
        "How lenders decide what you can afford, why Texas property taxes matter so much, and how to find a price that keeps your budget comfortable."),
    "buy-a-new-home-before-selling": ("Can I Buy a Home Before Selling My Current One? | Joe Bogdan",
        "Often, yes. Learn the four ways to buy your next home before selling, including Texas rules for using equity, and how to choose the right one."),
    "self-employed-mortgage-how-lenders-calculate-income": ("Self-Employed Mortgages: How Lenders Count Income | Joe Bogdan",
        "How lenders calculate self-employed income from tax returns, which deductions add back, and when bank-statement or Non-QM loans fit better."),
    "what-makes-a-jumbo-loan-different": ("What Is a Jumbo Loan and How Do I Qualify? | Joe Bogdan",
        "Jumbo loans exceed the conforming limit, so credit, reserves, documentation and appraisals get closer review. Here is how to prepare."),
    "dscr-loans-explained": ("DSCR Loans Explained for Texas Investors | Joe Bogdan",
        "How DSCR loans qualify a rental property on its own income, how the ratio is calculated, and how they compare with conventional investor loans."),
    "texas-property-taxes-homestead-exemption-mortgage": ("Texas Property Taxes & Homestead Exemption Guide | Joe Bogdan",
        "How Texas property taxes affect your mortgage payment, why MUD and PID taxes matter, and how the homestead exemption and protests help."),
    "when-does-refinancing-make-sense": ("When Does Refinancing Make Sense? Break-Even Guide | Joe Bogdan",
        "Calculate your refinance break-even point, see the common reasons to refinance, and learn how Texas cash-out rules affect your options."),
    "what-makes-a-strong-pre-approval": ("What Makes a Mortgage Pre-Approval Strong? | Joe Bogdan",
        "What separates a strong pre-approval from a weak one, what listing agents look for, and how buyers keep their approval solid until closing."),
}
for _post in POSTS:
    _post["seo_title"], _post["seo_description"] = SEO[_post["slug"]]
