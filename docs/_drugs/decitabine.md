---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 1
---

# Decitabine
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

# Decitabine: From Myelodysplastic Syndrome to Refractory Cytopenia of Childhood

## One-Sentence Summary

Decitabine is a DNA hypomethylating agent (DNMT inhibitor) widely used in adult myelodysplastic syndrome (MDS) treatment, and referenced in the supporting literature as used in pediatric MDS settings. The TxGNN model predicts it may be effective for **Refractory Cytopenia of Childhood (RCC)**, a rare pediatric subtype of MDS, with **0 registered clinical trials** and **1 observational publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myelodysplastic Syndrome (based on clinical context; no formal Taiwan regulatory records available) |
| Predicted New Indication | Refractory Cytopenia of Childhood (RCC) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 (1 retrospective single-center observational study) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, decitabine belongs to the DNA hypomethylating agent class. It inhibits DNA methyltransferase (DNMT), leading to hypomethylation of tumor suppressor gene promoters and restoration of normal cellular differentiation. Its efficacy in myelodysplastic syndrome has been established in adult populations, and mechanistically this may be applicable to refractory cytopenia of childhood.

Refractory Cytopenia of Childhood (RCC) is classified under the 2016 WHO category of pediatric MDS. Like adult MDS, RCC is characterized by ineffective hematopoiesis and dysplastic bone marrow morphology. The underlying epigenetic dysregulation makes it a biologically plausible target for hypomethylating agents such as decitabine. The supporting publication specifically reports decitabine use as a bridge to allogeneic hematopoietic stem cell transplantation (allo-HSCT) in children with MDS — directly encompassing RCC cases.

Given the rarity of RCC and the lack of approved pediatric-specific therapies, the high TxGNN prediction score (99.03%) is clinically plausible. The model's prediction aligns with the existing single-center clinical experience, suggesting that mechanistic extrapolation from adult MDS to pediatric RCC is scientifically grounded, though rigorous prospective evidence remains limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Decitabine in Refractory Cytopenia of Childhood.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Observational (single-center retrospective) | BMC Pediatrics | 10-year single-center experience with decitabine-combined minimally myelosuppressive regimen (DAC + MMR) as bridge to allo-HSCT in children with MDS, including RCC cases; reports outcomes with this novel pre-transplant approach |

---

## Taiwan Market Information

Decitabine is currently **not marketed in Taiwan**. No drug licenses or approved indications on record.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA Hypomethylating Agent (nucleoside analogue / DNMT inhibitor) |
| Myelosuppression Risk | High — decitabine causes dose-dependent and cumulative myelosuppression; neutropenia, thrombocytopenia, and anemia are among the most common and serious adverse effects |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Complete Blood Count with differential (CBC-diff), liver function tests, renal function (serum creatinine), serum electrolytes; in pediatric patients, additional growth and developmental monitoring is advisable |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in biological safety cabinet, use of personal protective equipment (PPE), and safe disposal per institutional cytotoxic waste protocols are required |

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack and represent a blocking data gap that must be resolved before clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base is currently insufficient for a repurposing decision: there are no registered clinical trials specific to decitabine in RCC, only one retrospective single-center observational study exists, and critical safety data (warnings, contraindications, drug interactions) are entirely absent. Additionally, decitabine is not marketed in Taiwan, presenting a significant access and regulatory pathway barrier.

**To proceed, the following is needed:**

- **Safety data resolution (Blocking):** Obtain and parse the full prescribing information (package insert / SmPC) to extract contraindications, black box warnings, and drug interactions — this is a prerequisite for any safety evaluation
- **MOA documentation (High priority):** Retrieve structured mechanism of action data from DrugBank API (DB01262) to support mechanistic linkage analysis
- **Expanded literature review:** Conduct a broader PubMed search for decitabine use in pediatric MDS subtypes (including RCC, RCMD-RS) to identify additional observational evidence or case series
- **Clinical trial landscape review:** Search ClinicalTrials.gov and ICTRP with broader terms (e.g., "decitabine AND pediatric MDS", "hypomethylating agent AND childhood MDS") to identify any ongoing or completed trials not captured under the RCC-specific query
- **Regulatory pathway assessment:** Evaluate whether an orphan drug designation or pediatric compassionate use pathway is feasible in Taiwan for this rare pediatric indication
- **Expert consultation:** Engage pediatric hematology-oncology specialists to assess clinical feasibility given RCC's rarity and existing transplant-first treatment paradigm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

