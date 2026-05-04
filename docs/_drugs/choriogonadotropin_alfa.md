---
layout: default
title: Choriogonadotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Choriogonadotropin Alfa
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

# Choriogonadotropin Alfa: From Assisted Reproduction to Peptic Esophagitis

## One-Sentence Summary

Choriogonadotropin alfa (recombinant human chorionic gonadotropin, r-hCG) is a gonadotropin hormone historically used in assisted reproductive technology (ART) to trigger final follicular maturation and ovulation induction.
The TxGNN model predicts it may be effective for **Peptic Esophagitis**, with **0 clinical trials** and **0 publications** currently found to support this direction.
This is a purely model-driven signal with no corroborating empirical evidence at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Assisted reproduction (final follicular maturation, ovulation induction in ART) |
| Predicted New Indication | Peptic Esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Choriogonadotropin alfa is a recombinant form of human chorionic gonadotropin (hCG) that binds to the luteinizing hormone/choriogonadotropin receptor (LHCGR). LHCGR is predominantly expressed in gonadal tissues (ovarian granulosa cells, testicular Leydig cells), where hCG stimulates steroidogenesis and supports luteal function. Its canonical use is in fertility medicine — specifically to mimic the endogenous LH surge and trigger oocyte maturation in women undergoing ART.

The mechanistic link between Choriogonadotropin alfa and peptic esophagitis is extremely tenuous. LHCGR expression has not been reliably demonstrated in esophageal tissue. A speculative pathway — that systemic anti-inflammatory or immune-modulatory effects of hCG could promote mucosal repair — lacks any experimental basis. Peptic esophagitis results primarily from acid-peptic injury to the esophageal mucosa (often in the context of gastroesophageal reflux) and is managed with acid suppression; there is no established hormonal axis connecting gonadotropin signaling to this pathophysiology.

The TxGNN model's high prediction score most likely reflects co-morbidity network connections within the knowledge graph rather than a true biological mechanism. Multiple esophageal diseases (esophageal ulcer, esophageal disease, non-syndromic esophageal malformation) appear in the top-10 predictions, suggesting a structural clustering artifact in the graph rather than a drug-specific signal. Taken together, the biological plausibility of this repurposing direction is very low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero empirical evidence (clinical trials or published literature) supporting the use of Choriogonadotropin alfa in peptic esophagitis, the mechanistic link is biologically implausible based on current receptor-expression knowledge, and the drug is not approved or marketed in Canada for any indication. This candidate does not meet the threshold for further investment under current evidence.

**To proceed, the following would be needed:**

- **MOA clarification**: Retrieve complete DrugBank MOA data (DG002) to determine whether any secondary pharmacological effects of hCG could plausibly interact with esophageal pathophysiology.
- **Receptor expression data**: Evidence of LHCGR or related receptor expression in esophageal mucosa or immune cells relevant to reflux-induced inflammation.
- **Hypothesis generation**: Identify a credible biological pathway (e.g., hCG's known immunomodulatory properties in pregnancy) that could be experimentally tested in a mucosal injury model before any clinical consideration.
- **Safety package review**: Obtain the full prescribing information (product monograph) to characterize contraindications, hormonal adverse effects, and population-specific risks (DG001), particularly relevant given that exogenous gonadotropin use carries risks of ovarian hyperstimulation syndrome (OHSS) and thromboembolic events.
- **Re-evaluation of prediction rank**: Given that ranks 1, 3, 5, and 6 all relate to esophageal pathology, a knowledge-graph topology review is warranted to assess whether this cluster represents a real signal or a graph-structural false positive before any resources are committed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

