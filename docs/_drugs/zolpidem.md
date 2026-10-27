---
layout: default
title: Zolpidem
parent: High Evidence (L1-L2)
nav_order: 997
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-13
description: "Zolpidem: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L1). Approved use: Insomnia"
monitor_inn: "Zolpidem"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Zolpidem
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

## Zolpidem: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)
{: .text-alpha }

## One-Sentence Summary

Zolpidem is a sedative-hypnotic originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, with **no registered clinical trials** and **20 publications** (including network meta-analyses and clinical guidelines) currently supporting this direction.
Because this predicted indication is essentially the same as the drug's established use, it is better seen as confirmation of an existing indication than as true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on the mechanistic assessment, zolpidem is a positive allosteric modulator of the GABA-A receptor with preferential affinity for the alpha-1 subunit. This produces sedative-hypnotic effects.

The predicted indication, difficulty initiating and maintaining sleep, is the core feature of insomnia. The prediction therefore mostly restates zolpidem's approved use. The very high score (99.87%) is consistent with this overlap.

The publications reviewed describe zolpidem as a "Z-drug" (with zopiclone, eszopiclone and zaleplon) that is widely used for insomnia. They also note that it carries risks of cognitive impairment, falls, dependence and next-day impairment, particularly in older adults.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Compared pharmacological treatments for acute and long-term management of insomnia disorder in adults |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical practice guideline (AASM) | J Clin Sleep Med | Recommendations for individual drugs used to treat chronic insomnia in adults |
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant vs placebo and zolpidem extended release (active comparator) in older adults with insomnia |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Compared efficacy and safety of lemborexant with other insomnia treatments |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | J Fam Pract | Insomnia is underrecognized and undertreated in primary care; treating it improves outcomes |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs are effective but have side effects including cognitive impairment, tolerance, falls, abuse and dependence |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management recommendations for insomnia in elderly patients |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem is a benzodiazepine receptor agonist and the most widely prescribed hypnotic in the US |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Review | CNS Drugs | Zolpidem extended-release, a dual-layer formulation for sleep onset and maintenance |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02391678 | SUBLINOX | Not specified | Not specified |
| 02370433 | SUBLINOX | Not specified | Not specified |
| 02434946 | APO-ZOLPIDEM ODT | Not specified | Not specified |
| 02436159 | APO-ZOLPIDEM ODT | Not specified | Not specified |
| 02472821 | MINT-ZOLPIDEM ODT | Not specified | Not specified |

Twelve valid single-ingredient licences are held in total. The remaining seven are other zolpidem ODT products from JAMP, PRO and PMS.

---

## Safety Considerations

- **Contraindication signals (from the knowledge graph, not label text)**: anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome, amnestic disorder, retrograde amnesia, substance-related disorder, substance abuse/dependence, and attention deficit hyperactivity disorder.
- **Key warnings (from the mechanistic assessment)**: complex sleep behaviors (boxed warning), next-day impairment, and increased risk in older adults.
- **Drug interactions**: 100 interactions were identified. Major interactions include **morphine** and **liposomal morphine**. Moderate interactions include opium, bupropion, aprepitant, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, miconazole and clotrimazole. The risk is greatest with other CNS depressants.

Please refer to the package insert for the full label warnings and contraindications.

---

## Other Predicted Indications (Low Evidence)

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Benign paroxysmal torticollis of infancy | 99.26% | L5 | Hold | No plausible mechanistic link. The condition is self-limiting and sedative-hypnotics raise safety concerns in infants. |
| Agoraphobia | 99.25% | L5 | Hold | Only a weak rationale. Zolpidem has minimal anxiolytic activity, first-line treatments are established, and Z-drugs carry dependence and misuse potential. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication essentially matches zolpidem's established use in insomnia, and it is supported by network meta-analyses and clinical guidelines. It is also marketed in Canada under 12 licences. No clinical trials are registered for this specific predicted indication, and the safety burden is significant.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- A risk-management plan for complex sleep behaviors, next-day impairment, use in older adults, and co-prescription with CNS depressants and opioids
- If true repurposing is intended, a clearly distinct target indication, since the two other predictions (benign paroxysmal torticollis of infancy and agoraphobia) lack supporting evidence and should remain on hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

