---
layout: default
title: Aluminum Hydroxide
parent: Model Prediction Only (L5)
nav_order: 43
evidence_level: L5
indication_count: 4
---

# Aluminum Hydroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Aluminum Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Aluminum hydroxide is an antacid, and the Health Canada labels supplied contain no approved-indication text, so the original indication is inferred rather than confirmed. The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but there are **0 registered clinical trials** and **20 publications** on this indication. Most of the publications are older reviews and mechanistic studies, with one small randomized trial. This is most likely an established antacid use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the label data provided (likely antacid use) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L2 (the one RCT has no Phase label and is a 1981 study of a combination regimen, so this grading is borderline) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the literature, aluminum hydroxide neutralizes gastric acid, raises intragastric pH and inhibits pepsin activity. Several studies also describe a cytoprotective, ulcer-healing effect beyond simple buffering. The proposed pathways are stimulation of endogenous prostaglandins and epidermal growth factor. These findings come mainly from rat models and small human pharmacology studies.

Peptic ulcer is driven by acid and pepsin injury to the gastric or duodenal mucosa, so a drug that lowers acidity and protects the mucosa fits the disease. That is why the prediction is plausible. Aluminum hydroxide is also the active component of sucralfate, and one cell study found that aluminum hydroxide itself protected gastric epithelial cells from acid- and pepsin-induced damage.

The evidence is mostly old, and modern care relies on proton pump inhibitors, H2 blockers and *H. pylori* eradication. Any new development would therefore have to be positioned as adjunctive or symptomatic relief.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial in 72 patients with duodenal or prepyloric ulcers, comparing cimetidine, an antacid suspension plus hyoscyamine, and placebo. Cimetidine healed 67% at 3 weeks (p<0.005 vs placebo). The antacid arm was a combination regimen, and its result is cut off in the abstract available. |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review | Clin Gastroenterol | Review of antacids and anticholinergics in duodenal ulcer treatment |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Des | Cellular and molecular mechanisms of gastroprotective and ulcer-healing actions of antacids beyond prostaglandins |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschr Med | Antacid usefulness rests on neutralizing gastric acid and inhibiting pepsin. Neutralizing capacity varies with chemical composition. |
| [1769429](https://pubmed.ncbi.nlm.nih.gov/1769429/) | 1991 | Mechanistic/Clinical pharmacology | Digestion | Compared protective effects of Maalox 70 and Al(OH)3 against experimentally induced gastric mucosal lesions, and examined the role of intragastric pH |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Rat study | Dig Dis Sci | Al(OH)3 and Maalox 70 enhanced ulcer healing, with prostaglandins and epidermal growth factor implicated |
| [2340961](https://pubmed.ncbi.nlm.nih.gov/2340961/) | 1990 | Rat study | Digestion | Acidified aluminum complex was 8.2 times more potent than its parent antacid in protecting against aspirin-induced gastric lesions |
| [9334882](https://pubmed.ncbi.nlm.nih.gov/9334882/) | 1997 | Cell study | Jpn J Pharmacol | Al(OH)3 prevented acid- and pepsin-induced damage to rat gastric epithelial cells |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Clinical pharmacology (not formally classified) | J Clin Gastroenterol | Compared postprandial gastric acid buffering by sodium bicarbonate versus aluminum-magnesium hydroxide in duodenal ulcer patients |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | Clinical study (not formally classified) | Aliment Pharmacol Ther | H2-receptor antagonists and antacids had an aggravating effect on *H. pylori* gastritis in duodenal ulcer patients. This is a caution signal. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 623709 | STOMAAX PLUS |
| 815527 | ALMAGEL PLUS SUS |

Dosage form and approved-indication text were not available in the licence records supplied.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and consistent with the literature, and the products are already marketed in Canada. The evidence is historical and mostly non-Phase-labeled. It includes one small RCT of a combination regimen and no registered trials. This looks like an established antacid use, not a novel repurposing opportunity.

**To proceed, the following is needed:**
- Confirmation of the approved indications from the Health Canada package inserts for STOMAAX PLUS and ALMAGEL PLUS SUS. The label data is currently empty, and warnings and contraindications are also missing.
- Mechanism-of-action data from DrugBank.
- Positioning against current standard care (PPIs, H2 blockers, *H. pylori* eradication), and attention to the *H. pylori* gastritis caution signal (PMID 9305482).
- Note that the other three predicted indications are weaker. Gastroduodenitis and gastrojejunal ulcer rest on extrapolated, mostly historical evidence (Research Question). Peptic ulcer perforation has no supporting evidence (Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

