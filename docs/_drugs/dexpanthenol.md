---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 7
---

# Dexpanthenol
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

# Dexpanthenol: From Skin Barrier Repair to Exanthem

## One-Sentence Summary

Dexpanthenol (provitamin B5) is a topical skin-conditioning agent widely used internationally for wound healing, skin barrier protection, and post-procedural skin recovery.
The TxGNN model predicts it may be effective for **Exanthem (acute skin rash)**, with **5 clinical trials** — including one completed Phase 3 RCT — currently supporting this direction.
Among the 7 TxGNN-predicted indications evaluated in this multi-indication pack, exanthem carries the strongest evidence base (L2) and is the only candidate recommended to proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Wound healing, skin barrier repair (topical; no Taiwan TFDA approval on record) |
| Predicted New Indication | Exanthem (Acute Skin Rash) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registered Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Dexpanthenol is the alcohol analogue of pantothenic acid (vitamin B5). Once absorbed through the skin, it is converted to pantothenic acid — an essential precursor to Coenzyme A (CoA). This metabolic role directly supports keratinocyte proliferation, accelerates skin barrier regeneration, and suppresses pro-inflammatory cytokines including IL-1β and TNF-α. Internationally, dexpanthenol is marketed as Bepanthen® (Europe), Bepantol® (Brazil), and Corneregel® (ophthalmic gel, EU) for applications ranging from nappy rash and minor wound care to dry eye and corneal repair.

The predicted indication, exanthem, describes acute widespread skin eruption. Its core pathology — epidermal barrier disruption and inflammatory cell infiltration — maps directly onto the mechanisms dexpanthenol is known to address. Chemotherapy-induced skin rash (a common and clinically meaningful form of exanthem) represents a particularly well-defined therapeutic niche where barrier-protective and anti-inflammatory agents have established roles.

The BeCet trial (NCT01136005), a completed Phase 3 RCT (n=160), directly evaluated Bepanthen® Cream against a comparator in preventing papulopustular eruption (skin rash) in patients receiving EGFR inhibitor therapy. This trial provides a strong clinical anchor. The high TxGNN score (99.60%) further reflects the topological proximity between dexpanthenol's established dermatological use nodes and exanthem within the drug-disease knowledge graph — a biologically coherent signal rather than a spurious one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Bepanthen® Cream (dexpanthenol) vs. Cetomacrogol Cream for **prevention of papulopustular skin eruption** in patients receiving EGFR inhibitor therapy; directly tests dexpanthenol in a clinically significant form of exanthem — the highest-quality trial in this pack |
| [NCT03852563](https://clinicaltrials.gov/study/NCT03852563) | N/A | Completed | 33 | Bepantol® Cream applied after ablative laser facial procedure; assesses skin redness, irritation, and recovery over 3 weeks — supports topical dexpanthenol for post-inflammatory skin repair |
| [NCT05699122](https://clinicaltrials.gov/study/NCT05699122) | N/A | Completed | 16 | Low-level laser therapy vs. standard barrier care (potentially including dexpanthenol) in incontinence-associated dermatitis; very small sample, indirect relevance |
| [NCT03866447](https://clinicaltrials.gov/study/NCT03866447) | Phase 4 | Unknown | 80 | Topical vitamin D analogues in acne vulgaris; dexpanthenol likely used as vehicle control — provides indirect tolerability data, but trial status is unverified |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Nanoencapsulated imiquimod in actinic cheilitis; dexpanthenol possibly used as comparator — trial was terminated, substantially limiting evidence value |

---

## Taiwan Market Information

Dexpanthenol is **not currently approved or marketed in Taiwan**. No licenses, product names, or approved indications are on record with the Taiwan TFDA.

Dexpanthenol is, however, approved and marketed in numerous international jurisdictions (EU, Brazil, USA as OTC ingredient) for topical wound healing and skin barrier applications. The absence of a Taiwan registration reflects a market access gap rather than a safety or efficacy concern.

---

## Safety Considerations

Detailed Taiwan TFDA package insert data (warnings, contraindications) were not available for this evaluation.

Based on international regulatory experience with topical dexpanthenol:
- **General tolerability**: Well tolerated topically; systemic absorption is minimal
- **Hypersensitivity**: Rare contact sensitization reactions have been reported; patch testing may be warranted in atopic individuals
- **Drug interactions**: No clinically significant interactions are expected for topical use

Please refer to the international product package insert (e.g., Bepanthen® SmPC) and the Taiwan TFDA database for full prescribing information before any clinical application.

---

## Other TxGNN Predictions (Summary)

This multi-indication pack evaluated 7 predictions. The remaining 6 are summarized below for completeness; all are rated **Hold** at this time.

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|-----------|-------------|----------------|----------------|-------|
| 1 | Anorectal stricture | 99.72% | L5 | Hold | Structural fibrosis — no pharmacological mechanism for reversal; high score likely reflects graph topology artefact |
| 2 | Imperforate anus | 99.71% | L5 | Hold | Congenital anatomical defect requiring surgery; drug repurposing framework does not apply |
| 3 | Anal polyp | 99.62% | L5 | Hold | Standard treatment is endoscopic excision; no mechanistic basis for dexpanthenol |
| 4 | Vulvar inverted follicular keratosis | 99.60% | L5 | Hold | Rare benign tumour; clonal proliferation not addressable by dexpanthenol; research priority very low |
| 5 | Proctitis | 99.60% | L5 | Research Question | Plausible mucosal repair mechanism (pantothenic acid → NF-κB suppression), but zero clinical evidence; proof-of-concept animal model study recommended first |
| 7 | Punctate epithelial keratoconjunctivitis | 99.34% | L5 | Research Question | Corneregel® (dexpanthenol 5% eye gel) is approved in EU for corneal repair; mechanistic extrapolation to this specific corneal epithelial condition is plausible but unvalidated |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The BeCet Phase 3 RCT (NCT01136005) provides direct, high-quality clinical evidence that Bepanthen® (dexpanthenol) prevents EGFR inhibitor-induced skin rash — a well-defined and clinically burdensome form of exanthem. The mechanism is coherent, the international safety profile is established, and the TxGNN score is high. The primary gaps are the absence of Taiwan market registration and the lack of Taiwan-specific safety documentation.

**To proceed, the following is needed:**

- **Safety documentation**: Download and parse the Taiwan TFDA package insert (or equivalent international SmPC) to complete formal warnings and contraindications review
- **Literature gap**: Conduct a targeted PubMed search for dexpanthenol + exanthem / skin rash / chemotherapy dermatitis to identify any supporting publications missed by this evidence pack (no literature was returned in the current query)
- **Evidence upgrade**: Obtain full BeCet trial results (NCT01136005) to confirm the primary endpoint; if efficacy is confirmed, evidence may upgrade to L1
- **Market access pathway**: Evaluate feasibility of Taiwan TFDA registration or import under the Special Access Programme for specific indications (e.g., EGFR inhibitor-associated skin rash in oncology)
- **Target population definition**: Narrow the clinical indication before proceeding — chemotherapy-induced exanthem is the most evidence-supported niche and has the clearest unmet need
- **MOA documentation**: Retrieve full DrugBank mechanism-of-action entry for dexpanthenol to strengthen the mechanistic rationale section in any subsequent submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

