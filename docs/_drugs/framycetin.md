---
layout: default
title: Framycetin
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 7
---

# Framycetin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Framycetin: From an Antibacterial Aminoglycoside to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin is an aminoglycoside antibiotic marketed in Canada in several topical products (nasal spray, ointment, suppositories and combination-type preparations). The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but **no clinical trials and no publications** were found to support this prediction. The evidence is model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian licence data compiled for this report |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for framycetin. Based on known information, framycetin is an aminoglycoside antibiotic, a class that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit. It is poorly absorbed when taken orally, so any effect would stay mostly within the gut.

That property offers a speculative link to sclerosing cholangitis. Oral vancomycin is being explored in primary sclerosing cholangitis on the "gut-liver axis" idea, in which changes in intestinal flora may influence bile duct inflammation. A poorly absorbed antibiotic could act in a similar way.

This link rests only on the TxGNN prediction. The high score is not corroborated by any trial or publication. It should be treated as a hypothesis to test, not as supported efficacy.

**Other predictions in the list** (all L5, all Hold):

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Urinary tract infection | 99.42% | Biologically plausible class effect (other aminoglycosides are used), but poor systemic absorption means inadequate urinary levels |
| Congenital prothrombin deficiency | 99.41% | No plausible mechanism; likely a knowledge-graph artifact |
| Ureaplasma urethritis | 99.28% | Weak link; tetracyclines or macrolides are usual treatment |
| Gonococcal urethritis | 99.28% | Class-level rationale only; not a recognized treatment |
| Uterine inflammatory disease | 99.18% | Class-level rationale in polymicrobial infections; tissue levels doubtful |
| Xanthogranulomatous pyelonephritis | 99.18% | Renal tissue penetration implausible; nephrotoxicity is a class concern |

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
| 02224860 | SOFRAMYCIN NASAL SPRAY | Not listed | Not listed |
| 02224623 | SOFRACORT | Not listed | Not listed |
| 02247322 | PROCTOL OINTMENT | Not listed | Not listed |
| 02226383 | TEVA-PROCTOSONE | Not listed | Not listed |
| 02247882 | PROCTOL SUPPOSITORIES | Not listed | Not listed |

All five licences are valid and single-ingredient. The product names suggest nasal, ointment and suppository forms.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interactions were found in the data compiled for this report. As a class concern, aminoglycosides can be nephrotoxic and ototoxic, which matters if systemic exposure were increased.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (99.66%), with no clinical trials or publications. The mechanism is speculative, and the available Canadian products are topical forms that do not match the likely route needed for a biliary or gut-liver indication.

**To proceed, the following is needed:**
- Mechanism of action data and a review of the gut-liver axis rationale
- A literature search for aminoglycosides or gut-restricted antibiotics in sclerosing cholangitis
- Package insert warnings and contraindications from Health Canada, and the approved indications for each DIN
- Route and formulation compatibility assessment (current products are topical, not oral)
- Preclinical or pilot evidence before any clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

