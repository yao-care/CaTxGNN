---
layout: default
title: Neratinib
parent: Model Prediction Only (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
---

# Neratinib
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

# Neratinib: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Neratinib is an irreversible pan-HER kinase inhibitor marketed in Canada as NERLYNX and, based on general knowledge, used for HER2-positive breast cancer. The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**, but **no clinical trials or publications** were supplied for this specific label, so the prediction rests on the model score and a mechanistic argument.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (from general knowledge; the supplied license record has no indication text) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 (model prediction only; the pack's own grade is L4, based on mechanistic reasoning alone) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Neratinib irreversibly inhibits the HER-family tyrosine kinases EGFR, HER2 and HER4. Detailed mechanism-of-action data were not supplied, so this description comes from background knowledge rather than the Evidence Pack.

Progesterone-receptor (PR) status describes hormone-receptor biology, while HER2 describes a separate growth-factor pathway. The two overlap in practice: some HER2-driven breast cancers are PR-positive, and neratinib is already used in HER2-positive disease. This overlap is the main reason the prediction is plausible.

The link is indirect, though. PR-positive status alone does not imply HER2 dependence, so any benefit would likely be limited to the HER2-positive or HER2-mutant subset. The prediction is therefore best read as a hypothesis to refine by HER2 status, not as evidence of benefit in PR-positive disease generally.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific predicted indication.

Related context: one completed Phase 2 trial in a neighbouring breast cancer label ("normal breast-like subtype", prediction rank 2) tested neratinib in HER2 non-amplified, HER2-mutant metastatic breast cancer. It is not direct evidence for PR-positive disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib alone and with fulvestrant in metastatic HER2 non-amplified, HER2-mutant breast cancer; tests how HER2-mutated tumours respond |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2490536 | NERLYNX |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (pan-HER tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for PR-positive breast cancer is a high model score and an indirect mechanistic argument. No trials or publications address this label. Neratinib's HER2 activity may still be relevant, but only in HER2-driven or HER2-mutant subsets.

**To proceed, the following is needed:**
- Subtype-specific evidence, such as trials or publications on neratinib in PR-positive disease stratified by HER2 status
- Health Canada package insert warnings and contraindications, which block safety screening
- Detailed mechanism-of-action data, for example from DrugBank
- The approved indication text for the Canadian license, to confirm the original indication

**Other predicted candidates:** the remaining top-10 predictions were not assessed in depth. The sarcoma and giant cell tumour labels (ranks 5–10) have no identified HER-pathway rationale and no evidence, so they stay at Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

