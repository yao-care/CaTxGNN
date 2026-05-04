---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Bimatoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Bimatoprost: From Glaucoma/Ocular Hypertension to Periodontal Malformation Syndrome

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analogue originally approved for treating glaucoma and ocular hypertension (Lumigan®) and eyelash hypotrichosis (Latisse®), though it is not currently marketed in Canada or Taiwan.
The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**, with **0 clinical trials** and **20 publications** retrieved — however, none of these publications directly examine bimatoprost in this condition.
The prediction is driven by knowledge graph topology and lacks pharmacological support; current evidence is **L5 only**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular hypertension (globally approved; no Canada/Taiwan registration on record) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on published pharmacological literature, bimatoprost is a synthetic prostamide F2α analogue (FP prostaglandin receptor agonist). Its efficacy in reducing intraocular pressure is well established, and its FDA-approved use for eyelash hypotrichosis (Latisse®, 0.03% solution) reflects its ability to activate FP receptors in hair follicle dermal papilla cells, prolonging the anagen (growth) phase and enlarging follicle diameter.

The predicted indication — malformation syndrome with odontal and/or periodontal component — refers to conditions involving structural abnormalities of teeth and the surrounding periodontal tissues. Prostaglandins (particularly PGE2) are known mediators of periodontal inflammation and alveolar bone remodeling. However, bimatoprost specifically targets the FP receptor subtype; there is no established link between FP receptor agonism and the developmental/malformation pathways that drive odontal and periodontal malformation syndromes, which are typically genetic in origin.

Critically, all 20 publications retrieved are general periodontal disease literature (e.g., EFP clinical guidelines, subgingival microbial complex studies, gingival fibroblast biology) — none involve bimatoprost. The high TxGNN score most likely reflects knowledge graph topological proximity (bimatoprost → hair follicle → connective tissue → periodontal tissue) rather than a true pharmacological relationship. This prediction should be considered a graph noise artifact at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Twenty publications were retrieved; however, **none examine bimatoprost in this indication**. All papers are general periodontal disease research and are listed below for completeness.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Clinical Practice Guideline | J Clin Periodontol | EFP S3-level CPG for Stage IV periodontitis treatment |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Bidirectional relationship between periodontitis and diabetes; ~3× increased susceptibility in diabetic patients |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontology 2000 | Complications and treatment errors in regenerative periodontal surgery |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Cochrane Systematic Review | Cochrane Database Syst Rev | Periodontal treatment and glycaemic control in diabetes; subgingival instrumentation assessed |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontology 2000 | Sleep disorders (especially OSA) as emerging risk factor for periodontal disease |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dent Res | Gingival fibroblasts as sentinel innate immune cells in periodontitis pathogenesis |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observational Study | J Clin Periodontol | Characterisation of microbial complexes in subgingival plaque (n=185) |
| [12010523](https://pubmed.ncbi.nlm.nih.gov/12010523/) | 2002 | Review | J Clin Periodontol | Evidence-based assessment of scaling and root planing as gold standard for chronic periodontitis |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnol | Biomaterial-mediated macrophage immunotherapy as a novel direction in periodontitis treatment |
| [20599785](https://pubmed.ncbi.nlm.nih.gov/20599785/) | 2010 | Review | Biochem Pharmacol | Complement system overactivation contributing to immunopathology in periodontitis |

> ⚠️ **Important caveat**: None of the 20 retrieved publications involve bimatoprost. This literature represents background periodontology research only. No direct evidence connecting bimatoprost to odontal/periodontal malformation syndrome was identified.

---

## Canada Market Information

Bimatoprost is currently not marketed in Canada. No Drug Identification Numbers (DINs) are registered with Health Canada.

| DIN | Product Name | Dosage Form | Approved Indication |
|-----|-------------|-------------|---------------------|
| — | No licensed products on record | — | — |

> Bimatoprost is marketed in other jurisdictions (e.g., Lumigan® for glaucoma and Latisse® for eyelash hypotrichosis in the USA), but Canada regulatory data was not found in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings, contraindications, and drug interaction data were not available in the current evidence pack. Safety data should be obtained from the Health Canada product monograph or the FDA-approved labelling (Lumigan®/Latisse®) before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction scores 99.997% but is supported by L5 evidence only — no clinical trials and no bimatoprost-specific literature for periodontal malformation syndrome. The mechanistic link between FP receptor agonism and odontal/periodontal malformation pathology is not established, and the repurposing rationale analysis identifies this as a probable knowledge graph topology artefact rather than a true pharmacological signal.

**To proceed, the following is needed:**
- Confirm MOA data for bimatoprost (specifically: does FP receptor signalling play any role in periodontal ligament, cementum, or odontal development?)
- Conduct a targeted literature search for prostaglandin FP receptor involvement in congenital odontal/periodontal malformation syndromes
- Determine whether high TxGNN rank reflects a true biological signal or graph noise (e.g., compare with known FP receptor biology in craniofacial development)
- Obtain Canada/Taiwan package insert and safety data before advancing to any Stage 1 assessment
- Consider deprioritising this indication in favour of the alopecia indication (Rank 8), which has L2 evidence and an "Proceed with Guardrails" recommendation supported by multiple completed Phase 2 RCTs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

