---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 4
---

# Captopril
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is a first-generation ACE (angiotensin-converting enzyme) inhibitor with established efficacy in managing hypertension, heart failure, and renal protection in diabetic nephropathy. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with **0 clinical trials** and **1 publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canada DINs on record; Captopril is established globally as an antihypertensive ACE inhibitor |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological class, Captopril is an angiotensin-converting enzyme (ACE) inhibitor — historically the first of its class approved for clinical use. Its core mechanism involves blocking the conversion of Angiotensin I to Angiotensin II, thereby reducing systemic vascular resistance and suppressing renin-angiotensin-aldosterone system (RAAS) overactivation.

Malignant hypertensive renal disease is characterized by severe, rapidly escalating hypertension that drives acute deterioration of renal function. The underlying pathophysiology is closely intertwined with RAAS dysregulation: elevated Angiotensin II promotes renal arteriolar vasoconstriction, glomerular hypertension, and pro-fibrotic cascades that accelerate nephrosclerosis. Captopril's ability to block Ang II generation may therefore offer a mechanistically coherent renoprotective effect — relieving intraglomerular pressure and attenuating fibrin deposition.

That said, the mechanistic reasoning remains inferential for this specific disease context. The evidence pipeline retrieved only a single tangentially related case report, and no prospective clinical studies targeting malignant hypertensive renal disease specifically were identified. The prediction is currently best classified as mechanistic hypothesis generation, warranting targeted preclinical and observational validation before clinical planning begins.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | Documents a case of positive captopril renography without renal artery stenosis, attributable instead to renin-secreting chromophobe renal cell carcinoma. Illustrates captopril's role as a diagnostic probe for renin-dependent hypertension; not direct therapeutic evidence for malignant hypertensive renal disease. |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data — including key warnings and contraindications — was identified as a blocking data gap (DG001). The full product monograph should be obtained from the relevant regulatory authority before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.28%) and a plausible RAAS-mediated mechanistic link, only one tangentially related case report exists for this specific indication, and no clinical trials have been registered. With an Evidence Level of L4 and a complete absence of Canadian regulatory approval, the evidence base is insufficient to support forward progression at this time.

**To proceed, the following is needed:**

- **Mechanism of action data** from DrugBank API (data gap DG002 identified; high severity)
- **Full safety profile** including warnings and contraindications from the product monograph (data gap DG001 identified; blocking severity)
- **Targeted literature search** for ACE inhibitor use specifically in malignant hypertensive nephrosclerosis and hypertensive emergency with acute kidney injury
- **Preclinical or observational data** supporting renoprotective outcomes in malignant hypertension models
- **Review of rank 2 prediction** — Malignant Renovascular Hypertension (L3 evidence, 20 publications, scored "Proceed with Guardrails") — which presents a stronger near-term development pathway with the same drug and closely related pathophysiology. A combined indication development strategy should be considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

