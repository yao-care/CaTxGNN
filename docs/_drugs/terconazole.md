---
layout: default
title: Terconazole
parent: Moderate Evidence (L3-L4)
nav_order: 891
evidence_level: L4
indication_count: 10
---

# Terconazole
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

# Terconazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Terconazole is a topical triazole antifungal. The published literature in this pack describes it for vulvovaginal candidiasis, but the Canadian license record does not state an approved indication.
The TxGNN model predicts it may be effective for **trichomonal vulvovaginitis**, but only **1 clinical trial** (a general pilot study) and **3 general or antifungal publications** relate to this prediction, and none tests terconazole against *Trichomonas vaginalis*.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record (literature describes vulvovaginal candidiasis) |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. From the literature, terconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase). This blocks ergosterol synthesis and disrupts fungal membranes. It is highly active against *Candida* species.

Trichomonal vulvovaginitis is a different kind of infection. It is caused by a protozoan, *Trichomonas vaginalis*, and is treated with 5-nitroimidazoles such as metronidazole. No plausible direct mechanism links terconazole to this organism. The high TxGNN score most likely reflects the "vaginitis" neighbourhood in the knowledge graph rather than shared pharmacology. This prediction should be treated as a graph-proximity artifact until direct evidence shows otherwise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503542](https://clinicaltrials.gov/study/NCT00503542) | Early Phase 1 | Completed | 46 | Pilot study of two ways to manage women with vaginal complaints in primary care. It does not isolate terconazole or show an anti-trichomonal effect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | Overview of bacterial, fungal and protozoal vaginitis. It is a general review and does not evaluate terconazole for trichomoniasis. |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Comprehensive Therapy | Epidemiology, diagnosis and therapy of vaginitis in healthy women. It is general and not terconazole-specific. |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review | Chemotherapy | Terconazole is highly active in vitro against yeasts and filamentous fungi and effective in topical animal models of dermatophytosis and candidosis. It supports antifungal activity only. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2247651 | TARO-TERCONAZOLE | Not specified | Not specified |

---

## Safety Considerations

Drug interaction queries returned no records. The license record has no warnings or contraindications, so please refer to the package insert for safety information.

One case report describes a systemic reaction (chills, fatigue, chest distress and raised inflammatory markers) after a single 80 mg terconazole vaginal suppository ([PMID 33860751](https://pubmed.ncbi.nlm.nih.gov/33860751/)). It appears in the evidence for other predicted indications and should be considered in any safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Terconazole has no known activity against *Trichomonas vaginalis*, and the only supporting data are general vaginitis reviews and a non-specific pilot study. The prediction looks like a knowledge-graph artifact, not a pharmacological signal.

The same evidence pack shows much stronger support for related fungal indications. Vulvitis, vulvovaginitis and vaginitis each reach L1 with Proceed with Guardrails, supported by randomized trials in vulvovaginal candidiasis. These are most likely established antifungal uses rather than true repurposing, and they should be evaluated separately.

**To proceed, the following is needed:**
- Direct in vitro or clinical evidence of terconazole activity against *Trichomonas vaginalis*, which is currently absent
- The Health Canada package insert, to confirm the approved indication, warnings and contraindications
- Detailed mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

