---
layout: default
title: Fremanezumab
parent: Moderate Evidence (L3-L4)
nav_order: 415
evidence_level: L4
indication_count: 2
---

# Fremanezumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Fremanezumab is a monoclonal antibody against calcitonin gene-related peptide (CGRP), marketed for migraine prevention.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**,
but there are **0 registered clinical trials** and only **20 publications**, mostly preclinical work, real-world cohorts in general migraine, and case reports.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (the Canadian license records provided contain no indication text) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fremanezumab is a monoclonal antibody that binds the CGRP ligand. CGRP is a potent vasodilator involved in trigeminovascular activation, which is central to migraine pathophysiology. Blocking it is the basis for the drug's use in migraine prevention.

Migraine with brainstem aura is a subtype of migraine, so the predicted indication is biologically close to the approved use. Aura is thought to arise from cortical spreading depression (CSD), and CGRP signalling has been linked to CSD. Two preclinical rat studies (PMID 31127003 and 31895266) found that fremanezumab slows CSD propagation and shortens cortical recovery, but does **not** prevent CSD from starting. Support for an effect on aura itself is therefore only partial.

The very high TxGNN score most likely reflects the close ontology relationship between this subtype and migraine, not independent evidence specific to brainstem aura. Evidence for this subtype is limited to case reports and a literature review (PMID 35268319).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomized controlled trials were found. The table lists the most relevant items, ordered from clinical to preclinical to background.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case reports + review | J Clin Med | Anti-CGRP antibodies are established for headache prevention, but evidence on preventing migraine aura is scarce |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational case series | CNS Neurosci Ther | Examines anti-CGRP therapy in migraine with aura; the abstract notes limited clinical evidence in this setting |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual patient quantitative analysis | J Headache Pain | Anti-CGRP antibodies in hemiplegic migraine, a rare aura subtype excluded from RCTs; evidence is limited |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case report + review | Front Neurol | Case of hemiplegic migraine treated with anti-CGRP antibodies; role in this subtype remains largely unexplored |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Post hoc subgroup analysis (phase 3b FOCUS) | Eur J Neurol | Efficacy and quality-of-life outcomes in difficult-to-treat migraine, with subgroups defined by aura or similar neurological symptoms (indirect) |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical (CSD animal model) | J Neurosci | CSD-induced arterial dilatation and plasma protein extravasation were unaffected by fremanezumab |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical (CSD animal model) | Pain | Slowed CSD propagation and shortened cortical recovery, but did not prevent CSD occurrence in rats with a compromised blood-brain barrier |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical | J Neurosci | Fremanezumab selectively inhibits trigeminovascular neurons |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Background review of CGRP's role in migraine, including aura in a subgroup of patients |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Prospective observational cohort | Front Neurol | Real-world efficacy and tolerability of fremanezumab in chronic migraine (indirect) |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2497859 | AJOVY |
| 2509474 | AJOVY |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on model output and on the subtype's closeness to migraine. There are no registered trials, and clinical support is limited to case reports and small observational series, while preclinical data show only a partial effect on the aura mechanism (CSD). The drug's safety profile in migraine prevention is established, but efficacy in this specific subtype is not.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Approved indication text for the Canadian licenses (DINs 2497859 and 2509474)
- Subtype-specific clinical evidence for brainstem aura, such as a registered prospective study or pooled analysis of case series
- Manual review and classification of the literature marked as pending, especially the hemiplegic migraine and aura studies

**Note on the second prediction:** *Atrophoderma vermiculata* (TxGNN score 99.04%) has no clinical trials, no literature, and no plausible mechanistic link to CGRP blockade. It is a model prediction only (evidence level L5, Hold) and should not be advanced without an independent biological rationale.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

