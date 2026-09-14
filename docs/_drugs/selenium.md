---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 707
evidence_level: L5
indication_count: 1
---

# Selenium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Selenium: From No Documented Indication to Sclerosing Cholangitis

## One-Sentence Summary

> Selenium (DrugBank ID DB11135) currently has no documented approved indication in this evidence pack; it is used generally as an essential trace element with antioxidant (glutathione peroxidase cofactor) activity.
> The TxGNN model predicts it may be relevant to **Sclerosing Cholangitis**, with a prediction score of **99.04%**,
> though supported so far only by **0 clinical trials** and **5 publications** (mostly observational/mechanistic, not interventional).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no approved indication on file; selenium is used generally as a trace-element/nutritional supplement) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.04% (raw rank #15,719 among candidates — high score but low relative rank) |
| Evidence Level | L3 (observational studies) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`[Data Gap]`). Based on known information, selenium is an essential trace element and a key cofactor of glutathione peroxidase and other antioxidant selenoproteins; its physiological role is broadly antioxidant and hepatoprotective rather than tied to a specific approved disease indication.

There is no documented "original indication" for selenium in this evidence pack, so the usual original-vs-new indication comparison is not applicable here. Instead, the biological rationale for this prediction rests on observed alterations in trace-element metabolism in patients with primary sclerosing cholangitis (PSC): a case-control study (PMID 9053974) found abnormal hepatic retention of copper **and selenium** in PSC patients, and a more recent dietary study (PMID 39601354) found that individuals with PSC have poor intake of fat-soluble vitamins and, by extension, other micronutrients. This supports a plausible — but not yet clinically tested — hypothesis that selenium status is disturbed in PSC and could be a target for supplementation or monitoring, rather than evidence that selenium is an effective treatment.

Given the absence of MOA data, no clinical trials, and a comparatively low TxGNN rank despite a high raw score, this prediction should be interpreted as an early, exploratory signal rather than a validated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Observational (case series, n=32) | Scandinavian Journal of Gastroenterology | Found abnormal hepatic retention of copper and selenium in patients with primary sclerosing cholangitis, suggesting disturbed trace-element metabolism in PSC |
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Observational (dietary survey) | Liver International | PSC patients showed poor fat-soluble vitamin intake and overall lower dietary quality versus Nordic nutrition recommendations, indicating micronutrient deficiency risk |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | Preclinical (murine model) | Proteomics | Characterized hepatic proteome changes in murine models of toxin-induced fibrosis and sclerosing cholangitis, providing mechanistic context for liver injury pathways |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Case report | JPEN Journal of Parenteral and Enteral Nutrition | Describes a patient with overlapping PSC and ulcerative colitis on parenteral nutrition, discussing oxidative stress and antioxidant depletion in cholestatic liver disease |

---

## Canada Market Information

Selenium (DB11135) currently has no authorized drug products on file with Health Canada under this evidence pack — market status is **Not Marketed** with **0 DINs** recorded. No licensed product information is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data are currently available for this candidate, and TFDA/Health Canada label warnings are flagged as a **Blocking** data gap (DG001) that must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to small observational and preclinical studies with no interventional trials, mechanism-of-action data is absent, safety labeling is a blocking data gap, and the drug is not marketed in Canada — together these are insufficient to support advancing this candidate.

**To proceed, the following is needed:**
- Resolve blocking gap DG001: obtain official product labeling (warnings/contraindications) from a regulatory source
- Resolve gap DG002: obtain confirmed mechanism of action data from DrugBank or another primary source
- Identify or commission interventional studies testing selenium supplementation specifically in sclerosing cholangitis (not just observational trace-element correlation)
- Clarify regulatory pathway and market feasibility in Canada given zero current DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

