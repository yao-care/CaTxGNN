---
layout: default
title: Galcanezumab
parent: Model Prediction Only (L5)
nav_order: 422
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Galcanezumab: From Migraine to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab is an anti-CGRP monoclonal antibody used for migraine and cluster headache.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but there are **0 clinical trials** and **0 publications** supporting this, and no plausible mechanistic link was found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine and cluster headache (taken from the prediction rationale; license indication text is not available) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Galcanezumab is a monoclonal antibody that neutralizes calcitonin gene-related peptide (CGRP), a neuropeptide involved in migraine. Detailed mechanism of action data is not available from the source record, so this description comes from the prediction rationale.

**No plausible mechanistic link was found.** Heparin cofactor 2 deficiency is a hereditary loss of a serpin (SERPIND1) that inhibits thrombin. Blocking CGRP neither replaces nor restores this protein. The high score of 0.995 most likely reflects knowledge-graph topology rather than biology, and it cannot be checked against known pharmacology because the original MOA record is missing.

The two next-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Antithrombin deficiency type 2 | 99.41% | No link. Anti-CGRP therapy acts on neuropeptide signalling, not the coagulation cascade. Likely a graph artifact. |
| 3 | Factor 5 excess with spontaneous thrombosis | 99.41% | No link. Galcanezumab has no known effect on factor V, thrombin generation or platelet function. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2491087 | EMGALITY |
| 2505134 | EMGALITY |
| 2491060 | EMGALITY |

Dosage form and approved indication text are not available in the source record.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found. Any thrombosis-related concern with CGRP-pathway drugs would be a separate safety question, not a therapeutic indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is a model output only (L5), with no trials, no literature and no plausible biological mechanism. The three predictions for this drug are all coagulation disorders with no shared pathway with CGRP, so they are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data from DrugBank, to allow a formal mechanistic-link analysis.
- Approved indication text, dosage forms and manufacturers for the three DINs.
- Any preclinical or clinical evidence linking CGRP signalling to SERPIND1, thrombin inhibition or the coagulation cascade. Without it, this candidate should not advance beyond S0.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

