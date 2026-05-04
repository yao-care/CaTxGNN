---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 7
---

# Cyclosporine
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

# Cyclosporine: From Organ Transplant Rejection to Chronic Granulomatous Disease

## One-Sentence Summary

Cyclosporine is a well-established calcineurin inhibitor and immunosuppressant, widely used in solid organ transplantation and a range of autoimmune conditions.
The TxGNN model predicts it may be effective for **Chronic Granulomatous Disease (CGD), Autosomal Recessive Form**,
with **1 clinical trial** and **1 publication** currently available — both situated in the context of hematopoietic stem cell transplantation (HSCT) used to cure CGD.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset (no DINs found) |
| Predicted New Indication | Granulomatous Disease, Chronic, Autosomal Recessive (CGD) |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed (per current dataset — likely a data gap) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on well-established pharmacological knowledge, cyclosporine is a calcineurin inhibitor that blocks T-cell activation by preventing calcineurin from dephosphorylating NFAT transcription factors, thereby suppressing interleukin-2 (IL-2) and other pro-inflammatory cytokines. This broad immunosuppressive effect underpins its use in transplantation, rheumatoid arthritis, psoriasis, and nephrotic syndrome.

Chronic Granulomatous Disease (CGD) is a primary immunodeficiency caused by inherited defects in the NADPH oxidase complex, leaving phagocytes unable to generate the reactive oxygen species needed to kill ingested pathogens. Patients suffer from recurrent, life-threatening bacterial and fungal infections and granuloma formation. Hematopoietic stem cell transplantation (HSCT) is currently the only curative therapy for CGD, and cyclosporine is a cornerstone of standard GvHD prophylaxis in that context.

The mechanistic link is therefore **indirect**: cyclosporine does not correct the NADPH oxidase defect itself, but rather suppresses alloreactive T-cell responses to prevent graft-versus-host disease — enabling HSCT to succeed and thus cure CGD. This is a well-accepted clinical use pattern rather than a novel repurposing hypothesis in the strict sense, which partly explains the high TxGNN score. Whether cyclosporine has a role as a direct immunomodulatory agent in CGD outside of HSCT remains an open research question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Assessed tolerability of abatacept added to cyclosporine + mycophenolate mofetil as GvHD prophylaxis in children undergoing unrelated donor HSCT for serious non-malignant diseases (including CGD); participants followed for 2 years. Cyclosporine served as background standard-of-care, not the primary investigational agent. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Retrospective Cohort | J Allergy Clin Immunol | Demonstrated excellent survival outcomes after both matched related and unrelated donor HSCT for CGD, supporting HSCT — and by extension standard GvHD prophylaxis regimens including cyclosporine — as an effective curative strategy for this disease. |

---

## Canada Market Information

No Drug Identification Numbers (DINs) were found in the current regulatory dataset for cyclosporine. This almost certainly reflects a **data collection gap** rather than true absence from the Canadian market: cyclosporine is a long-established reference drug available under brand names such as Neoral® and Sandimmune® in many jurisdictions. Regulatory data should be retrieved directly from Health Canada's Drug Product Database before any market access assessment proceeds.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug–drug interaction data were available in the current evidence pack.

> **Note:** Cyclosporine is known to carry significant safety considerations including nephrotoxicity, hepatotoxicity, hypertension, neurotoxicity, and a large number of clinically important drug–drug interactions (particularly with CYP3A4 substrates and P-glycoprotein modulators). Obtaining the full prescribing information is rated **Blocking** severity in the current data gap assessment and must be resolved before any clinical safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The available evidence supports cyclosporine's role as standard GvHD prophylaxis within HSCT for CGD — an **indirect and already-established** clinical use pattern rather than a novel repurposing application. The evidence base is limited to one small Phase 1 trial (n = 10, primary drug = abatacept) and one retrospective cohort study focused on HSCT outcomes. Significant blocking data gaps remain in safety information and regulatory status, preventing entry into a formal safety screening stage.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm Health Canada DIN status and retrieve approved prescribing information for cyclosporine products (Neoral®, Sandimmune®, generic equivalents)
- **Safety data**: Obtain TFDA/Health Canada package insert to extract warnings, contraindications, and drug interactions — currently a **Blocking** data gap
- **MOA clarification**: Retrieve full mechanism of action from DrugBank (DB00091) to support mechanistic analysis
- **Repurposing hypothesis refinement**: Clearly distinguish between (a) cyclosporine as standard GvHD prophylaxis enabling curative HSCT in CGD (already established practice, not a new repurposing opportunity) vs. (b) cyclosporine as a direct immunomodulatory agent in CGD patients not undergoing HSCT (genuinely novel, but currently unsupported by evidence)
- **Prospective evidence**: If hypothesis (b) is pursued, a proof-of-concept study or systematic review of any existing off-label use would be needed to elevate evidence beyond L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

