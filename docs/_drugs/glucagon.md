---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Glucagon: From Severe Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a pancreatic peptide hormone. Its Canadian product, BAQSIMI, is a nasal glucagon used for severe hypoglycemia.
The TxGNN model predicts it may be useful for **irritable bowel syndrome (IBS)**. However, none of the **10 clinical trials** or **20 publications** retrieved tests glucagon itself in IBS. They all concern related GLP-1 receptor agonists or general gut biology, so this is a research question rather than a supported indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe hypoglycemia (based on the BAQSIMI product; the licence record contains no indication text) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 (indirect evidence only; nothing tests glucagon in IBS) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glucagon is not available in the current record. Based on known information, glucagon and GLP-1 are both derived from proglucagon, and both slow gastrointestinal motility. Glucagon is also already used clinically as a short-acting gut antispasmodic. Since IBS involves disordered motility and visceral pain, a plausible link exists.

The main caveat is that glucagon acts on the glucagon receptor, not the GLP-1 receptor. Nearly all the supporting signals come from GLP-1 receptor agonists:

- ROSE-010, a GLP-1 analog, reduced pain during IBS attacks in clinical studies.
- Native GLP-1 inhibits gastric and small-bowel motility in humans.
- Exendin-4 improved GI dysfunction in a rat IBS model.

These findings cannot be assumed to apply to glucagon. The 99.24% TxGNN score is a knowledge-graph prediction and should be read as a hypothesis, not as evidence of efficacy.

---

## Clinical Trial Evidence

No trial tests glucagon in IBS. Only the trials with some relevance are listed below. The other retrieved trials (dietary, exercise, microbiota and obesity studies, plus one unrated organoid study) are unrelated to glucagon.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analog) effect on gastric, small-bowel and colonic motor function in women with constipation-predominant IBS. Most disease-relevant trial, but indirect (not glucagon). |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 vs ROSE-010 on stomach, duodenal and jejunal motility. Supports the motility-inhibition mechanism, but involves no glucagon or IBS patients. |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide vs placebo for chronic high bowel frequency after ileal pouch-anal anastomosis. Very weak indirect support. |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise training, gut dysbiosis and GLP-1 levels in IBS. A non-drug study with only a tangential incretin link. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic review / meta-analysis | Front Endocrinol | GLP-1 receptor agonists and IBS. GLP-1 and ROSE-010 inhibit GI motility in IBS patients. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT (secondary analysis) | Scand J Gastroenterol | Cross-analysis of ROSE-010 pain relief in IBS to identify the most suitable patient subgroup. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Explores the role of GLP-1-secreting L-cells in IBS pathophysiology. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolized GLP-1 for diabetes and IBS. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Novel investigational drugs for constipation-predominant IBS. |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Clinical study | Clin Res Hepatol Gastroenterol | Serum GLP-1 is decreased and correlates with abdominal pain in IBS-C. |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Animal study | Neurogastroenterol Motil | Exendin-4 ameliorated GI dysfunction in a rat IBS model. |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Clinical study | Front Nutr | Circulating GLP-1 rose after a low-FODMAP diet in IBS patients. |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cell Mol Gastroenterol Hepatol | Overview of the brain-gut-microbiome axis. |

All of these concern GLP-1 or general IBS biology, not glucagon.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2492415 | BAQSIMI |

Dosage form and approved-indication text are not recorded in the current licence data.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible. However, all supporting clinical evidence involves GLP-1 receptor agonists, which act on a different receptor. There is no direct evidence for glucagon in IBS, so it remains a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Detailed mechanism-of-action data for glucagon, and confirmation of its licensed indication
- A mechanistic or pilot motility and pain study of glucagon in IBS patients
- A safety assessment for this use, focusing on hyperglycemia, nausea and glucagon's short half-life

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

