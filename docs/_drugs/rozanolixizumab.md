---
layout: default
title: Rozanolixizumab
parent: Model Prediction Only (L5)
nav_order: 827
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rozanolixizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Generalized myasthenia gravis (anti-AChR or anti-MuSK antibody positi…"
monitor_inn: "Rozanolixizumab"
predicted_indications: ["bronchitis", "plasma cell myeloma", "indolent plasma cell myeloma", "hemoglobinopathy", "gastric carcinoma", "partial deletion of the short arm of chromosome 16", "diffuse gastric adenocarcinoma", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyruvate kinase deficiency of red cells"]
---

# Rozanolixizumab
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

# Rozanolixizumab: From Myasthenia Gravis (Anti-FcRn Therapy) to Bronchitis

## One-Sentence Summary

Rozanolixizumab is an anti-FcRn monoclonal antibody that lowers circulating IgG. It is marketed in Canada as RYSTIGGO and has been authorised elsewhere for generalized myasthenia gravis.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials and no publications** were found to support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Generalized myasthenia gravis (anti-AChR or anti-MuSK antibody positive). This comes from the FDA approval described in the pharmacology data, because the Canadian licence record has no indication text. |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 95.28% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known information, rozanolixizumab is an antibody that targets the neonatal Fc receptor (FcRn, encoded by FCGRT). Blocking this receptor shortens the half-life of IgG and lowers circulating IgG, including pathogenic autoantibodies. That is the basis for its use in antibody-mediated disease such as myasthenia gravis.

A plausible link would be reducing pathogenic IgG in antibody-mediated conditions. However, bronchitis is mostly infectious or irritant-driven and is not IgG-mediated. Lowering IgG would also be expected to raise infection risk, which argues against benefit. The high TxGNN score is therefore a computational association only, with no supporting mechanistic or clinical data.

For completeness, the other top predictions (plasma cell myeloma, indolent plasma cell myeloma, hemoglobinopathy, gastric carcinoma and others) are likewise L5 with no trials or literature. They are all rated Hold. The IgG-lowering rationale is at most theoretical for IgG-type myeloma paraprotein, and it has no plausible basis for the remainder.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02556081 | RYSTIGGO | Not listed | Not listed in the licence record |

---

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacology target entry, not a clinical interaction. It shows that rozanolixizumab binds the Fc fragment of IgG receptor and transporter (FCGRT, i.e. FcRn). No interaction severity level is given.
- **Mechanism-related concern**: IgG lowering may increase susceptibility to infection. This matters particularly for a respiratory condition such as bronchitis, and also for myeloma.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for bronchitis is supported only by the model score (L5). There are no trials or publications, and the mechanism does not fit, because bronchitis is not IgG-mediated and IgG depletion could worsen infection risk.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for the Canadian licence
- Detailed mechanism of action data
- A credible biological rationale, plus preclinical or clinical evidence, linking FcRn blockade to bronchitis
- Infection-risk assessment in the proposed population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

