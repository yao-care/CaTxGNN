---
layout: default
title: Pregabalin
parent: Model Prediction Only (L5)
nav_order: 761
evidence_level: L5
indication_count: 6
---

# Pregabalin
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

# Pregabalin: From Neuropathic Pain and Epilepsy to Tendinitis

## One-Sentence Summary

Pregabalin is marketed in Canada, and the published literature describes it as approved for partial epilepsy and neuropathic pain.
The TxGNN model predicts it may be effective for **tendinitis** with a high score (99.71%), but **no clinical trials** and **no studies directly on pregabalin for tendinitis** support this yet.
The prediction currently rests mainly on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuropathic pain and partial epilepsy (per published literature, PMID 30001248; the Canadian licence records contain no indication text) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (indirect evidence only; no tendinitis-specific studies) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. In general, pregabalin binds the alpha-2-delta subunit of voltage-gated calcium channels. This may reduce the release of excitatory neurotransmitters and dampen nociceptive and neuropathic pain signalling.

Tendinitis is mainly a painful mechanical and inflammatory condition of the tendon. Pregabalin could at most relieve the pain component, particularly where nerve irritation is involved. It has no known effect on the tendon pathology itself.

The related literature is indirect. It covers pain control after arthroscopic rotator cuff repair surgery and nerve-related pain syndromes, not tendinitis treatment. The high TxGNN score should therefore be read as a hypothesis, not as confirmed efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin versus single-shot interscalene block after arthroscopic rotator cuff repair; compares postoperative pain, opioid use and adverse effects. This is a surgical setting, not tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort | J Orthop Sci | Analgesic efficacy and opioid-sparing effect of pregabalin after rotator cuff repair; earlier studies gave conflicting results and evidence was described as limited. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Pract | Posterior femoral cutaneous nerve impingement linked to hamstring tendonitis in a marathon runner. Nerve-pain context only. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Commentary on piriformis syndrome (sciatic nerve compression) and its surgical management. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Fluoroquinolone-associated disability after ciprofloxacin, including tendinopathy as a side effect. Not about pregabalin treatment. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical (rat) | Adv Pharmacol Pharm Sci | Plant extract reduced vincristine-induced neuropathic pain in rats. Not related to pregabalin treatment of tendinitis. |

Overall, none of these studies tests pregabalin for tendinitis. The only pregabalin studies are on postoperative pain after shoulder surgery.

---

## Canada Market Information

20 licences (DINs) are on record. The five main ones are listed below. The records contain no dosage form or approved indication text for them.

| DIN | Product Name |
|---------|------|
| 02268418 | LYRICA |
| 02435977 | JAMP-PREGABALIN |
| 02436019 | JAMP-PREGABALIN |
| 02479133 | NRA-PREGABALIN |
| 02494892 | NAT-PREGABALIN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and no direct studies of pregabalin in tendinitis. The related literature concerns post-surgical or nerve-related pain, so the evidence is indirect (L4).

For comparison, among the other predictions for this drug, migraine disorder (L2, Research Question) has considerably more supporting evidence than tendinitis. That evidence includes pediatric RCTs and a follow-up study, although the dedicated Phase 3 trial was withdrawn.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence of pregabalin in tendinitis or tendinopathy pain
- Mechanism of action data (query DrugBank) to support the mechanistic-link analysis
- Health Canada product monograph (warnings and contraindications) for the safety screening
- Indication text, dosage form and route data for the Canadian licences, to assess route compatibility

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

