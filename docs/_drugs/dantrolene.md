---
layout: default
title: Dantrolene
parent: Moderate Evidence (L3-L4)
nav_order: 247
evidence_level: L3
indication_count: 9
last_modified_at: 2026-10-13
description: "Dantrolene: predicted new indication Malignant hyperthermia, susceptibility to (evidence level L3). Approved use: Malignant hyperthermia of anaesthesia"
monitor_inn: "Dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis, susceptibility to", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

# Dantrolene: From Malignant Hyperthermia to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant originally used to treat malignant hyperthermia during anaesthesia and exercise-induced malignant hyperthermia.
The TxGNN model predicts it may be effective for **malignant hyperthermia, susceptibility to**, which is essentially the same condition, so this is an on-label use rather than true repurposing.
Currently there are **no registered clinical trials** and **19 publications** (mostly reviews and guidelines) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant hyperthermia of anaesthesia; exercise-induced malignant hyperthermia |
| Predicted New Indication | Malignant hyperthermia, susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, dantrolene is a skeletal muscle relaxant that acts on the ryanodine receptor (RYR1) calcium release channel of the sarcoplasmic reticulum. One 2017 study (PMID 28373535) indicates that dantrolene needs magnesium ions to arrest a malignant hyperthermia episode.

Malignant hyperthermia is a pharmacogenetic skeletal muscle disorder. In susceptible people, volatile anaesthetics or succinylcholine trigger uncontrolled calcium release and a hypermetabolic crisis. Susceptibility is mainly caused by RYR1 mutations. Dantrolene directly counteracts this calcium dysregulation, so the original indication and the predicted indication are closely linked.

The other predicted conditions follow the same logic. Several are RYR1-related myopathies (King-Denborough syndrome, central core disease, multiminicore disease, centronuclear myopathy), where dantrolene's relevance lies mainly in managing malignant hyperthermia risk. There is no evidence that it treats the underlying myopathy. The periodic paralysis predictions (hypokalaemic and thyrotoxic) are speculative and have no supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table lists the most relevant publications for the top prediction. Guidelines are listed first, followed by reviews and mechanism studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists guideline (2020) on malignant hyperthermia; genetically susceptible people are at risk on exposure to potent inhalational anaesthetics or suxamethonium |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Consensus guideline | Br J Anaesth | European Malignant Hyperthermia Group guidance on perioperative management of suspected or susceptible patients; notes no interventional trial evidence exists |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | Describes malignant hyperthermia as a pharmacogenetic skeletal muscle disorder; incidence 1:10,000 to 1:250,000 anaesthetics |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative expert review of epidemiology and management in critically ill patients |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | Update on a rare, potentially lethal calcium release channel disorder; mortality has improved |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Review | Korean J Anesthesiol | Autosomal dominant inheritance with variable expression and incomplete penetrance |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanism study | PNAS | Dantrolene requires Mg2+ to arrest malignant hyperthermia |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | Dantrolene sodium is described as the definitive treatment |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet J Rare Dis | Earlier overview of the pharmacogenetic disorder and its triggers |
| [25989378](https://pubmed.ncbi.nlm.nih.gov/25989378/) | 2015 | Review | Acta Anaesthesiol Scand | Scandinavian update; RYR1 mutations account for most cases |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01997572 | DANTRIUM INTRAVENOUS | Not listed | Not listed |
| 02529998 | DANTROLENE SODIUM FOR INJECTION, USP | Not listed | Not listed |
| 01997602 | DANTRIUM CAPSULES | Not listed | Not listed |

---

## Safety Considerations

- **Disease-level cautions (from the TxGNN knowledge graph, not label text)**: liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, and lung disease are flagged as contraindication-related conditions. These should be verified against the Canadian product monograph.
- **Drug Interactions**: 72 interactions were identified. Main ones:
  - **Major**: morphine, liposomal morphine
  - **Moderate**: dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol, promethazine
  - Several other interactions (for example pantoprazole, metformin, omeprazole, simvastatin, clopidogrel) are of unknown severity.

Official warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dantrolene is the established, marketed treatment for malignant hyperthermia, supported by guidelines and reviews and decades of clinical use. The evidence level is capped at L3 because no Phase 3 RCT is registered (ethical limits make such trials impractical). The other predicted conditions (multiminicore disease, periodic paralyses) have no or only indirect evidence and should be held. King-Denborough syndrome, central core disease and centronuclear myopathy are research questions at most, since benefit is limited to managing malignant hyperthermia risk.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form details for the three Canadian authorisations
- Detailed mechanism of action data (for example from DrugBank)
- Review of the major morphine interaction and the knowledge-graph contraindications (liver disease, muscle and lung disease) in the intended patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

