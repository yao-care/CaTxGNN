---
layout: default
title: Sevoflurane
parent: Model Prediction Only (L5)
nav_order: 840
evidence_level: L5
indication_count: 10
---

# Sevoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sevoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

> Sevoflurane is an inhaled volatile anesthetic used for general anesthesia. The Canadian license records in the Evidence Pack do not list an approved indication text.
> The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
> It is a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (inhaled volatile anesthetic; approved indication text is not recorded in the license data) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sevoflurane is a volatile anesthetic, and its use in general anesthesia is well established. Mechanistically, it may be applicable to Prinzmetal angina only in a speculative sense.

Prinzmetal angina is caused by coronary artery vasospasm. Sevoflurane has known vasodilatory effects and acts on coronary smooth muscle, so a link to vasospasm is conceivable. This is a hypothesis only. Sevoflurane is not an established therapy for this condition. It is given for anesthesia, not for chronic angina management, and nothing in the evidence collected supports it as a treatment.

The high score most likely reflects proximity in the knowledge graph rather than demonstrated clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2265974 | SEVOFLURANE | Not specified | Not specified |
| 2307766 | SEVOFLURANE | Not specified | Not specified |
| 2172763 | SEVORANE AF | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5), with no trials or publications for Prinzmetal angina. The proposed mechanism is speculative, and sevoflurane is an acute-use anesthetic rather than a chronic angina therapy.

Other predicted indications for this drug also remain at Hold. Several are mechanistically implausible or carry possible harm signals:
- Migraine: the only registered trial treats headache as an anesthetic adverse effect.
- Nephrogenic syndrome of inappropriate antidiuresis: sevoflurane has known renal concerns.
- Inclusion body myositis: volatile anesthetics carry muscle-related risks in myopathies.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank) to test the coronary vasospasm hypothesis
- Preclinical or clinical evidence of sevoflurane's effect on coronary vasospasm
- Dosage form and route compatibility assessment, since an inhaled anesthetic would need to fit a chronic angina use case
- Approved indication text for the three Canadian licenses

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

