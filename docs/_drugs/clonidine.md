---
layout: default
title: Clonidine
parent: Model Prediction Only (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Clonidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Clonidine: From Hypertension to Tourette Syndrome

## One-Sentence Summary

Clonidine is a centrally acting alpha-2 adrenergic agonist, originally used to treat hypertension, open-angle glaucoma and attention deficit hyperactivity disorder (ADHD).
The TxGNN model's top-ranked prediction is faciodigitogenital syndrome, but it has no supporting studies. The best-supported prediction is **Tourette syndrome**, with **2 clinical trials** and **19 publications**, including a European guideline and a network meta-analysis.
This report covers Tourette syndrome as the prediction with the strongest evidence. Other candidates are summarized briefly where relevant.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma, ADHD (the Canadian license records contain no indication text) |
| Predicted New Indication | Top-ranked by TxGNN: faciodigitogenital syndrome (no evidence, L5, Hold). Best-supported: **Tourette syndrome** |
| TxGNN Prediction Score | 99.98% for Tourette syndrome (99.999% for the top-ranked faciodigitogenital syndrome) |
| Evidence Level | L3 (Tourette syndrome) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Proceed with Guardrails (Tourette syndrome) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, clonidine is an alpha-2 adrenergic agonist. It reduces noradrenergic tone, which is the basis of its use in hypertension and ADHD.

Tourette syndrome is a neurodevelopmental tic disorder that frequently occurs together with ADHD. Reduced noradrenergic activity in prefrontal-striatal circuits is thought to ease both tics and ADHD symptoms. Clonidine is already named as a treatment option in the 2022 European clinical guidelines for tic disorders, and a 2023 network meta-analysis supports its use. Because the original ADHD indication overlaps closely with Tourette syndrome, this is a practical label-expansion candidate.

The other predictions are weaker:
- **Specific developmental disorder** (L4, Hold): plausible given clonidine's ADHD use, but the evidence is reviews and a mouse study, and the category is heterogeneous.
- **Manic bipolar disorder** (L3, Research Question): a 2023 systematic review and a 2022 randomized adjuvant study exist, but the only registered trial was terminated with 5 participants.
- **Migraine** (L3, Research Question): older small studies only, and a 2023 meta-analysis does not make clonidine a recommended option.
- **Obesity** (L3, Research Question): the trials are mechanistic studies of obesity-related hypertension and inflammation, not weight-loss trials.
- **Trichotillomania** (L5, Hold): only indirect mouse data.
- **Faciodigitogenital syndrome, chondromyxoid fibroma, hypervitaminosis and proximal 16p11.2 microdeletion syndrome** (L5, Hold): prediction only, with no trials or literature and no evident mechanistic rationale.

---

## Clinical Trial Evidence

Tourette syndrome:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Completed | 12 | Levetiracetam vs clonidine for tics in children with Tourette syndrome (crossover design); directly relevant but very small |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Unknown | 32 | Whether night-time clonidine improves day-time aggression in children with Tourette syndrome and comorbid ADHD; targets aggression rather than tics |

Trials for other predicted indications:

| Trial Number | Indication | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT01983462](https://clinicaltrials.gov/study/NCT01983462) | Obesity | Phase 2 | Terminated | 33 | Effect of sympathetic blockade with clonidine on vascular function in obese hypertensive adults |
| [NCT04934228](https://clinicaltrials.gov/study/NCT04934228) | Obesity | Phase 1 | Recruiting | 60 | Oral clonidine for 4 weeks to reduce inflammatory markers in obesity; no results yet |
| [NCT03065933](https://clinicaltrials.gov/study/NCT03065933) | Manic bipolar disorder | Phase 4 | Terminated | 5 | Open-label add-on extended-release clonidine as an anti-manic agent; negligible evidence |

---

## Literature Evidence

Tourette syndrome (selected from 19 retrieved publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Clinical guideline | Eur Child Adolesc Psychiatry | European guidelines (version 2.0) on pharmacological treatment of Tourette syndrome and tic disorders |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network meta-analysis | Lancet Child Adolesc Health | Compares efficacy, tolerability and acceptability of drugs for Tourette syndrome in young people |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Clinical study | Psychiatry Investigation | Efficacy and safety of the clonidine patch in Tourette syndrome with comorbid ADHD |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Review | Eur J Paediatr Neurol | Pharmacological options for Tourette syndrome with comorbid ADHD |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic review | Neurology | Systematic review of tic treatments (retrieved under the broader developmental-disorder prediction) |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic review | J Psychopharmacol | Assesses the quality of evidence for Tourette syndrome drug treatments |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Systematic review | J Child Psychol Psychiatry | Treatments for Tourette syndrome in children and young people |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Early clinical study | Lancet | Small doses of clonidine improved some children unresponsive to haloperidol |

---

## Canada Market Information

Health Canada lists 14 valid single-ingredient authorizations for clonidine and no cancelled ones. Dosage form, manufacturer and approved indication text are not available for these records. Five are shown:

| DIN | Product Name |
|---------|------|
| 02046148 | TEVA-CLONIDINE |
| 02538490 | CLONIDINE |
| 02516217 | SANDOZ CLONIDINE |
| 02304163 | TEVA-CLONIDINE |
| 02524198 | MAR-CLONIDINE |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found, and all 20 listed in the data are rated Moderate.
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - Diabetes medicines: insulin products, sulfonylureas (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide) and SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Others: bupropion, morphine, dronabinol
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): liver failure, anxiety and neurotic disorders, pancreatitis, systemic lupus erythematosus, hypotensive disorder, anuria, gout, myocardial infarction and ischemia, heart conduction disease, sudden cardiac arrest, respiratory failure, type 1 and type 2 diabetes, diabetic ketoacidosis, and several electrolyte or metabolic disorders. These need verification against the Canadian product monograph.
- **Population guardrails**: hypotension, bradycardia and sedation are expected concerns, particularly in children and in psychiatric populations.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Tourette syndrome)**

**Rationale:**
- Clonidine is already guideline-listed for tic disorders, and a network meta-analysis supports it. The only trials are small Phase 4 studies (n=12 and n=32), so the evidence is L3 rather than pivotal.
- The other predictions remain at Hold or Research Question, and the top-ranked prediction has no supporting evidence.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A review of clonidine's place in Tourette syndrome treatment from the guideline and meta-analysis, including comparison with approved alternatives
- Approved indication text and dosage forms for the Canadian authorizations, to confirm whether a label expansion would be needed
- A safety monitoring plan for blood pressure, heart rate and sedation, especially in children, and for patients with diabetes or cardiac conduction disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

