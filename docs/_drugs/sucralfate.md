---
layout: default
title: Sucralfate
parent: High Evidence (L1-L2)
nav_order: 870
evidence_level: L2
indication_count: 2
last_modified_at: 2026-10-13
description: "Sucralfate: predicted new indication Duodenogastric reflux (evidence level L2). Approved use: Duodenal ulcer"
monitor_inn: "SUCRALFATE"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction"]
---

# Sucralfate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

## Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux
{: .text-alpha }

## One-Sentence Summary

Sucralfate is a mucosal protectant originally used to treat duodenal ulcer.
The TxGNN model predicts it may be effective for **duodenogastric reflux** (alkaline/bile reflux gastritis),
with **no registered clinical trials** but **10 publications**, including **2 randomized controlled trials**, supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer (the Canadian licence records contain no approved indication text; this comes from the knowledge-graph indication data) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the known pharmacology of sucralfate, it is a mucosal protectant. In an acidic environment it forms a viscous, adherent barrier over damaged mucosa and binds bile acids and pepsin.

Duodenogastric reflux (alkaline or bile reflux gastritis) involves mucosal injury caused by refluxed bile salts. A drug that coats the mucosa and binds bile acids could plausibly reduce this injury and ease symptoms. This action does not depend on acid suppression, which fits a condition where acid-lowering therapy alone gives limited benefit.

The original indication, duodenal ulcer, also involves mucosal damage, so both conditions share a mucosal-protection rationale. This mechanistic link rests on general knowledge of sucralfate rather than on the supplied mechanism data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Double-blind study in 23 post-gastric-surgery patients with alkaline reflux gastritis symptoms: sucralfate 6 g/day vs placebo for 6 weeks, followed by 6 weeks of open-label sucralfate |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Post-cholecystectomy alkaline reactive gastritis: sucralfate compared with rabeprazole or no treatment for dyspeptic symptoms and endoscopic/histological signs |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Clinical study | Minerva Gastroenterol Dietol | 18 patients with duodenogastric reflux gastritis: cisapride 30 mg/day vs sucralfate 4 g/day for two months |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Cohort | Rev Esp Enferm Apar Dig | 50 cases of gastritis caused by postsurgical biliary reflux treated with sucralfate |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | Review | Scand J Gastroenterol Suppl | Randomized trial of sucralfate vs placebo in symptomatic gastritis, comparing gastroesophageal with duodenogastric reflux |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Committee report | Am J Gastroenterol | Sucralfate's non-ulcer uses (gastritis, esophagitis, stomatitis) are promising but not clearly established |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Duodenogastric reflux-induced esophagitis; proton-pump inhibitors are the best medical treatment, and medical and surgical management can be difficult |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Alkaline reflux gastritis and esophagitis: features and pathophysiology of bile-induced mucosal injury |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Cohort | Eur J Pediatr | Six children and adolescents with primary duodenogastric reflux unresponsive to antacid therapy |
| [2186496](https://pubmed.ncbi.nlm.nih.gov/2186496/) | 1990 | Review | Ter Arkh | 72 patients with erosive and ulcerous gastroduodenal lesions treated with sucralfate (Antepsin), with beneficial effects on pain and healing |

The two RCTs are small and old, and the summaries available here do not report their outcomes, so their results should be checked in the full papers before relying on them.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02125250 | APO-SUCRALFATE - TAB 1G | Not listed | Not listed |
| 02100622 | SULCRATE | Not listed | Not listed |
| 02103567 | SULCRATE SUSPENSION PLUS | Not listed | Not listed |
| 02045702 | TEVA-SUCRALFATE | Not listed | Not listed |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text)**: hyperglycemia, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure.
- **Drug Interactions**: 100 interactions were found. The first 20 returned include:
  - **Major**: dolutegravir, bictegravir
  - **Moderate**: acarbose, doxycycline, tetracycline, albiglutide, alogliptin, pioglitazone, alendronic acid, risedronic acid, ibandronate, allopurinol, ascorbic acid, baloxavir marboxil, calcifediol
  - **Minor**: acebutolol, anagrelide, atenolol, betaxolol, bisoprolol

  Many of these probably involve reduced absorption of the other drug, but the interaction mechanisms are not given in the data.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is plausible, and two small randomized trials plus several clinical studies address sucralfate in alkaline reflux gastritis. However, there are no registered trials, the published studies are old and small, and the safety data are incomplete.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Mechanism of action data from DrugBank
- Review of the full RCT papers for outcomes and quality
- A safety plan for patients with renal impairment or hyperglycemia, and for the flagged drug interactions (e.g. separating dosing from integrase inhibitors, tetracyclines and bisphosphonates)

**Note on the second predicted indication (duodenal obstruction):** This prediction was rated L5 with a **Hold** decision. Duodenal obstruction is usually a mechanical problem, and sucralfate's mucosal protection does not treat it. The high score of 99.30% most likely reflects its closeness to duodenal ulcer in the knowledge graph, not a real therapeutic effect.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

