---
layout: default
title: Cinchocaine
parent: Model Prediction Only (L5)
nav_order: 196
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Cinchocaine: predicted new indication Bronchitis (evidence level L5). Approved use: Dermatitis"
---

# Cinchocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cinchocaine: From Dermatitis to Bronchitis

## One-Sentence Summary

Cinchocaine (dibucaine) is a local anaesthetic originally used for dermatitis and is marketed in Canada in topical anorectal products.
The TxGNN model predicts it may be effective for **bronchitis**, but there are **no registered clinical trials and no publications** supporting this direction. It rests on a model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cinchocaine is known as an amide-type local anaesthetic that blocks voltage-gated sodium channels. Its efficacy in surface (topical) pain and itch relief is established.

A possible link to bronchitis is the suppression of airway sensory nerve activity and the cough reflex, similar to topical anaesthetics used in airway procedures. This link is speculative. Cinchocaine has no known anti-inflammatory or anti-infective action in the airway, and it is a highly potent and toxic local anaesthetic used mainly topically. Its systemic or inhaled safety has not been established.

The other six predictions follow the same pattern (all L5, Hold, scores 99.64%–99.76%):
- Acrodermatitis chronica atrophicans
- Neonatal dermatomyositis
- Childhood secondary interstitial lung disease associated with a connective tissue disease
- Acne keloid
- Familial hydroa vacciniforme
- Amyopathic dermatomyositis

Of these, acne keloid is the most pharmacologically plausible, and only for symptomatic relief of pain or itch with topical use. The interstitial lung disease prediction has no credible mechanistic connection and likely reflects network proximity to connective tissue disease.

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
| 02247882 | PROCTOL SUPPOSITORIES | Not specified | Not specified |
| 02247322 | PROCTOL OINTMENT | Not specified | Not specified |
| 02226383 | TEVA-PROCTOSONE | Not specified | Not specified |

All three authorisations are valid single-ingredient products.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, sudden cardiac arrest, heart conduction disease, cardiovascular disease, heart disease, respiratory failure, myasthenia gravis (including adult-onset), neuromuscular junction disease, and butyrylcholinesterase deficiency.
- **Other concerns:** Local anaesthetic systemic toxicity is a particular worry for neonatal and paediatric use, and for any inhaled or systemic route.

No drug interaction records were found. Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, the mechanism is only loosely plausible, and the safety profile for systemic or airway use is unfavourable.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search specific to cinchocaine and bronchitis, or to a more plausible topical symptomatic use such as acne keloid
- Route-compatibility assessment, since current products are rectal and topical
- A safety assessment for any non-topical route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

