---
layout: default
title: Rufinamide
parent: Model Prediction Only (L5)
nav_order: 828
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Rufinamide is an antiseizure medication originally used to treat Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut syndrome |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

Note: the Canadian licence records compiled for this report contain no approved-indication text. The original indication is therefore taken from the drug-disease knowledge graph, which lists Lennox-Gastaut syndrome (and also cutis verticis gyrata).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on general knowledge, rufinamide is an antiseizure medication that is widely understood to prolong the inactive state of voltage-gated sodium channels. It is approved for Lennox-Gastaut syndrome, a severe childhood epileptic encephalopathy.

FIRES is also a severe, treatment-resistant epileptic encephalopathy. However, neuroinflammation is thought to play a major role in it, so a sodium-channel mechanism alone gives only a plausible but unproven link. The high TxGNN score (0.996) reflects the drug's closeness to other epilepsy conditions in the knowledge network. It is not clinical evidence.

Other predicted indications also have no supporting studies. They are listed below for reference:

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|------|------|------|------|
| 2 | Perioral myoclonia with absences | 99.51% | L5 |
| 3 | Atypical childhood epilepsy with centrotemporal spikes | 99.44% | L5 |
| 4 | Cryptogenic late-onset epileptic spasms | 99.44% | L5 |
| 5 | Photosensitive occipital lobe epilepsy | 99.44% | L5 |

For atypical childhood epilepsy with centrotemporal spikes, sodium-channel blockers can aggravate some of these syndromes. This would need careful consideration in any future evaluation.

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
| 02545985 | AURO-RUFINAMIDE | Not specified | Not specified |
| 02369613 | BANZEL | Not specified | Not specified |
| 02369648 | BANZEL | Not specified | Not specified |
| 02369621 | BANZEL | Not specified | Not specified |
| 02545993 | AURO-RUFINAMIDE | Not specified | Not specified |

All five licences are valid single-ingredient products.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from network associations, not from package insert text): liver failure, liver disease, gallbladder disease, leukopenia, anxiety disorder, neurotic disorder, dysthymic disorder.
- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed here were all rated Moderate. They include:
  - Corticosteroids: hydrocortisone, prednisone, betamethasone, triamcinolone
  - Vitamin D analogues: cholecalciferol, calcifediol, calcitriol
  - Opioids and related agents: morphine, difenoxin, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Antiemetics and prokinetics: ondansetron, metoclopramide, rolapitant
  - Others: pioglitazone, bupropion, eliglustat, naloxegol, nitisinone

Please refer to the package insert for warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5), with no registered trials or publications. The mechanistic link to FIRES is plausible but unproven.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are needed for safety screening
- Detailed mechanism of action data, for example from DrugBank
- A literature and trial search for rufinamide in FIRES and other refractory epileptic encephalopathies
- A review of the relevance of the knowledge-graph contraindications (liver disease, leukopenia) to the target population
- Dosage form and approved-indication details for the Canadian licences, to assess route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

