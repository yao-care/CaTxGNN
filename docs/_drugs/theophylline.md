---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 907
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Asthma to Thrombotic Disease

## One-Sentence Summary

Theophylline is a bronchodilator originally used for airway diseases such as asthma, bronchitis and emphysema. The TxGNN model predicts it may be effective for **thrombotic disease**, but this is a computational prediction only, with **no registered clinical trials** and no publications that test theophylline for thrombosis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (also bronchitis, emphysema and related lung diseases) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

The Canadian licence records compiled for this report contain no indication text. The original indication above comes from the drug's known disease associations in the TxGNN knowledge graph.

## Why is This Prediction Reasonable?

Theophylline is a non-selective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. In airways, these actions relax smooth muscle and reduce inflammation.

PDE inhibition can raise cAMP in platelets, which could plausibly reduce platelet aggregation. That gives a theoretical link to thrombosis. Other cAMP-raising agents, such as milrinone, have shown antiplatelet effects in laboratory studies.

There are important counterpoints:
- Adenosine itself inhibits platelet function, so theophylline's adenosine antagonism may work against any antiplatelet effect.
- No clinical data support an antithrombotic benefit.
- The retrieved literature is mostly about measuring platelet biomarkers, the pharmacokinetics of a different drug (ticlopidine), or theophylline assay methods. None of it tests theophylline for thrombosis.

The high score of 0.996 is therefore a model output, not a finding supported by evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publication identified directly tests theophylline for treating or preventing thrombosis. The items below are the closest platelet- and vascular-related results.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Pharmacokinetic review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug. It concerns a different drug and is not about theophylline. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Thromboxane A2 and prostacyclin in platelets and atherosclerosis. Prostacyclin acts through adenylate cyclase and cAMP, which gives background on the mechanism. |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | Gen Pharmacol | Milrinone, a PDE inhibitor, reduced human platelet aggregation and raised cAMP, and interacted with adenosine. This is an analogous mechanism, not theophylline. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Not classified | Minerva Cardioangiol | A theophylline nicotinate derivative studied in chronic obliterating peripheral arteriopathy. It concerns a related compound, and no abstract is available. |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Not classified | Cardiologia Pratica | Cardiocirculatory effects of a theophylline nicotinic ester in cerebral and peripheral angiopathies. It concerns a related compound. |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Ex vivo observational | Rheumatology (Oxford) | Platelet and neutrophil activation in Behçet's disease. It is not about theophylline therapy. |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Laboratory method | Platelets | Measuring soluble CLEC-2 as a marker of platelet activation in people at risk of thrombotic disease. |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Laboratory method | PLoS One | Plasma preparation for monitoring platelet-stored molecules. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Laboratory method | Br J Haematol | A platelet factor 4 radioimmunoassay. Theophylline is used only as an anticoagulant-tube additive to prevent platelet activation in the sample. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Anal Chim Acta | An aptasensor for detecting theophylline. It has no therapeutic relevance to thrombosis. |

## Canada Market Information

All six licences are valid single-ingredient products. Dosage form and approved-indication text are not available in the records compiled for this report.

| DIN | Product Name |
|---------|------|
| 00692700 | AA-THEO LA |
| 00692697 | AA-THEO LA |
| 00692689 | AA-THEO LA |
| 00627410 | ELIXIR DE THEOPHYLLINE |
| 02360101 | THEO ER |
| 02360128 | THEO ER |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** The knowledge graph links theophylline to contraindication with many conditions. They fall into these groups:
  - **Cardiovascular and neurological:** hypertension, epilepsy.
  - **Psychiatric:** anxiety and neurotic disorders, psychotic disorders including schizophreniform and schizoaffective disorders.
  - **Hepatic, renal and gastrointestinal:** liver failure and liver disease, kidney disease, gallbladder disease, peptic ulcer disease.
  - **Endocrine and metabolic:** hypothyroidism and myxedema, diabetes mellitus and diabetic ketoacidosis, porphyria.
  - **Blood disorders:** thrombocytopenia, neutropenia and agranulocytosis. These are relevant to any antithrombotic use.
  - **Other:** open-angle glaucoma, benign prostatic hyperplasia, dermatitis herpetiformis.
- **Drug Interactions:** 100 interactions were recorded. Bupropion is rated **Major**. Examples of Moderate interactions:
  - Acid suppressants: cimetidine, famotidine, ranitidine, omeprazole, rabeprazole.
  - Macrolide and tetracycline antibiotics: clarithromycin, doxycycline, minocycline, tetracycline.
  - Corticosteroids: dexamethasone, hydrocortisone, budesonide, betamethasone, triamcinolone.
  - Bowel-prep agents and activated charcoal.
  - Ephedrine is Minor.

Please refer to the package insert for full warnings. Detailed label warnings were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trials exist, and the literature does not test theophylline for thrombosis. The mechanistic link (PDE inhibition raising platelet cAMP) is plausible, but it is partly offset by adenosine antagonism. Theophylline is a marketed drug in Canada, so access is not a barrier.

**To proceed, the following is needed:**
- Preclinical or ex vivo data showing that theophylline at clinically achievable serum levels inhibits platelet aggregation or thrombus formation.
- A clear thrombotic indication and population, supported by a clinical hypothesis.
- Package insert warnings and contraindications from Health Canada, so safety screening can be done.
- A safety plan for theophylline's narrow therapeutic range, serum level monitoring, and its many drug interactions, especially with anticoagulants and antiplatelet drugs.

**Note on other predictions:** Among theophylline's other predicted indications, *obstructive lung disease* ranks fifth. It falls within the drug's existing use and has the strongest support: several Phase 3 trials (for example NCT01599871 and NCT02340520) and an L1 evidence level. This is not true repurposing. Nasal cavity disease (allergic rhinitis) and tracheal disease have limited, indirect support (L4). The remaining predictions have little or no support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

