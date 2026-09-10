---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

# Mupirocin: From Topical Skin Infections to Staphylococcal Scalded Skin Syndrome (SSSS)

## One-Sentence Summary

Mupirocin is a topical antibacterial agent traditionally used for skin and nasal *Staphylococcus aureus* infections (e.g., impetigo, MRSA decolonization). Among 10 TxGNN-predicted indications in this evidence pack, **Staphylococcal Scalded Skin Syndrome (SSSS)** stands out as the lead candidate — not the highest-scoring one, but the only one supported by actual clinical literature (**0 clinical trials, 14 publications**), reaching evidence stage S2 while the other 9 candidates remain at S0/S1 with weak or absent mechanistic plausibility.

> Note: the top TxGNN-scored candidate (pleural empyema, 99.49%) was explicitly flagged by the model's own rationale as biologically implausible (mupirocin has no systemic formulation) and has zero supporting evidence. SSSS was therefore selected as the reportable candidate on evidentiary grounds rather than raw score rank.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical treatment of bacterial skin/nasal infections (e.g., impetigo, *S. aureus* decolonization) — based on general pharmacology; no Canada-specific licensed indication text is available |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome (SSSS) |
| TxGNN Prediction Score | 95.57% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap). Based on the mechanistic evidence captured alongside this prediction, mupirocin inhibits bacterial isoleucyl-tRNA synthetase and shows high activity against *S. aureus*, including MRSA.

SSSS is caused by exfoliative toxin A/B-producing strains of *S. aureus* originating from a localized infection focus (commonly nasal, umbilical, or skin). Because mupirocin's antibacterial spectrum directly targets the causative organism, it is mechanistically well-matched — not as monotherapy for the systemic toxin-mediated disease, but as an adjunct to clear the infectious focus alongside systemic antibiotics.

This is corroborated by real-world use: a cohort study (PMID 37404367) evaluated 2% mupirocin ointment combined with intravenous antibiotics specifically in pediatric SSSS management. However, emerging mupirocin-resistant *S. aureus* clones causing SSSS-related skin infections have been reported (PMID 28592549, 30418106), which tempers the mechanistic confidence and should be monitored.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Cohort | Clinical, Cosmetic and Investigational Dermatology | Compared IV antibiotics combined with 2% mupirocin ointment for treatment duration, cost, and outcomes in pediatric SSSS |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Review of Anti-infective Therapy | Reviews treatment approaches for bullous impetigo and SSSS in infants, a disease spectrum caused by staphylococcal exfoliative toxin |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Case report | Journal of Clinical Microbiology | Documents emergence of a mupirocin- and fusidic acid-resistant *S. aureus* clone causing community-acquired skin/soft tissue infections |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Case report / Molecular epidemiology | Journal of Medical Microbiology | Reports a mupirocin- and fusidic acid-resistant, toxinogenic methicillin-susceptible *S. aureus* clone driving an SSSS increase |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Cohort / Outbreak investigation | Journal of Hospital Infection | Epidemiological investigation and infection control of a nosocomial SSSS outbreak among 13 neonates |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case series | Advances in Neonatal Care | Identification and wound care case series of SSSS in neonates caused by methicillin-susceptible *S. aureus* |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Cohort | Pediatric Infectious Disease Journal | Molecular epidemiology showing increasing SSSS cases caused by ST121 *S. aureus* strain in children |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | Cohort / Molecular epidemiology | Pediatric Infectious Disease Journal | Describes SSSS cases in premature infants and infection-control strategies to prevent outbreak spread |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case report | Dermatopathology (Basel) | Rare adult SSSS case in an immunocompromised chemotherapy patient, illustrating atypical presentation |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatologic Clinics | Discusses staphylococcal control (including topical mupirocin) as central to managing staphylococcal skin disease |

---

## Canada Market Information

Mupirocin is currently not marketed in Canada under this evidence pack (0 licenses/DINs on record). No product authorization data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between mupirocin's anti-*S. aureus* activity and SSSS's toxin-producing bacterial etiology is sound, and real-world cohort/case evidence supports its use as adjunct therapy — but no controlled trials exist, mupirocin resistance is emerging in SSSS-associated strains, and Canada market/safety documentation is entirely absent.

**To proceed, the following is needed:**
- Health Canada product monograph, warnings, and contraindications (currently blocking — DG001)
- Confirmed mechanism-of-action detail from DrugBank (DG002)
- Assessment of local mupirocin resistance prevalence before adjunct-use recommendations
- Route-compatibility review, since mupirocin is topical-only and SSSS requires systemic antibiotic co-therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

