# Voice and brand

Derived from the *MuJo Brand & Identity Guideline* (Thomond, January 2015), the current repo implementation, and the audiences the relaunch site is actually for.

## The five pillars

Health · Science · Technology · Data · People.

From the guideline: *"These five core principles of our expertise have been used as the basis to form the visual structure of our identity. Each pillar visually represented by a circle, forms the axis' which hold together the structural form of our logo."*

They are a **test, not a template**. A strong MUJO page usually touches two or three of them naturally; the site as a whole should cover all five. Never write a section per pillar or name them in body copy on a marketing page — that turns a brand structure into filler. The About page is the one place it is legitimate to state them explicitly.

Used as a diagnostic, they are genuinely useful. A page that touches only Technology reads as an engineering spec. A page that touches only People reads as a brochure. Most weak MUJO drafts are missing **Data** — the thing that makes this company different from a manufacturer of gym equipment is that every repetition becomes a record.

**One thing to know:** the 2015 guideline maps colour to three *sub-brands* (Medical & Rehabilitation, Elite Sports Performance, Leisure & Wellbeing), not to the five pillars. The pillars have no colour assignment in the source document. If per-pillar colour is wanted on the site, that is a new decision extending the brand rather than an application of it — worth saying out loud rather than assuming.

## Brand modes

| Mode | Colour | Where | Photography direction (2015) |
| --- | --- | --- | --- |
| Corporate | Multi-colour from the 12-colour palette, max four per element | Non-sector-specific communication | "MADE TO MOVE" — vibrant, active, natural, not elitist |
| Medical & Rehabilitation | **Mint `#78c4b7`** | Site default in the current build | "CARE & REPAIR" — physiotherapy, clinician-and-patient scenarios, human-centric |
| Elite Sports Performance | **Blue `#222f5d`** | `/athletes`, via `data-brand="sports"` frontmatter | "TO THE LIMIT" — athletes in peak condition, individuals and teams |
| Leisure & Wellbeing | **Lime `#bed35f`** | Not currently used on the site | "MIND, BODY & SOUL" — the health-conscious individual |

Universal: Grey **`#484544`** and White **`#ffffff`**. Type is Proxima Nova (Adobe Fonts kit `wgh8jyb`), Arial as fallback. Colour lives in the "M" icon only — the logotype is always grey or white.

**Voice shifts with mode.** Medical & Rehabilitation is the site default and the register is peer-to-peer clinical: precise, unhurried, evidence-forward. Elite Sports is tighter and more direct — shorter sentences, more verbs, performance vocabulary. The guideline's own instruction for the medical audience is the best single line in the document: the brand must *"quickly find common ground and make them feel comfortable that we understand their world."* That is the whole job.

## How MUJO sentences work

**Fact first, meaning second.**

> Twelve devices are in the field — NHS trusts, orthopaedic hospitals, elite sport institutes, private clinics. The 1.5 release brings their data layer back online.

not

> MUJO is trusted by leading healthcare providers across the UK to deliver world-class rehabilitation outcomes.

**Concrete nouns over abstract ones.** Shoulder, cam, torque, repetition, session, protocol, clinician, joint envelope. Not solution, offering, ecosystem, platform-as-a-service.

**Let the important sentence stand alone.** MUJO copy should have rhythm. Three medium sentences and then a short one that lands.

**Explain the mechanism.** This audience rewards being told *how* something works. The multi-axial cam, admittance versus impedance control, process measurement versus outcome measurement — these are the most persuasive material the company has, and most competitors' sites are too vague to compete on them.

**Write to a peer.** The reader is a clinical lead, an investment principal, a head of performance. They have read a hundred of these pages. Assume competence, skip the education, get to the specific.

## Lexicon

**Use:** multi-axial · full envelope of motion · objective measurement · process measurement · session data · admittance control · clinician · practitioner · installed fleet · deployment · protocol · evidence · musculoskeletal / MSK

**Avoid:** revolutionary · cutting-edge · game-changing · state-of-the-art · seamless(ly) · unlock · empower · journey · holistic · synergy · leverage (as a verb) · solution (as a noun for the product) · world-class · best-in-class · trusted by · transform(ative)

**Handle with care** — these are claims, not adjectives; see `claims-guardrails.md`: medical-grade · clinically proven · independently validated · intelligent · smart · predictive · AI-powered

### Already live — do not propagate

The draft site breaks these rules in a few places. `mdx-contract.md` tells you to match the style of the surrounding pages, so these need calling out explicitly, or they get copied forward:

| Where | Wording | Problem |
| --- | --- | --- |
| `index.astro` | "Trusted by clinicians and elite institutions." | On the avoid list. Replace with the named institutions — which are more persuasive anyway. |
| `index.astro`, `technology.mdx`, `investors.mdx` | "clinical-grade data" | Same pattern as "medical-grade": reads as a regulatory status, isn't one. "Structured session data" or "an objective record" says the same thing without the claim. |
| `gerard-kool.md` | "medical-grade image analytics" | Describes a previous employer's product, so lower risk — but check it against what AOS can actually substantiate before it goes public. |

Fix these when you touch the page for another reason. Flag them if you spot new ones.

**British English.** Optimise, recognise, programme (for a project), metre, colour. Metric units. "NHS trust" lower-case t unless naming a specific one. Sentence case for headings. En dashes with spaces for parenthetical asides — like this — rather than em dashes tight.

## Rewriting the legacy voice

The WordPress site's register was consumer-clinic: *"Book a Free Intro Session"*, *"why not book a free 30 minute session at a time of your choice before scrolling down?"* That was a London walk-in clinic selling to individuals. The relaunch is selling a platform to institutions and a company to investors. When migrating legacy copy, the whole address changes — not just the words.

**Before** (legacy home page tagline):
> MUJO is the latest connected rehabilitation technology, independently validated within the NHS and elite sport.

Three problems: "latest" ages badly and says nothing; "independently validated" reads as a regulatory status and isn't one; "within the NHS and elite sport" is vague where the specifics are impressive.

**After:**
> A shoulder rehabilitation system that trains the joint across its full range of motion and records every repetition. Studied at the Royal National Orthopaedic Hospital. In use at the English Institute of Sport.

Same length. Every clause checkable. More interesting.

## Headlines

- **Say the thing.** "The shoulder does not move in one plane. Neither should the machine." beats "Rethinking rehabilitation."
- **A number in a headline earns its place.** "Twelve devices. Six sites. Every rep recorded."
- No colons-and-a-subtitle construction on every heading; it becomes a tic.
- Questions as headlines are usually a hedge. Make the statement instead.

## Calls to action

The primary conversion for this price point and audience is a conversation, not a purchase. "Request a demonstration", "Talk to us about a pilot", "Download the validation study". Not "Get started", "Learn more", "Book now". One primary CTA per page; a secondary document-download CTA captures the technical reader who is not ready to talk to anyone.
