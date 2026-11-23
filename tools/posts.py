"""Insights articles. Run `python3 tools/build.py` to regenerate content/.

Article rules:
- Answer the question in the first paragraph (what search and AI assistants quote).
- Question-style H2s, a key-takeaways box, an FAQ (emits FAQPage schema).
- One relevant next action mid-article; the theme adds a closing CTA by topic.
- Compliance: no rates, APRs, payment amounts or down-payment figures (Regulation Z
  triggering terms), no guarantees, and only programs Joseph offers in Texas.
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
                       "Joseph will turn your income, savings and goals into a personalized buying-power analysis. Free, about two minutes, no credit pull.",
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
    "How Much House Can I Afford in North Texas? | Joseph Bogdan",
    "buyers.webp",
    body(
        lead("How much house you can afford comes down to five things: your gross income, your monthly debts, the cash you have for a down payment and closing costs, your credit, and the full monthly cost of the home - including Texas property taxes and homeowners insurance. Lenders turn those into a maximum. The more useful question is what price keeps your monthly budget comfortable."),
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
            "<strong>Mortgage insurance</strong> - conventional loans with a smaller down payment usually include private mortgage insurance; FHA loans have their own mortgage insurance.",
            "<strong>HOA dues</strong> - common in planned communities and counted in your DTI.",
            "<strong>Closing costs and prepaid items</strong> - set aside cash beyond your down payment, including initial escrow deposits.",
            "<strong>Reserves</strong> - having savings left after closing makes your file stronger and your life less stressful.",
        ]),
        h("Approved amount vs. comfortable amount"),
        p("Start with the monthly payment that fits your life - savings goals, childcare, travel, business swings - then work backward to a price. Joseph’s buying-power analysis shows both: what you may qualify for and the range that keeps your monthly budget where you want it."),
        h("How do I get a reliable number?"),
        ol([
            "Gather the basics: income, monthly debts, savings and a rough credit estimate.",
            "Get a personalized analysis instead of relying on a generic calculator.",
            "Turn it into a documented pre-approval before you start making offers.",
        ]),
        faq([
            ("Does Texas have a state income tax?", "No. Texas does not have a state income tax, but local property taxes are relatively high, which affects your monthly mortgage payment through escrow."),
            ("What is a MUD or PID tax?", "Municipal Utility Districts and Public Improvement Districts fund infrastructure in many newer Texas neighborhoods. They add to a home’s property tax rate, so check whether a home is in one before you make an offer."),
            ("Is it better to put more money down?", "Not always. A larger down payment can reduce your loan amount and mortgage insurance, but keeping cash in reserve also has value. Joseph can show you the trade-offs with your actual numbers."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "buy-a-new-home-before-selling",
    "Can I Buy a New Home Before Selling My Current One?",
    "home-buying",
    "Often, yes. Depending on your income, equity and reserves you may qualify carrying both homes or use your current home’s equity. Here are the options and the trade-offs.",
    "Can I Buy a Home Before Selling My Current One? | Joseph Bogdan",
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
        p("If most of your down payment is tied up in your current home, you may be able to access that equity before you sell. In Texas, home equity loans and lines of credit on a homestead follow specific state rules, including limits on how much you can borrow against the home’s value and required waiting periods, so timing matters. Joseph will walk through which options fit your situation and timeline."),
        h("Option 3: Make an offer contingent on selling"),
        p("A home-sale contingency protects you if your current home does not sell, but many sellers see it as a weaker offer. It works best in slower markets, with new construction or when your current home is already under contract."),
        h("Option 4: Sell first and rent back"),
        p("Some sellers negotiate a short leaseback after closing so they can stay in the home while they buy. You get your equity in hand first, but you need a buyer willing to agree to it and you may need short-term housing if timelines slip."),
        cta("Planning a move-up purchase?", "Tell Joseph about your current home and your next one. He will outline which buy-before-you-sell options fit.", "/contact/", "Ask Joseph About Your Scenario"),
        h("Questions to answer before you start"),
        ul([
            "Can you comfortably carry two payments for a few months if needed?",
            "How much equity do you realistically have after selling costs?",
            "How competitive is the market for the home you want?",
            "Is the next home new construction, with a longer timeline?",
        ]),
        h("Bring your Realtor into the plan"),
        p("Your agent’s offer strategy depends on your financing strategy. When Joseph and your Realtor coordinate early, your offer reflects what you can actually do, and there are fewer surprises after you go under contract."),
        faq([
            ("Will my current mortgage count against me when I buy?", "Yes, unless your current home is sold or under contract with conditions satisfied, lenders generally count the existing payment in your debt-to-income ratio."),
            ("Can rental income from my current home help me qualify?", "Sometimes. If you plan to keep and rent your current home, some programs allow a portion of the expected rent to count, with documentation such as a lease. Joseph will tell you what applies."),
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
    "Self-Employed Mortgage: How Lenders Calculate Business Income | Joseph Bogdan",
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
        cta("Self-employed and planning a purchase?", "Request a Self-Employed Mortgage Strategy Review. Joseph will show you which documentation path fits.", "/loan-programs/self-employed-business-owners/#strategy-review", "Request a Strategy Review"),
        h("What are bank-statement loans and other Non-QM options?"),
        p("Non-QM (non-qualified mortgage) programs use alternative documentation. A <strong>bank-statement loan</strong> calculates income from business or personal deposits over a set period instead of tax returns. <strong>Asset-based</strong> programs look at significant liquid assets. These programs exist for borrowers whose finances do not fit standard guidelines, and their pricing and requirements typically differ from conventional loans. Joseph will compare them side by side with traditional options."),
        h("How to prepare"),
        ol([
            "Talk to a loan officer before you file, especially if you expect large write-offs.",
            "Keep business and personal accounts separate and clean.",
            "Have a year-to-date profit and loss statement ready.",
            "Document large deposits and transfers.",
            "Loop in your CPA so tax and mortgage strategy work together.",
        ]),
        p("Joseph built and ran companies for more than 30 years before becoming a loan officer. He has been on the business-owner side of these conversations and knows how to present your file clearly."),
        faq([
            ("Do I need two years of tax returns to get a mortgage?", "For most traditional loans, yes. Some programs allow a shorter self-employment history with prior experience in the same field, and alternative-documentation programs qualify you differently."),
            ("Can I use business funds for my down payment?", "Often, yes, with documentation. Lenders may want to confirm that withdrawing the funds will not hurt the business. Plan this before you move money."),
            ("Is a bank-statement loan more expensive?", "Non-QM programs typically have different pricing and requirements than conventional loans. Whether one makes sense depends on how much more income it lets you document. Joseph will compare the options with you."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "what-makes-a-jumbo-loan-different",
    "What Makes a Jumbo Loan Different - and How to Prepare",
    "luxury-jumbo",
    "Jumbo loans exceed the conforming loan limit, so lenders set their own standards for credit, reserves, documentation and appraisals. Preparation shapes your terms and flexibility.",
    "What Is a Jumbo Loan and How Do I Qualify? | Joseph Bogdan",
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
        p("Any loan amount above the conforming loan limit for the county is considered jumbo. The limit changes each year and is higher in some high-cost areas. You can find the current limits on the <a href=\"https://www.fhfa.gov/data/conforming-loan-limit\" target=\"_blank\" rel=\"noopener\">FHFA website</a>, or Joseph can confirm whether your loan amount falls into jumbo territory."),
        h("How is qualifying for a jumbo loan different?"),
        ul([
            "<strong>Credit</strong> - lenders typically look for strong credit histories.",
            "<strong>Reserves</strong> - you will usually need several months of payments in savings or investments after closing.",
            "<strong>Asset documentation</strong> - expect to document where your down payment and reserves come from, including brokerage and retirement accounts.",
            "<strong>Income</strong> - complex income from business ownership, bonuses, commissions or investments needs careful presentation.",
            "<strong>Appraisal</strong> - higher-value and unique homes can be harder to value, and some lenders require additional review.",
        ]),
        cta("Considering a high-value purchase?", "Request a private jumbo financing consultation before you go under contract.", "/loan-programs/jumbo-luxury-financing/#consultation", "Request a Consultation"),
        h("Down payment vs. liquidity: a strategic choice"),
        p("With large loans, how much you put down is a real decision. A larger down payment can reduce the loan amount, while keeping more cash or investments can protect flexibility for your business, other properties or opportunities. There is no single right answer. Joseph helps you weigh it the way a CFO would."),
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
            ("Can I get a jumbo loan if I am self-employed?", "Yes, though documentation is especially important. Joseph will help you present business income clearly and compare program options."),
            ("Can I use a jumbo loan for a second home?", "Often, yes. Second-home financing has its own occupancy and reserve requirements, which Joseph will walk through with you."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "dscr-loans-explained",
    "DSCR Loans Explained: Qualifying for a Rental Property Based on Its Income",
    "real-estate-investing",
    "A DSCR loan qualifies an investment property mainly on whether its rent covers the mortgage payment, taxes, insurance and HOA dues - not on your personal tax returns.",
    "DSCR Loans Explained for Texas Real Estate Investors | Joseph Bogdan",
    "strategy.webp",
    body(
        lead("A DSCR (debt-service coverage ratio) loan is an investment-property mortgage that qualifies mainly on the property’s rental income instead of your personal income. The lender divides the property’s monthly rent by its monthly housing expense - principal, interest, taxes, insurance and any HOA dues. If the rent covers the expense, the property supports the loan."),
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
        cta("Running numbers on a property?", "Send Joseph the price, expected rent and cash available. He will reply with the financing options that fit.", "/loan-programs/investment-property/#investor-scenario", "Run an Investor Scenario"),
        h("DSCR vs. conventional investment loans"),
        p("A conventional investment-property loan uses your personal income, debts and tax returns, much like a home loan. It may have different pricing than a DSCR loan, but it counts against your personal DTI, and it can get harder to use as you add properties. A DSCR loan focuses on the property. Many investors use both at different stages."),
        h("What about Texas property taxes?"),
        p("Taxes and insurance are part of the DSCR calculation, so high-tax areas reduce the ratio. Check the full tax rate, including any MUD or PID, before you run your numbers on a North Texas rental."),
        faq([
            ("Do DSCR loans require tax returns?", "Usually personal income is not the main qualifying factor, though you will still need credit, assets for the down payment and reserves, and documentation on the property."),
            ("Can I use a DSCR loan for a short-term rental?", "Some programs allow it, using short-term rental income data. Requirements vary, so share the property details with Joseph."),
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
    "Texas Property Taxes & Homestead Exemption: What Buyers Should Know | Joseph Bogdan",
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
    "When Does Refinancing Make Sense? Break-Even & Texas Cash-Out Rules | Joseph Bogdan",
    "strategy.webp",
    body(
        lead("Refinancing makes sense when what you gain - a lower payment, a shorter term, removing mortgage insurance or accessing equity - is worth more than what it costs, within the time you expect to keep the loan. The simplest test is your break-even point: total closing costs divided by your monthly savings tells you how many months it takes to come out ahead."),
        takeaways([
            "Break-even months = closing costs ÷ monthly savings.",
            "If you will sell or refinance again before the break-even point, it may not be worth it.",
            "Cash-out refinancing on a Texas homestead follows specific state rules.",
            "Sometimes the best advice is to wait. Joseph will tell you if that is the case.",
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
            ("How much does it cost to refinance?", "Costs vary with the loan amount, title and appraisal fees and other factors. Joseph will give you an itemized estimate so you can calculate your break-even point accurately."),
            ("Can I remove PMI without refinancing?", "Often, yes, on conventional loans once you reach enough equity based on the original value or a new appraisal. FHA mortgage insurance usually requires a refinance to remove. Joseph can check which applies to you."),
            ("How often can I do a cash-out refinance in Texas?", "Texas limits how frequently a homestead can be used for a cash-out loan. Joseph will review your loan history and the current rules with you."),
        ]),
    ),
)

# ---------------------------------------------------------------------------
post(
    "what-makes-a-strong-pre-approval",
    "What Makes a Pre-Approval Letter Strong? A Guide for Buyers and Agents",
    "mortgage-strategy",
    "Not all pre-approvals are equal. A strong one is based on verified income, assets and credit, matches the offer, and comes from a loan officer the listing agent can reach.",
    "What Makes a Strong Mortgage Pre-Approval? | Joseph Bogdan",
    "buyers.webp",
    body(
        lead("A strong pre-approval is based on documents that have actually been reviewed - income, assets and credit - not just numbers the buyer typed into a form. It is tailored to the offer, it comes from a loan officer the listing agent can reach, and it has no surprises waiting in underwriting. To sellers and their agents, that combination signals that the buyer can close."),
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
        cta("Ready to shop with a strong letter?", "Start with your buying-power analysis. Joseph will turn it into a documented pre-approval.", "/get-pre-approved/", "Discover Your Buying Power"),
        h("For Realtors: what to ask your buyer’s lender"),
        ol([
            "Has the buyer’s income and asset documentation been reviewed, or only stated?",
            "Is there anything in the file that could cause a delay, such as a recent job change, large deposits or a home to sell?",
            "Will you call the listing agent if it helps the offer?",
            "How will you keep me updated through closing?",
        ]),
        p("Joseph works exclusively as a mortgage loan originator. He does not sell real estate, so referring your clients to him never puts your relationship at risk. Agents can <a href=\"/realtor-partners/#client-scenario\">send a client scenario</a> before writing an offer."),
        h("What buyers can do to keep a pre-approval strong"),
        ul([
            "Avoid new credit accounts or large purchases before closing.",
            "Do not change jobs without talking to your loan officer first.",
            "Document large deposits and keep funds in the same accounts.",
            "Respond quickly when the lender asks for updated documents.",
        ]),
        faq([
            ("How long is a pre-approval good for?", "Pre-approvals are time-limited, because credit reports and documents age. If your search runs longer, your loan officer can update it with fresh documents."),
            ("Does getting pre-approved hurt my credit?", "A pre-approval typically includes a credit check, which can have a small effect. Joseph’s buying-power analysis on this site does not pull credit, and he will tell you before any credit check happens."),
            ("Should the pre-approval show my maximum amount?", "Not necessarily. Many buyers ask for a letter that matches each offer so the seller does not see their ceiling. Joseph can issue letters tailored to the offer."),
        ]),
    ),
)

# Search titles/descriptions (excerpts above are the longer card summaries).
SEO = {
    "how-much-house-can-i-afford-north-texas": ("How Much House Can I Afford in North Texas? | Joseph Bogdan",
        "How lenders decide what you can afford, why Texas property taxes matter so much, and how to find a price that keeps your budget comfortable."),
    "buy-a-new-home-before-selling": ("Can I Buy a Home Before Selling My Current One? | Joseph Bogdan",
        "Often, yes. Learn the four ways to buy your next home before selling, including Texas rules for using equity, and how to choose the right one."),
    "self-employed-mortgage-how-lenders-calculate-income": ("Self-Employed Mortgages: How Lenders Count Income | Joseph Bogdan",
        "How lenders calculate self-employed income from tax returns, which deductions add back, and when bank-statement or Non-QM loans fit better."),
    "what-makes-a-jumbo-loan-different": ("What Is a Jumbo Loan and How Do I Qualify? | Joseph Bogdan",
        "Jumbo loans exceed the conforming limit, so credit, reserves, documentation and appraisals get closer review. Here is how to prepare."),
    "dscr-loans-explained": ("DSCR Loans Explained for Texas Investors | Joseph Bogdan",
        "How DSCR loans qualify a rental property on its own income, how the ratio is calculated, and how they compare with conventional investor loans."),
    "texas-property-taxes-homestead-exemption-mortgage": ("Texas Property Taxes & Homestead Exemption Guide | Joseph Bogdan",
        "How Texas property taxes affect your mortgage payment, why MUD and PID taxes matter, and how the homestead exemption and protests help."),
    "when-does-refinancing-make-sense": ("When Does Refinancing Make Sense? Break-Even Guide",
        "Calculate your refinance break-even point, see the common reasons to refinance, and learn how Texas cash-out rules affect your options."),
    "what-makes-a-strong-pre-approval": ("What Makes a Mortgage Pre-Approval Strong? | Joseph Bogdan",
        "What separates a strong pre-approval from a weak one, what listing agents look for, and how buyers keep their approval solid until closing."),
}
for _post in POSTS:
    _post["seo_title"], _post["seo_description"] = SEO[_post["slug"]]

# ===========================================================================
# Builders & New Construction (original content for the builder audience)
# ===========================================================================
BUILDER_CTA = cta("Want a lender your sales team can count on?",
                  "Make Joseph your preferred lending partner. He will meet your team, learn your communities and give your buyers a predictable path from contract to keys.",
                  "/builders-developers/#partner", "Become a Preferred Lending Partner")
BUILDER_SCENARIO_CTA = cta("Have a buyer you are unsure about?",
                           "Send Joseph the scenario before you sign. He will tell you what it would take to close, in plain language.",
                           "/builders-developers/#partner", "Talk to Joseph About a Buyer")

post(
    "price-cut-or-rate-buydown-builder-incentives",
    "Price Cut or Rate Buydown? How Builders Should Spend Incentive Dollars",
    "builders-new-construction",
    "The same incentive budget can lower a home's price or lower the buyer's monthly payment. Here is how each works, which buyers each helps, and how to choose.",
    "Price Cut or Rate Buydown? Builder Incentives Explained",
    "feat-joseph-model-home-a.webp",
    body(
        lead("A price cut and a rate buydown can cost a builder the same amount, but they do very different things for the buyer. A price cut lowers the sales price, the loan amount and the appraised comparable for the next sale. A rate buydown uses the same dollars to lower the buyer's interest rate, either for the first years of the loan or for its full life, which usually has a bigger effect on the monthly payment. The right choice depends on the buyer, the loan program and what you need your comparable sales to show."),
        takeaways([
            "A price cut lowers the price and the loan amount, and resets your comparable sales.",
            "A buydown spends the same dollars on the buyer's rate, which usually moves the monthly payment more.",
            "Temporary buydowns lower the payment for the first years; permanent buydowns lower it for the life of the loan.",
            "Every loan program caps how much a seller can contribute, so the incentive has to fit the buyer's loan.",
            "The best incentive is the one that solves the specific buyer's problem: payment, cash to close or qualifying.",
        ]),
        h("What does a price cut actually do?"),
        p("A price cut reduces the contract price. The buyer borrows less, pays a little less each month and may need slightly less for the down payment. For the builder, the lower price becomes a comparable sale that appraisers and future buyers will see, which can pull down values across the rest of the community."),
        h("What does a rate buydown do?"),
        p("With a buydown, the builder pays the lender to reduce the buyer's interest rate. A <strong>permanent buydown</strong> uses discount points to lower the rate for the life of the loan. A <strong>temporary buydown</strong> lowers the payment for the first year or two, with the difference funded up front, then the payment steps up to the full note rate. Because the dollars go toward the payment instead of the price, buyers often feel the benefit more, and your sales price stays intact."),
        h("Which incentive fits which buyer?"),
        ul([
            "<strong>Payment-sensitive buyers</strong> usually benefit most from a buydown.",
            "<strong>Buyers short on cash to close</strong> may be better served by closing-cost help, within program limits.",
            "<strong>Buyers who barely qualify</strong> need care: with many temporary buydowns, the buyer still qualifies at the full note rate, so the buydown does not change approval.",
            "<strong>Buyers planning to refinance or move soon</strong> may get more from a temporary buydown or closing-cost help than a permanent buydown.",
        ]),
        BUILDER_CTA,
        h("How much can a builder contribute?"),
        p("Every loan program limits seller and builder contributions, sometimes called interested party contributions. The limit depends on the loan type, the buyer's down payment and how the home will be used. Money spent beyond the limit can force a price reduction late in the process. See <a href=\"/builder-incentive-limits-seller-concessions/\">how seller-concession limits work by loan type</a>."),
        h("How to decide, community by community"),
        ol([
            "Look at who is actually buying in that community and what is stopping them: payment, cash or qualifying.",
            "Compare what the same incentive budget does as a price cut, a temporary buydown and a permanent buydown.",
            "Check each option against program contribution limits for your typical buyer.",
            "Advertise carefully. Promoting a specific rate or payment in your marketing triggers federal disclosure requirements, so involve your lender before you print it.",
        ]),
        p("Joseph built and ran companies for more than 30 years before becoming a loan officer, so he approaches incentives the way a builder does: as a budget that has to produce sales."),
        faq([
            ("Is a buydown better than a price cut?", "Often for payment-sensitive buyers, because the same dollars typically lower the monthly payment more. A price cut can make more sense when a buyer needs a lower loan amount or the price itself is the obstacle. It depends on the buyer and the program."),
            ("Does a temporary buydown help a buyer qualify?", "Usually not. For many programs the buyer still qualifies at the full note rate, so a temporary buydown improves early payments but does not change approval."),
            ("Can I advertise a bought-down rate on my spec homes?", "You can advertise financing, but quoting a specific rate or payment requires specific disclosures under federal advertising rules. Ask your lender to review any rate-based marketing before it runs."),
        ]),
    ),
)

post(
    "builder-incentive-limits-seller-concessions",
    "How Much Can a Builder Contribute? Seller-Concession Limits by Loan Type",
    "builders-new-construction",
    "Conventional, FHA and VA loans each cap what a builder can pay toward a buyer's costs. Here is how the limits work and how to keep closings on track.",
    "Builder Incentive Limits: Seller Concessions by Loan Type",
    "feat-joseph-national-mall.webp",
    body(
        lead("Builder incentives are limited by the buyer's loan program. Conventional loans allow builder and seller contributions that range from 3% to 9% of the price, depending on the buyer's down payment and occupancy. FHA generally allows up to 6%. VA limits certain concessions to 4%, while some normal closing costs do not count toward that cap. Contributions above the limit usually have to be removed or turned into a price reduction, which is why incentives should be planned with the lender before the contract is signed."),
        takeaways([
            "Contribution limits depend on the loan type, the down payment and how the home will be used.",
            "Investment-property loans have tighter limits than primary-residence loans.",
            "Money over the limit typically becomes a required price reduction.",
            "Incentives can pay closing costs, prepaids and buydowns, but generally cannot be paid to the buyer as cash.",
            "Program rules change, so confirm limits on each file before you promise an incentive.",
        ]),
        h("What counts as a builder contribution?"),
        p("Interested party contributions are costs paid by anyone with a financial interest in the sale, including the builder, the seller and the listing agent. They commonly include closing costs, prepaid items such as escrow deposits, and rate buydowns. Design-center credits and upgrades that become part of the home are generally treated differently from money applied to the buyer's financing costs, which is one reason to put incentives in writing clearly."),
        h("How the limits work by loan type"),
        ul([
            "<strong>Conventional:</strong> limits range from 3% to 9% of the price for a primary residence, depending on the buyer's down payment, with a lower limit for investment properties.",
            "<strong>FHA:</strong> generally up to 6% of the sales price toward eligible costs.",
            "<strong>VA:</strong> concessions such as paying the buyer's debts or prepaid items are limited to 4% of the reasonable value, while normal closing costs and discount points are not counted toward that cap.",
            "<strong>Jumbo and Non-QM:</strong> limits are set by each investor and can be lower, so check early.",
        ]),
        p("These are general guidelines. Joseph confirms the limit that applies to each buyer's actual loan before the incentive is finalized."),
        BUILDER_CTA,
        h("What happens if an incentive exceeds the limit?"),
        p("The excess usually cannot simply be absorbed. It is typically treated as a sales concession that reduces the price used for the loan, which can change the loan amount, the down payment and sometimes the buyer's approval, often late in the process. Planning the incentive against the buyer's program at contract avoids that."),
        h("A simple process for your sales team"),
        ol([
            "Identify the buyer's likely loan program at the first meeting.",
            "Write incentives into the contract with specific uses: closing costs, prepaids or a buydown.",
            "Have the lender confirm the contribution fits the program before the contract is final.",
            "Keep design-center credits separate and clearly documented.",
        ]),
        faq([
            ("Can a builder give the buyer cash back at closing?", "Generally no. Contributions are applied to allowable costs such as closing costs, prepaids and buydowns. Cash back to the buyer is typically not permitted."),
            ("Do design-center upgrades count toward the limit?", "It depends on how they are structured and documented. Upgrades that become part of the home are usually treated differently from money applied to financing costs. Confirm with the lender on each contract."),
            ("Why is the investment-property limit lower?", "Investors present different risk, so programs restrict how much a seller can contribute when the buyer will not live in the home."),
        ]),
    ),
)

post(
    "vetting-a-buyers-pre-approval-builders",
    "Seven Questions to Ask Before You Accept a Buyer's Pre-Approval",
    "builders-new-construction",
    "A pre-approval letter is only as strong as the work behind it. These seven questions help builders' sales teams separate real buyers from risky contracts.",
    "Vetting a Buyer's Pre-Approval: 7 Questions for Builders",
    "feat-joseph-model-home-b.webp",
    body(
        lead("A pre-approval letter can mean anything from a fully reviewed file to a quick estimate based on what the buyer said. Before you take a home off the market, your sales team should know whether the buyer's income, assets and credit were actually reviewed, whether the loan program fits your contract and your timeline, and whether the buyer has to sell another home first. Seven questions to the buyer's lender will tell you most of what you need."),
        takeaways([
            "Ask whether the lender reviewed documents or relied on what the buyer reported.",
            "Confirm the loan program and that it allows your incentives and timeline.",
            "Find out early if the buyer must sell another home.",
            "For longer builds, ask how the lender will handle rate locks and re-verification.",
            "A lender who answers clearly and quickly is a good sign in itself.",
        ]),
        h("The seven questions"),
        ol([
            "<strong>Were income, assets and credit actually reviewed?</strong> Ask whether pay stubs, tax returns, bank statements and a credit report were reviewed, or only stated.",
            "<strong>Which loan program is the buyer approved for?</strong> Conventional, FHA, VA, jumbo and Non-QM loans have different rules for incentives, appraisals and timing.",
            "<strong>Does the approval cover this price and these incentives?</strong> A letter for a lower price, or one that ignores contribution limits, can unravel later.",
            "<strong>Does the buyer need to sell or rent another home?</strong> If so, ask whether they qualify carrying both payments.",
            "<strong>Is anything unusual in the file?</strong> Recent job changes, self-employment, large deposits or a credit event are not deal-breakers, but they need a plan.",
            "<strong>How will the loan work on our construction timeline?</strong> Ask about rate-lock options and what will need to be updated before closing.",
            "<strong>How will you keep our team updated?</strong> You want a lender who calls before problems become delays.",
        ]),
        BUILDER_SCENARIO_CTA,
        h("Red flags to watch for"),
        ul([
            "A letter with no lender contact name or license number",
            "Vague answers about whether documents were reviewed",
            "A buyer who says they need to sell, while the letter assumes they do not",
            "A lender who is hard to reach before the contract is even signed",
        ]),
        h("Why this matters more for new construction"),
        p("New-construction timelines are longer than resale. A buyer's situation can change between contract and completion, so a well-documented approval up front, and a lender who keeps the file current, protects the home you are holding for them."),
        faq([
            ("Can we require buyers to use a specific lender?", "No. Buyers are always free to choose their lender. You can ask for a strong, verified pre-approval and offer a preferred lender option, within RESPA rules."),
            ("How recent should a pre-approval be?", "Recent enough that the documents behind it are current. For longer builds, expect the lender to update income, assets and credit before closing."),
            ("What if the buyer's lender will not answer questions?", "Ask the buyer to authorize the lender to speak with your team. A lender who stays unresponsive before contract rarely improves later."),
        ]),
    ),
)

post(
    "why-new-construction-closings-slip",
    "Why New-Construction Closings Slip, and How to Keep Yours on Schedule",
    "builders-new-construction",
    "Most delayed new-construction closings trace back to a few predictable causes. Here is what goes wrong between completion and closing, and how builders prevent it.",
    "Why New-Construction Closings Slip and How to Prevent It",
    "feat-joseph-model-home-c.webp",
    body(
        lead("New-construction closings usually slip for predictable reasons: the buyer's documents went stale during the build, the rate lock expired, the final inspection or certificate of occupancy was late, the completion appraisal raised questions, or the title and lender teams were not coordinated with the build schedule. Most of these can be prevented by planning the financing around the construction timeline from the day the contract is signed."),
        takeaways([
            "Long builds mean buyer documents and credit need updating before closing.",
            "Rate locks have to be timed to realistic completion dates.",
            "Lenders typically need the home complete, with final inspection, before closing.",
            "A completion appraisal or final inspection can raise last-minute questions.",
            "One coordinated schedule between builder, lender and title prevents most delays.",
        ]),
        h("The five most common causes"),
        ol([
            "<strong>Stale documents.</strong> Pay stubs, bank statements and credit reports expire. If the file was approved months ago, it needs updating, and changes can surface late.",
            "<strong>Rate locks that run out.</strong> A lock that expires before completion can mean extension costs or a new rate.",
            "<strong>Completion paperwork.</strong> Lenders generally need the home finished, with the final inspection or certificate of occupancy in hand, before closing.",
            "<strong>Appraisal and completion questions.</strong> Unfinished items, value questions or missing documentation can hold up the final approval.",
            "<strong>Buyer changes during the build.</strong> A new car loan, a job change or a large deposit can change approval.",
        ]),
        BUILDER_CTA,
        h("How to keep closings on schedule"),
        ul([
            "Share realistic completion estimates with the lender and update them as the build moves.",
            "Ask the lender to schedule document updates ahead of completion, not after.",
            "Coach buyers not to open new credit, change jobs or move money without calling their lender.",
            "Plan the rate lock around the build schedule, and discuss extension options up front.",
            "Coordinate the final walk-through, inspection and closing date with the lender and title company in one shared timeline.",
        ]),
        h("What Joseph does differently"),
        p("Joseph treats a new-construction loan like a project with milestones. Builders and their sales teams get proactive status updates at each stage, so issues come up while there is still time to fix them."),
        faq([
            ("Can a buyer close before the home is complete?", "Generally no. Lenders typically require the home to be complete, with final inspection or occupancy approval, before a standard purchase loan closes."),
            ("When should the rate be locked on new construction?", "It depends on the build timeline and the program. Longer locks are available on many programs but can cost more. Joseph plans the lock around a realistic completion date."),
            ("Why did the lender ask for new documents right before closing?", "Documents expire. On longer builds, lenders must confirm the buyer's income, assets and credit are still current before closing."),
        ]),
    ),
)

post(
    "selling-new-construction-to-buyers-who-must-sell-first",
    "Selling New Construction to Buyers Who Have to Sell First",
    "builders-new-construction",
    "Move-up buyers are often your best prospects, but their current home can stall a contract. Here are the financing options that can keep the sale moving.",
    "Move-Up Buyers Who Must Sell First: Options for Builders",
    "feat-joseph-model-home-a.webp",
    body(
        lead("Many of a builder's best prospects already own a home. Whether they can sign without selling first depends on three things: whether their income supports both housing payments, how much equity is in their current home, and how much cash they have in reserve. If they qualify with both payments, they can buy without a sale contingency. If not, options like accessing equity, a contingency with a realistic timeline, or matching the build schedule to their sale can still make the deal work."),
        takeaways([
            "Find out at the first meeting whether the buyer needs to sell.",
            "Qualifying with both payments is the cleanest path.",
            "Equity in the current home can fund the next down payment, within Texas homestead rules.",
            "A long build can give a buyer time to sell, if the timeline is planned.",
            "Get the lender involved before the contract, not after.",
        ]),
        h("Why move-up buyers need a plan"),
        p("A move-up buyer's current home is both their biggest asset and their biggest risk to your contract. Without a plan, a slow sale can push back your closing or end the contract. With a plan, a move-up buyer is often one of the strongest buyers in your pipeline."),
        h("The main options"),
        ul([
            "<strong>Qualify with both payments.</strong> If income, credit and reserves support carrying both homes for a period, the buyer can sign without a sale contingency.",
            "<strong>Use existing equity.</strong> Equity in the current home may help fund the down payment. Texas rules for borrowing against a homestead affect timing and amounts, so plan early.",
            "<strong>Time the sale to the build.</strong> On a longer build, the buyer may be able to list and sell their current home before completion.",
            "<strong>Rent the current home.</strong> Some programs allow a portion of documented rental income to count, which can help the buyer qualify.",
            "<strong>A sale contingency.</strong> Works best when the current home is priced to sell and the timeline is realistic.",
        ]),
        BUILDER_SCENARIO_CTA,
        h("What your sales team should ask"),
        ol([
            "Do you own a home now, and do you plan to sell it or keep it?",
            "Is it listed, under contract or not yet on the market?",
            "Have you talked with a lender about qualifying with both payments?",
        ]),
        p("Joseph reviews move-up buyers' options before they sign, so your team knows which path is realistic and how it fits the build schedule. See also <a href=\"/buy-a-new-home-before-selling/\">can I buy a new home before selling my current one?</a>"),
        faq([
            ("Can a buyer qualify for a new home while still owning their current one?", "Often, yes, if their income, credit and reserves support both payments. Joseph will review the numbers before the contract."),
            ("Does a long build help move-up buyers?", "It can. A build timeline may give the buyer time to sell their current home before closing, if the plan is set at contract."),
            ("Can rental income from the current home help?", "Sometimes. If the buyer will keep and rent the current home, some programs allow part of the documented rent to count toward qualifying."),
        ]),
    ),
)

post(
    "spec-homes-qualifying-the-real-buyer",
    "Spec Homes: How to Tell a Real Buyer From a Risky Contract",
    "builders-new-construction",
    "A spec home under contract with a buyer who can't close costs you time and carrying costs. Here is how to qualify spec-home buyers early and protect your inventory.",
    "Spec Homes: Qualifying Buyers Before You Take a Contract",
    "feat-joseph-national-mall.webp",
    body(
        lead("A spec home is ready or nearly ready, so every week it sits under contract with a buyer who cannot close costs you carrying costs and lost buyers. The way to protect it is to verify the buyer before the contract is final: a reviewed pre-approval, a loan program that fits the home and your incentives, a clear answer on whether the buyer must sell first, and a lender who can close on your completion date."),
        takeaways([
            "Spec homes have short timelines, so the buyer's financing must be ready now.",
            "Verify the pre-approval, the program and any home the buyer must sell.",
            "Match incentives to the buyer's program limits before signing.",
            "Short option periods only help if the financing is already solid.",
            "A responsive lender is part of protecting the inventory.",
        ]),
        h("Why spec homes are different"),
        p("With a to-be-built home, a financing problem can surface months before completion. With a spec home, the timeline is compressed. There is little room to fix documentation problems, change programs or wait for another home to sell, so the buyer's financing needs to be verified up front."),
        h("A spec-home buyer checklist"),
        ol([
            "A pre-approval based on reviewed income, assets and credit",
            "A loan program that fits the price, the home and your incentives",
            "Confirmation of whether the buyer must sell or rent another home",
            "Cash to close confirmed, including any amounts not covered by incentives",
            "A closing date the lender has confirmed it can meet",
        ]),
        BUILDER_SCENARIO_CTA,
        h("Marketing spec homes with financing"),
        p("Financing incentives can help spec homes sell, but advertising a specific rate or payment triggers federal disclosure requirements. Promote the incentive generally, such as builder-paid closing costs or rate buydown options, and have your lender review any rate-based advertising before it runs."),
        p("For a closer look at incentive options, see <a href=\"/price-cut-or-rate-buydown-builder-incentives/\">price cut or rate buydown</a>."),
        faq([
            ("How quickly can a spec-home buyer close?", "It depends on the program, the appraisal and how quickly the buyer provides documents. A buyer with a fully reviewed pre-approval is in the best position to close on a short timeline."),
            ("Should we accept a buyer who has to sell first on a spec home?", "Only with a realistic plan. On a spec home, a sale contingency can tie up inventory, so verify whether the buyer qualifies without selling."),
            ("Can we advertise a monthly payment on a spec home?", "Quoting a payment triggers required disclosures. Ask your lender to review the ad before it runs."),
        ]),
    ),
)

post(
    "what-builder-sales-teams-should-expect-from-a-lender",
    "What Your Sales Team Should Expect From a Lender",
    "builders-new-construction",
    "A good lending partner makes your sales team's job easier. Here is what builders should expect, from first buyer meeting to closing day, and what to ask any lender.",
    "What Builder Sales Teams Should Expect From a Lender",
    "feat-joseph-model-home-b.webp",
    body(
        lead("A builder's sales team should expect a lender to respond quickly to new buyers, give clear answers about whether a buyer can close, explain how incentives fit each loan program, plan financing around the construction schedule, and send proactive updates through closing. Just as important, a good lender protects your relationship with the buyer and never surprises your team at the closing table."),
        takeaways([
            "Responsiveness to walk-in and model-home traffic matters most.",
            "Clear, early answers about each buyer's real ability to close.",
            "Incentive guidance that fits program limits.",
            "Financing planned around construction milestones.",
            "Regular status updates without your team having to chase them.",
        ]),
        h("Before the contract"),
        ul([
            "Prompt follow-up with buyers your team introduces",
            "A straight answer on whether the buyer can close, and what it will take",
            "Guidance on which incentive works best for that buyer's program",
        ]),
        h("During the build"),
        ul([
            "A rate-lock plan tied to realistic completion dates",
            "Document updates scheduled ahead of completion",
            "Early warning if anything in the buyer's file changes",
        ]),
        h("At completion"),
        ul([
            "Coordination of the final inspection, appraisal and closing date",
            "One point of contact for your team, the buyer and the title company",
            "No surprises at the closing table",
        ]),
        BUILDER_CTA,
        h("Questions to ask any lender you are considering"),
        ol([
            "How quickly do you follow up with a new buyer?",
            "How will you keep my team updated, and how often?",
            "How do you handle rate locks on longer builds?",
            "How do you handle buyers who are self-employed or need to sell first?",
            "Who is my contact if you are unavailable?",
        ]),
        p("Joseph offers a short kickoff with your sales team to learn your communities, incentives and process, then keeps your team informed on every buyer. Buyers are always free to choose their own lender."),
        faq([
            ("How should a lender update our sales team?", "On a schedule you agree on, plus immediately when anything changes. Many builders prefer a regular pipeline update covering every buyer."),
            ("Can a preferred lender offer our buyers special incentives?", "Builders can offer incentives through any lender within program limits, and preferred lender arrangements must follow RESPA. Buyers remain free to choose their lender."),
            ("What if a buyer chooses an outside lender?", "Ask the buyer to authorize communication between their lender and your team, and use the same questions to verify the approval."),
        ]),
    ),
)

post(
    "financing-on-a-construction-timeline",
    "Financing on a Construction Timeline: What Builders Should Plan For",
    "builders-new-construction",
    "A new-construction loan has to work across months of building. Here is how rate locks, document updates, appraisals and completion fit the construction schedule.",
    "Financing on a Construction Timeline: A Builder's Guide",
    "feat-joseph-model-home-c.webp",
    body(
        lead("Financing a home that is still being built means planning around a moving date. The buyer is approved at contract, but the loan closes at completion, sometimes months later. Along the way the rate lock, the buyer's documents and the appraisal all have to line up with the build schedule. Planning those milestones at contract is the simplest way to protect the closing."),
        takeaways([
            "Approve the buyer thoroughly at contract.",
            "Choose a rate-lock strategy that fits the realistic completion date.",
            "Expect to update documents and credit before closing.",
            "Plan for the appraisal and completion inspection.",
            "Share schedule changes with the lender as they happen.",
        ]),
        h("At contract"),
        p("Start with a fully reviewed approval, a loan program that fits the price and incentives, and a clear answer on whether the buyer has to sell another home. This is also when the lender should explain rate-lock options for the expected build time."),
        h("During construction"),
        p("Rate locks can be timed in different ways. A buyer may lock early for certainty, often at extra cost for a longer lock, or float and lock closer to completion. Joseph explains the trade-offs to each buyer so the decision is made deliberately, not by default."),
        p("Buyers should also be coached not to change jobs, open new credit or move large sums of money during the build without calling their lender first."),
        BUILDER_CTA,
        h("Approaching completion"),
        ul([
            "The lender updates the buyer's income, assets and credit",
            "The appraisal is completed, or updated if the home was appraised from plans",
            "The final inspection or certificate of occupancy is obtained",
            "The closing is scheduled with the title company",
        ]),
        h("The construction-timeline checklist"),
        ol([
            "Share the expected completion date at contract, and update it monthly.",
            "Decide on a rate-lock approach with the buyer and lender.",
            "Schedule document updates before completion.",
            "Confirm appraisal timing and any completion requirements.",
            "Coordinate the walk-through, inspection and closing date together.",
        ]),
        p("Related: <a href=\"/why-new-construction-closings-slip/\">why new-construction closings slip</a>."),
        faq([
            ("How long can a rate be locked on new construction?", "Many programs offer extended locks, usually at additional cost. The right length depends on the build timeline. Joseph will outline the options for each buyer."),
            ("Will the buyer need to re-qualify before closing?", "Lenders confirm that income, assets and credit are still current before closing. On longer builds, expect updated documents."),
            ("When is the appraisal done on new construction?", "It can be done from plans and specifications, with a completion inspection later, or once the home is complete. Timing depends on the program and the lender."),
        ]),
    ),
)

post(
    "new-construction-appraisals-what-builders-should-know",
    "New-Construction Appraisals: What Builders and Buyers Should Know",
    "builders-new-construction",
    "How appraisers value new construction, why incentives and comparable sales matter, and what builders can do if an appraisal comes in low.",
    "New-Construction Appraisals: What Builders Should Know",
    "feat-joseph-model-home-a.webp",
    body(
        lead("An appraisal on a new home tells the lender what the home is worth as security for the loan. For new construction, appraisers rely on recent sales of comparable homes, often in the same community, and they look closely at incentives and upgrades. If the appraisal comes in below the contract price, the buyer, builder and lender have to resolve the gap before closing, so it pays to understand how new-construction appraisals work."),
        takeaways([
            "Appraisers rely heavily on recent comparable sales in and around the community.",
            "Price cuts become comparables for future appraisals.",
            "Upgrades add value only to the extent the market supports them.",
            "Some appraisals are done from plans, with a completion inspection later.",
            "A low appraisal can be addressed, but it is better to plan for it.",
        ]),
        h("How appraisers value new homes"),
        p("Appraisers compare the home with recent sales of similar homes, adjusting for size, lot, features and timing. In a new community, the builder's own recent closings are often the most relevant comparables. That is one reason pricing decisions, including price cuts, affect the value of every home that follows."),
        h("Upgrades and lot premiums"),
        p("Design-center upgrades and lot premiums can support a higher price, but appraisers value them by what buyers in the market have paid, not by what they cost to build. Documenting upgrades clearly helps the appraiser understand what is in the home."),
        BUILDER_CTA,
        h("What if the appraisal comes in low?"),
        ul([
            "Provide the appraiser with additional comparable sales or upgrade documentation through the lender's process",
            "Renegotiate the price or restructure incentives",
            "The buyer covers the difference with additional cash, if they are able",
        ]),
        p("A buydown instead of a price cut can also help protect future comparables. See <a href=\"/price-cut-or-rate-buydown-builder-incentives/\">price cut or rate buydown</a>."),
        faq([
            ("Can a new home be appraised before it is finished?", "Yes. Appraisals can be completed from plans and specifications, with a completion inspection confirming the work before closing."),
            ("Do builder incentives affect the appraisal?", "They can. Appraisers consider concessions in comparable sales and in the contract, and large concessions may be adjusted for."),
            ("Who orders the appraisal?", "The lender orders it through an independent process. Builders and agents cannot select or pressure the appraiser, but they can provide relevant information through the lender."),
        ]),
    ),
)

post(
    "build-to-rent-holding-completed-homes-dscr",
    "Build to Sell or Hold? Financing Completed Homes as Rentals With DSCR",
    "builders-new-construction",
    "Builders holding completed homes as rentals can often use DSCR loans that qualify on rent, not tax returns. Here is how it works and what lenders review.",
    "Build to Rent: Financing Completed Homes With DSCR Loans",
    "feat-joseph-national-mall.webp",
    body(
        lead("When a builder decides to keep completed homes as rentals instead of selling them, the financing question changes from the buyer's income to the property's income. A DSCR (debt-service coverage ratio) loan qualifies primarily on whether the home's rent covers its mortgage payment, taxes, insurance and HOA dues, rather than on the builder's personal tax returns. That can make holding completed inventory a realistic option."),
        takeaways([
            "DSCR loans focus on the rental property's income compared with its payment.",
            "They can suit builders whose tax returns show reduced income from depreciation and write-offs.",
            "Rent is documented by a lease or an appraiser's market-rent estimate.",
            "Texas property taxes and insurance affect the ratio, so plan for them.",
            "Some programs allow closing in an LLC.",
        ]),
        h("Sell or hold: the decision"),
        p("Selling returns capital for the next project. Holding builds long-term income and equity, but ties up capital. Many builders do both, selling most homes and holding a few. The financing has to fit whichever path each home takes."),
        h("How a DSCR loan looks at a completed home"),
        ul([
            "<strong>Rent:</strong> from a signed lease or an appraiser's market-rent estimate",
            "<strong>Payment:</strong> principal, interest, taxes, insurance and any HOA dues",
            "<strong>The ratio:</strong> rent divided by the payment; stronger ratios generally mean more options",
            "<strong>Equity and reserves:</strong> how much is invested and how much cash remains",
            "<strong>Ownership:</strong> whether the home will be held personally or in an entity",
        ]),
        BUILDER_CTA,
        h("Planning ahead"),
        p("The best time to plan a hold is before the home is finished: estimate realistic rents, check the tax rate, including any MUD or PID, and confirm how the loan will treat the property once it is complete. Joseph will compare DSCR options with conventional investment financing so you can decide which homes to sell and which to keep."),
        p("Related: <a href=\"/dscr-loans-explained/\">DSCR loans explained</a>."),
        faq([
            ("Do DSCR loans require personal tax returns?", "Personal income is typically not the main qualifying factor, though credit, assets for the down payment and reserves still matter."),
            ("Can a builder hold rentals in an LLC?", "Some DSCR programs allow LLC ownership. Talk with your attorney and CPA about the structure."),
            ("Does the home need a tenant before closing?", "Not always. Many programs can use an appraiser's market-rent estimate when there is no lease yet."),
        ]),
    ),
)
