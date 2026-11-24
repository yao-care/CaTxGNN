---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Gout"
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria
{: .text-alpha }

## One-Sentence Summary

Colchicine is an anti-inflammatory drug originally used to treat gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but this is a computational prediction with **0 clinical trials** and only **2 laboratory-level publications** behind it, so evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (the Canadian licence records contain no indication text) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 5; dormant: 1) |
| Number of DINs | 5 (marketed: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for colchicine: "Colchicine’s effectiveness as a treatment for gout has been postulated to be due to its ability to block neutrophil-mediated inflammatory responses induced by monosodium urate crystals in synovial fluid. Colchicine disrupts the polymerization of β-tubulin into microtubules, thereby preventing the activation, degranulation, and migration of neutrophils to sites of inflammation." ([DailyMed: Mitigare (colchicine) prescribing information, Hikma Specialty USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb5f9d85-6b81-49f8-bcd6-17b7bfbc10f2), label version 2026-10-16; accessed 2026-11-19.) Based on well-known pharmacology, colchicine binds tubulin and disrupts microtubule polymerization. *Plasmodium falciparum* relies on microtubules for spindle formation and parasite development, so a tubulin-targeting mechanism is biologically plausible.

The link to the original indications is weak. Gout and FMF are inflammatory conditions treated through colchicine's effect on neutrophil activity, whereas malaria is a parasitic infection. The prediction therefore rests on a shared target (microtubules) rather than a shared disease process.

The supporting literature does not test colchicine as an antimalarial in people. One paper studies curcumin and microtubule disruption in *P. falciparum*. The other studies *pfmdr1* expression in mammalian cells and chloroquine susceptibility, which concerns drug transport. Colchicine's narrow therapeutic index and known human toxicity are significant barriers to any antimalarial use. The high score should be read as a model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Preclinical (in vitro) | PLoS One | Curcumin, not colchicine, disrupts microtubules in *P. falciparum*; supports microtubules as a parasite target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Preclinical (cell-based) | Mol Cell Biol | Expressing the parasite *pfmdr1* gene in mammalian cells increased chloroquine susceptibility; relates to drug transport, not colchicine efficacy |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00572349 | COLCHICINE TAB 0.6MG | COLCHICINE | Marketed |
| 02373823 | JAMP-COLCHICINE | COLCHICINE | Marketed |
| 02402181 | PMS-COLCHICINE | COLCHICINE | Marketed |
| 02519380 | MYINFLA | COLCHICINE | Marketed |
| 02456559 | EURO-COLCHICINE | COLCHICINE | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

Safety information comes from the drug-disease contraindication links in the knowledge graph, not from the package insert. It should be confirmed against the Health Canada label.

- **Contraindication signals (knowledge graph):**
  - Liver failure and impaired renal function
  - Blood disorders: hematologic disease, thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including congenital and idiopathic forms), aplastic anemia
  - Muscle disorders: myopathy, rhabdomyolysis, familial periodic paralysis
  - Gastrointestinal disorders: peptic ulcer disease, diarrheal disease
  - Acute urate nephropathy
- **Drug Interactions** (100 recorded; examples below):
  - Major: clarithromycin, cobicistat, aprepitant, rolapitant, eliglustat, deferiprone, rosuvastatin, simvastatin
  - Moderate: chloroquine, cimetidine, metronidazole, tinidazole, miconazole, ticagrelor, deferasirox, disulfiram

Chloroquine is a moderate interaction, which matters if colchicine were ever considered alongside standard antimalarial therapy.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial support, and the only two papers are in vitro or cell-based studies that do not test colchicine against malaria. Colchicine's toxicity and narrow therapeutic index add a major safety barrier. Better-tolerated, established antimalarials already exist.

**To proceed, the following is needed:**
- In vitro testing of colchicine against *P. falciparum* (including chloroquine-resistant strains), with a selectivity index compared with human cell toxicity
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications
- A safety and drug-interaction assessment covering the antimalarial drugs that would be co-administered

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Mitigare (colchicine) prescribing information, Hikma Specialty USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb5f9d85-6b81-49f8-bcd6-17b7bfbc10f2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

