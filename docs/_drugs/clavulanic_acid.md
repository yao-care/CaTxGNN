---
layout: default
title: Clavulanic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 202
evidence_level: L4
indication_count: 10
---

# Clavulanic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Clavulanic Acid: From Beta-Lactamase Inhibition to Ureaplasma Urethritis

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor, marketed in Canada mainly as a partner drug in amoxicillin/clavulanate products. The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but **0 clinical trials** and only **4 general urethritis publications** (none specific to Ureaplasma or clavulanate) support this. The mechanism is also biologically implausible, so this specific prediction should be treated as a likely graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

The Canadian licence records contain no approved-indication text, so the original indication cannot be quoted from the data.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Clavulanic acid is generally known to inhibit bacterial beta-lactamases and protect a partner beta-lactam such as amoxicillin. This background knowledge does not come from the Evidence Pack.

For Ureaplasma urethritis, this mechanism does not fit. Ureaplasma has no cell wall, so beta-lactam antibiotics are intrinsically ineffective and beta-lactamase inhibition adds no benefit. The retrieved literature covers urethritis in general (Pasteurella bettyae, anaerobes in prostatitis, empirical treatment reviews) and contains no Ureaplasma-specific clavulanate data. The high graph score most likely reflects proximity to other urethritis nodes rather than a real drug-pathogen link.

A more credible candidate appears at rank 2: **gonococcal urethritis** (score 99.93%, evidence level L3). Clavulanate restores amoxicillin activity against penicillinase-producing *Neisseria gonorrhoeae*, and 14 publications, mostly 1980s single-dose amoxicillin/clavulanate studies in men, address this use. Current gonococcal resistance patterns and guidelines favour other agents, so contemporary relevance is limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Retrospective review | Rev Esp Quimioter | 3-year review of the prevalence and trends of organisms causing male urethritis in Madrid. No clavulanate data. |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Rev Esp Quimioter | Discusses the best empirical treatment of urethritis in Madrid. No Ureaplasma-specific clavulanate evidence. |
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Case report | Infect Dis Now | First association of *Pasteurella bettyae* with urethritis and balanitis in men who have sex with men. Not related to Ureaplasma. |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Review | Int J Androl | Role of anaerobic bacteria in chronic prostatitis. Not related to Ureaplasma or clavulanate. |

None of these studies tests clavulanic acid for Ureaplasma urethritis.

---

## Canada Market Information

Five of the 20 authorizations are listed below. Dosage form and approved-indication text are not recorded for these licences.

| DIN | Product Name |
|---------|------|
| 02238831 | CLAVULIN 200 |
| 02510634 | AG-AMOXI CLAV |
| 02495937 | AMOXICILLIN SODIUM AND POTASSIUM CLAVULANATE FOR INJECTION |
| 02243351 | APO-AMOXI CLAV |
| 02510642 | AG-AMOXI CLAV |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ureaplasma lacks a cell wall, so the mechanism is implausible, and no trials or Ureaplasma-specific publications support the prediction. The high TxGNN score is most likely a knowledge-graph artifact from the urethritis neighbourhood.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- If the goal is a urethritis indication, redirect the assessment to **gonococcal urethritis** (rank 2), which has the strongest human evidence, but only historical studies. That work would need verified study designs and a comparison against current gonococcal resistance data and treatment guidelines.

**Other lower-ranked predictions:**
- **Uterine inflammatory disease** (L4) has one postpartum endometritis guideline; the other publications are veterinary, murine or case-level.
- **Xanthogranulomatous pyelonephritis** and **urogenital tuberculosis** (L4) rest on case reports or teaching items only.
- **Abdominal cystic lymphangioma**, **celiac trunk compression syndrome**, **abdominal ectopic pregnancy**, **lymph node palisaded myofibroblastoma** and **disease of uterine broad ligament** (L5) have no plausible mechanism and no supporting evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

