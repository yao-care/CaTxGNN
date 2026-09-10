---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Linaclotide: From Data-Gap Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Linaclotide is a guanylate cyclase-C (GC-C) agonist that acts locally on the intestinal epithelium; its originally approved indication is not recorded in this evidence pack (data gap). TxGNN predicts it may be effective for **Cauda Equina Syndrome**, but **0 clinical trials** and **0 publications** currently support this direction, and the evidence pack's own mechanistic review flags the signal as likely a knowledge-graph artifact rather than a genuine pharmacological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — no indication or DIN records in this pack) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (original_moa: data gap). Based on the information captured in this pack, linaclotide's known pharmacology is a GC-C agonist that promotes intestinal fluid secretion by acting locally on gut epithelium; its systemic bioavailability is very low, so it is not expected to reach or act on central or non-gut tissue.

Cauda equina syndrome, however, is a neurosurgical emergency caused by nerve root compression (bladder/bowel/perineal sensorimotor dysfunction), requiring urgent surgical decompression — it is not a pathology treatable by any drug, let alone one confined to the gut lumen. The evidence pack's own rationale is explicit that linaclotide's GC-C mechanism has no plausible link to nerve compression itself, and at most could address a downstream secondary symptom (neurogenic constipation).

Taken together with the model's rank/score, this looks like a case where TxGNN's high confidence score reflects proximity in the knowledge graph (shared "bowel dysfunction" or comorbidity nodes) rather than a real causal or mechanistic relationship. The same caveat applies to the other two ranked predictions for this drug (neurogenic bladder, insomnia), both of which the pack itself flags as mechanistically unsupported or graph-noise artifacts — reinforcing that this candidate should be treated as a low-confidence signal rather than a genuine repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Linaclotide currently has no Canadian market authorizations recorded in this pack (market status: not marketed, 0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Health Canada label warnings and contraindications are marked as a **Blocking** data gap in this pack — this alone prevents progression to the S1 safety screening stage.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, S0) with zero supporting clinical trials or literature, and the pack's own mechanistic analysis concludes the drug-disease link is biologically implausible (likely a knowledge-graph proximity artifact rather than a real mechanism) for cauda equina syndrome, a surgical emergency not amenable to any drug therapy.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action (MOA) documentation for linaclotide from DrugBank or primary literature
- Independent mechanistic or preclinical evidence connecting GC-C agonism to any component of cauda equina pathology, before any further clinical evaluation
- Given the weak plausibility across all three ranked predictions for this drug, consider deprioritizing this candidate relative to others with stronger mechanistic or evidentiary support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

