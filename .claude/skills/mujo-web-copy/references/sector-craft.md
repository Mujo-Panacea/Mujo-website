# Sector craft

How healthcare, medtech, fitness and sports-science websites actually earn trust — and what the comparators do well and badly. Researched August 2026; the web moves, so treat competitor detail as a snapshot.

## What the comparators do

| Company | Pattern worth stealing |
| --- | --- |
| **VALD** (vald.com) | Runs three co-equal brand portals — VALD Health (clinicians), VALD Performance (S&C and athletes), VALD Tactical (defence) — rather than one site with audience tabs. Homepage runs on countable facts ("over 8,000 clients in over 130 countries") rather than benefit adjectives. **The closest structural precedent for MUJO's clinics / sport split.** |
| **Sword Health** (swordhealth.com) | A dedicated clinical-evidence hub with study-level granularity, framed as "peer-reviewed studies, clinical research, and real-world evidence". Notably its listing page omits journal names and DOIs — **MUJO can beat the category leader cheaply by putting journal, year, design, n and DOI on the index itself.** |
| **Hinge Health** (hingehealth.com) | Audience-first navigation — "For Individuals" / "For Organizations", sub-routed to employers, health plans, consultants, providers — rather than product-first. Enterprise CTA is "Request a business demo". |
| **Kinvent** (k-invent.com) | Credibility architecture in order: institutional partnerships → awards → academic theses → practitioner testimonials. Copy sits almost entirely in measurement language: "precise dynamometry instruments", "quantification", "objectively assess". A good model for staying the right side of the claims line while still sounding confident. |
| **dorsaVi** (dorsavi.com) | A useful negative example in an adjacent space. Claims "medical-grade" and "speeds up rehab" with **no study citations, no outcome statistics and no conformity-marking statement on the page**. UK procurement leads discount this immediately, and per `claims-guardrails.md` it is also the pattern the ASA rules against. |

## The trust hierarchy

For a clinical or institutional buyer, persuasive weight runs roughly:

1. **Named peer institutions already using it.** Nothing else comes close. For MUJO: NHS trusts, the RNOH, EIOS, university sport departments, named clubs.
2. **Published, checkable evidence.** With journal, design and n visible.
3. **Validity and reliability data.** Clinics buying a measurement device ask two questions — is it accurate against a gold standard, and is it repeatable between clinicians. A published validation study or an accessible technical validation PDF closes more clinical deals than a demo video.
4. **Regulatory and procurement clarity.** Conformity status, ISO 13485, DTAC, data ownership, GDPR posture.
5. **A defensible commercial case.** Throughput, retention, reduced assessment time, chargeable outcome reporting.
6. **The team.**

Adjectives appear nowhere on that list.

## UK-specific assets most vendors miss

Two things a UK-facing MSK company can put on its site that competitors mostly don't:

**NHS DTAC** (Digital Technology Assessment Criteria) — five domains: clinical safety, data protection, technical security, interoperability, usability and accessibility. A published "DTAC completed" statement is a genuine procurement shortcut. *Caveat: a revised form followed NHS England's 2024 review; the previous version ceases to be used from April 2026 and the revision narrows focus to software-based digital health technologies — confirm which version applies to a hardware-plus-software platform before publishing a claim about it.*

**NICE Evidence Standards Framework** — tiers A/B/C. Stating which tier the product sits in, and what evidence that tier demands, signals a fluency most vendors don't have. Last substantively updated August 2022; worth re-checking currency.

## B2B page structure that converts

- **A landing page per buyer type**, each with its own hero, proof set and case studies. The VALD three-portal pattern at lower cost.
- **Hero = one measurable capability plus one named institution.** Not a benefit adjective.
- **One primary CTA per page**, repeated. Demo request is the universal primary conversion at this price point. A secondary "download the validation study" or spec sheet captures the technical reader who is not ready to talk to sales.
- **No public pricing.** Neither VALD nor Kinvent publishes it; this is settled convention for institutional equipment. Publish finance options instead if a price signal is wanted.
- **Case studies with a named organisation, a baseline, an intervention and a number.** Generic testimonials read as decoration.
- **A procurement/compliance page.** Disproportionately load-bearing in UK institutional sales and almost nobody builds it.
- **An ROI calculator**, if the CSP's national analysis holds up — they publish one, and building MUJO's own on the same logic (throughput, retention, assessment time) gives clinic buyers a reason to return to the site.

## Condition pages and search

Condition-led pages are where SEO and regulated claims collide. Google's own guidance says its systems look for experience, expertise, authoritativeness and trustworthiness, that **trust is the most important of these**, and that it gives even more weight to E-E-A-T for topics that could significantly affect health, financial stability or safety — the YMYL category, which every MUJO condition page is in.

Practical requirements:

- **Dual byline** — written by, plus **"medically reviewed by [name], HCPC-registered physiotherapist"**, with a visible review date and a linked author bio carrying registration number and affiliations. Google explicitly encourages accurate authorship information and bylines linking to author background. A generic "by the MUJO team" byline is the anti-pattern.
- **Answer-first structure** — a direct two-to-four sentence answer, then question-based H2s, short paragraphs, defined terminology. Serves readers and AI extraction equally.
- **Cite authoritative UK sources inline** — NICE, NHS, CSP, peer-reviewed journals.
- **An editorial policy page** documenting who reviews, how often, and how corrections are handled.
- **Keep education and product claims structurally separate.** A condition page ending in a product CTA converts the whole page into device advertising, and CAP 12.1 and 12.6 then apply to all of it.

**Schema markup — the accurate picture.** `MedicalWebPage`, `MedicalCondition` and `MedicalDevice` are **not** in Google's supported rich-results list, whatever an SEO vendor says. Mark them up for semantic and LLM benefit if wanted, but expect no rich results. What is worth implementing for actual rich results: `Organization`, `Product`, `Article`, `BreadcrumbList`, `VideoObject`, `ProfilePage` for author and reviewer bios, and `LocalBusiness` if there is a physical demonstration facility. **`FAQPage` and `HowTo` rich results were withdrawn by Google** — do not invest in FAQ schema for rich results.

## Things to re-check before relying on them

- **MHRA draft 2026 UK medical device regulations** — reported to introduce controls on misleading and unsubstantiated device claims and tighter equivalence rules. Adoption expected December 2026, in force June 2027. This will likely make GB claims rules materially stricter than the current CAP-only position.
- **NHS DTAC revised form** — confirm applicability to hardware-plus-software.
- **Financial Promotion Order thresholds** — changed twice inside 2024. Verify current figures at the moment any gated investor page is built.
- **A GB equivalent of EU MDR Art 21(3)** (demonstrating non-conforming devices at trade fairs) — **not verified.** Confirm with regulatory counsel.
- **NICE ESF** — last substantive update August 2022.

## Key sources

- ASA / CAP: <https://www.asa.org.uk/type/non_broadcast/code_section/12.html> · <https://www.asa.org.uk/advice-online/health-medical-devices.html> · <https://www.asa.org.uk/advice-online/remit-health-related-claims-addressed-to-medical-practitioners.html>
- ASA rulings: [HealthTracker Apps](https://www.asa.org.uk/rulings/healthtracker-apps-a26-1327464-healthtracker-apps.html) · [Cleriva](https://www.asa.org.uk/rulings/cleriva-a25-1304540-cleriva.html) · [Actegy](https://www.asa.org.uk/rulings/actegy-ltd-g24-1239847-actegy-ltd.html)
- MDR Article 7: <https://www.medical-device-regulation.eu/mdr-article-7-claims/>
- MHRA device regulation: <https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk>
- FCA PERG 8 (financial promotions): <https://handbook.fca.org.uk/handbook/perg8> · approver gateway: <https://www.fca.org.uk/firms/financial-promotions-and-adverts/approving-financial-promotions>
- Companies Act 2006 s755: <https://www.legislation.gov.uk/ukpga/2006/46/section/755>
- NHS DTAC: <https://digital.nhs.uk/services/digital-technology-assessment-criteria-dtac>
- NICE ESF: <https://www.nice.org.uk/corporate/ecd7/chapter/update-information>
- CSP return on investment: <https://www.csp.org.uk/publications/return-investment-physiotherapy-uk>
- Google helpful content / E-E-A-T: <https://developers.google.com/search/docs/fundamentals/creating-helpful-content> · rich results gallery: <https://developers.google.com/search/docs/appearance/structured-data/search-gallery>
