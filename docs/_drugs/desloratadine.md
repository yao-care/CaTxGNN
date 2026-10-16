---
layout: default
title: Desloratadine
parent: Model Prediction Only (L5)
nav_order: 262
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Desloratadine: predicted new indication Cold urticaria (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis…"
---

# Desloratadine
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

# Desloratadine: From Allergic Rhinitis and Urticaria to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation antihistamine, originally used for allergic and vasomotor rhinitis, allergic conjunctivitis and idiopathic or allergic urticaria.
The TxGNN model predicts it may be effective for **cold urticaria**,
with **2 completed clinical trials** and **6 publications** (3 of them randomized controlled trials) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, idiopathic and allergic urticaria, and related conditions (the Canadian licence records do not contain indication text) |
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (see note in the Clinical Trial Evidence section) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, desloratadine is a selective peripheral H1-receptor inverse agonist.

Cold urticaria is driven by mast cell degranulation and histamine release after cold exposure. Blocking H1 receptors therefore targets the effector pathway directly. This is the same mechanism that underlies desloratadine's existing indications of idiopathic and allergic urticaria, so cold urticaria is a close neighbour of the approved uses.

Published studies also suggest that higher doses (up to 20 mg, four times the labeled dose) improve cold provocation thresholds more than the standard dose. This is consistent with current guidance on up-dosing non-sedating antihistamines in patients who respond poorly to the standard dose.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-centre, double-blind, dose-escalating comparison of 5, 10 and 20 mg desloratadine in acquired cold urticaria; aims to find the dose sufficient to inhibit symptoms |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg vs 20 mg desloratadine on experimentally induced cold urticaria lesions |

Both trials directly test the predicted indication, but they are Phase 4 studies with small samples. They do not strictly meet the Phase 3 criterion for the L1 level; the L1 grade rests mainly on the randomized controlled publications below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomized, placebo-controlled crossover study: high-dose desloratadine reduced wheal volume and improved cold provocation thresholds compared with standard dose in acquired cold urticaria |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized trial of H1-antihistamine dose escalation, using critical temperature threshold measurement in cold urticaria |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | Desloratadine 5 mg for 4 days, tested with ice cubes before and after treatment in 12 patients with cold urticaria; cold urticaria was inhibited |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of the causes, management and treatment options for chronic urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of ebastine (a different antihistamine) in allergic rhinitis and chronic idiopathic urticaria; indirect support only |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria after black ant bite anaphylaxis; background on the condition only, not on desloratadine |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02546019 | DESLORATADINE | Not listed | Not listed |
| 02243919 | AERIUS | Not listed | Not listed |
| 02298155 | DESLORATADINE ALLERGY CONTROL | Not listed | Not listed |
| 02247193 | AERIUS KIDS | Not listed | Not listed |
| 02309300 | AERIUS SINUS + ALLERGY | Not listed | Not listed |

## Safety Considerations

Warnings and contraindications from the Canadian package insert were not available in the compiled data. Please refer to the package insert for safety information.

- **Disease associations flagged in the knowledge graph (not label text):** the TxGNN knowledge graph links desloratadine to caution in hypertension, kidney disease, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (including Graves disease). These should be verified against the official label.
- **Drug Interactions:** The interaction screen returned 100 potential interacting drugs, but none has a severity grade (all are "Unknown"). Examples include calcitriol, phentermine, pantoprazole, doxycycline, morphine, metformin, omeprazole, cimetidine, simvastatin, prednisone and epinephrine. Their clinical significance needs confirmation.
- **Dose caution:** The supporting studies use up to 20 mg, four times the labeled dose. Safety at these doses needs separate review.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cold urticaria is a histamine-driven condition, and several randomized studies, including two completed Phase 4 trials, show benefit from desloratadine, particularly at higher doses. The evidence is promising but comes from small studies, and the Canadian safety label data is still missing.

**To proceed, the following is needed:**
- Obtain and review the Health Canada package insert (warnings, contraindications, dosing), which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A safety assessment of high-dose use (above the labeled 5 mg), including the knowledge-graph-flagged conditions
- Grading of the unrated drug interactions
- Confirmation of the approved indication text and dosage forms for the Canadian licences

### Other Predicted Indications (for reference)

| Predicted Indication | Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Nasal cavity disease | 99.87% | L4 | Hold | Broad term overlapping existing rhinitis indications; only animal studies, no clinical trials |
| Acute laryngopharyngitis | 99.85% | L5 | Hold | Model prediction only; mostly infectious, antihistamines would give symptomatic relief at most |
| Recalcitrant atopic dermatitis | 99.75% | L5 | Hold | Model prediction only; histamine plays a limited role |
| IgE responsiveness, atopic | 99.64% | L5 | Hold | A trait label, not a treatable disease |
| Rosacea conjunctivitis | 99.40% | L5 | Hold | Model prediction only; weak mechanistic fit |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

