---
layout: default
title: Dapsone
parent: High Evidence (L1-L2)
nav_order: 248
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-13
description: "Dapsone: predicted new indication Pneumocystosis (evidence level L1). Approved use: Dermatitis herpetiformis, acne, leprosy"
monitor_inn: "DAPSONE"
predicted_indications: ["pneumocystosis"]
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

# Dapsone: From Dermatitis Herpetiformis to Pneumocystosis

## One-Sentence Summary

Dapsone was originally used for dermatitis herpetiformis, leprosy and acne.
The TxGNN model predicts it may be effective for **Pneumocystosis**,
with **10 clinical trials** (4 completed Phase 3 trials among them) and **20 publications** currently supporting this direction.
Note that this is effectively an already-established use, since dapsone is a guideline-recognised alternative to trimethoprim-sulfamethoxazole.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis herpetiformis, acne, leprosy (the licence records compiled for this report carry no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, dapsone is a sulfone that inhibits dihydropteroate synthase in the folate synthesis pathway. This is the same target as sulfonamides such as sulfamethoxazole.

*Pneumocystis jirovecii* depends on this folate pathway. This explains the very high prediction score and the clinical activity of dapsone in preventing and treating Pneumocystis pneumonia (PCP). Dapsone's original uses (leprosy, dermatitis herpetiformis) also reflect its anti-microbial and anti-inflammatory effects.

This is not a novel repurposing signal. Dapsone is already used as an alternative to trimethoprim-sulfamethoxazole, particularly in patients who cannot tolerate it. The model's prediction is consistent with existing clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Daily dapsone vs daily atovaquone for PCP prophylaxis in HIV patients intolerant of trimethoprim/sulfonamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three anti-Pneumocystis regimens (dapsone among them) plus zidovudine for primary prevention in advanced HIV |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Monthly aerosolised pentamidine vs thrice-weekly dapsone for PCP prophylaxis |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim and clindamycin/primaquine vs TMP-SMX for mild-to-moderate PCP in AIDS |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly oral dapsone for PCP prophylaxis in HIV-infected children; toxicity and pharmacokinetics |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate with leucovorin plus dapsone vs TMP-SMX for moderately severe PCP; safety and pharmacokinetics |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | Completed | Not reported | Dapsone 100 mg vs 50 mg for primary PCP prophylaxis in AIDS-related complex |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | Not reported | Dapsone plus trimethoprim vs TMP-SMX for first-episode PCP in AIDS patients |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3130 | HLA-B*1301 genetic screening to reduce dapsone hypersensitivity syndrome (safety-focused) |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Phase 4 | Withdrawn | 0 | Corticosteroids and pulmonary fibrosis in mild PCP; not about dapsone and no data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares PCP prophylaxis regimens in people with HIV, including TMP-SMX, dapsone-based regimens, aerosolised pentamidine and atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares treatment regimens for PCP in people with HIV; TMP-SMX remains the primary treatment |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline (ECIL) | J Antimicrob Chemother | Evidence-based PCP prophylaxis recommendations for haematological malignancy and stem cell transplant patients; TMP-SMX is the drug of choice |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | Review of *P. jirovecii* with a focus on prevention and treatment |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Review | Dermatol Clin | Dapsone is the most important drug for leprosy, useful for PCP prophylaxis in HIV, and the treatment of choice for dermatitis herpetiformis |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | Overview of Pneumocystis pneumonia |
| [19879509](https://pubmed.ncbi.nlm.nih.gov/19879509/) | 2009 | Review | Paediatr Respir Rev | Pneumocystis pneumonia in children |
| [10073326](https://pubmed.ncbi.nlm.nih.gov/10073326/) | 1999 | Pharmacokinetic study | J Clin Pharmacol | Pharmacokinetics of trimetrexate and dapsone in AIDS patients with PCP |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report | Ann Pharmacother | Methemoglobinemia in a patient receiving dapsone for PCP prophylaxis |
| [31631707](https://pubmed.ncbi.nlm.nih.gov/31631707/) | 2021 | Review | Drug Chem Toxicol | Dapsone-induced hepatic complications beyond methemoglobinemia |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02481227 | MAR-DAPSONE | Not specified | Not specified |
| 02281074 | ACZONE | Not specified | Not specified |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease, anaemia (including macrocytic anaemia), G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, and methemoglobinemia due to methemoglobin reductase deficiency.
- **Safety signals in the literature**: methemoglobinemia with hypoxia, hepatic complications, acute pancreatitis (case reports), and dapsone hypersensitivity syndrome (HLA-B*1301 screening has been studied).
- **Drug Interactions**: 100 interactions were identified. Those rated Moderate include aprepitant, metronidazole, picosulfuric acid, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, activated charcoal and troglitazone. Others, such as pantoprazole, omeprazole, metformin and vancomycin, have an unknown severity level.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four completed Phase 3 trials (290 to 700 participants each) and recent network meta-analyses support dapsone for PCP prophylaxis and treatment, and its use is already guideline-recognised as an alternative to TMP-SMX. Safety risks (haemolysis, methemoglobinemia, G6PD deficiency) and a heavy interaction burden call for guardrails.

**To proceed, the following is needed:**
- Review of the Health Canada package insert for official warnings and contraindications, and confirmation of whether PCP is a labelled indication for the two Canadian products
- Mechanism of action data from a primary source
- G6PD screening before use, plus monitoring of methemoglobin levels, haemoglobin and liver function
- A medication review to manage the interactions identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

