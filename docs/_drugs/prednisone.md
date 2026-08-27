---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Prednisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Prednisone: From General Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Prednisone is a synthetic glucocorticoid; this evidence pack does not have its original approved indication on file (the product is not currently marketed in Canada, and DrugBank MOA data was not returned).
The TxGNN model predicts it may be effective for **Alopecia Areata**, a hypothesis reinforced by decades of existing off-label clinical practice — supported here by **32 clinical trials** (mostly indirect autoimmune-mechanism analogs) and **20 publications**, including one completed Phase 3 RCT that tested prednisone directly in severe alopecia areata.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no Health Canada license record for this product; general glucocorticoid/anti-inflammatory use only known from pharmacological class) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for prednisone was not returned in this evidence pack (flagged as data gap DG002), and no original indication is on file because the product currently has no Canadian market authorization. Based on general pharmacological knowledge, prednisone is a synthetic glucocorticoid that suppresses immune-mediated and inflammatory processes — it inhibits pro-inflammatory cytokine transcription, reduces lymphocyte activation and proliferation, and dampens antigen-presenting cell activity. This broad immunosuppressive/anti-inflammatory action underlies its long-established use across autoimmune and inflammatory conditions generally.

Alopecia areata (AA) is a T-cell–mediated autoimmune attack on the hair follicle. Mechanistically, prednisone's suppression of peri-follicular lymphocytic infiltration and cytokine release is directly relevant to this pathophysiology, and systemic corticosteroids (alone or combined with methotrexate) have in fact been used clinically for severe AA for decades — the literature evidence below dates back to 1956.

Importantly, this means the TxGNN signal is less a "novel" repurposing discovery and more a **rediscovery/validation of established off-label practice**. Contemporary high-quality trial activity for AA has largely shifted toward newer biologics and JAK inhibitors (baricitinib, VIB7734, etc.), with prednisone appearing mainly as a comparator/background therapy rather than the primary investigational agent — an important nuance for prioritization.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | RCT: methotrexate alone vs. methotrexate + low-dose prednisone vs. placebo in severe AA (alopecia totalis/universalis/"grave pelade"). **Only trial directly testing prednisone in this indication.** |
| [NCT02141672](https://clinicaltrials.gov/study/NCT02141672) | Phase 2 | Completed | 265 | Voclosporin vs. placebo for remission in active lupus nephritis. Graded B — same broad autoimmune category, different drug; not prednisone-specific. |
| [NCT03021499](https://clinicaltrials.gov/study/NCT03021499) | Phase 3 | Completed | 358 | Voclosporin vs. placebo for renal response in lupus nephritis. Indirect autoimmune analog only. |
| [NCT03843125](https://clinicaltrials.gov/study/NCT03843125) | Phase 3 | Terminated | 1147 | Long-term safety/efficacy of baricitinib in SLE; study terminated early. Indirect analog. |
| [NCT04058028](https://clinicaltrials.gov/study/NCT04058028) | Phase 2 | Completed | 244 | Dose-ranging study of rozibafusp alfa in SLE with inadequate response to standard care. Indirect analog. |
| [NCT04925934](https://clinicaltrials.gov/study/NCT04925934) | Phase 2 | Completed | 214 | VIB7734 vs. placebo in moderate-to-severe SLE. Indirect analog, not prednisone. |
| [NCT03845517](https://clinicaltrials.gov/study/NCT03845517) | Phase 2 | Completed | 350 | PF-06700841 dose-ranging study in active SLE. Indirect analog. |
| [NCT02975336](https://clinicaltrials.gov/study/NCT02975336) | Phase 2 | Terminated | 469 | M2951 dose-ranging study in SLE; terminated. Indirect analog. |
| [NCT02437890](https://clinicaltrials.gov/study/NCT02437890) | Phase 2 | Completed | 312 | ALX-0061 (subcutaneous) dose-ranging study in SLE, includes a steroid-reduction endpoint. Indirect analog. |
| [NCT04835441](https://clinicaltrials.gov/study/NCT04835441) | Phase 2 | Completed | 76 | Acazicolcept (ALPN-101) vs. placebo in moderate-to-severe SLE. Indirect analog. |

**Note:** Of the 32 trials returned for this drug–disease query, only NCT02037191 tests prednisone directly in alopecia areata; the remaining B/C-graded trials were retrieved via broader autoimmune-disease association and test unrelated investigational drugs (largely for SLE/lupus nephritis, not AA itself).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | 2-step double-blind RCT: methotrexate alone vs. methotrexate + low-dose prednisone in alopecia totalis/universalis; combination improved hair regrowth over methotrexate alone. |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Archives of Dermatology | Comprehensive review of AA therapies (including corticosteroids); notes efficacy/safety data are difficult to compare across heterogeneous studies. |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Cohort | Archives of Dermatology | Immunologic studies in AA with prednisone treatment — early evidence supporting immune-mediated pathogenesis and steroid responsiveness. |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Case Series | Archives of Dermatology | Follow-up of 18 AA patients on alternate-day prednisone: initial response often not durable long-term; notable steroid-related side effects. |
| [911178](https://pubmed.ncbi.nlm.nih.gov/911178/) | 1977 | Case Series | Archives of Dermatology | Reports clinical outcomes of prednisone therapy for alopecia areata. |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort | Dermatology (Basel) | Methotrexate combined with low-to-moderate dose corticosteroids evaluated for efficacy/safety in severe AA. |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case Series | Clinical and Experimental Dermatology | 8-case series: baricitinib + low-dose corticosteroids produced major improvement in very severe AA (SALT ≥95) after baricitinib or methotrexate alone had failed. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case Series | Medical Times | Early historical report of AA (partialis/totalis) treated with cortisone, hydrocortisone, prednisone, and prednisolone. |
| [38650498](https://pubmed.ncbi.nlm.nih.gov/38650498/) | 2024 | Cohort | Italian Journal of Dermatology and Venereology | Real-world characterization of hospitalized AA patients in Italy — comorbidities, treatment patterns, economic burden. |
| [16019495](https://pubmed.ncbi.nlm.nih.gov/16019495/) | 2005 | Case Report | Leukemia & Lymphoma | Case of AA with multifocal bone involvement in a young adult, later diagnosed with Hodgkin's disease. |

---

## Canada Market Information

Prednisone currently holds **no marketing authorization (DIN) in Canada** for this product record — `taiwan_regulatory.total_licenses = 0` and the license list is empty. No product-level dosage form or approved-indication text is available from this data source.

---

## Other Candidate Indications From This Evidence Pack (Context)

TxGNN returned 10 alopecia/immune-related high-score predictions for prednisone. Beyond the primary candidate above, the table below summarizes the rest for transparency — most are assessed as low-confidence noise or already-established use, not new repurposing opportunities:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 2 | Alopecia mucinosa | 99.99% | L4 | Research Question | Follicular mucinosis can be idiopathic or malignancy-associated; malignancy must be excluded before considering steroids. |
| 3 | Telogen effluvium | 99.99% | L5 | Hold | Typically non-immune/reactive hair loss; mechanistic link to corticosteroids is weak — likely false positive. |
| 4 | Quinquaud's folliculitis decalvans | 99.99% | L5 | Hold | Primarily bacteria-driven scarring folliculitis; antibiotics are first-line, steroids only adjunctive. |
| 5 | Alopecia antibody deficiency | 99.99% | L5 | Hold | No direct evidence; only a broad "autoimmune comorbidity" inference. |
| 6 | Hereditary hypotrichosis with recurrent skin vesicles | 99.99% | L5 | Hold | Monogenic follicular development disorder; no plausible steroid target. |
| 7 | Alopecia-intellectual disability-hypogonadism syndrome | 99.99% | L5 | Hold | Rare genetic syndrome; no supporting evidence. |
| 8 | Atrichia with papular lesions | 99.95% | L5 | Hold | HR-gene structural defect (non-inflammatory); no supporting evidence. |
| 9 | Tenosynovitis | 99.80% | L2 | Proceed with Guardrails | Prednisone is already standard therapy for RA/PMR/ICI-induced inflammatory tenosynovitis — this reflects established practice, not a novel repurposing signal. |
| 10 | Prolapse of lacrimal gland | 99.66% | L5 | Hold | Anatomic/mechanical condition typically requiring surgery; no mechanistic or evidentiary support. |

**Interpretation:** Only ranks 1 and 9 clear the bar for "Proceed with Guardrails," and both represent confirmation of long-standing clinical practice rather than a new hypothesis. Ranks 2–8 and 10 should be treated as low-priority/likely knowledge-graph noise pending further evidence.

---

## Safety Considerations

Please refer to the package insert for safety information. (This evidence pack's key warnings, contraindications, and drug-interaction fields returned no usable data — the TFDA/Health Canada label review is flagged as a **Blocking** data gap (DG001) and must be resolved before any S1 safety screening.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT (NCT02037191) directly tested prednisone (combined with methotrexate) in severe alopecia areata, and this is corroborated by a multi-decade body of case series/cohort literature (1956–2024) showing biological plausibility and real-world use. However, this is best framed as validating existing off-label practice rather than a novel discovery, current standard-of-care trends favor newer JAK inhibitors/biologics, and this specific product record has no Canadian market authorization or safety-label data on file.

**To proceed, the following is needed:**
- TFDA/Health Canada product label — warnings and contraindications (currently a Blocking gap, DG001)
- Confirmed mechanism-of-action reference via DrugBank API (DG002)
- Clarification of the drug's original/approved indication (no license or indication text is currently on file for this Canadian market record)
- Drug interaction (DDI) screening — current query status is "not_found"
- Dermatology specialist input weighing prednisone against current first-line AA options (e.g., JAK inhibitors) given the evolving standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

