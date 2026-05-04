---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 4
---

# Codeine
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

# Codeine: From Analgesic/Antitussive to Nasal Cavity Disease

## One-Sentence Summary

Codeine is a well-established opioid prodrug, widely used for mild-to-moderate pain relief and cough suppression via μ-opioid receptor activation.
The TxGNN model assigns its highest prediction score (99.93%) to **Nasal Cavity Disease**; however, only **0 clinical trials** and **2 case reports** are available, and critically, both publications document codeine as a *cause* of nasal pathology through misuse — not as a treatment.
This prediction is assessed as an adverse-effect artefact rather than a genuine therapeutic signal, and the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic / Antitussive (no Canadian DINs on record in this dataset) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | 未上市 (Not Registered) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacology, Codeine is an opioid prodrug converted to morphine primarily via CYP2D6, acting as a μ/κ/δ opioid receptor agonist. Its principal clinical roles are mild-to-moderate analgesia and centrally mediated cough suppression (via inhibition of the cough centre in the medulla oblongata). These mechanisms have no established relevance to the treatment of nasal cavity disease.

The TxGNN model's top-ranked prediction of nasal cavity disease (score 99.93%) requires careful contextual interpretation. Both pieces of retrieved literature describe codeine as a contributor to nasal pathology rather than a remedy: one reports mucosal necrosis resulting from intranasal abuse of hydrocodone-acetaminophen tablets, and the other describes a rhinolith that formed around a hardened mass of codeine and opium (an "opioma") used as a nasal foreign body. The high TxGNN score most likely reflects a statistical co-occurrence signal in the biomedical literature between codeine and nasal cavity pathology — driven entirely by adverse-event and misuse reports — rather than any therapeutic relationship.

There is no identified mechanistic pathway by which codeine would provide benefit in nasal cavity disease. The evidence does not support this prediction as a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case Report | The Laryngoscope | Describes necrosis of the nasal cavity and pharynx caused by intranasal abuse of crushed hydrocodone-acetaminophen tablets — documents opioid misuse as a cause of nasal pathology, not a treatment |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case Report | Ear, Nose & Throat Journal | Reports rhinolithiasis in a 21-year-old in whom a hardened codeine/opium foreign body ("opioma") served as the nidus — again documents harm, not therapeutic use |

---

## Canada Market Information

No registered products (DINs) for Codeine are present in this dataset. Please consult the Health Canada Drug Product Database directly for current registration and scheduling status, as codeine-containing products (e.g., low-dose OTC combination formulations, prescription-only formulations) may exist under controlled substance schedules not captured here.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings (DG001) and contraindications are flagged as data gaps in this Evidence Pack. Retrieval of the Canadian prescribing information is a blocking prerequisite before any clinical evaluation proceeds. Given that codeine is a Schedule I controlled substance with known risks of respiratory depression, dependence, and death in certain populations (e.g., ultra-rapid CYP2D6 metabolisers, paediatric patients post-tonsillectomy), the absence of safety data is a critical gap.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The available evidence for codeine in nasal cavity disease consists solely of adverse-event case reports documenting harm from misuse, not any therapeutic benefit; there is no mechanistic basis for this repurposing direction, and the high TxGNN score appears to be an artefact of literature co-occurrence rather than a true therapeutic signal.

**To proceed with any further evaluation, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve and review the full Canadian prescribing information (contraindications, warnings, Black Box equivalents) before any clinical safety assessment can begin.
- **Resolve DG002 (High):** Confirm the complete mechanism of action via DrugBank API to enable rigorous mechanistic plausibility analysis.
- **Re-evaluate the TxGNN signal:** Determine whether the model's top prediction is driven by adverse-event/misuse co-occurrence rather than therapeutic association; consider applying a signal-filtering step to exclude adverse-effect literature from repurposing candidate scoring.
- **Consider redirecting analysis to Rank 2 — Acute Laryngopharyngitis:** This indication has a biologically plausible mechanistic rationale (codeine's μ-opioid–mediated suppression of the cough centre providing symptomatic relief for the dry cough characteristic of acute laryngopharyngitis) and is classified at L4 with a "Research Question" decision stage — representing a more defensible candidate for further investigation.
- **Verify Health Canada registration status:** Consult the Health Canada Drug Product Database to confirm current scheduling and availability of any codeine-containing products in Canada, as the 0-DIN record in this dataset may be incomplete.

---

> ⚠️ **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application to patient care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

