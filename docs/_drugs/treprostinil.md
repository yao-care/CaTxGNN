---
layout: default
title: Treprostinil
parent: High Evidence (L1-L2)
nav_order: 798
evidence_level: L2
indication_count: 10
---

# Treprostinil
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Treprostinil: From Pulmonary Arterial Hypertension to Connective Tissue Disease-Associated PAH

## One-Sentence Summary

Treprostinil is a prostacyclin analog originally developed for pulmonary arterial hypertension (WHO Group 1).
The TxGNN model predicts continued and reinforced efficacy in **Connective Tissue Disease-Associated Pulmonary Arterial Hypertension (CTD-PAH)** — a well-recognized clinical subgroup of the original indication —
with **1 clinical trial** and **19 publications**, including a systematic review/meta-analysis and RCT subgroup data, currently supporting this direction.

*(Note: TxGNN also flagged several additional Group 1 PAH subtypes — congenital heart disease-associated PAH, HIV-associated PAH — with weaker but non-trivial evidence, and a set of unrelated diseases such as hypotrichosis and periodontal malformation syndromes that appear to be knowledge-graph noise with no supporting mechanism or literature. CTD-PAH was selected as the headline candidate here because it has the strongest evidence level (L2) among all ranked predictions.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (WHO Group 1) |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Connective Tissue Disease (CTD-PAH) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal Health Canada/DrugBank mechanism-of-action record is not available for this candidate (flagged as a High-severity data gap). However, based on the mechanistic rationale documented alongside this prediction, treprostinil is a stable prostacyclin (PGI2) analog that activates the IP receptor, producing pulmonary vasodilation, inhibition of vascular smooth muscle remodeling, and suppression of platelet aggregation. This mechanism does not depend on the underlying etiology of pulmonary hypertension — it acts downstream on the shared pulmonary vascular pathology.

CTD-PAH is not a distinct disease from the original indication in a mechanistic sense; it is a clinically defined etiological subgroup within WHO Group 1 PAH (most commonly arising in systemic sclerosis, followed by SLE and mixed connective tissue disease). Because treprostinil's original approval covers idiopathic/heritable Group 1 PAH, and CTD-PAH shares the identical obstructive pulmonary vascular pathobiology, the TxGNN prediction essentially reflects an established clinical practice pattern rather than a novel mechanistic leap.

This is further reinforced by direct clinical evidence: a landmark RCT (Simonneau et al., 2002, PMID 11897647) established subcutaneous treprostinil's efficacy across the general PAH population, and a dedicated RCT subgroup analysis (Oudiz et al., 2004, PMID 15302727) specifically evaluated treprostinil in CTD-PAH patients. A 2024 systematic review and meta-analysis of CTD-PAH treatment (PMID 38378970) further consolidates this evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02663895](https://clinicaltrials.gov/study/NCT02663895) | Phase 2 | Completed | 12 | Pilot open-label trial of oral treprostinil in systemic sclerosis-associated calcinosis (indirect evidence; primary endpoint was calcinosis reduction, not PAH hemodynamics) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | RCT | Am J Respir Crit Care Med | Pivotal double-blind, placebo-controlled RCT establishing efficacy of continuous SC treprostinil in PAH |
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | RCT subgroup analysis | Chest | Efficacy and safety of SC treprostinil specifically in CTD-associated PAH patients |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review/Meta-analysis | Intern Emerg Med | Meta-analysis of RCTs reporting outcomes for CTD-PAH treatment |
| [34462153](https://pubmed.ncbi.nlm.nih.gov/34462153/) | 2021 | Cohort/Case series | Rev Med Interne | Multicenter retrospective study characterizing CTD-PAH patients treated with prostanoids |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treatment of CTD-associated PAH |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review | Biomolecules | Current therapeutic strategies and future prospects for CTD-PAH |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH associated with connective tissue diseases |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Treatment of PAH in connective tissue disease |
| [18473715](https://pubmed.ncbi.nlm.nih.gov/18473715/) | 2008 | Review | Expert Opin Pharmacother | Treprostinil for the treatment of pulmonary hypertension |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Diagnosis and treatment of pulmonary arterial hypertension |

---

## Canada Market Information

Treprostinil currently has no active Canadian drug identification numbers (DINs) or market authorizations on record — market status is **Not Marketed**, with 0 licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Treprostinil's mechanism directly applies to CTD-PAH as an established WHO Group 1 PAH subgroup, and the evidence base (L2) includes a dedicated RCT subgroup analysis and a recent systematic review/meta-analysis — considerably stronger than the other ranked candidates in this evidence pack, most of which have no clinical trial or literature support. However, the drug is not currently marketed in Canada, and formal regulatory safety documentation is missing.

**To proceed, the following is needed:**
- Health Canada/TFDA-equivalent product monograph — key warnings and contraindications (Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-severity data gap, DG002)
- Canadian market authorization pathway, since the drug currently has 0 DINs on file
- Route-of-administration compatibility assessment (SC/IV/inhaled/oral), currently marked "pending" in the evidence pack
- Drug-drug interaction data (current DDI query returned no results — status should be reconfirmed rather than treated as negative evidence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

