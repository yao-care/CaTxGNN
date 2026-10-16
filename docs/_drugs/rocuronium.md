---
layout: default
title: Rocuronium
parent: Model Prediction Only (L5)
nav_order: 820
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rocuronium: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the licence data compiled for this report"
monitor_inn: "Rocuronium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
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

# Rocuronium: From Neuromuscular Blockade in Anaesthesia to Migraine Disorder

## One-Sentence Summary

Rocuronium is a non-depolarizing neuromuscular blocker given by injection. It is used in anaesthesia for muscle relaxation. The TxGNN model predicts it may be effective for **migraine disorder**, but the evidence is very weak: only **1 registered clinical trial** (a general pharmacokinetics study not designed to test migraine) and **no publications** directly support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, rocuronium is a non-depolarizing neuromuscular blocker. It competitively blocks nicotinic acetylcholine receptors at the motor endplate, producing skeletal muscle relaxation.

No established mechanism links this action to migraine. Migraine involves CGRP signalling, trigeminovascular activation and cortical spreading depression, none of which rocuronium is known to act on. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than a biologically grounded signal. The same applies to the other predicted indications (migraine with brainstem aura, cauda equina syndrome, irritable bowel syndrome, sciatic neuropathy and others), which also have no supporting trials or literature.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pharmacokinetics of understudied drugs given to children per standard of care. Not designed to test efficacy in migraine; the link is nonspecific (relevance grade C). |

## Literature Evidence

Currently no related literature available for migraine disorder.

For the related prediction "headache disorder", two publications were retrieved. Both are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | Clinical study | The journal of ECT | Compared succinylcholine with rocuronium-sugammadex for myalgia and headache after electroconvulsive therapy. Headache is a peri-procedural outcome, not a treatment target. |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | Case report | Pediatric emergency care | Propofol and remifentanil for rapid sequence intubation in a child at risk of aspiration with raised intracranial pressure. Not related to headache treatment. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02528657 | Rocuronium Bromide Injection | Injection | Not available |
| 02517744 | Rocuronium Bromide Injection | Injection | Not available |
| 02469774 | Rocuronium Bromide Injection | Injection | Not available |
| 02529831 | Rocuronium Bromide Injection | Injection | Not available |
| 02498820 | Rocuronium Bromide Injection | Injection | Not available |

Six valid single-ingredient licences are registered in total. The first five are shown above.

## Safety Considerations

- **Drug Interactions**: 73 interactions were identified in total. Examples from the first 20 reviewed:
  - **Major**: paromomycin, kanamycin, neomycin. Aminoglycosides can enhance neuromuscular blockade.
  - **Moderate**: magnesium sulfate, magnesium chloride, vancomycin, amphotericin B, tetracyclines (doxycycline, tetracycline, minocycline), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, prednisone), mannitol, metoclopramide.
  - **Minor**: ranitidine.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no plausible mechanistic basis and is supported only by a nonspecific pharmacokinetics study. Rocuronium is given intravenously in monitored settings and causes paralysis, so it is not a realistic candidate for migraine. The high TxGNN score is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Mechanism of action data (for example from DrugBank)
- Any mechanistic or clinical evidence linking neuromuscular blockade to migraine
- Assessment of route and setting compatibility with a migraine treatment context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

