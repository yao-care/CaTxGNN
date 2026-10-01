---
layout: default
title: Rifabutin
parent: High Evidence (L1-L2)
nav_order: 798
evidence_level: L1
indication_count: 10
---

# Rifabutin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Rifabutin: From Antimycobacterial Use (Original Indication Not Recorded) to HIV Infectious Disease

## One-Sentence Summary

Rifabutin is a rifamycin antibiotic that acts against mycobacteria. The Canadian license record in this dataset does not state its original indication.
The TxGNN model predicts it may be useful in **HIV infectious disease**, with **39 clinical trials** and **20 publications** linked to this prediction.
The supported benefit is against HIV-associated mycobacterial co-infection (MAC and tuberculosis), not against HIV replication. This is probably not true repurposing, because MAC prophylaxis in advanced HIV is a known labeled use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian license data (MAC prophylaxis in advanced HIV is a known labeled use per the analysis) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured drug record. Based on the mechanistic analysis, rifabutin inhibits bacterial DNA-dependent RNA polymerase (rpoB). This action targets *Mycobacterium avium* complex (MAC) and *M. tuberculosis*, the main opportunistic pathogens in advanced HIV. It has no direct activity against HIV.

The link between the original use and the predicted indication is therefore patient population, not viral biology. People with advanced HIV are at high risk of MAC and tuberculosis, and rifabutin is used to prevent or treat these infections. Several completed Phase 3 trials in AIDS patients tested rifabutin for MAC prevention or treatment.

Rifabutin also induces CYP3A4, which causes significant interactions with protease inhibitors and other antiretrovirals, so dose adjustment is required. Even so, it is often preferred over rifampicin in patients on protease inhibitor–based antiretroviral therapy, because it induces these enzymes less strongly.

---

## Clinical Trial Evidence

The prediction has 39 linked trials. The 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Three-arm comparison of clarithromycin/ethambutol with rifabutin 450 mg, rifabutin 300 mg, or placebo for MAC bacteremia in AIDS; the primary outcome is a ≥2-log CFU reduction sustained to week 16 |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Clarithromycin vs rifabutin vs the combination for preventing MAC bacteremia in HIV patients with CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and rifabutin, alone and combined, for preventing disseminated MAC in HIV; also compares daily vs weekly fluconazole |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Two clarithromycin doses plus ethambutol and either rifabutin or clofazimine for disseminated MAC in AIDS |
| [NCT00002080](https://clinicaltrials.gov/study/NCT00002080) | Not labeled | Completed | N/A | Treatment IND providing rifabutin to prevent or delay MAC bacteremia in HIV patients with CD4 ≤200 |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Not labeled | Completed | 750 | Double-blind, placebo-controlled trial of rifabutin monotherapy to prevent MAC bacteremia in AIDS (CD4 ≤200) |
| [NCT00002343](https://clinicaltrials.gov/study/NCT00002343) | Phase 4 | Completed | 200 | PK/PD-guided rifabutin dosing, alone or with ethambutol, for MAC prophylaxis in AIDS (CD4 ≤100) |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | Completed | 246 | Clarithromycin combined with rifabutin, ethambutol, or both for disseminated MAC in AIDS |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Not labeled | Completed | 215 | TBTC Study 23: failure and relapse rates with an intermittent rifabutin-based regimen for HIV-related tuberculosis |
| [NCT03478033](https://clinicaltrials.gov/study/NCT03478033) | Not labeled | Unknown | 230 | Prospective cohort comparing rifampicin- and rifabutin-containing TB regimens in HIV/AIDS with pulmonary TB |

Many of the other linked trials are Phase 1 drug-interaction or pharmacokinetic studies (for example with maraviroc, cabotegravir, indinavir, and dolutegravir). They inform interaction guardrails rather than efficacy.

---

## Literature Evidence

The prediction has 20 linked publications. No randomized controlled trial publication was identified; the 10 most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety and efficacy of rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir-based ART; an earlier pediatric study had treatment-limiting neutropenia in 2 of 6 children |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort/PK | J Antimicrob Chemother | Rifabutin pharmacokinetics and safety in TB/HIV-coinfected children on lopinavir/ritonavir second-line ART; an earlier study was stopped early for severe neutropenia |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | Cohort/PK | J Antimicrob Chemother | Short-term safety and PK of rifabutin with lopinavir/ritonavir in young HIV-infected children |
| [32979587](https://pubmed.ncbi.nlm.nih.gov/32979587/) | 2020 | Retrospective observational | Int J Infect Dis | Whether co-administering tenofovir alafenamide and rifabutin loses HIV-1 suppression, despite concern that rifabutin lowers TAF absorption |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | Population PK analysis | J Antimicrob Chemother | Pooled analysis of rifabutin–protease inhibitor interactions to predict rifabutin doses achieving recommended exposure in HIV-associated TB |
| [20660678](https://pubmed.ncbi.nlm.nih.gov/20660678/) | 2010 | Randomized PK crossover | Antimicrob Agents Chemother | Darunavir/ritonavir plus rifabutin interaction study in HIV-negative healthy volunteers |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK model | Br J Clin Pharmacol | Population PK of dolutegravir with rifabutin 300 mg daily, as a possible alternative to rifampicin |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectr | Overview of TB associated with HIV infection |
| [21406051](https://pubmed.ncbi.nlm.nih.gov/21406051/) | 2011 | Review | Infect Disord Drug Targets | Management of active TB in the HIV era, including antiretroviral–rifamycin drug interactions |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | Review | Clin Pharmacokinet | Clinical PK of rifabutin and the demonstrated effectiveness of MAC prophylaxis in HIV-positive patients with low CD4 counts |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2063786 | MYCOBUTIN | Not recorded | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: Rifabutin induces CYP3A4, which creates significant interactions with protease inhibitors and other antiretrovirals, so dose adjustment is required. The interaction database query returned no entries, so the evidence above comes from the trials and publications, not a formal interaction list.
  - Co-administration with tenofovir alafenamide has raised concern about reduced absorption.
  - Interaction studies exist with dolutegravir, darunavir/ritonavir, and lopinavir/ritonavir.
- **Neutropenia in children**: Severe or treatment-limiting neutropenia has been reported in children receiving rifabutin with lopinavir/ritonavir.
- **Uveitis**: Rifabutin-associated uveitis has been reported, including in an HIV-infected child.

Please refer to the package insert for the full list of warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials in AIDS patients support rifabutin for preventing and treating MAC, so the evidence level is L1. The benefit is limited to HIV-associated mycobacterial co-infection and does not extend to HIV itself. Significant drug interactions with antiretrovirals require dose adjustment.

**To proceed, the following is needed:**
- Canadian package insert warnings and contraindications (health authority labeling)
- Confirmation of the original labeled indication, to clarify whether this is true repurposing
- Structured mechanism-of-action data from DrugBank
- A dose-adjustment and interaction-management plan for co-administration with protease inhibitors and other antiretrovirals
- A neutropenia monitoring plan, especially for pediatric use

**Other predicted indications (for reference):** Leprosy is a research question, supported only by preclinical and in vitro work. All other predictions remain on Hold because they have no supporting evidence or a mechanistic link: multiple endocrine neoplasia, sclerosing cholangitis, the rare neurodevelopmental disorder, conjunctivitis (the literature points to an adverse effect), endocarditis, pneumocystosis, and the feline and simian immunodeficiency indications.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

