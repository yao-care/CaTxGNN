---
layout: default
title: Nizatidine
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Nizatidine: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "NIZATIDINE"
predicted_indications: ["duodenal obstruction", "multiple endocrine neoplasia"]
---

# Nizatidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Nizatidine: From Gastric Ulcer to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is an H2-receptor antagonist originally used for gastric ulcer, duodenal ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis and dyspepsia.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **0 registered clinical trials** and **20 publications** currently supporting this direction.
Note that this prediction largely confirms an existing use rather than a true new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis, dyspepsia, duodenal ulcer (the Canadian licence record contains no indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (based on published randomized placebo-controlled trials; study designs were not verified beyond titles and abstracts) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nizatidine blocks histamine H2 receptors on gastric parietal cells and so suppresses basal, nocturnal and stimulated gastric acid secretion. Detailed mechanism-of-action data were not available in the data compiled for this report, but this class effect is well described in the retrieved literature.

Active peptic ulcer disease (duodenal and gastric) is acid-dependent and already falls within nizatidine's original indications. This is therefore a confirmation of an existing use, not a true repurposing candidate. The high TxGNN score reflects how close the disease sits to nizatidine's known indications in the knowledge graph.

Several lower-ranked predictions are weaker and mostly extrapolations from ulcer disease:
- **Gastrojejunal ulcer** (99.94%): acid suppression is plausible for marginal ulcers, but no retrieved paper studies this condition, and proton pump inhibitors are generally preferred. Evidence level L4, a research question only.
- **Gastroduodenitis** (99.58%): indirect support from NSAID-induced lesion prevention studies and an in vitro antioxidant study. Evidence level L3, a research question only.
- **Peptic ulcer perforation, duodenal obstruction, duodenogastric reflux and multiple endocrine neoplasia**: no direct evidence and a weak mechanistic fit. Evidence level L5, hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 8-week multicentre, double-blind comparison of nizatidine 150 mg twice daily or 300 mg at bedtime versus placebo in active benign gastric ulcer |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled trial of nizatidine 150 mg twice daily for healing and recurrence of active duodenal ulcer |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | One-year maintenance trial in 513 patients; ulcer recurrence at 12 months was 34% with nizatidine versus 64% with placebo |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | RCT | Isr J Med Sci | Placebo-controlled trial in 55 patients with active duodenal ulcer, nizatidine 300 mg nightly for 4 weeks, assessing healing and mucosal inflammatory mediators |
| [1977089](https://pubmed.ncbi.nlm.nih.gov/1977089/) | 1990 | RCT | Neth J Med | Nizatidine versus ranitidine in 230 patients with gastric or duodenal ulcers (Dutch part of a European multicentre trial) |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepatogastroenterology | 8-week double-blind comparison of nizatidine (two regimens) and ranitidine in 101 gastric ulcer patients |
| [2892253](https://pubmed.ncbi.nlm.nih.gov/2892253/) | 1987 | Safety analysis | Scand J Gastroenterol Suppl | Safety review of 3,800 nizatidine-treated patients in US and European ulcer trials |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Review of pharmacology and therapeutic use of nizatidine in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy of peptic ulcer; nizatidine described as safe and effective |
| [8429117](https://pubmed.ncbi.nlm.nih.gov/8429117/) | 1993 | Pharmacodynamic study | J Clin Pharmacol | 24-hour intragastric pH control with nizatidine 150 mg and 300 mg versus ranitidine and placebo |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00778338 | AXID | Not listed | Not listed |

---

## Safety Considerations

- **Disease-related contraindications flagged in the knowledge graph** (not label text): liver disease, gallbladder disease, impaired renal function, and gastric cancer and its subtypes (gastric neoplasm, diffuse gastric adenocarcinoma, linitis plastica, gastric carcinoma). Acid suppression can mask symptoms of gastric malignancy, so cancer should be excluded before treatment.
- **Drug interactions**: 100 interactions were identified. Those listed include:
  - **Major**: atazanavir, dasatinib
  - **Moderate**: acalabrutinib, bosutinib, brigatinib, cefditoren, cefpodoxime, cefuroxime, ceritinib, chlorpropamide, dabrafenib, dacomitinib
  - **Minor**: ketorolac, ibuprofen, alendronic acid, axitinib, cyanocobalamin, diclofenac, magnesium oxide, oxaprozin

  Many of the major and moderate interactions involve drugs whose absorption depends on gastric acidity.
- Please also refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For active peptic ulcer disease, published randomized placebo-controlled and comparator trials support nizatidine, and it is already marketed in Canada (AXID). This is confirmation of an existing use, not a new indication. The other predicted indications lack direct evidence and should be treated as research questions or held.

**To proceed, the following is needed:**
- The Canadian package insert (warnings, contraindications, approved indications and dosage form), which is a blocking gap for safety screening
- Detailed mechanism of action data
- Verification of the trial designs and results beyond titles and abstracts
- Direct evidence before pursuing gastrojejunal ulcer or gastroduodenitis, with comparison against proton pump inhibitors
- A review of clinically significant interactions, especially with drugs that need gastric acid for absorption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

