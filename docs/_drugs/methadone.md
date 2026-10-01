---
layout: default
title: Methadone
parent: Moderate Evidence (L3-L4)
nav_order: 591
evidence_level: L4
indication_count: 7
---

# Methadone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Methadone: From Opioid Dependence and Pain Management to Tourette Syndrome

## One-Sentence Summary

Methadone is a long-acting opioid used in opioid dependence treatment and chronic pain management. The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are currently **0 registered clinical trials** and only **5 publications**, none of them randomized trials. The strongest item is a 1992 case-level report, so this is a model-driven hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data provided. The literature describes methadone use in opioid dependence and pain management |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Methadone is a mu-opioid agonist that also antagonizes the NMDA receptor, according to a 2009 review of its pharmacology. It is established in opioid dependence and pain management, and mechanistically it may be applicable to Tourette syndrome, but no validated mechanism for this condition is provided.

The link between the original and new indications is indirect. A 2007 preclinical study proposes that opioid-system modulation influences 5-HT2A/C-mediated behaviors (head twitch) related to tics, stereotypies, and compulsive symptoms. It also notes that opiate drugs are effective in treatment-refractory OCD and Tourette syndrome. This gives a biologically plausible direction, but it comes from animal work and a general statement, not from human efficacy data.

The very high TxGNN score (99.76%) is a model output only. The one directly relevant human item is a 1992 report titled "Methadone treatment of Tourette's disorder". It has no abstract in the record, so its findings cannot be confirmed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Case report/series (inferred from title) | Am J Psychiatry | "Methadone treatment of Tourette's disorder". This is the only directly relevant treatment report. No abstract is available, so outcomes cannot be confirmed |
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Preclinical | Psychopharmacology | Atypical opiates studied through 5-HT2A/C-mediated behavior. Opiates are noted as effective in treatment-refractory OCD and Tourette syndrome |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Review | Curr Opin Neurol | Review of non-genetic causes of chorea. Only background differential-diagnosis context, with no methadone treatment data |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Review | Palliat Care Soc Pract | Review of novel analgesics for neuropathic pain in advanced cancer. Not specific to Tourette syndrome |
| [30395551](https://pubmed.ncbi.nlm.nih.gov/30395551/) | 2018 | Cohort/case series | J Psychiatr Pract | Heroin addiction in Serbian patients with Tourette syndrome. This describes comorbidity, not treatment benefit |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02552736 | PMS-METHADONE HYDROCHLORIDE ORAL CONCENTRATE |
| 02495872 | ODAN-METHADONE |
| 02241377 | METADOL |
| 02394618 | METHADOSE |
| 02247698 | METADOL |

Five of the 19 authorizations are shown.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Tourette syndrome is limited to one 1992 case-level report, one preclinical study, and non-treatment papers, with no clinical trials. The high TxGNN score alone does not justify moving forward. The other predicted indications reviewed (nephrogenic syndrome of inappropriate antidiuresis, trichotillomania, headache disorder, manic bipolar affective disorder, trigeminal autonomic cephalalgia, common cold) are also on Hold. Several of these look like graph or term-matching artifacts.

**To proceed, the following is needed:**
- The full text of the 1992 report (PMID 1728167) to confirm design, dose, and outcome
- Health Canada product monograph warnings and contraindications, which are currently missing and block the safety screening
- Mechanism of action data (for example from DrugBank) to test the opioid/NMDA hypothesis in tic disorders
- Any controlled or prospective human data in Tourette syndrome, and an assessment of the QT, respiratory depression, and dependence risks in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

