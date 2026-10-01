---
layout: default
title: Dapsone
parent: High Evidence (L1-L2)
nav_order: 246
evidence_level: L1
indication_count: 1
---

# Dapsone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Dapsone: From Established Anti-infective and Dermatological Use to Pneumocystosis

## One-Sentence Summary

Dapsone is an older sulfone antibacterial drug. The literature describes its use in leprosy and dermatitis herpetiformis, and the Canadian licence data provided here does not state an approved indication.
The TxGNN model predicts it may be effective for **pneumocystosis** (*Pneumocystis* pneumonia), with **14 registered clinical trials (4 completed Phase 3 trials)** and **19 publications** on this direction.
This looks like confirmation of a use already established in practice, not a new discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data. The literature describes leprosy and dermatitis herpetiformis (PMID 11155588). |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. The literature does describe how dapsone acts on *Pneumocystis*. A 1998 review (PMID 9675476) reports that dapsone blocks folic acid synthesis in the organism by inhibiting dihydropteroate synthetase. This is the same pathway targeted by sulfamethoxazole, the standard treatment. *Pneumocystis* depends on this pathway, which is consistent with the very high TxGNN score.

The same review reports strong anti-*Pneumocystis* activity in laboratory studies, animal studies and clinical trials. A dermatology review (PMID 11155588) also notes that dapsone is useful in preventing *Pneumocystis* pneumonia in patients with HIV. Guidelines and network meta-analyses treat dapsone-based regimens as one of several prophylaxis options.

Because the use is already established, the prediction is best read as model confirmation of known clinical practice. The remaining question is whether Canadian labelling and access support it.

---

## Clinical Trial Evidence

The 14 registered trials include 4 completed Phase 3 randomized trials of dapsone-containing regimens. Most were run in the 1990s in HIV populations. The nine most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Daily dapsone vs daily atovaquone for PCP prophylaxis in HIV patients intolerant to trimethoprim/sulfonamides |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim and clindamycin/primaquine vs TMP/SMX for mild-to-moderate PCP in AIDS |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Monthly aerosolized pentamidine vs thrice-weekly dapsone for PCP prophylaxis in TMP/SMX-intolerant HIV patients |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three anti-*Pneumocystis* regimens plus zidovudine for primary prevention in advanced HIV |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | Not applicable | Completed | Not reported | Dapsone 100 mg vs 50 mg as primary PCP prophylaxis in patients with AIDS-related complex |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | Not applicable | Completed | Not reported | Dapsone (plus trimethoprim) vs TMP/SMX for a first episode of PCP in AIDS patients |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly dapsone for PCP prophylaxis in HIV-infected children: toxicity and pharmacokinetics |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate with leucovorin plus dapsone vs TMP/SMX for moderately severe PCP: safety and pharmacokinetics |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3130 | HLA-B*1301 genetic screening to reduce dapsone hypersensitivity syndrome. Relevant to safety, not PCP efficacy. |

---

## Literature Evidence

The provided abstracts are truncated, so results are summarised only where the abstract states them.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic review / network meta-analysis of RCTs | Clin Microbiol Infect | Compares PCP prophylaxis regimens in people living with HIV, including dapsone-based regimens, TMP-SMX, aerosolized pentamidine and atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic review / network meta-analysis of RCTs | Clin Microbiol Infect | Compares PCP treatment regimens in people living with HIV, with TMP-SMX as the primary treatment |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline | J Antimicrob Chemother | ECIL guidance for PCP prophylaxis in haematological malignancy and stem cell transplant patients. TMP/SMX is the drug of choice. |
| [8018144](https://pubmed.ncbi.nlm.nih.gov/8018144/) | 1993 | Randomized trial | Am J Med | Dapsone vs aerosolized pentamidine for prophylaxis of PCP and toxoplasmic encephalitis in HIV patients with CD4 <250/mm³ |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | Clinical study | AIDS | Aerosolized pentamidine, cotrimoxazole and dapsone-pyrimethamine for primary prophylaxis of PCP and toxoplasmic encephalitis, including survival effects |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | Pharmacokinetic / safety study | Antimicrob Agents Chemother | Weekly dapsone, with or without pyrimethamine, for PCP prevention. Maximum tolerated weekly dose was 200 mg in patients receiving at least 500 mg of zidovudine. |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clin Infect Dis | Dapsone has strong anti-*Pneumocystis* activity by inhibiting folic acid synthesis |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | Overview of *Pneumocystis jirovecii* pneumonia risk factors, prevention and treatment |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report | Ann Pharmacother | Methemoglobinemia in a patient on dapsone for PCP prophylaxis |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Case report | Cureus | Hypoxia caused by dapsone-induced methemoglobinemia |

---

## Canada Market Information

The provided licence data has no dosage form, manufacturer or approved-indication text for either product.

| DIN | Product Name |
|---------|------|
| 02481227 | MAR-DAPSONE |
| 02281074 | ACZONE |

---

## Safety Considerations

No package-insert warnings or contraindications are available in the provided data, and no drug interactions were found. Please refer to the package insert for safety information.

The following points come from the literature and trial records in this pack:

- **Methemoglobinemia:** reported in patients taking dapsone for PCP prophylaxis, and can cause hypoxia and cyanosis (PMID 9606476, 32714715).
- **Hemolysis and G6PD deficiency:** screen for G6PD deficiency before use and monitor for hemolysis.
- **Hypersensitivity:** dapsone hypersensitivity syndrome has been studied with HLA-B*1301 screening (NCT02550080). Check for sulfonamide cross-reactivity.
- **Photosensitivity:** a rare complication, described in a case report (PMID 18309716).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four completed Phase 3 randomized trials of dapsone-containing regimens for PCP prevention or treatment, plus recent network meta-analyses, meet the L1 criteria. The trials are mostly from the 1990s and HIV-focused, and TMP/SMX remains the first-choice agent. Dapsone is therefore best positioned as an alternative for patients who cannot take TMP/SMX, with G6PD screening and methemoglobinemia monitoring as guardrails.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications for both products (a blocking gap for safety screening)
- Approved indication, dosage form and route for MAR-DAPSONE and ACZONE, to confirm whether a systemic formulation for PCP is authorized in Canada
- Mechanism-of-action data from DrugBank
- A review of the recent network meta-analyses (PMID 38583518, 39732393) for dapsone-specific efficacy and safety versus alternatives
- A monitoring plan covering G6PD testing, methemoglobin levels and hemolysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

