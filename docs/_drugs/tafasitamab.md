---
layout: default
title: Tafasitamab
parent: 僅模型預測 (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
---

# Tafasitamab
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

Using no additional skill — this is a direct content-generation task with a fully specified template already provided; I'll follow it and the evidence data exactly, without guessing missing fields (original indication/MOA/licenses are explicitly absent in this pack).

---

# Tafasitamab: Original Indication Undocumented → Predicted Signal for Drug-Induced Osteoporosis

## One-Sentence Summary

> Tafasitamab (DB15044) is described in this evidence pack only as an anti-CD19 monoclonal antibody — no original approved indication or mechanism-of-action data is available in this dataset (flagged as data gaps DG001/DG002).
> The TxGNN model's top-ranked new-indication signal is **Drug-Induced Osteoporosis**,
> but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as likely knowledge-graph topology noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — `original_indications` empty) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

### Other TxGNN-Predicted Candidates Screened (Ranks 2–10)

For context, this pack evaluated 10 candidates for Tafasitamab. None reached a "Go" or "Proceed" recommendation:

| Rank | Disease | Score | Evidence Level | Recommendation |
|------|---------|-------|-----------------|-----------------|
| 2 | Severe nonproliferative diabetic retinopathy | 97.34% | L5 | Hold |
| 3 | Diabetic retinopathy | 95.40% | L5 | Hold |
| 4 | HER2 positive breast carcinoma | 94.51% | L5 | Hold |
| 5 | Psoriasis | 94.03% | L5 | **Research Question** |
| 6 | Progesterone-receptor positive breast cancer | 93.00% | L5 | Hold |
| 7 | Normal breast-like subtype of breast carcinoma | 93.00% | L5 | Hold |
| 8 | Breast tumor luminal A or B | 92.91% | L5 | Hold |
| 9 | Progesterone-receptor negative breast cancer | 92.67% | L5 | Hold |
| 10 | Pityriasis lichenoides | 92.29% | L4 | Hold (adverse-effect signal, not efficacy) |

Notably, rank 8's 19 retrieved "literature hits" were reviewed and found to be false positives from a letter-B keyword mismatch (B-cell biology, hepatitis **B** vaccines, HLA-**B** typing), not genuine evidence. Psoriasis (rank 5) is flagged as the only candidate with partial mechanistic plausibility (B-cell depletion has precedent in other autoimmune disease treatment) but has no disease-specific trial or literature support yet.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002). Based on information embedded in the model's own rationale notes, Tafasitamab is described as an anti-CD19 monoclonal antibody that acts via B-cell depletion.

For the top-ranked candidate, **drug-induced osteoporosis**, the evidence pack's own mechanistic review finds **no known biological link** between CD19-mediated B-cell depletion and the bone-remodeling pathways implicated in drug-induced osteoporosis (e.g., osteoclast activation, glucocorticoid signaling). The reviewers explicitly suspect this score reflects knowledge-graph topological similarity rather than a real pharmacological relationship, an interpretation made harder to rule out given the missing original-indication data.

Across the full candidate list, the only prediction judged to have partial mechanistic grounding is psoriasis — B-cell-depleting antibodies have some theoretical basis in autoimmune disease (per precedent in SLE/RA), though no psoriasis-specific trial or publication currently exists to support it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Tafasitamab is currently **not marketed** in Canada — the evidence pack lists 0 DINs and no product authorizations to summarize.

---

## Safety Considerations

- **Reported Adverse Reaction Signal (from literature review)**: A case report ([PMID 37701883](https://pubmed.ncbi.nlm.nih.gov/37701883/), *JAAD Case Reports*, 2023) describes a patient developing pityriasis lichenoides chronica while on tafasitamab + lenalidomide therapy for diffuse large B-cell lymphoma. This is a reported **adverse effect**, not a treatment-efficacy finding, and should be tracked as a dermatologic safety signal rather than a repurposing candidate.

Beyond this, please refer to the package insert / product monograph for safety information — core warnings, contraindications, and drug-interaction data are marked as data gaps in this evidence pack (DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (drug-induced osteoporosis) has no clinical trial or literature support and is assessed by the evidence pack itself as likely a false-positive knowledge-graph signal, with no plausible mechanistic link to the drug's known B-cell-depleting activity. No candidate in this set reached Go-level evidence, and core safety data (warnings, contraindications) is entirely missing (DG001, Blocking).

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph — warnings, contraindications, DDI data (resolves DG001, currently blocking)
- Confirmed original indication and mechanism of action via DrugBank API (resolves DG002)
- If pursuing psoriasis as a research hypothesis: preclinical or case-level evidence specific to that indication before any trial-design work
- Ongoing pharmacovigilance tracking of the pityriasis lichenoides signal as a known adverse effect, independent of the repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

