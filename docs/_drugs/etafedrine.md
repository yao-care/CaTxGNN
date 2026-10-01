---
layout: default
title: Etafedrine
parent: Moderate Evidence (L3-L4)
nav_order: 356
evidence_level: L4
indication_count: 1
---

# Etafedrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Etafedrine: From an Undocumented Original Indication to Bronchitis

## One-Sentence Summary

Etafedrine is an ephedrine-derivative bronchodilator, and the Canadian license record does not list its original approved indication. The TxGNN model predicts it may be effective for **bronchitis**. Support is limited to **2 old double-blind trials (1976-1977) of multi-ingredient combination products** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank. Based on its drug class, etafedrine is an ephedrine derivative that acts as a beta-adrenergic agonist bronchodilator. Relieving bronchospasm in bronchitis is therefore mechanistically plausible. This reasoning rests on the drug class, not on curated target data.

Bronchitis may also be close to etafedrine's historical use as a bronchodilator, so this may not be a true repurposing case. The original indication could not be confirmed, because the Canadian license record has no approved indication text.

The TxGNN score of 99.50% is a computational prediction, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [326265](https://pubmed.ncbi.nlm.nih.gov/326265/) | 1977 | RCT | Arzneimittel-Forschung | Double-blind long-term study of a combination of tetracycline, theophylline, doxylamine, etafedrine, phenylephrine and guaifenesine in chronic bronchitis. Of 57 patients with a prior exacerbation, only 12 showed clinical signs of exacerbation during the study. |
| [793781](https://pubmed.ncbi.nlm.nih.gov/793781/) | 1976 | RCT | Current Medical Research and Opinion | Double-blind, placebo-controlled crossover study in 48 patients with bronchospastic disease. It tested a long-acting bronchodilator combination containing etafedrine, bufylline, doxylamine and phenylephrine (1 week per arm). |

**Caveats:** Both studies tested multi-ingredient combinations, so etafedrine's own contribution cannot be separated. Only truncated abstracts were available, so full results were not assessed. The studies are nearly 50 years old.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2230769 | DALMACOL |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence is two old combination-product trials and a model score. There are no registered trials, the original indication is undocumented, and the safety data is missing entirely. At this stage it is a research question, not a candidate for advancement.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication). This is a blocking gap for safety screening.
- Mechanism of action and target data, for example via the DrugBank API.
- Full-text review of the two trials, to judge whether etafedrine contributes independently of the other ingredients.
- Confirmation of the original indication, to decide whether bronchitis is a true repurposing case.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

