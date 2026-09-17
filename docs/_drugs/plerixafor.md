---
layout: default
title: Plerixafor
parent: High Evidence (L1-L2)
nav_order: 628
evidence_level: L2
indication_count: 7
---

# Plerixafor
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **7** 
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

# Plerixafor: From Hematopoietic Stem Cell Mobilization to Myeloid Leukemia (AML)

## One-Sentence Summary

Plerixafor is a CXCR4 antagonist originally used to mobilize hematopoietic stem cells into peripheral blood for autologous transplantation in patients with lymphoma and multiple myeloma. Among seven indications predicted by the TxGNN model, myeloid leukemia (AML) is the only one with substantive supporting evidence — **30 clinical trials** and **20 publications** — including multiple completed Phase 1/2 studies testing plerixafor as a leukemia chemosensitizing agent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hematopoietic stem cell mobilization for autologous transplantation (context confirmed via trial records in the evidence pack, e.g. NCT01319864: "Plerixafor is FDA approved for mobilizing stem cells from the bone marrow"); no formal indication text is available because the drug is not licensed in Canada |
| Predicted New Indication | Myeloid Leukemia (AML) |
| TxGNN Prediction Score | 99.02% (rank 16,154) |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Plerixafor is a small-molecule CXCR4 antagonist that blocks the CXCR4/CXCL12 (SDF-1) axis. This axis is the primary mechanism by which normal hematopoietic stem cells — and, importantly, leukemic stem/blast cells — adhere to the bone marrow niche. That is precisely why plerixafor was originally developed: to force stem cells out of the marrow niche into peripheral blood for collection prior to transplant.

The proposed repurposing rationale in AML exploits the same mechanism from a different angle. AML blasts use CXCR4/CXCL12 signaling to anchor themselves in protective bone-marrow niches, where they are shielded from cytotoxic chemotherapy. Disrupting this adhesion with plerixafor is hypothesized to mobilize leukemic blasts out of their protective niche and into the circulation, increasing their sensitivity to concurrently administered chemotherapy ("chemosensitization"). This is mechanistically a natural extension of plerixafor's known pharmacology rather than a novel, unrelated mode of action — which is reflected in the fact that this line of investigation has already progressed into more than a dozen Phase 1/2 human trials (as chemosensitizing combinations with fludarabine/idarubicin/cytarabine, decitabine, sorafenib, and standard "7+3" regimens), rather than remaining purely computational.

Currently, a formally documented original mechanism-of-action record and original indication text are not available in this evidence pack (flagged as a data gap), so the description above is reconstructed from mechanistic statements embedded in the trial and literature evidence itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | Completed | 55 | Fludarabine + idarubicin + cytarabine + G-CSF + plerixafor (PLERIFLAG regimen) as second-line induction in relapsed/refractory AML patients ≤65 years |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Completed | 39 | Plerixafor + G-CSF chemosensitization in relapsed/refractory AML |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Completed | 71 | Decitabine + escalating-dose plerixafor priming/induction in AML patients ≥60 years |
| [NCT01160354](https://clinicaltrials.gov/study/NCT01160354) | Phase 1/2 | Terminated | 22 | Plerixafor + clofarabine in previously untreated older (≥60y) AML with unfavorable prognostic factors; closed before Part 2 |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Completed | 47 | G-CSF + plerixafor (AMD3100) with busulfan/fludarabine conditioning for allogeneic transplant in AML/MDS/CML |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Completed | 36 | Plerixafor added to cytarabine + daunorubicin ("7+3") in newly diagnosed AML, with/without G-CSF |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | Completed | 33 | Sorafenib + G-CSF + plerixafor in FLT3-mutated AML; dose-finding for tolerability |
| [NCT01236144](https://clinicaltrials.gov/study/NCT01236144) | Phase 1/2 | Completed | 113 | AML18 pilot trial; feasibility of combining plerixafor (or AC220 or ganetespib) with standard DAE chemotherapy in older AML/high-risk MDS |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Completed | 20 | Plerixafor + cytarabine/etoposide as chemosensitizer in pediatric relapsed acute leukemia/MDS |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Completed | 52 | AMD3100 (plerixafor) + mitoxantrone/etoposide/cytarabine (MEC) in relapsed/refractory AML |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 trial | Blood | Landmark study: plerixafor disrupts CXCR4/CXCL12-mediated blast-microenvironment interaction, increasing AML blast chemosensitivity in 52 relapsed/refractory patients |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase 1-2 trial | Annals of Hematology | PLERIFLAG regimen (FLAG-Ida + high-dose IV plerixafor) in first early-relapsed/refractory AML |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 trial | Haematologica | Decitabine + plerixafor in newly diagnosed older AML; evaluated effects on leukemia stem cells (n=69) |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 trial | American Journal of Hematology | Sorafenib + G-CSF + plerixafor in relapsed/refractory FLT3-ITD-mutated AML (n=28) |
| [28282031](https://pubmed.ncbi.nlm.nih.gov/28282031/) | 2017 | Phase 1/2 trial | Blood Cancer Journal | Follow-up chemosensitization study of plerixafor plus G-CSF in relapsed/refractory AML |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematic review/meta-analysis | Leukemia Research | Systematic review of plerixafor + chemotherapy/HCT in acute leukemia across preclinical and clinical studies, informing design of definitive trials |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | Comprehensive review of CXCR4 as a therapeutic target in AML, covering proliferation, apoptosis, and chemoresistance mechanisms |
| [33080779](https://pubmed.ncbi.nlm.nih.gov/33080779/) | 2020 | Review | Cells | Review of hyperleukocytosis/leukostasis pathophysiology in AML, contextualizing niche-targeted approaches |
| [27822339](https://pubmed.ncbi.nlm.nih.gov/27822339/) | 2016 | Review | World Journal of Stem Cells | Update on AML leukemia stem cells, including niche-disruption strategies as therapeutic opportunities |
| [32079173](https://pubmed.ncbi.nlm.nih.gov/32079173/) | 2020 | Review | Biology | CXCR4 antagonists as stem cell mobilizers and therapy sensitizers in AML and glioblastoma |

---

## Canada Market Information

Plerixafor currently holds no Health Canada drug identification numbers (DINs) and is **not marketed** in Canada under this evidence pack's data (`total_licenses: 0`). No authorization or approved-indication text is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Over a dozen completed Phase 1/2 trials and a supporting systematic review establish biological plausibility and early feasibility for plerixafor as an AML chemosensitizer, but no confirmatory Phase 3 efficacy trial exists, and the drug is not currently marketed in Canada under any indication. This places the candidate at evidence level L2 — promising mechanistically and clinically explored, but not yet actionable for a Go or Guardrailed-proceed decision.

**To proceed, the following is needed:**
- A confirmatory randomized (Phase 2/3) trial demonstrating clinical benefit (response rate, survival) of plerixafor-based chemosensitization versus standard chemotherapy alone
- Formal mechanism-of-action and original-indication documentation (currently flagged as data gaps)
- Canadian regulatory pathway assessment, given plerixafor has no existing DIN/market presence
- TFDA/Health Canada label warnings and contraindications (currently unavailable) before any safety evaluation (S1) can begin

---

### Appendix: Other TxGNN-Predicted Indications (Low Confidence, Not Further Evaluated)

The evidence pack also returned six additional TxGNN predictions for plerixafor. All are pure model outputs (Evidence Level L5) with **zero matching clinical trials or literature** found on targeted searches, and are scored **Hold**:

| Disease | TxGNN Score | Evidence |
|---|---|---|
| Indolent plasma cell myeloma | 99.97% | None found |
| CMM7 (melanoma susceptibility locus) | 99.34% | None found |
| Pediatric leptomeningeal melanoma | 99.30% | None found |
| Epithelioid cell uveal melanoma | 99.27% | None found |
| Bronchitis | 99.22% | None found (likely model noise) |
| Vulvar melanoma | 99.17% | None found |

These are noted for completeness but require no action at this time given the complete absence of supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

