---
layout: default
title: Neratinib
parent: Model Prediction Only (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
---

# Neratinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Neratinib: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Neratinib is an irreversible pan-HER (EGFR/HER2/HER4) tyrosine kinase inhibitor, known clinically for use in HER2-positive breast cancer. The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (based on known drug classification; no formal indication record found in this evidence pack) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, Neratinib is an irreversible small-molecule inhibitor of the pan-HER family (EGFR/HER2/HER4) tyrosine kinases, and its efficacy in HER2-positive breast cancer (both early-stage extended adjuvant and metastatic settings) is well established.

The predicted new indication, PR-positive breast cancer, is defined by hormone-receptor status rather than HER2 status. TxGNN's high score reflects a knowledge-graph-level association between HER2/EGFR signaling and PR signaling across breast cancer molecular subtypes — these pathways are known to cross-talk biologically — but this is an indirect, graph-topology signal rather than evidence of clinical activity in a PR+, HER2-unselected population.

Critically, this dataset contains **no clinical trials, ICTRP records, or literature** specifically evaluating Neratinib in PR+ breast cancer. By contrast, a related but distinct prediction in the same evidence pack (rank 2, "normal breast-like subtype of breast carcinoma") is supported by a completed Phase 2 trial (NCT01670877) in HER2 non-amplified/HER2-mutant metastatic breast cancer — population overlap exists, but it does not directly validate the PR+ subgroup claim. The mechanistic rationale for PR+ breast cancer therefore remains plausible but unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Neratinib currently has no marketing authorizations on file (market status: Not Marketed; 0 licenses recorded).

---

## Cytotoxicity

Neratinib is an antineoplastic agent (targets breast cancer and other malignancies).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (irreversible pan-HER [EGFR/HER2/HER4] tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PR-positive breast cancer prediction rests solely on TxGNN's knowledge-graph score (L5) with zero supporting clinical trials or literature, and a Blocking-severity data gap (missing TFDA/label safety data) currently prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the official product label/warnings and contraindications data before any safety evaluation can begin
- Resolve DG002 (High): confirm mechanism of action via DrugBank or primary literature to validate the HER2/PR pathway rationale
- Generate or identify clinical/preclinical evidence specific to the PR+ (HER2-unselected) breast cancer subgroup, since the only related trial in this dataset (NCT01670877) targets a HER2 non-amplified/mutant population, not PR status specifically
- Re-run evidence collection (clinical trials, literature) periodically, as this candidate may mature from L5 if new studies emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

