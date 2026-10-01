---
layout: default
title: Itraconazole
parent: Moderate Evidence (L3-L4)
nav_order: 500
evidence_level: L4
indication_count: 1
---

# Itraconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Itraconazole: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Itraconazole is an azole antifungal marketed in Canada. Its approved indication text is not available in the data provided.
The TxGNN model predicts it may be effective for **pneumocystosis**, but **no clinical trials** are registered for this pairing, and the **20 publications** retrieved do not directly support it.
Standard biology argues against the prediction, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local licence data (itraconazole is an antifungal) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Itraconazole is known to inhibit fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis in fungal membranes. That is the basis of its use against fungi such as Histoplasma, Aspergillus and Talaromyces.

The high TxGNN score (0.993) is **not supported biologically**. *Pneumocystis jirovecii* has little or no ergosterol in its membrane and uses cholesterol instead, so azoles are not expected to be active against it. A 2003 study of the Pneumocystis carinii Erg11 enzyme also describes the organism as intrinsically resistant to azole antifungals.

The graph association most likely reflects co-mention in opportunistic-infection settings such as HIV and transplantation. In these settings itraconazole treats other fungi, while pneumocystosis is managed with trimethoprim-sulfamethoxazole. The prediction is therefore probably a literature-context artefact rather than a real therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled phase III trial of itraconazole prophylaxis against deep fungal infections in HIV-infected patients. It is not specific to pneumocystosis. |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanism study | Am J Respir Cell Mol Biol | Cloned the Pneumocystis carinii lanosterol 14-alpha-demethylase (Erg11), the azole target. The organism is described as intrinsically resistant to azoles. |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Reviews therapy and prophylaxis of systemic protozoan infections, including Pneumocystis carinii. |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infections after lung transplantation and their prevention and treatment. |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | Prophylaxis and treatment of infection in bone marrow transplant recipients. |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clin Evid | Primary and secondary prophylaxis of opportunistic infections in HIV. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid. |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplant Proc | Single-centre experience of invasive fungal infections after kidney transplantation. |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian J Med Microbiol | Respiratory fungal pathogens in immunocompetent versus immunocompromised hosts, in relation to CD4 counts. |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Front Immunol | Talaromyces marneffei and Pneumocystis jirovecii coinfection in a child with a STAT1 mutation. |

None of these publications shows itraconazole treating pneumocystosis. Relevance screening of all retrieved articles is still pending.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2495988 | ODAN ITRACONAZOLE |
| 2047454 | SPORANOX |
| 2484315 | JAMP ITRACONAZOLE ORAL SOLUTION |
| 2462559 | MINT-ITRACONAZOLE |

Dosage forms and approved-indication text are not available in the data provided, apart from the oral solution named in the JAMP product.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by biology. *Pneumocystis* lacks the ergosterol target of azoles and is intrinsically resistant, and no trial or study shows itraconazole benefit. The standard therapy and prophylaxis, trimethoprim-sulfamethoxazole, is well established.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications and approved indications)
- Mechanism-of-action data from DrugBank
- Relevance screening of the retrieved literature
- Any direct clinical or preclinical evidence of itraconazole activity against *Pneumocystis*. Without it, this candidate should not advance to safety screening.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

