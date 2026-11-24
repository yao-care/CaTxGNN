---
layout: default
title: Tiotropium
parent: Model Prediction Only (L5)
nav_order: 915
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "TIOTROPIUM"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
description: "Tiotropium: predicted new indication Respiratory malformation (evidence level L5). In Canada: 5 DINs (5 marketed)"
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Tiotropium: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Tiotropium is a long-acting inhaled anticholinergic bronchodilator marketed in Canada.
The TxGNN model predicts it may be relevant to **respiratory malformation**, but the supporting evidence is indirect: **3 clinical trials** (all in cystic fibrosis) and **5 publications** (none studying this condition directly) were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 5 of 5) |
| Number of DINs | 5 (marketed: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tiotropium: "Tiotropium is a long-acting, antimuscarinic agent, which is often referred to as an anticholinergic. It has similar affinity to the subtypes of muscarinic receptors, M 1 to M 5. In the airways, it exhibits pharmacological effects through inhibition of M 3 -receptors at the smooth muscle leading to bronchodilation." ([DailyMed: Spiriva Handihaler (tiotropium bromide) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=820839ef-e53d-47e8-a3b9-d911ff92e6a9), label version 2025-11-10; accessed 2026-11-19.) Tiotropium belongs to the class of long-acting muscarinic antagonists. Drugs in this class block cholinergic signalling in the airways and relax airway smooth muscle.

The link to respiratory malformation is indirect. Bronchodilation could in principle ease secondary airflow obstruction, but there is no evidence that tiotropium acts on a structural malformation itself. The linked trials enrolled patients with cystic fibrosis, not people with respiratory malformations. The score therefore most likely reflects overlap in how the conditions are classified rather than a true clinical signal. The prediction should be viewed as a hypothesis only.

## Clinical Trial Evidence

None of the trials below studies respiratory malformation directly. All were rated as not directly supporting this indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Phase 3 | Completed | 464 | Placebo-controlled trial of tiotropium 5 mcg once daily via Respimat for 12 weeks in cystic fibrosis; efficacy and safety |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Phase 2 | Completed | 510 | Two doses (2.5 and 5 mcg) vs placebo for 12 weeks in cystic fibrosis; lung function and dose selection |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Phase 1 | Completed | 113 | Safety, tolerability and pharmacokinetics of single and multiple doses (28 days) in children and adults with cystic fibrosis |

## Literature Evidence

None of these publications addresses respiratory malformation directly; they concern related respiratory topics.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31522031](https://pubmed.ncbi.nlm.nih.gov/31522031/) | 2019 | RCT | Respiratory Medicine | Tiotropium/olodaterol-induced lung deflation and cardiocirculatory responses to exertion in COPD |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Review | Int J Chron Obstruct Pulmon Dis | Dual bronchodilation with indacaterol-glycopyrronium in COPD and its effect on patient outcomes |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Cohort/Observational | Respiratory Medicine | Nasal ciliary beating is depressed in COPD subjects |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | Preclinical | Chem Biol Interact | Mechanisms of ventilatory dysfunction in mice exposed to an organophosphorus nerve agent |
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Case report | Rev Fac Cien Med (Cordoba) | COVID-19 infection in a young patient with pectus excavatum |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02246793 | SPIRIVA | TIOTROPIUM (TIOTROPIUM BROMIDE MONOHYDRATE) | Marketed |
| 02435381 | SPIRIVA RESPIMAT | TIOTROPIUM (TIOTROPIUM BROMIDE MONOHYDRATE) | Marketed |
| 02441888 | INSPIOLTO RESPIMAT | OLODATEROL (OLODATEROL HYDROCHLORIDE); TIOTROPIUM (TIOTROPIUM BROMIDE MONOHYDRATE) | Marketed |
| 02537850 | LUPIN-TIOTROPIUM | TIOTROPIUM (TIOTROPIUM BROMIDE MONOHYDRATE) | Marketed |
| 02550865 | APO-TIOTROPIUM | TIOTROPIUM (TIOTROPIUM BROMIDE MONOHYDRATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The main ones are moderate-level interactions with other anticholinergic agents, including hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, scopolamine, propantheline, methscopolamine and mepenzolate. Moderate interactions were also listed with eluxadoline, prucalopride and inhaled human insulin. Cimetidine is listed as minor.
- **Conditions of concern**: Recorded contraindication relationships include benign prostatic hyperplasia, impaired renal function, angle-closure (closed-angle) glaucoma and bladder neck obstruction. These come from database relations, not from label text.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9995), but no cited trial or publication studies respiratory malformation itself. The trials were conducted in cystic fibrosis, and the mechanistic link is indirect. A bronchodilator is unlikely to alter a structural malformation.

**To proceed, the following is needed:**
- Clear definition of the target population within respiratory malformation and a plausible clinical benefit (such as relief of secondary airflow obstruction)
- Studies, even exploratory, that enrol patients with this condition
- Mechanism of action data
- Package insert warnings and contraindications from Health Canada, to complete safety screening

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Spiriva Handihaler (tiotropium bromide) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=820839ef-e53d-47e8-a3b9-d911ff92e6a9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

