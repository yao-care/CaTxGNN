---
layout: default
title: Tranexamic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 790
evidence_level: L4
indication_count: 1
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Tranexamic Acid: From Antifibrinolytic Therapy to Amenorrhea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic agent; detailed original-indication and regulatory data are not available in the current evidence pack, and the drug is not currently marketed in Canada. The TxGNN model predicts possible relevance to **Amenorrhea**, but this direction is supported only by **2 review-level publications** and **no clinical trials**, and the mechanistic review embedded in this evidence pack flags the prediction as likely implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack (no regulatory license or indication text on file) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A structured mechanism/original-indication field is not available for this drug (blocking data gap). However, the evidence pack's mechanistic review confirms tranexamic acid's well-established pharmacology: it is an **antifibrinolytic** that competitively blocks the lysine-binding sites on plasminogen, preventing its conversion to plasmin and thereby reducing fibrin degradation. Clinically, this mechanism is used to **reduce bleeding** — e.g., in heavy menstrual bleeding (menorrhagia), surgical bleeding, and hereditary angioedema.

This mechanism points in the *opposite* pharmacological direction from the predicted indication. Amenorrhea is the absence of menstrual bleeding, whereas tranexamic acid's known clinical use is to control excessive bleeding. The two supporting literature items found also discuss tranexamic acid in the context of **menstrual suppression protocols in bleeding-risk patients** (e.g., hematologic cancer patients on cytotoxic therapy) and **abnormal uterine bleeding management** — i.e., tranexamic acid as an adjunct hemostatic agent, not as a treatment for absent menstruation.

The most likely explanation is that this is a **knowledge-graph embedding artifact**: "amenorrhea" and "menorrhagia/abnormal uterine bleeding" occupy adjacent regions of the disease embedding space (both are menstrual-cycle-related conditions), and the model may have confused these clinically opposite states. Mechanistic relevance to the predicted indication is therefore assessed as **low**.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Reviews pharmacological therapies for **abnormal uterine bleeding** (excess bleeding), not amenorrhea; tranexamic acid discussed as a nonhormonal option to reduce bleeding volume. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | Journal of Oncology Pharmacy Practice | Systematic approach to **menses prophylaxis and suppression** in pre-menopausal hematologic cancer patients; tranexamic acid used as adjunct for bleeding control in cytopenic patients, not as a primary amenorrhea-inducing or amenorrhea-treating agent. |

Both articles are reviews (Tier 2) discussing tranexamic acid's established use in bleeding management, not direct evidence for an amenorrhea indication.

## Canada Market Information

Tranexamic acid currently holds no active Canadian market authorizations (DINs) on file — market status is **Not Marketed**, with 0 licenses recorded in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The known antifibrinolytic mechanism of tranexamic acid runs counter to the predicted "amenorrhea" indication, the supporting literature discusses the opposite clinical problem (bleeding, not absent bleeding), and there are no clinical trials — evidence level is L4 with a plausible knowledge-graph mismatch. Blocking safety data gaps (regulatory warnings/contraindications) further preclude any progression.

**To proceed, the following is needed:**
- TFDA/Health Canada label data — key warnings and contraindications (currently a blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Independent verification that this is not a disease-direction inversion error in the TxGNN embedding (i.e., re-check whether the intended prediction target was menorrhagia/abnormal uterine bleeding rather than amenorrhea)
- Any primary clinical or case-level evidence directly addressing amenorrhea, if this direction is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

