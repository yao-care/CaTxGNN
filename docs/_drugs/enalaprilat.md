---
layout: default
title: Enalaprilat
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 1
---

# Enalaprilat
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

The txgnn-pipeline skill covers technical pipeline work; this is a report generation task fully specified in my system prompt. Proceeding directly with the report.

---

# Enalaprilat: From Cardiovascular Treatment to Primary Hereditary Glaucoma

## One-Sentence Summary

Enalaprilat is the pharmacologically active metabolite of enalapril, an established ACE inhibitor used in the management of hypertension and heart failure.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with a very high model confidence score of **99.09%**.
However, this prediction is currently supported by **no clinical trials** and **no publications**, placing it at the lowest evidence tier and warranting a Hold decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication on file; active metabolite of enalapril (ACE inhibitor, used for hypertension / heart failure) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Enalaprilat is the biologically active form of enalapril, produced after first-pass hepatic conversion of the prodrug. As an ACE inhibitor, it blocks the angiotensin-converting enzyme, which prevents the formation of angiotensin II — a potent vasoconstrictor that also promotes aldosterone secretion and fluid retention. This mechanism underpins the well-established use of the enalapril/enalaprilat class in hypertension, left ventricular dysfunction, and chronic heart failure.

The theoretical link to glaucoma rests on the **ocular renin-angiotensin system (ocular RAS)**. The ciliary body, trabecular meshwork, and retinal vasculature all express local ACE and angiotensin II receptors. In principle, ACE inhibition within the eye could reduce aqueous humor production, thereby lowering intraocular pressure (IOP) — a central mechanism in glaucoma management. Some preclinical and epidemiological data on systemic ACE inhibitors suggest a modest IOP-lowering effect, which may underlie the TxGNN model's high topological score for this drug-disease pair.

However, the connection to **primary hereditary glaucoma** specifically is mechanistically fragile. This condition is driven primarily by genetic mutations — notably in *MYOC*, *CYP1B1*, and *OPTN* — that impair trabecular meshwork development and outflow facility through gene-level pathophysiology. Modulating the RAS does not address these upstream genetic defects. The high TxGNN score likely reflects knowledge-graph topology (shared disease neighbours in the KG) rather than a causal druggable link. Additionally, enalaprilat is administered intravenously in clinical settings, which raises a significant route-of-delivery barrier for chronic ocular use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Enalaprilat is not currently marketed in Canada (0 DINs on file). No local product label, warnings, contraindications, or drug interaction data were retrievable for this report.

> Please refer to the reference country package insert (e.g., US FDA label for enalaprilat injection) for safety information, particularly regarding hypotension, renal impairment, and angioedema risk — class effects common to all ACE inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5) with zero corroborating clinical or preclinical evidence linking enalaprilat to primary hereditary glaucoma. The mechanistic rationale relies on an indirect pathway (ocular RAS → IOP reduction) that does not address the genetic aetiology of the target disease, and the drug's intravenous-only route makes chronic ophthalmic use impractical without reformulation.

**To proceed, the following is needed:**

- **MOA confirmation:** Query DrugBank API for enalaprilat's full mechanism profile to assess any direct ocular pharmacology
- **Prodrug evidence sweep:** Search for clinical or preclinical data on oral **enalapril** (the prodrug) and IOP reduction — these would serve as proxies for the active metabolite's ocular potential
- **Ocular RAS literature review:** Conduct a targeted PubMed search for `ACE inhibitor AND intraocular pressure AND glaucoma` to assess class-level biological plausibility
- **Route feasibility assessment:** Evaluate whether a topical ophthalmic formulation of enalaprilat is pharmacokinetically viable (enalaprilat is highly hydrophilic; corneal penetration may be poor)
- **Genetic pathway analysis:** Determine whether the *MYOC* / *CYP1B1* / *OPTN* mutation pathways intersect with any downstream RAS-regulated targets that could justify revisiting this prediction
- **Regulatory pathway:** If evidence accumulates, a Health Canada pre-submission consultation would be required given the current non-marketed status in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

