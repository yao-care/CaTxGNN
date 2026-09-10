---
layout: default
title: Nortriptyline
parent: 僅模型預測 (L5)
nav_order: 565
evidence_level: L5
indication_count: 2
---

# Nortriptyline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nortriptyline: From Depression to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Nortriptyline is a tricyclic antidepressant (TCA), classically used to treat depression.
The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
supported by **no registered clinical trials** but **20 relevant publications**, including several controlled/RCT-level studies in pediatric and adult ADHD populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (classic TCA indication; Canada-specific approved indication text not available in this evidence pack) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nortriptyline is not available in this evidence pack (data gap). Based on known pharmacological classification, nortriptyline is a tricyclic antidepressant (TCA) that primarily inhibits norepinephrine (NE) reuptake, with modest serotonin reuptake inhibition — its efficacy in depression is well established.

ADHD pathophysiology involves insufficient noradrenergic and dopaminergic signaling in the prefrontal cortex. Nortriptyline's NE reuptake inhibition is mechanistically analogous to atomoxetine, an already-approved non-stimulant ADHD medication that works via selective NE reuptake inhibition. This shared mechanism provides a plausible pharmacological rationale for TxGNN's prediction.

Notably, nortriptyline may offer a specific advantage in ADHD patients with comorbid tic disorders or Tourette's syndrome, since — unlike CNS stimulants — it does not tend to exacerbate tics. Multiple older controlled studies (see below) specifically explored this niche, supporting the biological plausibility of the prediction beyond a pure knowledge-graph association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | RCT/Controlled Trial | J Am Acad Child Adolesc Psychiatry | Nortriptyline evaluated in children with ADHD and comorbid tic disorder/Tourette's syndrome, avoiding tic exacerbation seen with stimulants |
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline efficacy and tolerability in children/adolescents with ADHD |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT (double-blind) | Pediatr Nephrol | Randomized double-blind trial of nortriptyline for enuresis in children with ADHD |
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of tricyclic antidepressants, including nortriptyline, as second-line ADHD treatment in children/adolescents |
| [7807071](https://pubmed.ncbi.nlm.nih.gov/7807071/) | 1995 | Systematic Assessment | J Nerv Ment Dis | Systematic assessment of TCAs, including nortriptyline, in adult ADHD |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatr Clin North Am | Reviews nonstimulant ADHD treatments; notes noradrenergic secondary amine TCAs (desipramine, nortriptyline) as established alternatives, limited by cardiovascular toxicity |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Guideline/Review | Ann Clin Psychiatry | CANMAT task force recommendations for managing mood disorders with comorbid adult ADHD |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opin Drug Saf | Safety review of non-stimulant ADHD agents including tricyclic antidepressants |
| [12270803](https://pubmed.ncbi.nlm.nih.gov/12270803/) | 2002 | Review | Adolesc Med | Overview of ADHD psychopharmacology in adolescents, including nortriptyline among TCAs used |
| [8444754](https://pubmed.ncbi.nlm.nih.gov/8444754/) | 1993 | Retrospective Study | J Am Acad Child Adolesc Psychiatry | Retrospective evaluation of serum levels and ECG effects of nortriptyline in a pediatric population — relevant for cardiac safety monitoring |

---

## Canada Market Information

Nortriptyline currently has no marketed products or DIN records in the Canadian regulatory dataset (`market_status: Not Marketed`, `total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale (NE reuptake inhibition analogous to atomoxetine) is well supported, and multiple controlled/RCT-level pediatric studies specifically tested nortriptyline in ADHD, including in the tic-disorder subpopulation — meeting L2 evidence criteria. However, no clinical trials are currently registered, the drug is not marketed in Canada, and key safety data (TFDA/product warnings, contraindications) are missing.

**To proceed, the following is needed:**
- Product label warnings and contraindications (currently blocking — data gap DG001)
- Detailed mechanism of action documentation from DrugBank (data gap DG002)
- Cardiac safety monitoring plan (ECG, serum level monitoring), given known TCA cardiotoxicity risk noted in pediatric literature
- Confirmation of Canadian market access pathway, since the drug is not currently marketed in Canada

*Note: A second, lower-confidence prediction (ADHD, Inattentive Type; TxGNN score 99.33%) was also generated but has no supporting clinical trials or literature (Evidence Level L5, decision stage S0) and is not recommended for further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

