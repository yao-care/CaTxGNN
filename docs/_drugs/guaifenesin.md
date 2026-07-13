---
layout: default
title: Guaifenesin
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 5
---

# Guaifenesin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Guaifenesin: From Expectorant to Nasal Cavity Disease

## One-Sentence Summary

Guaifenesin is a well-established expectorant and mucolytic agent, used globally to relieve chest congestion by reducing mucus viscosity and facilitating airway clearance.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease** (including chronic rhinitis and sinusitis),
with **1 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Expectorant — relief of chest congestion and productive cough |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Guaifenesin acts as a mucoexpectorant by stimulating the secretory glands of the respiratory tract, increasing water content in mucus and reducing its viscosity and stickiness. This facilitates mucociliary clearance throughout the entire respiratory epithelium — the same continuous mucosal surface that lines the nasal cavity, sinuses, and lower airways.

The mechanism extends naturally to nasal cavity disease. Chronic rhinitis and sinusitis are characterised by thickened, poorly draining nasal secretions that perpetuate mucosal inflammation and obstruction. By reducing mucus viscosity and promoting nasal drainage, guaifenesin can theoretically relieve these upper respiratory symptoms — a direct extrapolation of its approved expectorant action from the lower airways upward. Biological plausibility is strong because the target tissue (mucus-secreting respiratory epithelium) and the mechanism of action (hydration and thinning of secretions) are identical regardless of anatomical location within the airway.

The existence of a completed Phase 2 randomised controlled trial specifically testing oral guaifenesin for paediatric chronic rhinitis (NCT01364467) validates this scientific rationale. That trial investigators chose guaifenesin for nasal disease confirms the mechanistic intuition behind the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | 14-day randomised, placebo-controlled, parallel-group pilot RCT in children aged 7–18 with chronic rhinosinusitis (CRS). Evaluated relief of nasal symptoms via the Sinonasal-5 (SN-5) survey, nasal airway volume, and biophysical properties of nasal secretions. Pilot scale only (n=30); a larger confirmatory RCT is required before drawing efficacy conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review / Case Series | American Journal of Rhinology | Case series of 22 adult cystic fibrosis patients with chronic sinusitis. Guaifenesin is included among the medical management strategies targeting mucociliary clearance in this population, reinforcing its role in upper airway secretion management. |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Expert Review | Logopedics, Phoniatrics, Vocology | Expert review of respiratory allergy management in vocal professionals. Notes that decongestants combined with guaifenesin may be preferable to antihistamines for managing upper respiratory allergy symptoms (including nasal involvement) in patients where mucosal dryness must be avoided. |

---

## Canada Market Information

Guaifenesin currently holds no Drug Identification Numbers (DINs) in Canada and is not listed as an approved prescription or OTC product in Health Canada's drug licensing registry. No Canadian approved indication text is available. Note that guaifenesin is approved as an expectorant in the United States (FDA-approved monograph ingredient) and numerous other jurisdictions, suggesting a regulatory gap specific to the Canadian market rather than a global absence of approved use.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 pilot RCT directly investigated oral guaifenesin for chronic rhinitis in children, establishing a clinical proof-of-concept at the Phase 2 level (L2 evidence). The mechanism of action is biologically coherent and represents a direct anatomical extension of the drug's established expectorant use. However, the pilot trial was small (n=30), full efficacy results require review, and guaifenesin holds no Canadian regulatory approval — a structured evidence-building programme is needed before any indication expansion.

**To proceed, the following is needed:**
- Full published results from NCT01364467 to evaluate effect size, confidence intervals, and safety profile in paediatric rhinitis
- A larger, adequately powered Phase 2/3 RCT in adult populations with nasal cavity disease to confirm findings across age groups
- Pharmacokinetic data confirming adequate guaifenesin concentration in nasal mucosa following standard oral dosing
- Complete mechanism of action (MOA) documentation from DrugBank to support a formal mechanistic rationale package
- Health Canada product monograph review for warnings, contraindications, and drug interaction data prior to any clinical programme initiation
- Regulatory pathway scoping with Health Canada (New Drug Submission or Supplemental NDS) for a nasal cavity disease indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

