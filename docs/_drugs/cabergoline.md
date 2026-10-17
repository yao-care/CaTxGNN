---
layout: default
title: Cabergoline
parent: Model Prediction Only (L5)
nav_order: 142
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Cabergoline: predicted new indication Pituitary cancer (evidence level L5). Approved use: Hyperprolactinaemia and prolactin-producing pituitary tumour"
monitor_inn: "CABERGOLINE"
predicted_indications: ["progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma"]
---

# Cabergoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Cabergoline: From Hyperprolactinaemia to Pituitary Cancer

## One-Sentence Summary

Cabergoline is a dopamine agonist originally used to treat hyperprolactinaemia and prolactin-producing pituitary tumours.
The TxGNN model predicts it may be effective for **pituitary cancer**, with **14 registered clinical trials** and **20 publications** currently supporting this direction.
Most of this evidence concerns pituitary *adenomas* (benign tumours) rather than true carcinoma, so direct evidence for the predicted indication is limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinaemia and prolactin-producing pituitary tumour (the Canadian licence records contain no indication text) |
| Predicted New Indication | Pituitary cancer (the top-ranked prediction, pituitary adenocarcinoma, has only case-level literature and no trials, so the best-supported prediction is reported here) |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L1 (≥2 completed Phase 3 trials, though in adenoma subtypes) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails (research question; direct carcinoma evidence is lacking) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, cabergoline is a dopamine D2 receptor agonist. It suppresses prolactin secretion and can shrink tumours that express D2 receptors.

Many pituitary tumours, including corticotroph and lactotroph tumours, express D2 receptors. That gives a plausible mechanistic link between the original indication (prolactin-secreting tumours) and the predicted one (pituitary tumours more broadly). A 2020 review (PMID 31597135) also describes newer anti-tumour mechanisms of cabergoline, such as suppression of tumour cell proliferation and induction of cell death.

An important caveat is that pituitary carcinoma is rare and distinct from benign adenoma. The Phase 3 trials found study adenoma subtypes (corticotroph, nonfunctioning, microprolactinoma), not carcinoma. The "pituitary cancer" label is therefore best read as "pituitary tumours broadly". Evidence from adenoma trials cannot be assumed to transfer to true carcinoma.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | Not reported | Cabergoline for Cushing disease from corticotroph pituitary adenoma; outcome data still need to be retrieved |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Randomised open-label trial of cabergoline in residual nonfunctioning pituitary adenoma after transsphenoidal surgery |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Randomised trial of dopamine agonist treatment in nonfunctioning pituitary adenomas |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in nonfunctioning and resistant adenomas, with in vitro and in vivo responses |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline vs no treatment for 48 weeks in nonfunctioning pituitary adenoma |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Octreotide plus cabergoline in acromegaly partially responsive to somatostatin analogue alone (single arm) |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or with cabergoline in Cushing's disease |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Phase 3 | Recruiting | 70 | High-dose vs standard-dose cabergoline in microprolactinoma (original indication; informs dose and safety) |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | Recruiting | 60 | Metabolic outcomes in prolactinoma patients on dopamine agonists (original indication) |
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | Not applicable | Completed | 50 | Observational study of cardiac abnormalities and valvular regurgitation in prolactinoma patients on long-term cabergoline |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Diagnosis and management of pituitary adenomas, functioning and nonfunctioning |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Review | Lancet Diabetes Endocrinol | Pathogenesis, diagnosis and management of prolactin-secreting adenomas |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Approach to the patient with prolactinoma |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | New anti-tumour mechanisms of cabergoline and potential broader applications |
| [35460460](https://pubmed.ncbi.nlm.nih.gov/35460460/) | 2022 | Review | J Endocrinol Invest | Dopaminergic control of Cushing's syndrome, including corticotroph tumours |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Review | Pituitary | Use of cabergoline in acromegaly |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Preclinical | Neuro-oncology | Targeting HTR2B suppresses nonfunctioning adenoma growth and sensitises it to cabergoline |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline in pituitary tumours and valvular disorders; most studies show no significant increase in valvulopathy risk |
| [24985062](https://pubmed.ncbi.nlm.nih.gov/24985062/) | 2014 | Review | Endocrine | Safety of cabergoline in pregnancy |
| [23325364](https://pubmed.ncbi.nlm.nih.gov/23325364/) | 2013 | Case report | Endocrine | Double pituitary adenomas in a patient treated with cabergoline |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242471 | DOSTINEX | Not listed | Not listed |
| 02455897 | APO-CABERGOLINE | Not listed | Not listed |
| 02549611 | JAMP CABERGOLINE | Not listed | Not listed |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): liver disease, gallbladder disease, heart valve disease, pulmonary fibrosis (including post-inflammatory), IgG4-related retroperitoneal fibrosis, and severe pre-eclampsia/pre-eclampsia.
- **Drug interactions:** 60 interactions were found in total. The main ones are:
  - **Major:** lorcaserin, clarithromycin
  - **Moderate:** metoclopramide
  - Other listed interactions have an unclassified severity, including calcitriol, pantoprazole, omeprazole, glimepiride, metformin, morphine, simvastatin and prednisone.
- **Literature signals:** Valvular heart disease is a recognised concern with ergot-derived dopamine agonists, although most studies of cabergoline in pituitary tumours found no significant increase in risk (PMID 25732645). A case report describes bilateral angle-closure glaucoma in a patient on cabergoline (PMID 21347189).

Please refer to the package insert for full warnings and contraindications, as label data were not available for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Completed Phase 3 trials support cabergoline in nonfunctioning and corticotroph pituitary adenomas, and the D2-receptor mechanism is plausible. However, none of the evidence directly addresses true pituitary carcinoma, which is the predicted indication. The other predictions are weaker: pituitary adenocarcinoma has only case reports, and progeria-short stature-pigmented nevi syndrome and spastic quadriplegic cerebral palsy have no supporting data. Glaucoma shows a safety signal rather than a benefit, so it should be held.

**To proceed, the following is needed:**
- Retrieve and review results from the completed Phase 3 trials (NCT00889525, NCT03271918, NCT02288962)
- Direct evidence in aggressive pituitary tumours or true carcinoma (for example case series or registry data)
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications from Health Canada, which is a blocking gap for safety screening
- Cardiac valve and long-term safety monitoring plan, especially for high-dose or long-term use
- Indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

