---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From an Unrecorded Original Indication to Migraine Disorder

## One-Sentence Summary

Camphor is marketed in Canada in five products, but no approved indication text was recorded for any of them.
The TxGNN model predicts it may be relevant to **migraine disorder**, with **no registered clinical trials** and **5 publications**, none of which show that camphor benefits migraine.
Two of the five are case reports and a case series describing headache *triggered by* camphor-containing toothpaste, so the evidence is weak and points partly toward harm.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the Canadian licence data) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only). The pack lists L4, but the only camphor-specific papers are case reports of camphor-associated headache, not efficacy or mechanism studies. |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for camphor, and no original indication was recorded. The prediction therefore cannot be tied to a known drug mechanism.

A plausible link is sensory modulation, such as TRPV1/TRPM8 desensitisation and counter-irritant effects from topical or aromatic use. This is a hypothesis only, and nothing in the supplied evidence supports it.

Camphor also has known neurotoxicity and seizure risk. Essential oils with pro-convulsant properties may worsen migraine, and the two cluster headache reports link camphor-containing toothpaste to headache onset. The safety question should be settled before any research question is pursued.

The nine lower-ranked predictions are also on Hold and do not change this picture:
- **Migraine with brainstem aura and migraine susceptibility:** the scores likely reflect similarity to the parent migraine node. The literature retrieved for migraine susceptibility concerns epilepsy genetics and never mentions camphor.
- **Pulmonary hypertension:** all 20 papers concern CAMPHOR, the Cambridge Pulmonary Hypertension Outcome Review questionnaire. This is a name collision, not evidence for the drug.
- **Raynaud disease:** camphor is a topical rubefacient that causes local vasodilation, so a superficial rationale exists, but the one retrieved paper is a questionnaire review, not evidence for camphor.
- **Erectile dysfunction, kyphoscoliotic heart disease, ulerythema ophryogenesis, atrophoderma vermiculata and Tourette syndrome:** prediction only, with no trials, literature or plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cases of cluster headache secondary to toothpastes containing pro-convulsant essential oils. Reports harm, not benefit. |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Reports | Two cases of cluster headache temporally related to toothpastes containing camphor and eucalyptus oils. |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical analysis of paediatric neuropsychopharmacology in the 1940s and 50s. Does not test camphor for migraine. |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Review | Minerva Medica | Therapy for essential hemicrania. No abstract available, and no camphor-specific efficacy data. |
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT | J Headache Pain | Phase 3 trial of erenumab for chronic migraine prevention in Asian patients. Not a camphor study. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 299561 | CREO-RECTAL ADULTES/ADULTS |
| 299596 | CREO-RECTAL ENFANTS/CHILDREN |
| 319716 | DEMO-CINEOL ADULTES/ADULTS |
| 319724 | DEMO-CINEOL ENFANTS/CHILDREN |
| 2157292 | BLISTEX DCT |

Dosage form, manufacturer and approved indication text were not recorded for these products.

---

## Safety Considerations

- **Neurotoxicity and seizure risk:** camphor has a known neurotoxicity and seizure risk. The retrieved case reports describe headache attacks linked to camphor-containing products.

No warnings, contraindications or drug interaction records were retrieved. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high TxGNN score is not backed by any trial, mechanism data or efficacy literature. The only camphor-specific papers suggest camphor may trigger headache rather than treat it.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block any safety screening
- Mechanism of action data, for example from DrugBank
- The approved indications for the five Canadian products
- A safety review of camphor's neurotoxicity and seizure risk in headache-prone patients
- Preclinical or clinical evidence that camphor helps migraine, since none exists in the current data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

