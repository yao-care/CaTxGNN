---
layout: default
title: Nystatin
parent: Moderate Evidence (L3-L4)
nav_order: 567
evidence_level: L3
indication_count: 10
---

# Nystatin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Nystatin: From Fungal Infections (Candidiasis) to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal antibiotic long used to treat *Candida* (yeast) infections of the skin, oral cavity, and vagina. The TxGNN model predicts it may also be effective for **Vulvovaginitis**, with a prediction score of **99.92%**, but the 20 supporting publications on file are attributed to a closely related node ("vulvitis") rather than to vulvovaginitis directly, so current support should be read as indirect/extrapolated rather than as direct trial evidence for this exact term.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (candidiasis) — based on Nystatin's known pharmacology; no Canada license text is available to confirm the on-label wording |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nystatin is a polyene macrolide antifungal that binds ergosterol in the fungal cell membrane, forming pores that cause leakage of cell contents — the classical mechanism by which polyenes kill *Candida* species. This is not a new mechanism being repurposed; it is Nystatin's core, decades-old mode of action.

Vulvovaginitis is inflammation of the vulva and vagina, and *Candida albicans* is one of its most common infectious causes (accounting for an estimated 85–90% of vulvovaginal candidiasis cases per the literature on file). Because Nystatin's antifungal activity against *Candida* is already clinically established for vaginal and vulvar candidal infections, a high TxGNN score for "vulvovaginitis" is mechanistically expected rather than surprising.

The one caveat worth flagging: the evidence pack's own annotation notes that no trials or publications were retrieved directly against the search term "vulvovaginitis" — the 20 supporting papers are indexed under the adjacent node "vulvitis" (essentially vulvovaginal candidiasis) and are being used as an indirect extrapolation. Since vulvitis and vulvovaginitis substantially overlap clinically (both frequently driven by the same candidal infection), this extrapolation is reasonable, but it should be documented as indirect evidence rather than direct confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered directly against "vulvovaginitis." (Two trials were retrieved for a different, mechanistically unrelated candidate node — "disease of orbital region" — and are not relevant here; see Data Gaps below.)

---

## Literature Evidence

*Note: the following 20 publications were retrieved under the closely related node "vulvitis" (vulvovaginal candidiasis), not under "vulvovaginitis" directly. They are presented as indirect supporting evidence per the evidence pack's own rationale annotation.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21918792](https://pubmed.ncbi.nlm.nih.gov/21918792/) | 2012 | Comparative Study | Acta Dermato-Venereologica | Compared fluconazole vs. nystatin efficacy in 932 Brazilian women with vaginal *Candida*; nystatin was an effective treatment arm |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | In 287 *Candida* isolates from complicated VVC, correlated in vitro fluconazole/nystatin susceptibility with clinical outcome |
| [31969236](https://pubmed.ncbi.nlm.nih.gov/31969236/) | 2019 | Open-label Study | Acta Dermatovenerologica Croatica | GENIE study: 189 subjects treated with oxytetracycline + nystatin vaginal tablets; beneficial effect in 100% of patients |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclinical (Animal Study) | BMC Microbiology | Nystatin enhanced immune response against *C. albicans* and protected vaginal epithelial ultrastructure in a rat VVC model |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | In vitro Study | J Infect Dev Ctries | Compared tea tree oil vs. nystatin inhibition zones against vaginal *Candida* isolates in pregnancy |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Clinical Study | Ceska Gynekologie | Evaluated vaginal nystatin + nifuratel for diagnosis and therapy of mixed/miscellaneous vulvovaginitis |
| [4584828](https://pubmed.ncbi.nlm.nih.gov/4584828/) | 1973 | Clinical Trial | J Obstet Gynaecol Br Commonw | Early comparative trial of clotrimazole and nystatin in vaginal moniliasis |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Reviews topical antifungals; notes nystatin's historical first-line role in VVC, later surpassed by azoles |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Vulvovaginal candidiasis is the second most common cause of vaginitis; *C. albicans* causes 85–90% of cases |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | General clinical review of vulvovaginal candidiasis diagnosis and management |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nystatin's antifungal mechanism against *Candida*-driven vulvovaginal disease is well established, and the TxGNN prediction score is high (99.92%, L3). However, the 20 supporting papers are indirect — attributed to the adjacent "vulvitis" node rather than confirmed directly against "vulvovaginitis" — and two data gaps flagged in this evidence pack are significant: TFDA label warnings/contraindications are marked **Blocking** (prevents entry into the S1 safety review stage), and formal MOA data is marked **High** severity. The drug is also currently not marketed in Canada (0 DINs).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the product label/warnings and contraindications before any S1 safety assessment
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to formally support the mechanistic rationale
- Run a direct literature/trial search specifically on the term "vulvovaginitis" to confirm the vulvitis-node extrapolation is valid, rather than relying on the adjacent node
- Determine a Canada regulatory pathway (e.g., new DIN submission or special access) given the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

