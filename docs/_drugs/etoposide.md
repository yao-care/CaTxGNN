---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Germ Cell Tumors / Small Cell Lung Cancer to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide (VP-16) is a well-established topoisomerase II inhibitor used as a core component of standard chemotherapy regimens for germ cell tumors, small cell lung cancer, and lymphomas.
The TxGNN model predicts it may be effective for **Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFAL)** — a rare monophasic epithelial subtype within the pulmonary blastoma spectrum —
with **0 clinical trials** and **1 indirect case report** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Germ cell tumors, small cell lung cancer, lymphoma (established clinical uses; no Canadian DIN on file) |
| Predicted New Indication | Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFAL) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Canadian regulatory package. Based on information within this evidence pack and the broader scientific literature, etoposide is known to act as a **topoisomerase II (TOP2) inhibitor** — it stabilizes the TOP2-DNA cleavage complex, generating irreversible double-strand DNA breaks that selectively destroy rapidly proliferating tumor cells. This mechanism is referenced throughout the evidence pack (e.g., PMID 29513652 demonstrating TOP2 sensitivity in EWS-FLI1-driven tumors, and multiple EPOCH/ICE/BEP regimen citations), and is consistent with etoposide's validated efficacy across germ cell tumors, small cell lung cancer, and lymphomas.

Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFAL) is a rare single-phase epithelial malignancy residing within the pulmonary blastoma pathological spectrum, histologically resembling fetal lung tissue at 10–16 weeks gestation. These embryonal-type tumors exhibit high proliferative activity and relatively immature DNA repair machinery — biological features that theoretically increase sensitivity to TOP2 inhibitors such as etoposide. The closely related biphasic pulmonary blastoma has documented case-level responses to etoposide-containing regimens (e.g., BEP and cisplatin-etoposide; PMID 6086368 reporting complete remission with a VP-16-containing combination, PMID 11955657 noting cisplatin + etoposide use), providing mechanistic continuity across the spectrum.

However, WDFAL-specific pharmacological evidence is essentially absent. The TxGNN prediction is driven by shared molecular and histological features between WDFAL and etoposide's validated oncology targets. Without dedicated preclinical models or prospective data, this remains a biologically plausible but clinically unvalidated hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for etoposide in well-differentiated fetal adenocarcinoma of the lung.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report + Literature Review | The Journal of International Medical Research | Classic biphasic pulmonary blastoma case (WDFAL is the monophasic epithelial variant of the same spectrum). Patient underwent right upper lobectomy followed by nedaplatin + paclitaxel adjuvant chemotherapy — not etoposide. After disease recurrence, treatment was escalated. No standard treatment guidelines exist due to extreme rarity. Provides histopathological context for the WDFAL spectrum but no direct etoposide efficacy data. |

---

## Canada Market Information

Etoposide currently has no approved Drug Identification Numbers (DINs) in Canada. There are no listed products in the Health Canada drug database for this compound.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Epipodophyllotoxin class (Topoisomerase II inhibitor) |
| Myelosuppression Risk | High — dose-limiting leukopenia and thrombocytopenia are the primary toxicities; WBC and platelet nadirs typically at Days 9–16 post-infusion; febrile neutropenia risk requires G-CSF prophylaxis consideration in intensive regimens |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle and at nadir), ALT/AST, total bilirubin, serum creatinine |
| Handling Protection | Mandatory cytotoxic drug handling protocols required — personal protective equipment (double gloves, gown, face protection), closed-system drug transfer devices, and dedicated aseptic preparation area |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
WDFAL is among the rarest thoracic malignancies worldwide (fewer than 100 documented cases globally), with no registered clinical trials, no direct etoposide efficacy data, and only a single tangentially relevant case report describing a related but distinct pulmonary blastoma subtype. While the TxGNN prediction score is high (99.94%), the evidence infrastructure required to support clinical translation is absent.

**To proceed, the following is needed:**
- Preclinical studies in WDFAL or pulmonary blastoma cell line/xenograft models to formally confirm TOP2 sensitivity and etoposide activity
- Systematic case series review of etoposide-containing regimens across the entire pulmonary blastoma spectrum (biphasic PB, pleuropulmonary blastoma, WDFAL) to build a consolidated indirect evidence base
- MOA data retrieval from DrugBank (Data Gap DG002 remediation: query DrugBank API for DB00773)
- TFDA package insert retrieval for formal safety profiling (Data Gap DG001 remediation)
- Health Canada DIN registration for etoposide as a prerequisite before any Canadian clinical application is feasible
- Referral to a rare thoracic tumor multidisciplinary board or international rare lung tumor registry (e.g., pulmonary blastoma registries) for expert input on feasibility of a compassionate use or registry-based evidence generation strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

