---
layout: default
title: Velpatasvir
parent: Model Prediction Only (L5)
nav_order: 962
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Velpatasvir is an HCV NS5A inhibitor, used in the fixed-dose combinations Epclusa (with sofosbuvir) and Vosevi (with sofosbuvir and voxilaprevir) to treat hepatitis C.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but none of the **26 retrieved clinical trials** or **20 publications** shows that velpatasvir treats HBV.
Only one trial involves HBV, and it uses velpatasvir for HCV in HCV/HBV co-infected patients, with tenofovir alafenamide (TAF) given for HBV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the product identity; the Canadian licence text is not provided) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (per Evidence Pack; no study shows anti-HBV efficacy) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Velpatasvir is known to inhibit the HCV NS5A protein, and its efficacy in hepatitis C is well established.

The prediction is weak mechanistically. HBV is a DNA virus (Hepadnaviridae) with no NS5A homolog, and no anti-HBV activity of velpatasvir is documented. The high score most likely reflects the shared "viral hepatitis" neighborhood in the knowledge graph rather than a shared drug target.

The clinical signal in the data is about HCV/HBV co-infection. In that setting HBV reactivation during direct-acting antiviral (DAA) therapy is a safety concern, not a therapeutic effect. The Phase 4 trial pairs sofosbuvir/velpatasvir with TAF, and TAF is the anti-HBV agent.

---

## Clinical Trial Evidence

Only the first trial involves HBV. The others are HCV studies retrieved by drug name and have no HBV endpoint.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | 12-week sofosbuvir/velpatasvir with prophylactic TAF in treatment-naïve HCV/HBV co-infected adults in China. It tests prevention of HBV reactivation, not HBV treatment by velpatasvir. |
| [NCT05016609](https://clinicaltrials.gov/study/NCT05016609) | Phase 4 | Unknown | 1800 | Same-visit HCV test-and-treat cluster trial in people who inject drugs. No HBV endpoint. |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | Sofosbuvir + velpatasvir ± ribavirin in treatment-naïve chronic HCV. Does not address HBV. |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | Sofosbuvir/velpatasvir ± ribavirin in HCV with decompensated cirrhosis. Does not address HBV. |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Completed | 268 | Sofosbuvir/velpatasvir in HCV with Child-Pugh B cirrhosis. Does not address HBV. |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Completed | 40 | Observational study of HCV in pregnancy, with postpartum sofosbuvir/velpatasvir. Does not address HBV. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | HBV reactivation, with a surface-antigen immune-escape mutant, in an anti-HBc-positive patient during sofosbuvir/velpatasvir for HCV. |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Real-world study | J Virus Erad | Effectiveness and safety of sofosbuvir/velpatasvir-based therapy for HCV in Chinese patients, including HCV/HBV co-infection subgroups. |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Treatment outcomes and cost study | J Viral Hepat | Simplified HCV treatment in Myanmar; HBV co-infected patients received tenofovir concurrently. |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Pediatric viral hepatitis. HCV has available DAAs, while HBV treatment remains far from curative. |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective evaluation | Klin Mikrobiol Infekc Lek | Antiviral treatment of chronic hepatitis B and C in children in Ostrava. |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | Overview of viral hepatitis treatment, including HBV and HCV. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2456370 | EPCLUSA |
| 2467542 | VOSEVI |

Dosage form and approved indication text are not provided for either product.

---

## Safety Considerations

- **Literature signal**: One published case report describes HBV reactivation in an anti-HBc-positive patient during sofosbuvir/velpatasvir for HCV ([PMID 31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/)). HBV status should be assessed before DAA therapy.

Please refer to the package insert for warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.87% TxGNN score is not backed by any anti-HBV efficacy evidence. No study shows velpatasvir treats HBV, and HBV has no NS5A target. The only HBV-related trial and the literature concern HCV treatment in co-infected patients, where HBV reactivation is a risk. The other nine predicted indications are also on Hold, and most of them are Level 5 (model prediction only).

**To proceed, the following is needed:**
- In vitro data showing whether velpatasvir has any anti-HBV activity
- Detailed mechanism of action data (MOA) from DrugBank
- Health Canada package insert warnings and contraindications
- Results from NCT04997564, interpreted as HBV reactivation prevention rather than HBV treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

