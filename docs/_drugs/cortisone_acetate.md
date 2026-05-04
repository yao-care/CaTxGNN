---
layout: default
title: Cortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Cortisone Acetate
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

# Cortisone Acetate: From Adrenocortical Insufficiency to Alopecia Areata

## One-Sentence Summary

Cortisone acetate is a synthetic glucocorticoid historically used for adrenocortical insufficiency and inflammatory conditions, though no Health Canada–approved products are currently on record.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **0 clinical trials** and **20 publications** currently supporting this direction — though the vast majority of the literature dates from the 1950s.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Health Canada–registered products on record) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Alopecia areata (AA) is an autoimmune condition in which CD8+ T cells breach the immune-privilege environment of hair follicles, causing non-scarring hair loss. Glucocorticoids act through the glucocorticoid receptor (GR) to suppress the NF-κB and AP-1 signalling pathways, reducing pro-inflammatory cytokines including IL-2 and IFN-γ. This dampens T cell activation and proliferation, theoretically relieving the perifolicular immune infiltration that characterises AA — a mechanistically plausible connection between the drug class and the disease.

Although detailed mechanism of action data for cortisone acetate (DB01380) is not available in the current dataset, its pharmacological class is well established. As a synthetic glucocorticoid with a relative anti-inflammatory potency of approximately 1, cortisone acetate is among the earliest corticosteroids used in clinical medicine. It is a cortisol prodrug requiring hepatic conversion to become pharmacologically active. This class-level evidence forms the biological rationale behind the TxGNN prediction, and early clinical case series from the 1950s do document hair regrowth in AA patients treated with systemic cortisone.

The key limitation, however, is clinical positioning. Current standard of care for AA relies on far more potent corticosteroids — intralesional triamcinolone acetonide for localised patches, and systemic prednisone or prednisolone for extensive disease. JAK inhibitors (baricitinib, ritlecitinib) have also recently received regulatory approval for severe AA. Cortisone acetate's lower potency relative to these established options, combined with its systemic side effect profile and absence from the Canadian market, significantly narrows any viable clinical development path without a compelling differentiating rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39345662](https://pubmed.ncbi.nlm.nih.gov/39345662/) | 2024 | Case Report | Case Reports in Endocrinology | A patient with refractory myasthenia gravis and concurrent AA postthymectomy showed improvement following a cortisone taper, supporting the shared autoimmune basis between the two conditions |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Comparative Case Series | Medical Times | Compared cortisone, hydrocortisone, prednisone, and prednisolone across AA subtypes; provided early comparative evidence within the corticosteroid class |
| [13460157](https://pubmed.ncbi.nlm.nih.gov/13460157/) | 1957 | Retrospective Case Series | British Journal of Clinical Practice | Retrospective observations on cortisone use in AA and alopecia totalis; documented clinical response patterns |
| [13271835](https://pubmed.ncbi.nlm.nih.gov/13271835/) | 1955 | Case Series | Journal of Investigative Dermatology | Documented the effect of cortisone in AA with clinical observations on hair regrowth patterns |
| [14908175](https://pubmed.ncbi.nlm.nih.gov/14908175/) | 1952 | Case Series | Journal of Investigative Dermatology | Treatment of AA totalis and universalis specifically with cortisone acetate; reported partial hair regrowth in some patients |
| [12980788](https://pubmed.ncbi.nlm.nih.gov/12980788/) | 1952 | Observational / Case Series | JAMA | Therapeutic experiments with orally administered cortisone in AA; mixed efficacy results noted across cases |
| [14927344](https://pubmed.ncbi.nlm.nih.gov/14927344/) | 1952 | Case Series | JAMA | Cortisone and ACTH in AA and alopecia totalis; among the earliest published evidence of glucocorticoid response in AA |
| [13554262](https://pubmed.ncbi.nlm.nih.gov/13554262/) | 1958 | Case Series | Problemy Endokrinologii | Treatment of alopecia totalis and AA with ACTH and cortisone; documented outcomes in a Soviet patient cohort |
| [14952032](https://pubmed.ncbi.nlm.nih.gov/14952032/) | 1952 | Case Report | AMA Archives of Dermatology | AA universalis treated with ACTH and cortisone acetate intramuscularly; post-treatment observations including relapse patterns documented |
| [13012012](https://pubmed.ncbi.nlm.nih.gov/13012012/) | 1953 | Review / Clinical Summary | Lancet | Early clinical review of AA including cortisone as an emerging therapeutic option at the time |

---

## Canada Market Information

Cortisone acetate has no Drug Identification Numbers (DINs) on record with Health Canada. The drug is not currently marketed in Canada, and no approved product monographs or licensed indications are available through the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (key warnings, contraindications, drug-drug interactions) was not retrievable from the current data sources. As a systemic glucocorticoid, prescribers should be aware of class-level risks including HPA-axis suppression, adrenal insufficiency on abrupt withdrawal, immunosuppression, and metabolic effects. Full safety assessment requires consultation of the product monograph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting evidence consists exclusively of small uncontrolled case series from the 1950s, with a single 2024 case report — none of which constitute controlled clinical trial data. More potent corticosteroids and JAK inhibitors are already established as the standard of care for alopecia areata, and cortisone acetate is absent from the Canadian market entirely, making any near-term clinical development pathway difficult to justify without a clear differentiation strategy.

**To proceed, the following is needed:**
- Modern randomised controlled trial data comparing cortisone acetate to current standard-of-care agents (intralesional triamcinolone, systemic prednisolone, JAK inhibitors)
- Mechanism of action data from DrugBank confirming GR-mediated activity and pharmacokinetic profile relative to currently preferred corticosteroids
- Full safety monograph data including contraindications, key warnings, and drug-drug interaction profile
- Benefit-risk reassessment in the context of approved JAK inhibitor therapies (baricitinib, ritlecitinib) for severe AA
- Health Canada regulatory pathway assessment for new DIN registration, including any bridging data requirements
- Identification of a specific patient subpopulation where cortisone acetate may offer a meaningful advantage over existing treatments (e.g., cost, tolerability, route of administration)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

