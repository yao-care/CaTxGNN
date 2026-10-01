---
layout: default
title: Leucovorin
parent: Model Prediction Only (L5)
nav_order: 534
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Leucovorin: From Established Folate-Analogue Use to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (folinic acid) is a reduced folate marketed in Canada as an injectable calcium salt. The TxGNN model predicts it may be effective for **primary hyperoxaluria**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence data |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Leucovorin is a reduced folate that supports one-carbon metabolism and bypasses the DHFR enzyme. Whether that activity is relevant to primary hyperoxaluria cannot be verified from the supplied data.

Primary hyperoxaluria arises from defects in glyoxylate metabolism (for example AGXT, GRHPR or HOGA1 deficiency), which is not a known folate-dependent pathway. No direct mechanistic link to leucovorin is established, and any link would be speculative. The high TxGNN score (99.41%) is a knowledge-graph prediction and is not evidence of efficacy.

**Second-ranked prediction: congenital intrinsic factor deficiency (score 99.34%).**
- This one has a plausible but indirect link through the cobalamin-folate axis. Intrinsic factor deficiency causes vitamin B12 malabsorption, and its megaloblastic anaemia overlaps with folate-pathway dysfunction.
- In theory, leucovorin could correct the haematologic features by supplying reduced folate.
- It would not treat the underlying B12 deficiency, and it may mask anaemia while neurologic damage progresses.
- The standard of care is parenteral B12 replacement, so leucovorin would be adjunctive at most.
- No trials or literature were supplied for this indication either.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the nine authorizations are listed below. Dosage form and approved-indication text were not provided in the supplied records.

| DIN | Product Name |
|---------|------|
| 2496925 | LEUCOVORIN CALCIUM INJECTION |
| 2493357 | RIVA LEUCOVORIN |
| 2087316 | LEUCOVORIN CALCIUM INJECTION |
| 2548208 | JAMP LEUCOVORIN |
| 2182998 | LEUCOVORIN CALCIUM INJECTION USP |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions are supported only by the TxGNN model (evidence level L5). There are no registered trials or publications, and no verifiable mechanistic link for primary hyperoxaluria. The intrinsic factor deficiency link is plausible but only adjunctive, and it carries a risk of masking B12 deficiency.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to assess the mechanistic link
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Approved-indication and dosage-form data for the Canadian licences
- A targeted literature and trial search for leucovorin in primary hyperoxaluria and intrinsic factor deficiency
- For intrinsic factor deficiency, a clinical review of the risk of masking B12 deficiency
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

