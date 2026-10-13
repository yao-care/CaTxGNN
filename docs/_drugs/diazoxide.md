---
layout: default
title: Diazoxide
parent: Model Prediction Only (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Diazoxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Alopecia

## One-Sentence Summary

Diazoxide is a potassium channel opener, originally used to treat hyperinsulinemic hypoglycemia, including insulinoma and congenital hyperinsulinism.
The TxGNN model predicts it may be effective for **alopecia** (the top-ranked prediction is hypotrichosis simplex of the scalp), but there are currently **no registered clinical trials** and only **6 publications** for alopecia, most of them reviews, case reports, or animal studies.
Evidence is therefore limited to preclinical and mechanistic support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperinsulinemic hypoglycemia (including pancreatic insulinoma and congenital hyperinsulinism) |
| Predicted New Indication | Hypotrichosis simplex of the scalp (rank 1); alopecia (rank 4) has the most relevant supporting literature |
| TxGNN Prediction Score | 99.96% (hypotrichosis simplex of the scalp); 99.91% (alopecia) |
| Evidence Level | L5 (hypotrichosis simplex of the scalp); L4 (alopecia) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, diazoxide opens ATP-sensitive potassium (KATP) channels. In the pancreas, this suppresses insulin release, which explains its use in hyperinsulinemic hypoglycemia. The same channel-opening action is the proposed reason for its well-known side effect of excess hair growth (hypertrichosis).

This is the basis for the hair-related predictions. Minoxidil, a related vasodilator that also acts through KATP channels, is established as a hair-growth treatment. Topical diazoxide produced hair regrowth in the bald scalps of macaques, an animal model of androgenetic alopecia. The link is therefore plausible for hair-loss conditions in which stimulating follicle growth could help.

The link is much weaker for other predicted conditions:
- **Hypotrichosis simplex and congenital hypotrichosis milia:** These are genetic conditions, so stimulating growth may not address the underlying defect, and no supporting data exist.
- **Diffuse alopecia areata:** This is autoimmune, and KATP-driven growth does not address the immune cause.
- **Hypertrichosis and Ambras type hypertrichosis:** These involve excess hair. Diazoxide causes hypertrichosis, so these predictions likely reflect a drug side-effect association in the knowledge graph rather than a therapeutic relationship. They should not be pursued.
- **Autosomal dominant hyperinsulinism due to Kir6.2 deficiency:** This is close to the existing approved use, so it is closer to an on-label use than true repurposing. Efficacy depends on the variant, since dominant KCNJ11 variants are often unresponsive to diazoxide.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature for **alopecia** (rank 4):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Animal study (primate) | J Dermatol Sci | Topical diazoxide applied to the bald frontal scalp of stumptailed macaques, taking advantage of its hypertrichotic effect; systemic side effects were also monitored |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Review | J Invest Dermatol | Topical minoxidil and diazoxide induced significant hair regrowth in bald macaque scalps (androgenetic alopecia model) |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Review | Drug Saf | Review of drug-induced hair loss and hair growth, including incidence, management and avoidance |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Case report | Pediatr Dermatol | Child with generalized hypertrichosis from topical minoxidil exposure; diazoxide listed among causative drugs (indirect evidence) |
| [20682429](https://pubmed.ncbi.nlm.nih.gov/20682429/) | 2010 | Review | Vet Clin North Am Exot Anim Pract | Medical management of insulinomas in ferrets, including diazoxide (not related to alopecia) |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Case series | Arch Dis Child | Fetal exposure to diazoxide in four infants (not related to alopecia) |

Literature for **hypertrichosis** (rank 7) mainly documents hypertrichosis as an adverse effect of diazoxide, for example a neonatal case ([36726424](https://pubmed.ncbi.nlm.nih.gov/36726424/), 2023), a Japanese post-marketing survey of 384 children in which hypertrichosis was the most common adverse reaction at 8.6% ([30083030](https://pubmed.ncbi.nlm.nih.gov/30083030/), 2018), and real-world congenital hyperinsulinism data ([40917359](https://pubmed.ncbi.nlm.nih.gov/40917359/), 2025). These papers do not support a therapeutic use.

No literature was available for the other predicted conditions.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00503347 | PROGLYCEM | Not specified | Not specified |

## Safety Considerations

**Contraindication-related diseases (from the knowledge graph, not label text):** Diazoxide is flagged as contraindicated or to be used with caution in conditions including:
- Metabolic: diabetes mellitus, hyperglycemia, diabetic ketoacidosis, gout, hyperuricemia, potassium deficiency
- Cardiovascular: congestive heart failure, coronary artery disease, cerebrovascular disorder, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- Renal and hepatic: kidney disease, kidney failure, uremia, liver disease, gallbladder disease, pyoureter

**Drug Interactions:** 100 interactions were identified. The 20 listed are all moderate severity, mainly with other blood-sugar-lowering drugs and corticosteroids:
- Antidiabetic agents: acarbose, alogliptin, albiglutide, dulaglutide, metformin, pioglitazone, chlorpropamide, acetohexamide, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
- Others: bupropion, morphine, dronabinol

**Adverse effects reported in the literature:** Hypertrichosis, fluid retention, cardiac failure, hyperglycemia, acute renal failure, and necrotizing enterocolitis in neonates. Systemic use carries substantial risk, so any hair-loss development would likely need a topical route.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predictions rest on model scores alone, with no clinical trials. For alopecia, the only support is animal data and mechanistic similarity to minoxidil. Several predictions (hypertrichosis, Ambras type hypertrichosis) reflect a side-effect association rather than a therapeutic one. Alopecia may be treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from Health Canada, which are needed before safety screening
- Human data on topical diazoxide for androgenetic alopecia, including dose, formulation, and local and systemic safety
- Assessment of a topical formulation, since systemic diazoxide has significant adverse effects
- Confirmation of the approved indication and dosage form for the Canadian product (PROGLYCEM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

