---
layout: default
title: Lovastatin
parent: Moderate Evidence (L3-L4)
nav_order: 563
evidence_level: L3
indication_count: 6
last_modified_at: 2026-10-13
description: "Lovastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L3). Approved use: Hyperlipidemia, familial hyperlipidemia, hypertriglyceridemia…"
monitor_inn: "LOVASTATIN"
predicted_indications: ["homozygous familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency"]
---

# Lovastatin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Lovastatin: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a statin (HMG-CoA reductase inhibitor) originally used to treat hyperlipidemia, including familial forms, and atherosclerosis.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, with **1 clinical trial** (which tests a different drug, so it is not direct evidence) and **20 publications** compiled for this direction. Several of these publications are small lovastatin case series, and they show a limited and variable response.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia, familial hyperlipidemia, hypertriglyceridemia, atherosclerosis (Canadian licence text for the indication is not available) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, lovastatin inhibits HMG-CoA reductase, the rate-limiting enzyme in cholesterol synthesis. This lowers hepatic cholesterol and upregulates LDL receptors, which increases clearance of LDL cholesterol from the blood.

HoFH is a severe inherited form of hypercholesterolemia caused by a defect in the LDL receptor. It is closely related to lovastatin's original lipid-lowering indications. However, the drug's effect depends on residual LDL receptor activity. Patients with receptor-defective mutations may respond partly, while receptor-negative patients show little or no response. A published paediatric series in receptor-negative HoFH found no reduction in LDL cholesterol on lovastatin. So the prediction is plausible, but efficacy is likely limited to a subset of patients.

Five other predicted indications were also reviewed:

- **Hyperlipoproteinemia** and **familial hypercholesterolemia** are essentially on-label or near-label uses. Both have lovastatin-specific evidence, including a placebo-controlled angiographic study and adolescent FH trials. Both reach evidence level L1 with a recommendation of Proceed with Guardrails.
- **Cholesterol 7α-hydroxylase deficiency**, **CETP deficiency** and **hepatic lipase deficiency** have no lovastatin-specific clinical evidence. Their high TxGNN scores appear to reflect closeness within the lipid pathway rather than clinical support. All three are rated Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (not lovastatin) in children and adolescents aged 8–17 with HoFH, measuring LDL-C reduction at Week 12. It shows disease-context relevance only, not lovastatin efficacy. |

---

## Literature Evidence

The table below lists the most relevant publications. Lovastatin-specific HoFH reports are prioritised, followed by reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Case series | J Pediatr | Three children with receptor-negative HoFH on lovastatin 2 mg/kg/day showed no decrease in LDL-C and no change in LDL turnover. |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Clinical study | An Esp Pediatr | Two HoFH patients on lovastatin combined with probucol and cholestyramine. LDL receptor status was linked to the response. |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Case report | An Esp Pediatr | A receptor-defective HoFH patient treated with combined cholestyramine and lovastatin. |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case report | JAMA | A child with HoFH reached normal cholesterol on lovastatin after liver transplantation, which restored about 60% of LDL receptor activity. |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case report | Eur J Pediatr | LDL apheresis (HELP) in a 7-year-old girl with HoFH, with and without lovastatin. |
| [2912429](https://pubmed.ncbi.nlm.nih.gov/2912429/) | 1989 | Review | Arteriosclerosis | Plasma exchange and LDL apheresis in HoFH. Combining lovastatin with apheresis was under assessment. |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | Clinical study | Arteriosclerosis | Drug treatment of children with FH, including 3 with HoFH. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical treatment of dyslipidemia in children, including lovastatin. |
| [12063772](https://pubmed.ncbi.nlm.nih.gov/12063772/) | 2001 | Review | Nutr Metab Cardiovasc Dis | Why and when to use statins in children with FH. |
| [3278832](https://pubmed.ncbi.nlm.nih.gov/3278832/) | 1988 | Review | Clin Pharm | Chemistry, pharmacology, efficacy and adverse effects of lovastatin. |

The remaining publications are reviews of other agents (ezetimibe, rosuvastatin, atorvastatin) or indirect papers on lipoprotein or LDL receptor biology. They are not listed here.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02220180 | LOVASTATIN | Not specified | Not specified |
| 02220172 | LOVASTATIN | Not specified | Not specified |

Both licences are valid single-ingredient products.

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: The TxGNN knowledge graph links lovastatin to the following conditions. Examples include liver disease, gallbladder disease, myopathy and other muscle diseases, rhabdomyolysis, thrombocytopenia, diabetes mellitus and diabetic ketoacidosis, hyperglycemia, gout, peptic ulcer disease, hypotensive disorder, blood coagulation disease, acute coronary syndrome, coronary artery disease, myocardial infarction and substance abuse/dependence. These are not confirmed label contraindications and should be checked against the product monograph.
- **Drug interactions**: 100 interactions were found in total, and 20 are listed in the compiled data. Notable ones:
  - **Major**: clarithromycin.
  - **Moderate**: aprepitant, omeprazole, esomeprazole, lansoprazole, pantoprazole, metronidazole, tinidazole, cimetidine, clotrimazole, miconazole, naltrexone, eluxadoline, pectin, rosuvastatin, simvastatin and troglitazone.
  - **Minor**: exenatide.
  - **Unknown level**: calcitriol and glimepiride.
  
  Lovastatin is a CYP3A4 substrate, so strong inhibitors carry a particular risk of myopathy. Combining two statins (rosuvastatin, simvastatin) is not advisable.
- **Suggested guardrails**: Monitor liver enzymes and creatine kinase. Review the interaction burden before prescribing. Use caution in pregnancy and in children.

Warnings and contraindications from the Canadian product monograph were not available. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
- The prediction is mechanistically plausible, but the only listed trial tests alirocumab rather than lovastatin. The lovastatin evidence for HoFH is limited to a few small, old case series and reports, and one of these shows no LDL-C reduction in receptor-negative patients. Response likely depends on residual LDL receptor function.
- Of the other predicted indications, hyperlipoproteinemia and familial hypercholesterolemia are on-label or near-label and could proceed with guardrails. The remaining three have no supporting clinical evidence.

**To proceed, the following is needed:**
- Canadian product monograph warnings, contraindications and approved indication text for DINs 02220180 and 02220172. These are currently missing and block safety screening.
- Mechanism-of-action data from DrugBank.
- Lovastatin-specific data in HoFH stratified by LDL receptor status (receptor-defective vs receptor-negative), ideally from a prospective study.
- A comparison against current HoFH standards of care (for example more potent statins, add-on therapies and LDL apheresis) to define any role for lovastatin.
- A safety monitoring plan covering liver function, creatine kinase and interaction management, especially in paediatric patients.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

