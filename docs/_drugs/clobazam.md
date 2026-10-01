---
layout: default
title: Clobazam
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: From Antiseizure Therapy to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a benzodiazepine antiseizure medication marketed in Canada, although the supplied licence records do not list its approved indication text.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**.
There are currently **0 clinical trials** and **2 publications** on this disease, and neither publication studies clobazam, so the prediction rests almost entirely on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence records (general use: antiseizure benzodiazepine) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 (as scored in the pack; no clobazam-specific evidence) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. From general pharmacology, clobazam enhances GABA-A receptor signalling. That dampens neuronal excitability and is the basis for its use in seizure disorders.

FIRES is a form of new-onset refractory status epilepticus in previously healthy children, and it often fails conventional antiseizure drugs. A GABAergic agent is a plausible fit. The supplied literature, however, covers lorazepam (another benzodiazepine) and perampanel, not clobazam. The high TxGNN score is a prediction, not clinical evidence.

Clobazam's regulatory status is also unconfirmed. The rank 6 prediction, childhood-onset epileptic encephalopathy, has much richer literature (Lennox-Gastaut and Dravet reviews and guidelines). If clobazam is already approved for Lennox-Gastaut syndrome, that indication may be on-label rather than true repurposing. This should be checked against an authoritative source.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disord | Enteral lorazepam used as a weaning strategy in midazolam-dependent FIRES patients. It does not involve clobazam. |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | Perampanel may reduce barbiturate dependency in a 13-year-old boy with FIRES. It does not involve clobazam. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02238334 | TEVA-CLOBAZAM | Not listed | Not listed |
| 02244638 | APO-CLOBAZAM | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no clobazam-specific publications for FIRES. The high model score is the only direct support, and the Health Canada indication and safety data are missing.

**To proceed, the following is needed:**
- Health Canada package insert (approved indications, warnings, contraindications, interactions)
- Mechanism of action data from DrugBank
- A targeted literature search for clobazam use in FIRES or refractory status epilepticus
- Confirmation of clobazam's approved indications, including Lennox-Gastaut syndrome, to separate on-label from repurposed use
- Consideration of a higher-evidence candidate such as childhood-onset epileptic encephalopathy (rank 6)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

