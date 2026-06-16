---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 1
---

# Eltrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Eltrombopag: From Immune Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is a thrombopoietin receptor (TPO-R) agonist globally approved for immune thrombocytopenia (ITP) and related haematological conditions, though it is not currently marketed in Canada.
The TxGNN model predicts it may have utility in **HIV Infectious Disease** — specifically HIV-associated thrombocytopenia — supported by **5 clinical trials** (all HCV-related, providing indirect mechanistic support) and **10 publications**, of which 2 case reports and 1 case series directly document eltrombopag use in HIV patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Immune thrombocytopenia (ITP); globally established but not licensed in Canada |
| Predicted New Indication | HIV Infectious Disease (HIV-associated thrombocytopenia) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eltrombopag is a non-peptide small molecule that binds to the transmembrane domain of the thrombopoietin receptor (TPO-R / c-Mpl) on megakaryocytes and their precursors. This binding stimulates their proliferation and differentiation, thereby increasing platelet production through a pathway distinct from — and additive to — endogenous thrombopoietin. This mechanism is well-characterised and forms the basis of its approved indications in ITP and severe aplastic anaemia.

HIV infection causes thrombocytopenia through two converging pathways: immune-mediated platelet destruction driven by autoantibodies and molecular mimicry between viral antigens and platelet surface proteins, and direct bone marrow suppression by the virus that impairs megakaryocyte maturation. The net result is a chronically low platelet count that can increase bleeding risk and complicate the management of opportunistic infections — particularly those requiring antivirals or invasive procedures. Since impaired platelet production is a core mechanism, TPO-R agonism is mechanistically positioned to compensate by driving megakaryocyte expansion, much as it does in ITP or aplastic anaemia. The clinical parallel with HCV-associated thrombocytopenia (where eltrombopag has demonstrated efficacy in Phase 3 trials) further supports biological plausibility.

A second mechanistic dimension adds both potential and uncertainty: a 2020 FDA-approved drug library screen (PMID 32977702) identified eltrombopag as a modulator of HIV-1 proviral transcription. This raises the possibility that the drug could influence viral latency — conceivably suppressing or inadvertently reactivating latent HIV. The direction and clinical significance of this effect remain uncharacterised, representing an active safety signal that must be resolved before HIV-specific repurposing can be advanced.

---

## Clinical Trial Evidence

All 5 identified trials were designed for **HCV-associated or liver disease–related thrombocytopenia**, not HIV. They provide indirect mechanistic support by demonstrating that eltrombopag can raise and maintain platelet counts in the setting of chronic viral infection — a pathophysiological context broadly analogous to HIV-associated thrombocytopenia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | ENABLE-1: Eltrombopag vs placebo in HCV-related thrombocytopenia during Peg-IFNα-2b + ribavirin; primary endpoint was sustained virological response (SVR); largest pivotal trial for virus-associated thrombocytopenia |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | ENABLE-2: Identical design with Peg-IFNα-2a arm; together with ENABLE-1, demonstrates eltrombopag's ability to maintain platelets during antiviral therapy in a chronic viral infection context |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Eltrombopag to reduce platelet transfusions in chronic liver disease patients undergoing elective invasive procedures; terminated early — reason for early termination not specified in available summary and warrants verification |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | Open-label Phase 2 in HCV cirrhosis with thrombocytopenia (SB-497115 = eltrombopag developmental code); assessed platelet elevation to enable Peg-IFN + ribavirin initiation |
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Long-term rollover safety extension of a prior HCV trial; extremely small n, contributes long-term tolerability data only |

> No HIV-specific clinical trials were identified. The shared mechanism of virus-driven thrombocytopenia provides indirect bridging evidence, but direct clinical validation in HIV cohorts is absent from the current evidence base.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematol Oncol Clin North Am | HIV, HCV, and H. pylori as infectious causes of chronic immune thrombocytopenia; treatment of the primary infection often resolves thrombocytopenia; contextualises TPO-R agonist rationale |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Semin Hematol | Therapeutic strategies for infection-related immune thrombocytopenias including HIV; reviews mechanism and therapeutic options including TPO pathway |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Registry / Cohort | Platelets | Danish national registry of TPO-RA use 2009–2011; includes off-label use in secondary ITP; provides real-world safety and efficacy signals outside ITP |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Clinical Cohort | Intern Med J | TPO-RA use in ITP of <6 months duration; short-term ITP cohort relevant to acute or early HIV-associated thrombocytopenia management |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case Series | J Int Assoc Provid AIDS Care | Eltrombopag and romiplostim used as salvage therapy in refractory HIV-associated ITP after HAART optimisation; most directly relevant publication — documents clinical outcomes in HIV-positive patients |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro Screen | Viruses | FDA-approved drug library screen identifies eltrombopag as a modulator of HIV-1 proviral transcription; raises open questions about viral latency and reactivation risk |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case Report | AIDS (London) | Successful eltrombopag use without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia; single patient, positive outcome |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case Report | AIDS (London) | First reported eltrombopag use in severe aplastic anaemia (SAA) associated with HIV; trilineage haematological response and possible immunomodulatory effect (decreased Th1/Th17, increased T-regulatory cells) |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case Report | Farm Hosp | Eltrombopag for HCV-related thrombocytopenia (two cases); cross-viral-infection utility supports generalisation to other virus-associated thrombocytopenias |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case Report | J Coll Physicians Surg Pak | HBV-associated severe thrombocytopenia with megaloblastic anaemia; contextualises virus-induced megakaryocyte suppression across different viral infections |

---

## Safety Considerations

Safety data for eltrombopag is not available in the current Canadian regulatory dataset. This is classified as a **blocking data gap** that prevents S1 safety screening.

Please refer to the full product monograph for complete safety information. The following specific concerns should be prioritised for investigation:

- **Drug interactions with antiretrovirals**: Eltrombopag chelates polyvalent cations and is subject to CYP1A2, UGT1A1, BCRP, and OATP1B1 interactions. Many antiretrovirals — particularly integrase strand transfer inhibitors (e.g., dolutegravir, bictegravir) — share chelation-related interaction profiles; co-administration timing and separation may be critical.
- **Hepatotoxicity**: Eltrombopag carries an established hepatotoxicity warning in approved markets. HIV-positive patients frequently have concurrent hepatic involvement (HBV/HCV co-infection, antiretroviral hepatotoxicity), making liver function monitoring particularly important.
- **HIV-1 proviral transcription modulation**: The in vitro finding (PMID 32977702) raises unresolved safety questions about whether eltrombopag could disrupt viral latency in patients on suppressive HAART. This signal must be characterised before clinical use in this population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for eltrombopag in HIV-associated thrombocytopenia is biologically coherent — TPO-R agonism directly addresses the impaired platelet production component of HIV-related cytopenias — and is supported by real-world case reports and case series. However, the complete absence of Canadian regulatory safety data, the lack of any HIV-specific controlled trial, and the unresolved question of eltrombopag's effect on HIV-1 proviral transcription collectively prevent advancement beyond exploratory research. A Hold decision is appropriate until blocking data gaps are resolved.

**To proceed, the following is needed:**

- **Blocking — Safety data retrieval**: Obtain the eltrombopag product monograph (from FDA, EMA, or Health Canada if available for reference) to complete the S1 safety screen covering key warnings, contraindications, and DDI profile with antiretrovirals
- **Mechanistic clarification**: Determine the direction and clinical significance of eltrombopag's effect on HIV-1 proviral transcription (follow-up to PMID 32977702); assess whether this poses a viral reactivation risk in HAART-suppressed patients
- **DDI modelling**: Conduct pharmacokinetic interaction assessment between eltrombopag and the most commonly used antiretroviral combinations, with particular attention to integrase inhibitors and chelation-related interactions
- **Systematic literature review**: Perform a formal systematic search of all published HIV-specific case reports, case series, and cohort studies of TPO-R agonists to quantify the available evidence base and assess for publication bias
- **Regulatory pathway mapping**: Eltrombopag has existing approvals in ITP, aplastic anaemia, and HCV-associated thrombocytopenia across multiple jurisdictions; if mechanistic and safety data support progression, a label extension strategy for HIV-associated thrombocytopenia should be scoped
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

