---
layout: default
title: Mycophenolic Acid
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
---

# Mycophenolic Acid
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

# Mycophenolic Acid: From Organ Transplant Rejection to Hemoglobinopathy

## One-Sentence Summary

Mycophenolic acid (administered as its prodrug mycophenolate mofetil, MMF) is an immunosuppressant historically used to prevent organ transplant rejection.
The TxGNN model predicts it may be relevant to **Hemoglobinopathy**, but the **27 clinical trials** and **9 publications** identified largely describe MMF as a *background immunosuppressive/GVHD-prophylaxis agent* within hematopoietic stem cell transplantation (HSCT) for sickle cell disease and thalassemia — not as a direct disease-modifying treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Canadian regulatory data (drug unlicensed in Canada); literature within this evidence pack documents its established use as an immunosuppressant for prevention of organ transplant rejection |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed (Unlicensed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from regulatory sources (flagged as a High-severity data gap). Based on information within the evidence pack's own literature (e.g., PMID 9399601, 9646007), mycophenolic acid selectively inhibits inosine monophosphate dehydrogenase (IMPDH), blocking de novo purine synthesis and thereby suppressing T- and B-lymphocyte proliferation. This mechanism underlies its established use, in combination with calcineurin inhibitors and corticosteroids, to prevent solid-organ transplant rejection.

Hemoglobinopathies such as sickle cell disease and thalassemia major have no pharmacological relationship to lymphocyte proliferation — their only connection to MMF's mechanism is indirect: allogeneic HSCT is a curative option for severe hemoglobinopathy, and MMF is a standard component of the post-transplant GVHD-prophylaxis regimen (typically alongside tacrolimus/cyclosporine) in those transplants.

This is an important caveat flagged directly in the evidence pack's own rationale: the high TxGNN score most likely reflects that "MMF frequently co-occurs with hemoglobinopathy in transplant-trial contexts," a **confounding relationship**, rather than a genuine drug-disease treatment signal. No evidence in this pack shows MMF treating hemoglobinopathy pathology itself (e.g., abnormal hemoglobin production or red cell membrane defects) — its role throughout is adjunctive/prophylactic within HSCT.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02776202](https://clinicaltrials.gov/study/NCT02776202) | Phase 2 | Unknown | 15 | HLA-identical sibling BMT with reduced-intensity conditioning for severe SCD; MMF likely part of background immunosuppression, not the primary study drug |
| [NCT02435901](https://clinicaltrials.gov/study/NCT02435901) | Phase 1/2 | Completed | 29 | Allogeneic HSCT with reduced-intensity conditioning for high-risk SCD/β-thalassemia major, combined with standard immunosuppressive medications |
| [NCT01279616](https://clinicaltrials.gov/study/NCT01279616) | Phase 2 | Terminated | 8 | Pilot unrelated-donor HSCT using an immunosuppressive/myeloablative regimen for severe SCD; small sample, incomplete results |
| [NCT00029380](https://clinicaltrials.gov/study/NCT00029380) | Phase 2 | Completed | 30 | Sibling cord blood banking and transplantation program for hemoglobinopathies/thalassemia |
| [NCT03263559](https://clinicaltrials.gov/study/NCT03263559) | Phase 2 | Completed | 95 | Haploidentical BMT with reduced-intensity conditioning for symptomatic SCD (BMTCTN1507); evaluated efficacy/toxicity |
| [NCT03121001](https://clinicaltrials.gov/study/NCT03121001) | Phase 2 | Recruiting | 50 | HLA-haploidentical SCT with TBI/fludarabine/cyclophosphamide conditioning for aggressive SCD; primary endpoint is Day+60 engraftment |
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Abatacept + cyclosporine + MMF as GVHD prophylaxis in pediatric HSCT for non-malignant disease; MMF is standard-of-care background, not the study drug |
| [NCT02342145](https://clinicaltrials.gov/study/NCT02342145) | Phase 4 | Completed | 205 | Basiliximab for acute GVHD prevention in unrelated allogeneic HSCT for thalassemia major; MMF used as background regimen |
| [NCT01850108](https://clinicaltrials.gov/study/NCT01850108) | N/A | Unknown | 26 | Non-myeloablative conditioning with HLA-matched/mismatched BMT for SCD and other hemoglobinopathies |
| [NCT02678143](https://clinicaltrials.gov/study/NCT02678143) | Phase 1 | Terminated | 1 | Pilot nonmyeloablative mismatched HSCT for severe SCD; terminated after enrolling only 1 participant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Cohort | Transplantation and Cellular Therapy | MMF "immunosuppression boost" evaluated for stabilizing mixed chimerism after HSCT in thalassemia; retrospective outcomes analysis |
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Cohort/Dosing study | European Journal of Drug Metabolism and Pharmacokinetics | Population PK model to guide off-label MMF dosing in pediatric thalassemia patients undergoing HSCT |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Cohort | Biology of Blood and Marrow Transplantation | Alternative-donor HSCT with post-transplant cyclophosphamide for nonmalignant disorders, including hemoglobinopathies |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Cohort | Biology of Blood and Marrow Transplantation | Stable long-term donor engraftment following reduced-intensity HCT for sickle cell disease (n=7) |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Cohort | Hematology (Amsterdam) | Risk factors for pure red cell aplasia after major ABO-incompatible allo-HSCT |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Cohort (Phase 1 trial) | Biology of Blood and Marrow Transplantation | Unrelated umbilical cord blood transplant with reduced-intensity conditioning for SCD |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Cohort | Biology of Blood and Marrow Transplantation | Outcomes of unrelated-donor SCT using post-transplant cyclophosphamide plus tacrolimus/MMF GVHD prophylaxis for severe SCD |
| [15126382](https://pubmed.ncbi.nlm.nih.gov/15126382/) | 2004 | Review | Genetics | General review on the genetics–medicine interface; background context only, not disease-specific |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case report (adverse event) | Journal of Perinatology | Neonatal anemia and hydrops fetalis after maternal MMF use in pregnancy — a safety signal, not efficacy evidence |

---

## Canada Market Information

This drug currently holds **no Canadian market authorization (DIN)** — it is unlicensed in Canada, so no product/dosage-form/indication records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data are currently available in this evidence pack; retrieval of the Canadian product monograph is a **blocking** gap (see Conclusion below) that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap exists: no product-label warnings/contraindications are available, which by itself prevents any preliminary safety assessment (S1).
- The drug is unlicensed in Canada (0 DINs), and the mechanistic rationale for hemoglobinopathy is explicitly flagged as likely **confounded** — MMF's role in the supporting trials/literature is as a background GVHD-prophylaxis agent within HSCT, not as a direct treatment for hemoglobinopathy pathology. Evidence level is L3 (observational/cohort only), decision stage S1 ("Research Question"), with no completed RCT directly testing MMF against hemoglobinopathy.

**To proceed, the following is needed:**
- Canadian product monograph / label warnings and contraindications (resolves the blocking gap, DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Clarification of whether MMF's association with hemoglobinopathy outcomes reflects a direct treatment effect or purely an adjunctive/prophylactic role within HSCT
- If pursued further, reframing the indication as "adjunctive immunosuppression in HSCT for hemoglobinopathy" rather than a standalone disease-modifying indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

