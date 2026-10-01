---
layout: default
title: Tocilizumab
parent: Model Prediction Only (L5)
nav_order: 914
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is an interleukin-6 receptor (IL-6R) antibody whose main use in the supplied literature is rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, with **9 clinical trials** and **19 publications** retrieved. Only 2 of those trials test tocilizumab directly in this disease, and both were terminated early.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (taken from the literature, because the Canadian license records contain no indication text) |
| Predicted New Indication | Ankylosing spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 as assigned in the Evidence Pack. Caution: both direct Phase 3 trials are registered as Terminated, not Completed, so this is a lenient reading. |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Based on the literature, tocilizumab is a humanized monoclonal antibody against the IL-6 receptor. Its efficacy in rheumatoid arthritis is established, and it is also used in juvenile idiopathic arthritis and giant cell arteritis. IL-6 is elevated in axial spondyloarthritis, and the knowledge graph links ankylosing spondylitis to other inflammatory joint diseases treated with the drug.

The mechanistic case is weak, however. IL-6 blockade is not a validated driver pathway in ankylosing spondylitis, where TNF and IL-17 are the established targets. The two direct randomized Phase 3 trials were terminated, which can indicate lack of efficacy or futility. The Evidence Pack provides no outcome data, so this must be checked against the published results. The very high model score (99.99%) is not matched by a clear clinical signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | Placebo-controlled RCT of tocilizumab 8 or 4 mg/kg IV in AS patients with inadequate response to TNF antagonists; outcomes need verification |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 3 | Terminated | 306 | Phase 2/3 placebo-controlled RCT in NSAID-failure, TNF-naïve AS patients, with signs and symptoms and structural damage endpoints |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2500 | Cytokine and biomarker profiling cohort in systemic inflammatory diseases; no efficacy endpoint |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10000 | Korean biologics registry (RA, AS, PsA); observational safety data |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab on T follicular helper cells, apparently in RA |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Peri-operative immunosuppressant management in rheumatology patients; not an efficacy study |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Bayesian randomized trial in Takayasu arteritis (secukinumab); not tocilizumab in AS |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1431 | Real-world observatory of an infliximab biosimilar; different drug |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750000 | Registry on incident immune-mediated diseases after biologics; not efficacy evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT report | Ann Rheum Dis | Short-term symptomatic efficacy of tocilizumab in AS from the BUILDER-1 and BUILDER-2 placebo-controlled trials; results should be read directly from the paper |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic review / network meta-analysis | Medicine | Comparative effectiveness of biologic regimens for AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis (safety) | Clin Rheumatol | Risk of serious infections with biologics in AS and non-radiographic axSpA |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | Short review of IL-6 antagonism in AS |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | Alternatives for AS patients refractory to TNF inhibition |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Review (infection risk) | Expert Rev Clin Immunol | Infection risk of biologics versus non-biologics in inflammatory arthritis |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporos Int | Systemic bone effects of biologics in RA and AS |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Review | Front Immunol | Tuberculosis risk, screening and preventive therapy in patients on biologics |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case report | Front Med | Two cases of AA amyloidosis in AS successfully treated with tocilizumab |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case report | Joint Bone Spine | Tocilizumab in a patient with AS and Crohn's disease refractory to TNF antagonists |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2350092 | ACTEMRA |
| 2350114 | ACTEMRA |
| 2552450 | TYENNE |
| 2552469 | TYENNE |
| 2562030 | AVTOZMA |

Dosage form and approved indication text are not provided in the license records. The five products above are 5 of the 15 DINs on file.

---

## Safety Considerations

Safety fields (key warnings, contraindications, drug interactions) are empty in the Evidence Pack. Please refer to the package insert for safety information.

The retrieved literature repeatedly raises the following concerns. They come from published reviews and case reports, not from product labeling:
- Serious infection, including tuberculosis, with biologic therapy (PMIDs 29290076, 31852268, 39963138).
- Rare case reports of tocilizumab-associated vasculitis and severe liver injury in RA patients (PMIDs 36090738, 36258634, 21435128).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence for ankylosing spondylitis comes from two Phase 3 trials that were terminated, and IL-6 blockade is not an established pathway in this disease. The high model score is not supported by a clinical signal.

**To proceed, the following is needed:**
- Published outcome data from the terminated trials NCT01209689 and NCT01209702 (BUILDER-1 and BUILDER-2, PMID 23765873) to confirm whether efficacy was shown or the trials stopped for futility.
- Package insert warnings and contraindications from Health Canada, plus the approved indication text for each DIN, so the safety screen can proceed.
- Detailed mechanism-of-action data from DrugBank.

**Other predicted indications in the Evidence Pack:**
- Polyarticular juvenile idiopathic arthritis and its rheumatoid factor-positive subtype are already marketed uses with Phase 3 support. They are not novel repurposing signals and rate Proceed with Guardrails.
- Rheumatoid vasculitis is a research question with only case-level evidence, and tocilizumab-induced vasculitis reports are a counter-signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

