---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 1
---

# Dapsone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dapsone: From Leprosy to Pneumocystosis

## One-Sentence Summary

Dapsone is a sulfone antibiotic with a long history of use in treating leprosy and dermatitis herpetiformis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PJP),
with **14 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Leprosy; dermatitis herpetiformis (from published literature; no Canadian product currently licensed) |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dapsone is a sulfone-class antibiotic that exerts its antimicrobial effect by inhibiting **dihydropteroate synthase (DHPS)**, a key enzyme in the folate biosynthesis pathway. This blockade starves susceptible organisms of the folate they need to synthesize DNA. When combined with trimethoprim — which inhibits the downstream enzyme dihydrofolate reductase (DHFR) — the two drugs attack the same pathway at two different steps, producing a synergistic bactericidal effect. This dual-target strategy is mechanistically identical to the first-line regimen trimethoprim-sulfamethoxazole (TMP-SMX), but Dapsone targets the DHPS node with a distinct chemical scaffold, making it a viable alternative for patients who cannot tolerate sulfonamides.

Pneumocystis jirovecii (formerly Pneumocystis carinii) is an atypical fungus that relies entirely on the folate pathway for survival, yet cannot synthesize or salvage exogenous folate. It therefore represents a near-ideal target for DHPS inhibitors. Multiple Phase 3 randomised controlled trials conducted in the 1990s established Dapsone (alone or combined with trimethoprim or pyrimethamine) as an effective second-line agent for both **prophylaxis** and **treatment** of PJP in HIV-infected patients with CD4 counts ≤ 200 cells/mm³. Contemporary guidelines from ECIL and major infectious disease societies continue to list Dapsone-based regimens as standard alternatives to TMP-SMX.

One critical safety caveat underpins the "Proceed with Guardrails" recommendation: patients with **glucose-6-phosphate dehydrogenase (G6PD) deficiency** are at substantially elevated risk of Dapsone-induced **methemoglobinemia** and haemolytic anaemia. Pre-treatment G6PD screening is therefore mandatory in any clinical programme that expands Dapsone use. The TxGNN prediction score of 99.73% is consistent with this already well-characterised mechanistic and clinical relationship — the model essentially confirms a use that is widely accepted internationally but remains unlicensed in Canada.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Head-to-head RCT: daily Dapsone vs Atovaquone for PCP prophylaxis in HIV patients intolerant of TMP/SMX (CD4 ≤ 200 cells/mm³); completed 1997. Primary evidence supporting Dapsone as a second-line prophylaxis agent. |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Three-arm RCT comparing Dapsone/TMP vs Clindamycin/Primaquine vs TMP/SMX for mild-to-moderate PCP treatment in AIDS patients; completed 1994. Establishes Dapsone combination as an effective treatment alternative. |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Randomised trial of three anti-PCP regimens (including Dapsone-based) plus Zidovudine for primary prevention in advanced HIV infection (CD4 < 200 cells/mm³); completed 1994. |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Randomised comparison of monthly aerosolised pentamidine vs thrice-weekly Dapsone for PCP prophylaxis in TMP/sulfonamide-intolerant HIV patients; completed 1994. |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3,130 | Large multicentre double-blind RCT evaluating prospective HLA-B\*1301 screening to reduce Dapsone Hypersensitivity Syndrome (DHS) incidence across multiple indications including PCP. Completion status unconfirmed; results pending verification. |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Compares daily vs weekly oral Dapsone for PCP prophylaxis in HIV-infected infants and children; pharmacokinetic data in paediatric population; completed 1998. |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | Completed | 168 | Case-control study of PCP risk factors after allogeneic HSCT; Dapsone evaluated as one real-world prophylaxis strategy, with up to 7.2% PCP breakthrough rate noted on low-dose Dapsone. |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | Completed | N/A | Head-to-head dose optimisation: Dapsone 100 mg vs 50 mg daily as primary PCP prophylaxis in ARC patients with CD4 < 400 cells/mm³. Informs minimum effective dosing. |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Randomised study of Trimetrexate + Leucovorin + Dapsone vs TMP/SMX for moderately severe PCP; pharmacokinetic characterisation of the three-drug regimen in AIDS patients. |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | N/A | Randomised prospective study of Dapsone + TMP vs TMP/SMX for first-episode PCP in AIDS patients; evaluates relative efficacy and suitability for outpatient treatment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic Review / Network Meta-analysis | Clin Microbiol Infect | Compared PCP prophylaxis regimens (TMP-SMX, Dapsone-based, aerosolised pentamidine, atovaquone) in people living with HIV via RCT network meta-analysis; provides current ranking of Dapsone regimens for efficacy and tolerability. |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic Review / Network Meta-analysis | Clin Microbiol Infect | Network meta-analysis of RCTs for PCP treatment regimens in HIV-positive patients; contextualises Dapsone-combination therapies relative to TMP-SMX and alternatives. |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Clinical Practice Guideline (ECIL-5) | J Antimicrob Chemother | European Conference on Infections in Leukaemia evidence-based recommendations for PJP prophylaxis in haematological malignancies and HSCT recipients; Dapsone listed as key alternative to TMP-SMX. |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Narrative Review | Expert Opin Pharmacother | Comprehensive review of Pneumocystis jirovecii with focus on prevention and treatment strategies including Dapsone; covers HIV and non-HIV immunocompromised populations. |
| [8018144](https://pubmed.ncbi.nlm.nih.gov/8018144/) | 1993 | RCT | Am J Med | Prospective randomised trial comparing Dapsone vs aerosolised pentamidine for prophylaxis of PCP and toxoplasmic encephalitis in HIV patients with CD4 < 250/mm³. |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | Comparative Trial | AIDS | Compares three primary prophylaxis regimens — aerosolised pentamidine, cotrimoxazole, and Dapsone-pyrimethamine — for PCP and toxoplasmic encephalitis, including survival outcomes. |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clin Infect Dis | Detailed pharmacological review of Dapsone for PCP: mechanism (DHPS inhibition), pharmacokinetics, clinical trial outcomes, and dosing strategies; foundational reference. |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Review / Pharmacology | Dermatol Clin | Reviews Dapsone and sulfapyridine pharmacology; confirms Dapsone's established role in PCP prophylaxis in HIV disease alongside anti-leprosy and anti-inflammatory uses. |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | Taiwan-authored review of Pneumocystis pneumonia epidemiology, diagnosis, and treatment; highlights Dapsone as a secondary option in the local clinical context. |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case Report / Safety | Ann Pharmacother | Case report of methemoglobinemia in a patient receiving Dapsone for PCP prophylaxis; directly relevant to the key safety guardrail requiring G6PD screening before use. |

---

## Canada Market Information

Dapsone currently holds **no active Drug Identification Numbers (DINs)** in Canada and is not commercially marketed through standard Health Canada regulatory pathways. Patients requiring Dapsone in Canada would typically access it through the **Special Access Programme (SAP)** or through importation. This regulatory gap is a practical barrier to routine prescribing and underscores the importance of establishing a formal access pathway if expanded use for PJP is pursued.

---

## Safety Considerations

Formal product monograph data for the Canadian market is unavailable (no licensed product). Based on the clinical trial and literature evidence reviewed, the following safety signals are well-established and must be addressed before clinical use:

- **Methemoglobinemia / Haemolytic Anaemia**: The most clinically significant adverse effect. Dapsone oxidises haemoglobin to methaemoglobin, causing functional hypoxia. Risk is markedly elevated in patients with **G6PD deficiency**. Pre-treatment G6PD screening is mandatory.
- **Dapsone Hypersensitivity Syndrome (DHS)**: A rare but potentially life-threatening multi-organ hypersensitivity reaction. Associated with the **HLA-B\*1301** allele; prospective genetic screening has been evaluated in a large Phase 4 trial (NCT02550080) to reduce incidence.
- **Photosensitivity Dermatitis**: Rare but documented complication; patients should be counselled on sun exposure.

> For complete warning and contraindication details, please refer to the package insert of a jurisdiction where Dapsone is licensed (e.g., FDA prescribing information or UK SmPC) until a Canadian product monograph becomes available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (including a 700-patient head-to-head comparison with Atovaquone and a 290-patient three-arm treatment trial) along with contemporary systematic reviews and international clinical practice guidelines (ECIL, IDSA) provide robust L1 evidence that Dapsone-based regimens are effective and guideline-endorsed alternatives for both prophylaxis and treatment of Pneumocystis jirovecii pneumonia. The TxGNN prediction score of 99.73% aligns with this strong empirical record.

**To proceed, the following is needed:**

- **Regulatory access pathway**: Dapsone has no Canadian DIN; a Special Access Programme application or formal Health Canada submission is required before prescribing.
- **Mandatory pre-treatment screening protocol**: Establish a G6PD deficiency screening programme to identify patients at high risk of methemoglobinemia before initiating therapy.
- **HLA-B\*1301 screening consideration**: Evaluate the cost-effectiveness of routine genetic screening to reduce Dapsone Hypersensitivity Syndrome risk, particularly in Asian patient populations where allele frequency is higher.
- **Methemoglobin monitoring plan**: Define baseline and on-treatment monitoring intervals for methemoglobin levels and complete blood count.
- **Patient population specification**: Clarify whether the target use case is (a) PJP prophylaxis in HIV-positive patients, (b) prophylaxis in non-HIV immunocompromised hosts (transplant, haematological malignancy), or (c) treatment of active disease — each carries a distinct evidence base and risk-benefit calculus.
- **Formal MOA documentation**: Obtain full DrugBank pharmacology record to complete the mechanism-of-action section of the regulatory dossier.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

