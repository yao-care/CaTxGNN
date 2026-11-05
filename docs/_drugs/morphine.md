---
layout: default
title: Morphine
parent: Model Prediction Only (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-05
monitor_inn: "Morphine"
predicted_indications: ["myofascial pain syndrome", "manic bipolar affective disorder", "Tourette syndrome", "restless legs syndrome", "attention deficit hyperactivity disorder, inattentive type", "migraine disorder", "trichotillomania", "methemoglobinemia", "migraine with brainstem aura", "specific developmental disorder"]
description: "Morphine: predicted new indication Myofascial pain syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Morphine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

Morphine is a mu-opioid receptor agonist analgesic that is marketed in Canada.
The TxGNN model predicts it may be useful for **myofascial pain syndrome**, but **no clinical trials** are registered and none of the **10 publications** retrieved tests morphine in this condition. The evidence level is therefore L5.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Morphine acts as an agonist at the mu-opioid receptor and provides general analgesia. Detailed mechanism-of-action data were not available in the data compiled for this report, so this link rests on the drug's known class pharmacology.

Myofascial pain is a musculoskeletal pain condition, so a general analgesic link is plausible. However, the retrieved literature is mostly indirect. It covers opioid use in temporomandibular joint dysfunction, post-surgical analgesia and adjunct infiltration comparisons. Opioids are generally not a recommended first-line approach for myofascial pain. No myofascial-specific morphine study was identified, so the high model score has not been confirmed by direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications directly tests morphine as a treatment for myofascial pain syndrome.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine J | Double-blind trial comparing dexmedetomidine plus morphine with plain ropivacaine for myofascial infiltration in spinal fusion surgery. This is a postoperative pain setting, not myofascial pain syndrome. |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | RCT | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block for perioperative pain after OnabotulinumtoxinA injection for myofascial pelvic pain. Morphine was not the studied treatment. |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Pract | Retrospective study of a structured stretching program for myofascial pain and opioid use in "legacy pain" patients. |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Cohort | Rev Assoc Med Bras | Descriptive study of therapeutic approaches in 56 patients with failed back surgery pain syndrome. |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted by current evidence. |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Review | J Calif Dent Assoc | Use of oral medications, infusions and injections in the differential diagnosis of orofacial pain. |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Not classified | J Oral Maxillofac Surg | Arthrocentesis followed by intra-articular morphine infusion for refractory temporomandibular joint pain. |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | Randomized comparison | Eur J Pain | Epidural bupivacaine and morphine compared with intercostal nerve cryoanalgesia for post-thoracotomy pain in 107 patients. |
| [15176410](https://pubmed.ncbi.nlm.nih.gov/15176410/) | 2004 | Case report | Nervenarzt | Botulinum toxin A injected into trigger points for long-term phantom and stump pain. |
| [7478690](https://pubmed.ncbi.nlm.nih.gov/7478690/) | 1995 | Preclinical | Pain | Rat model of visceral pain and referred lumbar muscle hyperalgesia. |

---

## Canada Market Information

Morphine is marketed in Canada with 20 valid single-ingredient licences and no cancelled licences. The licence records may be partial. The main authorizations are listed below. Approved indication text and dosage forms are not recorded in the local data.

| DIN | Product Name |
|---------|------|
| 02474980 | Morphine Sulfate Injection BP |
| 02244792 | Sandoz Morphine SR |
| 02014238 | MS.IR |
| 02184451 | Kadian |
| 00392561 | Morphine Sulfate Inj 15mg/mL USP |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level interactions include fentanyl, codeine, dihydrocodeine, tramadol, butalbital, dichloralphenazone, alprazolam and ethanol. Combining morphine with other central nervous system depressants or opioids needs particular caution. Moderate-level interactions include chlorpheniramine, cetirizine, nifedipine, hydrochlorothiazide and metformin.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. No study tests morphine in myofascial pain syndrome, and the one randomized trial retrieved concerns postoperative pain after spinal fusion. Opioids are not a standard approach for this condition, and the indirect literature does not support moving forward on the model score alone.

**To proceed, the following is needed:**
- Controlled studies of morphine or other opioids specifically in myofascial pain syndrome
- Comparison with established non-opioid treatments for myofascial pain
- Detailed mechanism-of-action data
- A risk assessment covering dependence, respiratory depression and opioid-induced hyperalgesia in a chronic musculoskeletal pain population
- The package insert warnings and contraindications from Health Canada

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

