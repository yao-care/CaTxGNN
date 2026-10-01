---
layout: default
title: Perphenazine
parent: Model Prediction Only (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
---

# Perphenazine
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

# Perphenazine: From Antipsychotic Use (Original Indication Not Recorded) to Retinal Dystrophy

## One-Sentence Summary

Perphenazine is a phenothiazine antipsychotic, and the Canadian licence records provided contain no approved-indication text. The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and no relevant publications supporting this. The 15 retrieved papers are generic eye-anomaly reviews that never mention perphenazine, so this prediction is best treated as a likely model artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the Evidence Pack. Perphenazine is known as a phenothiazine that blocks dopamine D2 and serotonin 5-HT2A receptors.

Retinal dystrophy is a group of inherited degenerative eye disorders. Dopamine and serotonin receptor blockade has no established role in treating it, and no plausible mechanistic link was identified. The very high score (0.9996) most likely reflects how the knowledge graph connects entities, not real biology.

Phenothiazines are also associated with pigmentary retinopathy. That makes this prediction a safety concern as well as a lack of support.

Other predicted indications such as syndromic myopia, X-linked myopias, polymicrogyria, hydranencephaly, Charcot-Marie-Tooth type 1G, glycosylation disorders and atypical glycine encephalopathy also scored above 99.9%. They share the same problem: no trials, no literature and no mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers mentions perphenazine. They matched on eye-anomaly keywords only and are not evidence for this use. No RCTs were found. The table lists up to 10 of the 15 retrieved papers, reviews first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Overview of orbital infections, most often caused by sinusitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic approach to evaluating double vision |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis, its features and associated refractive problems |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens size, shape and position |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex of vitreoretinal degeneration |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Differential diagnosis and imaging of pediatric ocular pathologies |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | Clinical features and outcomes in orbital arteriovenous malformations |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two patients with unilateral cryptophthalmia |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | Rare congenital trochlear-oculomotor synkinesis in a child |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optom Vis Sci | Synergistic divergence in congenital fibrosis of the extraocular muscles |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 335134 | PERPHENAZINE |
| 335096 | PERPHENAZINE |
| 335126 | PERPHENAZINE |
| 335118 | PERPHENAZINE |

Dosage form, manufacturer and approved indication text are not available in the licence records provided.

---

## Safety Considerations

- **Retinal safety signal**: Phenothiazines are associated with pigmentary retinopathy. This works against any use in retinal disease.
- **Drug Interactions**: The DDI query returned no results.

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials, the retrieved literature is unrelated to perphenazine, and no mechanistic link exists. The known retinal toxicity of phenothiazines is a safety signal against this use.

**Side note on the other candidates:**
Among all predictions for this drug, only **anxiety disorder** (rank 10, score 99.53%) has any supporting evidence. It is rated L3 and "Research Question".
- Two trials are on record, both graded C: a Phase 2 antioxidant study (NCT05646693) and a Phase 3 pharmacovigilance study (NCT02374567). Neither tests perphenazine for anxiety.
- Historical RCTs from 1959–1968 and a 2006 review of antipsychotics for anxiety are consistent with the mechanism.
- The old, small studies and possible overlap with an existing label mean it may not be true repurposing.

**To proceed, the following is needed:**
- The Health Canada package insert, for warnings, contraindications and approved indications (a blocking gap)
- Mechanism-of-action data from DrugBank
- Original-indication data, to judge whether the anxiety use is truly new
- For anxiety disorder, a review of the older trials and a weighing of somnolence, extrapyramidal and metabolic risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

