---
layout: default
title: Mepivacaine
parent: Model Prediction Only (L5)
nav_order: 584
evidence_level: L5
indication_count: 2
---

# Mepivacaine
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

# Mepivacaine: From Local Anaesthesia to Gastroduodenitis

## One-Sentence Summary

Mepivacaine is an amide local anaesthetic, marketed in Canada in dental and other injectable products.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (from the drug's class; the Canadian licence records provided contain no indication text) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source records. Mepivacaine belongs to the amide local anaesthetics, which block voltage-gated sodium channels and so stop nerve signal conduction. This is the basis of its use for numbing tissue.

The link to gastroduodenitis is weak. Gastroduodenal inflammation is treated by suppressing acid, eradicating *H. pylori*, protecting the mucosa or reducing inflammation, and sodium channel blockade has none of these effects. At most, a topical anaesthetic effect on mucosal pain is conceivable, and that would only relieve symptoms rather than treat the disease.

The very high score (99.49%) should be read with caution. It comes from the model only, and it may reflect knowledge-graph artefacts, since the drug has no recorded original indications and no mechanism data.

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
| 479934 | SCANDONEST 3% PLAIN INJ |
| 2474174 | CARBOCAINE 3% |
| 2241999 | CARBOCAINE 1% |
| 2330733 | 3% POLOCAINE DENTAL |
| 364304 | ISOCAINE HCL INJ 3% |

The records provided do not list dosage forms or approved indication text for these products. Two more authorizations exist but are not shown, giving 7 in total.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the interaction query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it, and no plausible mechanism connects sodium channel blockade to gastroduodenal disease. The only literature retrieved for the related prediction of peptic ulcer disease concerns a different drug (lofexidine), so it gives no support.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank, to test whether any biological link to gastroduodenitis exists
- Health Canada package insert warnings and contraindications, to complete safety screening
- Approved indication text and dosage forms for the Canadian licences
- Any mepivacaine-specific clinical or preclinical studies in gastroduodenal disease; none were found, so the prediction should not advance without them

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

