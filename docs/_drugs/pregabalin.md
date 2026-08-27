---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the report as directly specified by your detailed prompt template (this is a content-generation task with a fully-specified format, not a coding/pipeline task, so no additional skill invocation is needed). Note upfront: this Evidence Pack is unusually data-poor — `original_moa`, `original_indications`, and all safety fields are flagged as gaps in `meta.data_gaps` (one of them **Blocking**), and Canada licensing data is empty. I've followed the prohibition against fabricating or printing literal "[Data Gap]" text, and omitted sections/rows with no underlying data.

---

# Pregabalin: From Original Indication Not Documented to Tendinitis

## One-Sentence Summary

The original approved indication for pregabalin (DrugBank DB00230) is not documented in this evidence pack, and the drug currently has no marketing authorization on record in this jurisdiction. The TxGNN model predicts a possible signal for **Tendinitis**, but this is currently supported only by **0 clinical trials** and **6 publications** (mostly case reports and mechanistically indirect studies), making it the weakest of the five candidates surfaced in this pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license/label text available) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pregabalin is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic reasoning captured elsewhere in this pack's rationale fields, pregabalin acts through α2δ calcium-channel modulation, which underlies its known central analgesic and anticonvulsant effects.

Tendinitis, however, is primarily a peripheral soft-tissue inflammatory/degenerative condition rather than a neuropathic-pain process. Pregabalin's calcium-channel modulation can plausibly contribute central analgesic or opioid-sparing benefit as a *perioperative adjunct* (e.g., in patients undergoing arthroscopic rotator cuff repair), but this is a symptomatic pain-control effect, not a disease-modifying mechanism directed at the tendon inflammation itself. The mechanistic link between pregabalin and tendinitis as a *treatment target* is therefore weak and indirect — the model's high similarity score more likely reflects shared "pain/musculoskeletal" graph neighbors rather than a genuine disease-modifying pathway.

By contrast, this same evidence pack contains a considerably stronger secondary signal for **migraine disorder** (rank 5, L2 evidence, one Phase 3 RCT plus multiple completed pediatric/adult RCTs, and a coherent mechanistic story via α2δ-1 inhibition of cortical spreading depression). This is noted here because it materially changes how the overall repurposing opportunity for pregabalin should be prioritized (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(0 trials were returned for the tendinitis query; the RCTs identified for pregabalin in this pack relate to perioperative pain control after rotator cuff surgery, not to treatment of tendinitis itself — these are listed under Literature Evidence below rather than as disease-targeted trials.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT (retrospective cohort) | J Orthop Sci | Evaluated analgesic efficacy and opioid-sparing effect of pregabalin after arthroscopic rotator cuff repair; adjunct pain control, not tendinitis treatment |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin produced pain scores equivalent to interscalene brachial plexus block after arthroscopic rotator cuff repair |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Fluoroquinolone (ciprofloxacin)-associated tendinopathy/disability — describes tendon toxicity from a different drug class, not a pregabalin treatment study |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial commentary | Arthroscopy | Discusses piriformis syndrome and sciatic/piriformis tendon release; not directly related to pregabalin or tendinitis treatment |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Practice | Posterior femoral cutaneous nerve impingement from hamstring tendonitis in a marathon runner; does not evaluate pregabalin as treatment |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | Plant extract (Cissus quadrangularis), not pregabalin, attenuates vincristine-induced peripheral neuropathy in rats |

## Safety Considerations

Please refer to the package insert for safety information.

**Important caveat:** the absence of listed warnings, contraindications, and drug-interaction data here is itself a **Blocking data gap (DG001)** in this evidence pack — it is explicitly recorded as preventing entry into the S1 safety initial-evaluation stage. This is not equivalent to "no known safety concerns"; it means the safety review has not yet been performed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic link between pregabalin and tendinitis is weak and indirect — no clinical trials target tendinitis directly, and the only RCTs available concern perioperative analgesic adjunct use, not disease treatment.
- A Blocking-severity data gap (DG001: missing product-label warnings/contraindications) currently prevents this candidate from entering the S1 safety evaluation stage at all, regardless of efficacy evidence.

**To proceed, the following is needed:**
- Retrieve official label warnings and contraindications (per DG001 remediation: source from the regulatory agency's label PDF)
- Retrieve DrugBank mechanism-of-action data (per DG002 remediation: DrugBank API query)
- Confirm original approved indication(s) and marketing/licensing status, currently absent from this pack
- Consider redirecting repurposing evaluation effort toward **migraine disorder** (rank 5), which has substantially stronger supporting evidence (L2, one completed-intent Phase 3 RCT albeit withdrawn, several completed pediatric RCTs, and a coherent CSD-based mechanistic rationale) and may warrant its own dedicated evaluation report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

