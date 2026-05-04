---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: From Schizophrenia / Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

Aripiprazole is a second-generation (atypical) antipsychotic with established international use in schizophrenia and bipolar I disorder, and as an adjunctive treatment for major depressive disorder (MDD).
The TxGNN model predicts it may be effective for **Major Affective Disorder** — encompassing the full spectrum of mood disorders including unipolar depression and bipolar depression —
with **over 40 registered clinical trials** and **20 publications** currently supporting this direction, reaching the highest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canadian database; internationally approved for Schizophrenia and Bipolar I Disorder |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aripiprazole possesses a pharmacologically distinctive profile that distinguishes it from conventional antipsychotics. It acts simultaneously as a **partial agonist at D2/D3 dopamine receptors** and **5-HT1A serotonin receptors**, and as a **full antagonist at 5-HT2A receptors**. This combination creates what has been described as a "dopamine system stabilizer" effect — dampening mesolimbic dopaminergic hyperactivity (relevant to psychosis and mania) while potentially augmenting hypodopaminergic activity in the prefrontal cortex (relevant to depression and cognitive blunting). The dual dopamine/serotonin modulation directly addresses the neurotransmitter imbalances central to the pathophysiology of major affective disorders.

The mechanistic link between aripiprazole's receptor profile and major affective disorder is well-established. Mood disorders, including MDD and bipolar disorder, are characterized by dysregulated prefrontal-limbic dopaminergic and serotonergic signaling — the same circuits modulated by aripiprazole. Its 5-HT1A partial agonism is particularly relevant: activation of presynaptic 5-HT1A autoreceptors reduces serotonin output (beneficial in anxiety/agitation), while postsynaptic 5-HT1A agonism in the prefrontal cortex may enhance glutamatergic signaling and thereby augment the antidepressant effect of co-administered SSRIs or SNRIs. This mechanistic rationale underpins its well-documented role as an antidepressant augmentation agent.

Importantly, the TxGNN prediction is not speculative: the U.S. FDA has formally approved aripiprazole as an **adjunctive therapy for MDD**, and multiple large Phase 3 RCTs have confirmed its efficacy in treatment-resistant depression, bipolar depression, and bipolar I maintenance. The TxGNN model, by predicting "major affective disorder," is correctly recognizing the drug's established breadth of action across the entire mood disorder spectrum — extending its Canadian regulatory potential in a market where it currently holds no approved indications.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | Completed | 1,200 | 14-week RCT: adjunctive aripiprazole vs. placebo added to ongoing antidepressant in MDD patients with incomplete prior response — pivotal trial |
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | Completed | 1,200 | 14-week RCT: parallel pivotal study confirming safety and efficacy of adjunctive aripiprazole in MDD; co-primary outcome was MADRS score change |
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | Completed | 1,522 | VAST-D (VA Cooperative Study): head-to-head comparison of aripiprazole augmentation vs. bupropion augmentation vs. switch to bupropion in Veterans with MDD unresponsive to first-line treatment |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | Aripiprazole vs. placebo as adjunct to SSRI/SNRI in MDD; demonstrated significant reduction in depressive symptoms and acceptability |
| [NCT00882362](https://clinicaltrials.gov/study/NCT00882362) | Phase 3 | Completed | 155 | Long-term adjunctive aripiprazole (up to 52 weeks) co-administered with SSRI/SNRI in MDD; assessed sustained efficacy and long-term safety profile |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | Completed | 349 | Aripiprazole vs. placebo adjunctive to open-label antidepressant in MDD after failure of 8-week antidepressant lead-in phase |
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Completed | 225 | Evaluated reduced-dose aripiprazole as adjunctive treatment for MDD patients with inadequate response to prior antidepressant therapy |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | ASC-01 (fixed-dose aripiprazole/sertraline combination tablet) vs. sertraline monotherapy in MDD with incomplete sertraline response |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Recruiting | 390 | 8-week RCT of aripiprazole adjunctive to mood stabilizer for major depressive episode in bipolar I or II disorder; ongoing confirmatory study |
| [NCT00095745](https://clinicaltrials.gov/study/NCT00095745) | Phase 3 | Completed | 1,002 | 52-week open-label long-term safety study of adjunctive aripiprazole in MDD outpatients with incomplete antidepressant response |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Systematic Review / Meta-analysis of RCTs | PLoS One | Largest meta-analysis evaluating aripiprazole or bupropion augmentation/switching in TRD and MDD; confirmed superior efficacy and acceptable safety of aripiprazole augmentation over monotherapy |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review / Network Meta-analysis | J Affect Disord | Compared efficacy and discontinuation rates of augmentation agents in adult TRD; aripiprazole among top-ranked options with strong evidence base |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review / Meta-analysis | Psychol Med | First comprehensive meta-analytic assessment of antipsychotics as both monotherapy and adjunctive therapy in MDD; aripiprazole showed robust efficacy as adjunctive agent |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review / Meta-analysis | Prim Care Companion CNS Disord | Assessed long-term (≥6 months) efficacy and tolerability of adjunctive aripiprazole in MDD; primary outcome was remission; confirmed durable benefit with manageable adverse effects |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review / Network Meta-analysis | Neuropsychopharmacol Rep | Indirect comparison of brexpiprazole vs. aripiprazole for Japanese MDD patients inadequately responsive to antidepressants; evaluated efficacy, acceptability, tolerability, and safety |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Systematic Review / Network Meta-analysis | Medicine | Ranked four atypical antipsychotics (including aripiprazole) by efficacy and safety in adjunctive MDD treatment using frequentist network meta-analysis |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | Identified atypical antipsychotics as the most widely studied augmentation class for TRD; aripiprazole, brexpiprazole, and quetiapine highlighted as primary options with regulatory approval |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | Placed aripiprazole within the rapidly evolving TRD therapeutic landscape; compared established augmentation strategies against emerging agents (esketamine, psilocybin) |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Comprehensive JAMA review of bipolar disorder diagnosis and treatment covering the full major affective disorder spectrum; estimated 40 million individuals affected worldwide |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Reviewed three SGAs (quetiapine, aripiprazole, olanzapine) with FDA approval for adjunctive MDD treatment; receptor-profile analysis explaining why subantipsychotic doses exert antidepressant effects |

---

## Canada Market Information

Aripiprazole currently has **no Drug Identification Numbers (DINs)** on record in the Canadian regulatory database provided. No approved indication text is available from the Canadian regulatory record.

> **Note:** Aripiprazole (Abilify®, Abilify Maintena®, Abilify MyCite®) is approved in the United States, European Union, Japan, and many other jurisdictions for schizophrenia, bipolar I disorder, adjunctive MDD treatment, and irritability associated with autism spectrum disorder. Canadian regulatory status should be verified directly with Health Canada, as the current dataset may not reflect the complete market authorization history.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aripiprazole has one of the strongest evidence bases of any TxGNN candidate reviewed, with multiple large completed Phase 3 RCTs (including the 1,522-patient VAST-D trial) confirming efficacy in treatment-resistant depression and bipolar depression, and an established FDA approval for adjunctive MDD treatment. The TxGNN prediction score of 99.62% aligns directly with this clinical reality, and the biological mechanism is well-characterized.

**To proceed, the following is needed:**
- Confirm Health Canada registration status: verify whether aripiprazole has a current or historical DIN and obtain the complete Canadian product monograph for warnings, contraindications, and drug interactions
- Define the specific therapeutic sub-indication to pursue (e.g., MDD augmentation after SSRI/SNRI failure vs. bipolar I depression vs. bipolar II depression maintenance), as evidence strength and regulatory pathways differ by sub-indication
- Establish a risk management and monitoring plan addressing known class-effect safety concerns of atypical antipsychotics: metabolic syndrome (weight gain, dyslipidaemia, hyperglycaemia), tardive dyskinesia with long-term use, akathisia, and QTc prolongation risk
- Obtain mechanism-of-action documentation from DrugBank to complete formal pharmacological characterization for the regulatory submission package
- Review pharmacokinetic data for special populations relevant to the Canadian patient population (elderly patients with late-life depression, renal/hepatic impairment, pregnancy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

