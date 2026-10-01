---
layout: default
title: Imiglucerase
parent: Moderate Evidence (L3-L4)
nav_order: 467
evidence_level: L4
indication_count: 10
---

# Imiglucerase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase is a recombinant form of the enzyme glucocerebrosidase, used as enzyme replacement therapy for Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**, but there are **0 clinical trials** and only **2 general reviews** on enzyme replacement therapy (ERT) in this area, and neither tests imiglucerase in Hurler syndrome.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (identified from the literature; the Canadian label text was not provided) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, imiglucerase is a recombinant glucocerebrosidase, an enzyme replacement therapy for Gaucher disease. It breaks down glucosylceramide that builds up in macrophages.

The link to the new indication is weak and works only at the drug-class level. Hurler syndrome (MPS I) is caused by a deficiency of a different enzyme, alpha-L-iduronidase. It leads to accumulation of glycosaminoglycans (GAGs), not glucosylceramide. Imiglucerase has no known activity on GAG substrates.

The high TxGNN score most likely reflects the shared "lysosomal storage disease / enzyme replacement" neighbourhood in the knowledge graph, not any overlap in enzyme or substrate. The prediction should be read as a class-level association, not a mechanistic one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review / imaging methodology | Proc Natl Acad Sci U S A | Discusses PET imaging of enzyme replacement therapy. It lists Hurler syndrome among the lysosomal diseases where ERT has been used, with Gaucher disease as the prototype. It does not test imiglucerase in Hurler syndrome. |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | Rev Med Interne | Overview of ERT for lysosomal storage diseases. It notes that imiglucerase (Cerezyme) replaced placenta-derived alglucerase for Gaucher disease. It provides no imiglucerase data in MPS I. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2241751 | CEREZYME |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score and general ERT reviews. There are no trials, and the mechanism does not fit: Hurler syndrome is an iduronidase deficiency with GAG accumulation, which imiglucerase does not act on. The high score is most likely a class-level artifact of the graph.

The same pack lists a "lysosomal storage disease with skeletal involvement" entry (rank 6). It reflects skeletal manifestations of Gaucher disease, which is on-label use, not repurposing.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any link to iduronidase or GAG metabolism exists
- Preclinical evidence of imiglucerase activity in MPS I models
- The Health Canada label text (approved indication, warnings, contraindications) for a safety screen
- A comparison against existing MPS I-specific ERT before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

