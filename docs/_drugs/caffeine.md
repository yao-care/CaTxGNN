---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis…"
monitor_inn: "CAFFEINE"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "vein disease"]
---

# Caffeine
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

# Caffeine: From Headache and Rhinitis Disorders to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a well-known methylxanthine stimulant, used in Canada mainly as an ingredient in combination headache and pain products and as a single-ingredient treatment in neonatal care. It is originally associated with allergic rhinitis, migraine, cluster headache, and cold-related conditions.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, but there are **0 clinical trials** and only **3 loosely related publications** (a review, a formulation study, and an animal study), so this remains a model-based hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis, common cold, cluster headache and related headache disorders (from the knowledge graph; no approved indication text is available in the Canadian licence data) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, caffeine is a methylxanthine that blocks adenosine receptors and inhibits phosphodiesterase. Its efficacy in headache disorders is established, and it is already linked to rhinitis and the common cold through combination products.

The link to nasal disease is plausible but unproven. Bitter taste receptors (TAS2Rs) in human airway epithelium respond to caffeine-like compounds and may influence ciliary beating and innate defence. A nasal caffeine gel has been studied, but for cognition after sleep deprivation, not for nasal disease. The high TxGNN score most likely reflects proximity to the existing rhinitis and cold indications rather than new evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in human airways, including the nasal cavity, and may play a role in airway defence |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical formulation study | Current Drug Delivery | Thermo-sensitive nasal caffeine in situ gel studied for cognition after sleep deprivation, not for nasal disease |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited lung tumour formation in rats; only tangentially relevant |

---

## Canada Market Information

Indication text and dosage forms were not available in the licence data. The first five of the 20 valid single-ingredient authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02496771 | PEYONA |
| 02526751 | Caffeine Citrate Oral Solution USP |
| 02526778 | Caffeine Citrate Injection USP |
| 02254468 | Tylenol Ultra Relief |
| 02544687 | Extra Strength Tylenol Daytime Relief |

---

## Safety Considerations

- **Knowledge-graph contraindications** (not from label text): hypertension, orthostatic hypotension and related autonomic conditions, long QT syndrome, liver failure and liver disease, kidney disease, epilepsy, insomnia, anxiety disorders, COPD, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, and porphyria.
- **Drug interactions**: 75 interactions were identified. Examples of those listed in the data:
  - **Major**: nasal and topical cocaine.
  - **Moderate**: alosetron, obeticholic acid, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole, duloxetine.
  - **Minor**: acetylsalicylic acid, cimetidine, atazanavir, disulfiram.

Official package insert warnings and contraindications were not available, so please refer to the Health Canada package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and indirect literature. There are no clinical trials and no direct evidence for nasal disease, and the mechanistic link is speculative.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Defined target nasal conditions and a feasibility check of a nasal or topical route
- Preclinical or early clinical evidence of benefit in nasal disease

---

### Other Predicted Indications (Brief Note)

The same analysis produced other predictions with the following evidence levels:
- **Hypnic headache** (L4, research question): reviews and case series support caffeine as a first-line option, but there are no controlled trials, and caffeine can contribute to medication-overuse headache.
- **Neuralgia** and **trigeminal autonomic cephalalgia** (L4, research question): mostly preclinical or adjuvant-focused evidence, or an extension of existing headache indications.
- **Thrombotic disease** (L4, hold): evidence is mixed and indirect, with no support for antithrombotic use.
- **Acute laryngopharyngitis, papillary conjunctivitis, glossodynia, coccygodynia, vein disease** (L5, hold): no supporting trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

