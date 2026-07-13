---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 5
---

# Montelukast
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

# Montelukast: From Asthma and Allergic Rhinitis to Bronchitis

## One-Sentence Summary

Montelukast (Singulair) is a selective cysteinyl leukotriene receptor 1 (CysLT1) antagonist, globally approved for the treatment of chronic asthma (≥2 years of age), allergic rhinitis, and exercise-induced bronchoconstriction.
The TxGNN model predicts it may also be effective for **Bronchitis** — spanning viral bronchiolitis in infants, post-viral airway wheezing, non-asthmatic eosinophilic bronchitis (NAEB), and bronchiolitis obliterans syndrome (BOS) after transplantation — with **23 clinical trials** and **20 publications** currently supporting this direction.
Evidence is strongest for BOS (completed Phase 2 FAM regimen trial) and RSV-related bronchiolitis in infants (multiple double-blind RCTs), though efficacy signals in acute viral bronchiolitis remain mixed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma (≥2 years), allergic rhinitis, exercise-induced bronchoconstriction (FDA/EMA approved) |
| Predicted New Indication | Bronchitis (viral bronchiolitis, NAEB, bronchiolitis obliterans syndrome) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (no DINs on file) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Montelukast's core mechanism is the selective blockade of the CysLT1 receptor on airway smooth muscle, eosinophils, and mast cells, inhibiting the downstream effects of cysteinyl leukotrienes LTC4, LTD4, and LTE4. These mediators drive bronchospasm, mucus hypersecretion, eosinophil recruitment, and airway hyperresponsiveness — pathological hallmarks shared across multiple bronchitis phenotypes. By interrupting leukotriene signalling, montelukast targets the inflammatory cascade at a mechanistic level applicable well beyond its approved asthma indication.

The prediction spans three clinically distinct but mechanistically related bronchitis subtypes. In **viral bronchiolitis** (primarily RSV-induced in infants), cysteinyl leukotriene concentrations are elevated during acute infection; CysLT1 blockade during primary RSV infection has been shown in animal models to prevent subsequent airway hyperresponsiveness and eosinophilic inflammation upon reinfection (PMID 20442434). In **non-asthmatic eosinophilic bronchitis (NAEB)**, montelukast as add-on to inhaled corticosteroids reduces airway eosinophilia, lowers cough VAS scores, and improves quality of life (PMID 25563311). In **bronchiolitis obliterans syndrome (BOS)** after hematopoietic or lung transplantation, the leukotriene B4 pathway is activated in fibrotic airway remodelling (LTB4 elevation confirmed in rat models, PMID 28545478), providing a rationale for CysLT1 blockade as an anti-fibrotic adjunct.

The mechanistic transition from asthma to bronchitis is biologically coherent: both disease groups involve leukotriene-driven lower airway inflammation, and the same CysLT1-mediated pathways govern the inflammatory phenotype. Clinical translation, however, differs by subtype — Phase 2 trial data supports the FAM regimen in BOS, randomised data in NAEB is promising, and results in acute viral bronchiolitis in infants remain inconsistent across trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | Double-blind, placebo-controlled RCT of once-daily montelukast for viral bronchiolitis in infants; primary endpoint was duration of acute illness |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completed | 51 | Double-blind, placebo-controlled RCT in acute RSV bronchiolitis; evaluated clinical progress and cytokine profiles; montelukast approved as oral granules for infants |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | FAM regimen (fluticasone + azithromycin + montelukast) with brief steroid pulse for new-onset BOS after stem cell transplant; primary endpoint: ≥10% FEV1 decline |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | RCT of montelukast monotherapy for BOS after lung transplantation; tested whether montelukast slows progression of chronic rejection |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Phase 4 | Completed | 100 | Oral montelukast added to maximal standard treatment in hospitalised preschool children with acute asthma/wheezing; assessed additive benefit |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Montelukast for acute bronchiolitis and post-bronchiolitis viral-induced wheezing in infants aged 3–12 months; dual endpoint of acute and post-acute phase |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Multi-institutional Phase 2 study of montelukast for BOS following allogeneic or autologous stem cell transplantation in children and adults |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Randomised double-blind study of add-on montelukast to inhaled budesonide in non-asthmatic eosinophilic bronchitis; primary endpoint: cough VAS reduction |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | feNO-guided differential diagnosis of chronic cough; compared montelukast vs. prednisolone on 24-hour cough counts at two weeks |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1,125 | Large Phase 3 RCT of two doses of montelukast vs. placebo for respiratory symptoms associated with RSV-induced bronchiolitis in children aged 3–24 months |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Phase 2 Trial | Biol Blood Marrow Transplant | FAM regimen for new-onset BOS after HCT; n=36, multicenter, open-label; primary endpoint was treatment failure (≥10% FEV1 decline or death) — key efficacy signal for montelukast in transplant-related BOS |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Prospective Phase 2 | Transplant Cell Ther | Montelukast monotherapy for BOS after HCT; assessed lung function decline and CysLT pathway biomarkers; confirmed mechanistic basis for CysLT1 blockade in fibrotic airways |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Clinical Practice Guidelines | Eur Respir J | ERS/EBMT joint guidelines on management of pulmonary chronic GVHD in adults; addresses FAM regimen (including montelukast) as a recognised management strategy |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chin Med J | Add-on montelukast to budesonide in NAEB; significantly reduced cough VAS, airway eosinophilia (FeNO), and improved quality of life scores compared to budesonide monotherapy |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | RCT | Respir Res | Budesonide/formoterol + montelukast + N-acetylcysteine vs. systemic corticosteroids for BOS after HSCT; evaluated FEV1 stabilisation as alternative to steroid-based therapy |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | RCT | PLoS One | Fish oil vs. montelukast alone and in combination on airway inflammation and hyperpnea-induced bronchoconstriction in asthmatics; demonstrates leukotriene pathway modulation in bronchospasm |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Narrative Review | Ther Adv Respir Dis | Comprehensive review of montelukast's therapeutic potential in BOS after lung and stem cell transplantation; covers TH-1/TH-2, NF-κB, TGF-β mechanistic pathways |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal Study | J Cardiothorac Surg | LTB4 elevation documented in transplantation-related bronchiolitis obliterans rat model; montelukast suppressed LTB4-driven fibrotic airway remodelling, providing preclinical mechanistic rationale |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clin Evid | Systematic evidence review of bronchiolitis management in infants; evaluates leukotriene receptor antagonists among other interventions for efficacy and safety |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Systematic Review | Pediatr Allergy Immunol | Systematic review of montelukast efficacy for preventing post-bronchiolitis wheezing; assessed CysLT pathway modulation in RSV-associated reactive airway disease sequelae |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important:** Although formal safety data was not available in this Evidence Pack, the medical literature retrieved contains a critical signal. The **US FDA issued a black box warning in 2020** regarding neuropsychiatric adverse events associated with montelukast, including nightmares, insomnia, anxiety, depression, and suicidal ideation (PMID 37758273, PMID 35608857). This risk is particularly relevant for the paediatric bronchiolitis population. Risk-benefit assessment should be conducted on an individual basis before initiating therapy in children.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed clinical trials directly test montelukast in bronchitis-related conditions, including a Phase 2 multicenter trial of the FAM regimen for BOS (PMID 26475726) and double-blind RCTs in RSV bronchiolitis, providing an L2 evidence base with clear biological plausibility. However, efficacy in acute viral bronchiolitis in infants remains inconsistent across trials, BOS evidence comes primarily from combination regimens rather than montelukast monotherapy, and Health Canada currently lists no approved DINs for any bronchitis indication.

**To proceed, the following is needed:**
- Retrieve and review the full product monograph (package insert) to document contraindications and warnings — currently a blocking data gap
- Clarify the primary target subtype: acute viral bronchiolitis, NAEB, or BOS carry different evidence strengths and patient populations, requiring separate clinical development paths
- Commission a meta-analysis of existing infant bronchiolitis RCTs to resolve conflicting efficacy signals before investment in further clinical development
- Develop a neuropsychiatric adverse event monitoring protocol for paediatric use, consistent with the 2020 FDA black box warning requirements
- Confirm route and formulation availability in Canada: oral granule formulation (for infants) and 4 mg/5 mg/10 mg tablets need Health Canada registration if proceeding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

