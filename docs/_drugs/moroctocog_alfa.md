---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Moroctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa (ReFacto AF / Xyntha) is a B-domain deleted recombinant coagulation Factor VIII (BDD-rFVIII), originally developed for the prevention and treatment of bleeding episodes in patients with Hemophilia A (congenital Factor VIII deficiency).
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
with **7 clinical trials** retrieved (all indirectly related, covering BDD-rFVIII in hemophilia A) and **no direct publications** currently supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hemophilia A — prophylaxis and treatment of bleeding episodes (Factor VIII replacement) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Moroctocog alfa is a B-domain deleted recombinant Factor VIII that acts as a direct replacement within the intrinsic coagulation pathway. As the essential cofactor in the tenase complex (with Factor IXa), activated FVIII dramatically accelerates Factor X activation, triggering an exponential amplification of thrombin generation — the central enzyme of hemostasis.

Primary release disorder of platelets refers to inherited defects in platelet dense (δ) granule or alpha (α) granule secretion. When platelets fail to release ADP, serotonin, and thromboxane A₂ upon activation, the critical second-wave amplification of platelet recruitment is blunted, prolonging bleeding. The TxGNN prediction is mechanistically grounded in the fact that thrombin is the most potent physiologic platelet activator (via PAR-1 and PAR-4 receptors): if FVIII supplementation can drive a stronger thrombin burst at the site of injury, it may partially compensate for the diminished autocrine platelet activation signal that granule release defects create.

However, the link remains indirect. FVIII acts at the coagulation level, downstream of and independent from the granule secretion machinery itself. The root defect — impaired vesicle fusion or granule biogenesis — is not addressed by FVIII supplementation. This is therefore best characterized as a **theoretical bypass strategy**, not a targeted therapy. No dedicated clinical or preclinical studies in this population have been identified.

---

## Clinical Trial Evidence

*Note: No trials directly evaluating moroctocog alfa in primary platelet release disorders were identified. The trials below are related to BDD-rFVIII replacement in hemophilia A and serve as indirect mechanistic analogues.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | Evaluated rFVIIIFc-VWF-XTEN (BIVV001) as prophylaxis in previously treated patients ≥12 years with severe hemophilia A; assessed efficacy, safety, and joint health outcomes — provides Phase 3 safety database for extended-half-life FVIII class |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | Pediatric extension (<12 years) of the BIVV001 program; evaluated safety, PK, and joint health, with prophylaxis as primary endpoint — demonstrates tolerability of next-generation rFVIII in younger patients |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | Assessed PEGylated rFVIII (BAX 855) in severe hemophilia A patients undergoing elective surgery; establishes surgical hemostasis performance of the BDD-rFVIII class |

---

## Literature Evidence

Currently no related literature available for primary release disorder of platelets with moroctocog alfa.

---

## Canada Market Information

Moroctocog alfa is **not currently marketed in Canada**. Health Canada has issued no Drug Identification Numbers (DINs) for this product, and no license records are on file. No Canadian product authorization table can be constructed.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Formal safety data including TFDA-sourced warnings, contraindications, and drug interaction records were not available at the time of this analysis.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While thrombin's role as a platelet activator provides a biologically plausible — if indirect — rationale for FVIII augmentation in platelet release defects, the current evidence base is limited to preclinical mechanistic reasoning (L4). No clinical trials or published studies have prospectively evaluated moroctocog alfa in this population, and the foundational mechanistic assumption (that FVIII-driven thrombin amplification is a limiting step in these patients) has not been validated.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro thromboelastography or thrombin generation assays using platelet-poor or granule-release-deficient plasma supplemented with rFVIII to confirm that FVIII dosing shifts hemostatic outcomes meaningfully
- **MOA documentation**: Obtain formal mechanism-of-action data for moroctocog alfa from DrugBank API (gap DG002) to confirm tenase complex pharmacology specific to this product
- **Safety data retrieval**: Download and parse the Health Canada or TFDA package insert for moroctocog alfa to complete the S1 safety screen (gap DG001, currently Blocking)
- **Subtype stratification**: Clarify whether the predicted indication refers to dense granule deficiency (Hermansky-Pudlak, Chediak-Higashi) or alpha granule deficiency (Gray Platelet Syndrome) — mechanistic implications differ significantly
- **Clinical context review**: Consult hematology expertise to determine whether current standard-of-care therapies (DDAVP, antifibrinolytics, platelet transfusions) already adequately address this population, and whether a FVIII augmentation strategy offers net clinical value
- **Note on stronger signal**: The sibling indication in this pack — **Acquired Coagulation Factor Deficiency** (rank #4, L2 evidence, "Proceed with Guardrails") — has materially stronger evidentiary support including two completed Phase 2/3 trials of BDD-rFVIII (OBI-1/susoctocog alfa) in acquired hemophilia A; that direction may warrant prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

