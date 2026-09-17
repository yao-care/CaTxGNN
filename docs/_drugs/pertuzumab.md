---
layout: default
title: Pertuzumab
parent: High Evidence (L1-L2)
nav_order: 613
evidence_level: L1
indication_count: 10
---

# Pertuzumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor-Negative Breast Cancer

## One-Sentence Summary

Pertuzumab (DrugBank DB06366) is an anti-HER2 monoclonal antibody already used clinically for HER2-positive breast cancer in combination with trastuzumab and chemotherapy. TxGNN scored 10 candidate indications for this drug; among them, **progesterone-receptor (PR) negative breast cancer** stands out with the strongest support — **20 publications**, including two Phase III RCTs — while most of the other predicted nodes (e.g., "normal breast-like subtype," rare sarcomas, HHV-8-related tumors) have **zero** supporting trials or literature and are pure model output.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (established use, in combination with trastuzumab ± chemotherapy) — *not captured in the evidence pack's Taiwan license data* |
| Predicted New Indication | Progesterone-receptor negative breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Licenses (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: `taiwan_regulatory.licenses` is empty and `total_licenses = 0`, so no DIN/license-level data exists for this drug in Taiwan.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap, DG002). Based on the information embedded in the evidence pack's own repurposing rationale, pertuzumab is a monoclonal antibody that inhibits HER2 dimerization, blocking HER2/HER3 heterodimer-driven signaling — a distinct binding epitope from trastuzumab, which is why the two are used together clinically.

Of the 10 candidate indications TxGNN generated for pertuzumab, most (normal breast-like subtype, ectomesenchymoma, malignant cutaneous granular cell tumor, HHV-8-related tumor, prostatic urethra urothelial carcinoma, kidney pelvis sarcomatoid transitional cell carcinoma) are unsupported model outputs (L5, "Hold") with no trials or literature returned by any query. **PR-negative breast cancer**, however, sits within the HER2-positive/hormone-receptor-negative breast cancer population — a population pertuzumab already treats in its approved regimens (with trastuzumab and docetaxel, in the neoadjuvant/adjuvant and metastatic settings). The mechanistic link here is therefore strong and direct rather than speculative: this TxGNN "prediction" largely reflects a real-world population already targeted by the drug's biology, refined by hormone-receptor subtyping.

A related, though weaker, signal appears at rank 4 ("breast tumor luminal A or B," L2, "Proceed with Guardrails"), where a dedicated Phase II trial (NCT04569747, ADEPT) is testing pertuzumab + trastuzumab + endocrine therapy in hormone-receptor-positive/HER2-positive early breast cancer — reinforcing that pertuzumab's TxGNN-favored "new" indications cluster around HER2-positive breast cancer subtyped by hormone-receptor status, not a mechanistically unrelated disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for progesterone-receptor negative breast cancer specifically (0 trials returned; see Query Log).

*For context, the adjacent candidate node "breast tumor luminal A or B" (rank 4) does have a directly relevant registered trial: [NCT04569747](https://clinicaltrials.gov/study/NCT04569747) (ADEPT), Phase 2, Recruiting, n=375 — pertuzumab + trastuzumab + adjuvant endocrine therapy in Stage I HR-positive/HER2-positive breast cancer.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (Phase 3, biosimilar) | British Journal of Cancer | QL1209 (pertuzumab biosimilar) vs. reference pertuzumab + trastuzumab + docetaxel in HER2+/ER-PR-negative neoadjuvant breast cancer; phase III equivalence trial |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | RCT (DECRESCENDO) | Future Oncology | De-escalated chemotherapy with anti-HER2 therapy in HR-negative, HER2-positive, node-negative early breast cancer (NCT04675827) |
| [41401771](https://pubmed.ncbi.nlm.nih.gov/41401771/) | 2026 | RCT (Phase 3, biosimilar equivalence) | ESMO Open | TQB2440 (pertuzumab biosimilar) vs. reference pertuzumab in HER2+/ER-PgR-negative early/locally advanced breast cancer |
| [37723497](https://pubmed.ncbi.nlm.nih.gov/37723497/) | 2023 | Real-world cohort/subgroup analysis | World Journal of Surgical Oncology | PR status is a more decisive factor than ER status for benefit of adding pertuzumab to neoadjuvant therapy in HER2+/node-positive breast cancer (China) |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | Systematic Review | International Journal of Molecular Sciences | Pertuzumab + trastuzumab + docetaxel as adjuvant doublet therapy for HER2-positive breast cancer |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Expert Review | Clinical Breast Cancer | BCTEG roundtable on clinical developments and practice guidance for HER2-positive breast cancer |
| [33902424](https://pubmed.ncbi.nlm.nih.gov/33902424/) | 2022 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | Immunotherapy for breast cancer, including trastuzumab/pertuzumab context |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Review | Southern Medical Journal | Neoadjuvant and adjuvant therapies for breast cancer across molecular subtypes |
| [33662161](https://pubmed.ncbi.nlm.nih.gov/33662161/) | 2021 | Review | European Journal of Clinical Investigation | CDK4/6 and PI3K inhibitors combined with anti-HER2 blockade in HER2-positive breast cancer |
| [27435628](https://pubmed.ncbi.nlm.nih.gov/27435628/) | 2016 | Review | Clinical Breast Cancer | Dual HER2 blockade shows greater benefit magnitude in hormone-receptor-negative vs. -positive breast cancer |

---

## Canada Market Information

Pertuzumab is currently **not marketed in Taiwan** — `taiwan_regulatory.total_licenses = 0` and no license records are present in the evidence pack, so no product-level table can be generated.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody, HER2-dimerization inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (as a monoclonal antibody, intrinsic myelosuppression is not typically class-defining; myelosuppression in clinical use is largely attributable to concurrent chemotherapy partners such as docetaxel) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Cardiac function (LVEF) given anti-HER2 class cardiotoxicity risk; CBC and infusion-reaction monitoring when combined with cytotoxic partners |
| Handling Protection | Standard biologic infusion handling; not subject to conventional cytotoxic drug handling regulations |

*TFDA label warnings/contraindications are a Blocking data gap (DG001); the above reflects general anti-HER2 antibody class characteristics, not confirmed product-specific toxicity data.*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Progesterone-receptor negative breast cancer (HER2-positive/HR-negative population) is supported by Level 1 evidence — two Phase III equivalence RCTs and a dedicated real-world subgroup analysis — but this largely represents refinement of pertuzumab's already-established anti-HER2 use rather than a mechanistically novel repurposing target. Taiwan-specific regulatory and safety label data are entirely missing (Blocking gap), and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action documentation
- Confirmation of Taiwan licensing/import status given 0 current licenses
- Clarification of true "novelty" of this indication relative to pertuzumab's existing approved use, versus adjacent low-evidence candidates (e.g., "normal breast-like subtype," ectomesenchymoma) which remain L5/Hold and are not actionable without new data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

