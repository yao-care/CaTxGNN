---
layout: default
title: Polymyxin B
parent: Moderate Evidence (L3-L4)
nav_order: 743
evidence_level: L4
indication_count: 3
---

# Polymyxin B
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Polymyxin B: From Topical Antibacterial Use to Bronchitis

## One-Sentence Summary

Polymyxin B is a polypeptide antibiotic. In Canada it is marketed mainly in topical antibiotic products (ointments, creams, eye drops, bandages), so its original use is inferred from product names, not from approved indication text.
The TxGNN model predicts it may be effective for **bronchitis**.
**No clinical trials** are registered for this indication, and the **14 publications** retrieved are mostly old case-level reports, bronchial provocation studies and animal models, so evidence for treating bronchitis is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical antibacterial use (inferred from product names; no approved indication text in the data) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, polymyxin B is a cationic lipopeptide that disrupts the outer membrane of gram-negative bacteria. A plausible link therefore exists for bacterial airway infections caused by *Pseudomonas aeruginosa* or multidrug-resistant gram-negative bacilli, especially by the inhaled or endobronchial route.

The original (topical antibacterial) and predicted (bronchitis) uses share only the antibacterial rationale. The best-fitting studies concern ventilator-associated tracheobronchitis and pneumonia caused by resistant gram-negative bacteria. These are a narrow subset and not typical bronchitis, which is mostly viral. Two older reports (1970 and 1974) describe endobronchial or aerosolised polymyxin B in chronic bronchitis and *Pseudomonas* tracheobronchitis, but without controlled data.

There is also a safety concern. Several reports show that inhaled polymyxin B can provoke bronchoconstriction, and it has been used as a bronchial challenge agent in asthma and chronic obstructive bronchitis. The high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No RCTs were found for this indication. The table lists the most relevant publications, with treatment-related studies first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Comparative study (labelled Review) | Infection | Compared polymyxin B with other antimicrobials for ventilator-associated pneumonia and tracheobronchitis caused by *P. aeruginosa* or *A. baumannii*; the abstract gives no results |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Cohort | Diagn Microbiol Infect Dis | 19 patients received inhaled polymyxin B for multidrug-resistant gram-negative respiratory infections (14 pneumonia, the rest tracheobronchitis); most pneumonia cases had previously failed intravenous therapy |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Experimental observation | Chest | Experimental observations of endobronchial polymyxin B in chronic bronchitis (no abstract available) |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Case report/series | J Kans Med Soc | Systemic gentamicin plus polymyxin B aerosol for *Pseudomonas* tracheobronchitis (no abstract available) |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Mechanistic/Safety | Lung | Bronchial reactivity to inhaled polymyxin B in asthma and chronic obstructive bronchitis |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Mechanistic/Safety | Orv Hetil | Polymyxin B sulfate used as a non-specific bronchial provocation agent in asthma and chronic bronchitis |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Safety report | Ann Intern Med | Reports the danger of polymyxin B inhalation |
| [7402949](https://pubmed.ncbi.nlm.nih.gov/7402949/) | 1980 | Mechanistic/Safety | Pneumonol Pol | Compared exercise-induced bronchospasm with histamine and polymyxin B provocation tests in asthma and chronic obstructive bronchitis |
| [8054833](https://pubmed.ncbi.nlm.nih.gov/8054833/) | 1994 | Preclinical | Clin Auton Res | Guinea-pig eosinophilic bronchitis model induced by intranasal polymyxin B; polymyxin B is the inducing agent, not the treatment |
| [28441858](https://pubmed.ncbi.nlm.nih.gov/28441858/) | 2017 | Preclinical | Zhonghua Yi Xue Za Zhi | Mouse eosinophilic bronchitis model induced by polymyxin B nasal drops; polymyxin B is the inducing agent, not the treatment |

---

## Canada Market Information

Dosage form and approved indication text are not available in the data. The product names point to topical products (ointment, cream, drops, bandages), and none of the listed products points to an inhaled or respiratory route.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02236954 | Band-Aid Brand Adhesive Bandages Plus Antibiotic | — | — |
| 02552418 | Soothe Antibiotic Drops | — | — |
| 02230844 | Polysporin Antibiotic Cream | — | — |
| 02230251 | Antibiotic Ointment USP | — | — |
| 02181908 | Polyderm Ointment USP | — | — |

---

## Safety Considerations

- **Respiratory safety signal (from literature)**: Inhaled polymyxin B has been reported to cause bronchoconstriction and is used as a bronchial challenge agent in asthma and chronic obstructive bronchitis (PMIDs 231152, 2984629, 4322737). This is a significant concern for any airway-delivered use.

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on the model score. There are no registered trials, and the literature consists of weak case-level evidence plus reports that inhaled polymyxin B can provoke bronchoconstriction. The antibacterial rationale applies only to bacterial infection with resistant gram-negative organisms, not to bronchitis in general.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications
- Controlled clinical data in a defined bacterial bronchitis or tracheobronchitis population
- An inhaled-route safety assessment, including bronchospasm risk and the availability of a suitable formulation (none of the listed Canadian products appears to be one)

**Note:** Among the other predictions for this drug, **conjunctivitis** (rank 3, TxGNN score 99.06%) has much stronger support: a Phase 4 and a Phase 3 trial plus several RCTs of polymyxin B/trimethoprim ophthalmic products. This is probably an established ophthalmic use and not true repurposing, and the evidence is for fixed-dose combinations. It may be a better candidate for further review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

