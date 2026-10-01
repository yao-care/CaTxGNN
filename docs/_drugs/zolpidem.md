---
layout: default
title: Zolpidem
parent: Model Prediction Only (L5)
nav_order: 990
evidence_level: L5
indication_count: 3
---

# Zolpidem
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

# Zolpidem: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Zolpidem is a sedative-hypnotic that is widely used for insomnia. The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, with **no registered clinical trials** and **20 publications** in the evidence pack. Most of those publications are reviews, network meta-analyses and trials where zolpidem served as a comparator. This looks like confirmation of an established use rather than a new repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in the Canadian licence data; insomnia is zolpidem's established labelled use |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 (systematic reviews and network meta-analyses; no registered trials in the pack) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the database record. Zolpidem is a non-benzodiazepine hypnotic of the imidazopyridine class. It acts as a positive allosteric modulator of GABA-A receptors with preferential affinity for the alpha-1 subunit, and this produces its sedative-hypnotic effect. The literature in the pack describes it the same way (PMID 20945020, PMID 28262178).

This mechanism matches the problem in insomnia, which is difficulty falling asleep and staying asleep. The prediction therefore fits zolpidem's known pharmacology.

The empty original-indication field appears to be a database omission, because insomnia is zolpidem's established labelled use. The high score reflects the model recovering a known drug-disease pair. It does not show a newly discovered use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Compares pharmacological treatments for acute and long-term management of adult insomnia disorder |
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant vs placebo and zolpidem extended-release in older adults with insomnia; zolpidem is the active comparator |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Intern Med | Masked taper plus behavioural intervention for discontinuing benzodiazepine receptor agonist hypnotics |
| [37477771](https://pubmed.ncbi.nlm.nih.gov/37477771/) | 2023 | RCT (post hoc) | CNS Drugs | Effect of daridorexant and zolpidem on night-time wake bouts in insomnia disorder |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | Trial analysis | J Clin Sleep Med | Lemborexant vs zolpidem ER 6.25 mg by polysomnographic insomnia subtype |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Efficacy and safety of lemborexant vs other insomnia treatments |
| [41101148](https://pubmed.ncbi.nlm.nih.gov/41101148/) | 2025 | Network meta-regression and FAERS analysis | Sleep Med | Efficacy and safety comparison of DORAs, benzodiazepines, Z-drugs and melatonin agonists |
| [28262178](https://pubmed.ncbi.nlm.nih.gov/28262178/) | 2017 | Review | Asian J Psychiatry | Zolpidem as a short-acting hypnotic in IR, ER, sublingual and oral spray forms |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs have a strong evidence base for insomnia but carry cognitive impairment, tolerance, rebound insomnia, falls and dependence risks |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem is a BZ-receptor agonist and the most widely prescribed hypnotic in the US |

Most of the trial literature uses zolpidem as a comparator for newer drugs. It supports efficacy only indirectly.

---

## Canada Market Information

12 authorizations are listed in total. The five below are shown. Dosage form and approved-indication text were not provided for these records.

| DIN | Product Name |
|---------|------|
| 02391678 | SUBLINOX |
| 02434946 | APO-ZOLPIDEM ODT |
| 02436159 | APO-ZOLPIDEM ODT |
| 02370433 | SUBLINOX |
| 02472821 | MINT-ZOLPIDEM ODT |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication coincides with zolpidem's established use, and the literature consistently treats it as a standard insomnia hypnotic. No registered trials were retrieved, and the available papers support efficacy mainly through comparator arms. The decision therefore rests on the established use, not on new evidence.

The other two TxGNN predictions, benign paroxysmal torticollis of infancy and agoraphobia, have no trials, no literature and no clear mechanistic link. Both should be on **Hold**. Zolpidem is also not approved for pediatric use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Confirmation of the Canadian labelled indication, dosage forms and dose limits (including for older adults)
- Mechanism-of-action data from DrugBank
- Guardrails covering dependence and tolerance, complex sleep behaviours, and next-day impairment
- Direct check of the product label and current guidelines, since the supporting literature is largely indirect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

