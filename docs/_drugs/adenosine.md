---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Adenosine: From Supraventricular Tachycardia to Obsolete Bundle Branch Block

## One-Sentence Summary

Adenosine is an injectable antiarrhythmic used for supraventricular tachycardia and in diagnostic cardiac testing. The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but the evidence is model prediction only: **0 clinical trials** and **0 publications** support this pairing. The disease term is flagged as obsolete in the ontology, so the prediction is likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records; supraventricular tachycardia per the prediction rationale |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source records. Based on the prediction rationale, adenosine acts on A1 receptors to slow conduction through the atrioventricular (AV) node. This is why it is used for supraventricular tachycardia and diagnostic testing.

That mechanism does not support treating bundle branch block, which is a conduction delay below the AV node. The source data give no mechanism for this pairing.

The TxGNN score is very high (99.94%), but the disease term is marked as obsolete in the ontology. A high score on a retired term most likely reflects an artifact of the knowledge graph rather than a clinically meaningful indication. The prediction should not be read as a real repurposing signal.

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
| 2457474 | ADENOSINE INJECTION | Not listed | Not listed |
| 2457482 | ADENOSINE INJECTION | Not listed | Not listed |
| 2267659 | ADENOSINE INJECTION | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model output only (L5), with no trials or publications. It points to an obsolete disease term, and adenosine's known mechanism does not fit bundle branch block.

**To proceed, the following is needed:**
- Map the obsolete term to its current ontology replacement, and check whether the prediction still holds
- Obtain the Health Canada package insert (warnings, contraindications, approved indications, dosage form)
- Obtain mechanism of action data from DrugBank

**Alternative lead (rank 2 prediction):** catecholaminergic polymorphic ventricular tachycardia (CPVT), score 99.42%, evidence level L4. It is a research question, not a recommendation.
- The support is indirect. One case report describes ATP (an adenosine precursor) terminating bidirectional ventricular tachycardia in a CPVT patient, and one in vitro study reports ATP interacting with the CPVT-associated region of the cardiac ryanodine receptor.
- The one registered trial (NCT07263139, Phase 2a, recruiting, n=10) tests a product named AGP100. Its link to adenosine is unconfirmed.
- Adenosine can provoke arrhythmias in some settings, so safety would need separate assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

