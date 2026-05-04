---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Basiliximab
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

# Basiliximab: From Renal Transplant Rejection to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab is a chimeric monoclonal antibody originally used to prevent acute rejection in renal transplantation, working by blocking the IL-2 receptor (CD25) on activated T cells.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma**,
with **3 clinical trials** and **3 publications** currently supporting this direction — primarily through its role in managing graft-versus-host disease (GvHD) and regulatory T-cell (Treg) depletion in the context of stem cell transplantation for myeloma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of acute organ rejection in renal transplantation |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Basiliximab is a chimeric (human/murine) monoclonal antibody that specifically blocks CD25 (IL-2Rα), the alpha subunit of the interleukin-2 receptor, on the surface of activated T lymphocytes. By competitively inhibiting IL-2 binding, it prevents T-cell proliferation — the central mechanism behind both transplant rejection and immune dysregulation in graft-versus-host disease (GvHD). Detailed pharmacological MOA data from a regulatory database was not available for this report; the mechanistic link described here is derived from published clinical literature and the evidence pack's repurposing rationale.

The connection between Basiliximab and plasma cell myeloma operates through two distinct immunological pathways rather than a direct anti-tumour mechanism. First, many myeloma patients who relapse or are refractory to standard therapy proceed to allogeneic haematopoietic stem cell transplantation (allo-HSCT), where GvHD is a life-threatening complication. Basiliximab has been used in this setting to prevent or treat steroid-refractory GvHD, thereby enabling safer transplantation. Second, and more innovatively, Treg cells — which constitutively express CD25 — reconstitute rapidly after autologous SCT and are thought to suppress the graft-versus-myeloma (GvM) immune effect. Depleting these Tregs with Basiliximab post-ASCT has been explored as a strategy to enhance anti-tumour immunity.

It is important to note that Basiliximab does not target myeloma cells directly. Its predicted benefit is indirect: by optimising the immune environment around transplantation, it may improve outcomes for a subset of myeloma patients undergoing cellular therapy. This "treatment-enabling" rationale is scientifically plausible but remains early-stage, and the evidence base reflects this exploratory status.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Evaluated whether Treg depletion using Basiliximab prior to autologous SCT is feasible and safe in multiple myeloma patients; primary goal was to assess immune reconstitution and enhance post-transplant anti-myeloma responses |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Tested Basiliximab + cyclosporine combination for GvHD prevention after non-myeloablative allogeneic transplantation in blood cancers (patient population may include myeloma); provided feasibility data for GvHD management post-transplant |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | Terminated | 10 | Compared Basiliximab + cyclosporine versus cyclosporine alone for GvHD prevention; terminated early with very small sample size and no stated reason — limited interpretability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Clinical trial report (Phase 1 follow-up) | Journal for Immunotherapy of Cancer | Published results of the NCT01526096 pilot study; Basiliximab-mediated Treg depletion prior to ASCT was feasible in multiple myeloma; rapid Treg reconstitution post-ASCT identified as a potential target for enhancing GvM immune response |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Prospective pilot / case series | Bone Marrow Transplantation | Basiliximab was well-tolerated and effective in 17 patients with steroid-refractory acute GvHD after allogeneic SCT across multiple haematological malignancies (including multiple myeloma); IL-2R antagonism provided a viable salvage option in this high-risk setting |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case reports | American Journal of Kidney Diseases | Described 4 multiple myeloma patients who underwent successful kidney transplantation (with standard immunosuppression including IL-2R antagonists); context: myeloma-related renal failure is increasingly manageable, suggesting transplant-based strategies are feasible in myeloma survivors |

---

## Canada Market Information

Basiliximab is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on file. Clinicians considering use would need to access the drug through Health Canada's Special Access Programme (SAP) or within the context of a clinical trial.

---

## Safety Considerations

Detailed safety information (package insert warnings, contraindications, and drug interaction data) was not available in this evidence pack for the Canadian context. Please refer to the current Simulect® (basiliximab) prescribing information and Health Canada product monograph for comprehensive safety guidance, particularly regarding:
- Immunosuppression-related infection risk (opportunistic infections, reactivation of latent infections)
- Hypersensitivity reactions (anaphylaxis reported)
- Use in pregnancy and lactation

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The existing evidence supports Basiliximab as a GvHD management tool in transplant settings that include myeloma patients, but there are no completed Phase 2/3 trials directly evaluating Basiliximab as a treatment for plasma cell myeloma as the primary indication. The mechanism is indirect (immune modulation around transplantation, not direct tumour targeting), and all available trials are small pilot or Phase 1/2 studies with n ≤ 30 patients. The L3 evidence level is insufficient to justify a formal clinical development programme for this indication without additional groundwork.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Confirm whether Treg depletion via Basiliximab translates to measurable GvM enhancement in myeloma patients — biomarker endpoints (Treg counts, GvM activity) needed from the NCT01526096 follow-up cohort
- **Formal Phase 2 design**: A dedicated, adequately powered Phase 2 randomised controlled trial in myeloma patients undergoing ASCT or allo-HSCT with Basiliximab as the Treg-depleting intervention, with PFS or MRD negativity as primary endpoint
- **Safety data package**: Obtain the full Health Canada product monograph and any post-marketing safety signals for Basiliximab in immunocompromised haematological malignancy populations
- **Regulatory status confirmation**: Verify whether Basiliximab could be accessed via SAP in Canada for the intended patient population while a trial is being established
- **Differentiation from newer agents**: Assess whether Basiliximab's role in Treg depletion is competitive with or complementary to anti-CD25 immunotoxins, checkpoint inhibitors, or CAR-T strategies currently under investigation in myeloma

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

