---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

---

## One-Sentence Summary

Dupilumab is a fully human monoclonal antibody that blocks the IL-4 receptor alpha subunit (IL-4Rα), globally approved for type 2 inflammatory conditions including atopic dermatitis and asthma.
The TxGNN model predicts it may be effective for **bronchitis** — particularly eosinophilic and plastic bronchitis subtypes — based on shared IL-4/IL-13 airway inflammatory pathways,
with **1 clinical trial** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No local regulatory record available (globally approved for: atopic dermatitis, asthma, chronic rhinosinusitis with nasal polyps, eosinophilic esophagitis) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, dupilumab is a fully human IgG4 monoclonal antibody that targets the shared IL-4 receptor alpha subunit (IL-4Rα), blocking downstream signaling of both IL-4 and IL-13 — two core Th2 cytokines that drive type 2 airway inflammation. This mechanism has been clinically validated in asthma, chronic rhinosinusitis with nasal polyps, and atopic dermatitis through multiple large Phase 3 RCTs.

The predicted efficacy in bronchitis rests on a mechanistic continuum: IL-4 and IL-13 promote goblet cell hyperplasia, abnormal mucus secretion, eosinophilic infiltration, and airway remodeling — processes central to eosinophilic bronchitis and the rarer plastic bronchitis. By blocking these cytokines upstream, dupilumab may reduce mucus plug formation and eosinophil-driven airway obstruction in these bronchitis subtypes. A 2025 comprehensive review (PMID 39904363) already incorporates dupilumab BOREAS/NOTUS trial data in the context of COPD chronic bronchitis subtypes, extending mechanistic relevance beyond classic asthma.

However, the bridge from mechanistic plausibility to direct clinical evidence remains incomplete. The only registered trial in this evidence pack (NCT04362501) targets upper airway CRSsNP — not bronchitis — making it anatomically adjacent but not directly supportive. The strongest airway RCT evidence (TRAVERSE, PMID 34597534) and the pediatric plastic bronchitis case series (PMID 38488768) together support biological rationale, but dedicated bronchitis-specific trials are absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Dupilumab for chronic rhinosinusitis without nasal polyps (CRSsNP) — an upper respiratory Th2 inflammatory condition sharing IL-4/IL-13 mechanistic pathways with bronchitis. Provides indirect mechanistic support within the unified airway inflammation model, but bronchitis was not a primary endpoint. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Phase 3 RCT Extension | The Lancet Respiratory Medicine | TRAVERSE open-label extension: confirms long-term (>1 year) safety and efficacy of dupilumab in moderate-to-severe asthma. Strongest mechanistically adjacent RCT, demonstrating sustained IL-4/IL-13 blockade benefit in eosinophilic airway disease. |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review & Meta-analysis | The Journal of Asthma | Pooled analysis of RCTs evaluating dupilumab in uncontrolled asthma; confirms significant reduction in exacerbation rates and improvement in lung function, supporting the IL-4/IL-13 mechanistic rationale applicable to bronchitis. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | RCT | Chest | MRI-based lung ventilation assessment in prednisone-dependent asthma treated with anti-T2 biologics; demonstrates reversal of eosinophil-driven regional airway obstruction — directly relevant to eosinophilic airway dysfunction in bronchitis. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Comprehensive Review | Tuberculosis and Respiratory Diseases | 2025 review of pharmacologic strategies for COPD exacerbation prevention, incorporating dupilumab BOREAS/NOTUS data; contextualizes IL-4/IL-13 inhibition in chronic bronchitis-predominant COPD subtypes. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Narrative Review / Case Series | Pediatric Pulmonology | Emerging therapies for pediatric eosinophilic plastic bronchitis; includes dupilumab as a novel treatment option in this rare Th2-driven bronchitis subtype — the most direct evidence for the bronchitis repurposing hypothesis. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Narrative Review | Expert Opinion on Pharmacotherapy | Examines management challenges in asthma with smoking-induced airway diseases (chronic bronchitis, emphysema, ACO); highlights the unmet need and treatment uncertainty in this population not covered by existing trial data. |

---

## Canada Market Information

No dupilumab products are currently registered or authorized for sale in Canada based on the available regulatory data in this evidence pack. Local regulatory approval status should be independently verified against the Health Canada Drug Product Database, as dupilumab (Dupixent®) has received global approvals in multiple jurisdictions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for dupilumab in bronchitis remains indirect — derived from mechanistically adjacent conditions (asthma, COPD, CRSsNP) rather than dedicated bronchitis clinical trials. With only one peripherally relevant trial, no completed RCT specifically targeting bronchitis, and all local safety and MOA data absent, the current evidence base (L3) is insufficient to advance beyond a research hypothesis stage.

**To proceed, the following is needed:**

- **Direct clinical trial**: Commission or identify a Phase 2 RCT specifically in eosinophilic bronchitis or plastic bronchitis, distinct from asthma protocols
- **Biomarker stratification plan**: Define patient selection criteria using blood eosinophil counts, fractional exhaled nitric oxide (FeNO), sputum eosinophilia, and IL-13 levels to identify the subpopulation most likely to respond
- **MOA documentation**: Retrieve full dupilumab mechanism of action data from DrugBank (DB12159) to complete mechanistic analysis
- **Regulatory status verification**: Confirm current Canada (Health Canada) and local regulatory approval status via official drug product databases — Dupixent® is approved in multiple markets and local registration gaps should be resolved
- **Safety data retrieval**: Obtain the full product monograph / package insert (TFDA or Health Canada) to complete safety screening including warnings, contraindications, and drug interactions
- **Assess bronchitis subtype specificity**: Distinguish between eosinophilic bronchitis (IL-4/IL-13 mechanism plausible), infectious/viral bronchitis (mechanism not applicable), and chronic obstructive bronchitis (partial overlap), as TxGNN prediction likely captures the Th2-driven subtype only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

