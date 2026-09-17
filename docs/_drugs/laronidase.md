---
layout: default
title: Laronidase
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Laronidase: From Mucopolysaccharidosis I to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase (recombinant human alpha-L-iduronidase) is the enzyme replacement therapy already used worldwide for Mucopolysaccharidosis I (MPS I). TxGNN's top prediction — "lysosomal storage disease with skeletal involvement" — is not a genuinely new indication but a near-synonym for the skeletal manifestations of MPS I itself, supported by **4 publications** (no dedicated clinical trials) rather than novel repurposing evidence. The drug is currently **not marketed in Taiwan** (0 licenses on file), so the practical question here is market access, not drug discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in Taiwan regulatory data (drug unmarketed); internationally approved for Mucopolysaccharidosis I (MPS I, alpha-L-iduronidase deficiency) |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 (observational/cohort evidence; no completed RCTs specific to this label) |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

`original_moa` is marked as a data gap in the DrugBank record field, but the literature in this evidence pack directly describes the mechanism: laronidase is a recombinant form of human alpha-L-iduronidase, the lysosomal enzyme absent in MPS I. It is taken up by fibroblasts and osteoblasts mainly via mannose-6-phosphate receptors and transported to lysosomes, where it degrades the accumulated glycosaminoglycans (dermatan sulfate, heparan sulfate) responsible for the disease (PMID 18758061).

The predicted indication, "lysosomal storage disease with skeletal involvement," is essentially the same disease process laronidase was built for — skeletal dysplasia and joint stiffness are core, well-documented features of MPS I (PMID 25345091). This is best understood as the model **re-identifying an already-known indication** rather than proposing a new mechanistic hypothesis: the drug-disease link is direct and causal (enzyme replaces the missing enzyme), not inferential.

TxGNN also flagged a second candidate, **Sanfilippo syndrome (MPS III)**, with a similar score (99.22%) but a much weaker rationale: Sanfilippo results from deficiency of different enzymes in the heparan sulfate pathway (SGSH/NAGLU/HGSNAT/GNS), not alpha-L-iduronidase. Every retrieved publication for this candidate actually discusses laronidase in MPS I, not Sanfilippo — none provide direct evidence of efficacy in Sanfilippo syndrome. This score is best explained by network similarity between lysosomal storage diseases rather than a real pharmacological link, and the corresponding recommendation is **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Describes MPS I disease spectrum (Hurler, Scheie, Hurler-Scheie), including skeletal involvement; diagnosis via urine GAGs and enzyme assay |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review/Drug monograph | BioDrugs | BioMarin's development of laronidase as ERT for MPS I; received US/EU orphan drug designation and FDA fast-track status |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Cohort | Pediatric Neurology | 6.5-year follow-up of ERT in a Scheie syndrome patient, including skeletal radiographs; overall status declined despite treatment |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | Mechanistic/In-vitro | Biological & Pharmaceutical Bulletin | Laronidase is taken up dose-dependently by MPS I fibroblasts/osteoblasts via mannose-6-phosphate receptors, confirming lysosomal delivery mechanism |

---

## Taiwan Market Information

Laronidase is not currently marketed in Taiwan — no licenses (許可證) are on file, and no product/dosage-form data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications could not be retrieved for this drug (data gap, Blocking severity) — this must be resolved before any safety pre-assessment (S1) can be completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction is mechanistically sound because it is functionally the drug's already-established indication (MPS I with skeletal involvement) rather than a novel repurposing hypothesis, so pharmacological risk is low. However, this is currently unsupported by dedicated clinical trials in the evidence pack and the drug is unmarketed in Taiwan, so any path forward is a market-access/registration exercise, not new drug development. The second candidate, Sanfilippo syndrome, lacks mechanistic and evidentiary support and should be held.

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) — currently a Blocking data gap preventing safety pre-assessment
- Confirmed DrugBank/manufacturer mechanism-of-action documentation (to formally replace the current "[Data Gap]" MOA field)
- Regulatory pathway assessment for Taiwan market entry (e.g., via existing Aldurazyme approvals in other jurisdictions)
- No further action recommended on the Sanfilippo syndrome candidate absent disease-specific preclinical or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

