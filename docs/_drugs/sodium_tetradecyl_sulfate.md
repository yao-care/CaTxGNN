---
layout: default
title: Sodium Tetradecyl Sulfate
parent: 僅模型預測 (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Sodium Tetradecyl Sulfate
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

# Sodium Tetradecyl Sulfate: From Varicose Vein Sclerotherapy to Esophageal Variceal Bleeding

## One-Sentence Summary

Sodium tetradecyl sulfate (STS) is a detergent-type sclerosing agent, traditionally used to treat varicose veins via endothelial injury and thrombosis induction. The TxGNN model predicts it may be effective for **Esophageal Varices with Bleeding**, with **1 clinical trial** and **20 publications** currently supporting this direction — including five randomized controlled trials dating back to the 1990s that already demonstrate real-world use of STS for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Sclerosing agent for varicose veins (based on established pharmacological knowledge; not confirmed via Canadian regulatory filing, as the drug is not currently marketed) |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, sodium tetradecyl sulfate is a detergent-type sclerosant. When injected intravenously, it disrupts the vascular endothelium, triggering thrombosis and subsequent fibrosis — this is the established mechanism behind its use in peripheral varicose vein sclerotherapy.

Esophageal and gastric varices are, mechanistically, the same underlying pathology — abnormally dilated, thin-walled veins prone to rupture — just occurring in the portal venous system rather than peripheral limbs. The same endothelial-injury/thrombosis/fibrosis mechanism that closes varicose veins is directly applicable to closing esophagogastric varices via endoscopic sclerotherapy or balloon-occluded retrograde transvenous obliteration (BRTO).

Notably, this is not a purely theoretical extrapolation: the literature evidence shows STS has already been used clinically for esophageal and gastric variceal bleeding since at least the 1980s–1990s, with several head-to-head RCTs against other sclerosants (polidocanol, ethanolamine oleate, sodium morrhuate) and more recent BRTO/foam-sclerotherapy studies. This strongly supports the plausibility of the TxGNN prediction — it correctly identified a real, long-standing off-label/regional clinical practice rather than a speculative association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | N/A | Unknown | 70 | Compares EUS-guided coil + cyanoacrylate injection versus BRTO for gastric variceal bleeding; BRTO commonly uses STS as the sclerosant, making this an indirect comparator-arm reference rather than a direct STS efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8886633](https://pubmed.ncbi.nlm.nih.gov/8886633/) | 1996 | RCT | Endoscopy | Prospective RCT comparing hypertonic glucose water vs. STS for acute gastric variceal bleeding in advanced cirrhosis |
| [1734694](https://pubmed.ncbi.nlm.nih.gov/1734694/) | 1992 | RCT | Am J Gastroenterol | RCT of STS vs. polidocanol as variceal sclerosants; comparable eradication rates (88% both arms) |
| [2279644](https://pubmed.ncbi.nlm.nih.gov/2279644/) | 1990 | RCT | Gastrointest Endosc | RCT of STS vs. sodium morrhuate for acute esophageal variceal bleeding; no significant mortality difference |
| [8287811](https://pubmed.ncbi.nlm.nih.gov/8287811/) | 1993 | RCT (Double-blind) | Endoscopy | Double-blind RCT comparing STS vs. ethanolamine oleate in 95 patients with bleeding esophageal varices |
| [30717949](https://pubmed.ncbi.nlm.nih.gov/30717949/) | 2019 | RCT | J Vasc Interv Radiol | Compares BRTO vs. endoscopic cyanoacrylate for gastric variceal bleeding, with extended follow-up on rebleeding/mortality |
| [30170340](https://pubmed.ncbi.nlm.nih.gov/30170340/) | 2019 | Review | J Gastroenterol Hepatol | Review of BRTO development, including transition from ethanolamine oleate to STS foam as sclerosant |
| [28180928](https://pubmed.ncbi.nlm.nih.gov/28180928/) | 2017 | Cohort | Cardiovasc Intervent Radiol | Safety/efficacy of STS + lipiodol foam in BRTO for large porto-systemic shunts and gastric fundal varices |
| [21353984](https://pubmed.ncbi.nlm.nih.gov/21353984/) | 2011 | Case Series | J Vasc Interv Radiol | Initial experience using STS foam as an alternative sclerosant to ethanolamine oleate in BRTO for bleeding gastric varices |
| [3443730](https://pubmed.ncbi.nlm.nih.gov/3443730/) | 1987 | Prospective Cohort | J Clin Gastroenterol | Prospective histopathologic study of esophageal effects of STS endoscopic variceal sclerotherapy |
| [9540875](https://pubmed.ncbi.nlm.nih.gov/9540875/) | 1998 | Cohort | Gastrointest Endosc | Comparison of cyanoacrylate vs. STS sclerotherapy for variceal bleeding in hepatocellular carcinoma patients |

---

## Canada Market Information

Sodium tetradecyl sulfate is **not currently marketed in Canada** — no Health Canada Drug Identification Numbers (DINs) are on file (0 licenses). Any repurposing pathway would require a new market authorization submission rather than a label-expansion of an existing product.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this Evidence Pack (Data Gap DG001, flagged as **Blocking** — required before proceeding to the S1 safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Five RCTs and multiple cohort studies spanning the 1990s to present already document real-world use of STS for esophageal/gastric variceal bleeding, and the mechanism is a direct, well-understood extension of its known sclerosant activity. However, the drug is not currently marketed in Canada, and mandatory safety documentation (label warnings/contraindications) is missing, which blocks formal safety sign-off.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph warnings and contraindications (DG001 — Blocking; required for S1 safety pre-assessment)
- Confirmed mechanism of action documentation (DG002)
- A Canadian market-entry pathway assessment, since the drug currently holds zero DINs
- Resolution of literature items still marked "pending" relevance/classification (e.g., PMIDs 8287811, 26757912, 19078888, and others) to finalize the evidence grade
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

