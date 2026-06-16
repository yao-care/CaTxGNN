---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flunarizine: From Vertigo to Migraine Disorder

## One-Sentence Summary

Flunarizine is a selective calcium channel blocker traditionally used for vertigo and vestibular disorders, widely established in Europe, Asia, and Latin America but not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **19 clinical trials** and **20 publications** currently supporting this direction — evidence already at Level L1, anchored by multiple completed head-to-head RCTs and international clinical guidelines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vertigo / Vestibular Disorders (traditional; no Canada DIN on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flunarizine is a selective calcium channel blocker acting primarily on voltage-dependent L- and T-type calcium channels. Its mechanism maps directly onto migraine pathophysiology at multiple levels: (1) it inhibits **cortical spreading depression (CSD)** — the core neurophysiological cascade underlying migraine aura and headache onset; (2) it suppresses abnormal neuronal firing within the trigeminal neurovascular system, dampening neurogenic inflammation; (3) it blocks calcium influx into cerebrovascular smooth muscle, preventing pathological vasospasm; and (4) its mild dopamine D2 receptor blockade activity may reduce central sensitization. Together, these complementary actions make flunarizine one of the most mechanistically well-founded options for migraine prevention.

The relationship between flunarizine's traditional use in vertigo and its predicted efficacy in migraine is not coincidental. Vestibular migraine is a recognized migraine phenotype, and the shared calcium-mediated pathophysiology means that flunarizine addresses both conditions through the same receptor targets. The 2023 European Headache Federation meta-analysis (PMID 37723437) explicitly characterizes flunarizine as "a repurposed, first- or second-line treatment for migraine prophylaxis," and it is listed on the WHO Essential Medicines List for this indication — further validating the TxGNN model's prediction.

Compared to other first-line prophylactics, flunarizine occupies a distinct mechanistic niche: it complements β-blockers (propranolol) and antiepileptics (topiramate) and is particularly useful for patients who cannot tolerate those agents. Multiple completed head-to-head RCTs confirm its efficacy is comparable to propranolol, topiramate, and amitriptyline in both adult and pediatric populations. The Canadian Headache Society (2012) guideline already references flunarizine within its evidence framework, creating a strong foundation for a Canadian market authorization application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | NA | Completed | 120 | Three-arm RCT: direct head-to-head comparison of greater occipital nerve block (GONB), topiramate, and flunarizine for episodic migraine prevention; outcomes assessed by post-treatment VAS scores and attack frequency reduction |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine (CM) prophylaxis — one of the few head-to-head trials conducted specifically in the chronic migraine subpopulation |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | NA | Unknown | 84 | RCT comparing flunarizine vs amitriptyline for migraine prophylaxis in a Pakistani tertiary care population; measured acute attack frequency and VAS pain scores across both sexes, ages 18–60 |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | NA | Recruiting | 44 | Pediatric RCT comparing flunarizine vs propranolol in children aged 8–15 using the validated PedMIDAS disability scale; addresses an evidence gap in the under-studied pediatric age group |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not Yet Recruiting | 460 | PREMI pragmatic multicentre trial: four-arm comparison of amitriptyline, flunarizine, topiramate, and propranolol as first-line migraine prophylaxis in primary care (Spain); powered for real-world effectiveness comparison |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Completed | 60 | RCT evaluating alpha-lipoic acid as add-on nutraceutical to background flunarizine therapy in adolescent migraineurs; establishes flunarizine's role as a standard reference treatment in adolescents |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | PK/DDI open-label study examining pharmacokinetic interaction between flunarizine and topiramate during mono- and concomitant therapy; defines safety parameters for combination use |
| [NCT00740259](https://clinicaltrials.gov/study/NCT00740259) | Phase 4 | Completed | 70 | Phase 4 RCT vs haloperidol testing flunarizine's D2 receptor blockade hypothesis; provides long-term safety characterization including extrapyramidal symptoms, weight gain, and depression risk |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Active, Not Recruiting | 60 | Observational comparison of transcutaneous pulsed radiofrequency therapy vs calcium channel blockers (including flunarizine) for childhood migraine; explores long-term effectiveness |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | NA | Unknown | 96 | RCT comparing acupuncture vs flunarizine hydrochloride as active comparator for migraine without aura; validates flunarizine as the standard-of-care reference arm in this setting |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Systematic Review + Meta-Analysis | J Headache Pain (EHF) | EHF critical re-appraisal confirming flunarizine as an evidence-based, repurposed first/second-line migraine prophylactic; formally rates strength of evidence for regulatory reimbursement decisions |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Systematic Review + Meta-Analysis | J Assoc Physicians India | Comparative meta-analysis of amitriptyline vs propranolol and flunarizine for migraine prophylaxis; flunarizine demonstrates comparable efficacy with a distinct side-effect profile |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | Network meta-analysis across pharmacological interventions for **pediatric** migraine prophylaxis; positions flunarizine within the comparative efficacy and safety landscape for children and adolescents |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic Review + Economic Model | Health Technol Assess | Systematic review comparing clinical effectiveness and cost-effectiveness of chronic migraine preventive drugs vs newer CGRP monoclonal antibodies; informs payer reimbursement frameworks |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Clinical Practice Guideline (CHS) | Can J Neurol Sci | **Canadian Headache Society guideline** for migraine prophylaxis in episodic migraine (≤14 headache days/month); directly relevant to the Canadian regulatory and prescribing context |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Clinical Practice Guideline (AAN) | Neurology | AAN/AHS updated evidence-based guideline for pharmacologic prevention of pediatric migraine, with specific evidence grading for flunarizine use in children |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | RCT | Acta Neurol Scand | RCT demonstrating that flunarizine combined with transcutaneous supraorbital neurostimulation (tSNS) significantly improves migraine prophylaxis outcomes compared to either modality alone |
| [9443168](https://pubmed.ncbi.nlm.nih.gov/9443168/) | 1997 | Post-Marketing Study | Pharm World Sci | Large prospective post-marketing study (n=686 migraine patients) comparing flunarizine vs propranolol; documents risk/benefit ratio including incidence of depression and extrapyramidal syndrome in real-world use |
| [3878734](https://pubmed.ncbi.nlm.nih.gov/3878734/) | 1985 | Clinical Study | Cephalalgia | Foundational study (n=75 migraine patients) establishing flunarizine 10 mg/day efficacy: 78.5% of treated patients showed favourable headache response; also characterized vestibular function effects |
| [35791513](https://pubmed.ncbi.nlm.nih.gov/35791513/) | 2022 | Clinical Trial | Brain Behav | Clinical evaluation of flunarizine combined with duloxetine for chronic migraine comorbid with depression and anxiety disorder; characterizes a high-prevalence comorbidity scenario in clinical practice |

---

## Canada Market Information

Flunarizine has no active Drug Identification Numbers (DINs) in Canada and is not currently marketed. No licensed products are on file with Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model's prediction for flunarizine in migraine disorder is supported by the strongest available level of clinical evidence (L1), including multiple completed Phase 4 head-to-head RCTs, a 2023 European Headache Federation meta-analysis, two international clinical practice guidelines (Canadian Headache Society 2012; AAN/AHS 2019), and WHO Essential Medicines List inclusion — making this one of the most evidence-rich drug repurposing candidates in this pipeline.

**To proceed, the following is needed:**

- **Health Canada regulatory pathway assessment**: Determine whether a New Drug Submission (NDS) or a hybrid pathway applies given flunarizine's long global post-marketing history
- **Safety dossier**: Retrieve and formally review the product monograph/package insert to characterize extrapyramidal symptoms, depression risk, and drug-drug interaction profile per Health Canada standards
- **Canadian market positioning**: Reconcile with the 2012 Canadian Headache Society guideline and assess competitive positioning vs currently approved prophylactics (propranolol, topiramate, amitriptyline, CGRP monoclonal antibodies)
- **Formulation confirmation**: Flunarizine is typically available as 5 mg and 10 mg capsules — confirm the target dosage form, strength, and route for the Canadian filing
- **Pediatric data package**: Given the evidence gap in pediatric populations specifically noted in the AAN guideline, determine whether a pediatric investigation plan is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

