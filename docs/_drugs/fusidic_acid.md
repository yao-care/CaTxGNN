---
layout: default
title: Fusidic Acid
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Fusidic Acid
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

The `txgnn-pipeline` skill covers pipeline operations, not report formatting — the full template is already established in the system prompt. Proceeding directly with the report generation.

---

# Fusidic Acid: From Staphylococcal Skin Infection to Exposure Keratitis

## One-Sentence Summary

Fusidic acid is a narrow-spectrum bacteriostatic antibiotic with well-established global use against *Staphylococcus aureus* infections, but it is currently not approved or marketed in Canada.
The TxGNN model's top-ranked novel prediction is **Exposure Keratitis**, supported by only **0 clinical trials** and **1 indirect case series**; however, across all 10 predicted indications, the most evidence-backed finding is **Post-bacterial Disorder (ABSSSI)** at rank 5, supported by a **completed Phase 3 RCT (n = 716)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the submitted evidence pack. Based on established pharmacological knowledge, fusidic acid is a steroidal antibiotic that inhibits bacterial protein synthesis by binding to and stabilizing the EF-G elongation factor on the ribosome, thereby blocking translocation. This mechanism is highly selective for gram-positive organisms, with *Staphylococcus aureus* (including MRSA) as its primary target. It has no relevant activity against gram-negative bacteria or non-bacterial pathogens.

Exposure keratitis arises from incomplete eyelid closure (lagophthalmos), resulting in chronic corneal desiccation, epithelial breakdown, and heightened susceptibility to secondary bacterial superinfection — with *S. aureus* among the most common colonizers of the compromised ocular surface. Given fusidic acid's potent anti-staphylococcal activity, there is a coherent mechanistic rationale for preventing or treating staphylococcal superinfection in this context. Importantly, ophthalmic formulations of fusidic acid (e.g., Fucithalmic® viscous eye drops) are already approved in several European countries for conjunctivitis, providing formulation and regulatory precedent for ocular use.

That said, the sole literature item retrieved (PMID 31246677) describes *Tsukamurella* spp. ophthalmic infections — an entirely different pathogen well outside fusidic acid's antibacterial spectrum. There is no direct clinical evidence for this specific indication. The TxGNN prediction likely reflects knowledge-graph proximity between the drug's antibacterial spectrum and ocular surface infection nodes rather than a documented mechanistic chain. A **Hold** decision is appropriate until targeted evidence is developed.

---

## Clinical Trial Evidence

Currently no clinical trials registered for exposure keratitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case Series | *Cornea* | Largest reported case series of *Tsukamurella* spp. ophthalmic infections; highlights clinical spectrum and risk factors of opportunistic ocular infections, but does not evaluate fusidic acid and involves a pathogen outside its antibacterial spectrum — indirect relevance only |

---

## All Predicted Indications — Summary

This evidence pack covers 10 TxGNN-predicted indications. The full landscape is presented below:

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Key Reason |
|------|-----------|-------------|----------------|---------|------------|
| 1 | Exposure Keratitis | 99.95% | L4 | Hold | No direct evidence; sole publication addresses an unrelated pathogen |
| 2 | Non-human Animal Disease | 99.86% | L5 | N/A | Out of scope for clinical repurposing framework |
| 3 | Otitis Externa | 99.84% | L4 | Research Question | Mechanistic support exists; evidence is primarily veterinary |
| 4 | Postinfectious Vasculitis | 99.83% | L5 | Hold | Immune complex–mediated pathology; antibacterial MOA does not apply |
| **5** | **Post-bacterial Disorder (ABSSSI)** | **99.82%** | **L2** | **Proceed with Guardrails** | **Phase 3 RCT completed (NCT02570490, n = 716)** |
| 6 | Post-infectious Syndrome | 99.82% | L5 | Hold | Neuroimmune dysregulation; no mechanistic link |
| 7 | Infective Urethral Stricture | 99.81% | L5 | Hold | Gram-negative pathogens; outside fusidic acid's spectrum |
| 8 | Chagas Cardiomyopathy | 99.80% | L5 | Hold | Protozoan (*T. cruzi*) disease; antibacterial MOA entirely irrelevant |
| 9 | Infection-related HUS | 99.79% | L5 | Hold | STEC-mediated; antibiotics generally contraindicated in this context |
| 10 | Parasitic Eyelid Infestation | 99.65% | L5 | Hold | Arthropod/parasitic infection; outside antibacterial spectrum entirely |

---

### Clinical Trial Evidence — Post-bacterial Disorder / ABSSSI (Rank 5, Priority Finding)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02570490](https://clinicaltrials.gov/study/NCT02570490) | Phase 3 | Completed | 716 | Randomized, double-blind, multicenter RCT comparing oral sodium fusidate (CEM-102 loading dose) vs. oral linezolid in ABSSSI; the largest and highest-quality existing trial for systemic fusidic acid — pivotal evidence for efficacy and safety |
| [NCT03173053](https://clinicaltrials.gov/study/NCT03173053) | NA | Terminated | 63 | Long-term *S. aureus* decolonization in home parenteral nutrition patients using topical ± systemic fusidic acid; terminated early at n = 63 — reason for early termination must be investigated before interpreting results |

### Literature Evidence — Otitis Externa (Rank 3, Secondary Finding)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [807907](https://pubmed.ncbi.nlm.nih.gov/807907/) | 1975 | Veterinary Clinical Study | *Nordisk veterinaermedicin* | Evaluated a topical preparation containing Fucidin (fusidic acid), framycetin, nystatin, and prednisolone in 235 canine ears with otitis externa; bacteriological sensitivity assessment included |
| [20434850](https://pubmed.ncbi.nlm.nih.gov/20434850/) | 2010 | Veterinary Microbiological Survey | *Veterinary Microbiology* | Combined case series/case-control study of coryneform bacteria in canine otitis externa across referral hospitals in Denmark and the US; fusidic acid is active against coryneforms |
| [12542200](https://pubmed.ncbi.nlm.nih.gov/12542200/) | 2002 | Observational Survey | *Acta Oto-laryngologica* | Assessed prevalence of community-acquired MRSA in discharging human ears; highlights MRSA as a pathogen in otorrhoea — relevant to fusidic acid's MRSA coverage |
| [12437801](https://pubmed.ncbi.nlm.nih.gov/12437801/) | 2002 | Observational/Bacteriology | *Journal of Laryngology and Otology* | Prospective bacteriological study of 161 patients with otorrhoea in Taiwan; *S. aureus* found in 43.5% of isolates, with increasing MRSA trend noted |
| [41148721](https://pubmed.ncbi.nlm.nih.gov/41148721/) | 2025 | Veterinary AMR Survey | *Antibiotics (Basel)* | AMR profiles of *S. pseudintermedius* in canine otitis externa and healthy dogs; discusses fusidic acid resistance implications and zoonotic potential |
| [41594059](https://pubmed.ncbi.nlm.nih.gov/41594059/) | 2025 | Veterinary AMR Survey | *Antibiotics (Basel)* | Retrospective review of bacterial etiology and AMR in canine otitis externa and pyoderma in Serbia (2017–2024); multidrug resistance patterns described |

---

## Canada Market Information

Fusidic acid is currently **not registered in Canada**. No Drug Identification Numbers (DINs) have been issued.

> Fusidic acid (as sodium fusidate) is approved and commercially available in numerous other jurisdictions, including the United Kingdom (Fucidin®), Australia, and multiple EU member states. Its ophthalmic formulation (Fucithalmic® viscous eye drops) is approved in several European countries. Any Canadian commercialization would require a full New Drug Submission (NDS) to Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Health Canada package insert data (warnings, contraindications, and drug interactions) were not available in this evidence pack. Based on international labels, known safety concerns include hepatotoxicity with prolonged systemic use, contact sensitization with topical formulations, and the risk of resistance emergence when used as monotherapy against *S. aureus*. No drug interaction data was identified in this analysis.

---

## Conclusion and Next Steps

### Primary Prediction: Exposure Keratitis (Rank 1)

**Decision: Hold**

**Rationale:**
The sole retrieved publication addresses a pathogen (*Tsukamurella* spp.) with no mechanistic link to fusidic acid, and no clinical trials exist for this indication. Mechanistic plausibility exists via anti-staphylococcal ophthalmic use, but is currently unverified by direct clinical data.

**To advance this indication, the following is needed:**
- Targeted clinical studies or retrospective analyses of fusidic acid ophthalmic formulation in exposure keratitis
- MOA data from DrugBank (data gap DG002)
- Health Canada package insert safety data (data gap DG001)
- Assessment of European ophthalmic approval (Fucithalmic®) as a regulatory bridge

---

### Priority Finding: Post-bacterial Disorder / ABSSSI (Rank 5)

**Decision: Proceed with Guardrails**

**Rationale:**
NCT02570490 (Phase 3, n = 716, completed, double-blind, multicenter) provides L2-level evidence for oral sodium fusidate in ABSSSI — the highest-quality evidence in this entire evidence pack. Clinically, this represents validation of fusidic acid's established antibacterial indication rather than a true novel repurposing, which is important for framing the regulatory strategy. NCT03173053 was terminated early and its findings cannot be relied upon without knowing the reason for termination.

**To proceed:**
- Obtain the full clinical study report for NCT02570490 and confirm primary endpoint outcomes
- Investigate the reason for early termination of NCT03173053
- Engage a Health Canada regulatory consultant to assess NDS requirements for systemic sodium fusidate
- Define the target patient population (e.g., MRSA skin infections as a linezolid/daptomycin alternative)

---

### Secondary Research Question: Otitis Externa (Rank 3)

**Decision: Research Question**

**Rationale:**
Fusidic acid covers the major otitis externa pathogens (*S. aureus*, CA-MRSA, coryneform bacteria), and otic formulations exist in some markets. However, the 6 retrieved publications are predominantly veterinary in origin, with only 2 addressing human otorrhoea bacteriology (without evaluating fusidic acid therapeutically). This is a viable research avenue, but requires a dedicated human clinical trial before a development decision can be made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

