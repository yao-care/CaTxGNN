---
layout: default
title: Nizatidine
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 7
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

# Nizatidine: From an Unlisted Original Indication to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is a histamine H2-receptor antagonist (an acid-suppressing drug) marketed in Canada as AXID. The Canadian licence record does not state its original indication.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **0 registered clinical trials** and **19 publications**, including several randomized, double-blind studies in duodenal and gastric ulcer.
This is very likely an existing labeled use rather than true repurposing, and it should be confirmed against the product label.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence record |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (based on published randomized controlled studies; no registered trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. The published literature, however, describes nizatidine as an H2-receptor antagonist. In animal studies it was more active than cimetidine on a weight-for-weight basis, and in humans it is a potent inhibitor of basal, nocturnal and stimulated gastric acid secretion.

Peptic ulcers are acid-peptic lesions, and lowering gastric acid is the established route to healing them. The high TxGNN score is consistent with this. The retrieved studies already test nizatidine in duodenal and gastric ulcer healing, and in preventing recurrence. The prediction therefore looks like confirmation of a known use rather than a new one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 8-week multicenter, double-blind comparison of nizatidine 150 mg twice daily, 300 mg at bedtime and placebo in healing benign gastric ulcers |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled, double-blind trial of nizatidine 150 mg twice daily for duodenal ulcer healing and recurrence |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | One-year maintenance study in 513 patients with healed duodenal ulcer. Cumulative recurrence at 12 months was 34% with nizatidine vs 64% with placebo |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | RCT | Isr J Med Sci | Double-blind, placebo-controlled trial in 55 patients with active duodenal ulcer. Nizatidine 300 mg nightly for 4 weeks was assessed for ulcer healing and mucosal inflammatory mediators |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepato-gastroenterology | 8-week study in 101 gastric ulcer patients comparing nizatidine (two regimens) with ranitidine. Four-week healing rates with nizatidine were 51.5% (300 mg at bedtime) and 61.8% (150 mg twice daily) |
| [1344473](https://pubmed.ncbi.nlm.nih.gov/1344473/) | 1992 | RCT | Med Pregl | Prospective, randomized, double-blind study of nizatidine vs ranitidine in 120 duodenal ulcer patients, with endoscopic control after 1–2 months |
| [8429117](https://pubmed.ncbi.nlm.nih.gov/8429117/) | 1993 | Randomized pharmacodynamic study | J Clin Pharmacol | 24-hour intragastric pH monitoring in 12 duodenal ulcer patients in remission. Nizatidine 150 mg and 300 mg twice daily and ranitidine 300 mg twice daily all raised pH above placebo (P < .001) |
| [2575571](https://pubmed.ncbi.nlm.nih.gov/2575571/) | 1989 | Pharmacodynamic study | Hepato-gastroenterology | Nizatidine 150 mg vs ranitidine 150 mg in 10 patients with healed duodenal ulcer. Total acid inhibition was similar, but nizatidine acted more rapidly |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Preliminary review of nizatidine's pharmacology and its use in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of peptic ulcer therapy. Nizatidine and roxatidine are described as safe and effective but without new clinically important properties |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 778338 | AXID |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized, double-blind studies support nizatidine for healing duodenal and gastric ulcers and for preventing duodenal ulcer recurrence. However, the evidence is old (1987–1994) and no clinical trials are registered. The indication also appears to be an existing labeled use rather than true repurposing.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings and contraindications), which is currently a blocking gap. It should also confirm the labeled indications for AXID, so the prediction is not presented as new.
- Mechanism-of-action data from DrugBank.
- Confirmation of study designs for the papers whose designs were inferred only from titles or abstracts.
- Note that the other predicted indications (gastrojejunal ulcer, gastroduodenitis, peptic ulcer perforation, duodenal obstruction, duodenogastric reflux, multiple endocrine neoplasia) have weak or indirect evidence. They are classified as Research Question or Hold and are not recommended for advancement.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

