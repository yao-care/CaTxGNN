---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ofloxacin: predicted new indication Septicemic plague . The rank 1 prediction is polyclonal hyperviscosit… (evidence level L5). Approved use: Typhoid fever, salmonellosis, urinary tract infection, br…"
monitor_inn: "OFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Septicemic Plague

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic originally used for infections such as typhoid fever, urinary tract infection, bronchitis, and bacterial pneumonia.
The TxGNN model's top-ranked predictions are mostly unrelated to infection, so this report focuses on the best-supported candidate, **Septicemic Plague**, which has **0 clinical trials** and **11 publications** (all preclinical or laboratory studies).
Among the top 10 predictions, only septicemic plague has a biologically coherent rationale and a meaningful body of supporting literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, urinary tract infection, bronchitis, bacterial pneumonia, and other bacterial infections (the Canadian licence record has no indication text) |
| Predicted New Indication | Septicemic plague (rank 8 of the top 10 predictions; selected as the most plausible). The rank 1 prediction is polyclonal hyperviscosity syndrome. |
| TxGNN Prediction Score | 99.79% (septicemic plague); 99.91% (rank 1, polyclonal hyperviscosity syndrome) |
| Evidence Level | L4 (preclinical studies only) for septicemic plague; L5 for the rank 1 prediction |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (research question only; not ready to proceed) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ofloxacin is a fluoroquinolone, a class known to inhibit bacterial DNA gyrase and topoisomerase IV, and its efficacy in a range of bacterial infections is established.

Plague is caused by *Yersinia pestis*, a Gram-negative bacterium that is susceptible to this mechanism. The extension from the original indications to plague is therefore a broadening of the antibacterial spectrum rather than a new mechanism. Laboratory studies show ofloxacin is highly active against *Y. pestis* isolates, and mouse studies show activity in experimental plague.

By contrast, most of the higher-scoring predictions (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, premalignant and congenital haematological disorders, and monoclonal gammopathy) have no identifiable link to an antibacterial mechanism. Their high scores reflect network-based model output only, with no supporting trials or literature. Hematological disease associated with acquired peripheral neuropathy is a particular concern, since fluoroquinolones can themselves cause peripheral neuropathy. Punctate epithelial keratoconjunctivitis has only a weak indirect link: ofloxacin is used in eye infections, but this condition is often viral or inflammatory, and the single retrieved paper is not an ofloxacin efficacy study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for septicemic plague or any of the other top 10 predicted indications.

---

## Literature Evidence

All studies below concern septicemic plague. No human trials were found. Types are limited to animal and in vitro work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal study | Antibiot Khimioter | Ofloxacin showed in vitro activity against *Y. pestis* (MIC 0.08 mg/L) and was tested for prophylaxis and treatment in mice. It was less effective against strains lacking fraction I and mouse toxin. |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal study | Antimicrob Agents Chemother | Mouse model of pneumonic plague used to compare antibiotics against streptomycin. |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Ofloxacin was active in vitro and was compared with beta-lactams, aminoglycosides, and doxycycline in a mouse model of systemic *Y. pestis* infection. |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Animal study | Antibiot Khimioter | Experimental bubonic plague model in baboons developed to evaluate antibacterials. |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal study | Antibiot Khimioter | Fluoroquinolones including ofloxacin reduced vaccine-induced immunity in mice, which matters for combined emergency prophylaxis and vaccination. |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Among 14 agents tested on 78 *Y. pestis* strains, ceftriaxone and ciprofloxacin were most active, followed by ofloxacin and ampicillin. |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Ofloxacin and levofloxacin were highly active against 100 human isolates (MIC90 below 0.03 µg/ml). |
| [18644132](https://pubmed.ncbi.nlm.nih.gov/18644132/) | 2008 | In vitro / molecular | BMC Microbiol | Screening for genes that may reduce antibiotic susceptibility in *Y. pestis*. |
| [13677133](https://pubmed.ncbi.nlm.nih.gov/13677133/) | 2003 | In vitro | Antibiot Khimioter | Formation of plague mutants resistant to rifampicin and quinolones. |

Two further retrieved papers (PMIDs 19121669 and 12180019) concern fluoroquinolone resistance in *Burkholderia pseudomallei*, and one (PMID 11057367) concerns *Vibrio cholerae*. They are off-target organisms and do not support the plague indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02143291 | OCUFLOX | Not specified | Not specified |

The product name suggests an ophthalmic formulation. This has not been confirmed, and the available data do not specify a dosage form or route. Whether it can be used for systemic infections such as plague is therefore unknown.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are database associations, not label text):
- Cardiac: long QT syndrome (including familial), torsades de pointes
- Neurological and neuromuscular: epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, peripheral neuropathy, peripheral nervous system disease
- Tendon and musculoskeletal: tendinitis, periarthritis, rhabdomyolysis
- Hepatic and renal: liver failure, liver disease, drug-induced liver injury, kidney disease, impaired renal function
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Haematological: thrombocytopenia, leukopenia, anaemia
- Gastrointestinal: *Clostridium difficile* colitis

**Drug Interactions:** 100 interactions were identified in total. Interactions rated Major among those listed include:
- Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone
- Bupropion
- Chlorpropamide

Moderate interactions include:
- Antidiabetic agents (acarbose, alogliptin, metformin, pioglitazone, canagliflozin, albiglutide)
- Famotidine
- Loperamide
- Aspirin
- Balsalazide
- Bisacodyl
- Calcium and potassium salts (calcium phosphate, calcium acetate, potassium citrate)

Blood glucose monitoring is relevant with antidiabetic agents. Combining with corticosteroids is relevant to the tendon-related signals above.

Please refer to the package insert for label warnings and contraindications. Those were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring predictions are unsupported by any trial or literature and have no plausible mechanism, so they should not be pursued. Septicemic plague is biologically coherent and has consistent in vitro and animal data (L4), but there are no human trials. It also falls within ofloxacin's existing antibacterial spectrum, and the only Canadian licence in the data appears to be an ophthalmic product. This makes it a research question rather than a candidate ready to advance.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the dosage form and route for the Canadian licence, and whether a systemic formulation is available
- Comparison with current plague guidelines, in which other fluoroquinolones and agents are already established, and any human clinical data
- Review of the QT, tendon, neuropathy, and drug interaction signals for the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

