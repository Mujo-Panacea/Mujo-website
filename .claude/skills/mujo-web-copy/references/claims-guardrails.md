# Claims guardrails

What MUJO can and cannot say on a public web page. Two separate bodies of rule bite: medical device advertising, and financial promotion. The second is the one companies at MUJO's stage most often get wrong, and it carries criminal liability, so it is covered here in full.

**This is drafting guidance, not legal advice.** Nobody involved in producing it is a lawyer or a regulatory consultant. Every judgement here should be checked by Andre Santos (clinical/regulatory) or a solicitor before publish. Where this file says "verify", treat it as blocking.

## Contents

1. [The governing idea](#1-the-governing-idea)
2. [The UK regime for device advertising](#2-the-uk-regime-for-device-advertising)
3. [The measurement / therapeutic line](#3-the-measurement--therapeutic-line)
4. [What each MUJO product may claim](#4-what-each-mujo-product-may-claim)
5. [Advertising before conformity marking](#5-advertising-before-conformity-marking)
6. [The clinician-only carve-out](#6-the-clinician-only-carve-out)
7. [Financial promotion — the investor page](#7-financial-promotion--the-investor-page)
8. [Statistics discipline](#8-statistics-discipline)
9. [Pre-publish checklist](#9-pre-publish-checklist)

---

## 1. The governing idea

The cleanest checklist in existence is **EU MDR Article 7**, which prohibits text, names, trademarks or pictures that mislead the user about the device's intended purpose, safety or performance by:

- (a) ascribing functions and properties to the device which it does not have;
- (b) creating a false impression regarding treatment or diagnosis;
- (c) failing to inform the user of a likely risk associated with use of the device;
- (d) suggesting uses other than those stated as the intended purpose for which the conformity assessment was carried out.

Article 7 applies directly in the EU and Northern Ireland, not Great Britain. **Use it as the drafting discipline anyway.** MUJO's EU market is the primary conformity route for 2.0, and the MHRA's draft 2026 UK regulations are reported to introduce new controls on misleading and unsubstantiated device claims — adoption expected December 2026, in force June 2027. Copy written to Article 7 now survives that; copy written to today's looser GB position may not.

Test (d) is the one that catches good companies. A device conformity-assessed as a measurement aid, marketed with recovery language, fails (d) even if every individual sentence is technically defensible.

## 2. The UK regime for device advertising

There is no sector-specific advertising legislation for medical devices in Great Britain and no statutory pre-approval of advertising. What binds instead:

**CAP Code Section 12** (non-broadcast advertising, enforced by the ASA):

- **12.1** — "Objective claims must be backed by evidence, if relevant consisting of trials conducted on people." Medicinal claims are permitted for a medical device carrying the applicable conformity marking.
- **12.2** — must not discourage essential treatment for conditions for which medical supervision should be sought.
- **12.6** — must not falsely claim a product can cure illness, dysfunction or malformations.

**DMCC Act 2024** (consumer-facing unfair commercial practices, in force April 2025) and the **Business Protection from Misleading Marketing Regulations 2008** (B2B — which is most of MUJO's site).

Three ASA rulings worth internalising, because they map almost exactly onto MUJO's situation:

| Ruling | What it establishes |
| --- | --- |
| **HealthTracker Apps** (A26-1327464, June 2026) — upheld | A blood-pressure *logging* app crossed into unauthorised medical claims because its colour-coded chart constituted "enhancement of data". **The regulatory line sits between recording a number and interpreting a number.** This is precisely the boundary the MUJO dashboard and predictive-model page walks. |
| **Cleriva t/a NovaFlow** (A25-1304540, Nov 2025) — upheld | No medical claims are permitted at all for a product that is neither MHRA-registered nor conformity-marked. |
| **Actegy Ltd / Revitive Medic** (G24-1239847, Aug 2025) — partly upheld | A CE-marked Class IIa device successfully substantiated "relieves leg aches and pains" with an 8-week trial, but was found against for "reduces swelling" because the ad failed to qualify that the effect was temporary and session-linked. **Conformity marking buys the right to make claims; it substantiates none of them. Each claim needs its own evidence, at the same magnitude and duration the evidence actually supports.** |

The practical consequence for MUJO: a claim is only as strong as the specific study behind it, and it must be worded to the study's actual scope — same population, same duration, same effect size. "Improves shoulder function" is not a fair summary of a feasibility study in 20 patients.

## 3. The measurement / therapeutic line

This table is the working tool. The left column describes the device and what it captures. The right column describes what happens to the patient.

| Safe — device capability and measurement | Requires marking **and** claim-specific clinical evidence |
| --- | --- |
| "Trains the shoulder across its full envelope of motion, not a single plane" | "Restores shoulder function" |
| "Measures range of motion through the movement, not just at the end points" | "Improves range of motion" |
| "Captures every repetition as structured session data" | "Speeds up recovery" |
| "Gives the clinician an objective record of how the patient moved" | "Reduces re-injury risk" |
| "Quantifies force output across the session" | "Prevents shoulder injury" |
| "Designed to replicate the body's natural range of motion" | "Clinically proven to treat frozen shoulder" |
| "In use at the Royal National Orthopaedic Hospital" | "Recommended by the NHS" |
| "Studied in a feasibility trial at RNOH, published in *BMC Musculoskeletal Disorders*" | "Proven effective in NHS trials" |

Everything in the left column still needs substantiation under CAP 12.1 — accuracy and validity are objective claims. But it does not require a medicinal-claim conformity marking, and it is where MUJO's genuinely distinctive material lives anyway. Multi-axial training, process measurement rather than outcome measurement, admittance control versus impedance control — these are capability claims, they are true, and no competitor can copy them.

**Three phrases to strike on sight**, because they read as clinical claims regardless of intent: *medical-grade* (unless naming the actual conformity marking in the same sentence), *clinically proven*, *independently validated* used bare. The legacy site's tagline — "independently validated within the NHS and elite sport" — is exactly this pattern: it sounds like a regulatory status and is actually a summary of a feasibility study. Replace it with the specific study and where it was done.

**Never position the device as the agent of recovery.** The clinician treats the patient. MUJO gives the clinician something they could not previously see or control. That framing is safer, truer, and lands better with the clinical audience anyway.

## 4. What each MUJO product may claim

| Product | Status | Permitted register |
| --- | --- | --- |
| **The installed mechanical device** | On market; registrations per the fact register (verify) | Capability, mechanism, measurement, deployment sites, published research about it. No therapeutic outcome claims. |
| **MUJO 1.5** | Software release; the regulatory pack describes the baseline as a **range-of-motion measurement and reporting aid** | Describe it as measurement, feedback, guidance and reporting. **Do not describe it as therapy, treatment or rehabilitation delivery.** It guides prescribed exercises and records what happened; the prescription is the clinician's. |
| **MUJO 2.0** | In development. Not CE or UKCA marked. No clinical investigation run. Notified Body not appointed. | **Future and conditional tense only.** "Being developed to…", "targeting…", "the 2.0 programme aims to…". Never present tense. Never a patient-outcome claim. Say plainly that it is in development and not yet available. |
| **Dashboard / predictive model** | Internal recommendation is to exclude clinical-decision AI from V1 and ship descriptive reporting only | Descriptive language: counts, trends, session history, "tracked over time". **Not** "predicts recovery", "flags patients at risk", "recommends". The HealthTracker ruling is the reason. The existing page is already written future-tense with SaMD framing — preserve that discipline. |

### Intended use and setting is itself a claim

This one is easy to miss, because it isn't about wording at all. **MDR Article 7(d) prohibits suggesting uses other than those stated as the intended purpose for which conformity assessment was carried out.** Who you address a page to, and where you show the device being used, is a statement about intended use.

MUJO 2.0's stated intended use at V1 is **professional / clinical setting only**; home use is explicitly out of scope (REG-002 §2). So:

- **Gyms and studios are a live question, not a settled one.** A rehabilitation gym with a physiotherapist or S&C lead on staff is plausibly a professional setting. A consumer health club floor is not. If a page addresses gyms, say which kind, and flag for Andre that the intended-use statement needs to cover it. This is a regulatory question before it is a copy question — do not resolve it in the copy.
- **Never write or imply home use, unsupervised use, or direct-to-consumer purchase.**
- **Photography carries the same weight as words.** A device shown in a domestic setting makes a home-use claim whatever the caption says.

## 5. Advertising before conformity marking

A device without the applicable conformity marking cannot carry medical claims in advertising (Cleriva; HealthTracker). What MUJO *can* do publicly for 2.0:

- describe the clinical problem and its scale (with sourced statistics);
- publish its own and others' research;
- describe the technology, the engineering approach and the development programme;
- state the regulatory pathway it is pursuing and where it is on it;
- talk about it to investors through the compliant channels in section 7.

Under EU MDR Article 21(3), non-conforming devices may be shown at trade fairs and demonstrations provided a visible sign indicates they are for presentation only and cannot be made available until brought into compliance. **A GB equivalent of Art 21(3) has not been verified — check with regulatory counsel before relying on it.** For web, the conservative and conventional equivalent is a plain statement on the page: *"MUJO 2.0 is in development and is not available for sale. It has not been assessed for conformity under EU MDR or UK MDR."*

Stating the regulatory pathway openly is a strength, not a weakness. Investors and NHS procurement leads both read "Class IIb under MDR Rule 9, Notified Body route, clinical investigation planned" as a company that knows what it is doing. Vagueness reads as a company that does not.

## 6. The clinician-only carve-out

The CAP Code does not apply to claims in marketing communications in media addressed **only** to medical, dental, veterinary or allied practitioners, where the claims relate to those practitioners' expertise. This extends to websites clearly addressed solely to healthcare professionals.

The exemption is narrower than it sounds: it covers specific claims rather than whole advertisements; the medium must be addressed *exclusively* to practitioners; and general claims (pricing, "best-selling", offensiveness) stay in remit. **An open site with a "for clinicians" tab does not qualify.**

The practical opportunity: a genuinely gated, HCP-only clinical section could carry efficacy and comparative clinical data that the open marketing pages cannot. If MUJO wants to publish full study data to physios and sports medicine leads, that is the structure to propose. Do not treat it as a loophole for marketing copy.

## 7. Financial promotion — the investor page

**This is the sharpest edge on the site.** Two independent prohibitions apply, and most founders only know about one.

**Section 21, Financial Services and Markets Act 2000.** An unauthorised person must not, in the course of business, communicate an invitation or inducement to engage in investment activity, unless the content is approved by an authorised person or an exemption applies. The FCA applies an objective test (PERG 8.4.4G): would a reasonable observer consider the communicator intended to persuade or incite engagement in investment activity? Presenting purely factual information typically is not an inducement (PERG 8.4.13G), but promotional framing almost always is (PERG 8.4.12G). Breach is a **criminal offence carrying up to two years' imprisonment**, and — the part that reaches the company commercially — **investment agreements entered into in consequence are unenforceable.**

**Section 755, Companies Act 2006.** A private company limited by shares must not offer securities to the public, or allot securities with a view to their being offered to the public. This applies independently of FSMA, so an FSMA exemption does not cure it.

**So, can a public page state the raise and the valuation?**

- Stating that a round has **closed**, its size, and named investors: yes. That is factual corporate news.
- Stating "we are raising £X for Y% at a £Z valuation — get in touch": **no, not on an open public page.** That is a paradigm invitation or inducement under the objective test, made in the course of business by an unauthorised person, and it is also an offer to the public for s755 purposes.

**The current `/investors` page states the raise amount, the equity offered and the post-money valuation, with a contact CTA, on an open page. That combination is the pattern the rules are aimed at, and it should not go live in that form without an authorised person's approval or a compliant gate.** Flag this every time the page is touched until Gerard confirms it has been resolved with a solicitor.

The compliant patterns, in ascending order of cost:

1. **Open page carries no deal terms.** Market framing, team, traction, published news of prior rounds, regulatory status, IP, and a plain `investors@` contact address. No raise size, no valuation, no instrument, no terms, no returns language, no "opportunity". This is the cheapest fix and preserves nearly all the persuasive content — because what actually convinces a venture investor is the traction, the evidence and the team, not the number in the ask.
2. **Gated self-certification wall** in front of any deal content, requiring the visitor to certify as a certified high net worth individual, certified or self-certified sophisticated investor, or investment professional under the Financial Promotion Order, with the prescribed investor statement and risk warnings. Thresholds changed twice during 2024 — **verify the current figures at the moment the gate is built.** Gating is not magic: proper systems and procedures are expected to prevent access by unintended recipients.
3. **Section 21 approval by an authorised firm.** Since the FCA's approver gateway took effect in February 2024, an authorised firm needs specific FCA permission to approve promotions for unauthorised persons — this narrowed the pool and made ad-hoc approval materially more expensive than before.
4. **Route the raise through an FCA-authorised platform**, which handles both the s21 and s755 problems; the site then links out rather than promoting.

Conventional disclaimer furniture on any gated page: jurisdiction restriction, capital-at-risk warning, "past performance is not a guide to future performance", "this is not a prospectus", "no advice is given", and identification of who approved the communication and when. **Exact wording is a matter for a solicitor, not a template.**

Forward-looking figures — ARR targets, break-even dates, market-share projections — belong in a data room, not on a website, both for FSMA reasons and because they invite diligence you have not prepared for.

## 8. Statistics discipline

MUJO's research corpus is genuinely strong, and genuinely full of traps. The rules:

- **Quote the source, the year of the data, and the scope.** Not the year of publication if they differ.
- **Never launder a secondary citation.** If a UK paper quotes a 1995 Dutch incidence figure, cite the Dutch paper — or don't use the figure.
- **Never widen a figure's scope.** "Upper limb" is not "shoulder". "Frozen shoulder" is not "shoulder pain". "Cumulative registry entries" is not "annual procedures".
- **Say what a figure is.** A social return on investment is not a cash return; presenting SROI as money returned to a payer misrepresents the study and the authors say so explicitly.
- **Price years matter.** 2018 costs quoted in 2026 need the price year attached.
- **If you cannot state the source in the sentence or a footnote, cut the number.**

`evidence-library.md` has the verified figures, their real sources, and the specific trap in each.

## 9. Pre-publish checklist

Run this before handing over any page:

- [ ] Every device claim sits in the left column of section 3, or has a named study behind it that supports it at that magnitude and duration.
- [ ] MUJO 2.0 appears only in future or conditional tense, with its development status stated on the page.
- [ ] Dashboard language is descriptive, not interpretive.
- [ ] No "medical-grade", "clinically proven", or bare "independently validated".
- [ ] Every statistic carries source, year and scope.
- [ ] Every named institution, customer or individual has current permission to be named.
- [ ] Nothing on an open page reads as an invitation to invest; no raise amount, valuation or terms outside a compliant gate.
- [ ] Regulatory status stated plainly where relevant, per market.
- [ ] Anything you were unsure about is flagged in a `<ReviewBanner>` on the page, not just mentioned in chat.
