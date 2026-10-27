---
layout: default
title: Ceftolozane
parent: Model Prediction Only (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceftolozane: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "CEFTOLOZANE"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ceftolozane: From Urinary Tract Infection to Ureaplasma Urethritis
{: .text-alpha }

## One-Sentence Summary

Ceftolozane is a cephalosporin antibiotic originally used to treat urinary tract infection.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis** with a very high score, but **no clinical trials and no publications** currently support this prediction. The biological rationale is also weak, so this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (the Canadian licence record does not list approved indication text) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, ceftolozane is a beta-lactam cephalosporin that inhibits bacterial penicillin-binding proteins (PBPs). It is optimised for activity against *Pseudomonas aeruginosa* and Enterobacterales, which is why it is used for urinary tract infection.

For the top predicted indication, the mechanistic link is weak. *Ureaplasma* species have no cell wall, so beta-lactam antibiotics are expected to be intrinsically ineffective against them. The high TxGNN score most likely reflects the model grouping drugs by the shared category of urogenital infection, rather than a real biological effect.

Other predictions fit better. The best-supported one is **xanthogranulomatous pyelonephritis** (score 99.88%), a chronic renal infection often caused by Gram-negative bacteria such as *Proteus* and *E. coli*. It is closely related to the existing urinary infection use. However, definitive treatment is usually surgical, and the available literature is only an indirect general review.

Other notable predictions:
- **Gonococcal urethritis** (99.89%): some cephalosporins, such as ceftriaxone, work against *Neisseria gonorrhoeae*, so a class-level rationale exists. Ceftolozane itself has no clinical or literature data for this use.
- **Uterine inflammatory disease** (99.88%): pelvic infections are often polymicrobial, and ceftolozane/tazobactam has Gram-negative activity. The rationale is plausible but unsupported.
- **Urogenital tuberculosis** (99.50%): *M. tuberculosis* has a native beta-lactamase and low beta-lactam susceptibility, so this is unlikely.
- **Non-infectious conditions** (hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease): no antibacterial target exists, and these scores are likely artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top predicted indication, Ureaplasma urethritis, currently no related literature is available. The only publication found relates to the fourth-ranked prediction, xanthogranulomatous pyelonephritis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Review | Current Opinion in Infectious Diseases | Review of insights on complicated febrile urinary tract infections, including pyelonephritis and urosepsis. It is indirect evidence and does not study ceftolozane. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02446901 | ZERBAXA | Not listed | Not listed |

---

## Safety Considerations

**Drug Interactions**: 11 interactions were identified, all rated Moderate:
- Aminoglycosides: kanamycin, neomycin, streptomycin, amikacin (including liposomal), gentamicin
- Anticoagulants: warfarin, dicoumarol
- Others: chloramphenicol, ethinylestradiol, mycophenolic acid

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the model score (L5), with no trials or literature. The biology also argues against it, because *Ureaplasma* lacks a cell wall and beta-lactams are not expected to work. The same applies to most other high-scoring predictions. Xanthogranulomatous pyelonephritis is the only one worth keeping as a research question, and even there the evidence is indirect.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- In vitro susceptibility data for ceftolozane against the target organisms (*Ureaplasma*, *N. gonorrhoeae*, and uropathogens linked to xanthogranulomatous pyelonephritis)
- A focused literature search on ceftolozane/tazobactam in pyelonephritis and pelvic infection
- Approved indication text for the Canadian licence, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

