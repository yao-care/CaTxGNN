---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Hypertriglyceridemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a fibrate-class lipid-lowering drug (PPAR-α agonist) with well-established use in treating hypertriglyceridemia and dyslipidemia.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
with **0 clinical trials** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertriglyceridemia / Dyslipidemia |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data on file. Based on published pharmacology, gemfibrozil is a fibrate-class drug that activates PPAR-α (peroxisome proliferator-activated receptor alpha), primarily lowering triglycerides and raising HDL cholesterol through hepatic lipid metabolism pathways. What is less widely recognized is that PPAR-α activation also carries significant anti-inflammatory downstream effects.

By activating PPAR-α, gemfibrozil can suppress the NF-κB signaling pathway, reducing transcription of pro-inflammatory cytokines including TNF-α, IL-6, and IL-1β. These are precisely the cytokines that drive synovial inflammation and joint destruction in rheumatoid arthritis, providing a mechanistically plausible bridge between gemfibrozil's known pharmacology and a potential RA application.

Direct experimental support comes from a rat adjuvant-induced arthritis (AIA) model (PMID 30074417), where gemfibrozil combined with reduced-dose prednisolone achieved anti-arthritic outcomes comparable to full-dose steroid therapy — suggesting steroid-sparing potential. A related compound, bezafibrate (a pan-PPAR agonist), further demonstrated PPAR-γ-dependent attenuation of experimental RA in animals (PMID 41207105), providing class-effect biological plausibility across the fibrate family. Overall, evidence remains at an early preclinical stage with no formal human trials in RA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal Study (PPAR-α agonist + steroid taper) | Modern Rheumatology | Gemfibrozil (30 mg/kg) combined with reduced-dose prednisolone achieved similar anti-arthritic outcomes as full-dose steroid in rat AIA model; suggests steroid-sparing potential via PPAR-α activation |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical Animal Study | International Immunopharmacology | Bezafibrate (pan-PPAR agonist) attenuated experimental RA via PPAR-γ-dependent anti-inflammatory modulation; supports fibrate class-effect biological plausibility for RA |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Basic Research | Journal of Immunology | Nitric oxide-mediated reduction of Foxp3 expression in regulatory T cells following MBP priming; provides mechanistic context for fibrate-immune modulation pathways relevant to autoimmunity |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review | American Journal of Clinical Dermatology | Palmar erythema review covering systemic pathology associations; indirect contextual reference only, limited direct relevance to RA repurposing |

---

## Canada Market Information

Gemfibrozil is currently not marketed in Canada. No Drug Identification Numbers (DINs) are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN prediction score is high (99.90%), and a mechanistically plausible PPAR-α / NF-κB anti-inflammatory pathway connects gemfibrozil to rheumatoid arthritis. However, all available evidence is preclinical (animal models and basic research only), with no registered clinical trials and no human data specific to RA — placing this squarely at Evidence Level L4. The complete absence of Canada regulatory history adds an additional translational hurdle.

**To proceed, the following is needed:**
- Full mechanism of action documentation (DrugBank API query or published pharmacology review)
- Safety data retrieval: package insert warnings, contraindications, and DDI profile (particularly CYP2C8 inhibition risk and interaction with statins/immunosuppressants relevant to RA treatment)
- Systematic review of fibrate class anti-inflammatory effects in autoimmune conditions
- Proof-of-concept clinical feasibility assessment — most actionable in RA patients with comorbid hypertriglyceridemia where gemfibrozil is already indicated
- Regulatory pathway mapping for Canada, where gemfibrozil has no existing market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

