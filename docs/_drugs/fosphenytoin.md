---
layout: default
title: Fosphenytoin
parent: Model Prediction Only (L5)
nav_order: 415
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Fosphenytoin: predicted new indication Conjunctivitis (evidence level L5). Approved use: Epilepsy, status epilepticus"
---

# Fosphenytoin
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

# Fosphenytoin: From Epilepsy and Status Epilepticus to Conjunctivitis

## One-Sentence Summary

Fosphenytoin is an intravenous prodrug of phenytoin, originally used to treat epilepsy and status epilepticus.
The TxGNN model predicts it may be effective for **conjunctivitis**, but this is a knowledge-graph prediction only, with **0 clinical trials** and **0 publications** supporting it.
Among the other predicted indications, only manic bipolar affective disorder has any published evidence (1 small publication).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, status epilepticus (the Canadian licence record has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fosphenytoin is a prodrug of phenytoin, a voltage-gated sodium channel blocker, and its efficacy in seizure control is established.

For conjunctivitis, there is no clear mechanistic link. Conjunctivitis is typically infectious or allergic/inflammatory, and sodium channel blockade has no established role in it. The high score (0.994) reflects a pattern in the knowledge graph rather than biological or clinical evidence. Phenytoin is also associated with hypersensitivity reactions, which could plausibly worsen ocular inflammatory conditions.

**Other predicted indications (for reference):**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Nephrogenic syndrome of inappropriate antidiuresis | 99.28% | L5 | No action on the V2 receptor pathway; phenytoin can cause SIADH-like hyponatremia, which argues against benefit |
| Tourette syndrome | 99.22% | L5 | No established rationale; IV dosing and cardiac monitoring are impractical for a chronic tic disorder |
| Manic bipolar affective disorder | 99.18% | L4 | Plausible class-level rationale, since other anticonvulsants are mood stabilizers; one small publication; research question |
| Myositis fibrosa | 99.02% | L5 | No identified mechanistic link |
| Idiopathic granulomatous myositis | 99.02% | L5 | No immunomodulatory role; same score as myositis fibrosa suggests a shared graph signal |
| Fibromyalgia | 99.02% | L5 | Loose class-level rationale only; IV dosing is a poor fit for chronic pain |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for conjunctivitis (nor for any of the other predicted indications).

---

## Literature Evidence

Currently no related literature available for conjunctivitis.

For reference, the only publication retrieved across all predicted indications relates to manic bipolar affective disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/) | 2003 | Small pilot study / case report (to be verified from full text) | The Journal of Clinical Psychiatry | Tested the hypothesis that high-dose intravenous fosphenytoin might be acutely antimanic, using a prodrug with fewer cardiac and local vein side effects than phenytoin |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230988 | CEREBYX | Not listed | Not listed |

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease contraindication edges, not label text):

- **Cardiac and conduction:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, Adams-Stokes syndrome, hypotensive disorder
- **Haematological:** thrombocytopenia, leukopenia, pancytopenia, agranulocytosis, neutropenia (including congenital and cyclic forms), lymphatic system disease
- **Organ function:** kidney disease, liver disease, gallbladder disease, pyoureter
- **Other:** systemic lupus erythematosus (including paediatric), substance abuse/dependence, hyperphosphatemia

**Drug Interactions:** The interaction screen returned 100 interactions. Examples:
- **Major:** cimetidine, eliglustat
- **Moderate:** acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, betamethasone, clarithromycin, aprepitant, canagliflozin, dulaglutide, and others
- **Minor:** acetylsalicylic acid

Package insert warnings and contraindications from Health Canada were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The conjunctivitis prediction rests on the model score alone. There are no trials or publications, no plausible mechanism, and a possible hypersensitivity concern. The same applies to most of the other predicted indications. Manic bipolar affective disorder is the only one with a plausible rationale and a (small, preliminary) publication, and it could be considered a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Full-text review of PMID 12716241 to confirm study design and results if the mania direction is pursued
- Route compatibility assessment, since fosphenytoin is given intravenously and chronic or ocular conditions may need other routes
- Any preclinical or clinical evidence supporting a role in conjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

