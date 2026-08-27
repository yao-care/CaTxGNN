---
layout: default
title: Methyl Aminolevulinate
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Methyl Aminolevulinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Methyl Aminolevulinate: From Actinic Keratosis (PDT) to Acne Vulgaris

## One-Sentence Summary

Methyl Aminolevulinate (MAL) is a topical prodrug photosensitizer approved in multiple countries for photodynamic therapy (PDT) of actinic keratosis, superficial basal cell carcinoma, and Bowen's disease.
The TxGNN model predicts it may be effective for **Acne Vulgaris** — the highest-evidence prediction among 10 candidates in this multi-indication report — with **5 clinical trials** and **13 publications** currently supporting this direction.
Although TxGNN assigns its highest scores to haematological and metabolic disease nodes (ranks 1–2), those predictions lack any supporting evidence and are mechanistically implausible; acne vulgaris (rank 3) represents the most actionable and best-evidenced new indication identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Actinic keratosis; superficial basal cell carcinoma; Bowen's disease (approved in multiple international markets; no Canadian DIN on file) |
| Predicted New Indication | Acne Vulgaris |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Methyl Aminolevulinate is a methyl ester prodrug of 5-aminolevulinic acid (5-ALA). After topical application, it is preferentially taken up by metabolically active or rapidly proliferating cells and converted intracellularly to protoporphyrin IX (PpIX) — a potent photosensitizer. When activated by red light (~630 nm), PpIX generates singlet oxygen and reactive oxygen species (ROS) that selectively destroy the targeted tissue. This mechanism is fundamentally tissue-agnostic: any cell type that over-accumulates PpIX becomes vulnerable to light-triggered cytotoxicity.

Acne vulgaris shares two features that make it a mechanistically coherent target. First, *Cutibacterium acnes* (formerly *Propionibacterium acnes*), the principal pathogen, is intrinsically rich in endogenous porphyrins and is exquisitely sensitive to PDT-generated ROS — direct bactericidal activity can be achieved without antibiotic exposure, avoiding resistance concerns. Second, sebaceous glands preferentially accumulate PpIX after MAL application, and selective photothermal destruction of the gland reduces sebum output and thereby reduces the environment that supports bacterial overgrowth. This dual mechanism — antimicrobial + anti-sebaceous — is mechanistically orthogonal to all current first-line acne therapies (retinoids, antibiotics, benzoyl peroxide) and provides a strong rationale for use in moderate-to-severe or antibiotic-resistant cases.

The prediction is further supported by the positioning of MAL as an off-label PDT agent in inflammatory dermatoses across European academic centres. A 2013 retrospective study covering 20 Italian departments found MAL-PDT to be the most evidence-rich off-label PDT use in inflammatory skin conditions — of which acne vulgaris was the leading indication. Although detailed MOA data are absent from the current Evidence Pack (Data Gap DG002), the mechanistic link between MAL-PDT and acne pathophysiology is well-characterised in the published literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00594425](https://clinicaltrials.gov/study/NCT00594425) | Phase 2 | Completed | 150 | Multicenter dose-escalation then blinded randomized vehicle-controlled study of MAL cream in moderate-to-severe facial acne; the largest and most direct MAL acne trial in this dataset |
| [NCT00673933](https://clinicaltrials.gov/study/NCT00673933) | Phase 2 | Completed | 20 | Blinded, randomized, intra-individual, vehicle-controlled study of MAL-PDT specifically in Fitzpatrick skin type V–VI patients with acne vulgaris; addresses underrepresented population |
| [NCT00206895](https://clinicaltrials.gov/study/NCT00206895) | Phase N/A | Completed | 24 | Randomized blinded controlled head-to-head comparison of MAL-PDT vs. ALA-PDT in moderate-to-severe facial acne vulgaris |
| [NCT01245946](https://clinicaltrials.gov/study/NCT01245946) | Phase 2 | Completed | 46 | ALA-PDT vs. adapalene gel 0.1% + doxycycline for moderate acne; provides indirect class evidence for aminolevulinate PDT vs. standard of care |
| [NCT02075671](https://clinicaltrials.gov/study/NCT02075671) | Phase 4 | Completed | 30 | PDT for papulopustular rosacea — an adjacent follicular inflammatory condition; supports PDT anti-inflammatory activity in follicular unit diseases |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38243786](https://pubmed.ncbi.nlm.nih.gov/38243786/) | 2024 | Systematic Review | J Cutan Med Surg | Comprehensive clinical update on approved and emerging topical PDT indications; confirms acne as a validated emerging indication with superior or non-inferior efficacy vs. comparators |
| [32554971](https://pubmed.ncbi.nlm.nih.gov/32554971/) | 2021 | Critical Review | Dermatology (Basel) | Critical reappraisal of off-label PDT for non-neoplastic skin conditions over 30 years; notes variable study quality but identifies acne as one of the most-studied inflammatory off-label targets |
| [22949035](https://pubmed.ncbi.nlm.nih.gov/22949035/) | 2013 | Retrospective Cohort | Photochem Photobiol Sci | Real-world MAL-PDT data from 20 Italian dermatology departments; acne vulgaris was the leading inflammatory indication for off-label MAL-PDT use |
| [22123417](https://pubmed.ncbi.nlm.nih.gov/22123417/) | 2011 | Review | Semin Cutan Med Surg | Overview of PDT in dermatology; topical MAL and ALA identified as primary agents with documented activity in acne alongside approved neoplastic indications |
| [20944910](https://pubmed.ncbi.nlm.nih.gov/20944910/) | 2010 | Review | An Bras Dermatol | Documents MAL approval status globally and reviews evidence for inflammatory applications including acne vulgaris |
| [23986167](https://pubmed.ncbi.nlm.nih.gov/23986167/) | 2013 | Comparative Review | J Drugs Dermatol | Direct comparison of MAL/PDT vs. ALA/PDT protocols; discusses mechanistic similarities and notes MAL's shorter incubation time advantage |
| [15888131](https://pubmed.ncbi.nlm.nih.gov/15888131/) | 2005 | Review | Photodermatol Photoimmunol Photomed | Early evidence establishing PDT benefit in inflammatory dermatoses including acne vulgaris and granuloma annulare |
| [18280335](https://pubmed.ncbi.nlm.nih.gov/18280335/) | 2008 | RCT | J Am Acad Dermatol | Long-pulsed dye laser vs. LPDL-assisted PDT for acne vulgaris; randomized controlled design demonstrates additive benefit when PDT is combined with laser |
| [17598868](https://pubmed.ncbi.nlm.nih.gov/17598868/) | 2007 | Case Series | Photodermatol Photoimmunol Photomed | MAL-PDT for chronic folliculitis in acne-prone skin; seven patients successfully treated after antibiotic failure — relevant to antibiotic-resistant acne scenario |
| [16566733](https://pubmed.ncbi.nlm.nih.gov/16566733/) | 2006 | Review | J Environ Pathol Toxicol Oncol | Establishes MAL as the most selective topical PDT agent based on fluorescence enrichment data; mechanistic support for preferential PpIX accumulation in pilosebaceous units |

---

## Canada Market Information

Methyl Aminolevulinate (DrugBank: DB00992) has **no Health Canada Drug Identification Numbers (DINs) on file** as of the data cutoff (2026-06-22). The drug is not currently marketed in Canada in any dosage form or indication.

> **Note:** Metvix® (MAL 160 mg/g cream) holds regulatory approvals in the EU, Australia, and other jurisdictions for actinic keratosis and skin cancers. No equivalent Canadian market authorization was identified in this dataset. A separate Health Canada product database query is recommended to confirm current status.

---

## Safety Considerations

Detailed Canadian-specific warning text and contraindication data are not available in this Evidence Pack (Data Gap DG001). Based on the known pharmacological class and published literature:

- MAL is a **topical agent** with minimal systemic absorption; systemic toxicity is not expected at therapeutic doses
- The primary adverse effect of PDT treatment is **local phototoxicity**: erythema, oedema, burning sensation, and crusting at the application site, typically resolving within days
- Patients must avoid **sun exposure** to treated areas for at least 48 hours post-illumination (photosensitivity risk)
- **Contraindications** in approved markets include known porphyria, hypersensitivity to porphyrins, and morpheaform (sclerosing) basal cell carcinoma

Please refer to the current package insert (or equivalent approved product monograph) for complete warnings, precautions, and contraindications before clinical use.

---

## Multi-Indication Landscape Summary

This Evidence Pack covers 10 TxGNN predictions. The table below summarises the full landscape for context:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|----------------|----------------|------|
| 1 | Hereditary hemochromatosis | 99.86% | L5 | Hold | Knowledge graph artefact; no biological plausibility |
| 2 | Seborrheic keratosis | 99.84% | L5 | Hold | No evidence in dataset; external literature search advised |
| **3** | **Acne vulgaris** | **99.81%** | **L2** | **Proceed with Guardrails** | **Primary actionable indication** |
| 4 | Vulvar inverted follicular keratosis | 99.80% | L5 | Hold | Rare disease; no evidence |
| 5 | Psoriasis | 99.44% | L3 | Research Question | Literature only; nail psoriasis niche may be viable |
| 6 | Common wart | 99.42% | L3 | Research Question | MAL-PDT for recalcitrant warts; case series evidence |
| 7 | Drug-induced osteoporosis | 99.24% | L5 | Hold | No mechanistic plausibility |
| 8 | Pityriasis lichenoides | 99.13% | L5 | Hold | Theoretical basis; no studies identified |
| 9 | Wilson disease | 99.11% | L5 | Hold | Metal metabolism artefact; no plausibility |
| 10 | Iron metabolism disease | 99.09% | L5 | Hold | Same graph-topology artefact as rank 1 |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 randomized controlled trials — including one multicenter study (n=150) directly testing MAL cream in moderate-to-severe acne — provide L2-level evidence. The mechanistic basis (dual bactericidal + sebaceous gland destruction via PDT) is well-established and scientifically sound. MAL-PDT for acne is already practiced off-label across European academic dermatology departments with a documented real-world safety profile.

**To proceed, the following is needed:**

- **Health Canada regulatory status confirmation**: Verify whether MAL/Metvix® has a current or historical DIN, or whether a new regulatory pathway (e.g., supplemental NDS for acne indication) would be required
- **Formal MOA documentation**: Retrieve DrugBank pharmacology data (Data Gap DG002) to complete the mechanistic dossier
- **Canadian prescribing information**: Obtain and parse the approved product monograph or package insert (Data Gap DG001) for contraindications and drug interaction data
- **Phase 3 evidence gap**: Current trials are Phase 2; a well-powered Phase 3 RCT would be required to support a formal indication expansion — identify whether any ongoing international trials could serve as pivotal data
- **Comparator benchmarking**: Define the target population (moderate-to-severe acne, antibiotic-resistant acne) where MAL-PDT's benefit over isotretinoin or antibiotic combinations is most defensible
- **Seborrheic keratosis (rank 2)**: Commission a targeted external literature search outside this dataset before finalising the Hold recommendation, as dermatology reviews suggest off-label PDT activity in this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

