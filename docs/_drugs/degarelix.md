---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Advanced Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix is a GnRH receptor antagonist used internationally for the treatment of advanced prostate cancer, rapidly suppressing testosterone to castrate levels by blocking pituitary GnRH receptors.
The TxGNN model predicts it may be effective for **Hypertrichosis**, a condition of abnormal excessive hair growth;
however, **no clinical trials and no supporting literature** have been identified for this repurposing direction, leaving evidence at the lowest possible tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced prostate cancer (hormone-sensitive) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence package. Based on established pharmacological knowledge, Degarelix is a synthetic decapeptide GnRH receptor antagonist. Unlike GnRH agonists, it directly and competitively blocks pituitary GnRH receptors without an initial testosterone surge ("flare"), causing rapid and sustained suppression of LH, FSH, and consequently serum testosterone to castrate levels (< 0.5 ng/mL). This property makes it effective in hormone-sensitive advanced prostate cancer, where tumour growth is driven by androgens.

The theoretical basis for a connection to hypertrichosis is that sex hormones — particularly androgens and estrogens — modulate the hair growth cycle (anagen, catagen, telogen phases). By suppressing gonadal steroid output, GnRH antagonism could theoretically alter follicular behaviour. However, a critical biological distinction undermines this reasoning: **hypertrichosis** is defined as excessive hair growth that occurs independent of androgen stimulation, in any distribution. It differs fundamentally from **hirsutism**, which is androgen-driven male-pattern hair growth. Hypertrichosis most commonly arises from congenital gene mutations, inherited syndromes, or non-hormonal drug induction — none of which lie on the HPG (hypothalamic-pituitary-gonadal) axis that Degarelix targets.

This mechanistic mismatch suggests the high TxGNN score reflects indirect graph-neighbourhood proximity within the knowledge graph rather than a genuine pharmacological relationship. The mechanistic relevance is assessed as **very low**, and this prediction is unlikely to translate into clinical benefit without first establishing a credible biological rationale through preclinical work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> Note: 20 PubMed records were retrieved for the rank-4 indication "malformation syndrome with odontal/periodontal component," but all articles are general periodontics references (EFP clinical guidelines, periodontal-diabetes associations, microbiome studies) with no connection to Degarelix. They are **not counted** as supporting evidence for drug repurposing.

---

## Canada Market Information

Degarelix is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are on record in the regulatory database. The drug holds regulatory approvals in other jurisdictions (U.S. FDA, EMA) for advanced prostate cancer under the brand name Firmagon®, but these approvals do not extend to the Canadian market at the time of this report (data cutoff: 2026-04-04).

---

## Cytotoxicity

Degarelix is an antineoplastic agent (hormonal therapy class) used in oncology. It is **not** a conventional cytotoxic drug and does not carry the same myelosuppressive risk profile as chemotherapy agents.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal / Targeted therapy — GnRH receptor antagonist (not conventional cytotoxic) |
| Myelosuppression Risk | Low — myelosuppression is not a primary concern; major adverse effects are injection-site reactions and testosterone-suppression sequelae |
| Emetogenicity Classification | Low |
| Monitoring Items | Serum testosterone and PSA (for efficacy), liver function tests (ALT/AST), QTc interval (ECG), bone density (long-term androgen deprivation) |
| Handling Protection | Standard precautions for injectable oncology drugs; dedicated cytotoxic handling protocols are not typically required for hormonal agents, but local SOPs should be consulted |

---

## Safety Considerations

Please refer to the package insert (product monograph) for full safety information. Regulatory warning and contraindication data are not available in the current evidence package (Data Gap: DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN top-ranked predictions for Degarelix are rated L5 (model prediction only, no supporting evidence), and the leading prediction — hypertrichosis — has a mechanistic profile that is fundamentally incompatible with GnRH antagonism, as hypertrichosis is a non-hormonal condition. Proceeding toward clinical exploration without a credible biological mechanism and at least preclinical data would not be scientifically justified.

**To proceed, the following is needed:**
- Retrieve full product monograph / Health Canada regulatory data to complete safety profiling (warnings, contraindications, drug interactions)
- Obtain complete MOA data from DrugBank API (DG002) to enable rigorous mechanistic analysis
- Conduct a targeted literature review specifically on sex steroid involvement in any hypertrichosis subtype to evaluate whether any hormonal subphenotype exists that could theoretically respond to HPG-axis suppression
- Assess whether TxGNN knowledge graph embeddings are producing spurious associations for GnRH antagonists by benchmarking against known approved indications (e.g., prostate cancer, central precocious puberty — ranks 8–9 in this pack — which are mechanistically aligned and warrant separate evidence review)
- If any preclinical signal emerges, a Phase 0/translational study design should be considered before any clinical commitment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

