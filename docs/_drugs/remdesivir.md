---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 673
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

Using the evidence pack as given — the top-ranked prediction (rank 1, "multiple endocrine neoplasia") has zero supporting evidence and the rationale itself flags it as a likely false positive, so the report reflects that honestly rather than dressing it up.

# Remdesivir: From Antiviral Therapy (COVID-19/Ebola) to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Remdesivir is a nucleotide-analog RNA-dependent RNA polymerase (RdRp) inhibitor originally developed for Ebola virus disease and later authorized internationally for COVID-19 treatment.
> The TxGNN model assigns a high score (**99.50%**) to **Multiple Endocrine Neoplasia (MEN)** as a candidate new indication,
> but this is **not supported by any clinical trials or literature** — the model's own rationale flags it as a probable false positive arising from knowledge-graph embedding similarity rather than biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in Canadian licensing data (drug not marketed in Canada); internationally known as an antiviral for Ebola virus disease and COVID-19 (SARS-CoV-2) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% (rank 9240) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not retrievable for this evaluation. Based on publicly established pharmacology, remdesivir is a nucleotide analog prodrug that inhibits the RNA-dependent RNA polymerase (RdRp) of RNA viruses (e.g., Filoviridae, Coronaviridae), blocking viral genome replication. Its proven efficacy is in acute viral infections such as COVID-19.

Multiple endocrine neoplasia (MEN) is a hereditary endocrine tumor syndrome driven by germline mutations in genes such as *RET* (MEN2) or *MEN1*, with a pathophysiology centered on tumor suppressor/oncogene signaling in endocrine tissue — entirely unrelated to viral RNA replication. There is no known or plausible mechanistic pathway connecting RdRp inhibition to MEN prevention or treatment.

The evidence pack's own rationale for this candidate states this directly: the high TxGNN score most likely reflects a knowledge-graph embedding artifact rather than a genuine biological signal, and no clinical trials, literature, or mechanistic studies exist to support it. This prediction should be treated as a **low-confidence, unvalidated model output**, not a credible repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Remdesivir currently has no Canadian licenses on record (0 DINs, market status: Not Marketed). No product/dosage-form/indication data is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Multiple Endocrine Neoplasia) has no clinical, literature, or mechanistic support, and the model's own reasoning identifies it as a likely false positive from graph-embedding similarity rather than a real pharmacological signal. No further action is warranted on this candidate at this time.

**To proceed, the following is needed:**
- Confirmed DrugBank mechanism-of-action data for remdesivir (currently a data gap)
- Any preclinical or mechanistic rationale specifically linking RdRp inhibition to MEN-associated tumor pathways, if one is ever proposed
- TFDA/Health Canada labeling data (warnings, contraindications, DDI) before any safety-stage review can begin
- Note: other candidates in this same batch (e.g., ranked #2 HIV, #8 leprosy, #10 CMV) returned clinical trial/literature hits, but on inspection nearly all of that retrieved evidence is actually about remdesivir's already-known COVID-19 use (or, in the leprosy case, about an unrelated anti-leprosy drug repurposed *for* COVID-19) rather than genuine evidence for the disease label assigned — worth flagging as a possible disease-mapping/retrieval issue in the pipeline before trusting evidence counts at face value for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

