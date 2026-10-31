---
layout: default
title: Morphine
parent: Moderate Evidence (L3-L4)
nav_order: 632
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Morphine"
predicted_indications: ["myofascial pain syndrome", "manic bipolar affective disorder", "Tourette syndrome", "restless legs syndrome", "attention deficit hyperactivity disorder, inattentive type", "migraine disorder", "trichotillomania", "methemoglobinemia", "migraine with brainstem aura", "specific developmental disorder"]
description: "Morphine: predicted new indication Myofascial pain syndrome (evidence level L4). Approved use: Not recorded in the local data"
---

# Morphine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Morphine: Myofascial pain syndrome
{: .text-alpha }

## One-Sentence Summary

Morphine is an opioid analgesic that is linked to diarrheal disease as its original indication.
The TxGNN model predicts it may be effective for **myofascial pain syndrome**, but **no clinical trials** and only **10 publications** (mostly indirect) support this direction.
Of the ten predicted indications evaluated, **restless legs syndrome** has by far the strongest supporting evidence, and it is discussed in the conclusion.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, morphine is a mu-opioid receptor agonist that provides broad analgesia. Its link to the original indication, diarrheal disease, is the well-known slowing of gut motility by opioids.

Myofascial pain is a musculoskeletal pain condition, so a general analgesic link is plausible. However, the retrieved literature is mostly indirect: opioid use in temporomandibular joint dysfunction, post-surgical analgesia, and infiltration comparisons. Opioids are generally not recommended as first-line treatment for myofascial pain, and no myofascial-specific morphine trial was identified. The prediction is therefore mechanistically plausible but clinically unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for myofascial pain syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine J | Double-blind trial of dexmedetomidine plus morphine vs plain ropivacaine for myofascial infiltration in spinal fusion (a postoperative setting) |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | RCT | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block for pain after onabotulinumtoxinA injection in myofascial pelvic pain; morphine is not the studied treatment |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Pract | Structured stretching program for myofascial pain and opioid usage in "legacy pain" patients |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in TMJ dysfunction can be neither supported nor refuted by current evidence |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Review | J Calif Dent Assoc | Oral medications, infusions and injections for differential diagnosis of orofacial pain |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Cohort | Rev Assoc Med Bras | Therapeutic approaches in 56 patients with failed back surgery pain syndrome |

---

## Canada Market Information

Twenty valid single-ingredient licences are listed. Dosage form and approved indication text are not available for these products.

| DIN | Product Name |
|---------|------|
| 02474980 | Morphine Sulfate Injection BP |
| 02244792 | Sandoz Morphine SR |
| 02014238 | MS.IR |
| 02184451 | Kadian |
| 00392561 | Morphine Sulfate Inj 15mg/mL USP |

The remaining 15 licences include MS Contin, M-Eslon, M-Ediat, Teva-Morphine SR, PMS-Morphine Sulfate, Morphine LP Epidural, Statex and other injection products.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension and hypertensive disorder; orthostatic hypotension and related autonomic disorders; long QT syndrome and torsades de pointes; liver failure and liver disease; kidney disease; chronic obstructive pulmonary disease; epilepsy; pancreatitis; gallbladder disease; gastric ulcer; hypothyroidism and myxedema; psychotic and other mental disorders; anxiety and dysthymic disorders; potassium deficiency.
- **Drug interactions:** 100 interactions were recorded. Major-level examples include fentanyl, codeine, dihydrocodeine, tramadol, butalbital, alprazolam, ethanol and dichloralphenazone, which mainly reflect additive central nervous system and respiratory depression. Moderate-level examples include chlorpheniramine, cetirizine, nifedipine, hydrochlorothiazide, metformin and alfentanil.
- **Class concerns noted in the literature:** dependence, respiratory depression, opioid-induced hyperalgesia and medication-overuse headache.

Please refer to the package insert for full warnings and contraindications, as label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a high model score with only indirect literature and no myofascial-specific morphine trial. Opioids are not a recommended first-line approach for this condition, and the safety burden is substantial.

**Other predicted indications:**
- **Restless legs syndrome (rank 4)** is the only candidate with meaningful clinical support (Evidence Level L3, "Research Question"). Support includes registry cohorts of up to 5 years (National RLS Opioid Registry), intrathecal low-dose morphine reports and reviews. One Phase 1 pharmacokinetic trial (NCT01476124, n=18) provides only safety and PK data. There are no Phase 3 RCTs, and concerns include dependence, respiratory depression and augmentation or RLS emergence on discontinuation. It deserves priority review ahead of the top-ranked prediction.
- **Migraine disorder, migraine with brainstem aura** (L4/L5): literature suggests opioids are ineffective or may worsen migraine, and guidelines discourage their use.
- **Manic bipolar disorder, Tourette syndrome, ADHD (inattentive type), trichotillomania, methemoglobinemia, specific developmental disorder** (L5): no clinical support. Several have no literature at all, or the literature is off-topic.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A focused evidence review for restless legs syndrome, including route compatibility (oral vs intrathecal) and long-term dependence risk
- Dosage form and approved indication details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

