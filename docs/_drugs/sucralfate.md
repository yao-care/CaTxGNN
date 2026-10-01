---
layout: default
title: Sucralfate
parent: Moderate Evidence (L3-L4)
nav_order: 863
evidence_level: L3
indication_count: 2
---

# Sucralfate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **2** 
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

# Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux

## One-Sentence Summary

Sucralfate is a mucosal-protective drug marketed in Canada, and its established use is in ulcer disease.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, the backflow of alkaline duodenal contents (including bile) into the stomach.
Currently, **0 registered clinical trials** and **12 publications** relate to this direction. Two of the publications are randomized studies, and both are small and old.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer (taken from the literature context; the Canadian licence records supplied do not state an indication) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Based on general knowledge of the drug, sucralfate forms a viscous protective barrier over damaged gastric and oesophageal mucosa. It also binds bile acids and pepsin in an acidic environment.

Duodenogastric reflux injures the stomach lining because alkaline duodenal contents, including bile, wash back into the stomach. A drug that coats the mucosa and binds bile acids is therefore a plausible fit. The link between ulcer disease and reflux gastritis is a shared pattern of mucosal injury.

The mechanism above rests on general pharmacology rather than the supplied record, and the TxGNN score is a model prediction only. The literature adds direct clinical signals. These are a randomized double-blind study in alkaline reflux gastritis (PMID 3839973) and a sucralfate/cisapride study in duodenogastric reflux gastritis (PMID 1391144). Their size, effect size and design details could not be confirmed from the abstracts supplied.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Randomized, double-blind study in 23 patients with alkaline reflux gastritis after gastric surgery. Sucralfate 6 g/day (n=11) was compared with placebo (n=12) for 6 weeks, followed by 6 weeks of open sucralfate. Outcomes were symptoms, endoscopy and histology. |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | Randomized trial (per title) | Eur J Gastroenterol Hepatol | Compared sucralfate with rabeprazole or no treatment for post-cholecystectomy alkaline reactive gastritis. Outcomes were dyspeptic symptoms and endoscopic/histological signs. |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | Review / report of a trial | Scand J Gastroenterol Suppl | Half-year prospective randomized comparison of sucralfate with placebo in symptomatic gastritis. It also compares gastroesophageal reflux with duodenogastric reflux. |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Clinical study | Minerva Gastroenterol Dietol | 18 patients with duodenogastric reflux gastritis: cisapride 30 mg/day (n=9) vs sucralfate 4 g/day (n=9) for two months. |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Case series (per title) | Rev Esp Enferm Apar Dig | Evaluation of 50 cases of post-surgical biliary reflux gastritis treated with sucralfate. |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Committee statement | Am J Gastroenterol | Notes that sucralfate's role in gastritis, oesophagitis and stomatitis is promising but not clearly established. |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Duodenogastric reflux-induced (alkaline) oesophagitis. Proton-pump inhibitors are described as the best medical treatment, and medical and surgical management can be difficult. |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | J Chir (Paris) | Pathophysiology, diagnosis (24-hour bile monitoring) and management of duodenogastric and gastroesophageal bile reflux. |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Alkaline reflux (bile) gastritis and oesophagitis: causes, diagnostic features and pathophysiology. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | Six children and adolescents with primary duodenogastric reflux. It characterizes the disease, and no sucralfate evidence was confirmed. |

---

## Canada Market Information

Sucralfate has 4 Canadian authorizations. Dosage form and approved-indication text are not available in the supplied record.

| DIN | Product Name |
|---------|------|
| 02125250 | APO-SUCRALFATE - TAB 1G |
| 02100622 | SULCRATE |
| 02103567 | SULCRATE SUSPENSION PLUS |
| 02045702 | TEVA-SUCRALFATE |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for sucralfate in the supplied data. This is more likely a data gap than a true absence of interactions.

Points to check in the target population (from general knowledge of sucralfate, not the supplied record):
- Aluminum accumulation in patients with renal impairment
- Bezoar formation
- Binding of co-administered drugs, which can reduce their absorption

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and two small randomized studies point in the right direction. However, no registered trials exist, the studies are decades old, their results could not be verified, and Canadian safety information is still missing. Under the evidence rules this stays at L3 (research question stage).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Full-text review of PMID 3839973 and PMID 12923369 (sample size, outcomes, effect size). A confirmed well-designed RCT could justify raising the evidence level.
- Mechanism of action data from DrugBank
- A safety plan covering renal impairment and drug-binding interactions

**Note on the second prediction:** the second-ranked prediction, *duodenal obstruction*, is assessed as **Hold** (L4). It has no credible mechanistic rationale, and its high score likely reflects proximity to duodenal ulcer in the knowledge graph. Sucralfate bezoar formation could also worsen or mimic obstruction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

