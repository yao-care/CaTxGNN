---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma / Systemic ALCL to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (BV) is an anti-CD30 antibody-drug conjugate (ADC) approved globally for classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma (sALCL), though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **3 relevant clinical trials** and **several publications** providing supporting evidence.
Applicability is conditional on CD30 expression in individual cases, which is heterogeneous in follicular lymphoma and most prominent in relapsed or transformed disease.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Classical Hodgkin Lymphoma; Systemic Anaplastic Large Cell Lymphoma (sALCL) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current evidence pack. Based on published knowledge, brentuximab vedotin is an antibody-drug conjugate (ADC) comprising an anti-CD30 monoclonal antibody (brentuximab) chemically linked to monomethyl auristatin E (MMAE), a potent microtubule-disrupting agent. Upon binding to CD30-expressing tumor cells, the complex is internalized and MMAE is released intracellularly, disrupting mitosis and triggering apoptosis. This targeted delivery mechanism has been validated in classical Hodgkin lymphoma — where Reed-Sternberg cells uniformly overexpress CD30 — and in systemic ALCL.

The theoretical bridge to follicular lymphoma (FL) rests on the observation that a subset of FL cases, particularly in the relapsed, refractory, or histologically transformed setting, can express CD30 on tumor cells. This aberrant surface expression creates a targetable window for BV, even though CD30 positivity in de novo FL is far lower than in HL or ALCL. The mechanistic rationale is therefore valid but population-restricted: BV's activity in FL is expected to correlate tightly with the degree of CD30 expression, which requires prospective immunohistochemical testing to identify eligible patients.

The TxGNN prediction is further strengthened by the existence of a dedicated prospective Phase 2 trial (NCT04587687) designed explicitly for CD30+ relapsed/refractory FL, and by case-level evidence showing complete responses in FL that transformed to CD30+ lymphoma after BV-based therapy. The shared histological category of B-cell lymphoma between HL and FL also provides a degree of biological similarity that underpins model plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + bendamustine for relapsed/refractory follicular lymphoma; the only dedicated Phase 2 trial targeting CD30+ FL directly; results not yet published |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline therapy for CD30+ and/or EBV+ lymphomas including FL subgroup; terminated early but provides safety and preliminary efficacy signals across B-cell histologies |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized trial of rituximab + bendamustine ± BV for relapsed/refractory CD30+ DLBCL; terminated early with 25 cases enrolled, offering indirect evidence on BV activity in CD30+ B-cell lymphomas |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf Journal of Oncology | Grade I FL transformed to CD30+ ALK1− ALCL; complete response achieved with BV + high-dose methotrexate; demonstrates BV activity in FL after transformation to a CD30+ phenotype |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Review of immunotherapy in indolent NHL including FL; discusses emerging targeted agents and the rationale for CD30-directed therapy in select NHL subtypes |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Clinical Trial/Cohort | Blood Advances | LYSA Phase 2 study of BV + gemcitabine followed by BV maintenance in R/R PTCL patients with ≥5% CD30+ cells; provides contemporary data on BV efficacy in CD30-variable lymphomas |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Current treatment landscape for nodal PTCLs; describes BV+CHP as standard of care for CD30+ disease and contextualizes CD30 expression thresholds for treatment selection |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Real-World Study | Advances in Therapy | Retrospective real-world analysis of BV + CHP in untreated CD30+ NHL (including PTCL-TFH and ALCL); high overall remission rates observed across CD30+ B- and T-cell histologies |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC) with cytotoxic microtubule-disrupting payload (MMAE) |
| Myelosuppression Risk | Moderate to High (neutropenia is among the most common grade 3/4 adverse events; febrile neutropenia reported in clinical trials) |
| Emetogenicity Classification | Low to Moderate (MMAE-based ADCs generally carry low emetogenic potential compared to conventional cytotoxic chemotherapy) |
| Monitoring Items | CBC with differential (prior to each cycle), liver function tests, renal function, peripheral neuropathy assessment (sensory and motor), pulmonary function if respiratory symptoms arise |
| Handling Protection | Required — must be prepared and administered under cytotoxic drug handling regulations; MMAE payload constitutes a hazardous agent |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
An active, dedicated Phase 2 trial (NCT04587687) targeting CD30+ relapsed/refractory follicular lymphoma is currently recruiting, demonstrating that the scientific community has endorsed this repurposing hypothesis sufficiently to fund prospective investigation. Combined with mechanistic plausibility (CD30 expression in transformed/relapsed FL) and indirect Phase 2 data from related B-cell lymphoma studies, there is sufficient evidence to advance this candidate into structured evaluation — but only for the CD30-positive FL subpopulation.

**To proceed, the following is needed:**

- **CD30 expression testing**: Prospective immunohistochemistry (IHC) to confirm CD30 positivity in candidate patients; BV is unlikely to benefit CD30-negative FL cases
- **Results from NCT04587687**: The ongoing Phase 2 trial is the critical data gap; monitoring its outcomes should be the first priority before any independent clinical expansion
- **Full mechanism of action documentation**: DrugBank API query to formally document BV's MOA for regulatory submission purposes
- **Safety data retrieval**: Download and parse the full prescribing information/package insert (Health Canada or FDA) to populate the currently empty key warnings and contraindications fields
- **Drug interaction review**: Conduct formal DDI screening for the Canadian formulary context, particularly interactions involving MMAE metabolism (CYP3A4 pathway)
- **Canadian regulatory pathway review**: Assess whether Adcetris (BV) has a pending or completed Health Canada submission, as global approvals (FDA, EMA) exist and a regulatory bridging strategy may expedite Canadian access

---

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

