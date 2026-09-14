---
layout: default
title: Terconazole
parent: 僅模型預測 (L5)
nav_order: 762
evidence_level: L5
indication_count: 10
---

# Terconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Terconazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Terconazole is a triazole antifungal, established internationally for vulvovaginal candidiasis (per the drug's own literature record), though no Canadian license data is currently on file for this product. TxGNN's top-ranked prediction is **Trichomonal Vulvovaginitis**, but this is supported by only **1 clinical trial** and **3 publications**, none of which specifically tests terconazole against *Trichomonas vaginalis*. The predicted mechanism does not align with the drug's known antifungal activity, since trichomoniasis is a protozoal infection typically treated with metronidazole/tinidazole.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vulvovaginal candidiasis (per international drug literature; no Canadian license record — drug not marketed) |
| Predicted New Indication | Trichomonal Vulvovaginitis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on the literature attached to this candidate, terconazole is a triazole antifungal that inhibits fungal cytochrome P450-dependent ergosterol synthesis, and has been extensively studied and used for vulvovaginal candidiasis (a fungal infection caused by *Candida* species).

Trichomonal vulvovaginitis, however, is caused by the protozoan parasite *Trichomonas vaginalis*, and standard treatment relies on nitroimidazoles (metronidazole, tinidazole) that target anaerobic/protozoal metabolism — a pathway unrelated to ergosterol synthesis. The single clinical trial linked to this prediction (NCT00503542) is a small, non-specific pilot study of general vaginal complaint management, not a trichomoniasis efficacy trial, and the three literature entries are general vaginitis reviews or an antifungal drug-profile paper, none demonstrating anti-protozoal activity.

By contrast, other TxGNN-predicted indications for terconazole in this same Evidence Pack — vulvitis, vulvovaginitis, and vaginitis (candidal) — are mechanistically consistent with the drug's known antifungal action and are backed by multiple completed Phase 3/4 RCTs (evidence level L1). The mismatch specific to trichomonal vulvovaginitis appears to reflect a knowledge-graph co-occurrence pattern (shared anatomical/symptom space with vaginitis broadly) rather than a genuine pharmacological link.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503542](https://clinicaltrials.gov/study/NCT00503542) | Early Phase 1 | Completed | 46 | Pilot study comparing two general management approaches for vaginal complaints in primary care; not a trichomoniasis-specific terconazole efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | General review of vaginitis (bacterial, fungal, protozoal); does not report terconazole trichomoniasis data. |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Comprehensive Therapy | Review of vulvovaginitis epidemiology, diagnosis, and therapy in healthy women; general overview only. |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review (drug profile) | Chemotherapy | Describes terconazole's broad-spectrum *antifungal* activity against yeasts/dermatophytes; no anti-protozoal data reported. |

---

## Canada Market Information

No terconazole products are currently registered or marketed in Canada — `total_licenses = 0`, and no DIN records are available in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this candidate — see Data Gap DG001 in the source Evidence Pack, flagged as blocking for the safety initial assessment stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (trichomonal vulvovaginitis) is mechanistically inconsistent with terconazole's antifungal mode of action, and the supporting evidence is minimal and non-specific (1 pilot trial, 3 general reviews, evidence level L4). Combined with a blocking data gap on Canadian safety/label information, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Health Canada/product monograph warnings and contraindications (currently blocking — DG001)
- A trichomoniasis-specific pharmacological rationale or in vitro/in vivo anti-*Trichomonas* activity data, if this indication is to be pursued further
- Alternative: prioritize this drug's higher-evidence candidates from the same Evidence Pack (vulvitis, vulvovaginitis, candidal vaginitis — all L1/S3, "Proceed with Guardrails"), which are mechanistically sound and already supported by multiple completed Phase 3/4 RCTs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

