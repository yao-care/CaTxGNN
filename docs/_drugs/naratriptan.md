---
layout: default
title: Naratriptan
parent: 僅模型預測 (L5)
nav_order: 541
evidence_level: L5
indication_count: 3
---

# Naratriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Naratriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Naratriptan is a triptan (5-HT1B/1D receptor agonist) originally used for the acute treatment of migraine.
> The TxGNN model predicts it may be effective for **migraine with brainstem aura**, a specific and higher-risk migraine subtype,
> with **0 registered clinical trials** and **19 publications** currently available — none of which specifically studied this subtype,
> and current clinical guidance treats triptans as relatively contraindicated here.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (triptan class) — not recorded in the current dataset; based on known drug classification (see note below) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

**Note on Original Indication:** `original_indications` and `original_moa` are marked as data gaps in this evidence pack (DG002). The statement above reflects naratriptan's known pharmacological classification as a triptan indicated for acute migraine attacks, not a value extracted from the evidence pack itself.

---

## Why is This Prediction Reasonable?

Naratriptan is a selective 5-HT1B/1D receptor agonist. Its established mechanism in acute migraine involves cranial vasoconstriction and inhibition of pro-inflammatory neuropeptide release from trigeminal nerve terminals, which interrupts the migraine attack pathway.

Migraine with brainstem aura (formerly "basilar-type migraine") is not a separate disease but a specific migraine subtype involving aura symptoms attributable to the brainstem or bilateral hemispheres. Because naratriptan already treats migraine generally, the TxGNN model's graph-based similarity likely picked up this proximity — the two conditions share overlapping symptomatology and are adjacent in the knowledge graph.

However, this mechanistic overlap is also where the caution lies: major headache guidelines (ICHD-3, American Headache Society) list triptans as **relatively contraindicated** in migraine with brainstem aura, out of concern that their vasoconstrictive action could theoretically worsen posterior-circulation symptoms. None of the 19 literature records retrieved for this pairing specifically studied naratriptan in confirmed brainstem-aura patients — they address migraine in general, menstrual migraine, or comparisons with other triptans. The high TxGNN score therefore reflects strong general migraine efficacy data being generalized to a subtype where mechanistic extrapolation carries a recognized safety caveat rather than a straightforward efficacy signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomized, double-blind, crossover comparison of naratriptan vs. sumatriptan on headache recurrence in recurrence-prone migraine patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Evaluated naratriptan given during the migraine prodrome for attack prevention |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT (placebo-controlled) | Headache | Naratriptan 1 mg / 2.5 mg twice daily vs. placebo as short-term prophylaxis for menstrually associated migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies, including triptans |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Found reduced triptan (sumatriptan) efficacy in migraine **with aura** vs. without aura — directly relevant to aura-subtype treatment response |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Open-label | Headache | Long-term tolerability of naratriptan for short-term prevention of menstrually related migraine |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Pilot study | Neurological Sciences | Open, non-comparative pilot study of naratriptan for short-term prophylaxis of pure menstrual migraine |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of treatment options for menstrual migraine |
| [16268666](https://pubmed.ncbi.nlm.nih.gov/16268666/) | 2005 | Review | CNS Drugs | Review of triptan use in the management of menstrual migraine |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Case series/Review | Headache | Discussion of naratriptan use in managing intractable migraine |

---

## Canada Market Information

Naratriptan currently holds no Health Canada Drug Identification Number (DIN) and is not marketed in Canada (`total_licenses: 0`).

---

## Safety Considerations

- **Known class-level caution (not from safety module, but from repurposing rationale):** ICHD-3 and American Headache Society guidance list triptans as relatively contraindicated in migraine with brainstem aura, due to theoretical concern about vasoconstrictive effects on the posterior cerebral circulation.
- Structured safety fields (`key_warnings`, `contraindications`, `ddi`) are all marked as data gaps (DG001, blocking) — please refer to the package insert for full safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but it is driven by naratriptan's well-established efficacy in migraine generally — no clinical trial or literature evidence specifically addresses its use in migraine with brainstem aura, and the closest related finding (PMID 25841032) shows *reduced* triptan efficacy in migraine with aura. Combined with existing guideline-level caution against triptan use in this subtype, the evidence does not support advancing beyond a hold.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications for naratriptan (DG001, blocking — currently missing)
- Confirmed mechanism of action data from DrugBank (DG002)
- Any pharmacovigilance or case-level data on triptan use specifically in confirmed brainstem-aura patients
- Neurology/headache-specialist review given the existing contraindication guidance before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

