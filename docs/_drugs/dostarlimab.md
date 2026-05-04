---
layout: default
title: Dostarlimab
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: From Endometrial Cancer (dMMR/MSI-H) to Cervical Adenofibroma

## One-Sentence Summary

Dostarlimab (Jemperli®) is an anti-PD-1 immune checkpoint inhibitor approved internationally — including by the FDA and Health Canada — for mismatch repair-deficient (dMMR)/microsatellite instability-high (MSI-H) endometrial cancer and other solid tumours.
The TxGNN model predicts it may be effective for **Cervical Adenofibroma**, yet with **0 clinical trials** and **0 publications** directly supporting this direction, current evidence rests entirely on model prediction — and the mechanistic rationale is considered weak given the benign nature of this tumour.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | dMMR/MSI-H Endometrial Cancer (international approvals; not registered in Canada per this dataset) |
| Predicted New Indication | Cervical Adenofibroma |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on known pharmacological information, Dostarlimab is a humanised anti-PD-1 monoclonal antibody that blocks the binding of PD-1 to its ligands PD-L1 and PD-L2. This blockade restores the cytotoxic T-cell response against tumour cells that have upregulated PD-L1 as an immune evasion mechanism. Its established efficacy is concentrated in tumours with high tumour mutational burden (TMB), dMMR, or MSI-H features — all markers of heightened immunogenicity.

Cervical adenofibroma is a rare benign mixed epithelial–stromal tumour of the uterine cervix. Unlike the dMMR/MSI-H malignancies for which PD-1 blockade is indicated, benign tumours characteristically lack the immunogenic signals — including neoantigens from somatic mutations and PD-L1 upregulation — that are prerequisite for checkpoint inhibitor efficacy. There is no published evidence linking the PD-1/PD-L1 axis to the pathogenesis of cervical adenofibroma.

The TxGNN prediction most likely reflects topographic proximity in the knowledge graph (gynaecological domain overlap with the known endometrial cancer indication) rather than a genuine mechanistic connection. At present, the scientific rationale for applying Dostarlimab to cervical adenofibroma is considered insufficient to support further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dostarlimab is not currently registered in Canada according to this dataset (0 DINs, market status: not marketed). No product-level authorisation data is available.

> **Note:** Dostarlimab (Jemperli®) has received regulatory approvals from the FDA (2021), EMA (2021), and Health Canada for dMMR/MSI-H endometrial carcinoma. A dataset refresh from the Health Canada Drug Product Database may be required to capture current Canadian DIN registration status.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-1 monoclonal antibody (immune checkpoint inhibitor) |
| Myelosuppression Risk | Low (immune-mediated cytopenias are uncommon but reported as irAEs; unlike conventional cytotoxics, direct myelosuppression is not a primary toxicity) |
| Emetogenicity Classification | Minimal |
| Monitoring Items | Liver function (ALT, AST, bilirubin), thyroid function (TSH, free T4), adrenal/pituitary function, CBC with differential, renal function (creatinine), blood glucose, and clinical surveillance for immune-related adverse events (irAEs) at each infusion cycle |
| Handling Protection | Monoclonal antibody preparation — standard aseptic compounding applies; conventional cytotoxic closed-system handling is generally not required; follow institutional biosafety and biohazard protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack.

> **Class-specific considerations for PD-1 checkpoint inhibitors:** Dostarlimab carries well-characterised immune-related adverse event (irAE) risks, including immune-mediated pneumonitis, hepatitis, colitis, endocrinopathies (hypothyroidism, hypophysitis, adrenal insufficiency), nephritis, and dermatitis. Several predicted indications in this report (e.g., PBC/PSC–autoimmune hepatitis overlap syndrome, LAMA5-related multisystemic syndrome) represent populations where PD-1 blockade could precipitate or severely worsen pre-existing autoimmune pathology and should be considered contraindicated until safety data are available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Cervical adenofibroma is a benign stromal tumour without established mechanistic links to the PD-1/PD-L1 pathway; a 50% TxGNN prediction score with zero clinical or literature support does not constitute sufficient evidence to advance this indication.

**To proceed, the following is needed:**

- **Mechanistic validation:** Preclinical data demonstrating PD-L1 expression or immune infiltration in cervical adenofibroma tissue
- **Safety data:** Full package insert review for key warnings and contraindications (source: Health Canada drug product monograph for Jemperli®)
- **MOA data:** DrugBank API query to complete mechanism-of-action documentation
- **Dataset update:** Refresh Canada regulatory dataset to capture current Dostarlimab DIN/approval status
- **Broader indication review:** Indications at higher evidence tiers within this same prediction set — particularly **fallopian tube papillary adenocarcinoma** (Rank 8, L4, with mechanistic overlap via BRCA/dMMR features) and **bladder clear cell adenocarcinoma** (Rank 9, L3, with one Phase 2 basket trial: [NCT04779151](https://clinicaltrials.gov/study/NCT04779151)) — merit separate evaluation and may represent more scientifically grounded repurposing candidates for Dostarlimab

---

*This report is for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

