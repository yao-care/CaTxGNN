---
layout: default
title: Ceftolozane
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Ceftolozane
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

# Ceftolozane: From Complicated Gram-Negative Infections to Ureaplasma Urethritis

## One-Sentence Summary

Ceftolozane is a cephalosporin antibacterial, marketed in Canada as ZERBAXA, and the supplied record lists no approved indication text for it.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The mechanistic review finds the prediction biologically unsupported, so the high score is most likely a model artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license record (the rationale notes point to complicated Gram-negative infections, including complicated urinary tract infection) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. Ceftolozane is a cephalosporin, and cephalosporins inhibit penicillin-binding proteins and bacterial cell wall synthesis. Ceftolozane is paired with tazobactam and was developed for Gram-negative rods such as *Pseudomonas* and Enterobacterales.

On this evidence, the prediction is **not reasonable**. *Ureaplasma* species have no cell wall, so beta-lactam antibiotics are intrinsically inactive against them. The high TxGNN score (99.89%) most likely reflects graph propagation from the antibacterial drug class, not a real biological signal.

Other urogenital predictions from the same model were reviewed as well. Gonococcal urethritis is plausible only in general terms, and ceftriaxone already covers it. Uterine inflammatory disease is weak, because the infections are polymicrobial and involve atypical organisms and anaerobes that ceftolozane covers poorly. Urogenital tuberculosis is unlikely, because *M. tuberculosis* produces a beta-lactamase (BlaC) that breaks down most cephalosporins.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2446901 | ZERBAXA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trial or literature support (L5). It also conflicts with basic microbiology: *Ureaplasma* lacks a cell wall, so a cell-wall inhibitor is expected to be inactive.

**To proceed, the following is needed:**
- In vitro susceptibility data for ceftolozane against *Ureaplasma* species. Without this the prediction cannot advance.
- Health Canada package insert warnings, contraindications and approved indications, which are missing from the current record.
- Mechanism-of-action data from DrugBank.

**Related lead:** Among the other predictions, xanthogranulomatous pyelonephritis (score 99.88%) is rated L4 and "Research Question". It is a chronic kidney infection related to the on-label complicated urinary tract infection use. The only supporting paper is a general review of febrile urinary tract infection and pyelonephritis (PMID [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/), 2016), which offers only indirect support. This is a more sensible direction to explore than Ureaplasma urethritis, though surgery remains the main treatment.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

