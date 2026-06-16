---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Erdafitinib
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

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib (Balversa) is a pan-FGFR (Fibroblast Growth Factor Receptor 1–4) kinase inhibitor, approved by the US FDA in 2019 for locally advanced or metastatic urothelial carcinoma harbouring susceptible FGFR2/FGFR3 alterations.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, based on the biological role of the FGFR axis in pulmonary vascular remodelling;
however, **0 clinical trials** and **0 publications** specifically addressing this combination are currently available, placing the evidence at the earliest exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma with FGFR2/FGFR3 alterations (FDA-approved 2019; not approved in Canada) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 — Model prediction only, no clinical studies |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold — Research Question Stage |

---

## Why Is This Prediction Reasonable?

Erdafitinib is a selective pan-FGFR kinase inhibitor that potently inhibits FGFR1, FGFR2, FGFR3, and FGFR4 by competing with ATP at the kinase active site. In urothelial carcinoma, the drug targets tumour cells with FGFR2/FGFR3 fusions or point mutations that drive oncogenic proliferation. Its mechanism — blocking aberrant FGFR-mediated signalling (including the RAS–MAPK and PI3K–AKT pathways) — is the basis for exploring its potential beyond oncology wherever FGFR dysregulation is pathologically relevant.

Pulmonary arterial hypertension (PAH) is characterised by progressive pulmonary vascular remodelling driven by abnormal proliferation of pulmonary arterial smooth muscle cells (PASMCs). The FGF2/FGFR1 axis is now recognised as a key driver of this process: FGFR1 is overexpressed in the lung tissue of PAH patients, and FGF2 stimulates PASMC proliferation and resistance to apoptosis — the same cellular behaviours that FGFR inhibition suppresses in urothelial cancer. Pre-clinical animal models have confirmed FGFR involvement in experimental PAH, and the biological direction of treatment (inhibiting pathological cell proliferation) is conceptually aligned.

The mechanistic overlap between tumour-driven and PAH-driven FGFR1 overexpression makes this prediction biologically coherent. Nonetheless, PAH is a complex, multifactorial disease with approved therapies targeting distinct pathways (prostacyclin, endothelin, NO/cGMP), and a dedicated pre-clinical programme in PAH-specific models would be needed before any clinical hypothesis can be formulated.

---

## Clinical Trial Evidence

Currently no clinical trials investigating Erdafitinib in pulmonary hypertension are registered.

---

## Literature Evidence

Currently no literature specifically linking Erdafitinib to pulmonary hypertension is available.

---

## Canada Market Information

Erdafitinib is not currently approved or marketed in Canada. No DINs have been issued.

For reference, the drug holds FDA approval (United States) for:

> Locally advanced or metastatic urothelial carcinoma with susceptible FGFR2 or FGFR3 alterations that has progressed during or following platinum-containing chemotherapy.

---

## Cytotoxicity

Erdafitinib is classified as an antineoplastic targeted therapy (approved indication: urothelial carcinoma).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Pan-FGFR tyrosine kinase inhibitor (small molecule) |
| Myelosuppression Risk | Low to moderate; myelosuppression is not a primary toxicity for FGFR kinase inhibitors, though anaemia and thrombocytopenia have been reported |
| Emetogenicity Classification | Low to moderate (consistent with oral targeted kinase inhibitors) |
| Monitoring Items | Serum phosphate (hyperphosphataemia is a class effect of FGFR inhibition), CBC, liver function (ALT/AST), renal function, ophthalmic exam (central serous retinopathy/retinal pigment epithelial detachment) |
| Handling Protection | Standard oral cytotoxic drug precautions apply; dedicated cytotoxic handling procedures required per institutional policy |

---

## Safety Considerations

Detailed TFDA package insert warnings and contraindications were not retrieved in this evidence pack. Known class-effect safety signals for FGFR inhibitors include hyperphosphataemia, ocular toxicity (central serous retinopathy), stomatitis, and hand-foot syndrome.

Please refer to the official Balversa (erdafitinib) package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold — Research Question Stage**

**Rationale:**
The TxGNN model assigns a high prediction score (99.38%) based on a biologically plausible FGFR1–PAH mechanistic link, but there is zero clinical or human translational evidence to support advancing Erdafitinib into a pulmonary hypertension development programme at this time. The indication requires fundamental pre-clinical validation before any clinical hypothesis can be responsibly framed.

**To proceed, the following is needed:**

- **Pre-clinical validation**: Confirm FGFR1 overexpression and functional contribution in established PAH animal models (e.g., SU5416/hypoxia rat, monocrotaline rat) using Erdafitinib specifically — not just pan-FGFR class data
- **MOA documentation**: Retrieve complete DrugBank/FDA mechanism-of-action data for Erdafitinib to enable formal mechanistic comparison (DG002 remediation)
- **Dose-exposure modelling**: Assess whether pharmacologically active FGFR-inhibitory concentrations can be achieved in pulmonary tissue at tolerated doses
- **Safety profile review**: Obtain TFDA package insert and Health Canada product monograph to complete S1 safety screening (DG001 remediation)
- **Differentiation analysis**: Clarify whether FGFR1 inhibition would complement or interfere with current PAH standard-of-care (prostacyclin analogues, ERAs, PDE5i/sGC stimulators)
- **Literature gap-fill**: Conduct a targeted literature search specifically on FGFR inhibitors (not limited to Erdafitinib) in PAH models to estimate the translational readiness of this target–indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

