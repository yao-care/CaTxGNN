---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a synthetic progestin used as a long-acting contraceptive implant (Implanon/Nexplanon), not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Amenorrhea** with a score of 99.84%, but **this prediction carries a critical directional warning**: etonogestrel is known to **cause** amenorrhea in 20–30% of users as a side effect, not to treat it.
Evidence supporting this repurposing direction is rated **L4** (preclinical/mechanistic only), and the clinical trial and literature identified are tangential to the proposed indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (drug not marketed in Taiwan; known clinically as a contraceptive implant) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, etonogestrel is a third-generation synthetic progestin — the biologically active metabolite of desogestrel — that suppresses the hypothalamic-pituitary-gonadal (HPG) axis by reducing GnRH pulse frequency, blunting LH and FSH secretion, and inhibiting ovulation. Secondary actions include endometrial atrophy and cervical mucus thickening. These mechanisms are the basis of its contraceptive efficacy.

**⚠️ Critical Directional Warning — Prediction likely a false positive:** The TxGNN model's high score for amenorrhea almost certainly reflects a knowledge graph edge misclassification. The relationship encoded in the graph is `etonogestrel → causes → amenorrhea`, not `etonogestrel → treats → amenorrhea`. Amenorrhea is a well-documented side effect occurring in approximately 20–30% of Implanon/Nexplanon users within the first year of use, and this is consistently reported as an adverse outcome in clinical documentation — not a therapeutic benefit sought.

Administering etonogestrel to a patient **already experiencing amenorrhea** would further suppress the HPG axis and likely worsen the condition, particularly in cases of hypogonadotropic amenorrhea where the clinical goal is to restore — not deepen — hormonal suppression. No mechanistic pathway has been identified by which exogenous progestin would resolve amenorrhea arising from any of its common etiologies (hypothalamic dysfunction, pituitary tumors, thyroid disorders, PCOS, or outflow tract obstruction).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|-----------|------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Extended-use study assessing contraceptive efficacy and safety of the etonogestrel implant during years 4–5 of use. Amenorrhea was monitored as a bleeding-pattern endpoint (side effect), not a treatment target. **Relevance to treating amenorrhea: None (Grade C).** |

> ⚠️ The sole identified trial is a contraceptive efficacy study. Amenorrhea in this context is an adverse/secondary outcome, not a therapeutic goal. This trial does not constitute evidence supporting etonogestrel as a treatment for amenorrhea.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Compared single-rod Implanon (etonogestrel) vs six-capsule Norplant (levonorgestrel) in 200 women over 2–4 years in a multicenter Chinese study. No pregnancies in either arm. Documents bleeding pattern differences including amenorrhea as a known side effect of etonogestrel. Not a treatment study for amenorrhea. |

> ⚠️ A second retrieved citation (PMID [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/), 2021) concerns BIO101 for COVID-19 pneumonia and has no connection to etonogestrel or amenorrhea — excluded from evidence table.

---

## Taiwan Market Information

Etonogestrel (DrugBank ID: DB00294) is currently **not marketed in Taiwan**. There are no active drug licenses or approved indications registered with the Taiwan regulatory authority. No license table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields — key warnings, contraindications, and drug-drug interactions — are flagged as data gaps in the current Evidence Pack. Safety data must be retrieved from the official package insert before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.84% for amenorrhea is a likely artifact of a knowledge graph edge misclassification (causes vs. treats), and applying etonogestrel to patients with amenorrhea would be pharmacologically counterproductive. No clinical trial or literature evidence supports this repurposing direction. All other predicted indications (breast fibrocystic disease, blunt duct adenosis, apocrine adenosis, benign mammary dysplasia) are rated L5 with zero supporting evidence.

**To proceed, the following is needed:**

- **Knowledge graph audit**: Verify whether the TxGNN graph encodes `etonogestrel → causes → amenorrhea` vs. `treats → amenorrhea` and correct the edge type if mislabeled
- **MOA documentation**: Retrieve full mechanism of action from DrugBank API to formalize the pharmacological rationale for any future repurposing assessment
- **Package insert safety data**: Download and parse the official package insert (Implanon/Nexplanon) from TFDA or Health Canada for key warnings and contraindications
- **Alternative indication scoping**: If repurposing exploration is desired, consider indications where progestin suppression of the HPG axis is therapeutically beneficial (e.g., endometriosis pain, dysmenorrhea, heavy menstrual bleeding) — these are not currently in the TxGNN top-5 list but would be mechanistically coherent candidates
- **Preclinical evidence requirement**: Any breast-related indication (ranks 2–5) requires dedicated in vitro/in vivo evidence before clinical consideration, given the unresolved and potentially bidirectional role of progestins in benign breast disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

