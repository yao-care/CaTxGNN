---
layout: default
title: Pantoprazole
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Pantoprazole: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "PANTOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pantoprazole: From Peptic Ulcer Disease to Active Peptic Ulcer Disease
{: .text-alpha }

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease, esophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **1 completed Phase 3 trial** in the top-ranked indication and **18 publications** supporting this direction.
This prediction largely overlaps with the drug's established use, so it is closer to a marketed indication than to true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, Zollinger-Ellison syndrome (approved indication text for the Canadian licences is not available) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 (by the strict rules: 1 completed Phase 3 RCT in this indication). Supporting trials for the closely related duodenal ulcer prediction would qualify as L1. |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, however, pantoprazole irreversibly inhibits the gastric H+/K+ ATPase (the proton pump) in parietal cells. This suppresses gastric acid secretion and allows ulcers to heal.

Peptic ulcers are acid-mediated injuries. The predicted indication is therefore essentially the same disease as the drug's original use, and the mechanism applies directly. This is an on-label use rather than a novel repurposing candidate.

Other predictions from the model show a gradient of plausibility:
- **Duodenal ulcer**: well supported, with Phase 3 and head-to-head RCTs against ranitidine and omeprazole.
- **Gastrojejunal (marginal) ulcer and peptic ulcer perforation**: mechanistically plausible, but supported only by indirect evidence. Pantoprazole is an adjunct to repair or other management here.
- **Duodenogastric reflux**: pantoprazole mainly reduces acid reflux and has limited direct effect on bile reflux.
- **Duodenal obstruction**: no clear mechanistic link. The obstruction is usually mechanical, and the high score likely reflects network proximity to peptic ulcer disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind trial of ilaprazole vs pantoprazole triple therapy for 7 days in H. pylori-positive gastric and/or duodenal ulcer patients |

Further trials were retrieved for the closely related duodenal ulcer prediction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00374101](https://clinicaltrials.gov/study/NCT00374101) | Phase 3 | Completed | 450 | High vs standard dose PPI with endoscopic therapy for bleeding peptic ulcers |
| [NCT00843063](https://clinicaltrials.gov/study/NCT00843063) | Phase 4 | Completed | 161 | Famotidine vs pantoprazole to prevent recurrent aspirin-induced ulcers |
| [NCT02467621](https://clinicaltrials.gov/study/NCT02467621) | Phase 4 | Completed | 3350 | SUP-ICU: stress ulcer prophylaxis with pantoprazole in ICU patients |
| [NCT02551744](https://clinicaltrials.gov/study/NCT02551744) | N/A | Completed | 101 | Pantoprazole vs famotidine to prevent recurrent ulcers in thienopyridine users |
| [NCT00261300](https://clinicaltrials.gov/study/NCT00261300) | Phase 3 | Completed | 100 | Long-term pantoprazole in chronic acid peptic complaints |
| [NCT01182597](https://clinicaltrials.gov/study/NCT01182597) | Phase 3 | Unknown | 190 | Oral vs IV PPI in high-risk bleeding peptic ulcers after endoscopic hemostasis |
| [NCT00001191](https://clinicaltrials.gov/study/NCT00001191) | Phase 2 | Completed | Not reported | Oral omeprazole and IV pantoprazole in gastric acid hypersecretion (Zollinger-Ellison syndrome) |
| [NCT00881413](https://clinicaltrials.gov/study/NCT00881413) | Phase 4 | Withdrawn | 0 | Esomeprazole vs pantoprazole for rebleeding prevention; no data |
| [NCT00839488](https://clinicaltrials.gov/study/NCT00839488) | Phase 4 | Terminated | 6 | IV pantoprazole vs famotidine for stress ulcer prophylaxis; too small to be informative |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7569755](https://pubmed.ncbi.nlm.nih.gov/7569755/) | 1995 | RCT | Scand J Gastroenterol | Multicentre study of pantoprazole vs ranitidine in acute duodenal ulcer |
| [7614102](https://pubmed.ncbi.nlm.nih.gov/7614102/) | 1995 | RCT | Eur J Gastroenterol Hepatol | Double-blind comparison of pantoprazole 40 mg and omeprazole 20 mg for acute duodenal ulcer healing |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | P-CAB vs PPI for healing grade C/D esophagitis |
| [8882382](https://pubmed.ncbi.nlm.nih.gov/8882382/) | 1996 | Review | Drugs | Pantoprazole 40 mg was superior to ranitidine and equivalent to omeprazole in short-term treatment of acute peptic ulcer and reflux oesophagitis |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole binds irreversibly to the proton pump, with a long duration of action and few known drug interactions |
| [11402494](https://pubmed.ncbi.nlm.nih.gov/11402494/) | 2001 | Review | Am J Health Syst Pharm | Pharmacology, pharmacokinetics, efficacy and dosing of pantoprazole |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Comparative study | Am J Gastroenterol | Pantoprazole vs ranitidine in duodenal ulcer, multicenter study in Brazil |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut Liver | Tegoprazan (a P-CAB) vs active control for endoscopic resection-induced ulcers |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative study | Hepatogastroenterology | Lansoprazole vs pantoprazole in active duodenal ulcer and H. pylori eradication |
| [23480366](https://pubmed.ncbi.nlm.nih.gov/23480366/) | 2013 | Preclinical (rat) | J Pineal Res | Melatonin vs pantoprazole or ranitidine in a reflux esophagitis model |

## Canada Market Information

Health Canada lists 20 valid single-ingredient pantoprazole authorizations. Dosage form and approved indication text are not available for these records. The first five are shown below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02481588 | AG-PANTOPRAZOLE SODIUM | Not available | Not available |
| 02292920 | APO-PANTOPRAZOLE | Not available | Not available |
| 02357054 | JAMP-PANTOPRAZOLE | Not available | Not available |
| 02305046 | SPC-PANTOPRAZOLE | Not available | Not available |
| 02285487 | TEVA-PANTOPRAZOLE | Not available | Not available |

Injectable products (for example DIN 02458969 and 02306727) are also among the valid authorizations.

## Safety Considerations

- **Contraindications from the knowledge graph (not label text)**: osteoporosis, postmenopausal osteoporosis, bone fracture, pernicious anemia. These reflect known concerns with long-term acid suppression, such as effects on bone health and vitamin B12 absorption.
- **Drug interactions**: 100 interactions were identified. Examples:
  - **Major**: acalabrutinib, atazanavir.
  - **Moderate**: hydrochlorothiazide, alpelisib, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bosutinib, bumetanide.
  - **Minor**: acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin.

  Absorption of acid-dependent drugs such as atazanavir and acalabrutinib may be reduced by acid suppression.

Package insert warnings and contraindications from Health Canada have not been obtained. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pantoprazole is already marketed in Canada with 20 valid authorizations, and its acid-suppressing mechanism directly fits ulcer healing. A completed Phase 3 RCT and head-to-head RCTs in duodenal ulcer support this. The label-level safety information has not yet been reviewed, which is why the decision carries guardrails.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text, dosage forms and routes for the Canadian authorizations
- Detailed mechanism of action data from DrugBank
- A safety plan for long-term use (bone health, vitamin B12 status) and for interacting drugs such as atazanavir and acalabrutinib
- Evidence for the lower-ranked predictions (gastrojejunal ulcer, peptic ulcer perforation, duodenogastric reflux) before pursuing them. Duodenal obstruction should stay on hold, as there is no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

