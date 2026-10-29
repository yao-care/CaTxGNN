---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 4
monitor_inn: "Cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-10-30
description: "Cholecalciferol: predicted new indication Acromesomelic dysplasia, Campailla Martinelli type (evidence level L5). Approved use: Not stated in the licence records compiled for this report. The knowl…"
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cholecalciferol: From Vitamin D Deficiency and Bone Disorders to Acromesomelic Dysplasia, Campailla Martinelli Type
{: .text-alpha }

## One-Sentence Summary

Cholecalciferol (vitamin D3) is a vitamin D supplement used for conditions such as osteoporosis, rickets, osteomalacia and vitamin D deficiency.
The TxGNN model's top-ranked prediction is **acromesomelic dysplasia, Campailla Martinelli type**, but this prediction has **0 clinical trials and 0 publications** behind it.
The best-supported candidate further down the list is **renal osteodystrophy** (2 clinical trials, 20 publications), which is discussed below as a secondary finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report. The knowledge graph records osteoporosis, postmenopausal osteoporosis, vitamin deficiency disorder, osteomalacia, rickets and hypoparathyroidism, among others (relations recorded in the knowledge graph, not label text) |
| Predicted New Indication | Acromesomelic dysplasia, Campailla Martinelli type |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 17 of 20) |
| Number of DINs | 20 (valid: 17) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cholecalciferol is a pro-hormone: it is converted in the liver to 25-hydroxyvitamin D and in the kidney to the active form, calcitriol. Calcitriol supports calcium and phosphorus absorption and bone mineralisation.

For the top-ranked prediction, **no mechanistic link is established**. Acromesomelic dysplasias are rare, genetically determined skeletal disorders, typically involving growth plate signalling pathways such as NPR2 or GDF5. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Cholecalciferol is unlikely to correct a primary genetic defect in growth plate signalling. The very high score (0.9978) therefore should not be read as clinical support.

The second-ranked prediction, craniofacial conodysplasia (score 0.9975), is in the same position: no trials, no publications and no demonstrated vitamin D-responsive mechanism.

### Better-supported secondary candidates

- **Renal osteodystrophy (rank 3, score 0.9911)**: In chronic kidney disease, impaired vitamin D activation leads to vitamin D deficiency, secondary hyperparathyroidism and disordered bone mineral metabolism. Cholecalciferol replenishes 25(OH)D stores, which may lower PTH and support bone health. This overlaps with existing vitamin D deficiency management, but the trials and studies cited are in related populations (CKD, dialysis, kidney transplant) rather than renal osteodystrophy defined by bone histology.
- **Renal tubular acidosis (rank 4, score 0.9906)**: The link is indirect. Vitamin D deficiency, rickets and osteomalacia occur as complications of tubular disorders, so cholecalciferol would at most treat bone manifestations, not the acid-handling defect.

## Clinical Trial Evidence

For the top-ranked prediction (acromesomelic dysplasia, Campailla Martinelli type): currently no related clinical trials registered.

For reference, the trials compiled for the rank 3 candidate, renal osteodystrophy:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D: randomised, placebo-controlled study of cholecalciferol in vitamin D-deficient kidney transplant recipients, assessing graft function (GFR, creatinine), rejection episodes, infections and CRP in the first year |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | Not applicable | Completed | 55 | Cholecalciferol vs doxercalciferol for secondary hyperparathyroidism in CKD stages 3–4 |

## Literature Evidence

For the top-ranked prediction: currently no related literature available.

For reference, selected publications compiled for the rank 3 candidate, renal osteodystrophy (the list is mostly reviews, and the one randomised trial is in transplant recipients):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34747516](https://pubmed.ncbi.nlm.nih.gov/34747516/) | 2022 | RCT (secondary endpoint analysis) | J Bone Miner Res | Cholecalciferol supplementation attenuated bone loss in 193 incident kidney transplant recipients |
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | Observational clinical study | Biomedicines | Efficacy and safety of high-dose cholecalciferol in haemodialysis patients with 25(OH)D deficiency |
| [39597015](https://pubmed.ncbi.nlm.nih.gov/39597015/) | 2024 | Observational prospective study | Medicina (Kaunas) | Targeting high-normal 25(OH)D with cholecalciferol in haemodialysis patients and its effect on CKD-MBD |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | Prospective controlled study | Clin Nephrol | Effect of vitamin D sterols on bone histology in pre-dialysis CKD |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D in pre-dialysis CKD; role remains unclear |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Review | Nutrients | Vitamin D effects on bone and cardiovascular system in CKD and transplant recipients |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Workshop report | Am J Kidney Dis | National Kidney Foundation workshop on vitamin D in CKD stages 3–4 |

## Canada Market Information

Twenty valid single-ingredient licences are recorded. The compiled data does not include dosage forms or approved indication text for any of them, so no approved indication can be stated here.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02371502 | EURO-D 50000 IU | Not available | Not available |
| 02498944 | AG-VITAMINE D TABLETS | Not available | Not available |
| 02546876 | VITAMIN D3 | Not available | Not available |
| 02449110 | JAMP-VITAMIN D | Not available | Not available |
| 02417995 | VITAMINE D 10 000 | Not available | Not available |

Other listed products include D-TABS, SANDOZ D 10 000, LUXA-D, alendronate/vitamin D3 products (FOSAVANCE, APO-ALENDRONATE/VITAMIN D3, JAMP ALENDRONATE / VITAMIN D3) and prenatal multivitamins (PREGVIT, PREGNANCY MULTIVITAMIN).

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text)**: These include hypercalcaemia, nephrocalcinosis, hyperparathyroidism, sarcoidosis, kidney disease, liver disease, phosphorus metabolism disorders, primary hyperoxaluria, and several others (for example hypertension, diabetes and certain cancers). Their clinical relevance should be checked against the product monograph.
- **Drug Interactions**: 56 interactions were found. Major-level interactions are with other vitamin D analogues: calcifediol, calcitriol, dihydrotachysterol and doxercalciferol (additive risk of excess vitamin D effect). Moderate interactions include thiazide diuretics (bendroflumethiazide, chlorothiazide, chlorthalidone), digoxin and digitoxin, barbiturates (amobarbital, butabarbital, butalbital), carbamazepine, and bile acid sequestrants (cholestyramine, colestipol, colesevelam).
- **Condition-specific cautions**: In renal tubular acidosis, a report describes vitamin D3 overdose after hasty rickets diagnosis in a child with distal tubular acidosis. In CKD, hypercalcaemia and hyperphosphataemia need monitoring.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, acromesomelic dysplasia (Campailla Martinelli type), has a very high model score but no trials, no publications and no plausible mechanism for a vitamin D effect on a primary genetic skeletal defect. Evidence is at L5 (model prediction only). The same applies to craniofacial conodysplasia. Renal osteodystrophy is the more credible direction, but its supporting studies are in related CKD and transplant populations, and it overlaps with existing vitamin D deficiency management.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, to allow safety screening
- Mechanism of action data
- For acromesomelic dysplasia: preclinical or genetic evidence of a vitamin D-responsive pathway before any clinical consideration
- For renal osteodystrophy: studies directly in this condition (for example with bone histology or fracture endpoints) and a hypercalcaemia/phosphate monitoring plan
- Approved indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

