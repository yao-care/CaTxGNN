---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Felodipine: From Hypertension to Pulmonary Hypertension Due to Lung Disease/Hypoxia

## One-Sentence Summary

Felodipine is a dihydropyridine-class calcium channel blocker (CCB) well-established internationally for the treatment of hypertension and angina pectoris, though formal indication records are absent from this Evidence Pack.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia (Group 3 PH)**,
with **no registered clinical trials** and **20 background publications** retrieved — however, none of these publications represent direct clinical studies of felodipine in this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Angina pectoris (well-known drug class; no formal indication text available in this Evidence Pack) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, felodipine is a dihydropyridine calcium channel blocker that selectively blocks L-type voltage-gated calcium channels in arterial vascular smooth muscle. This inhibition prevents calcium influx, relaxes smooth muscle, and causes systemic arterial vasodilation — lowering blood pressure with minimal negative inotropic effect compared to non-dihydropyridine CCBs such as verapamil or diltiazem.

The mechanistic link to pulmonary hypertension is plausible in principle: the hallmark of all forms of pulmonary hypertension is elevated pulmonary vascular resistance driven by pulmonary arterial vasoconstriction and remodelling. Calcium channel blockers are, in fact, an established therapy for **Group 1 pulmonary arterial hypertension (PAH)** in the subset of patients (approximately 10–15%) who demonstrate a positive acute vasoreactivity response. In these patients, long-term CCB therapy with agents such as nifedipine, amlodipine, or diltiazem produces durable haemodynamic benefit, and felodipine's profile is pharmacologically similar.

However, an important mechanistic caveat applies directly to the predicted indication. **Group 3 PH** — pulmonary hypertension caused by chronic lung disease or hypoxia (e.g., COPD, interstitial lung disease, sleep-disordered breathing) — depends heavily on **hypoxic pulmonary vasoconstriction (HPV)** as a compensatory reflex that diverts blood from under-ventilated lung segments, partially preserving oxygenation. CCBs inhibit this protective reflex. By blunting HPV, felodipine could worsen ventilation-perfusion mismatch and deepen systemic hypoxemia — the very problem it is intended to address. Current **ESC/ERS 2022 Pulmonary Hypertension Guidelines** explicitly advise against the use of PAH-specific vasodilators, including CCBs, in Group 3 PH. This mechanistic counterargument substantially limits the translational case for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 publications retrieved for this indication are background papers on hypoxia biology (tumour hypoxia, altitude physiology, neurological sequelae of hypoxia, HIF signalling, etc.) and **do not represent direct clinical or preclinical studies of felodipine in pulmonary hypertension**. The search algorithm matched on the "hypoxia" component of the indication name rather than on felodipine-specific evidence. The most medically pertinent papers are presented below for mechanistic context only.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Mechanistic review of hypoxemia: V/Q mismatch, shunt, and hypoventilation as root causes — contextual background for understanding Group 3 PH pathophysiology |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Overview of oxygen sensing, HIF transcription factor pathways, and vascular adaptation to hypoxia — mechanistic context for pulmonary vascular responses |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | HIF-1 role in tissue repair and fibrosis; relevant to understanding hypoxia-driven pulmonary vascular remodelling in chronic lung disease |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Strategies to modify tumour hypoxia including vascular targeting; provides indirect context for pulmonary vascular regulation under hypoxic conditions |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | HIF and innate immunity under hypoxia — highlights systemic inflammatory consequences of chronic hypoxia beyond the vascular compartment |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Brain vulnerability to hypoxia in pulmonary disease; highlights multi-organ consequences of Group 3 PH-associated hypoxemia |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical evidence and molecular mechanisms of cognitive impairment under acute and chronic hypoxia — a comorbidity relevant to Group 3 PH patients |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mexicano Seguro Social | Physiological and adaptive responses to hypobaric hypoxia at altitude; provides comparator model for understanding chronic hypoxia adaptation |

> **Important caveat**: None of the 20 retrieved papers directly study felodipine in the context of pulmonary hypertension due to lung disease or hypoxia. A targeted search specifically for *"felodipine"* AND *"pulmonary hypertension"* or *"pulmonary vascular resistance"* is required before any evidence-based assessment can be made.

---

## Canada Market Information

Felodipine currently has **no active Drug Identification Numbers (DINs)** in Canada and is not marketed. No approved indication text is available from Health Canada licensing records in this Evidence Pack.

> Felodipine is approved in multiple other jurisdictions under brand names such as Plendil® (AstraZeneca) in the United States and European Union, and is indicated for hypertension and stable angina in those markets. Historical DIN records from Canada may exist and should be queried via the Health Canada Drug Product Database.

---

## Safety Considerations

Formal Health Canada safety data (product monograph warnings and contraindications) are not available in this Evidence Pack and must be retrieved before any regulatory or clinical assessment. Based on established class pharmacology, the following concern is particularly critical for this specific predicted indication:

- **Pharmacological safety concern specific to Group 3 PH**: Felodipine, as a CCB, inhibits hypoxic pulmonary vasoconstriction (HPV) — a compensatory reflex that is protective in lung disease-associated pulmonary hypertension. Blocking HPV may worsen ventilation-perfusion mismatch and increase systemic hypoxemia, directly opposing the therapeutic goal. This is a class-level, mechanism-based concern that is not merely a data gap but a pharmacological contraindication for this indication category per current guidelines.

Please refer to the Health Canada product monograph and ESC/ERS 2022 Pulmonary Hypertension Guidelines for complete safety information once sourced.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct clinical or felodipine-specific preclinical evidence supporting use in pulmonary hypertension due to lung disease/hypoxia, and — more critically — the established mechanism of HPV inhibition by CCBs creates a plausible pharmacological risk that is specifically contraindicated in Group 3 PH per current international guidelines. The high TxGNN prediction score reflects structural similarity to cardiovascular indications at the knowledge graph level but does not override this mechanistic safety concern.

**To proceed, the following is needed:**
- Retrieve the Health Canada product monograph (or equivalent DIN/NPN history) for complete warnings, contraindications, and drug interaction data (Data Gap DG001)
- Obtain felodipine MOA data from DrugBank API to confirm CCB mechanism and any distinguishing pharmacological features (Data Gap DG002)
- Conduct a targeted PubMed search: *"felodipine" AND "pulmonary hypertension"* and *"calcium channel blocker" AND "Group 3 pulmonary hypertension"* to identify any class-level clinical evidence
- Review ESC/ERS 2022 Guideline recommendation class for CCBs in Group 3 vs. Group 1 PH to formally document the regulatory and clinical rationale for Hold
- Consult a specialist in pulmonary hypertension to assess whether any subset of Group 3 PH patients (e.g., those with a mixed vasoreactive component) could be candidates before completely closing this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

