---
layout: default
title: Terconazole
parent: Model Prediction Only (L5)
nav_order: 898
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Terconazole: predicted new indication Trichomonal vulvovaginitis (evidence level L5). Approved use: Vulvovaginal candidiasis"
---

# Terconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

Terconazole is a triazole antifungal originally used to treat vulvovaginal candidiasis.
The TxGNN model's top-ranked prediction is **trichomonal vulvovaginitis**, but **no clinical trials** and only **1 general review** support it, and the mechanism is not plausible. Other predictions (vulvitis, vulvovaginitis, vaginitis) have **L1-level evidence**, but that evidence mostly restates the drug's already-approved candidiasis use rather than a true new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vulvovaginal candidiasis (the approved indication text in the Canadian licence record is blank) |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (for the top prediction: model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (for the top prediction); Proceed with Guardrails only for candidal vulvovaginitis-type indications |

---

## Why is This Prediction Reasonable?

Terconazole is a triazole antifungal. It inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis and disrupts the fungal cell membrane. This is the basis for its use in vulvovaginal candidiasis.

**Trichomonal vulvovaginitis (top prediction):** *Trichomonas vaginalis* is a protozoan, and it lacks ergosterol-dependent membrane biology comparable to that of fungi. There is therefore no plausible mechanistic link. The very high TxGNN score most likely reflects the drug's closeness to "vaginitis" in the knowledge graph rather than a real pharmacological effect. Standard therapy is a nitroimidazole (metronidazole or tinidazole).

**Other predictions:** Vulvitis, vulvovaginitis and vaginitis are supported by trials and publications, but nearly all of that evidence concerns candidal infection, which is the approved use. These are not true repurposing findings. Predictions such as atrophic vaginitis (estrogen deficiency), herpetic vulvovaginitis (a virus), vulvar ulceration, vulvar neoplasm and bacterial vaginosis have no credible mechanism for an azole antifungal.

Note: detailed mechanism-of-action data was not available in the compiled data. The mechanism described here is taken from the literature and from the mechanistic assessments in the data.

---

## Clinical Trial Evidence

The top-ranked prediction (trichomonal vulvovaginitis) has: Currently no related clinical trials registered.

For the closely related candidiasis-type predictions (vulvitis, vulvovaginitis, vaginitis), the main trials are below:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00803738](https://clinicaltrials.gov/study/NCT00803738) | NA | Completed | 572 | Terconazole 80 mg suppositories, test vs reference product; bioequivalence in vulvovaginal candidiasis |
| [NCT02180100](https://clinicaltrials.gov/study/NCT02180100) | Phase 4 | Completed | 140 | Terconazole suppository vs fluconazole in severe vulvovaginal candidiasis |
| [NCT02308007](https://clinicaltrials.gov/study/NCT02308007) | Phase 3 | Completed | 475 | Solubilized metronidazole and/or terconazole intravaginal gels in vaginal infections |
| [NCT02308046](https://clinicaltrials.gov/study/NCT02308046) | Phase 3 | Completed | 212 | Companion trial of terconazole gel in vaginal infections |
| [NCT03473418](https://clinicaltrials.gov/study/NCT03473418) | Phase 3 | Unknown | 69 | Ketoconazole in situ gel vs terconazole cream (terconazole as comparator) |
| [NCT04208555](https://clinicaltrials.gov/study/NCT04208555) | NA | Unknown | 76 | Boric acid vs terconazole in recurrent vulvovaginal candidiasis |

These trials do not test terconazole in trichomoniasis or bacterial vaginosis. NCT02308007 and NCT02308046 involve metronidazole and/or terconazole gels, and any signal in mixed-etiology vaginitis would need separate review.

---

## Literature Evidence

For trichomonal vulvovaginitis, the only publications are a general vaginitis review and an older antifungal review. Key publications for the candidiasis-type indications are shown below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25877666](https://pubmed.ncbi.nlm.nih.gov/25877666/) | 2015 | RCT | Medical Mycology | Terconazole suppository vs oral fluconazole in 140 patients with severe vulvovaginal candidiasis |
| [2381618](https://pubmed.ncbi.nlm.nih.gov/2381618/) | 1990 | RCT | Obstetrics and Gynecology | Placebo-controlled comparison of 0.8% and 1.6% terconazole cream in persistent vulvovaginal candidiasis |
| [3520601](https://pubmed.ncbi.nlm.nih.gov/3520601/) | 1986 | RCT | Pharmatherapeutica | Terconazole vs clotrimazole vaginal tablets in 60 patients with vulvovaginal candidosis |
| [8893111](https://pubmed.ncbi.nlm.nih.gov/8893111/) | 1996 | RCT | Annals of Pharmacotherapy | Weekly terconazole 0.8% cream to prevent recurrent candidal vaginitis |
| [1941796](https://pubmed.ncbi.nlm.nih.gov/1941796/) | 1991 | Randomized comparison | J Reprod Med | Terconazole vs miconazole cream in 900 patients; cure rates 87.9% (0.4%), 83.8% (0.8%) and 81.3% (miconazole) |
| [11220485](https://pubmed.ncbi.nlm.nih.gov/11220485/) | 2000 | Cohort | Infect Dis Obstet Gynecol | Retrospective analysis of terconazole cream in non-albicans Candida vaginitis |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Future non-invasive azole options for vulvovaginal candidiasis |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Boric acid for recurrent vulvovaginal candidiasis |
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | Overview of treating bacterial, fungal and protozoal vaginitis |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review | Chemotherapy | Terconazole as a new broad-spectrum antifungal; in vitro and animal data |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247651 | TARO-TERCONAZOLE | Not specified | Not specified in the compiled data |

---

## Safety Considerations

Please refer to the package insert for safety information.

One case report (PMID 33860751) describes chills, fatigue, chest distress and raised inflammatory markers after a single 80 mg terconazole vaginal suppository. It is an isolated report.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top prediction, trichomonal vulvovaginitis)

**Rationale:**
- The top prediction rests on model score alone (L5). Terconazole has no plausible mechanism against a protozoan, and the standard treatment is a nitroimidazole. The strong evidence for vulvitis, vulvovaginitis and vaginitis (L1) reflects the already-approved candidiasis indication. These could proceed with guardrails, but they are not new repurposing opportunities. The remaining predictions (atrophic, herpetic, ulcerative, neoplastic and bacterial vaginosis) have no supporting mechanism or evidence.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and interaction data from Health Canada (currently a blocking gap)
- Mechanism-of-action data from DrugBank
- For mixed-etiology vaginitis: review of NCT02308007 and NCT02308046 for any activity beyond candidiasis
- For trichomonal vulvovaginitis or bacterial vaginosis: in vitro activity data before any clinical consideration
- Confirmation of the approved indication text and dosage forms for DIN 02247651
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

