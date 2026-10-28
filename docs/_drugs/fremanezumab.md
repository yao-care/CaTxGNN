---
layout: default
title: Fremanezumab
parent: Model Prediction Only (L5)
nav_order: 418
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "FREMANEZUMAB"
predicted_indications: ["atrophoderma vermiculata"]
description: "Fremanezumab: predicted new indication Atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Fremanezumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fremanezumab: Atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Fremanezumab is a humanized monoclonal antibody that targets the CGRP ligand and is used for migraine prevention.
The TxGNN model predicts it may be effective for **atrophoderma vermiculata**,
but there are currently **no registered clinical trials** and only indirect support from **20 publications**, mostly reviews, observational studies and preclinical work in general migraine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9904 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fremanezumab is a humanized monoclonal antibody that binds the CGRP ligand. CGRP is a key mediator in the trigeminovascular system, and fremanezumab is used to prevent migraine. The literature reviewed describes CGRP as central to migraine pathophysiology (PMID 30725283, 28642283).

Migraine with brainstem aura is a migraine subtype, so it shares the trigeminovascular and CGRP-mediated pathways of the parent disease. This gives a plausible mechanistic rationale. Observational reports of anti-CGRP antibodies in migraine with aura and in hemiplegic migraine (a related aura subtype) point in the same direction, but they are small or case-level studies.

There are important caveats. The supplied literature covers general episodic and chronic migraine and does not address brainstem aura specifically. The pivotal Phase 3 trials (HALO, FOCUS) enrolled general migraine populations and typically did not analyze aura subtypes separately. A preclinical study (PMID 31127003) found that fremanezumab did not affect cortical spreading depression-induced vascular changes, so its effect on aura mechanisms remains uncertain. The evidence is therefore indirect and extrapolated from the parent indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38091211](https://pubmed.ncbi.nlm.nih.gov/38091211/) | 2024 | Cohort (pilot, prospective) | Neurol Sci | Examines whether anti-CGRP antibodies are effective in preventing migraine aura |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Case series | CNS Neurosci Ther | Observational case series on the effect of anti-CGRP therapy on migraine aura |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Systematic review | J Headache Pain | Individual patient analysis of anti-CGRP antibodies in hemiplegic migraine, a rare aura subtype |
| [41589756](https://pubmed.ncbi.nlm.nih.gov/41589756/) | 2026 | Case report | Eur J Neurol | Fewer prolonged sporadic hemiplegic migraine attacks after fremanezumab |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Cohort (post hoc) | Eur J Neurol | Fremanezumab efficacy and quality-of-life gains in difficult-to-treat migraine, including patients with aura or similar neurological dysfunction |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Cohort | Front Neurol | Real-world 3-month study of fremanezumab efficacy and tolerability in chronic migraine |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical | J Neurosci | Fremanezumab did not alter cortical spreading depression-induced arterial dilatation or plasma protein extravasation |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical | J Neurosci | Fremanezumab selectively inhibits trigeminovascular neurons |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Role of CGRP in migraine pathophysiology |
| [42090640](https://pubmed.ncbi.nlm.nih.gov/42090640/) | 2026 | Cohort | Neurology | Multinational cohort study of glaucoma risk with CGRP inhibitors in migraine |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02497859 | AJOVY | Not listed | Not listed |
| 02509474 | AJOVY | Not listed | Not listed |

## Safety Considerations

- **Emerging safety signals (literature)**: Two recent cohort studies examine glaucoma risk (PMID 42090640) and cerebrovascular risk, namely ischemic stroke or transient ischemic attack (PMID 42390441), with CGRP-pathway inhibitors. These warrant attention, particularly in patients with aura-related neurological symptoms.

For other safety information, including warnings, contraindications and drug interactions, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible because brainstem aura is a migraine subtype and fremanezumab is already used for migraine prevention. However, there are no registered trials, the supporting literature is indirect (reviews, small observational studies, case reports), and the preclinical data leave the effect on aura mechanisms uncertain. The package insert warnings and contraindications for the Canadian products have not yet been reviewed, which blocks safety screening.

**To proceed, the following is needed:**
- Review of the Health Canada package insert for warnings, contraindications and approved indications
- Detailed mechanism of action data
- Aura-subtype analyses of existing Phase 3 data, or prospective studies in brainstem aura
- Assessment of the glaucoma and cerebrovascular safety signals in this population

---

**Note on the second predicted indication:** The model also predicted atrophoderma vermiculata (score 0.9904). There are no clinical trials or literature for it, and no plausible mechanistic link to CGRP neutralization is evident. It is likely a TxGNN model (deep learning) artifact, and the recommendation is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

