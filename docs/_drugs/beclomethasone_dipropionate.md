---
layout: default
title: Beclomethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 1
---

# Beclomethasone Dipropionate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Beclomethasone Dipropionate: From Asthma to Atopic Eczema

## One-Sentence Summary

Beclomethasone Dipropionate (BDP) is a potent synthetic glucocorticoid currently used for inhaled asthma management and intranasal treatment of allergic rhinitis. The TxGNN model predicts it may be effective for **atopic eczema** — specifically via oral administration in refractory cases — with **0 registered clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma (inhaled); Allergic rhinitis (intranasal) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in the structured dataset. Based on established pharmacological knowledge, Beclomethasone Dipropionate is a high-potency synthetic glucocorticoid. It acts by binding intracellular glucocorticoid receptors (GR), which in turn suppresses the NF-κB transcription factor and downregulates pro-inflammatory Th2 cytokines — including IL-4, IL-13, and IL-31.

Atopic eczema is driven by precisely this Th2-skewed immune dysregulation, combined with impaired skin barrier function. The same cytokine cascade that BDP suppresses (IL-4, IL-13, IL-31) is responsible for the hallmark features of atopic eczema: intense pruritus, skin inflammation, and barrier breakdown. This mechanistic overlap makes the TxGNN prediction biologically well-grounded.

It is worth noting that topical corticosteroids (TCS) are already the established first-line treatment for atopic eczema — the novel repurposing angle here is specifically **oral BDP** for refractory, difficult-to-treat atopic eczema. This route potentially avoids heavier systemic immunosuppressants (e.g., cyclosporine) while leveraging BDP's gut-level immune modulation. Early clinical evidence from the 1980s–1990s demonstrated feasibility, though this administration route is not currently approved in Canada.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6434024](https://pubmed.ncbi.nlm.nih.gov/6434024/) | 1984 | RCT | British Medical Journal | Double-blind placebo-controlled crossover trial in 26 children with severe atopic eczema; combined oral + nasal BDP produced significant improvement over placebo across 4 weeks, with only mild adrenal suppression and no adverse effects observed |
| [1476023](https://pubmed.ncbi.nlm.nih.gov/1476023/) | 1992 | Clinical Case Series | Acta Dermato-Venereologica | Oral BDP (mean 1,000 µg/day) achieved stable disease control in 10/14 children with difficult atopic dermatitis; growth deceleration noted at maintenance dose, raising pediatric safety considerations |
| [30911861](https://pubmed.ncbi.nlm.nih.gov/30911861/) | 2019 | Formulation Study | AAPS PharmSciTech | Development and characterization of BDP-loaded mixed micelles incorporated into hydrogel for dermal delivery; sub-chronic dermatitis animal model confirms enhanced dermal BDP bioavailability via novel formulation |
| [14522624](https://pubmed.ncbi.nlm.nih.gov/14522624/) | 2003 | Clinical Safety Study | Journal of Dermatological Treatment | Assessed effects of intensive steroid wet-wrap therapy on short-term growth and bone turnover in 8 prepubertal children with atopic eczema; provides critical safety reference data for corticosteroid-based atopic eczema regimens |
| [8765824](https://pubmed.ncbi.nlm.nih.gov/8765824/) | 1996 | Clinical Study | Journal of Allergy and Clinical Immunology | Topical steroids in atopic dermatitis may paradoxically enhance in vitro IgE production; underscores the need for careful monitoring and the limitations of long-term corticosteroid use in atopic eczema |
| [19874229](https://pubmed.ncbi.nlm.nih.gov/19874229/) | 2009 | Comparative Animal Study | Immunopharmacology and Immunotoxicology | Head-to-head comparison of BDP vs mometasone furoate in murine ear edema model; mometasone showed superior local anti-inflammatory potency with lower systemic HPA axis suppression relative to BDP |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews HPA axis suppression risk from intranasal corticosteroids in patients with comorbid asthma and atopic dermatitis; directly relevant to systemic safety monitoring for patients on multi-route BDP |
| [9463794](https://pubmed.ncbi.nlm.nih.gov/9463794/) | 1998 | Review | Drugs | Comprehensive review of mometasone (a 16α-methyl analogue of BDP) for inflammatory dermatoses including atopic dermatitis; confirms class-level efficacy of glucocorticoids in atopic eczema and provides a reference benchmark for BDP |
| [11488426](https://pubmed.ncbi.nlm.nih.gov/11488426/) | 2001 | Review | Japanese Journal of Pharmacology | Broad review of glucocorticoids — specifically naming BDP and fluticasone — for allergic diseases; confirms mechanistic rationale and established anti-inflammatory efficacy across the Th2 disease spectrum |
| [37023229](https://pubmed.ncbi.nlm.nih.gov/37023229/) | 2023 | Computational Study | Journal of Chemical Information and Modeling | Knowledge graph–based drug repurposing framework (DrugRep-KG) that validates computational prediction methodology; provides methodological context for interpreting TxGNN's BDP–atopic eczema association |

---

## Canada Market Information

Beclomethasone Dipropionate currently has **no Drug Identification Numbers (DINs) on record** and is not marketed in Canada under this active ingredient profile. No licensed products are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (warnings, contraindications, and drug interactions) were not available in this evidence pack. Key known class-level concerns for glucocorticoids include HPA axis suppression, growth retardation in children, and adrenal suppression — particularly relevant given the oral route being explored.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 1984 double-blind RCT and a 1992 clinical case series provide early proof-of-concept for oral BDP in refractory atopic eczema, and the mechanistic rationale is strong; however, the absence of modern clinical trials, zero DIN registrations in Canada, and unresolved safety data gaps mean this candidate requires significant further validation before advancing.

**To proceed, the following is needed:**
- Retrieve and review the full prescribing information (package insert) to formally document warnings, contraindications, and drug interactions
- Assess HPA axis suppression risk and growth impact at oral doses required for atopic eczema, particularly in pediatric patients
- Evaluate the current clinical landscape: with dupilumab (IL-4/IL-13 blockade) now approved in Canada, determine whether an unmet need for oral BDP still exists in refractory atopic eczema
- Conduct a systematic literature search for any post-1992 clinical data on oral BDP in atopic dermatitis
- Define a regulatory pathway for a potential new DIN submission in Canada if evidence is deemed sufficient
- Design a prospective pilot study protocol with growth monitoring and cortisol surveillance if a clinical investigation is planned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

