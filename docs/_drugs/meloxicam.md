---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Meloxicam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# MELOXICAM: From Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a preferential COX-2 inhibitor NSAID, widely approved internationally for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis — though it is **not currently registered in Canada** based on the available data in this evidence pack.
The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type** (score: 99.92%), an ultra-rare skeletal dysplasia with **no clinical trials or publications** currently supporting this direction.
Across all 10 predicted indications evaluated, the strongest available evidence supports use in **RF-positive polyarticular juvenile idiopathic arthritis** (rank 8, L3, 1 publication), which also carries established pharmacological rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canada regulatory records available (Meloxicam is internationally approved for osteoarthritis and rheumatoid arthritis) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacological knowledge, Meloxicam is a preferential COX-2 (cyclooxygenase-2) inhibitor of the oxicam NSAID class. By selectively suppressing COX-2 over COX-1, it reduces prostaglandin synthesis at sites of inflammation with a relatively reduced gastrointestinal side-effect burden compared to non-selective NSAIDs. This mechanism is the pharmacological basis for its efficacy in chronic inflammatory musculoskeletal conditions globally.

Reviewing all 10 TxGNN predictions reveals a consistent pattern: 7 of the top 10 are ultra-rare skeletal dysplasias or complex genetic syndromes (acromesomelic dysplasia, brachyolmia, pseudoachondroplasia, WHIM syndrome, colobomatous microphthalmia-rhizomelic dysplasia, etc.) where COX-2 inhibition has no established disease-modifying role. The mechanistic rationale fields in the evidence pack explicitly flag that these high scores likely reflect **knowledge graph node clustering effects** — rare skeletal diseases share overlapping structural features in the TxGNN knowledge graph with bone and joint diseases where NSAIDs are therapeutically relevant. This is a recognised artifact of graph-based drug repurposing models and should not be interpreted as mechanistic plausibility.

The two predictions with the most credible biological rationale are **Spondyloarthropathy, susceptibility to** (rank 6, L4) and **RF-positive polyarticular juvenile idiopathic arthritis** (rank 8, L3). NSAIDs — and Meloxicam specifically — are guideline-recommended first-line therapy for spondyloarthropathies including ankylosing spondylitis, with approved indications in the EU and US. Meloxicam has also received US FDA approval for JIA in children aged ≥2 years. These findings are consistent with known COX-2 pharmacology and represent the most actionable predictions in this dataset.

---

## Clinical Trial Evidence

No clinical trials are currently registered for Meloxicam in **Acromesomelic Dysplasia, Hunter-Thompson Type** (the top-ranked TxGNN prediction).

> No clinical trials were identified across any of the 10 predicted indications evaluated in this analysis.

---

## Literature Evidence

No literature is available for the top-ranked prediction (Acromesomelic Dysplasia, Hunter-Thompson Type).

The only publication identified across all 10 predicted indications is for **rank 8: RF-positive polyarticular juvenile idiopathic arthritis**:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Retrospective Cohort / Safety Analysis | Pediatric Rheumatology Online Journal | Phase 4 registry assessing long-term safety of celecoxib vs. non-selective NSAIDs (class including Meloxicam) in JIA patients in routine clinical practice; provides real-world NSAID safety profile data in the paediatric JIA population |

---

## Canada Market Information

Meloxicam currently has **no registered products in Canada** (0 DINs) according to the evidence pack.

> This finding may reflect a data gap rather than confirmed absence. Meloxicam is commercially available in the United States, the European Union, and many other international markets. Direct verification against the Health Canada Drug Product Database (DPD) is strongly recommended before drawing conclusions about market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data — including warnings, contraindications, and drug-drug interactions — were not available in the current evidence pack (all fields reported as data gaps). Based on NSAID class pharmacology, key areas requiring assessment include: cardiovascular thromboembolic risk, gastrointestinal haemorrhage risk, renal function effects, avoidance in the third trimester of pregnancy, and interactions with anticoagulants, antihypertensives, and other NSAIDs. Full safety evaluation requires review of the official Canadian product monograph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (Acromesomelic Dysplasia, Hunter-Thompson Type, L5) carries no supporting clinical or preclinical evidence and the mechanism lacks biological plausibility; the high TxGNN score is most likely an artefact of skeletal disease node clustering in the knowledge graph. Notwithstanding, the analysis surfaces **RF-positive polyarticular JIA** (rank 8, L3) and **spondyloarthropathy** (rank 6, L4) as more clinically actionable directions with existing pharmacological rationale and indirect evidence support from international approvals — these merit a dedicated follow-up evaluation.

**To proceed, the following is needed:**

- **Confirm Canada registration status** — verify directly against Health Canada Drug Product Database; the 0-DIN result may be a data gap
- **Retrieve safety data** — obtain contraindications, warnings, and DDI profile from the official Canadian product monograph (Data Gap DG001, classified Blocking)
- **Obtain MOA data** — query DrugBank API for full mechanistic annotation (Data Gap DG002, classified High)
- **Targeted literature search for JIA** — conduct a focused PubMed/Embase search for Meloxicam specifically in paediatric RF-positive polyarticular JIA to characterise evidence depth beyond PMID 25057265
- **Spondyloarthropathy pathway assessment** — evaluate whether existing EU SmPC or US FDA approvals for ankylosing spondylitis could support a Health Canada submission under Class 5 or data-bridging pathways
- **Mechanistic plausibility review for skeletal dysplasias** — if any of the ultra-rare skeletal predictions are to be pursued, a formal mechanistic hypothesis must be established prior to any experimental work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

