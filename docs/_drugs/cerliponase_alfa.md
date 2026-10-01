---
layout: default
title: Cerliponase Alfa
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase alfa: From CLN2 Disease to Scheie Syndrome

## One-Sentence Summary

Cerliponase alfa (Brineura) is a recombinant TPP1 enzyme replacement therapy given directly into the brain ventricles. It is used for CLN2 disease, a lysosomal storage disorder caused by TPP1 deficiency. The TxGNN model predicts it may be effective for **Scheie syndrome** (attenuated MPS I), but **no clinical trials and no publications** support this, and the mechanistic review finds no plausible link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLN2 disease (TPP1 deficiency). The Canadian licence record does not list indication text. |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on the known profile, cerliponase alfa supplies TPP1, a lysosomal enzyme that cleaves tripeptides, and is delivered intraventricularly to the central nervous system. Its efficacy is established in CLN2 disease, where TPP1 is missing.

Scheie syndrome is caused by a different enzyme deficiency, IDUA, which leads to accumulation of glycosaminoglycans. TPP1 does not degrade these substrates. Because the drug is delivered to the brain, it would also not reach the systemic and skeletal disease that characterises Scheie syndrome. The only overlap is that both are lysosomal storage diseases.

The high TxGNN score most likely reflects this shared "lysosomal storage disease" neighbourhood in the knowledge graph, not a real pharmacological connection. The prediction should be treated as a model artefact until shown otherwise.

Other top-ranked predictions show the same pattern:
- **Hurler syndrome, Gaucher disease, cholesteryl ester storage disease and Wolman disease:** these are different lysosomal enzyme deficiencies, and TPP1 does not act on their substrates.
- **Neuroserpin inclusion body encephalopathy, juvenile myoclonic epilepsy, proximal myopathy with extrapyramidal signs and ichthyosis syndrome:** these have unrelated mechanisms, and no link to TPP1 biology could be identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Scheie syndrome.

Across all ten predicted indications, only one publication was found. It is a 2026 review of natural-history mapping in lysosomal storage disorders that uses Gaucher disease as a model ([PMID 41527340](https://pubmed.ncbi.nlm.nih.gov/41527340/)). It provides disease context only and contains no evidence about cerliponase alfa.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2484013 | BRINEURA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the available records.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). No trials or supporting publications exist. The mechanistic review finds that TPP1 replacement does not address the IDUA defect, and intraventricular delivery would not reach systemic disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- Any preclinical evidence that TPP1 replacement affects glycosaminoglycan accumulation or CNS disease in MPS I (none has been identified)
- A route-compatibility assessment, since the available route (intraventricular) does not match the systemic needs of Scheie syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

