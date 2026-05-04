---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cyclophosphamide: From Cytotoxic Alkylating Agent to Myeloid Leukemia Treatment

## One-Sentence Summary

Cyclophosphamide (DB00531) is a DNA-alkylating cytotoxic agent historically used across a wide range of malignancies and as a preparative conditioning regimen for haematopoietic stem cell transplantation (HSCT).
The TxGNN model predicts it may be effective for **Myeloid Leukemia** — including acute myeloid leukemia (AML) — with **39 clinical trials** and **20 publications** currently supporting this direction.
Evidence is primarily derived from its established role in myeloablative conditioning (e.g., the BuCy regimen) and post-transplant GvHD prophylaxis (PTCy), which together constitute one of the best-supported repurposing signals in this dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cytotoxic chemotherapy / HSCT myeloablative conditioning (no Canada DIN on file) |
| Predicted New Indication | Myeloid Leukemia (AML) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Cyclophosphamide is a nitrogen mustard–class alkylating agent. Upon metabolic activation by hepatic cytochrome P450 enzymes (primarily CYP2B6), it generates phosphoramide mustard, which forms inter-strand DNA crosslinks that block replication and trigger apoptosis in rapidly dividing cells. Detailed formal MOA data from DrugBank is not available in this Evidence Pack; however, cyclophosphamide's mechanism is extensively characterised in the published literature and is directly applicable to AML biology.

In the context of myeloid leukemia, cyclophosphamide is a backbone component of the BuCy (Busulfan + Cyclophosphamide) myeloablative conditioning (MAC) regimen used prior to allogeneic HSCT. This dual role — cytoreduction of residual leukemic blasts and creation of marrow space for donor engraftment — is mechanistically distinct from simple chemotherapy and explains why its therapeutic signal is so robust in AML. Post-transplant cyclophosphamide (PTCy), administered at high dose on days +3/+4 after transplant, further leverages its selective toxicity against alloreactive T cells to prevent graft-versus-host disease (GvHD), while preserving graft-versus-leukemia (GvL) activity.

AML and the classical indications for cyclophosphamide (lymphoma, multiple myeloma) share a common biological denominator: uncontrolled clonal proliferation of haematopoietic cells. The fact that multiple international Phase 3 RCTs — including the ongoing 700-patient pediatric AML trial (NCT02724163) — explicitly incorporate cyclophosphamide in their backbone regimens strongly validates TxGNN's prediction and supports the L1 evidence rating.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | Recruiting | 700 | International multicenter RCT comparing gemtuzumab ozogamicin doses added to cytarabine ± cyclophosphamide induction in children with AML; highest-level direct evidence |
| [NCT00002534](https://clinicaltrials.gov/study/NCT00002534) | Phase 3 | Completed | N/A | Randomized trial of unmodified vs T-cell–depleted HLA-identical BMT for acute leukemias; cyclophosphamide is the conditioning backbone |
| [NCT00152139](https://clinicaltrials.gov/study/NCT00152139) | Phase 3 | Completed | 33 | Matched unrelated donor PBSC or BM transplant for hematological malignancies including AML using cyclophosphamide-based conditioning |
| [NCT01707004](https://clinicaltrials.gov/study/NCT01707004) | Phase 2 | Completed | 20 | Decitabine + TBI → BMT + high-dose cyclophosphamide for relapsed/refractory AML; direct endpoint data available |
| [NCT00553202](https://clinicaltrials.gov/study/NCT00553202) | Phase 2 | Completed | 158 | KIR-incompatible unrelated donor HSCT for AML with monosomy 7, FLT3-ITD, or refractory/relapsed disease; cyclophosphamide in conditioning |
| [NCT02094794](https://clinicaltrials.gov/study/NCT02094794) | Phase 2 | Active, not recruiting | 108 | Total marrow + lymphoid irradiation + cyclophosphamide + etoposide as conditioning for high-risk ALL/AML |
| [NCT02294552](https://clinicaltrials.gov/study/NCT02294552) | Phase 2 | Completed | 200 | High-dose post-transplant cyclophosphamide as GvHD prophylaxis after allo-HSCT; risk-adapted single-agent vs combination strategy |
| [NCT00849147](https://clinicaltrials.gov/study/NCT00849147) | Phase 2 | Completed | 55 | Non-myeloablative conditioning + haploidentical BMT (PTCy) for leukemia/lymphoma; effective GvHD suppression with preserved GvL |
| [NCT05115630](https://clinicaltrials.gov/study/NCT05115630) | Phase 2 | Completed | 24 | "Off-the-shelf" NK cell (KDS-1001) + allo-SCT to decrease AML/MDS/CML relapse; cyclophosphamide as lymphodepletion agent |
| [NCT03766126](https://clinicaltrials.gov/study/NCT03766126) | Phase 1 | Active, not recruiting | 22 | Anti-CD123 CAR-T (lentivirally transduced) for relapsed/refractory AML; cyclophosphamide used for standard lymphodepletion pre-infusion |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | RCT / Multi-centre comparative | *Future Oncology* | BuCy vs FluBu myeloablative conditioning for allo-HSCT in AML: BuCy is the historical standard; FluBu shows similar efficacy with less toxicity |
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / Network meta-analysis | *Bone Marrow Transplantation* | Bayesian network meta-analysis of MAC regimens (including BuCy) in adult AML undergoing allo-HSCT in complete remission; optimal regimen remains context-dependent |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Phase 2 / Prospective cohort | *Transplant Immunology* | Cladribine + busulfan + cyclophosphamide as intensive conditioning for R/R AML prior to allo-HSCT; demonstrates feasibility and efficacy |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | Prospective case series | *Pediatric Hematology and Oncology* | Clofarabine + cyclophosphamide + etoposide in 17 children with R/R AML: 41% overall response rate including 4 CRs |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Retrospective cohort | *Leukemia & Lymphoma* | High-dose cyclophosphamide (60 mg/kg) for cytoreduction in AML with hyperleukocytosis (WBC ≥50×10⁹/L): rapid WBC reduction with manageable toxicity in 27 patients |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | Retrospective comparative | *Hematol Oncol Stem Cell Ther* | BuCy vs BuFlu myeloablative conditioning for allo-HCT in AML/MDS: comparable survival outcomes; quality-of-life differences noted |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Retrospective cohort | *Int J Mol Sci* | PTCy after matched sibling/unrelated donor HSCT in pediatric AML: first published data in this specific population; acceptable GvHD rates and survival |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Retrospective cohort | *Cytotherapy* | Prognostic factors in haploidentical HSCT with PTCy for AML: large multi-centre EBMT-based analysis confirming PTCy safety and efficacy |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Retrospective cohort | *Bone Marrow Transplantation* | 1,823-patient EBMT analysis: impact of MAC vs RIC conditioning intensity on transplant outcomes in AML patients receiving PTCy-based GvHD prophylaxis |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Retrospective cohort | *Haematologica* | Genetic risk classification in 217 AML patients undergoing allo-HCT with MAC + PTCy: 2-year OS 77%, EFS 72%; strong evidence for PTCy efficacy across genetic risk categories |

---

## Cytotoxicity

Cyclophosphamide is an antineoplastic alkylating agent (nitrogen mustard class) with well-established cytotoxic properties.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — alkylating agent (nitrogen mustard / oxazaphosphorine class) |
| Myelosuppression Risk | **High** — dose-dependent leukopenia, neutropenia, and thrombocytopenia are the primary dose-limiting toxicities, especially at myeloablative doses (e.g., 60–120 mg/kg); nadir typically at days 7–14 |
| Emetogenicity Classification | **Moderate to High** — particularly at intravenous doses ≥1,000 mg/m²; antiemetic prophylaxis (NK1-RA + 5-HT3-RA + dexamethasone) required |
| Monitoring Items | CBC with differential (at least twice weekly during induction); serum creatinine and electrolytes; liver function tests (LFTs); urinalysis for haematuria (haemorrhagic cystitis risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations — PPE (gloves, gown, eye protection), closed-system drug transfer devices for preparation; hazardous waste disposal required |

**Additional notes:** Haemorrhagic cystitis (caused by urinary metabolite acrolein) can be prevented with adequate hydration and MESNA co-administration, especially at doses >1 g/m². Cardiac toxicity is possible at very high doses (>100 mg/kg).

---

## Safety Considerations

Formal TFDA/Health Canada package insert warnings and contraindications data are not available in this Evidence Pack. Based on the evidence retrieved:

- **Drug Interactions**: No DDI data was identified in this dataset. Cyclophosphamide is metabolised primarily by CYP2B6 and to a lesser extent CYP3A4; clinically significant interactions with CYP2B6 inducers (e.g., rifampin) and inhibitors are expected.

Please refer to the approved package insert for complete warnings, contraindications, and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide in myeloid leukemia is supported by the strongest available evidence tier (L1), with at least one ongoing 700-patient international Phase 3 RCT and a completed Phase 3 randomised trial, multiple Phase 2 completions, and 20 peer-reviewed publications including systematic reviews and RCTs. Its use in AML-directed HSCT conditioning (BuCy) and as post-transplant GvHD prophylaxis (PTCy) is internationally recognised and guideline-endorsed.

**To proceed, the following is needed:**

- **Canada regulatory filing**: No DINs currently exist in Canada; a New Drug Submission or supplemental NDS specifying the AML/HSCT indication would be required
- **MOA data supplement**: Retrieve full DrugBank MOA profile (CYP2B6 activation pathway, phosphoramide mustard mechanism) to complete mechanistic documentation
- **Safety data supplement**: Download and parse the TFDA and Health Canada monograph PDFs to populate key warnings, contraindications, and DDI profile
- **Indication sub-classification**: "Myeloid leukemia" encompasses AML, CML, and MDS with varying treatment paradigms — define the precise target indication (e.g., AML in HSCT-eligible patients, AML with hyperleukocytosis, PTCy GvHD prophylaxis) before advancing
- **Comparator benchmarking**: Compare BuCy vs BuFlu (fludarabine-busulfan) positioning, given that FluBu may offer comparable efficacy with reduced toxicity per the 2025 literature

> **YMYL Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

