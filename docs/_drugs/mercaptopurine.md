---
layout: default
title: Mercaptopurine
parent: Model Prediction Only (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mercaptopurine: predicted new indication Myeloid leukemia (evidence level L5). Approved use: Acute lymphoblastic leukemia (Health Canada indication text is not av…"
monitor_inn: "MERCAPTOPURINE"
predicted_indications: ["myeloid leukemia", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "pulmonary blastoma", "Hodgkins lymphoma", "primary pulmonary lymphoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Mercaptopurine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine is a purine antimetabolite originally used to treat acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **myeloid leukemia**,
with **14 registered clinical trials** and **20 publications** currently linked to this direction. Most of the trials are multi-drug regimens, so the contribution of mercaptopurine alone cannot be isolated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (Health Canada indication text is not available; taken from the original indication list) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold (research question) |

*Evidence level note:* No completed Phase 3 trial tests mercaptopurine specifically in myeloid leukemia. The completed Phase 3 trials are regimen-level studies in acute promyelocytic leukemia (APL) and acute myeloid leukemia (AML), so the level is assigned conservatively as L2.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, mercaptopurine is a thiopurine antimetabolite. Its active thioguanine nucleotides are incorporated into DNA and RNA and inhibit de novo purine synthesis, which is cytotoxic to rapidly dividing leukemic cells.

Its efficacy in ALL, where it is the standard oral maintenance partner of methotrexate, is well established. Myeloid leukemia is also a cancer of rapidly dividing blood cells, so a similar antimetabolite mechanism may apply. In practice, mercaptopurine is already used in some AML and APL regimens, for example oral maintenance with methotrexate in APL and in transplant-ineligible AML patients.

The evidence has an important limitation. It comes mostly from combination protocols, so mercaptopurine's own contribution cannot be separated from the other agents in each regimen.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin plus chemotherapy with or without arsenic trioxide, followed by maintenance with tretinoin versus tretinoin plus mercaptopurine and methotrexate in untreated APL |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | SWOG S0521: maintenance versus observation in low and intermediate risk APL; maintenance commonly includes mercaptopurine and methotrexate |
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | Active, not recruiting | 280 | Response-based, risk-stratified chemotherapy for AML in Down syndrome; mercaptopurine's role is not confirmed |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Unknown | 750 | ATRA plus idarubicin and intensive consolidation in APL, with randomized maintenance depending on minimal residual disease |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | Venetoclax plus 6-mercaptopurine in relapsed or refractory AML; very small and early-stage |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea plus valproic acid, or 6-mercaptopurine plus valproic acid, in AML or high-risk MDS unfit for standard therapy |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | Completed | 133 | Arsenic trioxide plus ATRA and idarubicin versus AIDA in high-risk APL; mercaptopurine is at most a maintenance component |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Completed | 276 | Arsenic trioxide plus ATRA versus ATRA and anthracycline chemotherapy (AIDA) in non-high-risk APL |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Completed | 106 | Risk-adapted treatment of childhood APL with arsenic trioxide during consolidation |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | Two multi-agent regimens with different cytarabine doses in newly diagnosed AML or myelodysplasia; mercaptopurine's role is not evident |

Four further registered trials are not listed here: NCT00551460, NCT02419755, NCT00047268 and NCT00276601. They have only indirect relevance to mercaptopurine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Oral maintenance with daily 6-mercaptopurine and weekly methotrexate in transplant-ineligible AML patients |
| [27275453](https://pubmed.ncbi.nlm.nih.gov/27275453/) | 2016 | Prospective pilot | South Asian J Cancer | Metronomic oral 6-mercaptopurine in elderly AML |
| [32459546](https://pubmed.ncbi.nlm.nih.gov/32459546/) | 2020 | Retrospective | Pediatr Hematol Oncol | Sequential cytarabine and 6-mercaptopurine in juvenile myelomonocytic leukemia |
| [38828002](https://pubmed.ncbi.nlm.nih.gov/38828002/) | 2024 | Cohort | Ther Adv Hematol | Intensive chemotherapy with dual induction and ALL-like consolidation in childhood AML |
| [22715121](https://pubmed.ncbi.nlm.nih.gov/22715121/) | 2012 | Cohort (Phase 2) | Blood | ATRA, idarubicin and arsenic trioxide as initial therapy in APL (APML4) |
| [12057059](https://pubmed.ncbi.nlm.nih.gov/12057059/) | 2000 | Review | Curr Treat Options Oncol | Overview of APL treatment with ATRA and consolidation chemotherapy |
| [33183436](https://pubmed.ncbi.nlm.nih.gov/33183436/) | 2021 | Review | J Nanosci Nanotechnol | 6-MP nanomedicine for leukemia treatment |
| [34442422](https://pubmed.ncbi.nlm.nih.gov/34442422/) | 2021 | Review | J Pers Med | NUDT15 polymorphisms and severe thiopurine toxicity |
| [2676034](https://pubmed.ncbi.nlm.nih.gov/2676034/) | 1989 | Review | Blood Rev | Purine metabolism as a target for leukemia chemotherapy |
| [3513537](https://pubmed.ncbi.nlm.nih.gov/3513537/) | 1986 | Clinical study | Am J Clin Oncol | Hydroxyurea plus 6-mercaptopurine in chronic granulocytic leukemia |

No randomized trial in the retrieved literature tests mercaptopurine alone in myeloid leukemia. The evidence consists of small cohorts, pilot studies and reviews.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02415275 | MERCAPTOPURINE TABLETS USP | Not specified | Not specified |
| 00004723 | PURINETHOL | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine antimetabolite, thiopurine class) |
| Myelosuppression Risk | High. The knowledge graph lists leukopenia, neutropenia, thrombocytopenia, agranulocytosis and anaemia as contraindicated conditions. Genetic variants in TPMT and NUDT15 can greatly increase this risk |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function (bilirubin, transaminases), renal function, TPMT/NUDT15 status |
| Handling Protection | Must follow cytotoxic drug handling regulations. Please refer to the package insert for details |

---

## Safety Considerations

- **Conditions flagged as contraindicated in the knowledge graph** (these come from a computational knowledge graph, not from label text): kidney disease, pancreatitis, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), leukopenia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), cholestasis (including benign recurrent and familial intrahepatic forms), pyoureter, and hepatosplenic T-cell lymphoma.
- **Drug Interactions**: 100 interactions were found in the DDI query, and the 20 reviewed include:
  - **Moderate**: mesalazine, balsalazide, olsalazine, sulfasalazine, naltrexone
  - **Minor**: levofloxacin
  - **Unknown severity**: calcitriol, pantoprazole, omeprazole, lansoprazole, doxycycline, morphine, metformin, rosiglitazone, vancomycin, prednisone, simvastatin, amphotericin B, hydrocortisone, potassium chloride
- Other clinically important interactions with allopurinol, febuxostat and methotrexate are noted in the repurposing rationale but were not in the 20 interactions reviewed here.

Official warnings and contraindications from the Canadian package insert were not available. Please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
- The TxGNN score is very high (99.94%) and mercaptopurine is already used in some AML and APL regimens. However, the supporting trials are regimen-level studies, and none isolates mercaptopurine's contribution in myeloid leukemia. The Phase 1 and 2 mercaptopurine-specific studies are very small.
- The package insert safety data are missing, and the high myelosuppression risk needs to be addressed before any clinical use.

**To proceed, the following is needed:**
- The Canadian package insert warnings and contraindications (blocking gap), to allow safety screening
- Mechanism of action data from DrugBank
- Results from mercaptopurine-specific studies, such as NCT05506332 and NCT06199557, or analyses of maintenance-phase arms in the APL trials
- A genotype-guided dosing plan (TPMT and NUDT15) and a myelosuppression and hepatotoxicity monitoring plan

---

### Other Predicted Indications (Brief)

- **Acute lymphoblastic leukemia and precursor lymphoblastic lymphoma/leukemia (scores 99.73% and 99.74%)**: These are mercaptopurine's established core use, not true repurposing. Both have L1 evidence and multiple Phase 3 protocols, and the suggested decision is *Proceed with Guardrails*: TPMT/NUDT15 testing (NUDT15 variants matter especially in East Asian populations), metabolite-guided dosing and interaction checks.
- **Small cell lung carcinoma (99.79%)**: Only a 1985 Phase 2 study and preclinical work exist. Hold.
- **Hodgkin lymphoma and primary pulmonary lymphoma**: The evidence is indirect, and the retrieved trials are mostly in ALL and non-Hodgkin lymphoma. Hold.
- **CLL/SLL subtypes, pulmonary blastoma and fetal adenocarcinoma of the lung**: These are model predictions only, with no trials or literature. Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

