# Mujo Website Rebuild — Execution Checklist

**Version:** 0.4 · **Date:** August 2026 · **Status:** Active · **Owner:** Mujo Panacea Ltd

**Purpose:** Ordered execution tracker for the website rebuild, aligned to Phases 1–5 in [requirements.md](requirements.md). Sitemap dispositions live in [sitemap.md](sitemap.md). Tick items as they complete; add new items in the relevant phase as they surface.

## At a Glance — Current Status (2026-08-10)

| Phase | State |
| --- | --- |
| **Phase 1 — Content Audit & Sitemap** | ✔ Complete (closed 2026-07-31) |
| **Phase 2 — Framework & Repo Setup** | ✔ Complete (scaffold + Netlify deploy done 2026-08-04) |
| **Phase 3 — Content Migration + IA Reshape + Brand + First-Draft Copy** | ⧗ Mechanical and structural complete; **content refinement + team bios + legal review pending** |
| **Phase 4 — Deployment & Staging** | ⧗ Live on `beta.mujofitness.com` (attached 2026-08-17); analytics + cookie banner + Netlify Forms notifications still open |
| **Phase 5 — QA & Cutover** | ◯ Not started |

## Pick up where we left off

Everything below is live in the repo (`main`) and deployed to Netlify on push. Latest commit at write time: `f7f577d Add mobile hamburger menu`.

**Immediate next actions in priority order** — each item is either yours or mine.

1. **Review the deploy on desktop and mobile.** *Yours.* Come back with any specific pages/sections that need adjustment.
2. **Team bios + photos.** *Yours.* Send ~80–120 words per person (Gerard Kool CEO, Michael Sasserini CFO, Andre Santos CMO, Jeff McBride role-TBC) + a portrait photo each (any format, I'll process). Also confirm Jeff's actual role.
3. **Editorial refinement pass on shell pages.** *Yours to review, mine to implement.* Every shell page (`/`, `/technology`, `/technology/dashboard-and-predictive-model`, `/investors`, `/athletes`, `/about`, `/faqs`) carries a first-draft I wrote using facts from Confluence and the WP source; each page has an `EDITORIAL REVIEW IN PROGRESS` banner. Read them, mark up what needs changing, send me the edits.
4. **123-reg DNS credentials.** *Yours.* When they arrive from the previous owner, tell me and I'll walk you through attaching `beta.mujofitness.com` (5 min).
5. **Netlify → Forms → Notifications.** *Yours.* In the Netlify dashboard, add an email notification pointing at `gerard@panacea.ws` so contact-form submissions reach you.
6. **Legal review of `/privacy` and `/terms`.** *Yours (or your solicitor's).* The pages are shells with placeholder banners; need real content from a solicitor before cutover.
7. **Regulatory review of medical-device claims.** *Yours (or CMO Andre).* Anything on `/technology`, `/technology/dashboard-and-predictive-model`, `/treatments/*`, and `/evidence/*` making a clinical claim needs an eye. I've kept language deliberately factual (FDA "listed", MHRA "registered", never "approved"; predictive model always future-tense) but a formal pass is required before publish.
8. **Analytics + cookie banner decision.** *Yours.* Options: GA4, Plausible, Fathom, or defer to post-launch. Tell me and I'll wire in.
9. **Image alt text for accessibility (WCAG 2.1 AA).** *Mine.* Migrated post images currently have blank `alt` attributes. One quick pass through all 89 posts once you've confirmed nothing else is moving.
10. **Content-authoring `CONTRIBUTING.md`.** *Mine.* Short doc so anyone (you or a future editor) can add a blog post or update a page without ceremony.

**Live on the deploy right now** — feature summary:

- **Brand applied** end-to-end per the 2015 MuJo Brand Guidelines: Medical & Rehabilitation Mint on Grey; `/athletes` swaps to Elite Sports Blue; MuJo logo in header + footer; Proxima Nova wired via Adobe Fonts.
- **Six-item top nav**: Technology · Evidence · For Athletes · Investors · About + Contact CTA. Header is dark grey with mint accents.
- **Mobile hamburger menu** with dark dropdown panel, animated bars-to-X icon, Escape/outside-click/link-click to close, full keyboard accessibility.
- **Home page**: hero with real device photo, partners strip (RNOH · EIOS · Manchester · Coventry · Innovate UK · Circle · HERC · IET) below the hero, two-up "In use today / Where we are going" section, latest three Evidence cards, and a pale CTA band at the bottom.
- **Technology page**: alternating text/image bands using the `MediaRow` component — mechanism (patent US 8,821,357, Imperial origin), software (Mujo 1.5 Android + Bluetooth), regulatory posture, roadmap to hip/knee/spine.
- **Dashboard and Predictive Model page**: deliberately future-tense throughout, SaMD framing, no specific model-performance claims.
- **Track Record page** (URL still `/evidence/`): renamed and split into 01 Clinical Studies · 02 In the Field · 03 Milestones, with retrospective framing in the hero.
- **Investors page**: market framing (US PT ~$30bn, ~7% CAGR), traction, IP, regulatory posture, team, Series A CTA.
- **Athletes page**: anchored on real evidence (EIOS Lilleshall, Wasps Rugby, GB Weightlifting), regulatory-safe framing (no performance-enhancement claims).
- **About + Team pages**: company story (Douglas Higgins 2006 invention → MuJo 2011 → MuJo Panacea today), five pillars, four placeholder team cards ready for Gerard's bios and photos.
- **FAQs**: grouped questions with contact-us CTAs on every answer, factually correct regulatory phrasing.
- **Contact page**: Netlify Forms wired, five-category routing dropdown, honeypot spam protection, `/contact/thanks/` landing page.
- **Resources page** (footer link): six evergreen educational articles (anatomy series, home exercises, impingement exercises).
- **Redirects**: `public/_redirects` covers every legacy WordPress URL — retired sections, killed posts, condition pages, WP-dated URL patterns. Wildcard fallbacks catch anything unmapped.

**What's out on staging that will still change:**

- Copy on every shell page is a first-draft awaiting your review — expect tone/length tweaks.
- Team page has placeholder silhouette avatars and generic bios.
- Home hero image is the legacy WordPress product shot; you flagged wanting to process this in Illustrator or find an alternative — the file path (`public/images/site/mujo-device-1.jpg`) is the only reference to swap.
- No analytics loaded, no cookie banner.
- `noindex` is on every page — Google can't crawl.
- Legal pages are shells.

## Phase 1 — Content Audit & Sitemap

- [x] Fetch pages via WP REST API (`/wp-json/wp/v2/pages`) — 40 pages retrieved
- [x] Fetch posts via WP REST API (`/wp-json/wp/v2/posts`) — 42 posts retrieved
- [x] Fetch categories and tags (12 categories, 0 tags)
- [x] Capture site chrome (nav, footer, analytics, partner logos, embedded widgets) from live homepage
- [x] Produce `sitemap.md` — per-URL disposition table drafted
- [x] Capture confirmed decisions from open questions into `requirements.md`
- [x] Gerard: 5 REVIEW-row dispositions resolved (2026-07-31 — `/research` KILL, `/consulting` KILL, `/faqs` KEEP with rewrite, `/book-free-taster` KILL, `/technology/dashboard-and-predictive-model` KEEP with language change)
- [x] Team confirmed 2026-07-31 — current team: Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), Jeff McBride carrying over; other six previous bios KILL
- [x] "My Portal" confirmed 2026-07-31 — clinician dashboard, retain link, final destination URL TBD
- [x] Approach to old news / blog confirmed 2026-07-31 — keep all 42 posts for rebuild; cull is a post-launch task
- [ ] Media library inventory (162 items) — deferred to Phase 3, driven by which pages need which assets

**Exit criteria:** `sitemap.md` approved. All five REVIEW rows + three follow-up decisions resolved. ✔ Achieved 2026-07-31.

## Phase 2 — Framework & Repo Setup

**Blocked by:** Phase 1 exit criteria.

### Deferred decisions to settle at this phase

- [x] Framework — **Astro** (confirmed 2026-07-31)
- [x] Content authoring — **Markdown / MDX in repo** (confirmed 2026-07-31)
- [x] Staging subdomain — **`beta.mujofitness.com`** (confirmed 2026-07-31)
- [x] Contact form backend — **Netlify Forms** (confirmed 2026-07-31)
- [ ] Cookie banner library — deferred to Phase 4 with analytics choice
- [ ] Analytics — deferred to Phase 4 (UA-73890747-1 is dead; effectively starting fresh)

### Repo scaffold

- [x] Astro 7 initialised in this repo (2026-08-04) — `package.json`, `astro.config.mjs`, `tsconfig.json`, `src/`
- [x] Folder structure mirroring the rationalised sitemap
- [x] Base layout (`BaseLayout.astro`, `PageLayout.astro`), Header, Footer, ReviewBanner, PostCard components
- [x] Placeholder brand tokens in `src/styles/tokens.css` — to be replaced when brand kit lands
- [x] Global styles + minimal component set (button, card, section, form fields)
- [x] MDX support wired via `@astrojs/mdx` v7
- [x] Content Collections defined with Zod schemas (posts / team / partners)
- [ ] Image pipeline via Astro `<Image>` component — currently using plain `<img>` for speed; upgrade in Phase 5 QA
- [ ] `CONTRIBUTING.md` describing content authoring conventions

**Exit criteria:** the empty scaffold deploys to Netlify at the chosen staging subdomain and shows a working home page skeleton and one blog post skeleton, both with correct fonts, colours, and header/footer chrome. **✔ Achieved 2026-08-04** — deployed to Netlify auto-URL; `beta.mujofitness.com` attaches when DNS credentials arrive.

## Phase 3 — Content Migration

**Blocked by:** Phase 2 exit criteria.

### Pages

Every route below now has a live shell, migrated body, or first-draft editorial copy on the deploy. Items marked ⧗ still need something from Gerard (editorial refinement, bios, legal review).

- ⧗ `/` (home) — first-draft copy live with device hero + partners strip + two-up + Evidence cards + CTA band. Refinement pass welcome
- ⧗ `/technology` — first-draft copy with alternating MediaRow bands. Refinement pass welcome
- ⧗ `/technology/dashboard-and-predictive-model` — first-draft, future-tense throughout; needs regulatory sign-off before publish
- [x] `/treatments/frozen-shoulder` — migrated + merged from both legacy sources. Accuracy review pending
- [x] `/treatments/shoulder-impingement` — migrated + merged. Accuracy review pending
- [x] `/treatments/shoulder-instability` — migrated. Accuracy review pending
- [x] `/treatments/upper-back-and-neck-pain` — migrated + merged. Accuracy review pending
- ⧗ `/athletes` — first-draft copy with sports-blue variant + case-study anchors; refinement pass welcome. Regulatory review for performance-adjacent claims
- ⧗ `/investors` — first-draft covering market, traction, IP, team, roadmap. Numbers to confirm before publish
- ⧗ `/about` — first-draft company story + five pillars + team link
- ⧗ `/about/team` — four placeholder cards (Gerard Kool CEO, Michael Sasserini CFO, Andre Santos CMO, Jeff McBride role-TBC). Awaiting bios + photos
- ⧗ `/faqs` — first-draft grouped questions with contact-us CTAs. Refinement pass welcome
- [x] `/contact` — Netlify Forms wired, five-category routing dropdown, `/contact/thanks/` landing
- ⧗ `/privacy` — shell only. Solicitor-drafted copy required before cutover
- ⧗ `/terms` — shell only. Solicitor-drafted copy required before cutover
- [ ] Confirm the clinician "My Portal" destination URL (or agree on a "coming soon" holding page) before cutover — do not ship a broken link
- [x] Strip any residual "book a free taster" CTAs — none appear in migrated content

### Content indexes

- [x] `/evidence` — clinical evidence library index driven by posts with `category: evidence`
- [x] `/blog` — educational content index driven by posts with `category: blog`
- [x] `/news` — press / milestones index driven by posts with `category: news`

### Blog / post migration

- [x] Migrate all 42 posts to MDX in `/src/content/posts/` — full carry-over, cull deferred to post-launch
- [x] Assign each migrated post to its content index (evidence / blog / news) — routed via `category` frontmatter into `/blog/`, `/news/`, `/evidence/`
- [x] Show original publication dates prominently — do not silently rebadge 2015 content as 2026
- [x] Auto-mark 2013–2019 posts as `archived: true` so readers see them for what they are
- [x] Consolidate categories: retire the four zero-post categories; retain News, Blog, Evidence

### Assets

- [x] Enumerate images referenced by posts (89 images from 38 posts with heroes + body figures)
- [x] Download images to `/public/images/posts/<slug>/` — 89/89 fetched via `scripts/download_media.sh`
- [ ] Add descriptive `alt` text on every image (WCAG 2.1 AA) — currently blank alts on migrated images, needs a pass
- [x] Extract partner logos and place in `/public/images/partners/` — 8 logos downloaded, used in `Partners.astro` on home page (2026-08-08)
- [x] Extract and rehost the MUJO logo, favicon, and any brand-mark variants — 1850×603 grey PNG in `/public/images/brand/logo-grey.png`; inverted via CSS on dark header + footer; mint favicon (2026-08-06)
- [x] Curated legacy device / clinical / sports / dashboard imagery downloaded to `/public/images/site/` and placed on Home, Technology, Athletes, About, and Dashboard pages (2026-08-08)

### Manual rebuilds

- [x] Contact form component (Netlify Forms) — `src/components/ContactForm.astro` + `/contact/` + `/contact/thanks/`
- [ ] **Gerard: Configure Netlify → Forms → Notifications to email gerard@panacea.ws** (Netlify dashboard task)
- [ ] Cookie banner (implementation TBD once analytics decision is made)
- [ ] Any newsletter signup (only if requested — not currently on scope)
- [x] Instagram feed — dropped; no equivalent added
- [x] Twitter widget — dropped; API instability makes it not worth it
- [x] Reusable `MediaRow` component for alternating text/image bands (2026-08-08)
- [x] Reusable `Partners.astro` component for logo strips (2026-08-08)
- [x] Mobile hamburger menu with accessible toggle (2026-08-10)

**Exit criteria:** every page in the rationalised sitemap is present on staging with reviewed and approved content, images rehosted, and no `TODO` / `LOREM IPSUM` / placeholder markers.

## Phase 4 — Deployment: Netlify + Staging Subdomain

**Blocked by:** Phase 2 exit criteria (but runs alongside Phase 3).

- [x] Connect the repo to Netlify (done by Gerard, auto-URL live)
- [x] Configure production branch, build command, publish directory (Netlify auto-detected Astro)
- [ ] Attach `beta.mujofitness.com` subdomain — **blocked on 123-reg credentials** from previous owner handover
- [x] Block indexing — `robots.txt` `Disallow: /` **and** meta `noindex,nofollow` on every page (both live)
- [ ] Verify staging is blocked from indexing via Google Search Console URL inspection (Phase 5 QA)
- [ ] Configure Netlify → Forms → Notifications to email gerard@panacea.ws
- [ ] Set analytics — **decision still deferred**: GA4 fresh, Plausible, Fathom, or defer to post-launch
- [ ] Set cookie banner — implementation follows the analytics decision (Plausible / Fathom → no banner needed)
- [ ] Set custom 404 page with search / navigate-home
- [x] Canonical URLs and Open Graph / Twitter card meta on every page (in `BaseLayout.astro`)
- [x] `sitemap.xml` generated via `@astrojs/sitemap` integration on every build
- [ ] Swap production `robots.txt` to allow crawling at cutover (currently blocking everything)
- [ ] Configure security headers on Netlify (CSP, X-Frame-Options, Referrer-Policy, etc.) — Phase 5 QA
- [ ] Set up Netlify build hook (only if a CMS is chosen — not applicable now)

**Exit criteria:** staging site is reachable at the chosen subdomain, blocked from indexing, and functionally complete.

## Phase 5 — QA & Cutover

**Blocked by:** Phase 3 and Phase 4 exit criteria.

### QA against the sitemap

- [ ] Cross-check every URL in [sitemap.md](sitemap.md) — every KEEP / MERGE row has a live target on staging
- [ ] Cross-check every KILL row has a 301 destination that makes sense (usually home, treatments, or the closest topical page)
- [x] Build the 301 redirect map file (`public/_redirects` — done 2026-08-05)
- [ ] Run each Phase 3 page through Lighthouse — target ≥90 on Performance / Accessibility / Best Practices / SEO
- [ ] Fix any regressions from those Lighthouse runs
- [ ] Broken-link check across staging (`lychee` or a similar link checker)
- [ ] Manual review on mobile, tablet, desktop breakpoints
- [ ] Manual test of contact form → confirm email arrives at gerard@panacea.ws
- [ ] Confirm cookie banner (if present) works as intended
- [ ] Legal review of `/privacy` and `/terms` complete
- [ ] Regulatory review of any medical-device claims on `/technology` and `/treatments/*`
- [ ] Gerard: full walkthrough approval

### Cutover

- [ ] Prepare a rollback plan — DNS TTL check, Cloudways instance confirmed live, credentials to hand
- [ ] Confirm dedicated contact inbox is live and reachable (swap gerard@panacea.ws → new inbox)
- [ ] Remove `noindex` meta tag and update `robots.txt` on the production build
- [ ] Verify the production build has no `noindex` in the rendered HTML
- [ ] Perform DNS swap — point `mujofitness.com` (and `www.`) A / CNAME to Netlify
- [ ] Monitor DNS propagation (`dig`, `nslookup` from multiple regions)
- [ ] Submit new `sitemap.xml` to Google Search Console
- [ ] Request re-crawl of the new site in Search Console
- [ ] Announce cutover internally

### Post-cutover monitoring (30-day rollback window)

- [ ] Keep the Cloudways WordPress instance live but unpublished for 30 days
- [ ] Day 1, 7, 14, 30 checks: Search Console for 404 spikes, ranking movements on head terms, analytics working
- [ ] Log any post-cutover fixes as new items in this checklist under a `Post-cutover fixes` heading
- [ ] Day 30: sign-off to decommission the WordPress / Cloudways instance
- [ ] Cancel Cloudways subscription
- [ ] Archive the final WP export (`wp-json` JSON + media) in this repo under `docs/audit/final-export/`

**Exit criteria:** the new site is live at mujofitness.com, the old WP instance is decommissioned, and no unresolved regressions remain from the 30-day monitoring window.

## Ongoing / Post-Launch (out of this rebuild's scope)

Tracked here so nothing gets lost, but not delivered as part of the initial cutover:

- [ ] Adding a headless CMS if non-technical editing becomes needed
- [ ] Multi-language content (deferred per [requirements.md](requirements.md#out-of-scope-for-this-rebuild))
- [ ] Customer / clinician portal (out of scope — separate product)
- [ ] Brand refresh once the new kit arrives from the previous owner

## Notes / Decisions Log

Add dated entries here as decisions are made. Keep the entry short — the reasoning belongs in [requirements.md](requirements.md) or [sitemap.md](sitemap.md).

* **2026-07-31** — Phase 1 kickoff. Confirmed: brand lifts from live site pending kit; analytics — audit found UA is dead so effectively starting fresh, choice deferred to Phase 4; partners retained; contact goes to gerard@panacea.ws until a dedicated inbox is ready.
* **2026-07-31** — Five sitemap REVIEW rows resolved. `/research` → KILL (301 to `/evidence`). `/consulting` → KILL (service no longer offered). `/faqs` → KEEP, rewrite with contact-us language throughout. `/book-free-taster` → KILL (offer retired — also strip residual CTAs from other pages). `/technology/dashboard-and-predictive-model` → KEEP, but language shifts from "we have" to "we are building"; a future offering aligned with the Mujo 2.0 roadmap, regulatory review required to avoid overstatement.
* **2026-07-31** — Team confirmed. Current team is Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), and Jeff McBride carrying over from the previous seven bios. The other six bios are KILL with 301 to `/about/team`. Bios and photos to be supplied by Gerard at Phase 3.
* **2026-07-31** — "My Portal" clarified: clinician dashboard access, either live or planned. Retain the link on the new site; final destination URL to be confirmed at Phase 3 / 4, with a placeholder acceptable if the dashboard is not yet ready by cutover. Do not ship a broken link.
* **2026-07-31** — Posts approach confirmed: keep all 42 posts for the rebuild. Reshape the site around the sitemap first, then cull dated news and refresh the blog post-launch. Per-post disposition file deferred as post-launch cleanup.
* **2026-07-31** — Phase 1 audit closed. Ready to begin Phase 2 (framework + repo setup) on Gerard's go.
* **2026-07-31** — Phase 2 stack locked in: Astro + Markdown/MDX in-repo + Netlify hosting + Netlify Forms for contact + `beta.mujofitness.com` staging. No new accounts required beyond the Netlify account already opened. Cookie banner + analytics choices remain deferred to Phase 4.
* **2026-08-04** — Astro 7 scaffold committed, dev server working end-to-end. Node 26 LTS installed via Homebrew as a prerequisite.
* **2026-08-05** — Phase 3 mechanical migration complete. 42 WordPress posts → MDX (blog / news / evidence) with 89 hero + body images rehosted. 13 retained pages have shells or migrated bodies with `ReviewBanner` markers for editorial pass. Contact form wired to Netlify Forms. 301 redirect map covers every KILL / MERGE row in the sitemap. Production build clean — 60 pages built in ~5s. Awaiting Gerard's editorial pass on home, technology, about, faqs, and legal pages; awaiting brand kit and team bios/photos.
* **2026-08-05** — Deployed to Netlify auto-URL. `beta.mujofitness.com` subdomain attachment paused pending 123-reg credentials from the previous-owner handover.
* **2026-08-06** — **IA reshape.** New nav: Technology · Evidence · For Athletes · Investors · About · Contact. Retired `/blog`, `/news`, `/treatments` landing; condition pages under `/treatments/` retained for SEO. New `/athletes`, `/investors`, `/resources` pages as shells. 42 migrated posts → 18 evidence + 6 resources + 18 killed. `_redirects` rewritten to cover every URL move: surviving news → `/evidence/`, surviving educational blog → `/resources/`, sports-derivative → `/athletes/`, others to nearest section landing. Production build clean at 42 pages in ~3s.
* **2026-08-06** — **Brand applied.** Sourced Gerard's MuJo Brand & Identity Guidelines (2015) from Drive. Palette locked in: Medical & Rehabilitation Mint `#78c4b7` on Grey `#484544` site-wide; Elite Sports Performance Blue `#222f5d` swapped in on `/athletes` via `data-brand="sports"`. Logo PNG placed in Header + Footer; favicon rebuilt in Mint. Proxima Nova stack front-of-queue.
* **2026-08-07** — **Adobe Fonts Proxima Nova wired.** Kit `wgh8jyb` linked in `BaseLayout.astro`; Montserrat stand-in dropped. Kit served under Gerard's personal Adobe CC subscription; no domain lock so it works on localhost, netlify.app, beta.mujofitness.com, and mujofitness.com at cutover.
* **2026-08-07** — **First-draft editorial content** on `/`, `/technology`, `/technology/dashboard-and-predictive-model`, `/investors`, `/athletes`, `/about`, `/faqs`. Regulatory-safe throughout — "FDA listed", "MHRA registered", never "approved"; predictive-model page future-tense throughout. ReviewBanner on every page reframed as "first-draft copy — Gerard to refine."
* **2026-08-08** — **Layout iteration round 1.** PageLayout widened from 44rem to 64rem then 76rem. PostCard rebuilt for strict consistency (200px hero, `object-fit: cover`, line-clamped title and description). Descriptions on 17 posts cleaned of leading image markdown; 9 post bodies stripped of `mujofitness.com` links. Evidence page renamed **Track Record** and split into 01 Clinical Studies · 02 In the Field · 03 Milestones with retrospective hero framing. `MediaRow` component added for alternating text/image bands with panel-colour options (white / subtle / grey). Ten curated legacy images downloaded to `public/images/site/` and placed on Home, Technology, Athletes, About, and Dashboard pages. Partner-logo strip added below home hero — RNOH · EIOS · Manchester · Coventry · Innovate UK · Circle · HERC · IET, grayscale with hover-to-colour.
* **2026-08-09** — **Header inverted.** Dark-grey header with white logo (grey PNG inverted via CSS filter), light nav labels, mint underline on the active item. Home hero panel becomes pure white so the device product-shot's white background blends seamlessly. Home CTA band flipped from dark to `--color-subtle` warm off-white with dark text.
* **2026-08-10** — **Mobile hamburger menu.** Nav below 900px was previously hidden with no fallback — inaccessible. Added an accessible hamburger button, dark dropdown panel with all six nav items + Contact CTA, animated bars→X icon, closes on Escape / outside-click / link-click. Uses `[data-open]` attribute rather than a class to sidestep an Astro scoped-CSS descendant-selector edge case.
* **2026-08-12** — **Real team bios + portraits landed.** Gerard supplied B&W square upscaled portraits and finalised bios from Google Docs. Titles reconciled: André = Chief Clinical Officer, Jeff = Chief Operating Officer. Team page reveal-on-click pattern added so uneven bio lengths don't break the grid layout (native `<details>` element, no JS).
* **2026-08-13** — **Investors page v2** published. Includes MuJo Panacea Ltd company number `17165284`, US PT market at ~$50bn / 5% CAGR, patent family (US 9,776,034, UK/EU 2683451, CN ZL2012800227917), MHRA registration CA015151, FDA IKK, and the £1m for 20% at £4m post-money ask. Named sports clubs deliberately held out of public copy per Gerard until placements are confirmed.
* **2026-08-17** — **`beta.mujofitness.com` live and public.** DNS attached via 123-reg (nameservers on GoDaddy — `domaincontrol.com`). CNAME `beta` → `mujo-beta.netlify.app`. Netlify SSL auto-provisioned. Netlify site protection disabled so colleagues can preview and give feedback without needing accounts.
