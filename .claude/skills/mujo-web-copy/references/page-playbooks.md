# Page playbooks

One brief per live page: who it is for, what it must achieve, the structure that works, and the specific trap. Ends with recommended changes to the page set.

Audience priority for the relaunch, per Gerard: **investors and partners first, then gyms, studios, PTs and physiotherapy practitioners.** End users are reached through their provider, not the website. Where a legacy page speaks to patients, it is being kept for search visibility, not conversion.

## Contents

- [Home](#home) · [Technology](#technology) · [Dashboard and predictive model](#dashboard-and-predictive-model)
- [Evidence / Track Record](#evidence--track-record) · [Evidence posts](#evidence-posts)
- [Athletes](#athletes) · [Investors](#investors) · [About](#about) · [Team](#team)
- [Treatments / conditions](#treatments--conditions) · [Resources](#resources) · [FAQs](#faqs) · [Contact](#contact)
- [Recommended changes to the page set](#recommended-changes-to-the-page-set) — **including the brief for the proposed `/clinics` page, which does not exist yet. If you are asked for a page that isn't in the list above, look there first.**

---

## Home

**Reader:** someone who arrived from a LinkedIn post, an investor introduction or a search, and will decide in fifteen seconds whether this is a serious company.

**Must achieve:** establish that MUJO is real, working, evidenced, and going somewhere. Route the three audiences without making any of them feel like the afterthought.

**Structure that works:**
1. Hero — one sentence on what the system does mechanically, one on where it is deployed. A real device photograph, not an abstraction.
2. Partner / institution strip. This is the highest-value screen real estate on the site; institutional logos do more persuasive work than any paragraph.
3. Two-up: "In use today" / "Where we are going". Keeps 1.5 and 2.0 cleanly separated, which is a regulatory requirement as much as an editorial one.
4. Three audience routes — clinics and practitioners · sport · investors.
5. Latest evidence — three cards, dated.
6. Single CTA band.

**Trap:** the hero wants to be a mission statement. Resist. The mission is on About. The hero is for the mechanism and the proof.

## Technology

**Reader:** a clinically or technically literate evaluator. A head of physiotherapy, a performance director, an investor's technical diligence contact.

**Must achieve:** explain *how it works* well enough that the reader can explain it to someone else. This is where MUJO wins, because most competitors are vague here.

**Structure:** alternating text/image bands (`MediaRow`) — mechanism (multi-axial cam, origin, patent) → what it measures → software (1.5 Android, Bluetooth, session capture) → regulatory posture → roadmap to 2.0.

**Traps:** (1) the patent number contradiction in `company-facts.md` §7 — resolve before publishing. (2) The regulatory band is where the site is most likely to overstate; state class and market plainly, one sentence each. (3) Do not let the 2.0 roadmap section drift into present tense.

## Dashboard and predictive model

**Reader:** investor, and a clinician wondering whether this becomes a decision-support tool.

**Must achieve:** communicate the ambition without making a software-as-a-medical-device claim MUJO has not earned.

**The existing page is already written future-tense with SaMD framing and no model-performance claims. Preserve that discipline exactly.** The HealthTracker Apps ruling (June 2026) puts the regulatory line between *recording* data and *interpreting* it — this page sits on that line by design. Descriptive language for what exists today (session counts, ROM tracked over time), explicit future tense for anything that infers, predicts or recommends. See `claims-guardrails.md` §4.

## Evidence / Track Record

**Reader:** a sceptical clinician or a diligence analyst who wants to know whether the evidence is real.

**Must achieve:** convert scepticism into confidence by being more transparent than the reader expects.

**The differentiator is cheap and nobody does it.** Sword Health's clinical studies index — the best-in-class comparator — lists studies with a one-line methodology summary but omits journal names and DOIs from the listing. Put **journal, year, study design, n, and a DOI or PubMed link on the listing page itself.** A clinician who can check a citation without clicking through trusts the whole site more.

**Structure:** three sections, as currently built — 01 Clinical Studies · 02 In the Field · 03 Milestones. Retrospective framing throughout; this is a record, not a promise.

**Trap:** a feasibility study is a feasibility study. Describe design and size honestly. Overclaiming here is the fastest way to lose exactly the reader this page is for.

## Evidence posts

Eighteen migrated posts. Each needs: what was done, where, when, by whom, with what result, and what it does not show. A named institution and a date at the top. Where a post is a press mention rather than research, say so — mixing the two devalues the research.

## Athletes

**Reader:** a head of performance or medical lead at a club, institute or university sport programme.

**Brand mode:** Elite Sports Blue `#222f5d` (`data-brand="sports"`). Register tightens — shorter sentences, performance vocabulary, less hedging.

**Must achieve:** show peer institutions already using it. EIOS Lilleshall, Wasps Rugby, GB Weightlifting are the assets. **Confirm current permission to name each one** — some of these deployments are years old and one of those organisations no longer exists in the form it did.

**Trap:** performance audiences invite injury-prevention language, which is a clinical claim. "Objective shoulder data across the squad" is safe; "reduces shoulder injuries" is not.

## Investors

**Reader:** an angel or fund principal in healthcare, medtech or digital health, doing a first pass.

**Must achieve:** make the case on traction, evidence, IP, regulatory competence and team — **without becoming a financial promotion.**

**This page has a live compliance problem.** It currently states the raise amount, the equity offered and the post-money valuation on an open page with a contact CTA. Read `claims-guardrails.md` §7 in full before touching it. The short version: s21 FSMA 2000 and s755 Companies Act 2006 both bite, s21 breach is a criminal offence and renders resulting investment agreements unenforceable, and the fix is either to move deal terms behind a compliant self-certification gate or to remove them from the public page entirely.

**What survives the fix, and is what actually persuades anyway:** the problem and its scale (sourced), the mechanism and IP position, installed footprint and named institutions, published evidence, regulatory pathway stated with fluency, the 2.0 programme and its funding structure, the team, and a plain contact route. Forward projections — ARR targets, break-even months, market share — belong in a data room.

**Trap:** the seed-vs-Series-A contradiction (`company-facts.md` §10.1) and the two different US market figures (§10.2). Neither can go on the page until settled, and the market figure needs a named source or it should be cut.

## About

**Reader:** everyone, second click.

**Must achieve:** the company story — invention in 2006, MuJo founded 2011, clinical work with RNOH and Manchester under Innovate UK, acquisition by MUJO Panacea, relaunch. This is the one page where naming the five pillars explicitly is legitimate.

**Trap:** the acquisition is an asset. A new team that bought a proven mechanism and is rebuilding it properly is a better story than pretending there was no discontinuity. Say it plainly.

## Team

Four cards: Gerard Kool (CEO), Michael Sasserini (CFO), André Santos, Jeff McBride (COO). 80–120 words each plus a portrait.

**Bio structure that works:** what they do at MUJO in one sentence · the credential that makes that non-obvious · one prior thing that proves it · what they are accountable for here. No career chronology, no adjectives about character.

**Traps:** settle André's title (CCO on the site, CMO in every regulatory document — and if he is the PRRC candidate, the site should match the technical file). Confirm the Sasserini/Sassarini spelling. Do not add the two clinical champions until confirmed.

## Treatments / conditions

Four pages: frozen shoulder, shoulder impingement, shoulder instability, upper back and neck pain. Reachable from Technology and Evidence, not in the top nav.

These are search-visibility pages, and they are the highest-risk pages on the site because condition content plus a product CTA converts the whole page into medical advertising under CAP 12.1 and 12.6.

**Rules for these pages:**
- Educational content and product claims stay structurally separated.
- The CTA is "find a clinic" or "talk to us about assessment" — never "treat your frozen shoulder with MUJO".
- CAP 12.2 — do not discourage the reader from seeking medical supervision. A line recommending they see a clinician is both required in spirit and good copy.
- Dual byline: written by, **medically reviewed by** a named HCPC-registered clinician, with a visible review date. Google's guidance on YMYL content weights trustworthiness most heavily and explicitly encourages accurate authorship information; a generic "by the MUJO team" byline is the anti-pattern.
- Answer-first structure: a direct two-to-four sentence answer, then question-based H2s.
- Cite NICE, NHS, CSP and peer-reviewed sources inline.

**Consider retargeting these at the clinician rather than the patient.** Gerard has deprioritised end users, and a page written for a physiotherapist about how MUJO fits an impingement protocol serves the real audience and carries less advertising risk than one written for a patient in pain.

## Resources

Six evergreen educational articles, footer-linked. Same byline and review discipline as conditions pages. Legacy exercise articles carry "book a free 30 minute session" CTAs from the old clinic model — those need replacing wherever they survive.

## FAQs

Grouped questions, contact CTA per answer. The most useful FAQs for the current audience are the ones nobody writes: what does installation involve, what training do practitioners need, what happens to the data and who owns it, what is the regulatory status, what does it cost to run. Note that FAQ schema no longer produces rich results in Google, so write these for humans rather than for markup.

## Contact

Five-category routing dropdown, Netlify Forms, honeypot, `/contact/thanks/` landing. Enquiry categories should match the audience routes on the home page. Keep the form short — for this audience, name, organisation, role, category, message is enough.

---

## Recommended changes to the page set

Gerard asked whether to add, delete or change pages given the targeting. Six suggestions, most valuable first.

**1. Add a page for clinics and practitioners.** This is the clearest gap. The nav has *For Athletes* and *Investors* but nothing addressed to the physiotherapy clinic, gym or studio buyer — an audience Gerard named as a priority. Everything on the site currently speaks to that reader by implication. A `/clinics` page (Medical & Rehabilitation mint) carrying: what a MUJO station does on a clinic floor, what the practitioner sees, footprint and installation, training time, what data they get and own, named peer sites, and a demonstration CTA. Structurally this mirrors the VALD Health / VALD Performance split, which is the best comparator in the sector.

**2. Add a procurement and compliance page.** In UK institutional sales this page is disproportionately load-bearing and almost nobody builds it: DTAC status, ISO 13485 position, data protection and residency, DPIA posture, UKCA/CE status, warranty and servicing. Note the revised NHS DTAC form — the previous version ceases to be used from April 2026 and the revision narrows focus to software-based digital health technologies, so **confirm which version applies to a hardware-plus-software platform** before publishing a DTAC statement.

**3. Fix `/investors` before anything else.** See above and `claims-guardrails.md` §7.

**4. Upgrade the Evidence listing to carry full citations.** Cheapest available credibility win. Journal, year, design, n, DOI on the index page.

**5. Consider whether the four condition pages are aimed at the right reader.** Either commit to them as clinician-facing protocol pages, or keep them patient-facing purely for search and accept they will not convert. What they should not be is patient-facing pages carrying product CTAs.

**6. The Leisure & Wellbeing sub-brand (Lime `#bed35f`) is unused.** If gyms and studios become a real commercial channel rather than a subset of "clinics", that brand mode exists and is currently sitting idle. Not urgent — but worth knowing it is there before inventing something new.

**On the five-pillar colour idea:** the 2015 guideline assigns colour to three sub-brands, not to the five pillars, so a per-pillar colour scheme would be a new brand decision rather than an application of the existing one. Worth confirming that is intended before building pages around it.
