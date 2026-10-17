---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Moxifloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Streptococcal infection, bacterial pneumonia, peritonitis…"
monitor_inn: "MOXIFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections (Streptococcal Infection, Pneumonia, Plague) to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic originally used for bacterial infections such as streptococcal infection, bacterial pneumonia, peritonitis, conjunctivitis and plague.
The TxGNN model gives its top prediction as **Polyclonal Hyperviscosity Syndrome**, but **no clinical trials and no publications** support this prediction.
The best-supported candidate among the ten predictions is **bubonic plague**, which has **5 publications** (preclinical studies plus one adverse-event case report) and no human trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, peritonitis, staphylococcal infection, conjunctivitis, plague (from the knowledge graph; no approved indication text is available for Canadian licences) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Moxifloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is well established.

For the top-ranked prediction, polyclonal hyperviscosity syndrome, no plausible mechanistic link was identified. An antibacterial has no known effect on serum viscosity or immunoglobulin levels, so the high score (99.98%) appears to be an artifact of the knowledge graph rather than a real signal. The same applies to most other top predictions, such as hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, and hematopoietic and lymphoid neoplasm. All have no or only indirect evidence.

The one exception is **bubonic plague** (rank 10, score 99.41%). Moxifloxacin is active against *Yersinia pestis*, and plague and pneumonic plague are already among its original indications. Bubonic plague is therefore a close extension of an existing use, not a true new indication.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (polyclonal hyperviscosity syndrome). The trials below were linked to other predicted indications, and none tests moxifloxacin as a treatment for the predicted disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00324324](https://clinicaltrials.gov/study/NCT00324324) | Phase 3 | Terminated | 240 | Placebo-controlled trial of moxifloxacin to prevent bacterial infections after allogeneic stem cell transplant (linked to congenital hematological disorder; indirect) |
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | Terminated | 351 | Moxifloxacin alone vs ciprofloxacin plus amoxicillin/clavulanic acid for fever in low-risk neutropenic cancer patients (linked to monoclonal gammopathy; indirect) |
| [NCT07023029](https://clinicaltrials.gov/study/NCT07023029) | Phase 1 | Completed | 33 | Etavopivat cardiac repolarisation study in healthy participants; moxifloxacin is likely the QT positive control, so there is no efficacy evidence |

## Literature Evidence

No publications are available for the top-ranked prediction. The most relevant publications, linked to bubonic plague, are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Preclinical (animal) | Int J Antimicrob Agents | Moxifloxacin, gatifloxacin and ciprofloxacin gave full protection in mouse models of systemic and pneumonic plague |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Preclinical (animal) | Antibiot Khimioter | Levofloxacin and moxifloxacin were effective in mice infected with *Y. pestis* (ED50 5.5–14.0 mg/kg) |
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | Preclinical (in vitro) | Antimicrob Agents Chemother | A pharmacodynamic model was used to derive a moxifloxacin regimen that kills *Y. pestis* and prevents resistance |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | Preclinical (in vitro) | Antimicrob Agents Chemother | Comparative in vitro efficacy of candidate antibiotics against *Y. pestis* |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Case report (adverse event) | Ther Adv Drug Saf | Moxifloxacin-induced tinnitus in an older adult; relevant to safety only |

## Canada Market Information

Moxifloxacin is marketed in Canada under 14 valid single-ingredient DINs. Dosage form and approved indication text are not available in the data compiled for this report. The first 5 are listed below.

| DIN | Product Name |
|---------|------|
| 02472791 | M-MOXIFLOXACIN |
| 02520710 | MOXIFLOXACIN |
| 02462974 | MOXIFLOXACIN |
| 02432218 | PMS-MOXIFLOXACIN |
| 02375702 | TEVA-MOXIFLOXACIN |

Other authorisations include VIGAMOX, SANDOZ MOXIFLOXACIN, APO-MOXIFLOXACIN, MOXIFLOXACIN INJECTION, JAMP-MOXIFLOXACIN and AURO-MOXIFLOXACIN.

## Safety Considerations

**Contraindications (from knowledge graph drug-disease edges, not label text):**
- Cardiac: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease
- Neurological and neuromuscular: epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, peripheral neuropathy, peripheral nervous system disease
- Musculoskeletal: tendinitis, periarthritis, exostosis
- Liver: cirrhosis of the liver, drug-induced liver injury
- Gastrointestinal and metabolic: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, potassium deficiency disease

**Drug Interactions:** 100 interactions were identified. Examples are listed below.
- **Major:** hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids, which raise tendon-injury risk with fluoroquinolones), bupropion, chlorpropamide
- **Moderate:** antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, acarbose, albiglutide), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, calcium acetate, calcium phosphate, potassium citrate

Safety is also relevant to some predictions. Fluoroquinolones carry a labelled risk of peripheral neuropathy, which argues against use in neuropathy-associated hematological disease. Rare associations with pancreatitis argue against use in hyperamylasemia. Package insert warnings and precautions should be consulted for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions, including polyclonal hyperviscosity syndrome, are supported only by model scores. They have no trials, no relevant literature and no plausible mechanism, so they look like graph artifacts. Bubonic plague is the only credible candidate, but it is essentially an extension of an existing indication and rests on preclinical data without human trials.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, to complete the safety screening
- Mechanism of action data from DrugBank
- For bubonic plague: confirmation of whether the current Canadian label already covers plague, and review of human clinical or guideline evidence
- For all other predictions: de-prioritise unless independent clinical evidence appears
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

