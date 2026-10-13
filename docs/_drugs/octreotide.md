---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 676
evidence_level: L5
indication_count: 10
---

# Octreotide
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

# Octreotide: From Acromegaly to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a somatostatin analogue originally used for acromegaly, hyperpituitarism and carcinoid syndrome.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly, hyperpituitarism, carcinoid syndrome (no approved indication text is available from the Canadian licences) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, octreotide is a somatostatin analogue whose efficacy in acromegaly and carcinoid syndrome is established. It acts through somatostatin receptors, mainly in the pituitary and neuroendocrine tissue.

The predicted indication is a benign skin lesion. No somatostatin-receptor-mediated mechanism is documented for it. The high score most likely reflects shared associations among keratosis and skin-lesion nodes in the knowledge graph rather than a real biological link. The prediction should be treated as a computational hypothesis only.

Other predictions ranked highly for this drug are also weakly supported:
- **Seborrheic keratosis** (99.55%): prediction only, with no trials or publications.
- **Addison disease** (98.74%): three publications, all of low relevance. One is a case report of an ACTH response to octreotide in a probable corticotropic adenoma. One is a 1990 study that found no acute effect on pituitary-adrenal function. One is a diagnostic imaging study. Octreotide would not treat adrenal destruction.
- **Adrenocortical insufficiency** (98.47%): one descriptive pituitary pathology study that does not test octreotide.
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

