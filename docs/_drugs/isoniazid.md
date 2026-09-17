---
layout: default
title: Isoniazid
parent: Moderate Evidence (L3-L4)
nav_order: 423
evidence_level: L4
indication_count: 1
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line antimycobacterial drug historically used to treat and prevent tuberculosis. The TxGNN model predicts it may be effective for **Conjunctivitis**, with **1 clinical trial** and **20 publications** currently associated with this direction — though most of this evidence concerns tuberculosis-related eye complications rather than a general antibacterial or anti-inflammatory effect on conjunctivitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (inferred from mechanistic rationale; formal MOA record is a data gap) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for isoniazid is not available in the source record (drug-level data gap). Based on the mechanistic rationale captured alongside this prediction, isoniazid is known to inhibit InhA and block mycolic acid synthesis, giving it a specific antimycobacterial action. This mechanism has a plausible link only to **tuberculous conjunctivitis** — a rare ocular manifestation of TB infection — and not to conjunctivitis in general (viral, bacterial, or allergic).

The supporting literature largely describes cases where conjunctivitis is a *symptom or complication of tuberculosis* (e.g., phlyctenular keratoconjunctivitis, tuberculous conjunctivitis of the eye or socket), or where conjunctivitis appears as an *adverse drug reaction* to isoniazid or related TB therapies (e.g., BCG-associated arthritis with conjunctivitis, toxic epidermal necrolysis). This is an important distinction: the TxGNN score likely reflects an indirect knowledge-graph association ("isoniazid treats TB" → "TB can present as conjunctivitis") mixed with adverse-event signals, rather than genuine evidence that isoniazid treats conjunctivitis as a standalone indication. Two records — a 1965 report on isoniazid prophylaxis for phlyctenular keratoconjunctivitis and a 1971 report on local isoniazid treatment of ocular tuberculosis — are the closest to a direct therapeutic signal, but both are old, small, and specific to TB-associated ocular disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic adverse drug reaction rates between 3HP and 1HP regimens for latent TB infection; this trial evaluates isoniazid safety in TB prevention, not conjunctivitis efficacy or outcomes (rated low relevance to this indication). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Case Series | Am Rev Respir Dis | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Eskimos in southwestern Alaska — the most direct isoniazid-conjunctivitis therapeutic link in this evidence set. |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case Report | Annales d'oculistique | Local (topical) use of isoniazid in treatment of ocular tuberculosis. |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Reviews ocular side effects of systemic drugs; notes conjunctivitis/blepharoconjunctivitis has been associated with isotretinoin, sulfonamides, salicylates, and antineoplastic agents — isoniazid not specifically implicated as causative here. |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Review | Annals of Ophthalmology | General review touching on rifampicin/anti-TB therapy in ophthalmology context. |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Archives of Ophthalmology | Primary tuberculosis of the conjunctiva — describes TB as a cause of conjunctivitis, not isoniazid treating conjunctivitis. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | Mycobacterium tuberculosis presenting as chronic red eye/conjunctival TB. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket, treated within standard anti-TB regimen. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case Series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, mostly in children with primary TB. |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case Report | Can J Ophthalmol | Conjunctival phlyctenulosis re-emphasized as a presenting sign of impending clinical tuberculosis. |

---

## Canada Market Information

Isoniazid is currently **not marketed** in Canada under this record — no active DINs or product licenses are listed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between isoniazid and conjunctivitis appears to be a confounded knowledge-graph signal rather than a genuine repurposing opportunity: the supporting evidence overwhelmingly describes conjunctivitis as either a *manifestation of tuberculosis itself* or an *adverse reaction* to anti-TB therapy, not a condition isoniazid treats independently of TB. The one clinical trial in the evidence set evaluates isoniazid safety in latent TB infection and has no direct bearing on conjunctivitis outcomes. Combined with a blocking data gap on regulatory warnings/contraindications (DG001) and the drug's current non-marketed status in Canada, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Isoniazid mechanism-of-action (MOA) confirmation and disambiguation from the TB-conjunctivitis confound (DG002)
- Regulatory safety label data — warnings and contraindications (DG001, currently blocking)
- Evidence specifically testing isoniazid against non-tuberculous conjunctivitis, if this indication is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

