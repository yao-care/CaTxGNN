---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

Using the report structure directly from the Evidence Pack (RIBAVIRIN / DB00811, Taiwan candidate TW-DB00811-multi) — no additional research needed since all required fields are present in the pack itself.

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is a nucleoside antiviral classically used in combination with peginterferon for chronic hepatitis C (HCV), an RNA virus infection. The TxGNN model predicts it may also be effective for **Chronic Hepatitis B Virus Infection**, with a very high similarity score (99.86%) and a large body of supporting trials/literature. However, close review of that evidence shows it comes almost entirely from HBV/HCV **co-infection** studies where ribavirin was treating the HCV component, not HBV itself — so the signal does not currently support real-world repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C, combined with peginterferon (established use referenced throughout the evidence pack; not marketed in Taiwan so no official Taiwan label text exists) |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 (mechanism/preclinical-level; supporting trials are confounded, not HBV-specific) |
| Taiwan Market Status | Not marketed |
| Number of Licenses (Taiwan) | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ribavirin is a guanosine nucleoside analogue. Its established antiviral mechanism works through inhibition of IMPDH, interference with viral RNA-dependent RNA polymerase, and induction of lethal mutagenesis — mechanisms specific to **RNA** viruses such as HCV and RSV. Detailed mechanism-of-action documentation for this candidate is currently a data gap (DG002), but this general mechanism is consistently reflected in the supporting trial and literature evidence collected.

The TxGNN model's top prediction, chronic hepatitis B, is mechanistically discordant with this profile: HBV is a **DNA** virus that replicates via reverse transcription of a cccDNA template, and standard HBV therapy relies on nucleos(t)ide reverse-transcriptase inhibitors or interferon — not ribavirin. When the clinical trial and literature evidence behind this candidate's high score was reviewed in detail, essentially all of it turned out to originate from **HBV/HCV co-infection** studies, where ribavirin (plus peginterferon) was treating the HCV component of a dual infection rather than HBV itself.

This is best understood as a labeling/confounding artifact in the underlying evidence rather than a genuine repurposing signal. The evidence pack itself reflects this: despite a near-maximal similarity score, the candidate is graded only L4 with a "Hold" recommendation. It is a useful reminder that a high model score should never be read as clinical evidence on its own — the actual content of the underlying trials and papers must be checked.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01623336](https://clinicaltrials.gov/study/NCT01623336) | Phase 2/3 | Unknown | 740 | Peginterferon alfa comparator trial; no direct ribavirin-HBV intervention design, and the enrolled population is not clearly restricted to HBV. |
| [NCT01805882](https://clinicaltrials.gov/study/NCT01805882) | Phase 2 | Completed | 229 | Title explicitly describes an anti-HCV combination therapy pilot study, not an HBV indication. |
| [NCT00630058](https://clinicaltrials.gov/study/NCT00630058) | Phase 1 | Completed | 20 | MP-424 + peginterferon alfa-2b + ribavirin triple therapy for genotype 1b hepatitis C. |
| [NCT00493805](https://clinicaltrials.gov/study/NCT00493805) | Phase 4 | Terminated | 59 | Title explicitly targets chronic hepatitis C (CHC) genotype 1 with insulin resistance; unrelated to HBV. |
| [NCT00031343](https://clinicaltrials.gov/study/NCT00031343) | Phase 2 | Completed | 128 | Studies HAART's impact on hepatitis C treatment response in HIV/HCV co-infected patients, not a primary HBV indication. |
| [NCT00630084](https://clinicaltrials.gov/study/NCT00630084) | Phase 4 | Completed | 120 | Pegylated interferon + ribavirin combination therapy; conventional usage context is chronic hepatitis C. |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | Sofosbuvir + GS-5816 (± ribavirin) study in chronic HCV genotypes 1–6; HCV-specific. |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | ABT-493/ABT-530 ± ribavirin efficacy/PK study; drug class is HCV direct-acting antiviral (DAA) development. |
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Completed | 89 | Dose-ranging study of ABT-493/ABT-530 in genotype 1 chronic HCV; HCV drug-development context. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Ombitasvir/Paritaprevir/Ritonavir/Dasabuvir + ribavirin (AbbVie 3D regimen) for decompensated cirrhosis in chronic HCV; unrelated to HBV. |

*Note: These are the 10 trials with explicit relevance grading in the evidence pack (all graded "C" — low relevance to HBV). A further ~40 trials returned by the search were not yet graded ("pending") and are omitted here; based on their titles, the large majority also appear to be HCV-focused.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | Reviews HCV/HBV co-infection management; recommends peginterferon + ribavirin for HCV-dominant co-infected patients, not HBV monoinfection. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Updates on treatment/outcomes of dual chronic HCV/HBV infection; ribavirin's role is again tied to the HCV component. |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | "Treatment of HBV and HCV co-infection: still a challenge for the hepatologist" — no abstract available; title confirms co-infection framing. |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatol Int | Discusses viral interaction dynamics in dual HBV/HCV infection under treated vs. untreated settings. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Reviews treatment options for chronic HBV and HCV in children as separate, standardized regimens. |
| [15864105](https://pubmed.ncbi.nlm.nih.gov/15864105/) | 2005 | Review | Curr Opin Infect Dis | Overview of HBV vaccination, HCV transmission, and natural history/treatment efficacy in children. |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | Notes that interferon ± ribavirin was the prototype therapy for both HBV and HCV, but DAAs now differ by virus; HBV persists (cccDNA) even after treatment. |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review/Genetic | Semin Liver Dis | Reviews host genetic determinants of HBV and HCV disease outcome; not a treatment-efficacy study. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Genetic association study | World J Gastroenterol | IL28B polymorphism is linked to peginterferon+ribavirin response in HCV; its relevance to HBV outcomes (e.g., HBeAg seroconversion) remains unresolved. |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Genetic association study | Curr Opin Virol | IL28B genotype affects treatment-induced clearance in HCV (with peginterferon/ribavirin); effect on HBV is a separate, less-established association. |

## Taiwan Market Information

Ribavirin is currently **not marketed in Taiwan** — the evidence pack contains no license records (`total_licenses: 0`), so no product/DIN table can be produced.

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are all currently data gaps — DG001 flags TFDA label warnings/contraindications as a **blocking** gap that must be resolved before any safety pre-assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score (99.86%) for the top candidate, the supporting clinical trials and literature are almost entirely drawn from HBV/HCV co-infection studies where ribavirin was treating the HCV component — not genuine HBV-specific evidence. The remaining nine predicted indications in this pack have little or no supporting evidence (several show zero trials/literature and no plausible mechanistic link), and one (hepatic porphyria) is actually associated with ribavirin/interferon-*induced* porphyria cutanea tarda — a safety signal, not a treatment opportunity. Separately, blocking safety data (TFDA warnings/contraindications, DG001) and MOA documentation (DG002) are both missing, which alone prevents progression past S0.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to resolve blocking gap DG001
- Verified mechanism-of-action documentation from DrugBank to resolve DG002
- Re-run evidence collection with HBV/HCV co-infection studies explicitly excluded, to test whether any genuine HBV-specific signal remains
- An independent mechanistic plausibility review of using an RNA-virus-targeted agent (ribavirin) against a DNA virus (HBV) before further investment
- If revisited, the hepatic porphyria association should be reframed as a drug-safety/label item (risk of inducing porphyria cutanea tarda), not pursued as a repurposing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

