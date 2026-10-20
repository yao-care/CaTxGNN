---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Norfloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections"
monitor_inn: "NORFLOXACIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic originally used for bacterial infections such as urinary tract infection, typhoid fever, dysentery and bacterial pneumonia.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, typhoid and paratyphoid fever, salmonellosis, dysentery, bronchitis, bacterial pneumonia and others, based on the knowledge graph; no approved indication text is available for the Canadian licence) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, norfloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy is established in bacterial infections, mainly of the urinary and gastrointestinal tracts.

Hyperamylasemia is a laboratory finding (elevated serum amylase), not an infectious process. No plausible mechanistic link to norfloxacin's antibacterial action was identified. The high score (rank 6285 among model predictions) appears to be a network-based artifact without biological support.

Other top-ranked predictions show the same pattern. Polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant haematological disease and diffuse scleroderma have no mechanistic rationale and no evidence. The only biologically plausible candidate is **septicemic plague**, caused by the fluoroquinolone-susceptible *Yersinia pestis*. Its supporting literature is limited to two preclinical papers, and other fluoroquinolones have stronger data. Norfloxacin's limited systemic exposure also makes it a poor choice for septicemia.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For reference, the literature retrieved for other lower-ranked predictions is not supporting evidence for the lead indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Preclinical | Antibiotiki i Khimioterapiia | Mouse study of combined fluoroquinolone and vaccine prevention of plague. Norfloxacin's effect on post-vaccine immunity was lower than that of ciprofloxacin, ofloxacin and pefloxacin. |
| [11057367](https://pubmed.ncbi.nlm.nih.gov/11057367/) | 2000 | Preclinical | Antibiotiki i Khimioterapiia | Experimental resistance of *Vibrio cholerae* to nalidixic acid and fluoroquinolones (cholera, not plague). |
| [8834911](https://pubmed.ncbi.nlm.nih.gov/8834911/) | 1996 | Cohort | Antimicrob Agents Chemother | Fluoroquinolone-resistant *E. coli* emerged in 40% of 25 haematological cancer patients on norfloxacin prophylaxis (resistance surveillance). |
| [22959880](https://pubmed.ncbi.nlm.nih.gov/22959880/) | 2012 | Case series | Am J Ophthalmol | Repeated corneal swabbing for microsporidial keratoconjunctivitis; norfloxacin efficacy not shown. |
| [12867402](https://pubmed.ncbi.nlm.nih.gov/12867402/) | 2003 | Case series | Ophthalmology | Six cases of microsporidial keratoconjunctivitis in healthy individuals; norfloxacin efficacy not shown. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02229524 | NORFLOXACIN | Not specified | Not specified |

## Safety Considerations

**Contraindication signals from the knowledge graph** (not label text) include:
- **Cardiac:** long QT syndrome (including familial), torsades de pointes
- **Nervous system and psychiatric:** epilepsy, peripheral neuropathy, anxiety and other mental disorders (psychotic, schizoaffective)
- **Liver and kidney:** liver failure, liver disease, cirrhosis, kidney disease
- **Musculoskeletal:** tendinitis, rhabdomyolysis
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- **Blood:** thrombocytopenia, anaemia

**Drug interactions:** 100 interactions were found. Major-level examples include:
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)
- Bupropion
- Chlorpropamide

Moderate-level examples include:
- Antidiabetic drugs (metformin, pioglitazone, acarbose, canagliflozin)
- Famotidine
- Loperamide
- Aspirin
- Calcium and potassium salts

Fluoroquinolones also carry connective tissue (tendon) and peripheral neuropathy warnings, which weigh against use in indications such as diffuse scleroderma and neuropathy-associated disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication, hyperamylasemia, has a high model score but no clinical trials, no literature and no plausible mechanism. It is a laboratory finding rather than a treatable infection. The evidence level is L5. The knowledge graph also lists many safety signals for norfloxacin.

**To proceed, the following is needed:**
- The Canadian package insert (warnings, contraindications and approved indications), which is currently missing and blocks safety screening
- Mechanism of action data
- A clear biological rationale for hyperamylasemia, or redirection of the evaluation to the more plausible candidate (septicemic plague), where norfloxacin would need to be compared with better-supported fluoroquinolones
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

