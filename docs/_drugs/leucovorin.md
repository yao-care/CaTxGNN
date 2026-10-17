---
layout: default
title: Leucovorin
parent: Model Prediction Only (L5)
nav_order: 539
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Leucovorin: predicted new indication Primary hyperoxaluria (evidence level L5). Approved use: Megaloblastic anemia"
monitor_inn: "LEUCOVORIN"
predicted_indications: ["primary hyperoxaluria", "congenital intrinsic factor deficiency"]
---

# Leucovorin
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

# Leucovorin: From Megaloblastic Anemia to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (folinic acid) is a reduced form of folate, originally used to treat megaloblastic anemia.
The TxGNN model predicts it may be effective for **primary hyperoxaluria**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Megaloblastic anemia |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, leucovorin is a reduced folate that bypasses dihydrofolate reductase and supports one-carbon metabolism, purine and thymidine synthesis, and homocysteine remethylation. Its efficacy in megaloblastic anemia is established.

Primary hyperoxaluria, however, arises from inherited defects in glyoxylate metabolism (AGXT, GRHPR, HOGA1) that cause oxalate overproduction. Folate-dependent pathways are not known to be central to this process, so **no direct mechanistic link is established**. A speculative connection might involve folate or B-vitamin cofactor roles in glyoxylate or one-carbon metabolism, or hyperhomocysteinemia associated with oxalate-related kidney impairment, but no supporting data is available.

The high TxGNN score (99.41%) is a model-derived prediction and is not corroborated by any trial or publication in the compiled data.

**A second prediction worth noting:** the model also ranks **congenital intrinsic factor deficiency** (score 99.34%, also L5, Hold). There is a plausible rationale: this condition impairs vitamin B12 absorption and causes secondary functional folate deficiency, which presents as megaloblastic anemia, and leucovorin can bypass that folate block. However, it does not correct the underlying B12 deficiency and may mask the anemia while neurological damage progresses. Parenteral vitamin B12 remains the necessary standard therapy, so leucovorin would at most be an adjunct. The high score is likely driven by overlap with the approved megaloblastic anemia indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02496925 | Leucovorin Calcium Injection | – | – |
| 02493357 | Riva Leucovorin | – | – |
| 02087316 | Leucovorin Calcium Injection | – | – |
| 02548208 | Jamp Leucovorin | – | – |
| 02182998 | Leucovorin Calcium Injection USP | – | – |

Nine valid single-ingredient authorizations are listed in total; the five above are shown. Indication text and dosage form were not available in the compiled data.

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text):** vitamin B12 deficiency and pernicious anemia. This is consistent with the risk that leucovorin can mask megaloblastic anemia while neurological damage from B12 deficiency progresses.
- **Drug Interactions:** 100 interactions were identified in total. The only ones with a graded severity are:
  - Pancrelipase: Moderate
  - Sulfasalazine: Minor

  Many others (e.g., metformin, omeprazole, pantoprazole, doxycycline, morphine, vancomycin) have no assigned severity level.

Please refer to the package insert for warnings and full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions rest on model output alone (L5), with no clinical trials or literature. For primary hyperoxaluria, no mechanistic link is established. For congenital intrinsic factor deficiency, the rationale is plausible, but B12 replacement is required and leucovorin could mask neurological harm.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Literature and trial searches for folate/folinic acid in primary hyperoxaluria and in B12-malabsorption disorders
- Mechanistic evidence for folate or one-carbon metabolism involvement in glyoxylate/oxalate handling
- Route and formulation compatibility assessment for the proposed indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

