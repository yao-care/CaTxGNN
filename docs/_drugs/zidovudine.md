---
layout: default
title: Zidovudine
parent: Model Prediction Only (L5)
nav_order: 983
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Zidovudine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Zidovudine is a nucleoside reverse transcriptase inhibitor (NRTI) used against HIV. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (feline AIDS)**. **0 clinical trials** and **20 publications** are linked to this prediction, and the publications are almost entirely animal and in vitro studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection (inferred from the drug class; the Canadian licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical and animal-model evidence only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zidovudine is an NRTI. Its efficacy in HIV infection is established. Mechanistically, it may be applicable to feline immunodeficiency virus (FIV) infection.

FIV is a lentivirus that causes an AIDS-like disease in cats. Its reverse transcriptase is similar enough to that of HIV-1 that FIV is used as a model for testing reverse transcriptase inhibitors. This is why the knowledge graph links the drug to the disease.

Two caveats apply. First, the supporting literature is veterinary and preclinical. The results are mixed. Zidovudine lowered plasma virus titers and prevented early viremia in cats, but it did not prevent infection or alter the chronic course. Second, feline AIDS is not a human disease. The prediction therefore says little about new human uses of zidovudine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1666108](https://pubmed.ncbi.nlm.nih.gov/1666108/) | 1991 | Review | J Am Vet Med Assoc | Review of chemotherapy for FIV infection (no abstract available) |
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | Animal model study | Antimicrob Agents Chemother | FIV reverse transcriptase examined for similarity to HIV-1 reverse transcriptase, supporting FIV as a model for reverse transcriptase-targeted chemotherapy |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Animal study | J Acquir Immune Defic Syndr | Prophylactic zidovudine prevented early viremia and lymphocyte decline in FIV-inoculated cats but did not prevent primary infection |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Animal study | Arch Virol | Zidovudine lowered plasma virus titers at 2 weeks but not later, and did not prevent infection |
| [7618256](https://pubmed.ncbi.nlm.nih.gov/7618256/) | 1995 | Animal study (SCID-feline mice) | Vet Immunol Immunopathol | AZT reduced provirus burden and enhanced humoral immune function in FIV-inoculated mice |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | In vitro and in vivo study | Vet Immunol Immunopathol | AZT/3TC was additive to synergistic against FIV in primary PBMC but not in chronically infected T-cell lines |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | In vitro study | Antiviral Res | Zidovudine, lamivudine and abacavir combination suppressed FIV replication in vitro |
| [22816034](https://pubmed.ncbi.nlm.nih.gov/22816034/) | 2012 | Animal study | Viruses | Fozivudine tidoxil, a zidovudine-related compound, given as a single agent during acute FIV infection did not alter chronic infection |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Follow-up study | J Feline Med Surg | Long-term antiretroviral therapy, starting with zidovudine, was followed for 5–6 years in FIV-infected cats |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Animal study (FeLV, a related retrovirus, not FIV) | Antimicrob Agents Chemother | Alpha interferon plus AZT was tested in presymptomatic cats with FeLV-induced immunodeficiency syndrome |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 1946323 | APO-ZIDOVUDINE |
| 1902652 | RETROVIR (AZT) |
| 1902644 | RETROVIR (AZT) |
| 2414414 | AURO-LAMIVUDINE/ZIDOVUDINE |
| 2375540 | APO-LAMIVUDINE-ZIDOVUDINE |

Six licences are on record. The five main ones are shown above. Dosage form and approved-indication text were not available in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the supporting evidence is limited to veterinary and preclinical studies with mixed results. There are no clinical trials, and feline AIDS is not a human indication. Zidovudine's marketed use in Canada is unaffected by this prediction.

Two other predictions for this drug have more evidence: congenital HIV (rank 5) and AIDS-related complex (rank 6). Both look like existing HIV uses rather than true repurposing. Current guidelines favour combination regimens over zidovudine alone.

**To proceed, the following is needed:**
- A decision on whether a veterinary indication is in scope, since it falls outside human drug repurposing
- The Health Canada product monograph (warnings, contraindications, approved indications) to complete safety screening
- Mechanism of action data from DrugBank
- If the human HIV-related predictions are pursued, a check of the original labelled indications to confirm whether they are on-label uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

