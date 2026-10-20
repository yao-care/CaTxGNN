---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 803
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ribavirin: predicted new indication Chronic hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
monitor_inn: "RIBAVIRIN"
predicted_indications: ["chronic hepatitis B virus infection", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related mediastinitis", "IgG4-related mesenteritis"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is an antiviral originally used for chronic hepatitis C virus infection and respiratory syncytial virus infection.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**,
with **15 clinical trials** and **20 publications** compiled for this direction. Most of this evidence is indirect, because it concerns hepatitis C or combination regimens rather than ribavirin's own effect on hepatitis B.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection; respiratory syncytial virus infection (from the knowledge graph; the Canadian licence has no indication text) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (as assigned in the data; see the caveat below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

**Evidence level caveat:** The L1 label rests on the count of Phase 3 trials. Only one Phase 3 trial (NCT00114361) directly tests ribavirin in chronic hepatitis B, and it has no clear ribavirin-free comparator in the data provided. I therefore treat the evidence as weaker than a typical L1.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, ribavirin is a guanosine nucleoside analogue with broad antiviral activity. Its proposed actions include inhibiting IMPDH, depleting GTP pools, and modulating the immune response.

Hepatitis B is a DNA virus, so direct antiviral activity is limited. Any benefit in chronic hepatitis B appears to come mainly from immunomodulation when ribavirin is combined with interferon. In HBV/HCV co-infection, ribavirin acts on the HCV component. Current hepatitis B standards of care, nucleos(t)ide analogues and peginterferon, are superior, and ribavirin is not recommended as monotherapy.

The prediction is therefore plausible as an add-on or immunomodulatory strategy, not as a stand-alone antiviral.

## Clinical Trial Evidence

The table lists the 10 most relevant of the 15 trials compiled. Trials directly in HBV or HBV-containing populations come first.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | Peginterferon alfa-2a plus ribavirin vs peginterferon alone in HBeAg-negative chronic HBV (PARC study); the most directly relevant trial |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Pilot of ribavirin added to nucleos(t)ide analogue therapy to enhance HBV antiviral activity through immune modulation |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot of interferon alpha-2b plus ribavirin in chronic hepatitis B |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a plus ribavirin in HCV/HBV co-infection and chronic hepatitis C |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pilot of pegylated interferon alfa-2b plus ribavirin in dual hepatitis B and D infection |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Direct-acting antivirals plus ribavirin in HCV with decompensated cirrhosis; indirect for HBV |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon plus ribavirin and IL-28B expression in HCV genotype 1; indirect |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | Completed | 506 | Surveillance and treatment programme in chronic hepatitis C; indirect |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon and ribavirin in HCV genotypes 2/3; terminated early, indirect |
| [NCT01309932](https://clinicaltrials.gov/study/NCT01309932) | Phase 2 | Completed | 165 | Peginterferon lambda with ribavirin plus a direct-acting antiviral in HCV; indirect |

Most remaining trials are HCV studies in which ribavirin is a background or comparator agent.

## Literature Evidence

The compiled literature is mostly narrative reviews of HBV/HCV co-infection. It contains no randomised trials of ribavirin in HBV.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection; peginterferon plus ribavirin was previously recommended for patients with positive HCV RNA |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment and outcomes of dual HCV/HBV infection; viral load guides therapy |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Review | Nihon Rinsho | HCV-HBV infection; peginterferon alpha-2b plus ribavirin is the most effective initial HCV regimen |
| [16550038](https://pubmed.ncbi.nlm.nih.gov/16550038/) | 2006 | Review | Curr Opin Gastroenterol | Update on viral hepatitis treatment and prevention |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and HBV infection outcomes |
| [11929032](https://pubmed.ncbi.nlm.nih.gov/11929032/) | 2002 | Review | Indian J Pediatr | Management of chronic HBV and HCV infections |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | Prevention of hepatocellular carcinoma in chronic hepatitis B and C |
| [11005078](https://pubmed.ncbi.nlm.nih.gov/11005078/) | 2000 | Review | J R Coll Physicians Lond | Update on viral hepatitis |
| [38092311](https://pubmed.ncbi.nlm.nih.gov/38092311/) | 2024 | Preclinical/Mechanistic | Cell Mol Gastroenterol Hepatol | Gut microbiota and chronic hepatitis B progression; not about ribavirin |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02170140 | VIRAZOLE | Not listed | Not listed |

## Safety Considerations

No package-insert warnings or contraindications were available in the compiled data. Please refer to the package insert for safety information. The following items come from the knowledge graph and drug-interaction data.

- **Possible contraindicated conditions (knowledge graph, not label text):** The graph links ribavirin to contraindication with the following conditions.
  - Blood disorders: anaemia (including haemolytic anaemia and sickle cell anaemia), haemoglobinopathy and pancytopenia.
  - Heart and vascular disease: myocardial infarction, coronary artery disease and atherosclerosis.
  - Lung disease: COPD, asthma, interstitial lung disease and sarcoidosis.
  - Liver, pancreas and kidney disease: cirrhosis of the liver, autoimmune hepatitis, pancreatitis and impaired renal function.
  - Other: periodontitis.
- **Drug interactions:** The interaction screen returned 100 interacting drugs, but the severity level is "Unknown" for all of those listed. Examples include metformin, glimepiride, morphine, prednisone, amphotericin B, omeprazole and pantoprazole. Interaction severity needs to be verified against the label.
- **Reported harms in related literature:** Case reports describe porphyria cutanea tarda emerging during peginterferon/ribavirin therapy, and pulmonary granulomatosis during interferon/ribavirin treatment. Ribavirin-induced haemolysis is a known concern.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, and one Phase 3 trial tested ribavirin plus peginterferon in HBeAg-negative chronic hepatitis B. However, ribavirin has limited direct activity against HBV and any contribution beyond interferon is unproven. Current nucleos(t)ide analogue and peginterferon standards are superior. Safety data from the Canadian label are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Results of NCT00114361, specifically the effect of adding ribavirin versus peginterferon alone
- Outcomes of the pilot trial of ribavirin added to nucleos(t)ide analogue therapy (NCT03759782)
- Health Canada package-insert warnings and contraindications for VIRAZOLE (a blocking gap)
- Mechanism-of-action data from DrugBank to support the immunomodulation hypothesis
- A safety plan for haemolytic anaemia, cardiovascular and pulmonary risk, and teratogenicity precautions, using the label
- Verification of the severity of the listed drug interactions

**Other predicted indications:** The remaining nine predictions (for example idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, hepatic porphyria and the IgG4-related conditions) have no supporting trials and no plausible mechanism. For hepatic porphyria, the literature suggests ribavirin may trigger porphyria cutanea tarda rather than treat it. All are rated Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

