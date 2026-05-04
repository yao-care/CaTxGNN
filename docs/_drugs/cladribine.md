---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 7
---

# Cladribine
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog historically used to treat hairy cell leukemia (and more recently approved for relapsing multiple sclerosis), working by accumulating as cytotoxic triphosphate metabolites inside lymphoid cells and triggering apoptosis through DNA strand-break induction.
The TxGNN model predicts it may have activity against **Parameningeal Embryonal Rhabdomyosarcoma**, a rare pediatric soft-tissue sarcoma — however, there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction, placing evidence squarely at L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Health Canada regulatory data on file; known established use: hairy cell leukemia / relapsing multiple sclerosis |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cladribine (2-chloro-2'-deoxyadenosine, 2-CdA) is resistant to inactivation by adenosine deaminase. Inside target cells it is phosphorylated by deoxycytidine kinase (dCK) to its active triphosphate form, which then incorporates into DNA, inhibits both DNA polymerase and DNA ligase, depletes NAD⁺/ATP, and triggers p53-independent apoptosis. Its clinical selectivity for lymphoid malignancies — most notably hairy cell leukemia — derives from the exceptionally high dCK / 5'-nucleotidase ratio in lymphocytes, which drives intracellular drug accumulation. Detailed MOA data from DrugBank were not available in the current evidence pack; the above is based on published pharmacology literature.

Parameningeal embryonal rhabdomyosarcoma is a mesenchymal tumor arising from primitive skeletal muscle precursor cells, anatomically located adjacent to meningeal surfaces (orbit, nasopharynx, paranasal sinuses, middle ear). Biologically, it is entirely distinct from lymphoid tissue — the cell of origin, the signaling pathways driving proliferation (PAX-FOXO1 fusions in alveolar subtype; RAS/MAPK activation in embryonal subtype), and the tumor microenvironment all differ fundamentally from lymphoid malignancies. The TxGNN knowledge graph appears to derive this prediction through a shared "cell proliferation → DNA damage → tumor suppression" pathway chain, likely amplified by ontological clustering of rhabdomyosarcoma subtype nodes in the graph. A similar pattern is observed across all seven top-ranked predictions in this evidence pack — every indication is a rhabdomyosarcoma variant, strongly suggesting a graph topology artifact rather than disease-specific biological signal.

It is worth noting that Cladribine does have a documented, evidence-backed use in Langerhans cell histiocytosis (LCH) and systemic mastocytosis — both histiocytic/myeloid disorders that also carry MAPK pathway activation. This demonstrates some oncological range beyond hairy cell leukemia. However, the leap from histiocytic disease to mesenchymal soft-tissue sarcoma remains mechanistically unjustified without dedicated preclinical data. The high TxGNN score should be interpreted as a hypothesis-generating signal, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cladribine in parameningeal embryonal rhabdomyosarcoma or any rhabdomyosarcoma subtype in this evidence pack.

---

## Canada Market Information

Cladribine has no Health Canada-authorized products on record (0 DINs). The drug is not currently marketed in Canada under any trade name within this dataset. Internationally, it is available as **Leustatin** (intravenous, for hairy cell leukemia) and **Mavenclad** (oral tablets, for relapsing multiple sclerosis) in other jurisdictions.

---

## Cytotoxicity

Cladribine is a cytotoxic antineoplastic agent belonging to the purine analog class.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analog (adenosine deaminase-resistant, dCK-activated) |
| Myelosuppression Risk | High — profound and prolonged lymphopenia is the hallmark toxicity (CD4⁺ and CD8⁺ T-cell depletion lasting months to years); neutropenia and thrombocytopenia also common with IV formulation |
| Emetogenicity Classification | Low (IV Leustatin regimen); low to minimal (oral Mavenclad) |
| Monitoring Items | CBC with differential at baseline and regularly (lymphocyte count, CD4⁺ T-cell count); renal function (creatinine/eGFR); hepatic function (ALT, AST); screen for latent TB and viral reactivation (HBV, VZV, CMV, JC virus) prior to initiation |
| Handling Protection | Yes — must be handled under cytotoxic drug precautions per institutional hazardous drug policies; IV preparation requires a biological safety cabinet |

---

## Safety Considerations

Please refer to the product monograph / SmPC for complete safety information. No Health Canada-specific warning or contraindication data were present in the current evidence pack. Based on established pharmacology, known class-level concerns include: severe prolonged lymphopenia and secondary opportunistic infections (including progressive multifocal leukoencephalopathy), teratogenicity and embryotoxicity (Category X in pregnancy, mandatory contraception period), potential for secondary malignancies with repeated courses, and renal dose adjustment requirements. These should be formally documented from the authorized product label before any clinical use decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a numerically high TxGNN score (99.77%), the prediction rests entirely on L5 evidence — computational model output only — with zero supporting clinical trials, case reports, or preclinical studies in rhabdomyosarcoma of any subtype. More critically, Cladribine's established mechanism of action is dependent on a biochemical environment (high dCK/5'-nucleotidase ratio) characteristic of lymphoid cells, which is not present in mesenchymal tumors; this represents a fundamental biological barrier, not merely an evidence gap.

**To proceed, the following is needed:**

- **Preclinical validation (gating requirement):** Test Cladribine in embryonal RMS cell lines (e.g., RD, SMS-CTR) and patient-derived xenograft (PDX) models — specifically measuring intracellular dCK activity and drug accumulation to determine whether activation is even feasible in this tumor type
- **MOA data resolution:** Retrieve full DrugBank entry (DB00242) and authorized product monograph to formally document mechanism and enable proper indication-mechanism mapping (DG002 remediation)
- **Safety data resolution:** Download and parse the relevant product monograph to complete the safety profile assessment (DG001 remediation)
- **Knowledge graph audit:** Investigate why all seven top-ranked predictions are rhabdomyosarcoma subtypes — if this reflects graph node clustering rather than biological signal, a graph calibration review may be warranted to improve prediction specificity for this drug-class
- **Regulatory pathway check:** If preclinical data are positive, determine whether orphan drug designation pathways (RMS qualifies as a rare pediatric disease) would support a feasibility study within a pediatric oncology cooperative group (e.g., COG ARST basket trial framework)

> ⚠️ **Research use only.** This report is generated for drug repurposing research purposes and does not constitute medical advice. All repurposing candidates require rigorous clinical validation before any patient application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

