---
layout: default
title: Apremilast
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Apremilast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Apremilast: From Psoriatic Arthritis to Rheumatoid Arthritis

## One-Sentence Summary

Apremilast (Otezla®) is an oral phosphodiesterase 4 (PDE4) inhibitor approved in the US and EU for psoriatic arthritis and plaque psoriasis, but not currently marketed in Taiwan.
The TxGNN model identifies **Rheumatoid Arthritis** as the highest-evidence new indication candidate (ranked #3 by TxGNN score; migraine disorder holds the top score but carries no clinical evidence),
supported by **6 clinical trials** and **19 publications** — though a pivotal Phase 2 trial was terminated early, and the RA development program has since been discontinued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriatic arthritis, plaque psoriasis (FDA/EMA approved; not marketed in Taiwan) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

> **Note on prediction ranking:** Migraine disorder holds the highest TxGNN score (98.66%, rank #1) but has zero clinical trial or literature evidence (L5). Rheumatoid arthritis (rank #3) is the most clinically substantiated target and is the primary focus of this report.

---

## Why is This Prediction Reasonable?

Apremilast is a selective small-molecule inhibitor of phosphodiesterase type 4 (PDE4). By preventing PDE4 from breaking down cyclic AMP (cAMP), it raises intracellular cAMP levels, which in turn suppresses multiple pro-inflammatory mediators — including TNF-α, IL-6, IL-17, and IL-23 — while promoting the anti-inflammatory cytokine IL-10. This mechanism underlies its approved use in psoriatic arthritis (PsA), a condition that shares key immunological features with rheumatoid arthritis (RA).

Rheumatoid arthritis is characterised by synovial inflammation driven by overactivated Th1 and Th17 lymphocytes and a self-amplifying cytokine cascade involving TNF-α, IL-6, and IL-17 — all downstream targets of the PDE4/cAMP pathway. A mouse collagen-induced arthritis model (PMID 30072998) demonstrated that apremilast suppresses Th1/Th17 differentiation and expands regulatory T cells. Ex vivo experiments using synovial cells from human RA patients (PMID 20525198) confirmed direct inhibition of spontaneous TNF-α production. Since apremilast is already approved for PsA — which also involves TNF-α and IL-17 driven synovitis — extending its use to RA carries clear biological plausibility.

However, the clinical development story urges caution. RA and PsA differ in synovial pathology, bone erosion biology, and treatment bar: RA patients already have access to highly effective MTX, JAK inhibitors, and multiple biologics. The key Phase 2 RCT (NCT01285310, n=237) was terminated early — a strong negative signal — and the Genovese et al. 2015 publication (PMID 25779750) reporting Phase 2 results confirmed insufficient efficacy versus standard of care. The RA development programme for apremilast has since been discontinued by the originator.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | **Terminated** | 237 | Randomised, double-blind, placebo-controlled parallel-group study of two apremilast doses in active RA with inadequate MTX response. Early termination is a critical negative signal; likely reflects insufficient efficacy against primary ACR endpoints |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Controlled trial directly comparing apremilast vs. placebo in active RA; evaluated safety, time to response, and durability — the only completed direct RA efficacy trial, but underpowered |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | **Withdrawn** | 0 | Planned study of apremilast added to TNF inhibitor + MTX in active RA; withdrawn before any enrolment — no usable data, though the design concept (combination strategy) remains of theoretical interest |
| [NCT00521339](https://clinicaltrials.gov/study/NCT00521339) | Phase 2 | Completed | 31 | Open-label study in recalcitrant plaque psoriasis (not RA); provides safety and pharmacokinetic data supporting apremilast's general tolerability profile |
| [NCT03036995](https://clinicaltrials.gov/study/NCT03036995) | Phase 2 | Completed | 80 | Apremilast combined with phototherapy for vitiligo; not RA-specific, but confirms broad immunomodulatory skin activity consistent with PDE4 inhibition |
| [NCT01504113](https://clinicaltrials.gov/study/NCT01504113) | N/A | Unknown | 100 | Infection risk study in psoriasis patients receiving targeted therapies (TNF-α / IL-17 antagonists); not directly relevant to RA efficacy but contextualises infectious risk of PDE4/immune-modulating agents |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | Phase 2 RCT | *Arthritis & Rheumatology* | Apremilast vs. placebo in active RA (MTX inadequate responders); multicenter, double-blind, placebo-controlled — the most definitive clinical dataset for RA; results indicated insufficient efficacy |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Animal Model | *Frontiers in Immunology* | Apremilast ameliorates collagen-induced arthritis in mice by suppressing Th1/Th17 differentiation and enhancing CD4+Foxp3+ Treg expansion — core mechanistic support for the RA hypothesis |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | Ex vivo Study | *Arthritis Research & Therapy* | Apremilast inhibits spontaneous TNF-α production from human RA synovial cells and reduces joint inflammation in two murine arthritis models — direct ex vivo mechanistic evidence |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | Phase 1 PK Study | *Clinical Pharmacology in Drug Development* | Pharmacokinetic interaction study of apremilast co-administered with methotrexate in RA/PsA patients; no clinically significant PK interaction — supports safe combination use |
| [40283434](https://pubmed.ncbi.nlm.nih.gov/40283434/) | 2025 | Review | *Journal of Clinical Medicine* | Comprehensive review positioning apremilast alongside rituximab and upadacitinib as tsDMARDs/bsDMARDs in inflammatory arthritis — current therapeutic landscape context |
| [33403021](https://pubmed.ncbi.nlm.nih.gov/33403021/) | 2020 | Systematic Review | *Therapeutic Advances in Musculoskeletal Disease* | Systematic analysis of shared targeted therapy development across autoimmune diseases; supports biological rationale for PDE4 inhibitor repurposing from PsA to RA |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Drug Review | *Drugs* | First global approval review of apremilast; explicitly discusses RA as one of the investigated indications and summarises development status at time of PsA approval |
| [32453211](https://pubmed.ncbi.nlm.nih.gov/32453211/) | 2021 | Case Report | *Journal of Clinical Rheumatology* | Successful use of apremilast for rituximab-associated palmoplantar pustulosis in a seropositive RA patient — rare real-world intersection of apremilast use in an RA context |
| [38499181](https://pubmed.ncbi.nlm.nih.gov/38499181/) | 2024 | Clinical Guidelines | *J Am Acad Dermatology* | National Psoriasis Foundation guidelines on perioperative management of systemic immunomodulatory agents in psoriasis and PsA — relevant safety reference for apremilast use in inflammatory conditions |
| [30917076](https://pubmed.ncbi.nlm.nih.gov/30917076/) | 2019 | Real-world Study | *J Managed Care & Specialty Pharmacy* | Adherence, persistence, and cost analysis for high-cost anti-inflammatory agents in RA — provides real-world context for apremilast's competitive positioning |

---

## Taiwan Market Information

Apremilast is currently **not marketed in Taiwan** (0 approved licenses). The drug is commercially available as Otezla® in the United States (FDA-approved since 2014) and European Union (EMA-approved) for psoriatic arthritis, moderate-to-severe plaque psoriasis, and oral ulcers associated with Behçet's disease. No Taiwan Food and Drug Administration (TFDA) approval exists as of the data cutoff (2026-04-05).

---

## Safety Considerations

Package insert warnings and contraindications are currently unavailable (Data Gap DG001, severity: Blocking). No drug-drug interaction data was retrieved from the evidence sources queried. Please refer to the Otezla® US/EU prescribing information for complete safety details, particularly regarding:

- **Depression/suicidality** (black box warning in some jurisdictions)
- **Weight loss** (clinically significant in some patients)
- **Drug interactions with strong CYP3A4 inducers** (e.g., rifampicin, which substantially reduces apremilast exposure)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic hypothesis for apremilast in RA is biologically sound — shared PDE4/cAMP pathway, proven PsA efficacy, and positive preclinical RA data — the clinical development programme has been effectively discontinued. The pivotal Phase 2 RCT (NCT01285310, n=237) was terminated early, and published Phase 2 results (Genovese et al., 2015) indicate insufficient efficacy against standard-of-care comparators in MTX-inadequate responders. Proceeding without first understanding the magnitude and cause of failure would not be justified.

**To proceed, the following is needed:**

- **Root cause analysis of NCT01285310 termination:** Clarify whether the primary driver was efficacy failure, safety signal, or strategic business decision — this fundamentally changes whether any path forward exists
- **Full data review of Genovese et al. 2015 (PMID 25779750):** Quantify ACR20/50/70 response rates and determine if any subgroup (e.g., seronegative RA, early RA, mild-to-moderate disease) showed clinically meaningful benefit
- **Safety gap remediation:** Obtain TFDA/originator package insert to address Data Gap DG001 (Blocking) before any clinical assessment can progress
- **MOA documentation:** Retrieve full DrugBank mechanism-of-action data (DG002) to support regulatory and scientific submissions
- **Subpopulation hypothesis generation:** Assess whether a specific RA niche (e.g., patients ineligible for biologics, low-disease-activity maintenance, or combination strategies) could provide a viable development path
- **Competitive landscape review:** Evaluate whether apremilast's oral administration and tolerability profile offer any differentiated advantage over currently approved JAK inhibitors and biologics for the Taiwanese/Canadian RA market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

