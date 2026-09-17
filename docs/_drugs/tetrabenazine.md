---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazine: From Huntington's Disease Chorea to Polycystic Kidney Disease 3

## One-Sentence Summary

Tetrabenazine is a VMAT2 inhibitor with established clinical use in Huntington's disease chorea and other hyperkinetic movement disorders. The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)**, but this prediction is supported by **zero clinical trials** and **no drug-specific literature** — the 20 publications retrieved are general background on the disease itself, not evidence of tetrabenazine's use in it. The evidence pack's own mechanistic rationale states there is no known biological pathway connecting the two.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Huntington's disease chorea / hyperkinetic movement disorders (per evidence pack rationale; not confirmed via a formal regulatory filing in this pack) |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). What is known is that tetrabenazine is a VMAT2 (vesicular monoamine transporter 2) inhibitor that depletes presynaptic monoamines (dopamine, serotonin, norepinephrine), and its established clinical role — referenced in the trial and rationale data included here — is treatment of Huntington's disease chorea and related hyperkinetic movement disorders.

Polycystic Kidney Disease 3 is a ciliopathy-related renal/hepatic cystic disorder driven by fibrocystic and primary-cilia dysfunction pathways (e.g., PKD1/PKD2/PKHD1-related mechanisms), which have no established connection to monoamine transport or dopaminergic/serotonergic signaling. The evidence pack's own repurposing rationale explicitly states there is **no known molecular pathway overlap** between VMAT2 inhibition and cystogenesis, and attributes the very high TxGNN score to knowledge-graph embedding similarity rather than a genuine drug-disease relationship. This prediction should be treated as a likely false positive pending any independent mechanistic or preclinical signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

*Note: none of the publications below discuss tetrabenazine specifically — they are background reviews/case reports on polycystic kidney/liver disease etiology and management, retrieved on disease-term relevance only.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Review | Am J Gastroenterol | ACG guideline on focal liver lesions, including polycystic liver disease management |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Overview of autosomal dominant polycystic kidney disease (ADPKD) as a systemic disorder |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | ADPKD and polycystic liver disease (PCLD); notes tolvaptan slows renal deterioration |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic overlap and shared pathogenesis between ADPKD and ADPLD across 8 causative genes |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of PKD1/PKD2 mutations and resulting disease severity |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL clinical practice guidelines on cystic liver disease diagnosis and management |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Review | J Clin Invest | Exome sequencing identifies effectors of polycystin-1 function in isolated PCLD |
| [34034501](https://pubmed.ncbi.nlm.nih.gov/34034501/) | 2022 | Review | Rev Esp Enferm Dig | Diagnosis/management review of hydatid liver cysts (differential diagnosis) |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Review | Rev Med Suisse | Overview of polycystic liver disease subtypes: hamartomas, ADPLD, ADPKD |
| [37266470](https://pubmed.ncbi.nlm.nih.gov/37266470/) | 2023 | Case Report | Maedica | Rare case of ADPKD/APLD associated with advanced gastric cancer |

## Canada Market Information

Tetrabenazine is not currently marketed in Canada under this evidence pack (market status: Not Marketed), with 0 DIN licenses on file. No product or indication-text data is available.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are all flagged as missing in this evidence pack — including a **Blocking**-severity gap on TFDA/product-label warnings and contraindications, which by itself precludes any S1 safety pre-assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 (model-prediction-only) signal with no supporting clinical trials, no drug-specific literature, and no marketed product in Canada to anchor a safety review. The evidence pack's own mechanistic rationale states there is no plausible biological link between VMAT2 inhibition and PKD3 pathogenesis, indicating the prediction is likely a knowledge-graph embedding artifact rather than a genuine repurposing candidate.

**To proceed, the following is needed:**
- TFDA/product-label warnings and contraindications (currently a Blocking data gap)
- Verified mechanism-of-action data from DrugBank
- Any preclinical or mechanistic evidence directly linking VMAT2/monoamine pathways to ciliopathy-driven cystogenesis
- If no such evidence emerges, this candidate should be deprioritized rather than advanced to further evaluation stages
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

