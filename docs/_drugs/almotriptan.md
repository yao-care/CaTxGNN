---
layout: default
title: Almotriptan
parent: Moderate Evidence (L3-L4)
nav_order: 38
evidence_level: L4
indication_count: 3
---

# Almotriptan
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

# Almotriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Almotriptan is a triptan used for the acute treatment of migraine with or without aura.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but there are **0 clinical trials** and **19 publications**, all about migraine in general, and none study this subtype specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine with or without aura (from the published literature; the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record. The published reviews describe almotriptan as a selective serotonin 5-HT1B/1D receptor agonist. The proposed mechanism is cranial vasoconstriction and inhibition of trigeminal CGRP release, which is plausible for migraine in general.

Migraine with brainstem aura is a subtype of migraine, so a model that keys on proximity to the existing migraine indication would score it highly. The 99.98% score probably reflects that proximity rather than independent evidence for this subtype. No supplied trial or paper studies brainstem aura. The only aura-focused item is a meta-analysis of frovatriptan, a different triptan, in migraine with aura.

There is also a safety concern. Triptan labeling generally contraindicates use in hemiplegic and basilar-type migraine because of a theoretical risk from vasoconstriction (stroke). Brainstem aura is closely related to these subtypes, so the mechanism that supports the prediction may also be a reason for caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications addresses brainstem aura. They cover almotriptan in migraine generally, plus one aura-related triptan meta-analysis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [11768838](https://pubmed.ncbi.nlm.nih.gov/11768838/) | 2001 | RCT | Clinical Therapeutics | Dose-finding study of subcutaneous almotriptan in acute migraine, building on earlier oral trials that found it well tolerated and efficacious |
| [18302700](https://pubmed.ncbi.nlm.nih.gov/18302700/) | 2008 | RCT | Headache | AEGIS trial: early intervention with almotriptan vs placebo, assessed on functional disability and quality of life |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Evidence Assessment | Headache | American Headache Society update on the evidence for acute migraine drug therapies |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis/Review | J Headache Pain | Frovatriptan vs rizatriptan, zolmitriptan and almotriptan in migraine with aura. Notes triptans are probably ineffective during the aura phase and that randomised data for the headache phase are limited |
| [30845850](https://pubmed.ncbi.nlm.nih.gov/30845850/) | 2019 | Review | Expert Rev Neurother | 20 years of almotriptan experience: more than 15,000 patients in studies and an estimated >150 million treated attacks |
| [20945537](https://pubmed.ncbi.nlm.nih.gov/20945537/) | 2010 | Review | Expert Rev Neurother | 10-year review covering large RCTs and post-marketing studies in acute migraine with or without aura |
| [12455302](https://pubmed.ncbi.nlm.nih.gov/12455302/) | 2002 | Review | Am J Health-Syst Pharm | Pharmacology, pharmacokinetics, efficacy and adverse effects of almotriptan |
| [11380642](https://pubmed.ncbi.nlm.nih.gov/11380642/) | 2001 | Pooled safety analysis | Headache | Safety and tolerability of oral almotriptan from premarketing clinical trials |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of treatment options for menstrual migraine |
| [16688412](https://pubmed.ncbi.nlm.nih.gov/16688412/) | 2006 | Open-label pilot | J Headache Pain | 15 patients aged 11-17 treated with almotriptan 6.25-12.5 mg, well tolerated |

## Canada Market Information

Six licenses are on record and five are listed below. The supplied records contain no dosage form or approved-indication text.

| DIN | Product Name |
|---------|------|
| 2398443 | MYLAN-ALMOTRIPTAN |
| 2405334 | SANDOZ ALMOTRIPTAN |
| 2424029 | ALMOTRIPTAN |
| 2398435 | MYLAN-ALMOTRIPTAN |
| 2466821 | ALMOTRIPTAN |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone. There are no trials and no publications on brainstem aura, and triptan labeling generally contraindicates use in closely related subtypes (hemiplegic and basilar-type migraine). The other two predictions (atrophoderma vermiculata, ulerythema ophryogenes) have no evidence and no plausible mechanism, so they are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Mechanism-of-action data for almotriptan from DrugBank
- A clinical review of whether the triptan contraindication for hemiplegic and basilar-type migraine applies to brainstem aura
- A targeted literature search for almotriptan or other triptans in migraine with brainstem aura
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

