---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 5
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic widely used to treat bacterial infections, including respiratory tract infections and *Mycobacterium* species such as *M. abscessus* and *M. avium* complex (MAC).
The TxGNN model predicts it may be effective for **Hyperamylasemia**, with **0 clinical trials** and **1 publication** (a single 2004 case report) currently available to support this direction.
The mechanistic connection between clarithromycin and elevated serum amylase is indirect and does not reflect a genuine therapeutic target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (per current dataset) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this Evidence Pack. Based on established pharmacological knowledge, clarithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, blocking peptide chain elongation. It is a first-line agent for *Mycobacterium abscessus* and MAC lung infections, community-acquired pneumonia, and *Helicobacter pylori* eradication regimens. It also carries documented immunomodulatory properties — notably suppression of IL-1β, IL-6, IL-8, and NF-κB — which have been explored in chronic airway inflammatory conditions.

Hyperamylasemia (persistently elevated serum amylase) is a laboratory finding rather than a disease in its own right. It can arise from acute pancreatitis, salivary gland disorders, renal insufficiency, or macroamylasemia — a benign condition in which amylase binds to immunoglobulins forming large complexes that cannot be cleared renally. The sole supporting publication (PMID 15228140) describes a 76-year-old man with *M. abscessus* lung infection who was incidentally found to have primary macroamylasemia. Clarithromycin was prescribed to treat the mycobacterial infection; the elevated amylase was a coincidental co-existing condition, not the therapeutic target.

There is therefore no direct mechanistic rationale for clarithromycin to treat hyperamylasemia. The TxGNN model's high prediction score most likely reflects non-specific proximity in the knowledge graph — clarithromycin sits close to *M. abscessus* nodes, which in turn connect to the macroamylasemia case — rather than any genuine pharmacological opportunity. This prediction should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case Report | Nihon Kokyuki Gakkai Zasshi (Japanese Respiratory Society) | A 76-year-old man with *M. abscessus* lung infection was found to have co-existing primary macroamylasemia. Clarithromycin was used to treat the mycobacterial infection. The elevated serum amylase was an incidental finding, not the treatment target. No conclusion about clarithromycin's effect on amylase levels can be drawn from this case. |

---

## Canada Market Information

According to the current dataset, clarithromycin has no active Drug Identification Numbers (DINs) recorded in Canada and is listed as not marketed. This finding is inconsistent with clarithromycin's well-established global availability (e.g., Biaxin® in North America) and likely reflects a gap in the data pipeline rather than the true regulatory status. Verification via the Health Canada Drug Product Database is strongly recommended before drawing any conclusions about market access.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available evidence is a 2004 case report in which hyperamylasemia was a coincidental finding in a patient being treated for *M. abscessus* infection — it provides no clinical support for clarithromycin as a treatment for elevated amylase, and no clinical trials or mechanistic studies exist to justify further development in this indication.

**To proceed, the following is needed:**
- **MOA data**: Retrieve detailed mechanism of action from DrugBank (DB01211) to determine whether any plausible direct effect on pancreatic or salivary amylase secretion exists
- **Regulatory verification**: Confirm Canadian DIN status via the Health Canada Drug Product Database to obtain approved indications, labeling, and safety warnings
- **Package insert review**: Retrieve TFDA or Health Canada monograph to identify contraindications and key drug interactions (currently blocking for safety assessment)
- **Signal validation**: Investigate whether TxGNN's prediction reflects a biologically meaningful graph path or a topology artifact; if a hypothesis emerges, preclinical data (enzyme regulation models) would be the minimum threshold before any clinical consideration
- **Broader indication scan**: Note that clarithromycin's rank-4 predicted indication — **punctate epithelial keratoconjunctivitis** (L4, Research Question) — has a stronger mechanistic rationale via its anti-*Staphylococcal* and anti-inflammatory properties in meibomitis-related keratoconjunctivitis, and may warrant a separate focused evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

