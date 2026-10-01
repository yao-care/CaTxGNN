---
layout: default
title: Aspartic Acid
parent: Model Prediction Only (L5)
nav_order: 76
evidence_level: L5
indication_count: 1
---

# Aspartic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Aspartic Acid: From Amino Acid Nutrition Component to Renal Tubular Acidosis

## One-Sentence Summary

Aspartic acid is a non-essential amino acid. In Canada it appears in amino acid and parenteral nutrition products such as PROSOL, OLIMEL, PRIMENE and PERIOLIMEL. The TxGNN model predicts it may be useful for **renal tubular acidosis (RTA)**, but this is a model prediction only. The one registered clinical trial retrieved is unrelated, and **none of the 9 publications** shows aspartic acid treating RTA.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the original approved indication text was not provided in the retrieved licence records. The predicted link therefore cannot be checked against the drug's known pharmacology.

Aspartate does take part in kidney metabolism. It is a substrate for renal ammoniagenesis and the TCA cycle, and it is handled by tubular transporters. For example, SLC22A13 effluxes aspartate and glutamate at the basolateral membrane of type A intercalated cells in the collecting duct (PMID 24147638). This is physiological background, not a therapeutic rationale.

Aspartic acid is not an alkalinizing agent. No retrieved evidence shows a plausible route by which it would correct tubular acid-base handling. The high TxGNN score most likely reflects a graph association (aspartate metabolism in the kidney and acidosis) rather than demonstrated treatment benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04725812](https://clinicaltrials.gov/study/NCT04725812) | Phase 2 | Terminated | 2 | Eculizumab in preeclampsia (CRUSH study). Not related to RTA, and aspartic acid is not the intervention. No usable efficacy or safety evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Case report | J Inherit Metab Dis | Neonate with pyruvate carboxylase deficiency, proximal RTA and cystinuria. The infant began to thrive when the diet was supplemented with aspartic acid and other amino acids. This is a confounded, single-patient observation. |
| [990372](https://pubmed.ncbi.nlm.nih.gov/990372/) | 1976 | Clinical physiological study | Biomedicine | Intravenous arginine and ornithine-aspartate loading in siblings with a neurological syndrome, incomplete RTA and cystinuria. This was an amino acid handling study, not RTA treatment. |
| [12087557](https://pubmed.ncbi.nlm.nih.gov/12087557/) | 2002 | Case report | Am J Kidney Dis | Autosomal recessive distal RTA caused by the G701D mutation of the AE1 (SLC4A1) gene. |
| [23053187](https://pubmed.ncbi.nlm.nih.gov/23053187/) | 2013 | Case report | Ann Hematol | Hypokalaemic distal RTA with haemolysis and acanthocytosis in a band 3 (SLC4A1) A858D homozygote. |
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Cohort | J Pediatr (Rio J) | Whole-exome sequencing for the genetic diagnosis of distal RTA in four children. |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Case series | Nephron Physiol | Clinical and genetic features of distal RTA in Filipino children with SLC4A1 mutations. |
| [24147638](https://pubmed.ncbi.nlm.nih.gov/24147638/) | 2014 | Preclinical (in vitro) | Biochem J | SLC22A13 mediates unidirectional efflux of aspartate and glutamate in type A intercalated cells. |
| [2884989](https://pubmed.ncbi.nlm.nih.gov/2884989/) | 1987 | Preclinical (animal) | Biochem J | Fate of glutamate carbon in rat renal tubules, including the effect of chronic metabolic acidosis. |
| [5641145](https://pubmed.ncbi.nlm.nih.gov/5641145/) | 1968 | Preclinical (animal) | Nature | Concentrations of metabolic intermediates in kidneys of rats with metabolic acidosis. |

Most of these papers are on RTA genetics or renal amino acid metabolism. None tests aspartic acid as a treatment for RTA.

## Canada Market Information

Five of the 7 licences are listed below. The dosage form, manufacturer and approved indication text were not provided in the retrieved records.

| DIN | Product Name |
|---------|------|
| 2141450 | 20% PROSOL |
| 2352540 | OLIMEL 5.7% |
| 2236875 | PRIMENE 10% |
| 2477947 | OLIMEL 7.6% |
| 2352494 | PERIOLIMEL 2.5% E |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). The only clinical trial is unrelated, and the literature contains no study showing benefit of aspartic acid in RTA. Aspartic acid is not an alkalinizing agent, and there is no supported mechanistic route to the predicted indication.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank), to test whether any plausible link to tubular acid-base handling exists
- Approved indication text and package insert warnings and contraindications from Health Canada, which are needed for safety screening
- Direct preclinical or clinical evidence that aspartic acid, as opposed to alkalinizing therapy, improves acid-base status in RTA
- A pharmacological reason to prefer aspartic acid over standard RTA management

This is a research-stage prediction only. It is not medical advice and requires clinical validation before any use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

