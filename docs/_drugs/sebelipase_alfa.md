---
layout: default
title: Sebelipase Alfa
parent: Model Prediction Only (L5)
nav_order: 837
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sebelipase Alfa: predicted new indication Cholesteryl ester storage disease (evidence level L5). Approved use: Wolman disease"
monitor_inn: "Sebelipase alfa"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant", "cholesteryl ester storage disease", "Gaucher disease", "lysosomal storage disease with skeletal involvement", "autosomal ichthyosis syndrome with fatal disease course", "Tay-Sachs disease", "benign neoplasm of adrenal gland"]
---

# Sebelipase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Sebelipase alfa: From Lysosomal Acid Lipase Deficiency to Cholesteryl Ester Storage Disease
{: .text-alpha }

## One-Sentence Summary

Sebelipase alfa is a recombinant human lysosomal acid lipase (LAL) enzyme replacement therapy, originally used for Wolman disease and lysosomal acid lipase deficiency.
The TxGNN model's top-scoring prediction is Scheie syndrome, but it has no supporting evidence. The best-supported prediction is **cholesteryl ester storage disease (CESD)**, with **8 clinical trials** and **20 publications**. CESD is the later-onset form of LAL deficiency, so this is effectively an on-label indication rather than a true repurposing case.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Wolman disease; lysosomal acid lipase deficiency; lysosomal lipid storage disorder |
| Predicted New Indication | Cholesteryl ester storage disease (best-supported of the top 10 predictions; the top-ranked prediction, Scheie syndrome, has no evidence) |
| TxGNN Prediction Score | 99.72% (CESD); 99.80% (Scheie syndrome, rank 1) |
| Evidence Level | L1 (CESD) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails (CESD) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, sebelipase alfa is recombinant human lysosomal acid lipase. It replaces the missing enzyme in LAL deficiency, which reduces lysosomal accumulation of cholesteryl esters and triglycerides.

CESD is the later-onset, attenuated form of LAL deficiency, and Wolman disease is the severe infantile form. Both lie on the same disease spectrum as the drug's original indications, so the mechanistic link is direct. Phase 3 randomized trial data showed improvements in ALT and lipid parameters, and long-term extension data support durability.

Most other top-ranked predictions are not mechanistically supported:
- **Scheie syndrome and Hurler syndrome** (MPS I) are caused by alpha-L-iduronidase deficiency, a different enzyme acting on different substrates.
- **Gaucher disease** and **Tay-Sachs disease** involve other enzymes (glucocerebrosidase and hexosaminidase A). Sebelipase alfa does not act on their substrates.
- **Growth hormone insensitivity syndrome with immune dysregulation 2**, **autosomal ichthyosis syndrome**, **lysosomal storage disease with skeletal involvement** and **benign adrenal neoplasm** have no plausible mechanistic link. They appear to be knowledge-graph artifacts.

---

## Clinical Trial Evidence

The table covers CESD, the best-supported prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Phase 3 | Completed | 66 | Randomized, placebo-controlled study of sebelipase alfa 1 mg/kg every other week in late-onset LAL-D (CESD). Pivotal evidence, published in NEJM 2015 |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Phase 2 | Completed | 31 | Open-label multicenter study of safety and efficacy in a broad LAL-D population |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Phase 2/3 | Completed | 9 | Open-label dose-escalation study in children with growth failure due to LAL-D |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Phase 2 | Completed | 8 | Extension study of long-term safety and tolerability in adults with liver dysfunction due to LAL-D |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Phase 1/2 | Completed | 9 | First clinical study, a dose escalation in adults with liver dysfunction due to LAL-D |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Phase 2 | Terminated | 10 | Open-label study in infants with rapidly progressive LAL-D. Early termination limits interpretation |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | N/A | No longer available | N/A | Expanded access protocol (1 mg/kg every other week) until commercial product was available. No efficacy data |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | PEARL prenatal enzyme replacement platform study for lysosomal storage disorders. Not specific to CESD |

For the other predictions, only NCT04532047 appears (for Hurler syndrome and Gaucher disease). It is a platform study with no demonstrated efficacy data for sebelipase alfa in those diseases.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26352813](https://pubmed.ncbi.nlm.nih.gov/26352813/) | 2015 | RCT | N Engl J Med | Phase 3 trial of enzyme replacement in children and adults with LAL deficiency, an underappreciated cause of cirrhosis and severe dyslipidemia |
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | Cohort | J Hepatol | Final results of the phase III randomized ARISE study in children aged ≥4 years and adults |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Cohort | J Pediatr Gastroenterol Nutr | Long-term single-arm open-label study (NCT02112994) of efficacy and safety |
| [32657505](https://pubmed.ncbi.nlm.nih.gov/32657505/) | 2020 | Cohort | Liver Int | 5-year extension data: lower transaminases and liver fat, improved lipids |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | Cohort | J Clin Lipidol | Improved atherogenic biomarkers over up to 52 weeks in ARISE |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Cohort | Liver Int | Registry data: improved aminotransferase levels in treated vs untreated patients |
| [34664536](https://pubmed.ncbi.nlm.nih.gov/34664536/) | 2022 | Review | Expert Opin Drug Saf | Safety review of sebelipase alfa in LAL deficiency |
| [37181111](https://pubmed.ncbi.nlm.nih.gov/37181111/) | 2021 | Systematic review | Ther Adv Rare Dis | Systematic literature review of enzyme replacement therapy in LAL-D |
| [38918870](https://pubmed.ncbi.nlm.nih.gov/38918870/) | 2024 | Cohort | Orphanet J Rare Dis | Twice-weekly dosing rescued severely ill infants with Wolman disease |
| [34906190](https://pubmed.ncbi.nlm.nih.gov/34906190/) | 2021 | Cohort | Orphanet J Rare Dis | Nationwide Wolman disease cohort with up to ten years of follow-up |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02469596 | KANUMA | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: No drug interaction records were found.
- **Guardrails from the evidence review**: Monitor for infusion-related and hypersensitivity reactions and for anti-drug antibodies. Infants (Wolman disease) need close monitoring, and dosing may need to be individualized.

For full warnings and contraindications, please refer to the Health Canada package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (CESD and Wolman disease variants). Hold for all other predictions.**

**Rationale:**
- CESD is supported by a completed Phase 3 randomized placebo-controlled trial plus multiple Phase 2 studies and long-term follow-up. However, it is the same disease spectrum as the approved indication, so it is not a true repurposing finding.
- The Wolman disease variant (L2) is supported mainly by infant open-label studies and case series mapped from LAL deficiency studies.
- Scheie syndrome (rank 1), Hurler syndrome, Gaucher disease, Tay-Sachs disease and the remaining predictions have high model scores but no mechanistic or clinical support (L5).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Approved indication text and dosage form for the Canadian licence
- A safety monitoring plan for infusion reactions and anti-drug antibodies, especially in infants
- For any non-LAL-D prediction: preclinical or mechanistic evidence before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

