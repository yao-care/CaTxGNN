---
layout: default
title: Pantoprazole
parent: Model Prediction Only (L5)
nav_order: 698
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Pantoprazole: From Acid-Related Disorders (Label Not Recorded) to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI) that suppresses gastric acid secretion, and it is marketed in Canada under 20 licences. The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **3 clinical trials** and **19 publications** linked to this prediction. This is probably an established use rather than true repurposing, so the Canadian label should be checked first.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian licence data |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note: only one registered trial (NCT02084420, Phase 3, completed) meets the Phase 3 criterion, which gives L2 under the level rules. The upstream scoring lists L1, based on several published RCTs whose trial phase is not stated.*

---

## Why is This Prediction Reasonable?

Pantoprazole binds irreversibly and specifically to the gastric proton pump (H+/K+ ATPase), the final step of acid secretion. This lowers intragastric acidity, which allows ulcers to heal. In bleeding ulcers it also helps stabilise the clot. The drug has a relatively long duration of action and is less readily activated in mildly acidic body compartments.

Peptic ulcers are acid-driven, so acid suppression is a direct and plausible treatment. Pantoprazole is also used in *H. pylori* eradication regimens, where it is combined with antibiotics. The input has no recorded original indications or mechanism data, so this prediction is most likely a labelled or well-established use. Confirm the label status before treating it as a repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Randomised, double-blind comparison of ilaprazole vs pantoprazole triple therapy for 7 days, measuring *H. pylori* eradication in gastric and/or duodenal ulcer patients |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Effect of PPIs and statins on clopidogrel antiplatelet response after coronary stenting. This is an interaction study, not ulcer treatment |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Risk factors for choosing second-look endoscopy in bleeding peptic ulcers after endoscopic haemostasis and high-dose PPI infusion. It does not test pantoprazole efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Intermittent vs continuous pantoprazole infusion for rebleeding after endoscopic therapy in peptic ulcer bleeding |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Pantoprazole infusion as an add-on to endoscopic treatment in ulcer bleeding, to reduce rebleeding (about 20% after successful therapy) |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole and amoxycillin with azithromycin or clarithromycin for *H. pylori* eradication in duodenal ulcer |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Three pantoprazole-based triple therapies for *H. pylori* eradication and gastric ulcer healing |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | Amoxycillin and clarithromycin with either sucralfate or pantoprazole for *H. pylori* eradication in duodenal ulcer |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative study | Hepato-gastroenterology | Lansoprazole vs pantoprazole in active duodenal ulcer treatment and *H. pylori* eradication |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Clinical study | Med Arch | PPI efficacy after endoscopic haemostasis in bleeding ulcer, and the role of *H. pylori*. The authors note that controlled pantoprazole data are few |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | P-CAB vs PPI for healing grade C/D esophagitis. This is related acid-disease evidence rather than ulcer-specific |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pharmacology overview of pantoprazole as a PPI, including its long duration of action and a lack of identified drug interactions in numerous studies |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (rat) | Inflammopharmacology | Pantoprazole combined with mesenchymal stem cells in experimental gastric ulcer, examining oxidative stress, inflammation and apoptosis pathways |

---

## Canada Market Information

Twenty licences are on record. Five are shown below. Dosage form and approved indication text are not recorded for them.

| DIN | Product Name |
|---------|------|
| 02481588 | AG-PANTOPRAZOLE SODIUM |
| 02292920 | APO-PANTOPRAZOLE |
| 02357054 | JAMP-PANTOPRAZOLE |
| 02305046 | SPC-PANTOPRAZOLE |
| 02285487 | TEVA-PANTOPRAZOLE |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the Evidence Pack. The literature includes a pharmacodynamic study of PPIs with clopidogrel (NCT00930670), so interaction screening is worthwhile in patients on dual antiplatelet therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Peptic ulcer healing, ulcer rebleeding and *H. pylori* eradication regimens all have published RCTs involving pantoprazole, and the mechanism is direct. The registry evidence is thinner, with only one completed Phase 3 trial. The main uncertainty is whether this is already a labelled use, which would make it an established indication rather than a repurposing candidate.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indications) to confirm whether peptic ulcer is already labelled
- Mechanism of action data from DrugBank
- Confirmation of the arms and endpoints of NCT02084420, and of which PPI was used in the registered ulcer-bleeding trials
- Dosage form and route information for the Canadian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

