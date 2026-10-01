---
layout: default
title: Glecaprevir
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

# Glecaprevir: From Chronic Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is an HCV NS3/4A protease inhibitor, marketed in Canada as MAVIRET together with pibrentasvir for chronic hepatitis C.
The TxGNN model predicts it may be effective for **HIV infectious disease**, with a very high score (99.87%).
The 16 linked clinical trials and 20 publications are almost all HCV studies, some in HIV/HCV-coinfected patients. **None tests anti-HIV efficacy**, so the evidence is still essentially model-based.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from trial content; the Canadian license records list no indication text) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (no HIV efficacy study exists; only HCV trials in HIV-coinfected populations and drug-interaction literature) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, glecaprevir is a direct-acting antiviral (NS3/4A protease inhibitor) that is co-formulated with pibrentasvir (an NS5A inhibitor). Its efficacy in hepatitis C is well established, with pooled SVR12 of about 97.8% in a 2019 meta-analysis.

The prediction most likely reflects proximity in the knowledge graph. Glecaprevir sits near antiviral and protease-inhibitor nodes, which are strongly linked to HIV. Glecaprevir has no established activity against HIV-1 protease, which is structurally different from the HCV NS3/4A protease. The high score should therefore not be read as mechanistic support.

The clinical link is coinfection, not treatment of HIV. Many trials enrolled people living with HIV who also have HCV. These show that glecaprevir/pibrentasvir can be given to this group, and they inform drug-interaction management with antiretrovirals. They do not show any effect on HIV itself.

---

## Clinical Trial Evidence

Sixteen trials are linked. The table lists the nine that mention HIV. All are HCV-focused unless noted.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: efficacy and safety in HCV genotype 1-6 with HIV-1 coinfection (HCV endpoint) |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | Placebo-controlled HCV study in non-cirrhotic Asian adults, with or without HIV coinfection |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | HCV study in Asian adults with compensated cirrhosis, with or without HIV coinfection |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot of DAA regimens (including glecaprevir/pibrentasvir) in recently acquired HCV, with or without HIV |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | 4-week glecaprevir/pibrentasvir for acute HCV, with or without HIV-1 coinfection |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV cure in HIV/HCV-coinfected patients; the endpoint is not HIV control |
| [NCT04189627](https://clinicaltrials.gov/study/NCT04189627) | N/A | Completed | 99 | Real-world study in adolescents in Russia, including an HCV/HIV-coinfected subgroup |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not yet recruiting | 30 | PK and safety of glecaprevir/pibrentasvir started in pregnancy, with or without HIV |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | Completed | 17 | Telemedicine at needle exchanges (buprenorphine/naloxone, HIV PrEP, HCV treatment); a care-delivery study, not an anti-HIV drug test |

---

## Literature Evidence

No RCTs were found. The table lists the most relevant publications, with systematic reviews first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Systematic review / meta-analysis | Int J Antimicrob Agents | 13 studies, 3,082 patients; overall SVR12 97.8% in HCV genotypes 1-6 |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Response to glecaprevir/pibrentasvir in HIV/HCV-coinfected patients in routine practice |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | Pharmacology / DDI analysis | J Infect Dis | Drug interactions between glecaprevir/pibrentasvir and HIV antiretrovirals |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | Overview of glecaprevir/pibrentasvir for chronic HCV |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | HCV protease inhibitor therapy; notes frequent HIV/HCV coinfection |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Review | GMS Infect Dis | Protease inhibitors for HCV; notes HIV/HCV coinfection |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case report | Clin J Gastroenterol | Successful HCV genotype 4a cure with glecaprevir/pibrentasvir in an HIV/HCV-coinfected hemophilia patient |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | Case report | J Prev Med Hyg | Indirect hyperbilirubinemia and jaundice in an HIV-infected patient on glecaprevir/pibrentasvir plus antiretrovirals |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | Viral hepatitis conference summary, including pangenotypic DAAs |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02522470 | MAVIRET |
| 02467550 | MAVIRET |

---

## Safety Considerations

Warnings, contraindications and drug-interaction data are not available in the source record, so please refer to the package insert for safety information.

Two points from the linked literature are relevant to any HIV-related use:
- **Antiretroviral interactions:** Drug-interaction assessment with HIV antiretrovirals is needed (PMID 31504702).
- **Liver enzymes and bilirubin:** One case report describes hyperbilirubinemia and jaundice in an HIV-infected patient on glecaprevir/pibrentasvir plus antiretroviral therapy (PMID 36415300). It was seen with compensated cirrhosis and cytochrome-inhibiting co-medications, so liver monitoring is advisable.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score appears to be a graph artifact. Glecaprevir has no known activity against HIV-1 protease, and the linked trials measure HCV cure in HIV-coinfected people, not HIV control. The other nine predicted indications (HBV, HEV, HAV, animal and rare diseases) are weaker still, and most have no supporting evidence at all.

**To proceed, the following is needed:**
- Mechanism of action data, and in vitro activity of glecaprevir against HIV-1 (for example a protease or antiviral assay)
- Health Canada package insert warnings and contraindications, to allow S1 safety screening
- Confirmation of the approved indication text in the Canadian license records
- If pursued, a preclinical or early-phase study with an HIV-specific endpoint (viral load), not just HCV outcomes in coinfected patients

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

