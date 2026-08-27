---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Methylprednisolone
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

# Methylprednisolone: From Inflammatory/Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a synthetic glucocorticoid corticosteroid widely used to suppress inflammation and immune responses across a spectrum of autoimmune and inflammatory conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata**, with **1 directly relevant completed clinical trial** and **20 publications** — many specifically investigating methylprednisolone pulse therapy for this hair loss condition — currently supporting this direction.
Evidence level is classified as **L2**, reflecting a substantive body of prospective cohort and retrospective studies that stop short of a completed Phase 3 RCT.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory and autoimmune conditions (synthetic glucocorticoid corticosteroid) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed (0 DINs registered in this dataset) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alopecia areata (AA) is an autoimmune disease in which CD8+ T cells breach the immune privilege of the hair follicle, triggering an inflammatory cascade that arrests hair growth. Methylprednisolone is a potent synthetic glucocorticoid that acts by binding to the glucocorticoid receptor (GR), which translocates to the nucleus and suppresses NF-κB — a master regulator of pro-inflammatory gene expression. The net result is a marked reduction in T-cell infiltration around the hair follicle and partial restoration of follicular immune privilege.

High-dose "pulse" regimens of methylprednisolone are particularly relevant to this indication. When administered as a bolus (intravenous or oral mega-pulse), the drug achieves peak tissue concentrations sufficient to dampen JAK-STAT and IFN-γ signalling — the same intracellular pathway targeted by newer JAK inhibitors (baricitinib, ritlecitinib) that have received regulatory approval for AA. This mechanistic overlap with validated therapeutic targets provides a strong scientific rationale for the TxGNN prediction.

Corticosteroid pulse therapy for AA is an established, though under-formalised, clinical practice. Multiple prospective open-label studies, retrospective cohorts, and systematic reviews have evaluated both oral and intravenous methylprednisolone specifically in this disease. The primary evidence gap is the absence of a large, blinded Phase 3 RCT; head-to-head data against approved JAK inhibitors are also lacking.

---

## Clinical Trial Evidence

> **Note:** Of 18 clinical trials retrieved, only 1–2 directly investigated methylprednisolone in alopecia areata. The majority studied other agents (JAK inhibitors, biologics) in AA or SLE. High-relevance trials are listed first; lower-relevance trials are included to reflect the research landscape.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | **Directly relevant.** Oral mega-pulse methylprednisolone in severe, therapy-resistant AA (totalis, universalis, ophiasic subtypes). Used higher doses and more frequent pulses than earlier protocols to overcome known failure modes in severe disease. The sole core trial directly testing this drug-disease pair. |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared DERMOJET (needle-free device) vs standard syringe for intralesional corticosteroid injection in AA patients. Indirectly supports local steroid delivery in AA; specific corticosteroid agent not specified as methylprednisolone. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Completed | 296 | Observational safety and effectiveness study of tofacitinib (JAK inhibitor) in alopecia; a subset of participants received adjuvant prednisolone, illustrating real-world corticosteroid co-use patterns in this condition. |
| [NCT03252587](https://clinicaltrials.gov/study/NCT03252587) | Phase 2 | Completed | 363 | BMS-986165 (deucravacitinib) in systemic lupus erythematosus — context trial demonstrating active immunological drug development in immune-mediated alopecia-related conditions. |
| [NCT03843125](https://clinicaltrials.gov/study/NCT03843125) | Phase 3 | Terminated | 1,147 | Baricitinib long-term safety in SLE; terminated. Represents a JAK inhibitor mechanistically downstream of methylprednisolone's IFN-γ/JAK-STAT suppression, contextualising the competitive treatment landscape. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Prospective Open-Label Trial | Saudi Medical Journal | Oral mega-pulse methylprednisolone for severe therapy-resistant AA. Published results corresponding to NCT01167946; directly evaluates efficacy and safety of the specific drug in this indication. |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatologic Therapy | Methylprednisolone alone vs methylprednisolone + methotrexate in 26 patients with extensive AA; assessed whether combination therapy offers superior outcomes. |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Prospective Cohort | Indian J Dermatol Venereol Leprol | IV methylprednisolone pulse therapy in severe, extensive, therapy-resistant AA; evaluated as a systemic corticosteroid strategy where conventional therapy has failed. |
| [9777767](https://pubmed.ncbi.nlm.nih.gov/9777767/) | 1998 | Prospective Open-Label | J Am Acad Dermatology | Single IV methylprednisolone pulse in 45 patients with severe AA of <12 months' duration; one of the earliest systematic evaluations of this regimen. |
| [21592197](https://pubmed.ncbi.nlm.nih.gov/21592197/) | 2011 | Retrospective Cohort | The Journal of Dermatology | Prognostic factors for response to methylprednisolone pulse therapy in 70 AA patients; aimed at establishing proper treatment indications for this regimen. |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Retrospective Study | Open Access Macedonian J Med Sci | Methotrexate + mini-pulse methylprednisolone in severe AA totalis/universalis; Vietnamese cohort experience with combination protocol. |
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Cyclosporine with and without systemic corticosteroids in AA; synthesises the role of corticosteroid co-administration in combination protocols. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Narrative Review | Dermatology Practical & Conceptual | Comprehensive review of corticosteroid pulse therapy in AA: efficacy, relapse rates, side effects, and prognostic factors across different pulse regimens. |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Comparative Study | J Dermatological Treatment | Combination cyclosporine + methylprednisolone for chronic severe AA; addressed the high recurrence rates and toxicity seen with cyclosporine monotherapy alone. |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Retrospective Study | Indian Journal of Dermatology | Sex differences in AA response to steroid pulse therapy; retrospective analysis with literature review, relevant to patient stratification considerations. |

---

## Canada Market Information

No DIN records are registered for methylprednisolone in this dataset (market status: not marketed, 0 licences on file).

> **Important caveat:** Methylprednisolone is a long-established drug internationally (marketed as Medrol® tablets and Solu-Medrol® injection). The absence of DIN data in this evidence pack likely reflects a data collection gap rather than actual non-availability in Canada. Verification via Health Canada's Drug Product Database (https://health-canada.ca/dpd) is **strongly recommended** before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Methylprednisolone is a systemic corticosteroid; standard glucocorticoid safety considerations apply (HPA axis suppression, immunosuppression, metabolic effects, osteoporosis risk with prolonged use). Formal safety data were not retrievable from this evidence pack and must be obtained from the Health Canada product monograph or DrugBank (DB00959) prior to any clinical planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A converging body of evidence — including one completed Phase 4 trial directly testing methylprednisolone in severe therapy-resistant AA, alongside more than a dozen prospective/retrospective cohort studies and systematic reviews in the same indication — provides meaningful clinical support for this TxGNN prediction. The mechanistic rationale is strong (GR-mediated suppression of follicular T-cell infiltration, with functional overlap with the JAK-STAT pathway targeted by approved AA biologics). However, the absence of a Phase 3 blinded RCT, the unresolved Canada regulatory data gap, and the emergence of approved JAK inhibitors as the new standard of care all require a cautious, monitored approach before positioning methylprednisolone as a repurposing candidate for AA in the Canadian market.

**To proceed, the following is needed:**
- Confirm Health Canada DIN status for methylprednisolone products (Medrol®/Solu-Medrol®) via the Drug Product Database — the current "not marketed" flag is suspected to be a data gap
- Retrieve full mechanism of action (MOA) data from DrugBank (DB00959) to formalise the pharmacological rationale
- Obtain safety warnings, contraindications, and drug interaction data from the Health Canada product monograph
- Define the target patient population precisely: evidence is strongest for **severe/extensive AA** (totalis, universalis, ophiasic subtypes); evidence in mild/patchy AA is less compelling
- Assess positioning relative to approved JAK inhibitors (baricitinib FDA-approved 2022, ritlecitinib FDA-approved 2023) — methylprednisolone pulse may serve as a bridge therapy or option in patients who are ineligible for or unable to access JAK inhibitors
- Consider a prospective registry or comparative effectiveness study design given the existing evidence base and the ethical difficulty of placebo-controlled trials in a disease with available treatments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

