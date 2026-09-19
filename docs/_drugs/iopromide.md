---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Contrast Agent to Osteoarthritis Susceptibility

## One-sentence Summary

Iopromide is a nonionic, low-osmolarity iodinated contrast agent whose original purpose is contrast enhancement in imaging procedures such as CT and angiography, not a drug for treating specific diseases. The TxGNN model predicts a possible association with **osteoarthritis susceptibility**, but currently **0 clinical trials and 0 literature reports** support this association. The evidence level is lowest, and the high score is suspected to be a false positive resulting from knowledge graph confusion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original indication | Contrast agent (CT/angiography image enhancement), non-therapeutic use; Not marketed in Canada, no approved indication records |
| Predicted new indication | Osteoarthritis susceptibility |
| TxGNN prediction score | 99.57% (rank 8382) |
| Evidence level | L5 (model prediction only, no actual research) |
| Canadian market status | Not marketed |
| DIN count | 0 |
| Recommended decision | Hold |

---

## Why Might This Prediction Appear Reasonable?

Currently, there is no detailed mechanism of action (MOA) data available. Based on available information, iopromide belongs to the nonionic, low-osmolarity iodinated contrast agent family, with clinical applications limited to contrast enhancement in imaging diagnosis such as CT and angiography. It has no known pharmacological therapeutic mechanism and has not been approved for treatment of any disease.

From a mechanistic perspective, there is no known biological link between contrast agents and osteoarthritis—the pathophysiology of osteoarthritis involves cartilage degeneration, joint inflammation, and osteophyte formation, whereas contrast agents only act on X-ray attenuation properties to facilitate image interpretation and lack anti-inflammatory, cartilage-protective, or repair-related pharmacological activity.

The prediction rationale within the evidence package for the same drug regarding rank 2 (osteoarthritis) has already clearly indicated that the high score given by TxGNN likely originates from knowledge graph confusion—because contrast agents are frequently used in literature related to "disease imaging diagnosis" and co-occur at high frequency with various disease names, the model misinterprets them as therapeutic associations rather than genuine therapeutic signals. This pattern of confusion equally applies to the present rank-1 osteoarthritis susceptibility prediction, and moreover, this item lacks even a single co-occurrence literature citation, making mechanistic plausibility even weaker.

---

## Clinical Trial Evidence

Currently, there are no relevant clinical trial registrations.

---

## Literature Evidence

Currently, there are no relevant literature data.

---

## Canadian Market Information

Iopromide is currently **Not marketed** in Canada, with no valid drug license (DIN) records, so information on approved indications or dosage forms cannot be provided.

---

## Safety Considerations

Please refer to the drug product monograph for safety information.

(Note: This evidence package marks a blocking-level data gap DG001—TFDA product monograph warnings/contraindications have not yet been obtained, which is a necessary prerequisite for entering preliminary safety assessment; see "Follow-up Requirements" below.)

---

## Conclusion and Follow-up Recommendations

**Decision: Hold**

**Rationale:**
Iopromide is a contrast agent and not a therapeutic drug, with no reasonable mechanistic link to osteoarthritis susceptibility; this prediction lacks any clinical trial or literature support (0/0), and the evidence level is the lowest L5. Similar high-scoring items in the same batch of predictions have been shown to potentially be false positive signals due to knowledge graph confusion. Additionally, it is noteworthy that the same drug shows **opposing safety signals** in the hemoglobinopathy (rank 9) direction—literature reports that low-osmolarity intravenous contrast agents may trigger cerebrovascular occlusion events in patients with sickle cell disease, suggesting that such contrast agents warrant extra caution when used in drug repurposing assessments.

**To proceed further, the following need to be supplemented:**
- TFDA/Canadian official product monograph warnings and contraindication data (DG001, blocking-level, must be resolved before entry into preliminary safety assessment)
- Complete mechanism of action (MOA) data (DG002)
- Independent mechanistic hypotheses or preclinical experimental data demonstrating a reasonable link between contrast agents and osteoarthritis pathophysiology
- Specialized signal validation analysis to determine whether the TxGNN high score is a knowledge graph confusion resulting from co-occurrence of contrast agent/imaging literature

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

