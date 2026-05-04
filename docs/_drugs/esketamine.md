---
layout: default
title: Esketamine
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 2
---

# Esketamine
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

# Esketamine: From Treatment-Resistant Depression to Agoraphobia

## One-Sentence Summary

Esketamine is the S-enantiomer of ketamine, an NMDA receptor antagonist approved globally (as Spravato) for treatment-resistant depression and major depressive disorder with acute suicidal ideation, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Agoraphobia**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Treatment-resistant depression (global approval; not currently marketed in Canada) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Esketamine is the S-enantiomer of ketamine and acts as an NMDA (N-methyl-D-aspartate) receptor antagonist. Marketed as Spravato (intranasal spray), it has demonstrated rapid antidepressant effects in treatment-resistant depression — an established clinical profile that forms the starting point for exploring anxiety-related indications.

The neurobiological rationale connecting Esketamine to agoraphobia centres on the role of NMDA receptors in fear memory. NMDA receptor activity is critical to both fear conditioning (how fears are learned) and fear extinction (how fears are unlearned). Agoraphobia engages the amygdala–prefrontal cortex–hippocampal neural circuit, and NMDA receptor antagonism may theoretically disrupt pathological fear conditioning while facilitating extinction learning. Additionally, depression and agoraphobia are highly comorbid conditions, meaning Esketamine's established rapid antidepressant mechanism provides indirect biological plausibility for symptom overlap.

That said, this mechanistic link remains inferential. No clinical studies have examined Esketamine specifically for agoraphobia, and the connection to fear circuit modulation is a hypothesis that has not been tested in this population. The TxGNN model score reflects structural and pathway-level similarity, not demonstrated efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33424664](https://pubmed.ncbi.nlm.nih.gov/33424664/) | 2020 | Narrative Review | Frontiers in Psychiatry | Comprehensive review of current and emerging pharmacotherapy for anxiety disorders (panic disorder, GAD, social anxiety disorder); discusses both approved agents and off-label options, noting a relative dearth of novel medications under investigation — Esketamine/NMDA antagonists are not specifically studied for agoraphobia within this review |

---

## Canada Market Information

Esketamine currently holds no Drug Identification Numbers (DINs) in Canada. The drug is not approved or marketed in this jurisdiction, and no license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Two data gaps are outstanding that block a complete safety evaluation:
> - **DG001 (Blocking):** Package insert warnings and contraindications have not been retrieved. This prevents a standard safety screening.
> - **DG002 (High):** Formal mechanism of action documentation is unavailable, which limits mechanistic risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic hypothesis linking Esketamine's NMDA receptor antagonism to agoraphobia's fear-circuit pathology is biologically coherent, the evidence base consists of a single narrative review with no direct agoraphobia data and zero registered clinical trials. Combined with significant data gaps in safety documentation and MOA data, this candidate does not currently meet the threshold for active development investment.

**To proceed, the following is needed:**

- Retrieve the full package insert (warnings, contraindications, and special population data) from Health Canada to unblock the S1 safety screen (resolves DG001)
- Query DrugBank API for formal MOA documentation to enable mechanistic linkage scoring (resolves DG002)
- Conduct a targeted literature search for preclinical studies on NMDA antagonists in fear extinction or anxiety disorder models to establish L3/L2 evidence
- Assess route-of-administration compatibility: intranasal delivery (the approved route for Spravato) may not align with standard agoraphobia treatment pathways
- Evaluate the safety implications of using a dissociative anesthetic-class agent in an outpatient anxiety population, particularly regarding abuse potential and REMS requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

