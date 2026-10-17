---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Azithromycin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Streptococcal infection, bacterial pneumonia…"
monitor_inn: "AZITHROMYCIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Azithromycin is a macrolide antibiotic originally used for bacterial infections such as streptococcal and staphylococcal infections, bacterial pneumonia, conjunctivitis and sexually transmitted infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, staphylococcal infection, conjunctivitis and others (from the knowledge graph; no approved indication text is available from Health Canada licences) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azithromycin is a macrolide antibacterial whose efficacy in bacterial infections is established. A mechanistic link to polyclonal hyperviscosity syndrome has not been established.

Polyclonal hyperviscosity syndrome is a condition in which excess immunoglobulins raise blood viscosity. The data compiled for this report show no plausible connection between azithromycin's antibacterial or immunomodulatory activity and this condition. The very high score (99.81%) is a model output and is not backed by any trial or publication.

**Other predictions reviewed (all on Hold unless noted):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Hyperamylasemia | 99.81% | L5 | A laboratory finding rather than a distinct disease; no evidence |
| 3 | Congenital analbuminemia | 99.79% | L5 | Rare genetic disorder; no mechanism evident |
| 4 | Punctate epithelial keratoconjunctivitis | 99.78% | L4 | Ocular use is plausible, but the only publication is a case report on microsporidial keratoconjunctivitis that shows no azithromycin efficacy |
| 7 | Monoclonal gammopathy | 99.61% | L4 | In vitro data show macrolides, including azithromycin, block autophagy flux and sensitize myeloma cells to bortezomib; this is not MGUS itself |
| 9 | Septicemic plague | 99.52% | L4 | One in vitro study found azithromycin had poor activity against *Yersinia pestis* strains |
| 10 | Congenital hematological disorder | 99.40% | L4 | Sickle cell disease context (acute chest syndrome, lung function); relevant trials were withdrawn; flagged as a research question |

## Clinical Trial Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), currently no related clinical trials are registered.

The most relevant trials found among the other predictions are for sickle cell disease (under "congenital hematological disorder"):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy to improve FEV1 in adults with sickle cell disease; no data because no participants enrolled |
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | Azithromycin prophylaxis for acute chest syndrome in sickle cell disease; no data because no participants enrolled |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | General pharmacokinetic and safety study of understudied drugs in children; not specific to this condition |

## Literature Evidence

For the top-ranked prediction, currently no related literature is available.

Selected publications from other predictions (the most mechanistically relevant):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Antibiotics for preventing lower respiratory tract infections in high-risk children; only indirectly relevant |
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | Preclinical | Int J Oncol | Macrolides, including azithromycin, block autophagy flux and enhance bortezomib cytotoxicity in myeloma cell lines |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro study | Antimicrob Agents Chemother | Azithromycin showed poor activity against *Yersinia pestis* strains |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Preclinical (animal) | Antibiot Khimioter | Azithromycin was the most active agent in experimental brucellosis |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case report | Cornea | Microsporidial keratoconjunctivitis diagnosis; no evidence of azithromycin efficacy |

## Canada Market Information

Azithromycin has 20 valid single-ingredient licences in Canada. Dosage form and approved indication text are not available in the data compiled for this report. Main authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02452308 | JAMP-AZITHROMYCIN | – | – |
| 02523825 | AZITHROMYCIN FOR INJECTION | Injection (from product name) | – |
| 02415542 | APO-AZITHROMYCIN Z | – | – |
| 02267845 | TEVA-AZITHROMYCIN | – | – |
| 02261642 | PMS-AZITHROMYCIN | – | – |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis (including adult-onset), neuromuscular junction disease, hearing disorder and auditory system disease.
- **Drug Interactions:** 100 interactions were found. Those listed here are the ones in the data reviewed:
  - **Major:** cisapride, dolasetron (both linked to QT prolongation risk).
  - **Moderate:** famotidine, loperamide, aluminium hydroxide, clarithromycin, levofloxacin, granisetron, balsalazide, several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose) and magnesium-containing antacids.
  - **Minor:** amoxicillin, metronidazole.

Package insert warnings and contraindications were not available. Please refer to the Health Canada package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests only on a model score (99.81%), with no clinical trials, no literature and no plausible mechanism (Evidence Level L5). Among the other predictions, sickle cell disease (acute chest syndrome) is the most clinically interesting research question, but both relevant trials were withdrawn with zero enrolment.

**To proceed, the following is needed:**
- Mechanism of action data for azithromycin, plus a biological rationale linking it to hyperviscosity or paraproteinaemia
- Any preclinical or clinical evidence for the predicted indication
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Dosage form and approved indication text for the Canadian licences
- If pursuing the sickle cell disease direction: a new, adequately enrolled trial with QT, hearing and liver safety monitoring
- Route-of-administration compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

