---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Chemotherapy-induced Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF) widely used to stimulate neutrophil production in chemotherapy-induced neutropenia and to mobilize hematopoietic stem cells before transplantation.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **no supporting literature** and **10 retrieved clinical trials — none of which study Filgrastim directly for this indication**.
Overall evidence is classified as **L4 (mechanistic/preclinical level only)**, and the mechanistic rationale is weak; this prediction is most likely a knowledge-graph artefact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in dataset (0 registered Canadian products) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed (per dataset) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Filgrastim acts primarily through the G-CSF receptor (G-CSFR, CD114), activating JAK2/STAT3 and PI3K/AKT signalling cascades that drive proliferation and terminal maturation of neutrophil precursors in the bone marrow. Its established roles are reducing the duration and severity of chemotherapy-induced neutropenia and mobilising CD34⁺ progenitor cells into the peripheral blood before HSCT.

Primary release disorder of platelets refers to defective secretion of platelet α- and δ-granule contents, a process governed by RAB GTPases and the SNARE complex machinery that controls membrane fusion during degranulation. This pathway is mechanistically independent of G-CSF signalling. The only conceivable indirect link is a minor bystander effect of G-CSF on megakaryocyte differentiation outside the dominant TPO/c-Mpl axis — but this effect has never been demonstrated to influence platelet granule release in either preclinical or clinical settings.

The extremely high TxGNN score (99.998%) most likely reflects shared hematopoietic knowledge-graph nodes: neutrophils and platelets both originate in the bone marrow and are connected through common lineage and cytokine edges in the graph. This constitutes a network proximity artefact rather than a pharmacologically actionable mechanistic link. No published clinical trials or peer-reviewed literature specifically evaluating Filgrastim in platelet release disorders were found.

---

## Clinical Trial Evidence

All retrieved trials involve Filgrastim as a **stem cell mobilisation agent or post-chemotherapy supportive care drug**. None were designed to study Filgrastim as a treatment for platelet release disorders. Relevance grade for all trials is **C (not relevant to target indication)**; several are likely false-positive database matches.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral prophylaxis (valaciclovir vs valganciclovir) for CMV reactivation in immunocompetent ICU patients; Filgrastim not a study drug |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSCT vs best available therapy for treatment-resistant relapsing multiple sclerosis; Filgrastim used only for stem cell mobilisation |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplantation with NK cells for myeloid leukaemia (terminated early); Filgrastim as post-transplant haematopoietic support |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion followed by autologous HSCT for severe SLE; Filgrastim used for stem cell mobilisation only |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34⁺ selected vs unselected ASCT in advanced mantle cell and diffuse large B-cell lymphoma; Filgrastim used for progenitor cell harvest |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing post-transplant cyclophosphamide regimens for GvHD prophylaxis in mismatched unrelated donor PBSCT |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose optimisation of post-transplant cyclophosphamide + sirolimus/MMF for GvHD prophylaxis after reduced-intensity conditioning PBSCT |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT with busulfan, fludarabine and TBI for haematologic malignancies; Filgrastim as mobilisation agent |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile (oral NLRP3 inhibitor) for moderate COVID-19 and early cytokine release syndrome; Filgrastim is not the study drug — likely a false-positive match |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir vs placebo to reduce IL-6 and prevent CMV reactivation in immunocompetent adults with severe sepsis or trauma-associated respiratory failure; no connection to platelet disorders |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

The dataset contains **0 registered products** for Filgrastim in Canada. This almost certainly reflects a **data gap** — Filgrastim (e.g., Neupogen®) and its approved biosimilars have long been available in many markets globally. Formal verification against the Health Canada Drug Product Database is strongly recommended before drawing any regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack (data gaps DG001–DG002). Package insert review is required before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN model score of 99.998%, no direct mechanistic link has been established between G-CSF signalling and platelet α/δ-granule release pathways (RAB/SNARE machinery). All retrieved clinical trials use Filgrastim as a supportive or mobilisation agent — not as a therapy for platelet release disorders — and no relevant preclinical data or literature were identified. The high prediction score is most plausibly explained by shared hematopoietic knowledge-graph topology rather than pharmacological relevance.

**To proceed, the following is needed:**

- **Mechanistic feasibility study**: In vitro or animal-model data examining whether G-CSF signalling can modulate platelet granule secretion
- **Safety data retrieval**: Full package insert review (warnings, contraindications, drug interactions) to support any subsequent safety screening
- **Regulatory data reconciliation**: Confirm actual Canadian DIN status via the Health Canada Drug Product Database — the current dataset reports 0 licensed products, which is inconsistent with Filgrastim's known global approval history
- **Knowledge-graph audit**: Investigate why TxGNN assigns a near-perfect score in the absence of a plausible mechanistic pathway; this may point to a systematic graph artefact affecting other predictions in this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

