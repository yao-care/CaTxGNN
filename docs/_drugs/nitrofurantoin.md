---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran-class antibacterial originally used to treat urinary tract infection (UTI). The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but the **0 clinical trials** and **12 publications** currently available all describe nitrofurantoin-associated *adverse* effects (pulmonary fibrosis, drug-induced liver injury) rather than any therapeutic benefit — this prediction should be treated as a likely false positive pending further review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (antibacterial; original_moa not available — see Data Gap) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the information in this evidence pack, nitrofurantoin is a nitrofuran antibacterial that is activated by bacterial nitroreductase and causes DNA damage in bacteria; it has no known anti-inflammatory or immunomodulatory mechanism, and no established pathway connecting it to the autoimmune/synovial-inflammation biology of rheumatoid arthritis (RA).

More importantly, the direction of the supporting literature runs *against* a repurposing hypothesis rather than for it. Several publications describe nitrofurantoin **inducing** pulmonary fibrosis — including one severe case of irreversible pulmonary fibrosis when combined with methotrexate in an RA patient — and a self-controlled case series found antibiotic exposure associated with RA **flares**, not remission. Taken together, the evidence suggests the TxGNN model's high score most likely reflects a graph artifact: nitrofurantoin and RA co-occur frequently in the literature because nitrofurantoin causes adverse events (pulmonary fibrosis, autoimmune hepatitis) that are differential diagnoses or complications relevant to RA patients — not because nitrofurantoin treats RA.

Given this, the prediction should not be advanced on mechanistic grounds. A genuine assessment would require actual pharmacological or immunological rationale linking nitrofurantoin to RA pathophysiology, which is currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Antibiotic use was associated with RA **flares**, not improvement, in a UK CPRD cohort of 31,992 newly diagnosed RA patients |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Lists nitrofurantoin among drugs that **induce** pulmonary fibrosis; notes RA itself predisposes to pulmonary fibrosis |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | Nitrofurantoin + methotrexate combination caused irreversible pulmonary fibrosis in an RA patient treated for UTI |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Nitrofurantoin listed among antibiotics causing drug-induced interstitial lung disease |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | RA patients hospitalized for interstitial lung fibrosis had poor prognosis; no nitrofurantoin efficacy signal |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Nitrofurantoin listed among drugs that can induce sialadenitis; primary case was phenylbutazone-related |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | RCT (unrelated indication) | Acta Medica Scandinavica | Short-term nitrofurantoin therapy for bacteriuria; not related to RA |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis case where nitrofurantoin and RA-related autoimmune processes were considered in differential diagnosis |

---

## Canada Market Information

Nitrofurantoin is currently **not marketed** in Canada under this evidence pack — no Drug Identification Numbers (DINs) are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: although no structured warnings/contraindications/DDI data were available in this pack, the literature reviewed above documents known nitrofurantoin-associated risks including pulmonary fibrosis, methemoglobinemia, and hepatotoxicity — these should be factored into any future safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no clinical trials and no efficacy literature — every retrieved publication describes nitrofurantoin as a **cause** of adverse events (pulmonary fibrosis, hepatotoxicity, RA flares) rather than a treatment for RA. This pattern is consistent with a graph-based false positive rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for nitrofurantoin (currently a Data Gap)
- TFDA/Health Canada label warnings and contraindications (currently a Blocking Data Gap)
- A biologically plausible mechanistic hypothesis linking nitrofurantoin to RA pathophysiology before any further evaluation stage is considered
- Given the safety-signal-dominated evidence base, this candidate should likely be deprioritized rather than advanced
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

