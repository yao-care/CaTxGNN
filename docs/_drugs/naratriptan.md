---
layout: default
title: Naratriptan
parent: Model Prediction Only (L5)
nav_order: 638
evidence_level: L5
indication_count: 3
---

# Naratriptan
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

# Naratriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Naratriptan is a triptan (5-HT1B/1D agonist) marketed for acute migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but **no clinical trials** are registered for this condition, and the **19 publications** found cover migraine in general, not this subtype.
Because triptans carry a recognised vasoconstriction concern in this subtype, safety must be settled before any efficacy question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine (not stated in the supplied licence records; based on the drug's known class and use) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (indirect evidence only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Naratriptan is a 5-HT1B/1D agonist, a triptan already used in migraine. The predicted indication is a migraine subtype, so it sits next to the drug's existing use rather than being a distant repurposing.

The empty original-indication and MOA fields may partly explain the very high score (0.9998). The model may be matching on "migraine" in general rather than on the brainstem aura subtype.

The supplied literature covers menstrual migraine, treatment during the prodrome, headache recurrence, and reduced sumatriptan efficacy in migraine with aura. None of it addresses brainstem aura specifically.

Triptan vasoconstriction is a recognised safety concern in brainstem aura and hemiplegic migraine, and triptan labels commonly list these as contraindications or cautions. The evidence is therefore indirect, and the safety question comes first.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Showing 10 of 19 records. None is specific to brainstem aura.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomised, double-blind crossover comparing headache recurrence after naratriptan vs sumatriptan in recurrence-prone migraine patients |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT (per title) | Headache | Naratriptan 1 mg and 2.5 mg twice daily vs placebo as short-term prophylaxis of menstrually associated migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of drugs for acute migraine treatment in adults |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | Clinical study | Cephalalgia | Whether naratriptan given during the prodrome can prevent migraine headache |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Open pilot study | Neurol Sci | Efficacy and tolerability of naratriptan as short-term prophylaxis of pure menstrual migraine, in a six-month multicentre open study |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Open-label study | Headache | Long-term tolerability of intermittent naratriptan for short-term prevention of menstrually related migraine |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Acute treatment outcome, with sumatriptan, in migraine with aura vs without aura |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of treatment options for menstrual migraine |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Case series | Headache | Use of naratriptan for intractable migraine |
| [23877022](https://pubmed.ncbi.nlm.nih.gov/23877022/) | 2014 | Case report | Brain & Development | Naratriptan improved intractable migraine-like headaches in a patient with Sturge-Weber syndrome; lamotrigine prevented his visual aura and headaches |

---

## Canada Market Information

Dosage form, manufacturer and approved-indication text are not populated in the supplied licence records.

| DIN | Product Name |
|---------|------|
| 02314290 | TEVA-NARATRIPTAN |
| 02314304 | TEVA-NARATRIPTAN |
| 02322323 | SANDOZ NARATRIPTAN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. No trials exist for migraine with brainstem aura, and the literature addresses other migraine types. The class-level vasoconstriction concern in this subtype, together with missing product monograph safety data, makes it inappropriate to advance now.

The other two predictions (atrophoderma vermiculata, ulerythema ophryogenesis) are model-only, with no trials or literature and no plausible mechanistic link to 5-HT1B/1D agonism. They are also on Hold.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications for the three DINs, in particular any contraindication for brainstem aura or hemiplegic migraine
- Mechanism of action and original indication data (e.g. from DrugBank)
- Clinical evidence specific to brainstem aura, or a documented rationale for why existing migraine data apply
- A safety review of vasoconstriction risk in this subtype before any efficacy assessment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

