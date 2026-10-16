---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Cholecalciferol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Osteoporosis, vitamin D deficiency, rickets, osteomalac…"
---

# Cholecalciferol
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

# Cholecalciferol: From Osteoporosis and Vitamin D Deficiency to Familial Isolated Hypoparathyroidism (PTH Secretion Defect)

## One-Sentence Summary

Cholecalciferol (vitamin D3) is originally used for vitamin D deficiency, rickets, osteomalacia, osteoporosis and hypoparathyroidism.
The TxGNN model ranks **familial isolated hypoparathyroidism due to impaired PTH secretion** as its top prediction (score 99.79%), but this is **model prediction only, with no clinical trials and no disease-specific literature**.
The best-supported candidate among the seven predictions is **renal osteodystrophy**, with **2 clinical trials** and **20 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, vitamin D deficiency, rickets, osteomalacia, hypoparathyroidism (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion (top-ranked) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (top-ranked prediction); L3 for renal osteodystrophy (rank 6) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails for renal osteodystrophy |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, cholecalciferol is a pro-hormone. It is converted in the liver to 25-hydroxyvitamin D and then in the kidney to calcitriol (1,25-dihydroxyvitamin D), which acts on intestine, bone and kidney to maintain calcium and phosphate balance.

**Top-ranked prediction (familial isolated hypoparathyroidism).** Hypoparathyroidism is already one of the drug's original indications, so the high score probably reflects this known link rather than a new repurposing signal. In defects of PTH secretion, native vitamin D supports calcium balance only as adjunct therapy. No trials or literature were found for this specific familial subtype.

**Other predictions in the list:**
- **Acromesomelic dysplasia (Campailla-Martinelli type) and craniofacial conodysplasia:** These are rare genetic skeletal disorders with no known vitamin D-responsive mechanism. The scores appear to come from network proximity alone.
- **Dahlberg-Borer-Newcomer syndrome:** The retrieved literature covers generic vitamin D topics and does not appear to concern this syndrome. It is treated as non-specific.
- **Hypophosphatemic rickets:** Active analogues (calcitriol, alfacalcidol) plus phosphate are the standard therapy. Native cholecalciferol is relevant mainly to nutritional or vitamin D-dependent forms. The evidence is indirect.
- **Renal osteodystrophy:** This is the most plausible. In chronic kidney disease, vitamin D deficiency contributes to secondary hyperparathyroidism and mineral-bone disorder. Cholecalciferol restores 25(OH)D substrate and can lower PTH. Active sterols and calcimimetics remain standard for established disease, so cholecalciferol is best positioned as correction of deficiency.
- **Renal tubular acidosis:** Vitamin D is used for the secondary bone disease, not the acidosis itself. The evidence is case reports only.

## Clinical Trial Evidence

The top-ranked prediction has no registered clinical trials. The only trials retrieved relate to the renal osteodystrophy prediction (rank 6):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D: placebo-controlled study of cholecalciferol in vitamin D-deficient kidney transplant recipients, looking at post-transplant kidney function, rejection and infections. Indirect; no results available. |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | Not applicable | Completed | 55 | Cholecalciferol versus doxercalciferol for secondary hyperparathyroidism in stage 3-4 CKD. Directly relevant to the mineral-bone pathway, but small. |

## Literature Evidence

The top-ranked prediction has no relevant literature. The list below covers the renal osteodystrophy prediction, which has the strongest evidence base:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34747516](https://pubmed.ncbi.nlm.nih.gov/34747516/) | 2022 | RCT (secondary analysis) | J Bone Miner Res | Cholecalciferol attenuated bone loss in incident kidney transplant recipients (193 randomized patients) |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | Prospective controlled study | Clin Nephrol | Effect of vitamin D sterols on bone histology in pre-dialysis CKD |
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | Clinical study | Biomedicines | Efficacy and safety of high-dose cholecalciferol in haemodialysis patients |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D in pre-dialysis CKD remains unclear |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Review | Nutrients | Vitamin D effects on bone and cardiovascular system in CKD and kidney transplant recipients |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | Kidney bone disease and mortality: roles of vitamin D, calcimimetics and minerals |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Workshop report | Am J Kidney Dis | National Kidney Foundation report on vitamin D in CKD stages 3-4 |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Rickets types and treatment with vitamin D and analogues (hypophosphatemic rickets) |
| [38365463](https://pubmed.ncbi.nlm.nih.gov/38365463/) | 2024 | Review | Best Pract Res Clin Endocrinol Metab | Vitamin D deficiency or resistance and hypophosphatemia |
| [14575620](https://pubmed.ncbi.nlm.nih.gov/14575620/) | 2003 | Case report | Endokrynol Diabetol Choroby Przemiany Materii Wieku Rozwoj | Vitamin D3 overdose after hasty rickets diagnosis in a child with distal tubular acidosis |

## Canada Market Information

Twenty single-ingredient licences are valid in Canada. The data compiled for this report does not include dosage forms or approved indication text. The five main authorizations are:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02371502 | EURO-D 50000 IU | Not available | Not available |
| 02498944 | AG-VITAMINE D TABLETS | Not available | Not available |
| 02546876 | VITAMIN D3 | Not available | Not available |
| 02449110 | JAMP-VITAMIN D | Not available | Not available |
| 02276429 | FOSAVANCE (alendronate/vitamin D3) | Not available | Not available |

Other licences include combination-type products with alendronate (APO-ALENDRONATE/VITAMIN D3, JAMP ALENDRONATE/VITAMIN D3) and prenatal multivitamins (PREGVIT, PREGNANCY MULTIVITAMIN).

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are network associations, not label text): hypercalcaemia, nephrocalcinosis, hyperparathyroidism, sarcoidosis, kidney disease, liver disease, hypertension, diabetes mellitus, phosphorus metabolism disorders, primary hyperoxaluria, atrial fibrillation, hyperlipidaemia, Wilson disease, iron-overload disorders, sickle cell anaemia, and prostate and breast cancer, among others.

**Drug interactions:** 56 interactions were identified. The major-level ones are other vitamin D agents:
- Calcifediol
- Calcitriol
- Dihydrotachysterol
- Doxercalciferol

Moderate-level interactions include:
- Thiazide diuretics (bendroflumethiazide, chlorothiazide, chlorthalidone, benzthiazide)
- Barbiturates (amobarbital, butabarbital, butalbital)
- Carbamazepine
- Bile-acid sequestrants (cholestyramine, colesevelam, colestipol)
- Digoxin and digitoxin
- Topical vitamin D analogues

Cimetidine is a minor interaction.

**Case-based safety signals:** The literature reports vitamin D3 overdose in a child with distal renal tubular acidosis, and premature cranial synostosis possibly linked to alpha-hydroxylated vitamin D in X-linked hypophosphatemic rickets.

Please refer to the package insert for label warnings, since these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, familial isolated hypoparathyroidism)
**Proceed with Guardrails** (for renal osteodystrophy, rank 6, as the more evidence-supported direction)

**Rationale:**
- The top-ranked prediction duplicates an existing indication and has no trials or specific literature (L5), so it offers no new repurposing signal. The skeletal dysplasias and Dahlberg-Borer-Newcomer syndrome have no plausible mechanism or specific evidence.
- Renal osteodystrophy (L3) has a plausible mechanism, a Phase 3 trial (status unknown) and a completed comparison study, and a post-transplant RCT secondary analysis. Native cholecalciferol is best framed as deficiency correction alongside standard active sterols and calcimimetics. Hypophosphatemic rickets and renal tubular acidosis remain research questions (L4).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Detailed mechanism of action data (MOA)
- Results or an updated status for NCT00752401, and a well-powered RCT with bone outcomes in CKD
- A monitoring plan for serum calcium, phosphate, PTH and 25(OH)D, with caution in patients with hypercalcaemia, nephrocalcinosis or on interacting vitamin D agents and thiazides
- Dosage form and approved indication details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

