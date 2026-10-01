---
layout: default
title: Treprostinil
parent: Moderate Evidence (L3-L4)
nav_order: 932
evidence_level: L3
indication_count: 10
---

# Treprostinil
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Treprostinil: From an Unspecified Original Indication to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Treprostinil is a prostacyclin analogue marketed in Canada as Remodulin. The supplied data do not state its original approved indication.
The TxGNN model ranks **pulmonary arteriovenous malformation (PAVM)** as its top predicted new indication, but **0 clinical trials** and **0 publications** support it. This is a model prediction only, and there is a possible safety concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the supplied data (approved indication text is empty on all licences) |
| Predicted New Indication | Pulmonary arteriovenous malformation |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Treprostinil belongs to the prostacyclin analogue class. These drugs act on IP receptors to cause pulmonary vasodilation and to inhibit platelet aggregation and smooth muscle proliferation.

The data do not support a mechanistic link between treprostinil and PAVM. The high score most likely reflects graph proximity through shared pulmonary vascular terms in the knowledge graph. PAVM is a structural abnormality with abnormal connections between pulmonary arteries and veins. A vasodilator could plausibly worsen intrapulmonary shunting and hypoxemia, so this prediction raises a possible safety concern rather than a therapeutic rationale.

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
| 2246552 | REMODULIN |
| 2246553 | REMODULIN |
| 2246554 | REMODULIN |
| 2246555 | REMODULIN |

Dosage form, manufacturer and approved indication text are not provided for these licences.

---

## Safety Considerations

- **Possible concern specific to this prediction**: As a vasodilator, treprostinil could worsen intrapulmonary shunting and hypoxemia in PAVM. This is a mechanistic concern, not an observed finding.

Please refer to the package insert for warnings, contraindications and drug interactions. No drug interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PAVM prediction rests on a model score alone, with no trials, no literature and no supported mechanism. A plausible safety concern (worsened shunting) argues against pursuing it.

**Other predicted indications in this pack:**

| Predicted Indication | Evidence Level | Recommendation | Note |
|------|------|------|------|
| PAH associated with connective tissue disease | L1 | Proceed with Guardrails | Two RCT publications (PMID 11897647, 15302727); verify study designs from full records, since the supplied trial records do not independently show a Phase 3 RCT |
| PAH associated with congenital heart disease | L3 | Proceed with Guardrails | Small, terminated or observational studies; label scope needs verification |
| PAH associated with HIV infection | L3 | Research Question | Indirect evidence only, not HIV-specific |
| Schistosomiasis-associated PAH, chronic hemolytic anemia-associated PAH | L5 | Hold | No evidence supplied |
| Hypotrichosis simplex of the scalp, congenital hypotrichosis milia, Ambras-type hypertrichosis, odontal/periodontal malformation syndrome | L5 | Hold | No mechanistic link; the periodontal literature retrieved is unrelated to treprostinil |

**To proceed, the following is needed:**
- Treprostinil's approved indications and mechanism of action (DrugBank, Health Canada product monograph)
- Health Canada package insert warnings and contraindications, which block safety screening
- For PAVM specifically: any clinical or physiological evidence on prostacyclin analogues in intrapulmonary shunting
- For the CTD-PAH candidate: verification of the pivotal study designs and confirmation that the indication falls within the Canadian label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

