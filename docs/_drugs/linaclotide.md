---
layout: default
title: Linaclotide
parent: Model Prediction Only (L5)
nav_order: 550
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "LINACLOTIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
description: "Linaclotide: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Linaclotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Linaclotide: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Linaclotide is a guanylate cyclase-C agonist originally used for irritable bowel syndrome (IBS). The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this rests on a computational prediction alone: **0 clinical trials** and **0 publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Linaclotide is a guanylate cyclase-C (GC-C) agonist. It raises cGMP levels in the intestinal lining. Preclinical work suggests that extracellular cGMP may reduce the activity of visceral pain-sensing nerves, which could theoretically relate to neuropathic or visceral pain.

The link to the new indication is weak. Cauda equina syndrome is a neurological emergency caused by compression of the nerve roots at the base of the spine, and the standard treatment is surgical decompression. Linaclotide is barely absorbed into the bloodstream, so there is no established way it could act on compressed nerve roots. The high TxGNN score probably reflects the model's network proximity to bowel and bladder dysfunction features, not a real therapeutic mechanism. At most, linaclotide might be considered for secondary neurogenic bowel symptoms, which is a different indication.

Detailed mechanism-of-action data was not available in the data compiled for this report, so the reasoning above relies on general pharmacological knowledge.

The TxGNN model (deep learning) also lists Clostridium difficile colitis and neurocirculatory asthenia as associations. These come from the model and may reflect similarities the model learned between related diseases, not biological evidence. They are not approved uses.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02469510 | CONSTELLA | Not specified | Not specified |
| 02417162 | CONSTELLA | Not specified | Not specified |
| 02417170 | CONSTELLA | Not specified | Not specified |

All three authorizations are valid single-ingredient products.

## Safety Considerations

**Drug Interactions**: The interaction screen found 56 interacting drugs in total. The 20 entries in the data compiled for this report are mostly minor. The moderate-level interactions are:
- Levonorgestrel
- Ethinylestradiol
- Norethisterone
- Levothyroxine
- Thyroid, porcine

Minor interactions include proton pump inhibitors (rabeprazole, esomeprazole, dexlansoprazole), NSAIDs (ibuprofen, ketorolac, diclofenac, oxaprozin, bromfenac) and other laxatives or bowel-preparation agents (bisacodyl, docusate, castor oil, picosulfuric acid, polyethylene glycol).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials or publications. Cauda equina syndrome is a compressive emergency treated surgically, and linaclotide's minimal systemic absorption gives it no plausible direct effect. The high score is likely an artifact of network proximity to bowel and bladder symptoms.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Detailed mechanism-of-action data
- Preclinical or clinical evidence in a relevant nerve compression or neuropathic pain model
- Consideration of a more clinically coherent target, such as neurogenic bowel dysfunction, instead of cauda equina syndrome itself
- Review of the other predicted indications (neurogenic bladder, insomnia), which currently have no evidence assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

