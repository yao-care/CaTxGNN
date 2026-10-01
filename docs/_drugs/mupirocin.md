---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

# Mupirocin: From Topical Antibacterial Use to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibacterial that inhibits bacterial protein synthesis and is active against *Staphylococcus aureus*.
The TxGNN model predicts it may be effective for **pleural empyema**, with a very high score (99.49%).
However, there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pleural empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mupirocin inhibits bacterial isoleucyl-tRNA synthetase, which blocks bacterial protein synthesis. It is active against *Staphylococcus aureus*, and *S. aureus* is one possible cause of empyema. That is the only mechanistic link to the predicted indication.

The link is weak in practice. Mupirocin is a topical agent with no established systemic or intrapleural use, while pleural empyema is a deep infection of the pleural space. Topical activity on skin or mucosa does not show that the drug can reach or work in the pleural cavity. The high TxGNN score reflects patterns in the knowledge graph, not clinical support.

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
| 2279983 | TARO-MUPIROCIN |
| 2483459 | STRAMUCIN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials or publications, and a topical antibacterial has no plausible route to the pleural space. It stays at evidence level L5.

**Other candidates in the same prediction list:**
- **Staphylococcal scalded skin syndrome** (TxGNN 95.57%, L3) has the strongest support. It includes a 2023 cohort study of IV antibiotics combined with 2% mupirocin ointment in children, plus reviews and case reports. It is biologically plausible, since the toxin-producing organism is *S. aureus*. Mupirocin-resistant toxigenic clones (PMID 28592549) limit confidence, and there is no RCT.
- **Cutaneous candidiasis** (TxGNN 98.27%, L4) has one 1991 *Lancet* report of unverified design. An antifungal mechanism is unconfirmed, and bacterial co-infection may explain the benefit.
- The remaining candidates (keratitis and keratopathy variants, vaginal conditions, non-human animal disease) have no supporting evidence. "Non-human animal disease" is a non-specific category and should be excluded.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently blocking safety screening)
- Detailed mechanism of action data from DrugBank
- Approved indication text and dosage forms for the two Canadian licenses, to check route compatibility
- If pursuing further, prioritise staphylococcal scalded skin syndrome: review the 2023 cohort study in full and assess local mupirocin resistance rates

*This report is for research reference only and does not constitute medical advice. Predicted candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

