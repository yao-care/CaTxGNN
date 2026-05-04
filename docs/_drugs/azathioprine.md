---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Transplant Rejection Prevention to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine (AZA) is a purine antimetabolite immunosuppressant with a long history of clinical use in preventing organ transplant rejection and treating autoimmune conditions, though it currently holds no registered Drug Identification Numbers (DINs) in Canada.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)**,
with **50 clinical trials** and **20 publications** currently supporting this direction, placing the evidence at **Level L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canadian DIN on record; known clinical use includes transplant rejection prevention and autoimmune diseases |
| Predicted New Indication | Inflammatory Bowel Disease (IBD) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Azathioprine acts as a prodrug that is enzymatically converted in vivo to 6-thioguanine nucleotides (6-TGN). These active metabolites interfere with de novo purine synthesis and become incorporated into replicating DNA, halting lymphocyte proliferation. Through the Rac1/Vav1 signalling pathway, AZA additionally triggers apoptosis in activated T cells—a key effector of mucosal damage in IBD. Downstream, this reduces the intestinal production of pro-inflammatory cytokines, including TNF-α, IL-12, and IL-17, and promotes mucosal healing.

Inflammatory bowel disease—encompassing Crohn's disease (CD) and ulcerative colitis (UC)—is fundamentally driven by dysregulated, T-cell-mediated immune responses against intestinal commensal flora, occurring against a background of genetic susceptibility (>200 risk loci identified). The immunosuppressive and antiproliferative mechanism of AZA maps directly onto this pathology. By controlling aberrant lymphocyte activation and lowering the mucosal cytokine burden, AZA sustains the steroid-induced remission that would otherwise require ongoing corticosteroid exposure, with all its associated toxicities.

This mechanistic fit is strongly corroborated by decades of clinical experience. Multiple Cochrane systematic reviews (2007, 2012, 2016, and 2025 updates) consistently affirm the benefit of AZA and 6-mercaptopurine in maintaining remission in both CD and UC. The drug is currently enrolled as the standard-of-care comparator arm in active Phase 4 randomised trials (e.g., the MIRACLE trial for UC), confirming that the medical community still regards it as a first-line immunomodulator. The TxGNN prediction therefore reflects a biologically and clinically well-grounded connection.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | MIRACLE trial: AZA as the standard-of-care comparator arm vs. mirikizumab in newly diagnosed moderate-to-severe UC; confirms AZA's current benchmark role in UC treatment guidelines |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | Recruiting | 166 | Head-to-head RCT comparing AZA vs. methotrexate in combination with adalimumab for CD; directly addresses which immunomodulator is superior in anti-TNF combination regimens |
| [NCT03464136](https://clinicaltrials.gov/study/NCT03464136) | Phase 3b | Completed | 386 | Ustekinumab vs. adalimumab in biologic-naïve CD patients who failed conventional therapy (including AZA/6-MP/methotrexate); provides efficacy context for positioning AZA within the therapeutic ladder |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Multicentre RCT: AZA vs. mesalazine for prevention of postoperative CD recurrence; supports AZA's role in long-term post-surgical disease management |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind RCT: AZA vs. mesalazine for prevention of clinical relapse in CD patients with moderate-to-severe endoscopic recurrence after surgery |
| [NCT05599347](https://clinicaltrials.gov/study/NCT05599347) | Phase 2 | Recruiting | 180 | Azithromycin pre-treatment to reduce anti-TNF immunogenicity in CD; AZA serves as background therapy, indirectly validating its role in anti-TNF combination regimens |
| [NCT03219359](https://clinicaltrials.gov/study/NCT03219359) | Phase 2 | Recruiting | 50 | AZA as maintenance therapy post-autologous stem cell transplantation in refractory CD; represents AZA's extended application in treatment-resistant IBD populations |
| [NCT00167882](https://clinicaltrials.gov/study/NCT00167882) | Phase 4 | Completed | 24 | 5-ASA concentration effect on AZA/6-MP metabolite levels in IBD; confirms that co-administered 5-ASA inhibits TPMT, elevating 6-TGN — directly informs clinical dose management |
| [NCT00521950](https://clinicaltrials.gov/study/NCT00521950) | N/A | Completed | 853 | First prospective RCT on pre-treatment TPMT genotyping cost-effectiveness in IBD; foundational evidence for precision dosing of AZA to maximise efficacy and minimise adverse drug reactions |
| [NCT00904878](https://clinicaltrials.gov/study/NCT00904878) | N/A | Recruiting | 1,500 | Large multicentre prospective cohort study of pregnancy and neonatal outcomes in women with IBD on AZA and other agents; key evidence base for guardrail development in reproductive-age patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Updated 2025 Cochrane review confirming AZA/6-MP for maintenance of remission in UC; highest-quality current synthesis covering all available RCT data |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab + AZA vs. AZA monotherapy in acute severe UC responding to IV steroids; directly addresses the combination vs. monotherapy question in high-acuity disease |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | 2016 Cochrane update on AZA/6-MP for UC remission maintenance; establishes evidence continuity across review cycles |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | 2012 Cochrane review confirming AZA's efficacy in UC maintenance remission despite historical controversy |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Alimentary Pharmacology & Therapeutics | Meta-analysis resolving earlier debate on whether AZA/6-MP is as effective in UC as in CD; supports use across both IBD subtypes |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Narrative Review | Journal of Crohn's & Colitis | State-of-the-art expert review of thiopurine treatment in IBD; covers pharmacogenomics, emerging toxicity insights, and positioning within the treatment algorithm |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Systematic Review | World Journal of Gastroenterology | Review of metabolite monitoring strategies; provides practical guidance on targeting 6-TGN levels for efficacy while avoiding 6-MMP-associated hepatotoxicity and myelotoxicity |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Mechanistic Study | Cell Reports Medicine | Identifies Blautia wexlerae as a gut microbiota driver of AZA therapy failure via decreased 6-MP bioavailability; clinically relevant for predicting non-response and personalising therapy |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Review of Gastroenterology & Hepatology | Molecular mechanism review of AZA in IBD; summarises Rac1/Vav1-mediated T-cell apoptosis and implications for therapeutic optimisation |
| [9412914](https://pubmed.ncbi.nlm.nih.gov/9412914/) | 1997 | RCT | Journal of Clinical Gastroenterology | Retrospective RCT (n=56) evaluating AZA in steroid-resistant and steroid-dependent UC; one of the foundational efficacy datasets for AZA in UC |

---

## Canada Market Information

Azathioprine currently holds **no Drug Identification Numbers (DINs)** in Canada under this regulatory dataset and is listed as **not marketed**.

> **Note:** Clinicians should independently verify the current Health Canada drug product database status. Azathioprine may be accessible through generic product listings not yet captured in this dataset, compounding pharmacies, or the Special Access Programme (SAP) for patients with unmet clinical needs.

---

## Safety Considerations

Detailed Health Canada product monograph data (warnings, contraindications, and drug-drug interactions) were not available in the current Evidence Pack. Based on published clinical evidence, the following considerations are relevant for IBD use:

- **Myelosuppression**: Dose-dependent bone marrow suppression is the most serious toxicity. Pre-treatment TPMT genotyping or phenotyping is strongly recommended — homozygous TPMT-deficient patients face life-threatening myelotoxicity at standard doses.
- **Drug interaction — 5-ASA agents**: Co-administration inhibits TPMT enzymatic activity, raising 6-TGN levels. Dose reduction of AZA may be required when initiating 5-ASA therapy concurrently.
- **Infectious complications**: Immunosuppression increases susceptibility to opportunistic infections, including herpes zoster. Vaccinations (pneumococcal, influenza, HZ) should be completed before initiation.
- **Lymphoproliferative risk**: Long-term thiopurine use, especially in combination with anti-TNF biologics, is associated with a modestly elevated risk of lymphoma, particularly hepatosplenic T-cell lymphoma in young males.
- **Pregnancy**: Risk to fetal outcomes is an active area of investigation (see NCT00904878). Risk-benefit discussion with the patient is essential; current guidelines generally allow continuation in IBD patients where disease control outweighs risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting azathioprine in inflammatory bowel disease reaches Evidence Level L1, anchored by multiple completed Phase 3 RCTs, four independent Cochrane systematic reviews, and at least two meta-analyses. The drug's immunosuppressive mechanism directly targets the T-cell-driven inflammatory pathology of IBD, and it currently serves as the standard-of-care reference arm in active Phase 4 trials — a position reserved for treatments with firmly established efficacy. The primary barrier to clinical deployment in Canada is regulatory rather than scientific: no DIN is currently on record, and safety monitoring protocols (particularly TPMT-guided dosing) must be formalised before routine use.

**To proceed, the following is needed:**
- **Regulatory pathway**: Confirm Health Canada market status; if no DIN exists, determine whether a generic product application, SAP approval, or compounding route is applicable.
- **TPMT testing protocol**: Establish a standardised pre-treatment TPMT genotyping or phenotyping workflow to stratify patients by myelotoxicity risk and guide initial dosing.
- **Therapeutic drug monitoring plan**: Define monitoring intervals for 6-TGN and 6-MMP metabolite levels, CBC with differential, hepatic enzymes, and renal function.
- **Vaccination checklist**: Ensure all patients are current on pneumococcal, influenza, and herpes zoster vaccinations prior to starting immunosuppression.
- **Drug interaction management**: Clarify institutional guidance on AZA dose adjustment when co-administered with 5-ASA agents.
- **Reproductive safety counselling**: Develop a structured counselling protocol for women of childbearing age, incorporating evidence from the ongoing PIANO study (NCT00904878) as data mature.
- **Full product monograph review**: Obtain and incorporate the complete Canadian product monograph (or reference jurisdiction equivalent) to finalise the formal safety assessment for this evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

