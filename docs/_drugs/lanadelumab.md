---
layout: default
title: Lanadelumab
parent: High Evidence (L1-L2)
nav_order: 521
evidence_level: L1
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Lanadelumab: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab is a monoclonal antibody originally used to prevent attacks of hereditary angioedema (HAE).
The TxGNN model predicts it may be effective for **C1 inhibitor deficiency**,
with **5 clinical trials** and **20 publications** currently supporting this direction.
Note that this predicted indication essentially matches the drug's existing use (HAE due to C1 inhibitor deficiency), so this is a confirmation of the on-label use rather than a true repurposing case.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary angioedema (including HAE with C1-INH deficiency) |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded. Based on known information, lanadelumab is a fully human monoclonal antibody that inhibits plasma kallikrein (target: KLKB1).

In C1 inhibitor deficiency, the loss of C1-INH control allows plasma kallikrein to act unchecked. This produces excess bradykinin, a vasodilator that drives the swelling attacks. By blocking kallikrein directly, lanadelumab addresses this pathway.

Because the predicted indication is the same disease family as the original indication, the prediction is highly consistent with the established mechanism. The other nine predicted diseases (e.g., serpinopathy, pancreatitis, platelet disorders, myositis) rest on model prediction alone, with no trials or literature, and are not recommended for further pursuit at this time.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING study: open-label safety, pharmacokinetics and efficacy in children 2 to <12 years with HAE |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Open-label safety, pharmacokinetics and efficacy in Chinese HAE patients over 26 weeks |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Open-label efficacy and safety in Japanese patients with HAE type I or II |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | Active, not recruiting | 155 | Japanese post-marketing survey of long-term safety and effectiveness of the 300 mg syringe |
| [NCT04583007](https://clinicaltrials.gov/study/NCT04583007) | N/A | No longer available | N/A | Expanded access program for pediatric HAE and non-histaminergic angioedema with normal C1-INH |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab vs placebo for prevention of HAE attacks (HELP trial) |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review / RCT subgroup | BioDrugs | Preclinical and Phase I review for HAE with C1-INH deficiency |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label extension | Allergy | HELP OLE: long-term effectiveness and safety in patients ≥12 years with HAE 1/2 |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network meta-analysis | Drugs in R&D | Comparison of long-term prophylaxis therapies (garadacimab, lanadelumab, SC C1-INH, berotralstat) |
| [40504359](https://pubmed.ncbi.nlm.nih.gov/40504359/) | 2025 | Real-world cohort | Advances in Therapy | EMPOWER: up to 36 months of sustained effectiveness and safety |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect comparison | J Comp Eff Res | Lanadelumab vs C1-esterase inhibitor in pediatric HAE |
| [31560114](https://pubmed.ncbi.nlm.nih.gov/31560114/) | 2019 | Review | Drugs | Review of lanadelumab in HAE; significant reduction in attacks vs placebo in HELP |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | First global approval profile |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case report | J Allergy Clin Immunol Pract | Efficacy of lanadelumab in acquired angioedema with C1-inhibitor deficiency |
| [39399485](https://pubmed.ncbi.nlm.nih.gov/39399485/) | 2024 | Case report | Front Immunol | Lanadelumab in a kidney transplant patient with HAE-C1INH |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02505614 | TAKHZYRO | Not listed | Not listed |
| 02480948 | TAKHZYRO | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: One pharmacology-based entry was found, which is the drug's own target, plasma kallikrein (KLKB1). It reflects the intended mechanism, not a drug-drug interaction.
- **Coagulation testing**: The data compiled for this report note that lanadelumab can prolong aPTT in laboratory assays, which may complicate coagulation monitoring.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 studies and a pivotal placebo-controlled RCT (HELP) support lanadelumab in HAE with C1-INH deficiency, and the product is already marketed in Canada. However, the Phase 3 trials are small, open-label and uncontrolled, and this is an on-label confirmation rather than a new indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently missing and needed for safety screening)
- Approved indication text and dosage form for the two Canadian DINs
- Formal mechanism of action data from DrugBank
- Safety monitoring plan, including attention to coagulation assay interference
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

