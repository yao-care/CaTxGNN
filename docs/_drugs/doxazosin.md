---
layout: default
title: Doxazosin
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 2
---

# Doxazosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Doxazosin: From Hypertension to Migraine Disorder

## One-Sentence Summary

Doxazosin is a selective alpha-1 adrenergic receptor blocker commonly used to treat hypertension and benign prostatic hyperplasia (BPH). The TxGNN model predicts it may be effective for **Migraine Disorder**, though only **0 clinical trials** and **1 publication** currently support this direction. A closely related prediction — **Migraine with Brainstem Aura** — also emerged at nearly identical confidence (Rank 2, 99.19%), likely reflecting knowledge graph node adjacency rather than independent mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Benign Prostatic Hyperplasia (BPH) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacology, doxazosin is a selective **alpha-1 adrenergic receptor antagonist**: it blocks post-synaptic alpha-1 receptors in vascular smooth muscle, causing vasodilation and reducing peripheral resistance. Importantly, alpha-1 receptors are also expressed on **cerebral arterial smooth muscle**, which provides the theoretical basis for the TxGNN prediction — alpha-1 blockade could attenuate cerebrovascular constriction and theoretically modulate the vascular component of migraine attacks.

Migraine pathophysiology involves the **trigeminovascular system** and dynamic regulation of cerebrovascular tone. The rationale embedded in the evidence pack articulates this pathway: α1 receptor blockade → cerebral vasodilation → dampening of vasoconstrictive triggers in migraine. This mechanistic chain is biologically plausible at a conceptual level, and the single 1997 clinical observation (10 patients) noted improvement in 9 of 10 cases treated with alpha-1 blockers.

However, the overall mechanistic confidence is rated **Low**, and several counterarguments must be weighed. First-line migraine prophylactics are **beta-blockers (propranolol), CGRP antagonists, and anticonvulsants** — none of which act via alpha-1 blockade. Doxazosin's blood pressure–lowering effect may also trigger compensatory sympathetic rebound and reflex vasodilation, potentially worsening headache rather than alleviating it. The second-ranked prediction (migraine with brainstem aura) carries **Very Low** confidence and is assessed as a pure computational adjacency inference, with no independent mechanistic support specific to that subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Narrative Review / Commentary | *Headache* | Single-author report from a general neurology practice: 10 migraine patients treated with terazosin or doxazosin. Migraine frequency or severity decreased in 9 of 10 patients; however, 5 discontinued due to side effects. No serious adverse reactions reported. Study is uncontrolled, n=10, and nearly 30 years old — findings are hypothesis-generating only and require formal prospective validation. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire evidence base consists of a single 1997 narrative commentary (n=10, uncontrolled) and a TxGNN knowledge graph prediction. There are no registered clinical trials, no controlled studies, and the mechanistic link is assessed as weak-to-moderate at best. Additionally, doxazosin is not marketed in Canada, and critical safety data — including key warnings and contraindications — are currently unavailable.

**To proceed, the following is needed:**

- Retrieve the official product monograph or package insert (e.g., from Health Canada or a marketed jurisdiction) to establish key warnings, contraindications, and drug interaction profile
- Obtain full MOA data from DrugBank to formally characterise the mechanistic rationale and assess its applicability to migraine neurobiology
- Conduct a systematic literature search across MEDLINE, Embase, and Cochrane to identify any additional preclinical, observational, or open-label studies that may have emerged since 1997
- Evaluate whether a small, prospective proof-of-concept study is warranted given the safety/tolerability signals (50% discontinuation rate in the single available report)
- Clarify Canada regulatory pathway (Health Canada NDS/SNDS or Section 56 exemption) only if preclinical and safety evidence sufficiently strengthens the case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

