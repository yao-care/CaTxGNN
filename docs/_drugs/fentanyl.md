---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fentanyl: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic mu-opioid receptor agonist widely used for acute and chronic pain management, procedural sedation, and anesthesia.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction — making this a pure model-based prediction requiring substantial preclinical and mechanistic validation before further development can be justified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain management and anesthesia (potent opioid analgesic) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Canada Market Status | Not Marketed *(data requires verification — see note below)* |
| Number of DINs | 0 *(data requires verification)* |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, fentanyl is a highly selective **mu-opioid receptor (MOR) agonist** — one of the most potent synthetic opioids in clinical use. It acts on MORs distributed across the central nervous system, spinal cord, and peripheral tissues, producing analgesia, sedation, and dose-dependent respiratory depression. Its original clinical role is firmly in pain management and anesthesia.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare X-linked disorder caused by **gain-of-function mutations in the V2 vasopressin receptor (AVPR2)**, leading to constitutive receptor activation and persistent water retention independent of circulating antidiuretic hormone (ADH/vasopressin) levels. A plausible mechanistic bridge exists in that both the mu-opioid receptor and the V2 vasopressin receptor are **G-protein coupled receptors (GPCRs)**, and cross-talk between opioid and vasopressin signalling systems has been described in preclinical models — for example, opioids can modulate hypothalamic vasopressin release and influence renal water handling through central and peripheral pathways.

However, NSIAD's pathology resides in constitutive receptor activity rather than excess vasopressin secretion, making it distinctly different from classic SIADH. Whether fentanyl's MOR agonism translates into clinically meaningful modulation of AVPR2-driven antidiuresis is entirely unproven. The mechanistic hypothesis is biologically plausible but speculative, and the complete absence of any supporting clinical or literature evidence means this prediction must be classified as **L5** until dedicated mechanistic studies are conducted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No active Drug Identification Numbers (DINs) or product licences were retrieved for Fentanyl in the current dataset.

> ⚠️ **Data Verification Required:** This almost certainly reflects a **data extraction gap** rather than actual market absence. Fentanyl is widely marketed in Canada under multiple brand names (e.g., Duragesic®, Abstral®, Fentora®, Subsys®) across several dosage forms including transdermal patches, buccal tablets, sublingual spray, and parenteral solutions. **This gap must be resolved before any regulatory or commercial assessment can proceed.**

---

## Safety Considerations

Safety data was not retrievable from the Evidence Pack for this candidate. Based on well-established class-level pharmacology, the following high-priority safety considerations apply:

- **Respiratory Depression:** Dose-dependent respiratory depression is the primary life-threatening risk; fentanyl's high potency (approximately 100× morphine) significantly narrows the therapeutic window.
- **Opioid Dependence and Addiction:** Fentanyl carries a high abuse potential and is subject to Schedule I controlled substance regulations; any non-analgesic repurposing would require a robust risk mitigation strategy.
- **Drug–Drug Interactions:** Clinically significant interactions are expected with other CNS depressants (benzodiazepines, alcohol, other opioids) and with strong CYP3A4 inhibitors/inducers that affect fentanyl metabolism.
- **Special Populations:** Significant risk in elderly patients, those with respiratory compromise, and in paediatric dosing — particularly relevant given that NSIAD often presents in infancy.

Full contraindications, warnings, and DDI data must be obtained from the Health Canada product monograph before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero clinical or literature evidence supporting the use of fentanyl in nephrogenic syndrome of inappropriate antidiuresis, and the mechanistic link — while biologically conceivable — remains entirely speculative. Compounding this, fentanyl's serious safety profile (respiratory depression, addiction liability, narrow therapeutic index) imposes a very high burden of proof before repurposing into a rare indication — particularly one that often affects infants and young children — could be ethically or clinically justified.

**To proceed, the following is needed:**

- **Resolve the Canada regulatory data gap:** Retrieve active DINs, approved indications, and product monographs for fentanyl from Health Canada
- **Obtain full MOA data from DrugBank (DB00813):** Validate whether the proposed opioid–vasopressin receptor crosstalk hypothesis is pharmacologically grounded
- **Conduct a targeted preclinical literature review:** Focus on MOR signalling and AVPR2/NSIAD biology to determine whether any mechanistic link exists beyond GPCR superfamily membership
- **Retrieve complete safety data:** TFDA package insert warnings, contraindications, and DDI profile are blocking items per DG001 severity classification
- **Risk–benefit assessment:** Determine whether the risk profile of a high-abuse-potential controlled opioid is appropriate for a rare paediatric renal channelopathy with existing management options (fluid restriction, urea supplementation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

