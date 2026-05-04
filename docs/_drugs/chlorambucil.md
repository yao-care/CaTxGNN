---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil: From Chronic Lymphocytic Leukemia to Pregerminal Center CLL/SLL

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with a decades-long history of use in treating Chronic Lymphocytic Leukemia (CLL) and other B-cell malignancies worldwide, though it is not currently registered in Canada.
The TxGNN model predicts it may be effective for **Pregerminal Center CLL/SLL** (the IGHV-unmutated, high-risk molecular subtype), with a prediction score of **99.72%** and an Evidence Level of **L1**, reflecting chlorambucil's established role as the standard comparator arm in major Phase 3 RCTs that enrolled this specific CLL population.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada; globally indicated for Chronic Lymphocytic Leukemia (CLL), non-Hodgkin's lymphoma, and Hodgkin's disease |
| Predicted New Indication | Pregerminal Center CLL/SLL (IGHV-unmutated subtype) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, chlorambucil is a bifunctional alkylating agent of the nitrogen mustard class. It forms covalent DNA interstrand and intrastrand cross-links, disrupting DNA replication and transcription. This direct cytotoxic mechanism is particularly effective against slowly proliferating malignant B-lymphocytes — making CLL its canonical clinical application for over 60 years.

Pregerminal center CLL/SLL is defined by unmutated immunoglobulin heavy-chain variable-region (IGHV) genes, indicating that the malignant clone originated before undergoing the germinal center reaction. This molecular subtype is biologically distinct: it exhibits greater genomic instability, more aggressive clinical behavior, and historically lower response rates to alkylating agents compared to the IGHV-mutated subtype. Despite this relative resistance, chlorambucil has been selected as the standard-of-care control arm in landmark Phase 3 trials specifically because it represents the established backbone treatment for untreated CLL regardless of IGHV status — including the CLL11 (obinutuzumab + chlorambucil vs. chlorambucil alone), COMPLEMENT (ofatumumab + chlorambucil), and RESONATE-2 (ibrutinib vs. chlorambucil) studies.

The TxGNN prediction at this molecular level is therefore not a novel repurposing in the traditional sense, but rather a formal characterization of chlorambucil's activity within a molecularly defined high-risk subgroup. The model's high confidence score (99.72%) reflects the topological proximity of this disease node to established CLL indications within the biomedical knowledge graph. The practical significance lies in patient selection — understanding that this subtype responds less well to chlorambucil monotherapy, and should preferentially receive it in combination with a CD20 monoclonal antibody when a chlorambucil-based regimen is chosen.

---

## Clinical Trial Evidence

No clinical trials specifically targeting the pregerminal center (IGHV-unmutated) CLL/SLL subtype with chlorambucil were returned in this evidence pack's targeted query. The L1 evidence classification reflects the broader CLL evidence base, particularly IGHV-status subgroup analyses from the CLL11, COMPLEMENT, and RESONATE-2 Phase 3 trials, which are not captured in the targeted query below.

Currently no related clinical trials registered for this specific molecular subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Narrative Review | Nederlands Tijdschrift voor Geneeskunde | Describes the two newly identified CLL subtypes — pregerminal center (IGHV-unmutated) and post-germinal center (IGHV-mutated) — and their distinct clinical significance. Notes that ~50% of Binet stage A patients will eventually require treatment and that unmutated IGHV status predicts poorer prognosis, supporting the rationale for molecular subtype-specific treatment strategies |

---

## Canada Market Information

Chlorambucil is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on record with Health Canada. The drug is commercially available in other major jurisdictions — including the United States (Leukeran®, GlaxoSmithKline) and across Europe — where it holds approved indications for CLL, Hodgkin's disease, and non-Hodgkin's lymphoma.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard alkylating agent (bifunctional, cell-cycle non-specific) |
| Myelosuppression Risk | **High** — Bone marrow suppression is the primary dose-limiting toxicity; cumulative neutropenia, thrombocytopenia, and anemia are expected with prolonged use; may be severe and irreversible at high doses |
| Emetogenicity Classification | Low to moderate — oral formulation; lower emetogenic potential than intravenous alkylating agents, but nausea and vomiting may still occur |
| Monitoring Items | CBC with differential (at minimum weekly during therapy, and for ≥3 weeks after each cycle); liver function tests; renal function; signs of infection (especially in immunocompromised CLL patients) |
| Handling Protection | Must be handled under cytotoxic drug handling regulations; avoid skin, mucous membrane, and eye contact; dispose as cytotoxic waste; pregnant staff should not handle |

---

## Safety Considerations

Safety data from the Canadian regulatory database is unavailable, as chlorambucil holds no current Health Canada registration. Please refer to the US FDA prescribing information (Leukeran® label) or the EMA-approved product monograph for complete warnings, contraindications, and drug interaction information.

Key risks documented in published literature include:

- **Secondary malignancies**: Long-term use is associated with a significantly elevated risk of acute myeloid leukemia (AML) and other secondary malignancies. Retrospective cohort data from Hodgkin's disease patients treated with chlorambucil-containing regimens show standardized incidence ratios (SIR) for acute non-lymphocytic leukemia of 31.3 (PMID [1392790](https://pubmed.ncbi.nlm.nih.gov/1392790/)) and elevated risks for lung and other solid tumors (PMID [9000608](https://pubmed.ncbi.nlm.nih.gov/9000608/)).
- **Myelosuppression**: Cumulative bone marrow toxicity; risk increases with total dose and treatment duration.
- **Reproductive and developmental toxicity**: Chlorambucil is a known mutagen and teratogen; use during pregnancy carries serious fetal risk.

No drug-drug interaction data was retrieved in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorambucil's activity in pregerminal center (IGHV-unmutated) CLL/SLL is supported by its established role as the standard comparator arm in multiple Phase 3 RCTs. However, it is not registered in Canada, its efficacy in this high-risk molecular subtype is inferior to newer targeted agents (BTK inhibitors such as ibrutinib/acalabrutinib; BCL-2 inhibitors such as venetoclax), and its long-term secondary malignancy risk demands careful risk-benefit weighing.

**To proceed, the following is needed:**

- **Regulatory pathway**: Identify a Health Canada compassionate use, Special Access Programme (SAP), or clinical trial framework if deployment in Canadian patients is intended
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank API to support formal pharmacological rationale
- **Safety package**: Full review of FDA Leukeran® prescribing information and EMA product monograph, including black-box warnings and contraindications
- **Subgroup evidence extraction**: Obtain IGHV-unmutated subgroup-specific outcomes (ORR, PFS) from the CLL11, COMPLEMENT, and RESONATE-2 Phase 3 trial publications
- **Combination strategy**: Evaluate whether chlorambucil + obinutuzumab (the only combination shown to provide clinically meaningful benefit over chlorambucil monotherapy in elderly CLL patients) is the appropriate framing for this subtype
- **Patient population definition**: Clarify intended setting — first-line elderly/frail patients ineligible for intensive therapy vs. resource-limited contexts where targeted therapy is inaccessible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

