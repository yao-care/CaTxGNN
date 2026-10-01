---
layout: default
title: Adenine
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Adenine
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

# Adenine: From Red Blood Cell Storage Additive to Drug-Induced Osteoporosis

## One-Sentence Summary

Adenine is marketed in Canada as a component of SAG-M additive solutions (sodium, adenine, glucose, mannitol), which are used for red blood cell storage. The exact original indication is inferred from the product names, because the licence records contain no indication text.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but **1 clinical trial** (an unrelated registry) and **3 publications** (none showing adenine treats bone loss) currently support this direction.
The prediction looks like a knowledge-graph artifact, so the evidence is essentially model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Red blood cell storage additive (inferred from product names; no indication text in licence records) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Adenine is an endogenous purine base that is a building block of nucleotides such as ATP and NAD+. In the Canadian products it serves as a nutrient in blood storage solutions, helping red cells regenerate ATP. It is not used there as a treatment for any disease.

The evidence pack does not support a therapeutic link between adenine and drug-induced osteoporosis. The retrieved literature concerns **tenofovir**, an adenine nucleotide analog that is associated with bone density loss, not bone protection. The connection to adenine therefore looks like a structural-name artifact of the knowledge graph rather than a real pharmacological relationship.

The other top-ranked predictions (colonic neoplasm, rectosigmoid neoplasm, colonic benign lesions, cecal disease) are also model-only or rest on unrelated papers. Acne is supported only by one early-phase trial whose link to adenine is unverified.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06065852](https://clinicaltrials.gov/study/NCT06065852) | N/A | Recruiting | 35,000 | National registry of rare kidney diseases (RaDaR). Observational, with no adenine intervention and no osteoporosis focus, so this is a spurious match (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22943210](https://pubmed.ncbi.nlm.nih.gov/22943210/) | 2012 | Review | Expert Opin Drug Metab Toxicol | PK/PD of emtricitabine/tenofovir in HIV. It concerns an adenine nucleotide analog, not adenine itself, and does not address osteoporosis treatment. |
| [31026554](https://pubmed.ncbi.nlm.nih.gov/31026554/) | 2019 | Preclinical (rat) | J Ethnopharmacol | Liver injury from the herbal formula Xian-Ling-Gu-Bao, which is used for osteoporosis. It does not involve adenine. |
| [20026012](https://pubmed.ncbi.nlm.nih.gov/20026012/) | 2010 | Preclinical (in vitro) | Biochem Biophys Res Commun | Tenofovir altered gene expression in primary osteoclasts, offering insight into drug-induced bone loss. The drug causes harm, and this is not support for adenine as a treatment. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2386925 | SAG-M |
| 2444097 | ADDITIVE SOLUTION SODIUM ADENINE GLUCOSE MANNITOL (SAGM) |

---

## Safety Considerations

Please refer to the package insert for safety information.

One signal appeared in the literature retrieved for another predicted indication (cecal disease). In several animal studies, dietary adenine is used to deliberately **induce chronic kidney disease and nephropathy**. This is preclinical, high-dose animal data and not direct clinical evidence, but it warrants attention to renal safety if any systemic use were ever considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis is supported only by model score (99.16%), with no relevant clinical trial and no literature showing adenine benefits bone. The retrieved papers point to a tenofovir-related name artifact, and the evidence level is L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the original indication from the licence records
- Preclinical or mechanistic evidence that adenine affects bone metabolism, to establish any real rationale
- Review of the renal safety signal from adenine-induced nephropathy models before any systemic repurposing is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

