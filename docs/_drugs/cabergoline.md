---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabergoline: From Prolactinoma to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a dopamine D2/D3 receptor agonist used as first-line medical therapy for hyperprolactinemia and prolactin-secreting pituitary adenomas (prolactinomas). The TxGNN model predicts it may be effective for **pituitary adenocarcinoma** — the rare malignant variant of pituitary neuroendocrine tumors — with **3 literature publications** providing indirect contextual support; no dedicated clinical trials have been registered for this specific diagnosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperprolactinemia; prolactin-secreting pituitary adenoma (prolactinoma) |
| Predicted New Indication | Pituitary Adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, cabergoline is a potent ergot-derived dopamine agonist with high selectivity for D2 and D3 receptors. Its primary therapeutic role is in hyperprolactinemia and prolactinomas — benign prolactin-secreting pituitary adenomas — where it suppresses hormone secretion and causes measurable tumor shrinkage by engaging dopamine D2 receptors expressed on lactotroph cells. Corticotroph adenomas have also been shown to express D2 receptors, supporting a broader anti-tumor role beyond the lactotroph lineage.

Pituitary adenocarcinoma sits at the malignant end of the pituitary neuroendocrine tumor spectrum and shares cellular origins with the adenomas for which cabergoline already has established use. Preclinical research has demonstrated that cabergoline can induce autophagic cell death, suppress pituitary tumor cell proliferation, and enhance apoptosis through multiple pathways — mechanisms that are not inherently limited to benign tumor histology. A 2020 review in *Neuroendocrinology* (PMID 31597135, within the rank 3 evidence set) specifically explored these broader anti-tumor mechanisms and their potential applicability across pituitary tumor subtypes.

The TxGNN model's high-confidence prediction (99.06%) likely arises from the rich connectivity between cabergoline, dopamine receptor signaling, and pituitary neoplasm nodes in its knowledge graph. It is worth noting that the closely related indication **"pituitary cancer"** (TxGNN rank 3, score 99.04%) is supported by over **20 registered clinical trials and 20 publications**, including multiple completed Phase 3 studies — lending strong biological plausibility to the broader prediction. The conceptual step from well-documented efficacy in benign pituitary adenomas to the malignant adenocarcinoma is biologically coherent, but requires dedicated clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered specifically for cabergoline in pituitary adenocarcinoma.

> **Supporting context from the closely related indication "pituitary cancer" (TxGNN Rank 3):** Over 20 clinical trials examine cabergoline in pituitary tumor subtypes. Selected high-relevance examples are shown below for reference.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Cabergoline in residual clinically nonfunctioning pituitary adenoma (NFPA) post-transsphenoidal surgery — randomized, open-label |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Dopamine agonist treatment of NFPAs — randomized controlled trial assessing tumor control vs observation |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline as primary therapy in NFPA — assessing tumor size reduction over 48 weeks |
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | N/A | Cabergoline for Cushing's disease (corticotroph pituitary adenoma) — D2 receptor agonism in non-prolactin secreting tumors |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or combined with cabergoline in Cushing's disease |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Receptor expression in NFPA and resistant prolactinomas; in vitro and in vivo response to dopamine agonists |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Octreotide + cabergoline combination in acromegaly partially responsive to SSA monotherapy |
| [NCT01730729](https://clinicaltrials.gov/study/NCT01730729) | Early Phase 1 | Completed | 20 | Cabergoline for metastatic breast cancer (prolactin receptor-positive) — demonstrates interest in off-label oncologic use |

---

## Literature Evidence

*The following publications were retrieved for pituitary adenocarcinoma (Rank 1 indication). Note that none directly studies cabergoline as treatment for pituitary adenocarcinoma; they represent tangential or contextual mentions.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case report + review | Endocrine Practice | Long-term cabergoline and octreotide management in ectopic ACTH hypersecretion after adrenalectomy; illustrates dopamine agonist use in a corticotropin-secreting tumor context |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case report | Medicine | Atypical MEN1 case with multiple endocrine tumors including pituitary involvement; cabergoline used as part of the management strategy |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case report | Rev Esp Enferm Dig | Patient with pituitary adenoma on cabergoline who was subsequently diagnosed with pancreatic adenocarcinoma; cabergoline use is incidental to the primary case |

---

## Canada Market Information

Cabergoline is **not currently registered in Canada** based on available data. No Drug Identification Numbers (DINs) are on file.

> **Data note:** International market data indicates that cabergoline is commercially available in many countries under brand names including Dostinex (Pfizer) and Cabaser. The absence of Canadian registration records in this dataset likely reflects a data collection gap in the current version of the CaTxGNN pipeline rather than true market unavailability. Independent verification via [Health Canada's Drug Product Database](https://health-products.canada.ca/dpd-bdpp/) is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known safety signals from the literature** (not captured in structured safety data): Clinical trial data within the pituitary cancer evidence set highlights two clinically important concerns — (1) **cardiac valvulopathy** risk with high cumulative cabergoline doses (observed with ergot-derived dopamine agonists; see NCT00460616 observational study on cardiac abnormalities), and (2) **impulse control disorders** (ICD), with prevalence reported up to 59.8% in some prolactinoma cohorts (PMID 41619686, 2026). These risks should be formally assessed before any expanded use consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials have been specifically conducted for cabergoline in pituitary adenocarcinoma, and the 3 retrieved publications are incidental case reports that do not provide direct efficacy or safety data for this rare malignant entity. While cabergoline's anti-tumor effects on benign pituitary adenomas are well-documented (particularly for prolactinomas and NFPAs), the biological and clinical leap to malignant adenocarcinoma requires dedicated evidence before a repurposing decision can be made.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm cabergoline's actual Canadian market status via Health Canada's Drug Product Database, as current data likely reflects a pipeline gap
- **MOA data:** Retrieve complete mechanism of action data from DrugBank (DB00248) to support formal mechanistic linkage analysis
- **Safety package:** Obtain and parse the full prescribing information / product monograph for key warnings, contraindications, and drug interactions (currently all [Data Gap])
- **Targeted literature review:** Conduct a systematic search specifically for cabergoline or dopamine agonists in pituitary carcinoma / aggressive pituitary tumors, including compassionate-use reports and case series
- **Receptor profiling evidence:** Assess D2/D3 receptor expression data in pituitary adenocarcinoma specimens to confirm target engagement feasibility
- **Leverage Rank 3 evidence base:** The "pituitary cancer" indication (TxGNN Rank 3) has 20 clinical trials and 20 publications; an indication-broadening strategy targeting this better-evidenced category may be a more actionable near-term path than focusing narrowly on adenocarcinoma
- **Cardiac and neuropsychiatric risk management plan:** Any clinical development in oncology populations would require close monitoring protocols for valvulopathy and impulse control disorders given known class effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

