---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 676
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Octreotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Octreotide: Vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Octreotide is a somatostatin analogue originally used for acromegaly, hyperpituitarism and carcinoid syndrome.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 11 of 14) |
| Number of DINs | 14 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, octreotide is a somatostatin analogue whose efficacy in acromegaly and carcinoid syndrome is established. It acts through somatostatin receptors, mainly in the pituitary and neuroendocrine tissue.

The predicted indication is a benign skin lesion. No somatostatin-receptor-mediated mechanism is documented for it. The high score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a computational hypothesis only.

Other predictions ranked highly for this drug are also weakly supported:
- **Seborrheic keratosis** (0.9955): prediction only, with no trials or publications.
- The remaining predictions are rare renal and inflammatory conditions with no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02248640 | OCTREOTIDE ACETATE OMEGA | Not specified | Not specified |
| 00839191 | SANDOSTATIN | Not specified | Not specified |
| 02503778 | OCTREOTIDE FOR INJECTABLE SUSPENSION | Not specified | Not specified |
| 02239323 | SANDOSTATIN LAR | Not specified | Not specified |
| 02560291 | OCTREOTIDE INJECTION | Not specified | Not specified |

These are 5 of the 14 valid single-ingredient authorizations. None are cancelled.

## Cytotoxicity

Octreotide is not a cytotoxic anticancer drug. It is a hormone-modulating peptide, so this section does not apply.

## Safety Considerations

- **Contraindications and disease associations (from the knowledge graph, not label text)**: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypoglycaemia, hypothyroidism (including myxedema and congenital hypothyroidism), liver disease and cirrhosis, gallbladder disease and gallstones (cholelithiasis, cholecystolithiasis, choledocholithiasis), ileus, intestinal obstruction, sudden cardiac arrest, heart conduction disease, kidney failure, uraemia and vitamin B12 deficiency.
- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed here are all Moderate severity. Most involve glucose-lowering agents, which fits the glycaemic effects above. Examples include insulins (aspart, degludec, detemir, glargine, glulisine, human), metformin, acarbose, glimepiride, chlorpropamide, the GLP-1 agonists albiglutide, dulaglutide and semaglutide, the DPP-4 inhibitors alogliptin and linagliptin, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin.

Please refer to the package insert for official warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or literature, and no plausible mechanism links somatostatin-receptor agonism to vulvar inverted follicular keratosis. Evidence is at level L5. The other top-ranked predictions are also unsupported or only weakly supported.

**To proceed, the following is needed:**
- Mechanism of action data for octreotide
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- A biological rationale or preclinical evidence linking somatostatin signalling to the predicted skin condition
- Review of other predictions with some biological plausibility, such as pituitary-related ACTH disorders, though current data are largely negative or indirect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

