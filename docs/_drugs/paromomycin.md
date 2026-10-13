---
layout: default
title: Paromomycin
parent: Model Prediction Only (L5)
nav_order: 707
evidence_level: L5
indication_count: 8
---

# Paromomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Paromomycin: From Hepatic Encephalopathy to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Paromomycin is an oral aminoglycoside antibiotic, originally associated with hepatic coma and hepatic encephalopathy.
The TxGNN model predicts it may be effective for **idiopathic copper-associated cirrhosis**, but **no clinical trials and no publications** support this prediction, so it rests on a graph-based score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic coma / hepatic encephalopathy (from the knowledge graph; the Canadian licence has no indication text) |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, paromomycin is a poorly absorbed aminoglycoside that acts in the gut lumen. It reduces ammonia-producing bacteria, which is why it has been used in hepatic encephalopathy.

The predicted indication, idiopathic copper-associated cirrhosis, is a liver disease driven by copper handling. Paromomycin has no known link to copper metabolism or copper-associated liver injury. The high score most likely reflects shared liver-disease neighbours in the knowledge graph and not a real mechanism. The prediction should be treated as a hypothesis-generating signal, not as supported evidence.

Other predictions in the same list show a similar pattern. Several are portal hypertension or liver-vascular conditions (primitive portal vein thrombosis, early-onset familial noncirrhotic portal hypertension, hepatoportal sclerosis), and all are scored at L5 with a Hold recommendation. Of these, hepatopulmonary syndrome has a plausible but unverified hypothesis: antibiotics that reduce gut bacterial translocation have been explored there. The only prediction with any literature was peritonitis (L4), but that literature does not address peritonitis treatment, and oral paromomycin is minimally absorbed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for idiopathic copper-associated cirrhosis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02078759 | HUMATIN | Not specified | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): kidney disease, pyoureter, hearing loss disorder, and X-linked mixed deafness with perilymphatic gusher. These are consistent with the known renal and ototoxicity concerns of aminoglycosides, particularly with systemic exposure or impaired renal function.
- **Drug Interactions**: 36 interactions were recorded. The ones flagged as **Major** are:
  - Neuromuscular blockers: cisatracurium, atracurium, doxacurium, metocurine, mivacurium
  - Live cholera vaccine (Vibrio cholerae CVD 103-HgR strain)
- **Moderate** interactions include proton pump inhibitors (rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole), oestrogens (ethinylestradiol, estradiol, mestranol), methotrexate, mycophenolate mofetil, picosulfuric acid, enflurane, and indium In-111 oxyquinoline.
- **Minor**: digoxin.

Label warnings and contraindications from the Health Canada package insert were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature, and no plausible mechanism linking paromomycin to copper-associated cirrhosis. Paromomycin's nephrotoxicity and ototoxicity signals add caution. Evidence is at L5, and there is no basis to advance.

**To proceed, the following is needed:**
- Mechanistic evidence connecting paromomycin to copper metabolism or copper-associated liver injury
- Any preclinical or clinical data in this indication
- Mechanism of action data for paromomycin
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for DIN 02078759
- Route and exposure compatibility assessment, given minimal systemic absorption after oral use
- If the team wants to pursue other liver-related predictions, hepatopulmonary syndrome is the most mechanistically plausible candidate, but it would need its own evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

