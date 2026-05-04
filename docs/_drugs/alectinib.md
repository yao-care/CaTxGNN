---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Alectinib is a second-generation, highly selective ALK (Anaplastic Lymphoma Kinase) tyrosine kinase inhibitor, approved globally for the treatment of ALK-positive non-small cell lung cancer (NSCLC), though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis (Fibromatosis, Gingival)**,
with **no clinical trials** and **no published literature** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (based on globally recognized use; not marketed in Canada) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established global clinical evidence, alectinib is a highly selective, ATP-competitive inhibitor targeting the ALK tyrosine kinase — specifically the EML4-ALK fusion oncoprotein found in approximately 3–5% of NSCLC patients. By blocking this constitutively active kinase, alectinib disrupts downstream proliferative and survival signalling in tumour cells. It also inhibits RET kinase activity, which contributes to its broader oncological relevance.

Gingival fibromatosis, however, is a rare benign condition characterized by progressive fibrous overgrowth of gingival tissue. Its molecular basis is primarily linked to mutations in the **SOS1** or **PTCH2** genes, which regulate developmental signalling pathways unrelated to ALK or RET. There is no published evidence — experimental, translational, or clinical — that ALK overexpression or rearrangement plays any role in the pathogenesis of this condition.

The very high TxGNN prediction score (99.97%) most likely reflects semantic clustering within the knowledge graph, where both "tumour/proliferative" concepts are co-localized, rather than a genuine mechanistic connection. Without any preclinical rationale or biological plausibility, this prediction should be treated as a knowledge-graph artefact at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Alectinib is not currently marketed in Canada. No Drug Identification Numbers (DINs) have been issued by Health Canada.

---

## Cytotoxicity

Alectinib is an antineoplastic agent (targeted kinase inhibitor) used in cancer treatment. The following applies based on its drug class characteristics:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK/RET tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low (anaemia has been reported; severe haematological toxicity is uncommon compared to cytotoxic chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (AST/ALT/bilirubin), renal function, creatine phosphokinase (CPK), blood glucose |
| Handling Protection | Follow institutional cytotoxic drug handling guidelines; oral capsule formulation reduces direct exposure risk |

> Please refer to the package insert warnings and precautions for complete toxicity data, as drug-specific cytotoxicity records were not available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, translational, or preclinical evidence connecting alectinib to gingival fibromatosis, and no plausible mechanistic pathway linking ALK/RET inhibition to the SOS1/PTCH2-driven fibroblast overgrowth that characterises this condition. The high TxGNN score reflects knowledge-graph ontological similarity rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- Molecular profiling of gingival fibromatosis biopsy tissue to determine whether ALK expression or rearrangement is detectable in any subset of patients
- Preclinical in vitro studies assessing whether ALK inhibition has any effect on gingival fibroblast proliferation or extracellular matrix production
- Complete drug mechanism of action (MOA) and safety profile from DrugBank API query (DG002 remediation)
- Full Canadian product monograph and TFDA-equivalent label warnings when available (DG001 remediation)
- Re-evaluation of higher-ranked predictions with stronger mechanistic support (e.g., Rank 5: ALK-positive NSCLC / lung benign neoplasm — Evidence Level L1, "Proceed with Guardrails"; Rank 7: ALK-positive lung neuroendocrine tumour — Evidence Level L3, "Research Question") for prioritisation in parallel workstreams
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

