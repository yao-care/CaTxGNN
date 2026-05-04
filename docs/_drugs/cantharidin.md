---
layout: default
title: Cantharidin
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 1
---

# Cantharidin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Cantharidin: From Wart Treatment to Amenorrhea

## One-Sentence Summary

Cantharidin is a natural vesicant toxin derived from blister beetles, used topically in dermatology for conditions such as molluscum contagiosum and warts; it carries no approved indications on record in Taiwan. The TxGNN model predicts it may have relevance in **Amenorrhea**, likely drawing on historical traditional Chinese medicine records of 斑蝥 (blister beetle) as an emmenagogue, yet this prediction is supported by **no clinical trials** and **no published literature** — making it a model-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in Taiwan |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cantharidin is a naturally occurring terpenoid toxin secreted by blister beetles (e.g., *Lytta vesicatoria*, "Spanish fly"). Its primary known pharmacological mechanism is inhibition of serine/threonine protein phosphatases PP2A and PP1, which disrupts actin polymerisation and leads to cellular blistering. In modern dermatology it is applied topically as a keratolytic and vesicant for the removal of warts and molluscum contagiosum lesions. Detailed MOA data from DrugBank is not available in the current evidence pack.

The predicted connection to amenorrhea appears to originate from traditional Chinese medicine (TCM), where 斑蝥 — the dried beetle from which cantharidin is extracted — was historically classified as an *emmenagogue* (通經劑), meaning a substance used to stimulate or regulate menstrual flow. This historical usage is likely captured as an edge in the TxGNN knowledge graph, which would explain the very high model score (99.42%). However, the biological pathway from PP2A/PP1 inhibition to regulation of the hypothalamic–pituitary–ovarian (HPO) axis — the primary driver of most amenorrhea aetiologies — is not established by modern pharmacological evidence.

In summary, while the historical TCM record provides a superficially plausible narrative, the mechanistic link between cantharidin and amenorrhea is extremely weak by contemporary standards. The multiple root causes of amenorrhea (HPO axis dysregulation, structural/anatomical factors, nutritional deficiency, thyroid dysfunction) do not correspond to any known pharmacodynamic target of cantharidin. The high TxGNN score reflects pattern-based graph inference rather than validated pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada / Taiwan Market Information

Cantharidin (DrugBank ID: DB12328) carries no approved product licences in Taiwan. No DIN or product-level regulatory data is available to display.

---

## Cytotoxicity

Cantharidin and its semi-synthetic derivative norcantharidin are recognised cytotoxic agents with documented antineoplastic activity through PP2A/PP1 inhibition, a pathway relevant to cancer cell proliferation and apoptosis. The following cytotoxicity profile is derived from established pharmacological literature in the absence of DrugBank-sourced toxicity records.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic / natural product (terpenoid vesicant) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Insufficient data — systemic exposure risk depends heavily on route and dose |
| Monitoring Items | Renal function (cantharidin is renally excreted and nephrotoxic), hepatic function, urinalysis, signs of mucosal irritation |
| Handling Protection | Must be handled with cytotoxic drug precautions; direct skin and mucosal contact is hazardous due to severe vesicant activity |

---

## Safety Considerations

Please refer to the package insert for safety information. Note that cantharidin is a potent vesicant and systemic toxin — accidental mucosal exposure, ingestion, or skin contact carries serious risk of blistering, haemorrhagic cystitis, and multi-organ injury. No formal DDI data, key warnings, or contraindications were retrievable from the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is driven almost entirely by historical TCM records of blister-beetle-derived emmenagogue use, with no modern pharmacological mechanism linking cantharidin to amenorrhea pathophysiology, and zero clinical trials or peer-reviewed publications supporting this indication. L5 evidence does not meet the threshold required to proceed.

**To proceed, the following is needed:**

- **Mechanistic evidence**: Peer-reviewed studies demonstrating a plausible link between PP2A/PP1 inhibition (or another cantharidin target) and the HPO axis or endometrial function
- **Preclinical data**: In vitro or animal model data showing any effect on menstrual cycle regulation, uterine contractility, or gonadotropin signalling
- **Safety characterisation**: Full toxicological profile including systemic exposure at doses relevant to a gynaecological indication, given cantharidin's known nephrotoxicity and vesicant properties
- **Regulatory baseline**: Clarification of cantharidin's current regulatory status — it is not marketed in Taiwan and is a controlled/restricted substance in many jurisdictions; any clinical development pathway would require early engagement with regulatory authorities
- **Alternative hypothesis review**: Evaluate whether the TxGNN signal might instead reflect norcantharidin (a safer synthetic analogue) data that was merged into the cantharidin node within the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

