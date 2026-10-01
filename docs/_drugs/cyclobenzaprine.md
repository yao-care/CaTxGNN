---
layout: default
title: Cyclobenzaprine
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 3
---

# Cyclobenzaprine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cyclobenzaprine: From Muscle Spasm to Myofascial Pain Syndrome

## One-Sentence Summary

Cyclobenzaprine is a centrally acting skeletal muscle relaxant, used for muscle spasm associated with acute, painful musculoskeletal conditions.
The TxGNN model predicts it may be effective for **myofascial pain syndrome**, with **17 registered clinical trials** and **5 publications** on record.
Most of the trials are Phase 3 studies in fibromyalgia, a different condition. Direct evidence in myofascial pain syndrome is limited to small studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasm associated with acute, painful musculoskeletal conditions (from US labeling cited in NCT01041495; the Canadian indication text is not in the record) |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L2 (indirect: the completed Phase 2/3 RCT is in fibromyalgia, not myofascial pain syndrome) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. The following comes from general pharmacology, not from the supplied record.
Cyclobenzaprine is structurally related to tricyclic antidepressants. It is generally described as acting at the brainstem to reduce tonic somatic motor activity, through 5-HT2 antagonism and modulation of descending noradrenergic pathways. It also has H1 antihistamine and anticholinergic activity.

Myofascial pain syndrome involves painful muscle trigger points and muscle tension. That is close to the drug's original use in muscle spasm, so a muscle relaxant is a plausible fit. The sedative effect may also help the sleep disturbance that often accompanies chronic pain.

The link has limits. The large Phase 3 program in the record (TNX-102 SL, a sublingual low-dose cyclobenzaprine) targets fibromyalgia, not myofascial pain syndrome. Small RCTs exist in myofascial or strain-type pain, but no Phase 3 RCT is confirmed for myofascial pain syndrome itself.

The model also ranked two other indications for this drug. Neuralgia (99.08%) has only indirect evidence, mainly a compounded topical cream trial, so it stays at Hold. Papillary conjunctivitis (99.08%) rests on the model prediction alone, with no trials or literature.

---

## Clinical Trial Evidence

Ten of the 17 registered trials are shown, prioritised by relevance to myofascial pain.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00635037](https://clinicaltrials.gov/study/NCT00635037) | N/A | Completed | 30 | Acupuncture vs trigger point injection combined with dipyrone and cyclobenzaprine in myofascial pain. Population is on-target, but cyclobenzaprine is part of a combination, so its effect cannot be isolated |
| [NCT04704297](https://clinicaltrials.gov/study/NCT04704297) | Phase 4 | Recruiting | 180 | Trigger point injection RCT for low-back myofascial pain syndrome. Cyclobenzaprine's role is unclear (possibly background or comparator therapy) |
| [NCT01903265](https://clinicaltrials.gov/study/NCT01903265) | Phase 2/3 | Completed | 205 | Double-blind placebo-controlled study of TNX-102 SL (sublingual cyclobenzaprine) at bedtime in fibromyalgia |
| [NCT04172831](https://clinicaltrials.gov/study/NCT04172831) | Phase 3 | Completed | 503 | 14-week placebo-controlled study of TNX-102 SL 5.6 mg in fibromyalgia |
| [NCT05273749](https://clinicaltrials.gov/study/NCT05273749) | Phase 3 | Completed | 457 | 14-week placebo-controlled study of TNX-102 SL 5.6 mg in fibromyalgia |
| [NCT04508621](https://clinicaltrials.gov/study/NCT04508621) | Phase 3 | Completed | 514 | 14-week placebo-controlled study of TNX-102 SL 5.6 mg in fibromyalgia |
| [NCT02436096](https://clinicaltrials.gov/study/NCT02436096) | Phase 3 | Completed | 519 | 12-week placebo-controlled study of TNX-102 SL 2.8 mg in fibromyalgia |
| [NCT02829814](https://clinicaltrials.gov/study/NCT02829814) | Phase 3 | Terminated | 51 | Placebo-controlled study of TNX-102 SL 2.8 mg in fibromyalgia. Terminated early, so hard to interpret |
| [NCT01041495](https://clinicaltrials.gov/study/NCT01041495) | Phase 4 | Terminated | 37 | Cyclobenzaprine ER (Amrix) augmentation for fibromyalgia fatigue and muscle pain. Terminated early |
| [NCT01889173](https://clinicaltrials.gov/study/NCT01889173) | Phase 1 | Completed | 24 | Single-dose pharmacokinetics of TNX-102 SL formulations vs oral cyclobenzaprine in healthy adults. No efficacy data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11889661](https://pubmed.ncbi.nlm.nih.gov/11889661/) | 2002 | RCT | J Orofacial Pain | Compared clonazepam, cyclobenzaprine and placebo added to patient education and self-care for jaw pain upon awakening |
| [24822235](https://pubmed.ncbi.nlm.nih.gov/24822235/) | 2014 | RCT | J Oral Facial Pain Headache | Compared adding cyclobenzaprine, tizanidine or placebo to self-care in myofascial pain with jaw pain upon awakening |
| [12764337](https://pubmed.ncbi.nlm.nih.gov/12764337/) | 2003 | RCT | Ann Emerg Med | Cyclobenzaprine plus ibuprofen vs ibuprofen alone in emergency department patients with acute myofascial strain (analgesic and side effects) |
| [20673246](https://pubmed.ncbi.nlm.nih.gov/20673246/) | 2011 | Comparative study (non-drug) | Pain Pract | Acupuncture vs trigger point injection combined with cyclobenzaprine and dipyrone for myofascial trigger point pain |
| [3464212](https://pubmed.ncbi.nlm.nih.gov/3464212/) | 1986 | Review | Am J Med | Clinical review of fibrositis (tender-point musculoskeletal pain syndrome) |

---

## Canada Market Information

Dosage form and approved indication text are not provided for these licenses. Five of the 10 licenses are listed.

| DIN | Product Name |
|---------|------|
| 02212048 | PMS-CYCLOBENZAPRINE - TAB 10MG |
| 02357127 | JAMP-CYCLOBENZAPRINE |
| 02424584 | CYCLOBENZAPRINE |
| 02348853 | AURO-CYCLOBENZAPRINE |
| 02080052 | TEVA-CYCLOBENZAPRINE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the drug is already marketed in Canada as a muscle relaxant. However, the large Phase 3 trials are in fibromyalgia, and the direct myofascial pain evidence is limited to small or combination-therapy studies. The Health Canada safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Registry review to confirm the indication and cyclobenzaprine's role in NCT04704297 and the other trials with truncated titles
- Evidence specific to myofascial pain syndrome, such as a controlled trial of cyclobenzaprine alone
- Review of the safety profile for this use, given the sedative and anticholinergic effects

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

