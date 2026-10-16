---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 684
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Olsalazine: predicted new indication Myelodysplastic syndrome (evidence level L5). Approved use: Not stated in the Canadian licence data"
monitor_inn: "Olsalazine"
predicted_indications: ["myelodysplastic syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "partial deletion of the long arm of chromosome 5", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
---

# Olsalazine
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

# Olsalazine: From Inflammatory Bowel Disease Therapy to Myelodysplastic Syndrome

## One-Sentence Summary

Olsalazine is a dimer of 5-aminosalicylic acid (5-ASA), an anti-inflammatory agent that acts locally in the colon. The TxGNN model predicts it may be effective for **myelodysplastic syndrome**, but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, olsalazine is a 5-ASA dimer that colonic bacteria cleave into two active molecules. Its anti-inflammatory effects (local COX and lipoxygenase inhibition, NF-kB and PPAR-gamma modulation) act mainly on the gut lining, and very little of the drug is absorbed into the bloodstream.

The review found no plausible mechanistic link between this action and myelodysplastic syndrome, a clonal bone marrow disorder. The high TxGNN score appears to come from patterns in the knowledge graph rather than from any validated biology. The other top predictions point the same way:

- **Bone marrow and blood disorders:** unclassified myelodysplastic syndrome, refractory cytopenia of childhood, aregenerative anemia, severe congenital hypochromic anemia with ringed sideroblasts, and partial deletion of the long arm of chromosome 5. The del(5q) abnormality is a cytogenetic finding rather than a treatable disease, and it likely reflects the same cluster of predictions as myelodysplastic syndrome.
- **Hair disorders:** hypotrichosis simplex of the scalp, congenital hypotrichosis milia, alopecia, and diffuse alopecia areata. Alopecia areata is T-cell-mediated autoimmunity, which olsalazine's local mucosal action does not target.

For aregenerative anemia, the relationship may point toward harm instead of benefit. Drugs in the 5-ASA class have rare reports of blood disorders, including aplastic anemia, as adverse effects.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02063808 | DIPENTUM | Not stated | Not stated |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

**Drug Interactions:** The interaction screening returned 100 potential interactions. The first 20 are summarised below.

- **Major:**
  - Human immunoglobulin G (intravenous)
  - Human botulinum neurotoxin A/B immune globulin
  - Cidofovir
  - Iothalamic acid
- **Moderate:**
  - NSAIDs: ketorolac, ibuprofen, celecoxib, diclofenac
  - Antimicrobials and antivirals: acyclovir, amikacin, bacitracin, capreomycin, colistimethate
  - Amphotericin B (including the lipid complex)
  - Azathioprine
  - Ibandronate
  - Chlorpropamide
  - Cisplatin
  - Clofarabine

Many of these are nephrotoxic agents, so kidney function would need attention if any are combined with olsalazine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the knowledge-graph model. There are no clinical trials or publications, and no mechanistic link exists between a locally acting gut anti-inflammatory drug with minimal systemic absorption and a bone marrow disorder. The safety data also has gaps.

**To proceed, the following is needed:**
- Mechanism of action data for olsalazine
- Package insert warnings and contraindications from Health Canada
- Preclinical or mechanistic evidence linking 5-ASA to haematopoietic or myelodysplastic biology
- A literature and trial search specific to olsalazine or 5-ASA in myelodysplastic syndrome
- A review of the haematological safety signals associated with 5-ASA-class drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

