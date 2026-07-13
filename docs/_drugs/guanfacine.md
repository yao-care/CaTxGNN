---
layout: default
title: Guanfacine
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 7
---

# Guanfacine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Guanfacine: From ADHD to Specific Developmental Disorders

## One-Sentence Summary

Guanfacine is a selective α2A adrenergic receptor agonist with established FDA-approved efficacy for ADHD management in children and adolescents (ages 6–17), but is currently not marketed in Canada. The TxGNN model predicts it may be effective for **Specific Developmental Disorders** (including ADHD/ASD comorbidity) and **Tourette Syndrome**, with **2 completed clinical trials** and **6 publications** supporting the developmental disorder prediction, and an additional **2 completed clinical trials** (including a Phase 3 RCT) with **20 publications** supporting the Tourette syndrome prediction. Both indications are rated **L1** with a **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD in children and adolescents (FDA-approved; no Canadian registration) |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Guanfacine acts as a selective α2A adrenergic receptor agonist by binding to postsynaptic receptors on pyramidal neurons in the prefrontal cortex (PFC). This strengthens PFC executive control networks and attenuates disruptive subcortical impulse signals—a dual action that directly addresses the core deficits in attention regulation and impulse control that define ADHD and related specific developmental disorders. The extended-release formulation (Intuniv®) has already cleared FDA approval for ADHD in ages 6–17, establishing a well-characterized pharmacological precedent.

Specific developmental disorders encompass a spectrum of neurodevelopmental conditions—including ADHD, ASD with comorbid ADHD, and related learning and behavioral disorders—that share the same fronto-striatal circuit dysfunction targeted by Guanfacine's mechanism. A completed Phase 4 multicenter RCT (NCT04085172, N=396) directly evaluated extended-release guanfacine in ADHD children for whom prior stimulant treatment had failed. A large pragmatic trial using SMART design (NCT05916339, N=500) is actively examining Guanfacine's comparative effectiveness in children with ASD and ADHD comorbidity, further reinforcing the translational rationale.

Beyond the ADHD/ASD spectrum, Guanfacine also demonstrates strong mechanistic plausibility for **Tourette Syndrome** (TxGNN Rank #7, L1). Tic behaviors in Tourette syndrome are tightly linked to norepinephrine/dopamine imbalance in the PFC-basal ganglia-thalamus circuit. By enhancing α2A signaling in the PFC, Guanfacine reduces cortical excitatory drive that contributes to tic generation while simultaneously improving comorbid ADHD symptoms—providing a dual therapeutic benefit. European clinical guidelines (ESSTS v2.0, PMID 34757514) have formally endorsed Guanfacine as a pharmacological treatment option for tic disorders.

---

## Clinical Trial Evidence

### Primary Indication: Specific Developmental Disorder

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | Completed | 396 | Multicenter, double-blind, placebo-controlled RCT comparing guanfacine ER (TAK-503/SPD503) vs. atomoxetine vs. placebo in ADHD children/adolescents aged 6–17 for whom prior stimulant treatment failed; includes a 1-year open-label extension phase assessing long-term safety and efficacy |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Large pragmatic SMART-design trial comparing methylphenidate, amphetamine, and alpha-2 agonists (including guanfacine) for ADHD management in children and youth with autism spectrum disorder; results expected December 2027 |

> NCT03258476 was withdrawn before enrollment (0 participants); excluded from evidence table.

---

### Notable Secondary Indication: Tourette Syndrome (Rank #7, L1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004376](https://clinicaltrials.gov/study/NCT00004376) | Phase 3 | Completed | 35 | Randomized, double-blind, placebo-controlled trial directly evaluating guanfacine in children and adolescents with Tourette syndrome and comorbid ADHD; highest-level direct RCT evidence for this indication |
| [NCT01547000](https://clinicaltrials.gov/study/NCT01547000) | Phase 4 | Completed | 34 | Multi-site pilot study of extended-release guanfacine (Intuniv®) in children with Tourette disorder; provides real-world tolerability and preliminary efficacy data |

---

## Literature Evidence

### Specific Developmental Disorder

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Network Meta-analysis | The Lancet Psychiatry | Component network meta-analysis of pharmacological, psychological, and neurostimulatory interventions for adult ADHD; evaluates comparative benefits and harms across all available options including guanfacine |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | AAN comprehensive systematic review on treatment of tics in Tourette syndrome and chronic tic disorders; establishes evidence base for alpha-2 agonists including guanfacine |
| [15319020](https://pubmed.ncbi.nlm.nih.gov/15319020/) | 2004 | Retrospective Cohort | J Child Adolesc Psychopharmacol | Retrospective analysis of 80 children/adolescents with pervasive developmental disorders (ASD) treated with open-label guanfacine; preliminary data on effectiveness and safety in this population |
| [26894823](https://pubmed.ncbi.nlm.nih.gov/26894823/) | 2016 | Clinical Review | J Child Adolesc Psychopharmacol | Reviews guanfacine use in very young children (<6 years) for clinically significant hyperactivity and impulsivity; discusses pharmacokinetic factors unique to this age group |
| [31800525](https://pubmed.ncbi.nlm.nih.gov/31800525/) | 2020 | Commentary | J Dev Behav Pediatr | Case-based discussion of guanfacine ER combined with methylphenidate ER in a child with ADHD and comorbid behavioral challenges; practical prescribing considerations |
| [41057091](https://pubmed.ncbi.nlm.nih.gov/41057091/) | 2025 | Preclinical Study | Prog Neuropsychopharmacol Biol Psychiatry | Oral guanfacine restores catecholaminergic function and ameliorates ADHD-like symptoms in a rodent model of developmental manganese exposure; confirms α2A mechanism centrality |

---

### Tourette Syndrome

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Clinical Guideline | Eur Child Adolesc Psychiatry | European Society for the Study of Tourette Syndrome (ESSTS) guidelines v2.0 for pharmacological treatment; formally lists guanfacine as a treatment option for tic disorders |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic Review | J Psychopharmacol | Systematic review evaluating quality of evidence for pharmacological treatments of Tourette syndrome in children and adults; comprehensive quality assessment |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | AAN systematic review summarizing efficacy and risks of tic treatments; guanfacine identified as a viable alpha-2 agonist option |
| [37378108](https://pubmed.ncbi.nlm.nih.gov/37378108/) | 2023 | Case Series | Cureus | Three Tourette syndrome patients treated with guanfacine + aripiprazole combination showed significant improvement in motor and vocal tics; demonstrates combinability |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Review | Eur J Paediatr Neurol | Reviews pharmacological options for Tourette syndrome with comorbid ADHD; highlights guanfacine as a dual-target strategy addressing both tics and attentional symptoms |
| [7559307](https://pubmed.ncbi.nlm.nih.gov/7559307/) | 1995 | Preliminary Study | J Am Acad Child Adolesc Psychiatry | Early clinical experience with guanfacine for comorbid ADHD and Tourette syndrome; identified as a potential alternative to stimulants that may exacerbate tics |
| [12469007](https://pubmed.ncbi.nlm.nih.gov/12469007/) | 2002 | RCT (Pilot) | Clin Neuropharmacol | 4-week double-blind, placebo-controlled study of guanfacine in 24 children with Tourette syndrome; evaluated tic severity, neuropsychological function, and behavioral outcomes |
| [29335879](https://pubmed.ncbi.nlm.nih.gov/29335879/) | 2018 | Review | CNS Drugs | Comprehensive review of current pharmacological management approaches for Tourette syndrome; positions alpha-2 agonists including guanfacine within the treatment algorithm |
| [21183132](https://pubmed.ncbi.nlm.nih.gov/21183132/) | 2011 | Mechanistic Review | Behav Neurosci | Reviews norepinephrine and dopamine molecular signaling in the PFC across ADHD, PTSD, schizophrenia, and related disorders; provides pharmacological rationale for guanfacine |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Systematic Review | J Child Psychol Psychiatry | Practitioner review of treatments for Tourette syndrome and chronic tic disorder in children and young people; evaluates evidence across behavioral and pharmacological interventions |

---

## Canada Market Information

Guanfacine has **no Drug Identification Numbers (DINs) registered in Canada** and is currently not marketed. There are no Health Canada-approved product monographs available through standard regulatory channels.

| DIN | Product Name | Dosage Form | Approved Indication |
|-----|-------------|-------------|---------------------|
| — | No registered products | — | No Canadian authorization |

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug interaction profile) were not available in the current evidence pack. Notably, case reports suggest guanfacine may induce **syncope** through hypotension or bradycardia in children (PMID 16229000), and isolated cases of **guanfacine-induced mania** in pediatric patients have been reported (PMID 27228067, PMID 9730081), warranting psychiatric monitoring in predisposed individuals.

Please refer to the FDA-approved package insert (Intuniv®/Tenex®) for full safety information pending availability of the Canadian product monograph.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Guanfacine carries Level 1 evidence for both specific developmental disorders (ADHD/ASD spectrum) and Tourette syndrome—supported by completed Phase 3/4 RCTs, multiple systematic reviews, and formal European clinical practice guidelines. The mechanistic rationale is well-established and pharmacologically coherent. The key barrier is the complete absence of Canadian marketing authorization (0 DINs), which means no local regulatory framework, product monograph, or safety monitoring infrastructure currently exists in Canada.

**To proceed, the following is needed:**

- **Safety package**: Obtain and review the full FDA product monograph (Intuniv®/Tenex®) for warnings, contraindications, drug interactions, and cardiovascular monitoring requirements (hypotension, bradycardia, syncope risk)
- **MOA documentation**: Confirm mechanism of action details from DrugBank (DB01018) to complete the mechanistic link assessment
- **Regulatory pathway**: Assess Health Canada's New Drug Submission (NDS) or Notice of Compliance (NOC) requirements for pediatric neuropsychiatric indications; consider whether existing FDA/EMA data packages are sufficient for bridging
- **Canadian epidemiology**: Estimate the patient population in Canada with ADHD/ASD developmental disorders and Tourette syndrome who might benefit, to support the access case
- **Pharmacovigilance plan**: Develop a risk management strategy addressing cardiovascular monitoring, mania trigger screening, and sedation management—particularly for the pediatric population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

