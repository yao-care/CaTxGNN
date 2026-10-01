---
layout: default
title: Belimumab
parent: Model Prediction Only (L5)
nav_order: 97
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a monoclonal antibody that blocks the B-cell survival factor BLyS. It is known for treating autoimmune disease, mainly systemic lupus erythematosus (SLE), although the Evidence Pack does not record its approved indication.
The TxGNN model ranks **primary release disorder of platelets** as the top new candidate, with a very high score, but only **1 clinical trial** (in a different disease) and **0 publications** support it.
The high score looks like a graph-proximity artefact rather than real biology, so this candidate should be treated as unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus (from general knowledge; the licence indication text in the Evidence Pack is blank) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general knowledge, belimumab inhibits soluble BLyS (BAFF), which lowers B-cell survival and autoantibody production. That mechanism suits antibody-driven autoimmune diseases.

**For the top prediction, the mechanistic link is weak.** Primary platelet release disorders are inherited defects of granule secretion or signalling and are not antibody-mediated. B-cell/BLyS blockade has no clear target there. The score of 0.9996 most likely reflects proximity in the knowledge graph rather than biology.

The other five predicted indications do not fare better, with one exception:

| Rank | Predicted Indication | Score | Mechanistic Assessment |
|------|------|------|------|
| 1 | Primary release disorder of platelets | 99.96% | No credible link (inherited, non-immune) |
| 2 | Pseudo-von Willebrand disease | 99.96% | No plausible target (GP1BA gain-of-function variants) |
| 3 | Glanzmann thrombasthenia | 99.88% | Belimumab does not address integrin αIIbβ3 deficiency. The only tenuous link is alloantibodies after platelet transfusion, which is a complication, not the disease |
| 4 | Fetal and neonatal alloimmune thrombocytopenia (FNAIT) | 99.59% | **Most plausible.** Maternal anti-HPA-1a alloantibodies drive the disease, so B-cell/plasma-cell signals are a conceivable target |
| 5 | Severe nonproliferative diabetic retinopathy | 99.05% | No established role for BLyS or B-cell depletion |
| 6 | Autosomal dominant macrothrombocytopenia | 99.04% | Inherited cytoskeletal defects (e.g., TUBB1, ACTN1, MYH9), not immune-mediated |

FNAIT is the only candidate worth keeping as a research question. Belimumab is an IgG1 antibody that would cross the placenta, and pregnancy safety data are limited. Any further work would need a dedicated safety and feasibility review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label mechanistic study of belimumab (10 mg/kg IV) in anti-PLA2R–positive idiopathic membranous glomerulonephropathy. It did not study platelet disorders (relevance grade C), so it offers no direct or indirect support. It only shows belimumab has been tested in another autoantibody-mediated disease. |

No clinical trials were found for the other five predicted indications.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2370050 | BENLYSTA |
| 2470489 | BENLYSTA |
| 2370069 | BENLYSTA |

Dosage forms, manufacturers, and approved indication text are blank in the Evidence Pack for all three authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions are not backed by a plausible mechanism, and no trial or publication supports any of them. The one completed trial studied a different disease. All candidates are at evidence level L5. FNAIT is the only biologically plausible one and can be logged as a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For FNAIT: a literature search, then a dedicated pregnancy and placental-transfer safety review
- The approved indication text for the Canadian licences, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

