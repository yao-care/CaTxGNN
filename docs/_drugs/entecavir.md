---
layout: default
title: Entecavir
parent: Moderate Evidence (L3-L4)
nav_order: 332
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Entecavir: predicted new indication Chronic hepatitis C virus infection (evidence level L4). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "ENTECAVIR"
predicted_indications: ["chronic hepatitis C virus infection", "hepatitis B virus infection", "HIV infectious disease", "hepatitis C virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
---

# Entecavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is an antiviral drug originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but the evidence is weak: **2 clinical trials** and **20 publications** are linked to this prediction, and none shows entecavir treating hepatitis C. They address HBV in patients who have both infections.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, entecavir is a guanosine nucleoside analogue. Inside cells it is converted to its triphosphate form, which competes with the natural nucleotide dGTP and blocks the HBV polymerase.

Hepatitis B and C are both chronic viral liver infections, so the model's network proximity is understandable. The mechanisms differ, though. HCV replicates with its own RNA-dependent RNA polymerase (NS5B), and entecavir has no known direct activity against it. The high score most likely reflects how closely the two diseases sit in the knowledge graph, not a real antiviral effect on HCV.

The one plausible clinical link is co-infection. In people with both HBV and HCV, entecavir can suppress HBV replication or prevent HBV reactivation during HCV direct-acting antiviral (DAA) therapy. That is an HBV benefit, not treatment of HCV.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Tracks HBV reactivation during HCV DAA therapy in HCV/HBV co-infected patients. It does not test entecavir against HCV. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Not applicable | Unknown | 60 | Tests whether prophylactic nucleos(t)ide analogues, with 12 vs 24 weeks of prophylaxis, prevent HBV reactivation in co-infected patients on DAA therapy. This supports HBV prophylaxis, not HCV efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | RCT | Clin Gastroenterol Hepatol | Entecavir prevents HBV reactivation during DAA treatment of HCV/HBV dual infection (an HBV-protective effect). |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV co-infection. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and future prospects for chronic hepatitis B and C. |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation in anti-HCV-positive chronic hepatitis B patients (66 patients) on nucleos(t)ide analogue therapy for HBV. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Not classified | Dig Dis | Incidence and course of HBV reactivation in patients treated with DAAs for hepatitis C. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Not classified | J Gastroenterol Hepatol | HBV reactivation risk in chronic hepatitis C patients with HBV infection treated with DAAs. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Not classified | Clin Res Hepatol Gastroenterol | Present and future management of viral hepatitis B and C in children. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Not classified | World J Hepatol | Management of hepatitis B and C before and after liver and kidney transplantation. Entecavir and tenofovir are described for HBV. |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Not classified | World J Gastroenterol | HBV infection and alcohol consumption as causes of hepatocellular carcinoma. |

## Canada Market Information

Entecavir has 10 valid single-ingredient licenses in Canada, and no cancelled ones. The first 5 are listed below. Dosage form and approved-indication text were not available for these licenses.

| DIN | Product Name |
|---------|------|
| 02485907 | MINT-ENTECAVIR |
| 02448777 | AURO-ENTECAVIR |
| 02396955 | APO-ENTECAVIR |
| 02282224 | BARACLUDE |
| 02467232 | JAMP ENTECAVIR |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** impaired renal function, fatty liver disease, non-alcoholic steatohepatitis, and lactic acidosis.
- **Monitoring points from the evidence review:** lactic acidosis, renal function, thrombocytopenia (a case report exists, PMID 34823407), and hepatitis flares after stopping treatment.
- **Drug interactions:** 44 interactions were recorded, and all those shown are Moderate. The main ones are:
  - Acid-suppressing H2 blockers: famotidine, ranitidine, cimetidine.
  - Metformin.
  - Potentially nephrotoxic agents: amphotericin B (several formulations), vancomycin, kanamycin, neomycin, polymyxin B.
  - Levofloxacin, amoxicillin, and orlistat.
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is very high (99.98%), but there is no evidence that entecavir treats hepatitis C. Entecavir targets the HBV polymerase, not HCV NS5B.
- The linked trials and publications concern HBV reactivation in HBV/HCV co-infected patients, which is an HBV indication.
- HCV already has highly effective, specific direct-acting antivirals, so there is little need for this repurposing.

**To proceed, the following is needed:**
- In vitro evidence of anti-HCV activity, such as replicon assays.
- Detailed mechanism of action data to support or refute a link to HCV.
- If the co-infection use is of interest, a separate evaluation framed as HBV reactivation prophylaxis during HCV DAA therapy, not HCV treatment.
- The package insert warnings and contraindications from Health Canada, which were missing from the data compiled for this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

