---
layout: default
title: Diatrizoate
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Diatrizoate
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

# Diatrizoate: From Radiographic Contrast Agent to Osteoarthritis Susceptibility

## One-Sentence Summary

Diatrizoate is an ionic iodinated contrast agent used primarily for radiographic imaging procedures such as urography, angiography, and arthrography.
The TxGNN model predicts it may be effective for **Osteoarthritis Susceptibility** (rank #1, score 99.08%), yet **no clinical trials or publications** directly support a therapeutic role — and evidence for the related hemoglobinopathy prediction (rank #4) documents active harm rather than benefit.
All 10 predicted indications are at the lowest evidence tier (L5), and the predictions appear to reflect diagnostic co-occurrence in the knowledge graph rather than genuine therapeutic relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Radiographic contrast agent for imaging procedures |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for diatrizoate in this evidence pack. Based on known pharmacological properties, diatrizoate is an ionic, high-osmolality iodinated contrast medium belonging to the triiodobenzoic acid derivative class. Its high iodine content renders it radiopaque, enabling visualization of body cavities, vasculature, and joint spaces during imaging — its established clinical role.

The TxGNN model's clustering of diatrizoate with musculoskeletal conditions (osteoarthritis susceptibility, osteoarthritis, rheumatoid arthritis — ranks 1, 2, 3) most likely originates from the **EPIC (Equilibrium Partitioning of Ionic Contrast agent)** principle: diatrizoate's negative charge allows it to partition inversely with sulfated glycosaminoglycan (sGAG) content in cartilage matrix, making it useful for EPIC-µCT imaging of cartilage health. This physical-chemistry property has been explored diagnostically (PMID [25602512](https://pubmed.ncbi.nlm.nih.gov/25602512/)), but **it is a diagnostic principle, not a therapeutic mechanism**. No established biological pathway has been proposed by which diatrizoate would treat or prevent osteoarthritis.

A critical concern emerges from the rank-4 prediction (hemoglobinopathy): multiple case reports and observational studies document that diatrizoate, as a hyperosmolar ionic agent, **actively induces erythrocyte sickling and acute intravascular hemolysis** in patients with sickle cell disorders. The knowledge graph co-occurrence driving these TxGNN predictions reflects adverse event documentation and imaging procedure co-citations, not treatment relationships — illustrating a systematic model limitation for diagnostic agents whose disease co-occurrence is procedural rather than therapeutic.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis susceptibility.

> **Context note:** Two trials were retrieved under the broader "osteoarthritis" query but are not relevant to diatrizoate as a therapeutic agent:
> - [NCT01279395](https://clinicaltrials.gov/study/NCT01279395) — Terminated (n=3); studied anti-inflammatory drugs and cholesterol metabolism; diatrizoate not involved therapeutically.
> - [NCT00550524](https://clinicaltrials.gov/study/NCT00550524) — Status unknown (n=5); autologous bone marrow stem cell therapy for knee OA; diatrizoate role, if any, was as an imaging adjunct only.

---

## Literature Evidence

Currently no related literature available for osteoarthritis susceptibility.

> **Context note:** Literature retrieved for related queries (rheumatoid arthritis: 12 publications; osteoarthritis: 4 publications) is exclusively diagnostic in nature — arthrography studies, joint clearance pharmacokinetics, and EPIC-µCT cartilage imaging. Representative publications are listed below for completeness:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [5788057](https://pubmed.ncbi.nlm.nih.gov/5788057/) | 1969 | Diagnostic Imaging | Br J Radiol | Arthrography of the knee in rheumatoid arthritis — diatrizoate used as imaging contrast, not as treatment |
| [5421242](https://pubmed.ncbi.nlm.nih.gov/5421242/) | 1970 | Pharmacokinetic/Observational | Acta Rheumatol Scand | Clearance of ¹²⁵I-labelled urographin (diatrizoate salt) from RA knee joints — pharmacokinetic observation only |
| [6828677](https://pubmed.ncbi.nlm.nih.gov/6828677/) | 1983 | Diagnostic Imaging | Radiology | Arthrography of traumatized wrist; characterises soft-tissue injuries via contrast — diagnostic use only |
| [25602512](https://pubmed.ncbi.nlm.nih.gov/25602512/) | 2015 | Ex vivo / EPIC-µCT | Connective Tissue Res | EPIC-µCT used to observe sGAG content changes in elderly hip cartilage — diatrizoate as diagnostic tracer |
| [1147166](https://pubmed.ncbi.nlm.nih.gov/1147166/) | 1975 | Diagnostic Imaging | Am J Roentgenol | Arthrography in hip osteoarthritis — diagnostic application |

*All retrieved literature documents diagnostic or procedural uses only. None supports a therapeutic role in any musculoskeletal indication.*

---

## Canada Market Information

Diatrizoate is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on record with Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Critical Safety Signal Identified During Evidence Review**
>
> Although structured safety data (formal warnings/contraindications) was not available in this evidence pack, a review of retrieved literature for the rank-4 predicted indication (hemoglobinopathy) reveals the following well-documented adverse effects:
>
> - **Erythrocyte sickling induction:** Diatrizoate, as a hyperosmolar ionic contrast agent, has been documented to induce sickling of red blood cells *in vitro* and *in vivo* in patients with sickle cell disease (HbSS, HbSC). See PMID [3985742](https://pubmed.ncbi.nlm.nih.gov/3985742/), [5121421](https://pubmed.ncbi.nlm.nih.gov/5121421/).
> - **Acute intravascular hemolysis:** Case reports describe severe hemolysis and pulmonary complications following diatrizoate administration for coronary angiography in patients with HbSC disease. See PMID [3985742](https://pubmed.ncbi.nlm.nih.gov/3985742/), [7313758](https://pubmed.ncbi.nlm.nih.gov/7313758/).
> - **Serious neurological events:** Post-angiographic cortical blindness and cerebral infarction reported in a patient with homozygous sickle cell disease. PMID [1601612](https://pubmed.ncbi.nlm.nih.gov/1601612/) explicitly recommends low-osmolar contrast media instead of ionic agents in this population.
> - **Fatal outcome on record:** A fatality following selective coronary angiography in a patient with sickle cell haemoglobin is documented. See PMID [4638407](https://pubmed.ncbi.nlm.nih.gov/4638407/).
>
> Any further evaluation of diatrizoate for any therapeutic indication must account for these established harms in patients with haemoglobin disorders and any condition associated with compromised renal function.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for diatrizoate are evidence level L5 (model prediction only, no therapeutic studies), and the dominant pattern across retrieved evidence is diagnostic/procedural co-occurrence — not biological treatment relationships. The hemoglobinopathy prediction (rank 4, score 98.46%) is uniquely concerning because the existing literature documents serious harm from diatrizoate in that population, not benefit.

**To proceed, the following is needed:**
- **Formal MOA characterization:** DrugBank/literature review to document complete pharmacological profile of diatrizoate beyond its contrast imaging role
- **Preclinical therapeutic hypothesis testing:** If the EPIC cartilage-penetration property is proposed to have therapeutic value (e.g., modulation of cartilage proteoglycan metabolism), dedicated in vitro and in vivo studies would be required before any clinical consideration
- **TxGNN model audit for diagnostic agents:** A systematic review of how frequently high TxGNN scores for contrast agents and diagnostic tools reflect imaging co-occurrence rather than therapeutic potential — this case may serve as a benchmark for flag rules
- **Health Canada regulatory review:** Confirm current status of all diatrizoate-containing products in Canada (including any historical DIN records) and retrieve the approved product monograph for formal safety review
- **Safety contraindication mapping:** Formal compilation of contraindications (sickle cell disease, severe renal impairment, hypersensitivity to iodinated agents) before any indication expansion is considered

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

