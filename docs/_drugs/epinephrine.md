---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Epinephrine: From Anaphylaxis & Cardiac Arrest to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is a non-selective adrenergic agonist foundational to emergency medicine, classically used as the first-line treatment for anaphylaxis, cardiac arrest, and acute severe hypersensitivity reactions.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** with a score of **99.71%**,
supported by **multiple Cochrane systematic reviews**, **completed Phase 3 trials in asthma**, and **Phase 4 evidence in bronchiolitis** — making this a prediction with both strong mechanistic basis and existing clinical precedent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anaphylaxis, cardiac arrest, severe acute allergic reactions |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (no DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, epinephrine is a non-selective catecholamine that simultaneously activates α1, β1, and β2 adrenergic receptors. Its **β2-adrenergic action** on bronchial smooth muscle produces rapid bronchodilation — directly reversing airflow obstruction — while **α1-mediated vasoconstriction** reduces mucosal edema lining the airways. These two mechanisms together address the two principal pathophysiological components of obstructive airway disease.

Obstructive lung disease encompasses asthma, chronic obstructive pulmonary disease (COPD), and bronchiolitis — all sharing the defining feature of impaired airflow. Epinephrine's dual bronchodilatory and decongestant profile is mechanistically applicable across this spectrum. In acute severe asthma, intramuscular epinephrine is already recommended in many prehospital and emergency protocols when selective β2-agonists (e.g., salbutamol) are insufficient. In pediatric bronchiolitis — the leading infectious cause of infant hospitalization — nebulized epinephrine has been evaluated in multiple RCTs and Cochrane reviews, demonstrating short-term clinical improvement. In COPD, elevated endogenous catecholamines are documented in correlation with disease severity.

The TxGNN high-confidence prediction therefore captures an established pharmacological relationship rather than a speculative association. The clinical question for development is not whether epinephrine works in obstructive lung disease, but in **which subpopulation, by which route, and against which comparator** it offers the most favorable benefit-to-risk ratio relative to modern selective agents.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | Unknown | 100 | Directly tests Epinephrine + Dexamethasone + Hypertonic Saline vs. standard care in children with bronchiolitis (a form of obstructive lung disease); primary outcome is reduction in hospitalization rate |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | Completed | 208 | 3-month double-blind safety extension of epinephrine HFA inhaler (E004) vs. placebo in adolescent and adult asthma patients; evaluates 6-month safety profile |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | 4-week parallel RCT of inhaled epinephrine aerosol (E004) vs. placebo in children aged 4–11 with asthma; evaluates efficacy and safety |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Double-blind crossover single-dose study of E004 (epinephrine inhalation aerosol) vs. placebo in pediatric asthma aged 4–11 years |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | RCT testing intramuscular epinephrine as adjunct to inhaled β2-agonists in children with severe asthma exacerbation; weight-based dosing of epinephrine 1:1000 |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | Nebulized 3% hypertonic saline plus epinephrine in hospitalized infants with RSV-positive bronchiolitis; evaluates clinical severity scores and length of stay |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | Head-to-head RCT of epinephrine vs. albuterol in bronchiolitis; one of the largest direct comparisons of these two bronchodilators in this population |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Multicenter RCT of nebulized adrenaline + oral betamethasone in pediatric emergency bronchiolitis; terminated early — prior trend toward reduced hospitalization warranted confirmatory study |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Pharmacokinetic crossover study comparing Primatene Mist (inhaled epinephrine 0.25 mg) vs. IM epinephrine vs. ProAir (albuterol) in healthy adults; characterizes systemic exposure by route |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Phase 1/2 | Terminated | 9 | Dose-ranging 6-arm crossover study of epinephrine HFA-MDI (E004) vs. placebo vs. epinephrine CFC-MDI in adult intermittent-to-moderate persistent asthma; terminated with insufficient enrollment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34593615](https://pubmed.ncbi.nlm.nih.gov/34593615/) | 2022 | Systematic Review / Meta-analysis | *Thorax* | Epinephrine vs. selective β2-agonist in acute asthma; international guidelines currently discourage epinephrine unless anaphylaxis is co-present, but pre-hospital guidelines support IM epinephrine for acute severe/life-threatening asthma — this review synthesizes the comparative efficacy data |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Systematic Review | *Cochrane Database of Systematic Reviews* | Comprehensive meta-analysis of epinephrine for acute bronchiolitis; assesses multiple RCTs across inpatient and outpatient settings — foundational evidence base for current clinical use |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Systematic Review | *Cochrane Database of Systematic Reviews* | Earlier Cochrane review documenting modest short-term benefit of epinephrine in mild-to-moderate bronchiolitis; established the evidence trajectory subsequently updated in the 2011 revision |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | *Expert Review of Respiratory Medicine* | Dedicated therapeutic strategies review for pediatric bronchiolitis covering racemic epinephrine, corticosteroids, hypertonic saline, and high-flow oxygen; synthesizes 2009–2018 literature |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | *Pediatric Clinics of North America* | Reviews evidence for acute bronchiolitis and croup management; confirms temporary symptomatic benefit of nebulized adrenaline and contextualizes its role alongside corticosteroids |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | *BMJ Clinical Evidence* | Clinical evidence summary for bronchiolitis management in infants; covers the evidence base for bronchodilators including epinephrine in the most common lower respiratory infection of infancy |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | *BMJ Clinical Evidence* | Systematic clinical evidence review for bronchiolitis; includes evaluation of bronchodilators and adrenaline as part of a structured evidence-based summary |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | *Clinical Pharmacology and Therapeutics* | Direct comparative study of bronchodilator effects of terbutaline and epinephrine in obstructive lung disease; foundational pharmacological characterization of epinephrine's airway effects vs. selective β2-agonists |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Observational | *Scandinavian Journal of Clinical and Laboratory Investigation* | Elevated plasma noradrenaline in COPD patients correlated inversely with arterial oxygen saturation; demonstrates that the adrenergic system is pathophysiologically engaged in chronic obstructive lung disease |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review | *Journal of Allergy and Clinical Immunology* | Reviews childhood asthma as an obstructive airway disease with airway hyperresponsiveness; contextualizes the adrenergic pharmacology underpinning epinephrine's role in bronchospasm management |

---

## Canada Market Information

No Canadian Drug Identification Numbers (DINs) were found for epinephrine in the current regulatory database query. The drug is recorded as **not marketed** in this dataset.

> **Data Gap Notice:** This is likely a database query limitation rather than an accurate reflection of market availability. Epinephrine products (parenteral formulations, auto-injectors such as EpiPen, and OTC inhaled formulations) are expected to be present in the Canadian market. Direct verification against the **Health Canada Drug Product Database (DPD)** is recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the Health Canada-approved product monograph for complete safety information.

No drug interaction data was retrieved in this query (DDI status: not found). Warnings and contraindications from the product monograph were not parsed in this evidence pack. Key safety considerations known from the pharmacological class include cardiovascular effects (tachycardia, hypertension, arrhythmia) and anxiety, particularly relevant in elderly patients and those with ischemic heart disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Epinephrine has a well-validated mechanistic basis and documented clinical utility in obstructive lung conditions, supported by multiple Cochrane systematic reviews, completed Phase 3 trials in asthma, and Phase 4 evidence in bronchiolitis — making this the strongest prediction in the candidate list. The primary clinical question is not whether epinephrine is active in obstructive lung disease, but how to position it relative to modern selective β2-agonists, and for which specific subpopulations (e.g., pediatric bronchiolitis, acute severe asthma refractory to salbutamol) it offers the best risk-benefit profile in the Canadian context.

**To proceed, the following is needed:**
- Verification of Canadian epinephrine product listings in the Health Canada Drug Product Database (DPD) — current query shows 0 DINs, which likely reflects a data gap
- Full mechanism of action data from DrugBank to complete pharmacological documentation
- Obtain and parse the Health Canada-approved product monograph for complete warnings, contraindications, and drug interactions
- Define the target sub-indication: acute severe asthma, pediatric bronchiolitis, or another obstructive lung disease subtype — each has distinct evidence depth and regulatory pathways
- Safety monitoring plan addressing cardiovascular adverse effects (tachycardia, hypertension, arrhythmia) in the intended population, particularly for inhaled formulations in pediatric patients
- Comparative effectiveness analysis against current standard of care (inhaled salbutamol/albuterol) to establish where epinephrine adds clinical value beyond existing selective agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

