---
layout: default
title: Clobazam
parent: Moderate Evidence (L3-L4)
nav_order: 208
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Clobazam: predicted new indication Febrile infection-related epilepsy syndrome (evidence level L4). Approved use: Lennox-Gastaut syndrome"
monitor_inn: "Clobazam"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "atypical childhood epilepsy with centrotemporal spikes", "cryptogenic late-onset epileptic spasms", "photosensitive occipital lobe epilepsy", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
---

# Clobazam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Clobazam: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a benzodiazepine antiseizure medication, originally used for Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
but there are **no registered clinical trials** and only **2 indirect publications** (case reports and series on other drugs) supporting this direction, so it remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut syndrome (from the TxGNN knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, clobazam is a positive allosteric modulator of the GABA-A receptor, its efficacy in Lennox-Gastaut syndrome is established, and mechanistically it may be applicable to refractory status epilepticus such as that seen in FIRES.

FIRES is a form of new-onset refractory status epilepticus in previously healthy children. Benzodiazepines are a logical class to consider. However, FIRES is largely driven by neuroinflammation and usually resists standard antiseizure drugs. The two retrieved papers concern enteral lorazepam and perampanel, not clobazam. The support is therefore class-level and indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disord | Enteral lorazepam as a weaning strategy for midazolam-responsive FIRES (a different benzodiazepine) |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | Perampanel may reduce barbiturate dependency in a 13-year-old with FIRES (not clobazam) |

Neither paper evaluates clobazam directly.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02238334 | TEVA-CLOBAZAM | Not specified | Not specified |
| 02244638 | APO-CLOBAZAM | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The ones shown here include:
  - **Major**: morphine (including liposomal morphine) and eliglustat.
  - **Moderate**: bupropion, aprepitant, omeprazole, esomeprazole, lansoprazole, cimetidine, clarithromycin, fenfluramine, dexfenfluramine, dronabinol and metoclopramide.
  - **Minor**: antacids such as magnesium oxide, aluminum hydroxide and calcium carbonate.
- Combining clobazam with opioids and other central nervous system depressants warrants particular caution because of additive sedation.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FIRES prediction has a high model score, but there are no clinical trials. The only literature is two case-level reports on other drugs, and FIRES is mainly neuroinflammatory and typically resistant to standard antiseizure drugs. This is a research question, not an actionable repurposing candidate.

**To proceed, the following is needed:**
- Clobazam-specific data in FIRES or refractory status epilepticus (case series or registry data)
- Mechanism of action data, and a review of immunotherapy and ketogenic diet approaches as comparators
- Health Canada package insert warnings and contraindications, which are required before safety screening
- A DDI management plan, especially for opioids and CYP2C19/CYP3A4 modulators

**Other predicted indications (for reference):**
- **Childhood onset epileptic encephalopathy** (score 99.59%, L3) is the most credible option. Clobazam is already approved for Lennox-Gastaut syndrome, and multiple reviews and guidelines discuss it. However, this largely extrapolates from the approved indication rather than giving independent confirmation. It could be considered "Proceed with Guardrails": apply by syndrome and etiology, and monitor sedation, tolerance, and behavioural and cognitive effects.
- **Benign occipital epilepsy** (L4) has indirect support from a Cochrane review of clobazam monotherapy, but this condition often needs little or no treatment.
- The remaining predictions have little or no literature (L4–L5) and should be held. They are perioral myoclonia with absences, atypical childhood epilepsy with centrotemporal spikes, cryptogenic late-onset epileptic spasms, photosensitive occipital lobe epilepsy, GRIN2A-related encephalopathy, restless legs syndrome, and polymicrogyria with optic nerve hypoplasia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

