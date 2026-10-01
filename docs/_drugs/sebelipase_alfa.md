---
layout: default
title: Sebelipase Alfa
parent: Model Prediction Only (L5)
nav_order: 830
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

Sebelipase alfa (marketed in Canada as KANUMA) is a recombinant human enzyme used for lysosomal acid lipase (LAL) deficiency.
The TxGNN model's top-ranked prediction is **Scheie syndrome** (an attenuated form of MPS I), but **0 clinical trials** and **0 publications** support it, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lysosomal acid lipase deficiency (from the published literature; the Canadian label text is not in the supplied data) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Sebelipase alfa is recombinant human LAL. It replaces the deficient enzyme and breaks down accumulated cholesteryl esters and triglycerides in LAL deficiency.

**This prediction is not mechanistically supported.** Scheie syndrome is caused by a deficiency of alpha-L-iduronidase, which degrades glycosaminoglycans. LAL does not act on this substrate, so there is no plausible LAL-mediated mechanism. The high score most likely reflects a shared "lysosomal storage disease / enzyme replacement therapy" signal in the knowledge graph.

**Other predictions in the list.** The same pattern holds for most of the other entries:
- Hurler syndrome, Gaucher disease, Tay-Sachs disease, and several non-specific or unrelated diseases have no mechanistic link to LAL replacement.
- **Cholesteryl ester storage disease** (rank 4) and **Wolman disease** (rank 5) are the two phenotypes of LAL deficiency itself. They are probably the drug's existing labeled use, not true repurposing, so the empty original-indication field in the input is likely a data gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Scheie syndrome.

---

## Literature Evidence

Currently no related literature available for Scheie syndrome.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2469596 | KANUMA |

Dosage form and approved-indication text were not available for this authorization.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Scheie syndrome rests on a model score alone, with no trials, no literature, and no plausible mechanism, since LAL does not degrade glycosaminoglycans. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- Any evidence that links LAL replacement to iduronidase deficiency. None exists in the current data.
- The Health Canada package insert, including approved indication, warnings, and contraindications.
- Mechanism of action data from DrugBank.
- A re-evaluation focused on the LAL deficiency entries (cholesteryl ester storage disease and Wolman disease). These have a completed Phase 3 randomized placebo-controlled trial (NCT01757184, n=66), several Phase 2 studies, and cohort and registry data, and are likely on-label use rather than repurposing. Confirm that the Wolman entry (a composite label including hypolipoproteinemia and acanthocytosis) maps to classic Wolman disease.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

