---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 933
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Acute Promyelocytic Leukemia and Acne to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin is a retinoid (a vitamin A derivative) sold in Canada as Vesanoid and Retin-A. The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but **no clinical trials and no publications** support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute promyelocytic leukemia and acne (inferred from the marketed products Vesanoid and Retin-A; the supplied license records contain no indication text) |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tretinoin is a retinoid, a class with general immunomodulatory activity, and its efficacy in its approved uses is established. Mechanistically, it may be applicable to inflammatory conditions, but the supplied data do not support a specific link to rheumatoid nodulosis.

The high score most likely reflects the model's graph-neighbor patterns, not direct evidence. Related arthritis terms rank in the top 10 as well (juvenile idiopathic arthritis and its synonyms, rheumatoid factor-positive polyarticular JIA). Several of these are synonym-level overlaps, so they are not independent confirmations.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rheumatoid nodulosis.

### Best-evidenced alternative: Osteoarthritis (rank 7, score 99.44%, L4)

This is the only predicted indication with any literature. All of it is genetic, preclinical or computational, and there are no trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36542696](https://pubmed.ncbi.nlm.nih.gov/36542696/) | 2022 | Genetic/mechanistic | Sci Transl Med | ALDH1A2 variants (key enzyme for all-trans retinoic acid synthesis) are linked to severe hand OA, suggesting an anti-inflammatory role for retinoic acid |
| [37418291](https://pubmed.ncbi.nlm.nih.gov/37418291/) | 2023 | Genetic/computational | DNA Cell Biol | GWAS-to-drug analysis proposing retinoic acid metabolism blocking agents to suppress mechanoflammation in OA |
| [40564983](https://pubmed.ncbi.nlm.nih.gov/40564983/) | 2025 | Preclinical/computational | Int J Mol Sci | RNA-seq and network pharmacology study of retinoic acid-induced OA, suggesting excess exposure may be harmful |
| [15946654](https://pubmed.ncbi.nlm.nih.gov/15946654/) | 2005 | In vitro | Biochem Pharmacol | All-trans retinoic acid blocked cytokine-induced MMP production in human chondrocytes via JNK-AP-1 signaling |
| [38302538](https://pubmed.ncbi.nlm.nih.gov/38302538/) | 2024 | In vitro | Sci Rep | Effect of a retinoic acid analogue on stem cell chondrogenesis |

The direction of effect is conflicting: some studies suggest retinoic acid protects cartilage, others suggest it causes harm. Dose and route dependence are unresolved. Many of the other retrieved papers are not retinoid-specific and are omitted.

## Canada Market Information

Showing 5 of 10 authorizations. Dosage form and approved indication text were not supplied.

| DIN | Product Name |
|---------|------|
| 2145839 | VESANOID |
| 443794 | RETIN-A |
| 2264633 | RETIN-A MICRO |
| 2520036 | JAMP TRETINOIN |
| 1926462 | VITAMIN A ACID |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Retinoid, differentiation-inducing agent (oral use in leukemia); not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

The prediction notes flag two concerns for new uses. Retinoid teratogenicity and bone effects would need review for any pediatric arthritis use. Retinoid effects on skeletal development would need review for the skeletal dysplasias (pseudoachondroplasia, acromesomelic dysplasia).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, rheumatoid nodulosis, rests on the model score alone, with no trials, no literature and no supplied mechanism. The other nine predictions are also model-only (L5), except osteoarthritis, which has only preclinical and genetic evidence with conflicting direction. It is best treated as a research question, not a development candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search for retinoid use in rheumatoid nodulosis and the arthritis subtypes
- For osteoarthritis, resolution of the protective-versus-harmful direction, including dose and route, and a route compatibility assessment
- Original indication text and dosage forms for the Canadian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

