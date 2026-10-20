---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 949
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "TRIMETHOPRIM"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Trimethoprim: From Urinary Tract Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial originally used for urinary tract infections, otitis media, pneumocystosis, shigellosis and bacterial conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (the Canadian licence records compiled for this report contain no indication text, so this comes from the drug's known indications) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge (not the data compiled for this report), trimethoprim is an antibacterial that inhibits bacterial dihydrofolate reductase. Its efficacy in bacterial infections, including conjunctivitis and blepharoconjunctivitis, is established, and it is used in ophthalmic solutions, typically combined with polymyxin B.

The prediction is plausible mainly because punctate epithelial keratoconjunctivitis is close to the ocular indications already linked to the drug. There is an important caveat: this condition is often viral or immune-mediated (for example adenoviral), so an antibacterial mechanism may not address the main cause. The score is high, but it is a model prediction with no supporting studies for this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For the closely related, already-established indication of conjunctivitis, the compiled literature includes the following. These do not support the predicted indication directly:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | Clinical comparative study | J Pediatr Ophthalmol Strabismus | Multicenter comparison of polymyxin B/trimethoprim and moxifloxacin ophthalmic solutions for speed of clinical efficacy in bacterial conjunctivitis |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Clinical evaluation | Am J Ophthalmol | Trimethoprim combined with sulfacetamide and polymyxin B, or with polymyxin B alone, evaluated for efficacy and safety in bacterial conjunctivitis or blepharitis |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Survey | Clin Ther | Survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution |
| [2418736](https://pubmed.ncbi.nlm.nih.gov/2418736/) | 1985 | Clinical study | Ann Ophthalmol | Trimethoprim-polymyxin B compared with a multi-agent combination in surface ocular bacterial infections |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | Controlling contagious bacterial conjunctivitis and limiting transmission |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | Etiology, clinical features and management of acute infectious conjunctivitis in children |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic review/Meta-analysis | J Pediatric Infect Dis Soc | Antibiotic treatments for neonatal chlamydial conjunctivitis; trimethoprim not specifically assessed |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02243116 | Trimethoprim Tablets | Not specified | Not specified |
| 02243117 | Trimethoprim Tablets | Not specified | Not specified |
| 02525917 | Sulfamethoxazole and Trimethoprim for Injection, USP | Not specified | Not specified |
| 00445266 | Sulfatrim Pediatric | Not specified | Not specified |
| 02239234 | Sandoz Polytrimethoprim | Not specified | Not specified |

Eight valid single-ingredient authorizations are listed in total; the five above are shown. None of the listed products is documented as an ophthalmic formulation in the compiled data.

## Safety Considerations

- **Contraindications and disease associations (from the knowledge graph, not label text):** inherited porphyria and other porphyrin metabolism disorders, kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, and folic acid deficiency anemia.
- **Drug Interactions:** 100 interactions were found. The **Major** ones are all potassium products: potassium citrate, potassium bicarbonate, potassium chloride and potassium gluconate (hyperkalaemia risk is the likely concern). **Moderate** interactions include metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid and sapropterin. Several others, such as pantoprazole, doxycycline, omeprazole and simvastatin, have an unclassified severity level.

Please refer to the package insert for warnings and label-based contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.57%), but this is a model prediction with no registered trials or publications for punctate epithelial keratoconjunctivitis (evidence level L5). The condition is frequently viral or immune-mediated, so an antibacterial agent may not address the main cause. The conjunctivitis literature supports the existing indication but does not extend to this one.

**To proceed, the following is needed:**
- Mechanism of action data, and a clear link between trimethoprim's antibacterial action and the causes of this condition
- Clinical or observational evidence specific to punctate epithelial keratoconjunctivitis, including the proportion of cases with a bacterial cause
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Confirmation of the available routes and formulations (especially ophthalmic) and the approved indication text for the Canadian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

