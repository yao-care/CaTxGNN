---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 782
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
description: "Prucalopride: predicted new indication Hypoalphalipoproteinemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Prucalopride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Prucalopride: Hypoalphalipoproteinemia
{: .text-alpha }

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist (prokinetic) originally used to treat chronic constipation.
The TxGNN model predicts it may be effective for **hypoalphalipoproteinemia** (low HDL cholesterol), but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 10) |
| Number of DINs | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, prucalopride is a selective 5-HT4 receptor agonist that stimulates gastrointestinal motility, and its efficacy in constipation is established.

Mechanistically, there is no known pathway connecting 5-HT4 agonism to HDL metabolism, so the prediction does not have a plausible biological explanation at present. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or pharmacological reasoning, and no trials or publications support it.

Other top-ranked predictions show the same pattern. Most are also unsupported (homozygous familial hypercholesterolemia, oral candidiasis, strongyloidiasis, HIV infection). The only partly plausible group is amyloidosis (including primary amyloidosis and amyloid neuropathy). In these, gut involvement can cause dysmotility or chronic intestinal pseudo-obstruction, where a prokinetic might relieve symptoms. This would treat GI symptoms rather than the underlying disease, and no efficacy data exist. These are better framed as research questions than as repurposing candidates for the top-ranked indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for hypoalphalipoproteinemia.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02491591 | APO-PRUCALOPRIDE | Not specified | Not specified |
| 02493497 | JAMP PRUCALOPRIDE | Not specified | Not specified |
| 02550377 | NRA-PRUCALOPRIDE | Not specified | Not specified |
| 02377012 | RESOTRAN | Not specified | Not specified |
| 02377020 | RESOTRAN | Not specified | Not specified |

Five of the 10 valid single-ingredient licences are shown. All 10 are valid, and none are cancelled.

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: ulcerative colitis, inflammatory bowel disease, intestinal perforation.
- **Drug Interactions**: 98 interactions were found. Examples of moderate-level interactions include:
  - anticholinergics (aclidinium, atropine, hyoscyamine, glycopyrronium, clidinium, benzatropine, biperiden)
  - hormonal contraceptives (levonorgestrel, norethisterone, ethinylestradiol)

  Minor-level examples include nifedipine, afatinib, alpelisib, amiodarone, cobicistat, captopril, diltiazem, spironolactone, carvedilol and conivaptan.

Package insert warnings and contraindications were not available, so please refer to the Health Canada package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There is no mechanistic link, trial or publication for hypoalphalipoproteinemia, and the safety review cannot proceed without label data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Mechanism of action data (for example from DrugBank)
- A credible biological hypothesis linking 5-HT4 agonism to HDL metabolism, with preclinical or observational support
- Approved indication text and dosage forms for the Canadian licences
- Optionally, evaluation of the amyloidosis-related GI dysmotility indications as a separate research question, since they have the most plausible (though indirect) rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

