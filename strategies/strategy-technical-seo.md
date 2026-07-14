# Technical SEO Strategy

_Last updated: 2026-07-14_


## Goal and Metric

Ensure the brand's website infrastructure actively supports organic ranking growth by eliminating crawlability barriers, meeting Core Web Vitals standards, and maximizing the indexation efficiency of the content the brand creates. Primary success metric: all primary landing pages and pillar content pages achieving a Google PageSpeed Insights score of 85+ on mobile, with crawl coverage of 95%+ of intended indexable pages confirmed through Google Search Console within 6 months of executing the technical audit.

---

## Core Principles

**1. Technical SEO is the infrastructure layer; content is the signal layer.** Even the most authoritative, well-written content on the web cannot rank effectively if the crawlers cannot efficiently discover, render, and index it. Technical SEO does not replace content quality; it ensures that content quality is accurately perceived and rewarded by search engines.

**2. Mobile-first indexing is not a preference; it is the indexing standard.** Google uses the mobile version of a page as the primary version for indexing and ranking. A site that looks and performs well on desktop but poorly on mobile is, from Google's perspective, a poor-performing site. Every technical decision from 2026 forward begins with the mobile experience, not the desktop.

**3. Crawl budget is finite; every crawled URL costs something.** Large sites with many pages cannot rely on Google crawling every page frequently. Crawl budget is the number of pages Google's crawler will process in a given time period. Using crawl budget on low-quality, duplicate, or irrelevant pages means that important pages get crawled less frequently. Managing the crawl budget through canonical tags, robots.txt, and sitemap organization is a ranking lever for sites with more than 500 pages.

**4. Core Web Vitals are a ranking factor with a 2026 update cycle.** Google's Core Web Vitals thresholds for 2026 are: Largest Contentful Paint (LCP) below 2.5 seconds, Interaction to Next Paint (INP) below 200 milliseconds, and Cumulative Layout Shift (CLS) below 0.1. These metrics are measured from real user data, not lab tests. Sites that consistently fail these thresholds receive ranking disadvantages in direct competition with comparable sites that pass them.

**5. Schema markup is the language that makes content understandable to machines.** Schema markup tells Google what type of content a page contains (an article, a product, a FAQ, an event, a how-to guide) and what the specific data elements within the page mean. Structured data does not directly guarantee rich results, but it is the prerequisite for eligible content to receive them.

---

## Strategy Architecture

**Step 1: Technical audit**
Before any optimization work begins, conduct a full technical audit covering:
- Crawlability: which pages are being crawled, which are blocked, and which are producing crawler errors
- Indexation: which pages Google has indexed and which it has not, and why
- Core Web Vitals: measured on the actual site using Google PageSpeed Insights and Chrome User Experience Report (CrUX) data
- Canonical configuration: are self-referencing canonicals in place? Are duplicate content situations resolved?
- Internal linking: are important pages well-linked internally? Are there orphan pages with no internal links pointing to them?
- Mobile experience: does the mobile version of the site contain the same content as the desktop version?

Tools for the audit: Screaming Frog (crawl analysis), Google Search Console (indexation and Core Web Vitals data), Ahrefs Site Audit (combines crawl errors, internal link issues, and content quality signals).

**Step 2: Site architecture optimization**

Flat versus deep structure:
- A flat site architecture (primary pages accessible within 3 clicks from the homepage) allows crawlers to discover important pages efficiently and distributes link equity from the homepage to all primary pages
- A deep site architecture (important pages buried 5+ clicks from the homepage) requires more crawl budget to discover important pages and distributes less link equity to them
- Restructure site navigation so that all primary content categories are accessible from the homepage or from a single top-level navigation level

Crawl budget allocation:
- Canonicalize or noindex all paginated series, parameter-driven URLs, and filter combinations that do not produce genuinely unique content
- Add noindex to thank-you pages, login pages, user account pages, and internal search result pages
- Ensure robots.txt does not accidentally block CSS, JavaScript, or image files that the crawler needs to render pages correctly

**Step 3: Core Web Vitals optimization**

LCP (Largest Contentful Paint - target: under 2.5 seconds):
- Identify the LCP element on each primary page (usually the hero image, hero heading, or above-the-fold content block)
- Serve the LCP element from the server or a CDN; never load it via lazy loading or JavaScript defer
- Compress and properly size hero images; use WebP format with a JPEG fallback
- Implement resource hints (preconnect, preload) for the LCP element's required resources

INP (Interaction to Next Paint - target: under 200 milliseconds):
- Audit and minimize third-party JavaScript (advertising tags, analytics scripts, chatbots, and personalization tools are the primary sources of INP issues)
- Defer or async-load non-critical JavaScript so that the main thread is available to respond to user interactions
- Use web workers to move heavy JavaScript processing off the main thread

CLS (Cumulative Layout Shift - target: under 0.1):
- Set explicit width and height attributes on all images and video embeds so the browser reserves space before the resource loads
- Avoid inserting content above existing content after load (ad injections and cookie banners are common CLS sources)
- Use CSS transform animations rather than animations that trigger layout recalculations

**Step 4: Schema markup implementation**
Implement schema markup for the content types that the brand publishes:

Article schema (all blog posts and editorial content):
- Include: headline, author (with Person schema), datePublished, dateModified, image, publisher
- Mark up the author with a full Person schema including their name, URL, and sameAs links to authoritative profiles (LinkedIn, Wikipedia if applicable)

FAQ schema (pages with question-and-answer format sections):
- Eligible for FAQ rich results in Google search
- Each Q&A pair should represent a question real users search for and a complete, standalone answer

HowTo schema (step-by-step tutorial content):
- Eligible for HowTo rich results with numbered steps displayed in search results
- Each step should be a discrete, actionable instruction

Product schema (product and service pages):
- Include: name, description, offers (price, availability), aggregateRating if review data exists
- Accurate price and availability data are required; outdated information triggers rich result removal

LocalBusiness schema (if the brand has physical locations):
- Include: name, address, telephone, openingHours, geo coordinates
- Keep location data synchronized with Google Business Profile

**Step 5: Internal linking framework**
The internal linking structure should reflect the topical hierarchy of the site:
- Pillar pages link to all spoke pages within their cluster (and spoke pages link back to the pillar)
- The homepage links to all primary pillar pages
- High-authority legacy pages (pages that have accumulated links over time) link to newly published important pages to accelerate their indexation and early ranking
- Identify orphan pages through a site crawl and add internal links to any indexable page that has zero or fewer than 2 internal links pointing to it

---

## Mobile-First Indexing Checklist

Before any new page is published:
- [ ] The mobile version of the page contains all the same content as the desktop version (text, images, structured data, and schema)
- [ ] The page renders correctly at 375px viewport width without horizontal scrolling
- [ ] Tap targets (buttons, links) are at least 48px by 48px
- [ ] Font size is at least 16px for body text on mobile
- [ ] The mobile LCP element loads within 2.5 seconds on a 4G connection
- [ ] No interstitials block content access on mobile within the first session

---

## Log File Analysis Protocol

For sites with more than 1,000 indexable pages, analyze server log files quarterly to understand actual Googlebot behavior:
- Which pages is Googlebot crawling most frequently? (These are the pages Google considers most important)
- Which important pages is Googlebot visiting infrequently? (These need more internal links or a recrawl request via Google Search Console)
- What is the Googlebot crawl rate compared to the site's total page count? (This reveals whether the site is using crawl budget efficiently)
- Are there URLs being crawled that should be excluded from the crawl? (Identifies robots.txt and canonical gaps)

Tools for log file analysis: Screaming Frog Log Analyzer, Semrush Log File Analyzer, or Cloudflare Analytics if the site uses Cloudflare.

---

## Cadence

- Full technical audit: annually (more frequently after major site migrations, CMS changes, or significant architecture changes)
- Core Web Vitals monitoring: monthly via Google Search Console's Core Web Vitals report
- Crawl audit: monthly for sites with frequent content publishing; quarterly for static or infrequently updated sites
- Schema markup review: quarterly to add new schema types for newly created content categories and to validate existing markup against Google's Rich Results Test
- Log file analysis: quarterly for sites with 1,000+ indexable pages
- Internal link audit: every time a new content cluster is launched, and quarterly for the full site

---

## Failure Modes

1. **No canonical strategy.** A site without self-referencing canonical tags on all pages, and without canonicals resolving all duplicate content situations (HTTP vs HTTPS, www vs non-www, trailing slash vs no trailing slash, paginated pages), presents Google with multiple versions of the same page. Google chooses which version to index, and often chooses incorrectly.

2. **Slow page speed on mobile.** A site that passes Core Web Vitals on desktop but fails on mobile is failing the Google index. Mobile is the primary indexing surface. Every image optimization, JavaScript deferral, and CDN configuration decision should be validated against mobile performance metrics, not desktop metrics.

3. **Duplicate content at scale.** Ecommerce sites with faceted navigation, category filter combinations, and paginated product listings generate thousands of near-duplicate URLs if not managed with canonical tags, noindex directives, and parameter handling. At scale, duplicate content consumes crawl budget, dilutes link equity, and can trigger site-wide quality downgrades.

4. **Orphan pages.** Pages that have no internal links pointing to them are effectively invisible to crawlers. A page that earns a backlink from an external site but has no internal links gets crawled rarely, indexed slowly, and does not distribute its authority to related pages. Run an internal link audit every time a new cluster of pages launches.

5. **Broken internal links.** Links from high-authority pages that point to 404 pages waste link equity and create poor user experiences. Audit internal links monthly using Screaming Frog or Ahrefs Site Audit and redirect or repair broken internal links within 7 days of discovery.

---

## Recommended Tools

- **Screaming Frog SEO Spider** (the primary technical audit tool; crawls the entire site and reports on broken links, redirect chains, missing meta tags, duplicate content, canonical errors, and orphan pages; essential for any site with more than 100 pages)
- **Google Search Console** (authoritative source for indexation data, Core Web Vitals field data, crawl error reporting, and manual action notifications; the only tool that shows what Google actually sees and has indexed from the site)
- **Google PageSpeed Insights** (combines lab performance data with field data from the CrUX dataset; use the field data (CrUX) for reporting on real user experience and the lab data for diagnosing specific optimization opportunities)
- **Ahrefs Site Audit** (cloud-based site audit tool that identifies technical issues, internal linking gaps, and content quality signals without requiring a local crawl; complements Screaming Frog for sites where running a local crawl is impractical)
- **Schema.org Validator and Google Rich Results Test** (free validation tools for confirming that schema markup is correctly implemented and eligible for rich results; run after every schema markup deployment)

---

## Adaptation for Your Brand

Technical SEO priorities differ significantly based on site architecture and platform. Sites built on managed platforms (Shopify, Squarespace, Wix) have limited server-level configuration options but often handle the foundational technical requirements adequately. Sites built on custom CMS platforms or frameworks (Next.js, Nuxt, custom WordPress configurations) have full technical control but also full technical responsibility.

For sites built on headless architectures or JavaScript-rendered content, rendering is the highest-priority technical issue. If content is rendered client-side and Googlebot cannot execute the JavaScript reliably, the rendered content never gets indexed. Use Google Search Console's URL Inspection tool to confirm that rendered page content matches the intended source content.

For ecommerce sites, crawl budget and duplicate content management are the highest-priority concerns because of the scale of URL generation through filters, sorting, and pagination. For content-heavy sites (blogs, news sites), indexation depth and internal linking are the highest-priority concerns because content published deep in the archive may never be crawled.

Align technical SEO investments with the content team's publishing calendar. A site migration, URL restructuring, or canonical change executed during a period of high content publishing activity creates attribution confusion and complicates performance analysis. Major technical changes should be executed in months with lower content publishing volume.
