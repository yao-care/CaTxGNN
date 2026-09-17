---
layout: default
title: Zolmitriptan
parent: Moderate Evidence (L3-L4)
nav_order: 843
evidence_level: L4
indication_count: 3
---

# Zolmitriptan
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

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a triptan-class drug (5-HT1B/1D receptor agonist) originally established for the acute treatment of migraine. The TxGNN model predicts potential efficacy for **Migraine with Brainstem Aura**, but this specific subtype is conventionally treated as a relative contraindication for triptans in clinical practice. Currently, **0 clinical trials** and **19 publications** are linked to this candidate, and none directly confirm safety or efficacy in this subtype — several instead flag a theoretical safety concern.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine (acute treatment)¹ |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

¹ *No Canada regulatory license records are available for this product (0 DINs, not marketed), so this field is based on zolmitriptan's established pharmacological classification as evidenced in the literature below, not on a Canada-approved indication text.*

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for zolmitriptan is not available in the structured dataset (flagged as a High-severity data gap, DG002). However, the linked literature consistently characterizes zolmitriptan as a **selective serotonin 5-HT1B/1D receptor agonist ("triptan")**, acting through cranial vasoconstriction combined with central and peripheral inhibition of trigeminovascular CGRP release — the mechanism underlying its established efficacy in acute migraine treatment.

The predicted indication, migraine with brainstem aura (historically termed "basilar-type migraine"), is mechanistically a subtype of migraine, which is why TxGNN's knowledge graph links it strongly to zolmitriptan. However, this relationship needs an important caveat: because the proposed mechanism of vasoconstriction operates on the vertebrobasilar circulation in this subtype, most triptan product labels and AHS/IHS clinical guidelines list migraine with brainstem aura as a **relative contraindication**, due to a theoretical risk of inducing brainstem ischemia. One directly relevant reference in the evidence set (PMID 11903526, *Triptans in the treatment of basilar migraine and migraine with prolonged aura*) addresses exactly this concern.

In short, the high TxGNN score reflects a genuine mechanistic and taxonomic link between the drug's general migraine mechanism and this migraine subtype, but it does **not** account for the specific safety caution that clinical practice attaches to this subtype — this is a case where mechanistic plausibility and clinical appropriateness diverge.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------------|
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT (subgroup analysis) | Neurol Sci | Subgroup analysis of a double-blind RCT comparing frovatriptan vs. zolmitriptan (2.5 mg each) specifically in patients with migraine **with aura** (n=18/107). |
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical Report | Headache | Reports on triptan use, including zolmitriptan, specifically in basilar-type migraine and migraine with prolonged aura — directly addresses the predicted indication and its safety concerns. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | AHS evidence assessment grading acute migraine pharmacotherapies, including triptans such as zolmitriptan, for overall (non-aura-specific) efficacy. |
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | RCT | Headache | TEENZ Study: randomized, double-blind, multicenter trial of zolmitriptan nasal spray for acute migraine in adolescents (12–17y); primary endpoint pain-free at 2h. |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | RCT | Cephalalgia | Compared early triptan treatment (including zolmitriptan) on pain reduction and cutaneous allodynia in migraine patients with and without aura. |
| [12828501](https://pubmed.ncbi.nlm.nih.gov/12828501/) | 2003 | RCT | CNS Drugs | Randomised, double-blind, placebo-controlled, dose-ranging study comparing zolmitriptan nasal spray vs. oral tablet for speed of onset in acute migraine. |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis/Review | J Headache Pain | Compared frovatriptan vs. rizatriptan, zolmitriptan, and almotriptan specifically in migraine **with aura**; notes triptans are generally not effective when taken during the aura phase itself. |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | Review of zolmitriptan's clinical pharmacology as a selective 5-HT1B/1D agonist and its efficacy (2h response, pain-free rates) in migraine. |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical | Cephalalgia | Preclinical pharmacology establishing zolmitriptan as a centrally/peripherally acting 5-HT1B/1D agonist that inhibits trigeminovascular activation — foundational MOA data. |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Front Neurol | Review of vestibular migraine treatment options — a brainstem/vestibular-pathway-related subtype, relevant context but notes a scarcity of subtype-specific RCTs. |

---

## Canada Market Information

Currently no marketed authorizations in Canada. `taiwan_regulatory` data indicates a market status of **not marketed** with **0 DINs**, so no product-level details (dosage form, approved indication) are available for this drug.

---

## Safety Considerations

**Key Mechanistic Safety Signal:** Migraine with brainstem aura (basilar-type migraine) is conventionally treated as a **relative contraindication** for triptans, including zolmitriptan, in standard product labeling and AHS/IHS clinical guidelines, due to a theoretical risk of vertebrobasilar vasoconstriction and cerebral ischemia. This caution is not reflected in the TxGNN prediction score and should be weighed heavily against the prediction.

Formal structured safety data (key warnings, contraindications, drug interactions) are not currently available in this evidence pack. Please refer to the official product monograph or package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.99%), but it reflects zolmitriptan's general association with migraine pathology rather than specific support for the migraine-with-brainstem-aura subtype. No clinical trials directly evaluate this indication, and at least one reference (PMID 11903526) plus standard clinical guidance suggest this subtype is typically a relative contraindication for the drug class. Combined with a Blocking data gap on regulatory safety labeling (DG001), this candidate cannot yet proceed to the S1 safety evaluation stage.

**To proceed, the following is needed:**
- Official TFDA/Canada product monograph — key warnings and contraindications (Blocking data gap, DG001)
- Confirmed detailed mechanism-of-action data from DrugBank (High-severity data gap, DG002)
- Direct clinical evidence (trial or case series) specifically evaluating triptan safety/efficacy in migraine with brainstem aura, given the class-wide contraindication concern
- Verification of Canada market/regulatory status, as no licenses are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

