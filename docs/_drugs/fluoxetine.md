---
layout: default
title: Fluoxetine
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# FLUOXETINE: From Major Depression to Schizotypal Personality Disorder

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) widely used for major depressive disorder, OCD, bulimia nervosa, and panic disorder.
The TxGNN model predicts it may be effective for **Schizotypal Personality Disorder (SPD)**,
with **0 clinical trials** and **11 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder (internationally established SSRI; Health Canada product data not retrieved in this dataset) |
| Predicted New Indication | Schizotypal Personality Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Canada Market Status | Data gap (Health Canada DIN pipeline not yet completed for this drug) |
| Number of DINs | 0 (data gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluoxetine is the prototypical SSRI: it blocks the presynaptic serotonin transporter (SERT), increasing synaptic 5-HT availability across limbic and cortical circuits. Although the formal MOA field was flagged as a data gap in this evidence pack, fluoxetine's pharmacology is well-characterized — it also carries moderate 5-HT2C affinity and, at higher doses, weak norepinephrine reuptake inhibition. Formal DrugBank retrieval is recommended to populate this field for future evaluations.

Schizotypal personality disorder is characterized by cognitive and perceptual distortions (magical thinking, ideas of reference), marked social anxiety, and impulsive dysregulation — a symptom cluster that significantly overlaps with borderline personality disorder. Both conditions share documented serotonergic dysregulation: reduced central 5-HT activity has been linked to impulsive aggression, self-injury, and interpersonal instability across Cluster A and Cluster B personality disorders. This provides a plausible mechanistic bridge: SSRI-mediated 5-HT enhancement may attenuate the affective and impulsive components of SPD, and 5-HT2A modulation may partially blunt cognitive-perceptual distortions.

The most directly relevant evidence comes from a 1991 prospective open-label study (PMID 1853957, N=22) in which fluoxetine produced significant reductions in self-injury and global symptoms in patients meeting criteria for borderline or schizotypal personality disorder. However, the evidence base remains limited to small, non-blinded studies, and the quasi-psychotic features of SPD — which are more dopaminergically driven — may require antipsychotic augmentation beyond SSRI monotherapy. A documented adverse case of transient psychosis in a schizotypal patient on fluoxetine (PMID 9664779) further underscores the need for careful psychiatric monitoring.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1853957](https://pubmed.ncbi.nlm.nih.gov/1853957/) | 1991 | Open-label study | Am J Psychiatry | 22-patient prospective trial; fluoxetine significantly reduced self-injury and Hopkins Symptom Checklist scores in borderline/schizotypal PD patients regardless of diagnosis — most direct evidence available |
| [9448667](https://pubmed.ncbi.nlm.nih.gov/9448667/) | 1998 | Retrospective cohort | J Clin Psychiatry | Psychopharmacology review for BPD and SchPD; no single agent of choice, but SSRIs and other agents offer benefit depending on presenting symptom cluster (affective vs. cognitive) |
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Narrative Review | Ment Health Clin | Pharmacological treatment of Cluster A personality disorders (paranoid, schizoid, schizotypal); SSRIs mentioned for affective and impulsive symptoms, evidence overall sparse |
| [8227492](https://pubmed.ncbi.nlm.nih.gov/8227492/) | 1993 | Expert Review | J Clin Psychopharmacol | Conceptual framework for PD pharmacotherapy; early clinical data supporting SSRIs for affective dysregulation in both BPD and ScPD subtypes |
| [12214786](https://pubmed.ncbi.nlm.nih.gov/12214786/) | 2002 | Review | Psychol Med | PD diagnoses assessed before and after fluoxetine treatment in depressed outpatients; stability of PD classification across treatment explored |
| [7635854](https://pubmed.ncbi.nlm.nih.gov/7635854/) | 1995 | Clinical study | J Clin Psychiatry | Predictors of drug response in OCD; schizotypal features associated with reduced SSRI response — relevant safety/efficacy signal for SPD |
| [9664779](https://pubmed.ncbi.nlm.nih.gov/9664779/) | 1998 | Case report | Psychosomatics | Transient psychosis with psychogenic polydipsia in a schizotypal patient taking fluoxetine — important safety signal, suggests risk of serotonergic activation in quasi-psychotic presentations |
| [15209835](https://pubmed.ncbi.nlm.nih.gov/15209835/) | 2004 | Cohort | Aust NZ J Psychiatry | Bipolar II disorder personality traits and treatment outcome; schizotypal PD as comorbidity assessed in treatment response context |
| [33634761](https://pubmed.ncbi.nlm.nih.gov/33634761/) | 2021 | Case Report | CNS Neurol Disord Drug Targets | Asenapine treatment of catatonia in a schizotypal PD patient with COVID-19 septic shock; illustrates management complexity when SPD co-occurs with acute medical illness |
| [37082034](https://pubmed.ncbi.nlm.nih.gov/37082034/) | 2021 | Case study | Postepy Psychiatr Neurol | OCD/anorexia nervosa comorbidity diagnostic challenges; fluoxetine used, indirectly relevant to SSRI use in complex psychiatric presentations |

---

## Safety Considerations

Please refer to the package insert for safety information.

**Notable safety signal from literature:** PMID 9664779 documents a case of transient psychosis with psychogenic polydipsia in a schizotypal patient taking fluoxetine. This suggests that serotonergic activation may transiently worsen quasi-psychotic symptoms in SPD — psychiatric monitoring is warranted, particularly during early treatment initiation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a single small open-label trial from 1991 (N=22), and no registered clinical trials exist; the cognitive-perceptual core features of schizotypal personality disorder are more dopaminergically driven and may not respond adequately to SSRI monotherapy, limiting the translational value of the TxGNN prediction at this stage.

**To proceed, the following is needed:**

- At minimum a Phase 2 controlled trial specifically evaluating fluoxetine (or SSRI class) in schizotypal personality disorder with separate outcome tracking for affective vs. cognitive-perceptual symptom domains
- Formal MOA data retrieval from DrugBank API (DG002) to substantiate mechanistic rationale
- Health Canada package insert review for key warnings, contraindications, and drug interactions (DG001)
- Clarification of whether the target symptom cluster is impulsive/affective (SSRI-responsive) vs. cognitive-perceptual (likely requires antipsychotic augmentation)
- Health Canada DIN pipeline completion to accurately reflect Canada market status
- Careful risk stratification for patients with prominent quasi-psychotic features given the documented psychosis case report (PMID 9664779)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

