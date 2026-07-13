---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 1
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Folic Acid: From Folate Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (vitamin B9) is an essential water-soluble vitamin with established use in treating folate deficiency, megaloblastic anaemia, and preventing neural tube defects during pregnancy. The TxGNN model predicts it may have potential in **Biotin Metabolic Disease** (such as biotinidase deficiency), with **13 clinical trials** and **20 publications** identified in the evidence search — though none directly evaluate folic acid as a treatment for this specific condition. The prediction is driven primarily by knowledge-graph ontology clustering among B-vitamin metabolic disorders rather than a direct mechanistic link.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Folate deficiency, megaloblastic anaemia, neural tube defect prevention (well-known clinical use; no Canadian DIN on file in this dataset) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (no DIN on file) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Folic acid (vitamin B9) and biotin (vitamin B7) are both members of the B-vitamin family that serve as obligatory cofactors in core metabolic pathways. Folic acid drives one-carbon transfer reactions essential for DNA synthesis, amino acid interconversion, and the remethylation of homocysteine to methionine. Biotin, by contrast, functions as the prosthetic group for four mitochondrial carboxylase enzymes — propionyl-CoA carboxylase, pyruvate carboxylase, methylcrotonyl-CoA carboxylase, and acetyl-CoA carboxylase — that are central to fatty acid synthesis, amino acid catabolism, and gluconeogenesis.

Biotin metabolic diseases — primarily biotinidase deficiency and holocarboxylase synthetase (HCS) deficiency — are inherited disorders caused by defects in enzymes responsible for biotin recycling or covalent attachment to apocarboxylases. Folic acid is not a substrate, cofactor, or regulator for any of these biotin-dependent enzymes. There is therefore **no direct pharmacological mechanism** by which folic acid could substitute for or meaningfully supplement biotin in these diseases. The TxGNN model's high prediction score most plausibly reflects knowledge-graph ontology clustering: within the graph, B-vitamin metabolism disorder nodes are tightly co-located, leading to high predicted similarity scores across the class even where direct therapeutic relationships do not exist.

The indirect biological argument is worth noting. Folic acid does have established clinical evidence in other inherited metabolic disorders sharing overlapping biochemical territory — including MTHFR deficiency (where high-dose folinic acid is first-line) and homocystinuria (where folic acid combined with B6 reduces homocysteine burden). This precedent demonstrates that B-vitamins can be repurposed at pharmacological doses for enzyme-cofactor disorders in the same metabolic super-network, and in theory a patient with biotin metabolic disease and concurrent MTHFR deficiency could require both. However, this represents a co-morbidity scenario rather than a primary repurposing indication for biotin metabolic disease itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal genomic newborn screening programme (Belgium); biotinidase deficiency is one of 126 screened conditions — establishes disease prevalence and early detection framework, not a folic acid therapy trial |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Double-blind cross-over RCT of Q10 ubiquinol + vitamin B/E complex for metabolic support in autism and Phelan-McDermid syndrome; provides a model for B-vitamin cofactor supplementation in metabolic disease, but does not test folic acid specifically in biotin metabolic disease |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional supplementation including folic acid for oxidative stress and methylation imbalance in autism; folic acid is one of multiple components, primary target is autism not biotin metabolic disease |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completed | 202 | Multi-vitamin/mineral and omega-3 fatty acid supplementation on impulsivity and aggression; folic acid is a background micronutrient component, not primary intervention |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Unknown | 1,963 | Nutritional genomics platform studying gene-diet interactions; general platform trial, no specific biotin metabolic disease indication |
| [NCT02302729](https://clinicaltrials.gov/study/NCT02302729) | N/A | Completed | 1,730 | Micronutrient powder supplementation for stunted children in Guatemala; folic acid is one of multiple micronutrients, population is generally malnourished not specifically biotin metabolic disease |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Fortified food vs. milk in malnourished children; serum folic acid measured as one of several micronutrient outcomes |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin and mineral supplementation for diabetic neuropathy and nephropathy; folic acid is one of multiple components, indication is diabetes complications |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation RCT for child neurodevelopment; primary intervention is iodine, folic acid is background supplementation |
| [NCT07350538](https://clinicaltrials.gov/study/NCT07350538) | N/A | Active, not recruiting | 20 | Gut microbiome profiling and personalised prebiotic interventions for alcohol addiction recovery; no direct relevance to biotin metabolic disease or folic acid therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Comprehensive reference chapter on vitamin-responsive neurological disorders; explicitly covers cobalamin, **folate, and biotin** as separate clinical entities with distinct management pathways — the most directly relevant reference in this dataset |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | VitB12 functions as cofactor for succinyl-CoA synthesis (via biotin) and for methionine synthesis (via **folic acid and homocysteine**); illustrates the biochemical intersection of B12, folate, and biotin in mitochondrial metabolism |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Treatable inborn errors of metabolism causing movement disorders; biotin-responsive IEM identified as a distinct, reversible category — establishes clinical context for biotin metabolic disease |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics of North America | Foundational reference on megavitamin-responsive aminoacidopathies; B-complex vitamins used at pharmacological doses for inherited enzyme deficiencies — establishes the pharmacological rationale for the broader drug class |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Review | Advances in Human Genetics | Early framework for vitamin-responsive inherited metabolic disorders; classifies mechanisms of vitamin dependency in IEM |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Review | Archives de Pédiatrie | Neonatal epilepsy in inborn errors of metabolism; biotin-dependent enzyme defects discussed alongside pyridoxine and folate-responsive epilepsies — illustrates clinical overlap and differential diagnosis |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases; three mechanisms reviewed — malabsorption, inborn errors in vitamin metabolism, and vitamin-dependent apoenzyme syndromes; provides conceptual basis for this repurposing hypothesis |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Vitamin dependency syndromes; B-complex vitamins as therapeutic cofactors when apoenzyme affinity for cofactor is reduced — directly relevant mechanistic framing |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Arch Biochem Biophys | Micronutrient optimisation for metabolic health ("metabolic tune-up"); folic acid, B12, and other B-vitamins discussed in context of DNA damage and metabolic pathway support |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and diabetes; notes reduced thiamine, pyridoxine, and **biotin** levels in diabetes and discusses folic acid's role in vascular protection — illustrates metabolic co-involvement across B-vitamins without direct biotin disease treatment |

---

## Canada Market Information

Folic acid has **no active Health Canada DINs** recorded in this dataset. Folic acid is widely available in Canada as an over-the-counter dietary supplement (in prenatal vitamins, multivitamins, and standalone folate supplements) and is recommended by Health Canada at 0.4 mg/day for reproductive-age women for neural tube defect prevention. However, no formal prescription product authorisation appears in the current regulatory query.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 99.49% is high, but in this case it reflects knowledge-graph proximity among B-vitamin metabolic disorders rather than a direct treatment relationship: folic acid has no established mechanism of action in biotinidase deficiency or holocarboxylase synthetase deficiency, and none of the 13 retrieved clinical trials or 20 publications provide direct efficacy evidence for folic acid in biotin metabolic disease. At L4 evidence level — mechanistic reasoning and indirect associations only — the current data is insufficient to justify a clinical development programme.

**To proceed, the following is needed:**
- Targeted preclinical studies (cell models of biotinidase deficiency or HCS deficiency) to test whether folic acid supplementation can modify disease biomarkers or compensate for biotin pathway dysfunction
- Mechanistic clarification on whether one-carbon metabolism (folate pathway) and biotin-dependent carboxylase metabolism intersect at any pharmacologically actionable node
- Identification of a patient subgroup with genuine co-morbid folate and biotin pathway defects (e.g., MTHFR deficiency concurrent with biotinidase deficiency) where combined B-vitamin supplementation could be studied
- Full safety dossier from Health Canada (package insert warnings and contraindications currently unavailable in this dataset)
- Expert consultation with an inborn errors of metabolism specialist to assess biological plausibility and define a research question suitable for prospective study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

