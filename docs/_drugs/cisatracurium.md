---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium: From Neuromuscular Blockade (Anesthesia) to Cauda Equina Syndrome

---

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocking agent (NMBA), widely used as an adjunct to general anesthesia and ICU mechanical ventilation facilitation via its peripheral neuromuscular junction (NMJ) blockade.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction is assessed as a knowledge graph artifact rather than a genuine therapeutic signal, and all 10 predicted indications in this pack carry the same L5 / Hold verdict.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade — adjunct to general anesthesia and ICU mechanical ventilation |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack. Based on established pharmacology, Cisatracurium is a benzylisoquinolinium NMBA that competitively antagonises nicotinic acetylcholine receptors (nAChR) at the skeletal muscle NMJ, producing dose-dependent, reversible paralysis. Its key clinical advantage is Hofmann elimination — spontaneous, organ-independent degradation at physiological pH and temperature — making it the agent of choice in hepatic or renal failure patients. It does not cross the blood-brain barrier and has no appreciable central nervous system activity at therapeutic doses.

Cauda equina syndrome (CES) is caused by mechanical compression of the lumbosacral nerve roots within the spinal canal, typically from a large disc herniation or tumour, and requires urgent surgical decompression. The pathophysiology is entirely mechanical and ischaemic at the nerve root level — a domain in which NMJ blockade plays no role. Cisatracurium has no spinal neuroprotective, anti-inflammatory, vasodilatory, or decompressive mechanism that could influence CES outcomes.

The TxGNN model's near-perfect score (99.99%) for this pairing almost certainly reflects a **knowledge graph co-occurrence artefact**: cisatracurium is routinely used intraoperatively for spinal surgery, so anesthesia/NMBA nodes and spinal disease nodes are topologically proximate in the biomedical knowledge graph. This is a well-recognised limitation of graph neural network repurposing models — shared surgical context creates spurious high-confidence predictions that do not represent true therapeutic repurposing. The same pattern is observed across all 10 indications in this pack (preeclampsia, migraine, IBS, thrombotic disease, etc.), further supporting a systemic artefact rather than genuine pharmacological signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cisatracurium in Cauda Equina Syndrome.

> **Note on other indications:** Two clinical trials were retrieved for the preeclampsia pairing (NCT04645719, NCT04003688) and one for the thrombotic disease pairing (NCT03902470); however, all three studied **Magnesium Sulfate** or general anesthesia technique, not Cisatracurium as a treatment — these are data contamination artefacts and are excluded from this report.

---

## Literature Evidence

Currently no related literature available for Cisatracurium in Cauda Equina Syndrome.

> **Note on other indications:** One case series (PMID [12565113](https://pubmed.ncbi.nlm.nih.gov/12565113/)) was retrieved for the thrombotic disease pairing; it is a paediatric liver transplant anesthesia report in which Cisatracurium was used as an intraoperative muscle relaxant, not as a treatment for thrombosis. Excluded as irrelevant.

---

## Canada Market Information

Cisatracurium is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are registered, and no approved product monograph is available through Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information. Full warning, contraindication, and drug interaction data were not retrieved in this evidence pack.

> **Known clinical context (from general pharmacology):** Cisatracurium causes complete respiratory muscle paralysis and requires mechanical ventilatory support for the duration of its effect. Co-administration with Magnesium Sulfate (used in preeclampsia management) potentiates and prolongs neuromuscular blockade; dose reduction is required. Reversal with sugammadex or neostigmine/glycopyrrolate is standard practice.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this evidence pack are scored L5 (model prediction only) with zero supporting clinical trials or literature, and the mechanistic analysis confirms that Cisatracurium's exclusive peripheral NMJ mechanism of action is incompatible with the central, autonomic, vascular, or compressive pathophysiology of every predicted disease. The high TxGNN scores are best explained by systematic co-occurrence of NMBA use within surgical/procedural contexts in the knowledge graph, rather than any genuine repurposing signal.

**To proceed, the following is needed:**

- **Artefact investigation:** Audit the TxGNN knowledge graph to determine whether surgical co-occurrence nodes are driving false positives across all NMBA-class drugs; if confirmed, flag Cisatracurium as a low-priority repurposing candidate system-wide.
- **Safety data retrieval:** Obtain the full cisatracurium package insert (Health Canada / FDA label) to complete S1 safety screening.
- **MOA data retrieval:** Query DrugBank API for complete mechanism, targets, and enzyme interactions to enable rigorous mechanistic scoring.
- **Alternative framing:** If a repurposing rationale is sought, a more biologically plausible hypothesis would explore whether Hofmann elimination kinetics confer any advantage in specific ICU disease states (e.g., multi-organ failure, ARDS) — a question distinct from any of the 10 predicted indications listed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

