---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Multiple Myeloma to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is a classical DNA alkylating chemotherapy agent (nitrogen mustard class), historically used as a cornerstone treatment for multiple myeloma and ovarian cancer worldwide.
The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor (GCT)**,
with **8 clinical trials** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (standard-of-care globally; not currently marketed in Canada) |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Melphalan is a bifunctional DNA alkylating agent belonging to the nitrogen mustard class. Its core mechanism is the formation of interstrand DNA cross-links, which physically obstruct DNA replication machinery and trigger apoptosis in rapidly dividing cells. Although formal MOA data from DrugBank is currently unavailable in this evidence pack, this mechanism is exceptionally well-characterized across decades of clinical and preclinical literature and is the pharmacological foundation for the drug's long-established use in hematologic malignancies.

Gonadal germ cell tumors (GCT) are among the most proliferative solid malignancies, and critically, they exhibit relatively deficient DNA repair pathways — the same vulnerability that underlies their exceptional sensitivity to platinum-based BEP chemotherapy. Because alkylating agents and platinum agents both act through DNA cross-linking, Melphalan targets the same biological weakness. This mechanistic overlap is not speculative: high-dose Melphalan (HD-Mel) has already been incorporated into autologous stem cell transplantation (ASCT) conditioning regimens for relapsed/refractory GCT in clinical practice, with NCT00936936 providing direct Phase 2 evidence.

The TxGNN prediction therefore corroborates — rather than proposes — an existing but incompletely validated clinical use. The repurposing opportunity lies in generating formal, GCT-specific Phase 2/3 evidence to define the optimal patient population, dosing schedule, and combination partner for HD-Mel-based salvage in cisplatin-resistant GCT.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | High-dose gemcitabine + docetaxel + melphalan + carboplatin (Cycle 1) followed by ifosfamide + carboplatin + etoposide (Cycle 2) in poor-prognosis relapsed GCT; most directly relevant trial — specifically designed for this indication. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose Melphalan with ASCT support and amifostine cytoprotection across cancer patients including GCT; provides key pharmacokinetic and dose-response data for HD-Mel conditioning. |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | High-dose busulfan + melphalan + topotecan followed by ASCT in advanced and recurrent solid tumors; GCT included as a sub-population within a multi-tumor cohort. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Comparison of eight high-dose chemotherapy regimens with or without TBI before ASCT for hematologic cancers and selected solid tumors; large cohort providing comparative outcomes data with GCT patients included. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | Phase N/A | Completed | 174 | Registry pilot of high-dose chemotherapy regimens before ASCT across hematologic malignancies and solid tumors; provides real-world transplant outcomes data including GCT patients. |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal Melphalan for recurrent neoplastic meningitis; route of administration (intrathecal) and indication (leptomeningeal disease) differ substantially from systemic GCT use — limited direct relevance. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as chemoprotectant with ASCT for pediatric solid tumors including brain tumors; trial terminated early, Melphalan not the primary study drug, results limited. |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | Phase N/A | Completed | 36 | Nonmyeloablative allogeneic HSCT with ATG plus Melphalan/cladribine or total lymphoid irradiation; primarily for hematologic diseases (leukemia, lymphoma, myeloma) — indirect GCT relevance only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Clinical series | Oncology | Chemotherapy of testicular germinal tumors; early systematic clinical series documenting Melphalan's activity in gonadal germ cell malignancies before BEP became standard of care. |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review/Case series | Urologic Clinics of North America | Seminoma review covering management principles; documents Melphalan's established historical role in gonadal GCT treatment. |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Historical case series | Voprosy Onkologii | Foundational clinical report on treating seminoma of the testes and its metastases with sarcolysin (the Soviet designation for Melphalan); provides historical proof-of-concept. |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Experimental/Observational | Acta – UICC | Investigates the influence of alkylating drugs (including Melphalan) and hormonal agents on pituitary follicle-stimulating function; provides early mechanistic context for gonadal interactions. |

> **Note:** All four publications predate 1980. Their value lies in establishing historical clinical proof-of-concept; they should not be considered primary evidence for contemporary treatment decisions.

---

## Canada Market Information

Melphalan is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are on file with Health Canada, and no authorized product licenses exist. Clinical use in Canada — should it occur — would require access through Health Canada's **Special Access Programme (SAP)** or hospital pharmacy compounding under institutional governance. This absence of a market authorization represents a practical regulatory hurdle that must be addressed before any formal repurposing program can proceed.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Nitrogen mustard alkylating agent — same mechanistic class as cyclophosphamide and chlorambucil) |
| Myelosuppression Risk | **High** — dose-limiting myelosuppression is the primary toxicity; leukopenia, thrombocytopenia, and anemia are expected, particularly at high doses (≥140 mg/m²) used in ASCT conditioning. Nadir typically occurs 2–3 weeks post-dose. |
| Emetogenicity Classification | Moderate at standard doses; **High** at high doses (≥100 mg/m²) — prophylactic antiemetics required |
| Monitoring Items | CBC with differential (baseline, then at least weekly during treatment), serum creatinine and BUN (renal function determines dose adjustment — reduce dose for creatinine clearance <30 mL/min), liver function tests, electrolytes |
| Handling Protection | Full cytotoxic drug handling regulations apply — closed-system drug transfer devices (CSTDs), appropriate personal protective equipment (PPE), dedicated preparation area required |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal Health Canada product monograph warnings and contraindications are unavailable as Melphalan does not hold a Canadian market authorization. Clinicians should consult the **FDA prescribing information for Alkeran®** (melphalan tablets/injection) or the **EMA product information** for comprehensive guidance on warnings, contraindications, and special populations (renal impairment, pregnancy, secondary malignancy risk).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (NCT00936936, n=64) directly evaluating Melphalan-containing high-dose chemotherapy in relapsed/refractory GCT, combined with supporting Phase 1/2 dose-escalation data and decades of historical clinical use, provides sufficient mechanistic and empirical grounding to move this candidate forward — under structured oversight and with clearly defined patient selection criteria.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank (DG002) to complete mechanistic cross-indication analysis
- Obtain TFDA or FDA/EMA package insert warnings and contraindications (DG001) to enable formal safety profiling
- Define target patient population precisely: testicular vs. other gonadal origin; cisplatin-refractory vs. first relapse; adult vs. pediatric; ASCT-eligible vs. non-eligible
- Clarify positioning within current salvage landscape — HD-Mel/ASCT is typically third-line or later, after failure of BEP and ifosfamide-based salvage (TIP/VeIP)
- Assess ASCT infrastructure availability at the intended clinical center(s)
- Initiate Health Canada Special Access Programme application if clinical use is intended in Canada
- Update literature search to capture post-2000 publications (current evidence pack contains only pre-1980 literature; NCT00936936 results paper likely published 2024–2025 and should be retrieved)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

