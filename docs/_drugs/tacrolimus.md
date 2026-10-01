---
layout: default
title: Tacrolimus
parent: Model Prediction Only (L5)
nav_order: 869
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tacrolimus: From Transplant Immunosuppression to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor. In Canada it is marketed as oral products (Sandoz Tacrolimus, Advagraf), which are generally used to prevent organ transplant rejection. The TxGNN model predicts it may be effective for **seborrheic dermatitis**, mainly as topical tacrolimus ointment, and this is backed by **2 registered clinical trials** (one completed Phase 3, one completed Phase 4) and **20 retrieved publications**.

*Note: the Evidence Pack does not list an approved indication for any Canadian license, so the "original indication" above comes from general knowledge of these product names. It has not been confirmed from the data.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (marketed oral products are generally used for transplant rejection prophylaxis) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 by the rubric. The pack lists L1, but only one completed Phase 3 trial is registered (see Conclusion). |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank in this pack. The mechanism below comes from the pack's repurposing rationale and the retrieved literature. Tacrolimus inhibits calcineurin, which blocks T-cell activation and the release of inflammatory cytokines (IL-2, IL-4, IFN-gamma). It also has reported activity against *Malassezia* yeast.

Seborrheic dermatitis is a chronic, relapsing inflammatory skin disease of the face and scalp. It is linked to an abnormal inflammatory response to *Malassezia*. Both of tacrolimus's actions therefore match the disease biology. The reviews also describe topical calcineurin inhibitors as a steroid-sparing option for this condition.

The very high TxGNN score (99.26%) agrees with this reasoning. The practical caveat is that the supporting evidence concerns **topical** tacrolimus (0.03–0.1% ointment or cream). The Canadian licenses shown in this pack are oral products, so the topical route needs separate confirmation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Protopic (tacrolimus) ointment as maintenance treatment of severe seborrheic dermatitis on the adult face, aiming to reduce relapses and steroid use. Results are not included in the pack. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce exacerbations. Results are not included in the pack. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT (multicenter, double-blind) | J Am Acad Dermatol | Tacrolimus 0.1% vs ciclopiroxolamine 1% for maintenance therapy of severe facial seborrheic dermatitis. It addresses the lack of tested long-term maintenance options. The abstract in the pack does not give results. |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical trial | Ann Dermatol | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment, following the low-dose intermittent regimen used in atopic dermatitis. |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Comparative clinical trial | Ann Parasitol | Sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis. |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Comparative study | Indian J Dermatol Venereol Leprol | Oral itraconazole for two days plus topical tacrolimus vs topical tacrolimus alone for maintenance in Vietnam. No abstract available. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Topical treatments for facial seborrheic dermatitis (antifungals, keratolytics, corticosteroids). |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors are described as a safe alternative to corticosteroids, whose long-term adverse effects limit their use. |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis. |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Early experience with topical tacrolimus and pimecrolimus beyond atopic dermatitis, including seborrheic dermatitis. |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open pilot study | J Am Acad Dermatol | 18 patients on 0.1% tacrolimus for up to 28 days. 11 (61%) reached complete clearance. |
| [31053034](https://pubmed.ncbi.nlm.nih.gov/31053034/) | 2019 | Review (class-level) | J Cutan Med Surg | Off-label uses of topical pimecrolimus, a related calcineurin inhibitor. Indirect support only. |

---

## Canada Market Information

The pack lists 20 licenses and shows the first 5 below. Dosage form, manufacturer, and approved-indication text are blank for all of them.

| DIN | Product Name |
|---------|------|
| 2416832 | SANDOZ TACROLIMUS |
| 2416816 | SANDOZ TACROLIMUS |
| 2416824 | SANDOZ TACROLIMUS |
| 2296462 | ADVAGRAF |
| 2296489 | ADVAGRAF |

These product names correspond to systemic (oral) tacrolimus. Whether a topical tacrolimus license exists among the other 15 DINs was not verified.

---

## Safety Considerations

Please refer to the package insert for safety information.

- **Boxed warning (from the pack's guardrails):** Topical calcineurin inhibitors carry a boxed warning about long-term use. Use should be limited to the face or small areas.
- **Masking of infection:** Topical tacrolimus can alter the appearance of dermatophyte infection (tinea incognito, [PMID 20347654](https://pubmed.ncbi.nlm.nih.gov/20347654/)), which can resemble seborrheic dermatitis.
- **Route:** Evidence for seborrheic dermatitis applies to topical use only and should not be extrapolated to systemic tacrolimus.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial (NCT02004860), a completed Phase 4 study, and published randomized and clinical studies of 0.1% tacrolimus maintenance therapy directly address seborrheic dermatitis. The mechanism is plausible, and the two comparators in the Phase 3-type RCT (PMID 33010323) are established treatments. Strictly by the rubric this is L2, because only one completed Phase 3 trial is registered. PMID 33010323 appears to report that same trial, but this was not confirmed. The decision depends on topical use, limited-area application, and awareness of the long-term topical calcineurin inhibitor warning.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. The pack flags this as a blocking gap for safety screening.
- Confirmation of whether a topical tacrolimus product is licensed in Canada and what its label says, so on-label versus off-label status is clear.
- Published results and effect sizes for NCT02004860 and NCT01591070, plus confirmation of whether PMID 33010323 reports NCT02004860.
- Mechanism-of-action data from DrugBank.
- For context, the other predictions are weaker. Parapsoriasis rests only on case reports of the related pityriasis lichenoides (L4, research question). The broad "dermatitis" prediction is supported mostly by atopic dermatitis data and should not be generalized to other subtypes.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

