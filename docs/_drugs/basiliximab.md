---
layout: default
title: Basiliximab
parent: Model Prediction Only (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Basiliximab: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Not available"
monitor_inn: "Basiliximab"
predicted_indications: ["plasma cell myeloma", "bronchitis", "indolent plasma cell myeloma", "hemoglobinopathy", "gastric carcinoma", "diffuse gastric adenocarcinoma", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "Jeune syndrome situs inversus"]
---

# Basiliximab
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

# Basiliximab: From Transplant Immunosuppression to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab is an anti-CD25 (IL-2 receptor alpha) monoclonal antibody, marketed in Canada as SIMULECT.
The TxGNN model predicts it may be useful for **plasma cell myeloma**,
supported by **3 clinical trials** (all small, and mostly aimed at preventing graft-versus-host disease or depleting regulatory T cells around transplant) and **4 publications**. Any benefit would come from immune modulation in the transplant setting, not direct anti-myeloma activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Canadian licence record has no indication text) |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L2 (one completed Phase 2 trial, single-arm and small; no randomized Phase 2/3 evidence in myeloma) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Basiliximab blocks IL-2Rα (CD25) on activated T cells and regulatory T cells (Tregs). Detailed mechanism-of-action data are not available in the data compiled for this report, but this is the well-known action of the antibody.

In myeloma, it has been studied in two ways. One is preventing graft-versus-host disease (GVHD) after nonmyeloablative allogeneic transplant. The other is depleting Tregs around autologous stem cell transplantation, in the hope of strengthening immune responses against myeloma cells. Treg depletion is the more direct anti-myeloma rationale. A published Phase 1 pilot reports that Tregs reconstitute rapidly after autologous transplant and may suppress anti-myeloma immunity.

The effect is immune modulation, not direct cytotoxicity against myeloma cells. The prediction is plausible as an adjunct to transplant, but not as a standalone myeloma therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Pilot of Treg depletion with basiliximab around autologous stem cell transplant in myeloma; tests feasibility and safety (most directly relevant) |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab plus cyclosporine to prevent GVHD after nonmyeloablative allotransplant; population includes myeloma, but the endpoint is GVHD, not myeloma control |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | NA | Terminated | 10 | Basiliximab plus cyclosporine vs cyclosporine alone for GVHD prevention; early termination gives little interpretable evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Phase 1 trial report | J Immunother Cancer | Pilot of Treg depletion around autologous transplant in myeloma, based on the idea that rapidly reconstituted Tregs inhibit anti-myeloma immunity |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Cohort | Bone Marrow Transplant | Basiliximab was well tolerated and effective in 17 patients with steroid-refractory acute GVHD after allogeneic transplant (a minority had myeloma) |
| [42379467](https://pubmed.ncbi.nlm.nih.gov/42379467/) | 2026 | Case report/Review | Am J Kidney Dis | Kidney transplantation after CAR-T therapy in myeloma; context is transplant, not anti-myeloma efficacy |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case reports | Am J Kidney Dis | Four patients with myeloma who received kidney transplants after achieving disease response; context is transplant, not anti-myeloma efficacy |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242815 | SIMULECT | Not listed | Not listed |

---

## Safety Considerations

**Drug Interactions**: 69 interactions were identified in the interaction database. Examples by severity:
- **Major**: adalimumab, baricitinib, certolizumab pegol, BCG live vaccine (tice substrain). These mostly reflect additive immunosuppression and infection risk.
- **Moderate**: roflumilast, azathioprine, alemtuzumab, anakinra, canakinumab, alefacept, and several vaccines (tetanus toxoid, anthrax, adenovirus, live cholera).
- **Minor**: zinc salts (acetate, gluconate, sulfate, chloride).

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only myeloma-specific evidence is a small Phase 1 pilot (n=30) and a small Phase 2 trial (n=17) with GVHD endpoints. Neither shows anti-myeloma efficacy. The proposed role is transplant-adjunct immune modulation, not a direct treatment.
- Package insert safety data are missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism-of-action data
- Published outcomes from NCT01526096 (response, relapse, progression-free survival)
- A randomized, controlled study with myeloma-specific efficacy endpoints
- A defined target population (for example, autologous transplant recipients) and an infection-risk monitoring plan, given the many immunosuppressant interactions

---

### Notes on Other Predicted Indications

- **Hemoglobinopathy (score 94.28%)**: This has the largest trial (NCT02342145, Phase 4, n=205, completed) for GVHD prevention in thalassemia transplant. It supports basiliximab as supportive care, not as a treatment for the hemoglobin disorder. Whether the study was randomized is not confirmed in the available data.
- **Bronchitis and gastric carcinoma**: The literature concerns lung-transplant induction (likely a confusion with bronchiolitis obliterans) and a post-transplant surgical case report. Neither supports a therapeutic role.
- **Other predictions** (indolent myeloma, diffuse gastric adenocarcinoma, chromosome 16p deletion, beta-thalassemia with other manifestations, glucophosphate isomerase deficiency, Jeune syndrome): These rest on model prediction alone, with no clinical trials or literature, and are not recommended for follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

