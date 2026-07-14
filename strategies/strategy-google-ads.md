# Google Ads Paid Search Strategy

_Last updated: 2026-07-14_


## Goal and Metric

Drive qualified bottom-of-funnel traffic from Google Search at a target return on ad spend (ROAS) or target cost per acquisition (tCPA) that sustains profitable growth. Primary success metric: ROAS above 3x for ecommerce brands, or tCPA at or below the maximum acceptable customer acquisition cost for lead generation brands. Secondary success metric: Quality Score average of 7 or above across all active ad groups, which predicts lower cost-per-click and higher ad rank without increasing bids.

---

## Platform Overview

Google Search processes approximately 8.5 billion queries per day as of 2026 (Internet Live Stats, 2026). Google Ads commands approximately 28% of global digital advertising spend (Statista, 2025). The platform operates under a smart bidding-first model: Google's machine learning systems manage bid-level decisions using real-time signals that manual bidding cannot access, including device, search history, location, time, and intent signals derived from browsing behavior. Broad match paired with smart bidding has proven to deliver equivalent or superior ROAS to exact-match-heavy structures for most advertisers with sufficient conversion data (Google Internal Data, 2025). The minimum threshold for smart bidding to function reliably is 30 to 50 conversions per month per campaign; below that threshold, manual bidding or Enhanced CPC performs more predictably and prevents the algorithm from optimizing on insufficient data.

---

## Core Principles

**1. Campaign structure determines data quality.** Separating brand, competitor, and non-brand campaigns into distinct campaign groups is not an organizational preference; it is a data quality requirement. Brand campaigns carry structurally different CTR, conversion rate, and ROAS profiles than non-brand campaigns. Mixing them produces misleading averages that lead to incorrect bidding decisions and budget misallocation across the account.

**2. Quality Score is an optimization target, not a reporting number.** A Quality Score of 7 or above reduces average CPC by 16 to 50% compared to a Quality Score of 5 for equivalent ad rank (Google, 2024). Quality Score has three components: Expected CTR (how likely users are to click the ad), Ad Relevance (how closely the ad matches query intent), and Landing Page Experience (how well the landing page satisfies the query intent). Each component is independently improvable and requires a different optimization action.

**3. Match type strategy in 2026 is not binary.** Broad match with smart bidding performs well for accounts with 50 or more conversions per month and a well-maintained negative keyword list. Exact match provides control for high-value terms where query data justifies the restriction. The optimal structure for most accounts in 2026 uses broad match as the primary discovery mechanism and exact match for top-converting terms where precise query matching prevents wasted spend.

**4. Negative keywords are the most undervalued lever in paid search.** Negative keyword lists built, maintained, and shared across campaigns prevent broad match from matching irrelevant queries. A new campaign without negative keywords running on broad match wastes 20 to 40% of budget on irrelevant traffic within the first 30 days. Negative keyword maintenance is a weekly task, not a setup-and-forget configuration.

**5. Landing page relevance drives Quality Score more than ad copy does.** Advertisers consistently underinvest in landing page optimization relative to ad copy. A landing page that exactly matches the search query's intent, uses the query keyword in the headline, loads in under 2.5 seconds, and converts at 5% or above lifts Quality Score, reduces CPC, and improves ROAS without any change to bidding or keywords.

---

## Campaign Structure

**Brand campaigns:**
Brand campaigns capture users searching the brand name directly. Run these on exact and phrase match only, use Maximize Conversions or Target ROAS bidding, and allocate budget to maintain 95% or higher impression share on brand terms. Brand campaigns generate ROAS 5x to 20x above non-brand campaigns and function as revenue protection, not revenue generation. Never combine brand terms with non-brand terms in the same campaign.

**Competitor campaigns:**
Competitor campaigns target users searching for direct competitor brand names. They require legal review of trademark policies in each target country. Competitor ad copy cannot use the competitor's brand name in the headline due to trademark restrictions but can use it in the URL path. Expected CPC runs 2x to 4x above equivalent non-brand terms; Quality Scores are structurally lower because landing pages cannot exactly match competitor-brand queries. Set a strict tCPA ceiling on competitor campaigns and pause them if CPA exceeds 150% of the maximum acceptable acquisition cost.

**Non-brand campaigns:**
Non-brand campaigns target informational, categorical, and solution-aware queries where the user has not yet committed to a brand. These campaigns carry the highest volume potential and the most variable performance. Segment non-brand campaigns by intent stage (problem-aware, solution-aware, category-aware) and by product or service line to maintain ad relevance and accurate performance measurement per segment.

**RLSA campaigns (Remarketing Lists for Search Ads):**
RLSA campaigns layer audience signals onto search campaigns, enabling different bids or different ads for users who have already visited the site. A user searching a non-brand query who has already visited the pricing page is a fundamentally different prospect than a first-time searcher. RLSA campaigns for bottom-of-funnel pages (pricing, contact, demo request) with higher bids or dedicated ad copy consistently outperform standard campaigns in conversion rate for the same spend.

---

## Responsive Search Ad Best Practices

Google's Responsive Search Ads (RSAs) accept up to 15 headlines and 4 descriptions. Google's machine learning assembles combinations and learns which arrangements generate the highest CTR and conversion rate for each query.

**Headline strategy:**
- Write 15 distinct headlines. Avoid repeating concepts across headlines.
- Include the primary keyword in at least 2 of the 15 headlines.
- Include a specific benefit or outcome in at least 3 headlines ("Reduce Hiring Time by 40%").
- Include a CTA in at least 2 headlines ("Book a Free Demo," "Get a Custom Quote").
- Include social proof in at least 1 headline ("Trusted by 2,000+ Companies").

**Pinning strategy:**
Pin headlines sparingly. Pinning Position 1 to the most important headline (brand name or primary value proposition) ensures it always appears. Pinning too many headlines reduces the combinations Google can test and lowers Ad Strength scores. Pin Position 1 only; leave positions 2 and 3 unpinned for optimization.

**Description strategy:**
Write 4 descriptions that each stand alone as a complete message. Include the primary keyword in 1 description. Use the remaining 3 descriptions to address different objections or emphasize different benefits: speed, price, social proof, and risk reduction.

---

## Bidding Guidance

**tCPA (Target Cost Per Acquisition):** Use for lead generation campaigns. Set the initial tCPA at 20 to 30% above the current actual CPA to give the algorithm room to learn. After 30 days and 50 or more conversions, tighten the tCPA target toward the acceptable CPA ceiling in no more than 15% increments.

**Target ROAS:** Use for ecommerce campaigns with 30 or more tracked conversions per month. Set the initial target ROAS at 80% of the desired ROAS to ensure the algorithm does not restrict volume during learning. Increase the ROAS target in 10% increments every 2 weeks as performance stabilizes.

**Maximize Conversions:** Use for new campaigns with fewer than 30 conversions per month. This strategy prioritizes conversion volume over efficiency and has no target constraint. Switch to tCPA or Target ROAS once conversion data crosses the 30-conversion threshold.

**Manual CPC:** Reserve for brand campaigns and any campaign where exact query control is more valuable than algorithmic optimization. Manual CPC with Enhanced CPC enabled provides human control with marginal algorithm assistance.

---

## Distribution and Amplification

1. **Link Google Ads to Google Analytics 4 and import GA4 conversion events.** Native Google Ads conversion tracking without GA4 integration misses multi-session conversion paths and undervalues upper-funnel clicks. GA4-linked imports provide data-driven attribution that improves smart bidding accuracy.

2. **Use ad schedule bid adjustments during peak conversion windows.** Even with smart bidding active, ad schedule adjustments allow amplification during known high-conversion windows (identified from GA4 data) and reduction during low-conversion windows, improving efficiency without restricting the algorithm.

3. **Share negative keyword lists across campaigns via Shared Library.** Update the shared list weekly based on Search Terms reports from broad-match campaigns. Shared lists propagate updates automatically and prevent the same irrelevant queries from generating spend across multiple campaigns.

4. **Use extensions as conversion levers.** Sitelink extensions (linking to pricing, case studies, free trial pages), callout extensions, price extensions, lead form extensions, and call extensions add click-eligible real estate below the main ad at no additional cost. Most advertisers underuse extensions; full extension coverage improves CTR and Quality Score.

5. **Run Performance Max campaigns as a supplement, not a replacement.** Performance Max campaigns run across Search, Display, Shopping, and YouTube. They complement, rather than replace, Search campaigns. Use Performance Max for brand awareness and audience expansion; keep high-intent bottom-of-funnel queries in Search campaigns where Quality Score management and query-level control remain available.

---

## Cadence

- Review Search Terms reports weekly for all broad-match campaigns and add negative keywords immediately for irrelevant queries.
- Review Quality Score components bi-weekly. Landing page experience issues require development resources and longer resolution timelines; identify and escalate these early.
- Review bidding targets monthly. Adjust tCPA or ROAS targets in increments no larger than 20% to avoid triggering unnecessary learning periods.
- Replace the lowest-performing headline in any RSA that has accumulated 5,000 or more impressions every 6 to 8 weeks.
- Conduct a campaign structure audit quarterly. Add new campaigns as new product lines, geographies, or audience segments justify dedicated budget and measurement.

---

## Failure Modes

1. **Using a single match type across all campaigns.** Exact-match-only accounts cap volume artificially and miss query variations that convert. Broad-match-only accounts without negative keyword discipline waste budget on irrelevant traffic. The right match type structure depends on conversion data volume, negative keyword list quality, and campaign goals.

2. **Ignoring Quality Score.** Low Quality Scores mean paying more per click than competitors with higher Quality Scores for equivalent ad rank. Improving Quality Score from 5 to 8 on high-volume terms reduces CPC by 30 to 50% without changing bids (Google, 2024). Treating Quality Score as a reporting number rather than an optimization target leaves significant efficiency gains on the table.

3. **No negative keyword list at launch.** Running broad match or phrase match without a maintained negative keyword list burns budget on irrelevant queries within the first week. Every new campaign should launch with a starter negative keyword list of 50 to 100 terms based on category research and historical Search Terms data.

4. **Sending all traffic to the homepage.** Homepages are discovery pages, not conversion pages. A user who clicked an ad for "enterprise HR software pricing" and lands on a homepage must do additional navigation work to find pricing information; most do not. Dedicated landing pages that match ad intent convert at 2 to 5x the rate of homepage traffic for the same ad spend (Unbounce, 2024).

5. **Adjusting bids during the smart bidding learning period.** Smart bidding enters a learning period (typically 7 to 14 days) whenever significant changes are made to campaigns, bids, or targeting. Making changes before the learning period ends resets it and prevents the algorithm from stabilizing. Evaluate smart bidding performance over 30-day windows, not day-over-day.

6. **Launching without conversion tracking in place.** Campaigns without conversion tracking cannot use smart bidding effectively and provide no data for performance evaluation. Conversion tracking setup, including page verification and confirmation that conversion data flows correctly, is a prerequisite for launch, not a post-launch task.

---

## Recommended Tools

1. **Google Keyword Planner** (ads.google.com): Native keyword research tool within Google Ads. Provides keyword volume estimates, keyword ideas from seed terms, and CPC range benchmarks by market. Free with a Google Ads account.

2. **SEMrush Advertising Research** (semrush.com): Reveals competitor ad copy, keywords, landing pages, and estimated budgets. Use for competitor campaign analysis, negative keyword ideas, and benchmarking which messages perform in the category.

3. **Optmyzr** (optmyzr.com): Paid search management platform with automated rules, optimization suggestions, and Quality Score tracking at scale. Reduces manual review time for large accounts with many ad groups and campaigns.

4. **Google Looker Studio** (lookerstudio.google.com): Free reporting tool connecting Google Ads and GA4 data into dashboards tracking ROAS, Quality Score trends, CPA by campaign, and impression share over time. Shareable with stakeholders without requiring Google Ads access.

5. **Unbounce or Instapage**: Purpose-built landing page platforms with A/B testing that integrate with Google Ads click IDs. Dedicated landing pages created and tested in these tools consistently outperform internal website pages for paid search conversion rates.

---

## Adaptation for Your Brand

Campaign structure priority depends on the brand's competitive position. A brand with strong market recognition should protect brand terms aggressively, budgeting to 95% or higher impression share, because competitor brands frequently bid on established brand names. A newer brand should deprioritize competitor campaigns (which are expensive and yield low-quality traffic) and concentrate budget on non-brand solution-aware queries where purchase intent is high. For B2B brands with long sales cycles (30 days or more), import pipeline-stage conversions (demo requests, proposals accepted, contracts signed) as separate conversion actions with different values so smart bidding optimizes toward revenue-generating events rather than top-of-funnel form fills. For B2C brands with high purchase frequency, RLSA campaigns targeting recent purchasers with upsell or replenishment messaging frequently generate the highest ROAS in the account. Apply the brand's no-em-dash, active-voice, stat-backed writing standards to all ad copy and landing page content; ad copy that matches the tone of other brand communications performs better with audiences who have had prior brand exposure.
