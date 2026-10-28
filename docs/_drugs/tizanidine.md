---
layout: default
title: Tizanidine
parent: High Evidence (L1-L2)
nav_order: 919
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-28
description: "Tizanidine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the available Canadian licence data"
monitor_inn: "TIZANIDINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "Tourette syndrome", "ulerythema ophryogenesis"]
---

# Tizanidine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **5** 
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

## Tizanidine: From Spasticity Management to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Tizanidine is a centrally acting alpha-2 adrenergic agonist marketed in Canada as a single-ingredient product; the data compiled for this report do not include its approved-indication text.
The TxGNN model predicts it may be effective for **migraine disorder**, with **2 registered clinical trials** (1 directly relevant Phase 3 trial of unknown status) and **16 publications**, including one double-blind placebo-controlled trial in chronic daily headache.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Canadian licence data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L1 (conditional; see note below) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

*Note: The L1 level is the pre-assigned grade for this prediction. Strictly by the stated rules (≥2 completed Phase 3 RCTs), the evidence is weaker: the only Phase 3 trial has UNKNOWN status and no verified results. A conservative reading would sit between L2 and L3.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, tizanidine is a central alpha-2 adrenergic agonist. It reduces the release of excitatory neurotransmitters and is thought to dampen trigeminal nociceptive transmission and central sensitization, which are processes involved in migraine.

Tizanidine is also used for conditions involving muscle tone and spasm. Migraine and chronic daily headache often involve muscle tension and central pain sensitization, so a link between the two is plausible. Published reviews list tizanidine among agents studied for migraine and chronic headache prophylaxis.

Caveats: the older double-blind placebo-controlled study (2002) assessed chronic daily headache (chronic migraine, migrainous headache, or tension-type headache) rather than migraine alone. The Phase 3 migraine trial has no confirmed results.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | Unknown | 189 | Multicenter, randomized, double-blind, placebo-controlled study of oral tizanidine for preventing migraine attacks in adults with episodic migraine (planned completion Dec 2025); no results verified |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Completed | 300 | 24-week observational study of topical NSAIDs for pain relief; only weak indirect relevance to tizanidine and migraine |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | Double-blind, placebo-controlled, multicenter study of tizanidine as adjunctive prophylaxis for chronic daily headache |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | Open-label study | Headache | Dose-titration study of tizanidine tablets for chronic daily headache prophylaxis |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | Clinical study | Headache | Low-dose tizanidine with NSAIDs for detoxification from analgesic rebound headache |
| [20464578](https://pubmed.ncbi.nlm.nih.gov/20464578/) | 2010 | Review | Neurol Sci | Review of double-blind placebo-controlled trials of chronic migraine prophylaxis |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | Muscle-tone agents (baclofen, tizanidine, botulinum toxin A) as preventive treatment for migraine and tension-type headache |
| [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | Consensus guideline | Arq Neuropsiquiatr | Brazilian Headache Society consensus on chronic migraine treatment |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | Emerging migraine prevention options, including tizanidine |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | Prophylactic treatment of chronic daily headache; tizanidine among the agents with evidence |
| [21770931](https://pubmed.ncbi.nlm.nih.gov/21770931/) | 2011 | Review | Headache | Chronic migraine prophylaxis trials; tizanidine among agents evaluated |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | Preclinical/formulation | J Control Release | Supramolecular self-assembly of tizanidine with meloxicam showing enhanced anti-migraine efficacy |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02536765 | MINT-TIZANIDINE | Not stated | Not stated |
| 02259893 | APO-TIZANIDINE | Not stated | Not stated |

---

## Safety Considerations

- **Predicted contraindication signals (knowledge graph, not label text)**: liver failure, kidney disease, pyoureter, psychotic disorder, schizophreniform disorder, mental disorder, schizoaffective disorder, hypotensive disorder.
- **Drug Interactions**: 100 interactions were identified. Major-level examples include famotidine, cimetidine, morphine, dolasetron and obeticholic acid. Moderate-level examples include hyoscyamine, loperamide, atropine, clarithromycin, levofloxacin, metoclopramide, naltrexone and dronabinol.
- **Other points to manage** (from the mechanistic assessment): sedation, hypotension, hepatotoxicity risk, and CYP1A2 interactions (e.g., fluvoxamine, ciprofloxacin).

Please refer to the package insert for full label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A directly matched Phase 3 placebo-controlled trial in migraine prevention exists, and older controlled and open-label studies in chronic daily headache support the direction. However, the Phase 3 trial's status is unknown with no verified results, and the controlled evidence concerns chronic daily headache rather than migraine specifically.

**To proceed, the following is needed:**
- Confirmation of NCT05484349 status and results
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A safety plan covering sedation, hypotension, liver function and CYP1A2 interaction management
- Approved-indication text and dosage forms for the Canadian products

*Other predicted indications (migraine with brainstem aura, migraine susceptibility, Tourette syndrome, atrophoderma vermiculata, ulerythema ophryogenesis) have little or no supporting evidence. The migraine susceptibility entry is a genetic-risk label best handled through the main migraine indication, and the two dermatological predictions are probably TxGNN model (deep learning) artifacts.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

