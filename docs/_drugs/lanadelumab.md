---
layout: default
title: Lanadelumab
parent: Model Prediction Only (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Hereditary Angioedema Prophylaxis to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab is a monoclonal antibody that inhibits plasma kallikrein, and its established use is preventing attacks of hereditary angioedema (HAE). The TxGNN model predicts it is effective for **C1 inhibitor deficiency**, which is essentially the same disease, so this is a confirmation of an approved use rather than a true repurposing finding. There are **22 clinical trials** and **20 publications** supporting this direction, including a pivotal placebo-controlled Phase 3 trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Health Canada records provided (the label text is empty). The mechanism and evidence indicate HAE attack prevention. |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* the input pack assigned L1. Under the stated rules, L1 needs at least two completed Phase 3 RCTs, and only one is present (HELP, NCT02586805). The other Phase 3 studies are open-label, so this report uses L2.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is missing from the input. The following comes from the pack's mechanistic rationale and the literature. Lanadelumab inhibits plasma kallikrein. In C1 inhibitor deficiency (HAE), the missing C1-INH leaves kallikrein unchecked, so excess bradykinin is produced. Bradykinin drives the swelling attacks, so blocking kallikrein directly addresses the cause.

The predicted indication is the same disease as the drug's known use, so the prediction is very reasonable. The empty "original indication" field is a data gap, not evidence of a novel use.

One subset needs separate handling: **acquired** C1-INH deficiency is supported only by small case reports and series (PMIDs 33556593, 36379410).

The other nine predicted diseases (for example pancreatitis, Glanzmann thrombasthenia and myositis-type disorders) have no trials or literature. Their links are speculative or likely graph artifacts, and all are rated Hold.

---

## Clinical Trial Evidence

The 10 most relevant of 22 registered trials are listed below. No results were provided, so the findings column describes each trial's design and purpose.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP study: randomized, double-blind, placebo-controlled trial of attack prevention in type I/II HAE (pivotal) |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP extension: open-label long-term safety and efficacy |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING: safety and pharmacokinetics in children aged 2 to under 12 years |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Open-label efficacy and safety in Japanese patients with HAE type I/II |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Open-label safety, pharmacokinetics and efficacy over 26 weeks in Chinese patients |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan expanded access program for teenagers and adults with type I/II HAE |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | ENABLE: 3-year real-world study comparing attacks before and after starting lanadelumab |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER: US/Canada observational study of attack rate before and after treatment |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | N/A | Completed | 207 | Retrospective chart review of attack-free rates on 2-weekly and 4-weekly dosing |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | Completed | 155 | Japan post-marketing survey of long-term safety and effectiveness |

NCT04444895 (Phase 3, completed, n=73) studies non-histaminergic angioedema with **normal** C1-INH. It is not a direct test of the predicted indication, so it is left out of the table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab vs placebo for preventing HAE attacks (HELP trial) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label extension | Allergy | HELP OLE: long-term effectiveness and safety in patients aged 12 and over |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic review | Clin Rev Allergy Immunol | Characterizes breakthrough attacks in patients on long-term prophylaxis |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network meta-analysis | Drugs R D | Indirect comparison of long-term prophylaxis options, including lanadelumab |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect treatment comparison | J Comp Eff Res | Lanadelumab vs a C1-esterase inhibitor in children under 12 |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observational | J Allergy Clin Immunol Pract | INTEGRATED: multicountry real-world effectiveness |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Preclinical and Phase I studies in C1-INH-deficient HAE |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | First global approval; significant attack reduction vs placebo |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case series | J Allergy Clin Immunol Pract | Efficacy in acquired C1-INH deficiency |
| [36379410](https://pubmed.ncbi.nlm.nih.gov/36379410/) | 2023 | Case series | J Allergy Clin Immunol Pract | Efficacy in angioedema from acquired C1-INH deficiency |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2505614 | TAKHZYRO | Not listed | Not listed |
| 2480948 | TAKHZYRO | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found. Lanadelumab can prolong aPTT, which can confuse the interpretation of coagulation tests and needs care in patients with bleeding disorders.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed placebo-controlled Phase 3 trial, long-term extension data and many real-world studies support lanadelumab for C1-INH deficiency (HAE). The prediction matches the drug's established use, so it adds little as a repurposing finding.

**To proceed, the following is needed:**
- Confirm the approved indication text for both Canadian DINs, which are blank in the records provided
- Obtain the Health Canada package insert warnings and contraindications
- Obtain detailed mechanism-of-action data from DrugBank
- Evaluate the acquired C1-INH deficiency subset separately, since its evidence is limited to small case series
- Keep the other nine predicted indications on Hold, since none has any clinical or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

