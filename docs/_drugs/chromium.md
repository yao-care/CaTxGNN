---
layout: default
title: Chromium
parent: Model Prediction Only (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chromium: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available"
monitor_inn: "Chromium"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "gout", "pseudoachondroplasia", "hepatic porphyria", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Chromium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Chromium: From an Unspecified Original Indication to Osteoarthritis (Top Prediction), with Rheumatoid Arthritis as the Best-Supported Candidate

## One-Sentence Summary

Chromium is a trace mineral marketed in Canada in single-ingredient products. The data compiled for this report do not list an approved indication for it.
The TxGNN model ranks **osteoarthritis** as its top prediction, but the supporting trials and publications are almost entirely about cobalt-chromium orthopaedic implants, not chromium as a treatment.
The only prediction with real clinical support is **rheumatoid arthritis**, with **1 completed Phase 2/3 trial** and **1 randomized controlled trial publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the Canadian licence records) |
| Predicted New Indication | Osteoarthritis (top-ranked prediction) |
| TxGNN Prediction Score | 98.68% |
| Evidence Level | L5 (model prediction only; the trials and literature reflect implant materials, not therapy) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold (osteoarthritis); rheumatoid arthritis is a separate research question, see below |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for chromium, and no original indication is recorded in the Canadian licence data. The osteoarthritis prediction is therefore not backed by a documented mechanism.

**Osteoarthritis.** The "chromium" signal in the trials and publications comes from cobalt-chromium alloy hip and knee implants: metal ion release, metallosis, and resurfacing outcomes. Chromium appears as a potential source of harm from implant wear debris, not as a treatment. The high score most likely reflects a knowledge-graph link between chromium and joint disease through implant materials. A general nutrition and supplement review (PMID 10516985) is not chromium-specific evidence for osteoarthritis.

**Rheumatoid arthritis (score 98.54%).** This is the only prediction with a plausible therapeutic rationale. A rat study (PMID 35829940) reported that trivalent chromium eased adjuvant-induced arthritis, with proposed anti-inflammatory and immunomodulatory effects. A Phase 2/3 trial then compared trivalent chromium with baricitinib in RA patients. The evidence is still thin: a single small trial, limited follow-up, and no independent replication.

---

## Clinical Trial Evidence

**Osteoarthritis (top prediction)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00120952](https://clinicaltrials.gov/study/NCT00120952) | N/A | Withdrawn | 0 | Titanium vs cobalt-chromium femoral stem in cemented hip arthroplasty. An implant study, not a chromium drug trial |
| [NCT03681639](https://clinicaltrials.gov/study/NCT03681639) | N/A | Completed | 45 | Survival and outcomes of a hip resurfacing device. A device study, not a chromium therapy trial |

**Rheumatoid arthritis (best-supported prediction)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05545020](https://clinicaltrials.gov/study/NCT05545020) | Phase 2/3 | Completed | 60 | Trivalent chromium supplementation in RA patients, compared with baricitinib. Directly relevant, but small |
| [NCT03681639](https://clinicaltrials.gov/study/NCT03681639) | N/A | Completed | 45 | Hip resurfacing device study also listed under RA. Not relevant to chromium efficacy |

---

## Literature Evidence

**Rheumatoid arthritis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39030450](https://pubmed.ncbi.nlm.nih.gov/39030450/) | 2024 | RCT | Inflammopharmacology | First Phase 2/3 randomized trial of trivalent chromium vs baricitinib in RA, assessing efficacy and safety |
| [35829940](https://pubmed.ncbi.nlm.nih.gov/35829940/) | 2022 | Preclinical animal study | Inflammopharmacology | Trivalent chromium improved adjuvant-induced arthritis in rats, compared with prednisolone, via FOXP3 up-regulation and reduced synovial Cathepsin G |
| [29245125](https://pubmed.ncbi.nlm.nih.gov/29245125/) | 2018 | Cohort | Environmental Research | Review of delayed-type hypersensitivity to metals in connective tissue diseases, including RA |
| [1153978](https://pubmed.ncbi.nlm.nih.gov/1153978/) | 1975 | Observational | Scand J Rheumatol | Blood levels of several metals, including chromium, in RA patients vs controls |
| [3776595](https://pubmed.ncbi.nlm.nih.gov/3776595/) | 1986 | Observational | Acta Pharmacol Toxicol | Chromium, nickel and cadmium in biological fluids of RA patients vs healthy controls |

**Osteoarthritis (top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41231919](https://pubmed.ncbi.nlm.nih.gov/41231919/) | 2025 | RCT | J Bone Joint Surg Am | Serum metal levels after hip replacement with conventional vs modular dual-mobility bearings. Implant study, not chromium therapy |
| [41379985](https://pubmed.ncbi.nlm.nih.gov/41379985/) | 2025 | Systematic review / meta-analysis | JBJS Reviews | Hip resurfacing vs large-head metal-on-metal hip replacement: metal ion levels and revision risk |
| [39881936](https://pubmed.ncbi.nlm.nih.gov/39881936/) | 2024 | Review | Cureus | Mechanical and clinical aspects of metallosis after joint replacement |
| [38821495](https://pubmed.ncbi.nlm.nih.gov/38821495/) | 2024 | Cohort | Bone Joint J | 25-year results of the Birmingham Hip Resurfacing (metal-on-metal) |
| [10516985](https://pubmed.ncbi.nlm.nih.gov/10516985/) | 1999 | Review | Phys Med Rehabil Clin N Am | General review of nutrition and supplements; not specific to chromium in osteoarthritis |

The remaining osteoarthritis papers cover metal-on-metal hip and knee implant outcomes and metal ion levels. They are not evidence that chromium treats osteoarthritis.

**Other predictions.** Osteoarthritis susceptibility (rank 2) has only two papers on adverse metal reactions after hip arthroplasty. Gout and hepatic porphyria have only unrelated or very old reports. Pseudoachondroplasia, brachyolmia, colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia (Hunter-Thompson type) and brachyolmia-amelogenesis imperfecta syndrome have no trials or literature and rest on model prediction alone.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00786985 | MICRO CR | Not listed | Not listed |
| 02091135 | MICRO +4 REGULAR STRENGTH | Not listed | Not listed |
| 02552787 | MICRO+6 REGULAR | Not listed | Not listed |
| 02507587 | MICRO+6 CONCENTRATE | Not listed | Not listed |
| 02091100 | MICRO PLUS 6 (PEDIATRIC) | Not listed | Not listed |

A sixth licence (DIN 02497697, ADDNUTRIV) is also valid. All six are single-ingredient products, and none has been cancelled.

---

## Safety Considerations

Please refer to the package insert for safety information.

One safety-relevant point does come from the literature. Chromium released from cobalt-chromium implants is linked to metal hypersensitivity and adverse local tissue reactions, and occupational chromium exposure is a recognized sensitizer. Hypersensitivity should therefore be considered in any clinical use for arthritis. No drug interactions were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold** (osteoarthritis and all other predictions except rheumatoid arthritis)

**Rationale:**
- The top predictions, osteoarthritis and osteoarthritis susceptibility, are most likely artifacts of the link between chromium and orthopaedic implant materials, not evidence of a treatment effect. The remaining predictions have no supporting clinical evidence.
- **Rheumatoid arthritis** is the one exception. A completed Phase 2/3 RCT (n=60) and supportive animal data make it a worthwhile research question (evidence level L2), but not yet a basis for a Go decision.

**To proceed, the following is needed:**
- Safety information from the Health Canada package inserts (warnings and contraindications), which is currently missing and blocks safety screening
- Approved indication, dosage form and manufacturer details for the Canadian products
- Mechanism of action data for chromium
- Independent, larger, multi-centre replication of the rheumatoid arthritis trial with longer follow-up and long-term safety data
- A review of metal hypersensitivity risk in rheumatoid arthritis patients, particularly those with metal implants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

