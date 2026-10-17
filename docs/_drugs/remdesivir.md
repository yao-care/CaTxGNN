---
layout: default
title: Remdesivir
parent: Model Prediction Only (L5)
nav_order: 801
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Remdesivir: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not stated in the Health Canada record"
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia", "Prinzmetal angina", "leprosy", "antithrombin deficiency type 2", "cytomegalovirus infection"]
---

# Remdesivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Remdesivir: From Antiviral Therapy (Original Indication Not Specified) to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is a nucleotide analog antiviral, marketed in Canada as VEKLURY. The Health Canada record compiled for this report does not state its approved indication.
The TxGNN model's top-ranked prediction is **multiple endocrine neoplasia** (score 99.5%), but there are **0 clinical trials** and **0 publications** supporting it. The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada record |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, remdesivir is a nucleotide analog prodrug that inhibits viral RNA-dependent RNA polymerase (RdRp). Its established use is in viral disease, with the literature centred on COVID-19.

The predicted indication, multiple endocrine neoplasia, is a hereditary tumour syndrome (for example MEN1 or RET mutations) with no viral cause. **No mechanistic link could be identified.** The high score reflects graph-based proximity in the knowledge graph, not biological or clinical support.

Other predictions were also reviewed:

- **HIV infectious disease** (score 99.3%, L4): This is the most evidence-rich prediction, but the retrieved literature is almost entirely about COVID-19. HIV replicates via reverse transcriptase and integrase, not RdRp, so direct activity is not established.
- **Cytomegalovirus infection** (score 97.1%, L4): CMV is a DNA virus, so direct activity is not expected. The literature covers CMV co-infection or reactivation in COVID-19 patients, which is context only. It is a research question, not an efficacy signal.
- **Feline AIDS and simian immunodeficiency virus infection**: These are animal diseases predicted through HIV similarity, with no evidence for remdesivir.
- **Leprosy:** The literature describes a leprosy drug (clofazimine) used against coronavirus, which is the reverse of this prediction.
- **Prinzmetal angina, homozygous familial hypercholesterolemia, antithrombin deficiency type 2 and a rare neurodevelopmental disorder:** There is no plausible mechanism and no evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (multiple endocrine neoplasia).

For reference, the only trial found across the predictions relates to HIV:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04385719](https://clinicaltrials.gov/study/NCT04385719) | Phase 2 | Completed | 24 | Pharmacokinetic study in healthy Ugandan volunteers of how tenofovir/lamivudine or atazanavir/ritonavir affect remdesivir blood levels. It is a drug-interaction study, not an HIV efficacy trial. |

---

## Literature Evidence

Currently no related literature is available for the top-ranked prediction (multiple endocrine neoplasia).

For reference, selected publications retrieved for the HIV prediction (all concern COVID-19 rather than HIV treatment):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33264556](https://pubmed.ncbi.nlm.nih.gov/33264556/) | 2021 | RCT | N Engl J Med | WHO Solidarity trial of repurposed antivirals, including remdesivir, in hospitalised COVID-19 patients |
| [38675889](https://pubmed.ncbi.nlm.nih.gov/38675889/) | 2024 | RCT | Viruses | Resistance analysis of the Phase 3 SIMPLE trials. No remdesivir resistance was observed. |
| [35817072](https://pubmed.ncbi.nlm.nih.gov/35817072/) | 2022 | RCT | Lancet Respir Med | Tixagevimab-cilgavimab versus placebo in hospitalised COVID-19 patients receiving remdesivir |
| [34696838](https://pubmed.ncbi.nlm.nih.gov/34696838/) | 2021 | Review | The Enzymes | Mechanisms of nucleotide analogs inhibiting viral RNA replication, comparing SARS-CoV-2 RdRp with HIV reverse transcriptase |
| [34859557](https://pubmed.ncbi.nlm.nih.gov/34859557/) | 2022 | Observational | HIV Med | High frequency of potential drug interactions between antiretrovirals and COVID-19 medications in HIV-positive patients |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02502143 | VEKLURY | Not stated | Not stated |

---

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs. All of the first 20 listed are rated Moderate. Examples include:

- Antibiotics: doxycycline, minocycline, tetracycline, clarithromycin, vancomycin, levofloxacin, kanamycin, neomycin
- Antifungals: amphotericin B, amphotericin B (lipid complex)
- Antidiabetics: acarbose, pioglitazone
- Anabolic steroids: oxandrolone, oxymetholone
- Aminosalicylates: mesalazine, balsalazide, olsalazine
- Others: bupropion, naltrexone, chenodeoxycholic acid

Please refer to the package insert for warnings and contraindications. Its content was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, multiple endocrine neoplasia, has no clinical trials, no literature and no plausible mechanism, so it is supported only by a graph-based score. The other predictions are either veterinary or non-viral diseases with no supporting evidence, or relate to remdesivir only in the context of COVID-19. The CMV question (L4) is the only one worth considering, and then only as a clinical co-infection question.

**To proceed, the following is needed:**
- The Health Canada package insert, to establish the approved indication, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic evidence linking remdesivir to endocrine tumour biology, if this prediction is to be pursued
- Prioritisation of the CMV and HIV predictions for literature review. HIV evidence is currently limited to a pharmacokinetic interaction study, and CMV evidence to co-infection reports in COVID-19.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

