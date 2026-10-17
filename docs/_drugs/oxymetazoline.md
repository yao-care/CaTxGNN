---
layout: default
title: Oxymetazoline
parent: Moderate Evidence (L3-L4)
nav_order: 696
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Oxymetazoline: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Pharyngitis, common cold"
monitor_inn: "Oxymetazoline"
predicted_indications: ["nasal cavity disease", "headache disorder"]
---

# Oxymetazoline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Oxymetazoline: From Pharyngitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Oxymetazoline is a topical sympathomimetic decongestant, originally used for pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but there are currently **no registered clinical trials** and only **5 publications**, mostly indirect (one animal study, one physiology study, and several case reports or procedural papers).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, oxymetazoline is a topical alpha-adrenergic agonist. Pharmacology data show it binds alpha-1 (A, B, D) and alpha-2 (A, B, C) adrenoceptors, as well as the serotonin receptors 5-HT1B, 5-HT1D and 5-HT2C. Through alpha-adrenergic vasoconstriction of nasal mucosal vessels, it reduces congestion and improves nasal airflow.

The original indications (common cold, pharyngitis) involve upper-airway mucosal congestion, and "nasal cavity disease" is a very broad category in the same anatomical region. Nasal congestion relief is already the marketed use of oxymetazoline, so the high TxGNN score (0.9996) mostly reflects overlap with existing use rather than a truly new indication. The repurposing novelty is therefore limited. Conditions with a vascular or congestive component (rhinitis, sinusitis) are the most plausible extensions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Clinical study | Ann N Y Acad Sci | Effects of the common cold (acute rhinitis) on olfactory function in 36 subjects, measured with evoked potentials, psychophysical tests and acoustic rhinometry |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal study | Ann Otol Rhinol Laryngol | Oxymetazoline nose drops in a rabbit model of acute bacterial sinusitis, evaluating the effect on local tissue defense against infection |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Procedural study | Am J Rhinol Allergy | Endoscopic coblation treatment of nasal telangiectasias in hereditary hemorrhagic telangiectasia |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Clinical study (diagnostic) | J Plast Surg Hand Surg | Nasal patency measured by acoustic rhinometry in children after cleft lip and palate repair |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Glob Pediatr Health | Rhinoscleroma in a 9-year-old boy |

Most of these papers mention oxymetazoline only incidentally (for example as a decongestant in assessments or procedures), so none provides direct efficacy evidence for a new indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02498294 | DRIXORAL NO DRIP NASAL CONGESTION | Not specified | Not specified |
| 02380129 | DRIXORAL NASAL CONGESTION | Not specified | Not specified |
| 02460599 | NASAL CONGESTION SPRAY | Not specified | Not specified |
| 00740861 | DRIXORAL DECONGESTANT NASAL SPRAY | Not specified | Not specified |
| 01929380 | LONG LASTING DRISTAN MENTHOLATED NASAL SPRAY | Not specified | Not specified |

Thirteen valid single-ingredient licences are listed in total; the five above are shown as the main examples.

---

## Safety Considerations

- **Contraindications / cautions from the knowledge graph** (not label text): hypertension and other hypertensive disorders, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, heart disease, cardiovascular disease, coronary artery disease, arteriosclerosis/atherosclerosis, angle-closure glaucoma, hyperthyroidism (Graves disease, thyrotoxicosis), eye infectious disease and conjunctivitis, vision disorder and blindness.
- **Drug interactions:** The interaction query returned 9 entries, all pharmacological target bindings rather than drug-drug interactions: alpha-1A/1B/1D and alpha-2A/2B/2C adrenoceptors, and 5-HT1B, 5-HT1D and 5-HT2C receptors. A literature review (PMID 36425231) also notes that sympathomimetics may interact with monoamine oxidase inhibitors (MAOIs), which is relevant to guardrails.

Please refer to the package insert for label-based warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but there are no clinical trials, and the literature is indirect or incidental. The predicted indication largely overlaps with the existing marketed use (nasal congestion), so the repurposing value is low. Evidence stays at L4 (preclinical and mechanism-level).

**To proceed, the following is needed:**
- Narrow "nasal cavity disease" to specific conditions (for example rhinitis, sinusitis) and define a testable hypothesis
- Direct clinical studies of oxymetazoline for the defined condition
- Mechanism of action data and Health Canada package insert warnings and contraindications (currently missing, which blocks safety screening)
- Approved indication text, dosage form and manufacturer details for the Canadian licences
- A safety plan covering cardiovascular disease, hypertension, glaucoma and MAOI co-use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

