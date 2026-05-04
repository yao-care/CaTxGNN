---
layout: default
title: Cilazapril
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cilazapril: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Cilazapril is an ACE (Angiotensin-Converting Enzyme) inhibitor belonging to the RAAS-blocking drug class, traditionally used for systemic hypertension and heart failure.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia (Group 3 PH)**, scoring **99.20%** on the prediction model.
However, the evidence base is limited — **0 clinical trials** and **no cilazapril-specific publications** were identified for this indication, with retrieved literature covering only general hypoxia biology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (ACE inhibitor class; no Canada DIN on file) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia (Group 3 PH) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 — Mechanistic inference only, no clinical studies |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacological class, cilazapril is an ACE inhibitor that blocks the conversion of Angiotensin I to Angiotensin II, thereby suppressing the renin-angiotensin-aldosterone system (RAAS). This leads to systemic and — theoretically — pulmonary vasodilation, reduced vascular resistance, and attenuation of vascular remodeling driven by Angiotensin II.

In Group 3 PH (pulmonary hypertension secondary to lung disease or chronic hypoxia), RAAS activation has been documented as a contributing pathophysiological mechanism. Hypoxia-induced pulmonary vasoconstriction involves local Angiotensin II signaling, and ACE inhibition could theoretically interrupt this cycle, reduce pulmonary artery pressure, and slow vascular remodeling. This mechanistic linkage explains why a graph-based model like TxGNN would flag ACE inhibitors as candidates.

However, the clinical translation risk is significant. ACE inhibitors cause systemic vasodilation, which can worsen ventilation-perfusion (V/Q) mismatch and aggravate hypoxemia in patients with underlying lung disease — potentially the opposite of the intended effect. Current ESC/ERS pulmonary hypertension guidelines do not recommend ACE inhibitors as specific therapy for Group 3 PH. The prediction is mechanistically plausible but faces substantial clinical barriers that have not been resolved in published trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cilazapril in pulmonary hypertension owing to lung disease and/or hypoxia.

---

## Literature Evidence

The 20 publications retrieved address general hypoxia biology and are not specific to cilazapril or ACE inhibitors in pulmonary hypertension. They provide contextual background only. The 10 most relevant are listed below:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Describes mechanisms of hypoxemia including V/Q mismatch and shunt — relevant to understanding why systemic vasodilators may worsen oxygenation in lung disease |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology (RCR) | Reviews therapeutic strategies targeting tumor hypoxia; illustrates the complexity of hypoxia modification as a treatment approach |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Explores hypoxia's dual role in neurodegeneration and neuroprotection; general HIF-pathway biology |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Covers HIF-mediated innate immune responses under physiologic and inflammatory hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Overview of cellular oxygen sensing, angiogenesis, and vascular disease under hypoxia |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | HIF-1 signaling in tissue repair and fibrosis — relevant to vascular remodeling in chronic hypoxia |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical and molecular review of hypoxia-induced cognitive impairment; general hypoxia pathophysiology |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | DUB-HIF axis in hypoxic tumors; not directly relevant to pulmonary vascular disease |
| [36100192](https://pubmed.ncbi.nlm.nih.gov/36100192/) | 2022 | Review | Journal of Controlled Release | Hypoxia-targeted nanomedicines in solid tumors; background on hypoxic tumor microenvironment |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Examines hypoxia's role in multiple sclerosis pathology and vascular dysfunction |

> **Note:** None of the retrieved publications directly study cilazapril, ACE inhibitors, or RAAS blockade in Group 3 pulmonary hypertension. The evidence gap is confirmed.

---

## Canada Market Information

Cilazapril is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on file, and no approved product monographs are available through the Health Canada database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important class-level caution:** As an ACE inhibitor, cilazapril carries well-known class risks relevant to this predicted indication:
> - **Contraindicated** in bilateral renal artery stenosis or single functioning kidney (risk of acute renal failure)
> - **Risk of worsening hypoxemia** via systemic vasodilation causing V/Q mismatch in patients with underlying lung disease
> - **Hyperkalemia risk**, particularly in patients with renal impairment
> - **Dry cough** (ACE inhibitor class effect) may be poorly tolerated in patients with existing respiratory disease
>
> These class-level concerns are especially pertinent for the proposed Group 3 PH indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for ACE inhibition in Group 3 pulmonary hypertension is theoretically plausible through RAAS suppression, there are zero clinical trials and no drug-specific publications to support cilazapril's use in this setting. More critically, ACE inhibitors carry a recognized risk of worsening hypoxemia in patients with underlying lung disease — the very population this indication targets — and current ESC/ERS guidelines do not endorse this therapeutic approach. Cilazapril is also not marketed in Canada, creating an additional regulatory barrier.

**To proceed, the following is needed:**

- **Mechanism of action data:** Retrieve full DrugBank entry for cilazapril (DB01340) to confirm RAAS mechanism and any known pulmonary pharmacodynamics
- **Cilazapril-specific literature search:** Conduct a dedicated PubMed search combining cilazapril with "pulmonary hypertension," "ACE inhibitor pulmonary," or "RAAS lung disease" — the current 20 results appear to be generic hypoxia background literature, not drug-specific evidence
- **Class evidence review:** Review existing evidence for other ACE inhibitors (enalapril, ramipril) in Group 3 PH to determine whether class-level data could support extrapolation
- **Safety dossier:** Download and parse the product monograph from markets where cilazapril is approved (e.g., EU/UK — marketed as Vascace/Inhibace) to obtain formal contraindications, warnings, and drug interaction data
- **ESC/ERS guideline alignment check:** Confirm current guideline stance on RAAS inhibition in Group 3 PH before any clinical development planning
- **Regulatory pathway assessment:** If evidence is assembled, determine whether a Health Canada NOC submission or a compassionate use framework would apply, given zero current Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

