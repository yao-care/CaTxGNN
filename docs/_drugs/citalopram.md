---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Citalopram: From Its Marketed SSRI Use to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) marketed in Canada under 20 licences.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**.
The evidence is **27 registered trials and 15 publications**, but almost all direct OCD trials tested its S-enantiomer escitalopram, not citalopram itself.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* The input pack labelled this candidate L2. I graded it L3 because no completed Phase 2/3 RCT tests citalopram in OCD. The direct OCD trials use escitalopram or are open-label. The support comes mainly from meta-analyses and reviews, plus small citalopram open-label studies.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for citalopram is not available in the input data. Based on known information, citalopram is an SSRI, and OCD is well known to respond to serotonin reuptake inhibition.

SSRI class efficacy in OCD is well established. Escitalopram, the S-enantiomer of citalopram, has controlled OCD trial data. Citalopram-specific OCD evidence is limited to older open-label reports and class-level reviews. These include a 1999 randomized open-label study in treatment-resistant OCD and a small pediatric open-label study.

The prediction is therefore plausible mechanistically and by class, but it is not directly proven for citalopram. It would need citalopram-specific controlled data, or a decision to rely on the class evidence.

## Clinical Trial Evidence

Most direct OCD trials used escitalopram. Their relevance to citalopram is indirect (same racemic-to-enantiomer family and same mechanism).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label study of high-dose escitalopram (up to 50 mg/day) in adult OCD. It is the strongest direct OCD trial in the set but is not randomized. |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomized, double-blind, multi-center comparison of conventional-dose (20 mg) versus high-dose (40 mg) escitalopram in OCD. |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Escitalopram efficacy and optimal dose in OCD. Small sample. |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study of escitalopram safety and effectiveness in OCD symptoms. Very small. |
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | Unknown | 40 | Escitalopram in adolescents with OCD, with executive function and brain activation measures. Completion unverified. |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | Placebo-controlled trial of citalopram in children with autism and high levels of repetitive behavior. It tests citalopram, but the population is autism, not OCD. |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomized open trial of group CBT versus fluoxetine in OCD. Citalopram is not tested, so it only supports the SSRI class. |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Whether adding CBT improves serotonin reuptake inhibitor treatment in children with OCD who partially responded. |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Compares SSRIs, exposure and response prevention (ERP), and their combination in OCD, with predictors of response. |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Completed | 12 | fMRI proof-of-concept study of citalopram on restricted repetitive behaviors in autism. Indirect, mechanistic support only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Meta-analysis | J Psychiatr Res | Network meta-analysis comparing pharmacological and psychological treatments, alone and combined, in pediatric OCD. |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Front Psychiatry | Meta-review of antidepressant efficacy, tolerability and suicidality in children and adolescents, including OCD. |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | OCD shows a reduced placebo and antidepressant response compared with other anxiety disorders. |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Review | Compr Psychiatry | Long-term safety and tolerability of off-label high-dose serotonin reuptake inhibitors in OCD. |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Open-label study | Eur Psychiatry | Randomized open-label trial (n=16) of citalopram alone versus citalopram plus clomipramine in treatment-resistant OCD. |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label study | Psychiatry Clin Neurosci | Eight-week open-label study (n=15) of citalopram (20–30 mg/day) in children and adolescents with OCD. |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review | Int Clin Psychopharmacol | Review of citalopram for OCD in the context of the serotonin-OCD link. |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | Review of the serotonin hypothesis and beyond in OCD, covering both psychological and serotonergic treatment. |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | Pharmacogenetic study | CNS Spectr | Impact of the BDNF Val66Met polymorphism on response to escitalopram or paroxetine in OCD. |
| [30973183](https://pubmed.ncbi.nlm.nih.gov/30973183/) | 2019 | Imaging study | Psychiatry Clin Neurosci | ¹H-MRS study of brain neurochemistry in unmedicated OCD patients and changes after 12 weeks of escitalopram. |

## Canada Market Information

Dosage form, manufacturer and approved indication text are not available in the input data. The licence numbers below are shown as given in the data. Five of 20 licences are listed.

| DIN | Product Name |
|---------|------|
| 2312336 | TEVA-CITALOPRAM |
| 2313405 | JAMP-CITALOPRAM |
| 2248010 | PMS-CITALOPRAM |
| 2371871 | MAR-CITALOPRAM |
| 2429713 | MINT-CITALOPRAM |

## Safety Considerations

- **QT prolongation:** Citalopram causes dose-dependent QT prolongation. This limits the high-dose strategies often used in OCD. Citalopram is generally capped at 40 mg/day, or 20 mg/day in older adults and CYP2C19 poor metabolizers.
- **Co-medications:** Screen for QT-prolonging co-medications.
- **Suicidality:** Screen for suicidality in young patients.

Please refer to the package insert for full warnings, contraindications and drug interaction information. These were not available in the input data.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The serotonergic mechanism and SSRI class evidence in OCD are strong, and citalopram is widely marketed in Canada. However, direct controlled evidence for citalopram in OCD is thin. Most OCD trials used escitalopram, and the main citalopram-specific data are small open-label studies. Dose-dependent QT prolongation also limits the high-dose regimens often used in OCD.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Citalopram-specific controlled OCD data, or an explicit decision to rely on SSRI class and escitalopram evidence
- A safety plan covering the 40 mg/day cap, lower caps for older adults and CYP2C19 poor metabolizers, QT-drug screening and suicidality monitoring in young patients

The other four predicted indications (schizoid, histrionic, schizotypal and paranoid personality disorders) have little or no supporting evidence and no credible mechanistic link. They are rated **Hold**.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

