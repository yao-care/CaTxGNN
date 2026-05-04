---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic widely used for bacterial infections and approved by the US FDA for plague as a bioterrorism countermeasure.
The TxGNN model ranks **Diffuse Scleroderma** as its top new predicted indication (score: 99.87%), supported by a dual-mechanism hypothesis — direct antifibrotic activity via TGF-β modulation, and indirect immune modulation through treatment of small intestinal bacterial overgrowth (SIBO) commonly seen in scleroderma patients.
Current evidence consists of **2 publications** (no registered clinical trials), placing this indication at an early exploratory stage (Level L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (fluoroquinolone antibiotic; US FDA-approved for plague) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (Preclinical / Mechanism studies) |
| Canada Market Status | Not marketed (no DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Ciprofloxacin is a second-generation fluoroquinolone whose primary bactericidal mechanism is inhibition of bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV, disrupting DNA replication in a broad spectrum of Gram-negative and select Gram-positive pathogens. Beyond its antibacterial activity, emerging experimental evidence suggests ciprofloxacin may possess off-target properties relevant to fibrotic diseases such as scleroderma — though detailed MOA characterization for this application remains incomplete.

The first proposed pathway is a **direct antifibrotic mechanism**: ciprofloxacin has demonstrated the ability to inhibit collagen synthesis enzymes and downregulate TGF-β signaling in experimental settings. TGF-β is the master driver of fibrosis in diffuse scleroderma, promoting myofibroblast activation and excessive extracellular matrix deposition in the skin and visceral organs. A 2010 study (PMID 20507401, *The Journal of Dermatology*) directly evaluated oral ciprofloxacin as an antifibrotic agent in scleroderma patients using a controlled, double-blind randomized design, constituting the only available clinical evidence for this hypothesis.

The second pathway is **indirect immune modulation via SIBO treatment**: systemic sclerosis patients frequently develop small intestinal bacterial overgrowth as a consequence of gastrointestinal dysmotility. Bacterial translocation from the dysbiotic gut contributes to systemic inflammatory activation that may amplify fibrotic processes. Ciprofloxacin's ability to suppress enteric bacterial overgrowth — documented in a 1995 cohort of 24 scleroderma patients (PMID 7728404, *British Journal of Rheumatology*) — provides a mechanistically distinct but clinically complementary rationale for its potential benefit in this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for ciprofloxacin in diffuse scleroderma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Small Pilot RCT | The Journal of Dermatology | Controlled double-blind randomized trial evaluating oral ciprofloxacin as an antifibrotic agent in scleroderma; assessed whether ciprofloxacin reduces the clinical severity of skin fibrosis |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observational / Diagnostic | British Journal of Rheumatology | 24 scleroderma patients (6 diffuse form) investigated for SIBO using jejunal aspiration; treatment outcomes documented, supporting targeted antibiotic use as part of scleroderma management |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinically Important Notice:** All fluoroquinolones, including ciprofloxacin, carry a US FDA Black Box Warning for peripheral neuropathy, tendinopathy and tendon rupture, aortic aneurysm/dissection, and CNS effects. These risks are especially relevant when evaluating use in patients with connective tissue disorders such as diffuse scleroderma, where tissue integrity is already compromised. Any study in this population requires a careful benefit-risk assessment.

---

## Multi-Indication Summary

This Evidence Pack evaluates 10 TxGNN-predicted indications for ciprofloxacin. The table below provides an at-a-glance decision overview for all predictions:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|---------------------|-------------|----------------|----------------|-------|
| 1 | Diffuse Scleroderma | 99.87% | L4 | Research Question | 2 publications; dual mechanism hypothesis (antifibrotic + SIBO) |
| 2 | Hyperamylasemia | 99.87% | L5 | Hold | No evidence; KG inference artifact (pancreatitis → antibiotic use → elevated amylase) |
| 3 | Polyclonal Hyperviscosity Syndrome | 99.87% | L5 | Hold | No mechanistic basis; plasma viscosity is not reduced by antibiotics |
| 4 | Congenital Analbuminemia | 99.85% | L5 | Hold | Genetic (ALB gene) disease; antibiotics cannot correct albumin synthesis defects |
| 5 | Blood Group Incompatibility | 99.78% | L5 | Hold | Immunohematology problem; no biological relevance to antimicrobial therapy |
| 6 | Premalignant Hematological Disease | 99.73% | L5 | Hold | MDS/MGUS are clonal marrow disorders, not infection-driven |
| 7 | Punctate Epithelial Keratoconjunctivitis | 99.71% | L5 | Hold | PEK is typically viral/dry-eye etiology; ciprofloxacin eye drops approved for bacterial conjunctivitis only |
| 8 | Monoclonal Gammopathy | 99.71% | L4 | Research Question | Evidence reflects prophylactic infection prevention in MM/HSCT patients — not disease-modifying for gammopathy itself |
| 9 | Hematological Disease + Peripheral Neuropathy | 99.68% | L5 | Hold | ⚠️ Safety contraindication: fluoroquinolones can induce or worsen peripheral neuropathy (FDA Black Box Warning 2016) |
| **10** | **Septicemic Plague** ⭐ | **99.64%** | **L2** | **Proceed with Guardrails** | **US FDA-approved indication; Phase 2 RCT completed; strongest evidence in this pack** |

---

## Spotlight: Septicemic Plague (Rank 10 — Highest Clinical Evidence)

Although ranked 10th by TxGNN score, **septicemic plague** is the most actionable finding in this Evidence Pack, carrying Evidence Level **L2** and a **Proceed with Guardrails** recommendation. Notably, ciprofloxacin is already US FDA-approved for plague (including septicemic, bubonic, and pneumonic forms) under the Animal Efficacy Rule as a bioterrorism countermeasure — making this a confirmation of an established indication rather than a novel repurposing.

**Mechanism:** Ciprofloxacin inhibits the DNA gyrase of *Yersinia pestis* (GyrA/GyrB subunits), achieving bactericidal activity at MIC ≤ 0.015 µg/mL — among the lowest MICs of any approved antibiotic against this pathogen.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01243437](https://clinicaltrials.gov/study/NCT01243437) | Phase 2 | Completed | 200 | Non-inferiority randomized trial of ciprofloxacin vs. doxycycline in human plague (bubonic, septicemic, pneumonic); conducted in Africa where >95% of WHO-reported cases occur |

### Literature Evidence (Selected)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40768716](https://pubmed.ncbi.nlm.nih.gov/40768716/) | 2025 | RCT | New England Journal of Medicine | IMASOY trial final results: ciprofloxacin monotherapy vs. aminoglycoside + ciprofloxacin for bubonic plague in Madagascar |
| [32807214](https://pubmed.ncbi.nlm.nih.gov/32807214/) | 2020 | RCT Protocol | Trials | IMASOY trial protocol: open-label non-inferiority comparison of ciprofloxacin vs. streptomycin + ciprofloxacin, 10-day regimen |
| [38970065](https://pubmed.ncbi.nlm.nih.gov/38970065/) | 2024 | RCT Protocol Update | Trials | Updated IMASOY protocol (NCT04110340); reflects protocol amendments and revised endpoints |
| [28125398](https://pubmed.ncbi.nlm.nih.gov/28125398/) | 2017 | Case Series | Emerging Infectious Diseases | 5 culture-confirmed human plague cases (including 1 pneumonic) treated successfully with oral ciprofloxacin; first published human case series post-FDA approval |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal Model Study | Clinical Infectious Diseases | Ciprofloxacin and levofloxacin ≥90% effective in African green monkey pneumonic plague model; evaluates treatment delay effects |
| [12567312](https://pubmed.ncbi.nlm.nih.gov/12567312/) | 2003 | Case Report | Clinical Infectious Diseases | Critically ill patient with septicemic plague and peripheral gangrene — first reported case of successful ciprofloxacin treatment for plague |
| [9533478](https://pubmed.ncbi.nlm.nih.gov/9533478/) | 1998 | Animal Model Study | Journal of Antimicrobial Chemotherapy | Efficacy of ciprofloxacin prophylaxis and therapy against experimental pneumonic plague (Y. pestis strains GB and CO-92) in mouse model |
| [23285069](https://pubmed.ncbi.nlm.nih.gov/23285069/) | 2012 | Animal Model Study | PLoS ONE | Ciprofloxacin + gentamicin combination vs. monotherapy in murine bubonic plague; synergy assessment in vitro and in vivo |
| [8722542](https://pubmed.ncbi.nlm.nih.gov/8722542/) | 1996 | Animal Model Study | Journal of Antimicrobial Chemotherapy | Doxycycline or ciprofloxacin prophylaxis and therapy: complete protection with ciprofloxacin (20–40 mg/kg) against IP challenge of 5.24 × 10⁷ CFU |
| [28220110](https://pubmed.ncbi.nlm.nih.gov/28220110/) | 2017 | Animal Model Study | Frontiers in Microbiology | Inhaled liposomal ciprofloxacin (Lipoquin®/Pulmaquin®) protects against lethal pneumonic plague in murine model; novel delivery formulation data |

---

## Conclusion and Next Steps

### Primary Indication — Diffuse Scleroderma

**Decision: Research Question**

**Rationale:**
Evidence for ciprofloxacin in diffuse scleroderma is limited to 2 publications — one small pilot trial and one observational study — with no registered clinical trials. The dual-mechanism hypothesis (antifibrotic + SIBO) is biologically plausible and internally consistent, but falls far short of the evidence threshold needed for clinical development. Safety concerns associated with fluoroquinolones in connective tissue disease patients add an additional layer of risk that requires prospective evaluation.

**To proceed, the following is needed:**
- Full-text review and independent quality appraisal of PMID 20507401 to determine actual sample size, randomization quality, outcome measures, and effect size
- Preclinical studies in validated scleroderma models (e.g., bleomycin-induced fibrosis) confirming TGF-β inhibition and collagen reduction
- Patient stratification strategy: SIBO-positive vs. SIBO-negative scleroderma; diffuse vs. limited cutaneous forms
- Formal safety risk assessment: fluoroquinolone-associated tendinopathy and peripheral neuropathy risks are especially concerning in connective tissue disease populations
- Consideration of a small-scale investigator-initiated pilot study (Phase 1/2 open-label) in SIBO-associated systemic sclerosis before proceeding to a full RCT

---

### Secondary Finding — Septicemic Plague

**Decision: Proceed with Guardrails**

**Rationale:**
Ciprofloxacin is already FDA-approved for plague (including septicemic plague) under the Animal Efficacy Rule, and the 2025 NEJM publication of the IMASOY RCT provides the highest level of human clinical evidence available for any plague antibiotic. This is not a novel repurposing opportunity but rather a confirmation of an existing approved indication not yet registered in Canada.

**For Canada access and registration, the following may be needed:**
- Verify whether Health Canada has granted a Drug Identification Number (DIN) or emergency access authorization for ciprofloxacin for the plague indication
- Align with the Public Health Agency of Canada's National Emergency Strategic Stockpile (NESS) protocols for bioterrorism preparedness
- Confirm approved dosing regimens and treatment duration specifically for septicemic plague (vs. bubonic or pneumonic presentations)
- Consider submission of a regulatory supplement to Health Canada referencing the completed NCT01243437 data and 2025 NEJM results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

