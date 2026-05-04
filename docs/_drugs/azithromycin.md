---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Azithromycin is a broad-spectrum macrolide antibiotic established for treating community-acquired pneumonia, pharyngitis, skin and soft tissue infections, and sexually transmitted infections.
The TxGNN model's top-ranked prediction points to **Polyclonal Hyperviscosity Syndrome**, however **no clinical trials** and **no publications** currently support this direction.
The prediction score is high (99.81%), but internal analysis indicates this most likely reflects knowledge-graph proximity artifacts rather than genuine biological plausibility — the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, skin, sexually transmitted infections) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, azithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, blocking translocation of peptidyl-tRNA and halting peptide chain elongation. Beyond its antibacterial properties, azithromycin is well recognised for broad immunomodulatory effects — downregulating NF-κB signalling, reducing pro-inflammatory cytokines (IL-6, TNF-α), inhibiting leukotriene synthesis, and suppressing neutrophil-driven tissue inflammation. These properties have supported its use in chronic airway diseases such as cystic fibrosis and bronchiectasis.

Polyclonal hyperviscosity syndrome is characterised by excessive polyclonal immunoglobulin production (IgG, IgA, and/or IgM), leading to elevated serum viscosity, sludging in the microvasculature, and end-organ ischaemia. The cornerstone of management is plasmapheresis to physically remove immunoglobulin from the circulation. There is no known mechanism by which azithromycin would suppress polyclonal immunoglobulin synthesis, reduce serum viscosity, or alter the underlying lymphoproliferative or inflammatory process driving this syndrome.

The high TxGNN prediction score (0.998) for this indication most likely reflects non-specific proximity between haematological disease nodes in the knowledge graph rather than a genuine mechanistic signal. This pattern — high model scores paired with a "Hold" / L5 outcome — is observed across multiple top-ranked predictions in this candidate set (Ranks 1–3, 5–6, 8), suggesting a systematic graph-topology clustering effect rather than biologically informative predictions for these indications specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are currently on record for Azithromycin in this dataset.

> **Important Note:** This likely reflects a data collection gap rather than true market absence. Azithromycin (e.g., Zithromax®) is a widely marketed antibiotic in Canada and globally. Regulatory status should be confirmed directly via the Health Canada Drug Product Database before drawing any conclusions about Canadian market availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no established biological connection between azithromycin's known mechanisms and the pathophysiology of polyclonal hyperviscosity syndrome; the L5 evidence level confirms that no supporting clinical or preclinical studies exist for this specific indication.

**To proceed, the following is needed:**

- **Resolve the Canada market data gap:** Confirm market status by querying the Health Canada Drug Product Database directly; the current "0 DINs" result is inconsistent with azithromycin's global availability and likely reflects a data extraction issue rather than genuine absence.
- **Identify a credible mechanistic hypothesis** linking azithromycin to immunoglobulin regulation or serum viscosity reduction before committing further research resources to this indication.
- **Audit the TxGNN model output for haematological node bias:** Ranks 1–3, 5–6, and 8 all share the same L5 / Hold status with no supporting evidence; this cluster pattern warrants a systematic review of whether haematological disease nodes are being systematically over-ranked due to graph connectivity rather than biological signal.
- **Redirect evaluation to higher-yield candidates:** **Rank 10 (Congenital Hematological Disorder / Sickle Cell Disease)** carries the strongest evidence in this set — Evidence Level L3, 4 clinical trials (including two Phase 1/2 trials of azithromycin specifically in sickle cell disease), and 2 publications including a Cochrane-type systematic review — and merits a dedicated repurposing report in its own right.

---

*This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

