---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: From Inflammatory Skin Conditions to Alopecia Areata

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid widely used clinically for inflammatory, allergic, and autoimmune conditions — though no Health Canada DINs were identified in this dataset. The TxGNN model predicts it may be effective for **Alopecia Areata (AA)**, with **7 clinical trials** and **20 publications** currently supporting this direction; notably, betamethasone is already recognized in international clinical practice as a standard treatment for AA, making this a strong evidence-backed prediction rather than a novel hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory and autoimmune conditions (synthetic glucocorticoid; no DIN identified in this dataset) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (0 DINs on file) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betamethasone is a synthetic fluorinated glucocorticoid belonging to the same pharmacological class as prednisolone and dexamethasone, but with significantly greater potency (approximately 25–40 times that of prednisolone on a weight basis). Although detailed MOA data was not captured in this Evidence Pack, its mechanism is well-established in the pharmacological literature: betamethasone binds the intracellular glucocorticoid receptor alpha (GR-α), translocates to the nucleus, and suppresses the NF-κB transcription pathway. This leads to downregulation of key pro-inflammatory cytokines — including IL-1β, IL-6, and IFN-γ — and reduces lymphocyte trafficking and activation at sites of inflammation.

Alopecia areata is a T cell–mediated autoimmune disease in which CD8+ cytotoxic T cells aberrantly attack hair follicles at the bulge region, collapsing the normal state of immune privilege that healthy follicles maintain. This targeted immune attack causes non-scarring, often patchy hair loss. Betamethasone's broad immunosuppressive action directly addresses this pathophysiology: by suppressing perifollicular T cell infiltration and restoring the follicular immune microenvironment, it can halt the autoimmune assault and allow hair regrowth. This rationale is mechanistically sound and mirrors the approach used with other corticosteroids (e.g., triamcinolone, methylprednisolone) that have an established role in AA.

Clinical application of betamethasone for AA spans multiple routes — topical formulations (cream, lotion), intralesional injection, and oral mini-pulse regimens — each targeting different severities of disease. The breadth of clinical trial activity and published literature reviewed below confirms that this is not a speculative repurposing: betamethasone is actively studied and used in this indication globally, and the TxGNN model's high-confidence prediction aligns with real-world clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Completed | 60 | Head-to-head RCT comparing oral betamethasone mini-pulse (BOMP) vs. weekly azathioprine pulse in moderate-to-severe AA; provides direct efficacy and safety data for oral betamethasone in this indication |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Completed | 50 | Randomized comparison of topical betamethasone vs. topical latanoprost for localized AA; betamethasone serves as the active standard-of-care arm, confirming its real-world reference status |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Completed | 40 | RCT comparing combined topical 5% minoxidil + potent topical corticosteroid (including betamethasone) vs. intralesional triamcinolone injection in AA; supports betamethasone in combination topical regimens |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Unknown | 59 | Comparison of topical cetirizine 1% vs. topical betamethasone valerate 0.1% in localized AA; betamethasone as the active control arm; status unknown limits interpretability |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Unknown | 60 | Three-arm trial evaluating topical pentoxifylline 2% and metformin 10% gels vs. topical betamethasone valerate 0.1% cream in patchy AA; betamethasone serves as benchmark comparator |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | Unknown | 30 | Safety/efficacy study of clobetasol propionate 0.05% foam in central centrifugal cicatricial alopecia (CCCA); different drug and different alopecia subtype — limited direct relevance |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicenter prospective study of CCCA treatment outcomes; betamethasone may be one comparator but the indication (CCCA vs. AA) and status (still recruiting) limit applicability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-Analysis | Cochrane Database of Systematic Reviews | Cochrane NMA synthesizing evidence across immunosuppressants, hair growth stimulants, and contact immunotherapy for AA; highest-quality synthesis of the treatment landscape including corticosteroids |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | Journal of the American Academy of Dermatology | Microneedle-assisted transdermal delivery of compound betamethasone in AA; demonstrates improved delivery and efficacy vs. standard injection, addressing the pain barrier of intralesional therapy |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iranian Journal of Pharmaceutical Research | Double-blind, placebo-controlled RCT comparing oral betamethasone pulse (3 mg weekly), methotrexate (15 mg weekly), and combination in severe AA (n=36); direct evidence for oral betamethasone efficacy |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Clinical Study | Cureus | Prospective study assessing efficacy, safety, and tolerability of oral betamethasone mini-pulses in moderate-to-severe AA; intermittent dosing shown as promising alternative to continuous systemic steroids |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Comparative Study | Cureus | Head-to-head comparison of topical betamethasone dipropionate vs. topical minoxidil in AA patients; evaluates relative efficacy of the two most commonly used topical agents |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Comprehensive review of corticosteroid pulse therapy (including betamethasone) for AA: efficacy, relapse rates, side effects, and prognostic factors across different pulse regimens |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | Comparative RCT | Archives of Dermatological Research | RCT of fractional CO₂ laser alone vs. combined with topical betamethasone valerate in AA (n=30); supports betamethasone as additive component in laser-based combination strategies |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative RCT | Dermatologic Therapy | Six-arm blinded RCT comparing latanoprost, minoxidil, betamethasone, and combinations (18 patients per group) in AA; directly evaluates betamethasone efficacy and satisfaction vs. alternatives |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | Journal of Dermatological Treatment | Within-patient randomized controlled trial comparing intralesional betamethasone vs. triamcinolone acetonide in localized AA; establishes comparative effectiveness data specific to intralesional betamethasone |
| [37765130](https://pubmed.ncbi.nlm.nih.gov/37765130/) | 2023 | Translational/Experimental | Pharmaceuticals (Basel) | Development of polymeric and lipid nanoparticles co-entrapping betamethasone and minoxidil for follicle-targeted topical delivery in AA; supports rational formulation development for reduced systemic exposure |

---

## Safety Considerations

Detailed safety warnings and contraindications specific to betamethasone were not captured in this Evidence Pack's regulatory dataset. Based on the available clinical trial data, the following considerations are relevant to the AA indication:

- **Route-specific risks**: Oral and systemic corticosteroid use carries well-recognized risks including HPA axis suppression, hyperglycemia, weight gain, hypertension, osteoporosis, and immunosuppression — especially with prolonged use. The oral mini-pulse regimen (e.g., 3 mg once weekly) was specifically designed to minimize these effects compared to daily systemic dosing.
- **Topical/intralesional risks**: Local skin atrophy, telangiectasia, and adrenal suppression with extensive topical application; post-injection subcutaneous atrophy with intralesional use.
- **Infection risk**: Immunosuppression from systemic betamethasone may increase susceptibility to bacterial, fungal, and viral infections.

Please refer to the product monograph for complete warnings, contraindications, and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for betamethasone in alopecia areata is substantial and well-established: multiple completed Phase 2/4 RCTs directly testing betamethasone (both topical and oral mini-pulse formulations), a 2023 Cochrane network meta-analysis, and 20 publications spanning RCTs, reviews, and comparative studies collectively support an L2 evidence level. This is not speculative repurposing — betamethasone is a recognized clinical option for AA internationally, and the TxGNN model's 99.97% prediction score reflects this strong pharmacological and clinical alignment.

**To proceed, the following is needed:**

- **Health Canada DIN status clarification**: This Evidence Pack shows zero DINs on file; betamethasone products may be marketed under compound formulations or via individual DINs not captured here. A targeted Health Canada Drug Product Database query is recommended before drawing regulatory conclusions.
- **Formal package monograph review**: TFDA/Health Canada product monograph warnings, contraindications, and drug-drug interactions must be retrieved and assessed before entering a formal safety evaluation (DG001 and DG002 data gaps should be resolved).
- **Route-of-administration stratification**: A structured benefit-risk assessment should differentiate between topical, intralesional, and oral mini-pulse routes, as the risk profiles differ substantially — topical use is generally low-risk while systemic use requires monitoring protocols.
- **Population-specific monitoring plan**: Define CBC, fasting glucose, blood pressure, and bone density monitoring schedules appropriate to the intended use duration and patient population (adults vs. pediatric, localized vs. severe AA).
- **Comparison with newer AA therapies**: Evaluate betamethasone's positioning relative to approved JAK inhibitors (e.g., baricitinib, ritlecitinib) which represent a newer standard for moderate-to-severe AA, particularly for patients where corticosteroid use is contraindicated or has failed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

