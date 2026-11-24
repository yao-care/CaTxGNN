---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Acetic Acid: predicted new indication Post-bacterial disorder (evidence level L5). Approved use: Otitis externa"
monitor_inn: "ACETIC ACID"
predicted_indications: ["post-bacterial disorder", "postinfectious vasculitis", "post-infectious syndrome", "Chagas cardiomyopathy", "infective urethral stricture", "infection-related hemolytic uremic syndrome", "drug-induced osteoporosis", "pityriasis simplex", "tinea corporis"]
---

# Acetic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Acetic Acid: From Otitis Externa to Post-Bacterial Disorder
{: .text-alpha }

## One-Sentence Summary

Acetic acid is a topical acidifying antiseptic, originally used for otitis externa and external ear disease.
The TxGNN model predicts it may be effective for **post-bacterial disorder**, but **no clinical trials and no publications** currently support this prediction.
The top-ranked predictions are computational only. The most biologically plausible lead among the candidates is **tinea corporis** (rank 9), which has indirect, mostly historical literature support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Otitis externa; external ear disease (the Canadian licence records list no indication text) |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for acetic acid: "Acetic acid is antibacterial and antifungal; propylene glycol is hydrophilic and provides a low surface tension; benzethonium chloride is a surface active agent that promotes contact of the solution with tissues." ([DailyMed: acetic acid prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c1c28375-9b03-4590-9d39-ab28403da93d), label version 2026-03-18; accessed 2026-11-19.) Based on known information, acetic acid is a topical antiseptic and acidifier with antibacterial activity. Its use in otitis externa is consistent with lowering local pH and inhibiting microbial growth.

For the top prediction, post-bacterial disorder, no plausible mechanism is apparent. Post-infectious conditions are typically immune-mediated rather than ongoing infections, so a topical antiseptic is unlikely to address them. The same holds for the other high-scoring predictions: postinfectious vasculitis, post-infectious syndrome, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome and drug-induced osteoporosis. All have TxGNN scores of 0.9967 or higher, but the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Two lower-ranked candidates have a loose mechanistic rationale:
- **Infective urethral stricture (rank 5):** dilute acetic acid is used as an irrigant in other settings, but the condition is fibrotic and structural, and no data support benefit.
- **Tinea corporis (rank 9, score 0.9925):** acidification of the skin and disruption of fungal cell membranes could plausibly give antifungal activity. Historical reports describe dilute acetic acid for related dermatophyte infections (see below). This is the only candidate with an evidence level above L5 (L4), and it is best viewed as a research question rather than a validated indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top prediction (post-bacterial disorder), nor for tinea corporis or any other predicted indication.

---

## Literature Evidence

No literature is available for the top prediction, post-bacterial disorder. The only publications retrieved for the top predictions relate to rank 3 (post-infectious syndrome) and rank 9 (tinea corporis). The most relevant are shown below.

**Tinea corporis (rank 9)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Historical case series | The Urologic and Cutaneous Review | Larger series of tinea capitis patients treated with special iodine and dilute acetic acid; no abstract available |
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Historical clinical report | JAMA | Tinea capitis treated with special iodine and dilute acetic acid; no abstract available |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Historical clinical report | Archives of Dermatology and Syphilology | Same approach in tinea capitis; no abstract available |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Historical clinical report | Vestnik Dermatologii i Venerologii | Foot epidermophytosis treated with increasing concentrations of acetic acid; no abstract available |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Clinical report | Skin Appendage Disorders | Chemical peeling as an alternative to oral antifungals for onychomycosis in elderly and diabetic patients |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | In vitro study | Mycoses | Topical antifungal products compared in an in vitro onychomycosis model against *Trichophyton mentagrophytes* |
| [16233325](https://pubmed.ncbi.nlm.nih.gov/16233325/) | 2002 | In vitro study (indirect) | J Biosci Bioeng | Fermented herb product inhibited dermatophytes under low-pH conditions; organic acids implicated |
| [33625606](https://pubmed.ncbi.nlm.nih.gov/33625606/) | 2021 | In vitro study (indirect) | World J Microbiol Biotechnol | Lactic acid bacteria strain inhibited *Trichophyton rubrum* growth |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Case series (safety) | Archives of Plastic Surgery | Burns caused by Korean folk remedies, a warning about uncontrolled acid use |

**Post-infectious syndrome (rank 3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20848144](https://pubmed.ncbi.nlm.nih.gov/20848144/) | 2011 | Systematic review | J Gastroenterol | Reviews animal models of post-infectious IBS. It does not test acetic acid as a treatment, so it is not efficacy evidence |

These studies are old, uncontrolled, in vitro, or indirect. None directly tests acetic acid in tinea corporis.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02158159 | ACID CONCENTRATE D12264 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02217244 | ACID CONCENTRATE D12236 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02217619 | ACID CONCENTRATE D12294 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02254085 | ACID CONCENTRATE A1230 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02327333 | NATURALYTE H-332 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02327406 | NATURALYTE H-226 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02327538 | NATURALYTE H-408 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02329980 | NATURALYTE H-208 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02330172 | NATURALYTE H-200 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02414813 | SELECTBAG ONE (AX 125 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02414821 | SELECTBAG ONE (AX 150 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02414856 | SELECTBAG ONE (AX 225 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02414902 | SELECTBAG ONE (AX 325 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02415461 | SELECTBAG ONE (AX 250 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02415488 | SELECTBAG ONE (AX 450 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02415496 | SELECTBAG ONE (AX 2525 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02415526 | SELECTBAG ONE (AX 350 G) | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE | Marketed |
| 02533812 | ACID CONCENTRATE A1245 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02533820 | ACID CONCENTRATE A1246 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |
| 02533863 | ACID CONCENTRATE A1265 | ACETIC ACID; CALCIUM CHLORIDE; DEXTROSE; MAGNESIUM CHLORIDE; POTASSIUM CHLORIDE; SODIUM CHLORIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

The DINs in the data are combination products. The product names (acid concentrates and dialysis-related bags) suggest that the Canadian licences are mainly dialysis concentrates rather than ear preparations, so the licensed products may not match the original ear indication or a topical route.

<!-- review:begin ca-lic-20261124b-acetic_acid-1 -->

> **Review correction (2026-11-24)**: Originally stated: "There are 20 valid single-ingredient licences in total." Corrected: in the Health Canada DPD data, the DINs for this drug on this page are combination products (or include combination products), so describing them as single-ingredient products did not match. The Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-acetic_acid-1 -->

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** inherited porphyria, porphyrin metabolism disease, porphyria, herpes simplex infection, geniculate herpes zoster.
- **Tolerability signal:** a 2023 case series reported burns from folk remedies, so uncontrolled use of acids on skin carries a risk of chemical injury.
- **Systemic exposure:** systemic acid exposure is a safety concern for the systemic or deep-tissue conditions among the predictions (e.g. Chagas cardiomyopathy, hemolytic uremic syndrome).

No drug-interaction records were found. Please refer to the package insert for label warnings and contraindications, which are not yet available for review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions have high model scores but no trials, no publications, and no plausible mechanism, so they rest on computation alone (L5). Tinea corporis is the only candidate with indirect support (L4), but that support comes from historical, uncontrolled or in vitro studies. Label safety data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Mechanism of action data for acetic acid
- Confirmation of which licensed Canadian products are relevant, and their routes and dosage forms
- For tinea corporis: in vitro susceptibility testing against dermatophytes, then a modern controlled trial with defined concentrations and skin-tolerability monitoring
- Deprioritising the immune-mediated and systemic predictions unless a mechanistic rationale emerges

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acetic acid prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c1c28375-9b03-4590-9d39-ab28403da93d) |
| 2026-11-24 | Reworded: "There are 20 valid single-ingredient licences in total." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

