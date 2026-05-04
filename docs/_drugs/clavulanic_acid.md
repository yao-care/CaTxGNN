---
layout: default
title: Clavulanic Acid
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Clavulanic Acid
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

# Clavulanic Acid: From Beta-Lactamase Inhibition to Urogenital Infections

> **Research Use Only.** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.

---

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor — always used in fixed-dose combination with amoxicillin (Augmentin) — that has no standalone approved indication but is clinically valued for overcoming bacterial penicillin resistance. This multi-indication TxGNN analysis (10 predictions) identifies **gonococcal urethritis** and **uterine inflammatory disease** as the most evidence-supported candidates, with **14 publications** (including historical RCTs) and one clinical practice guideline respectively. However, the top-ranked prediction (Ureaplasma urethritis) is mechanistically implausible, and the majority of predictions (7 of 10) are assessed as high-confidence false positives driven by knowledge graph topology rather than true pharmacological relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No standalone registered indication (functions exclusively as a beta-lactamase inhibitor in amoxicillin-clavulanate combinations) |
| Top Ranked Prediction (TxGNN) | Ureaplasma urethritis *(assessed as false positive — see note below)* |
| Best-Evidence Prediction | Gonococcal Urethritis (Rank 2 by TxGNN, strongest clinical evidence) |
| TxGNN Prediction Score | 99.93% (Ranks 1 & 2 tied) |
| Evidence Level (Best Candidate) | L3 — Gonococcal Urethritis |
| Taiwan Market Status | ✗ Not Marketed (0 product licenses) |
| Number of Product Licenses | 0 |
| Recommended Decision | **Hold** |

> **Note:** The #1 TxGNN prediction (Ureaplasma urethritis) is identified as a false positive: *Ureaplasma urealyticum* lacks a cell wall and is intrinsically resistant to all beta-lactam antibiotics. The high prediction score reflects knowledge graph node proximity, not pharmacological validity. The most clinically meaningful prediction is **gonococcal urethritis** (Rank 2).

---

## Why is This Prediction Reasonable?

Clavulanic acid is a naturally occurring beta-lactam compound produced by *Streptomyces clavuligerus*. Rather than killing bacteria directly, it acts as a "suicide inhibitor" of bacterial beta-lactamase enzymes — especially the widely distributed TEM-1 class — by irreversibly binding the enzyme's Ser-70 active site. This protects co-administered amoxicillin from enzymatic degradation and restores its antibacterial activity against otherwise resistant organisms. Clavulanic acid has essentially no intrinsic antibacterial activity on its own; its entire clinical value lies in the combination.

The TxGNN predictions cluster around urogenital infections, which is broadly coherent: multiple urogenital pathogens produce beta-lactamases, and amoxicillin-clavulanate has well-documented activity against them. The mechanistically strongest prediction is **gonococcal urethritis** caused by penicillinase-producing *Neisseria gonorrhoeae* (PPNG). From 1982–1994, multiple clinical trials demonstrated that single-dose oral amoxicillin-clavulanate could overcome PPNG resistance and achieve 85–97% cure rates. **Uterine inflammatory disease** (particularly postpartum endometritis and pelvic inflammatory disease) similarly involves polymicrobial infections rich in beta-lactamase-producing anaerobes (*Bacteroides*, *Prevotella*, *Peptostreptococcus*), and the 2019 French CNGOF/SPILF guidelines explicitly list amoxicillin-clavulanate as a first-line option.

The remaining eight predictions present progressively weaker or absent mechanistic rationale. Three involve non-infectious conditions where antibiotics have no role whatsoever (cystic lymphangioma, celiac trunk compression syndrome, palisaded myofibroblastoma). Two others (urogenital tuberculosis, Ureaplasma urethritis) involve organisms with intrinsic resistance mechanisms that cannot be overcome by clavulanic acid. The model's consistently high scores (~99.8%) for these biologically implausible predictions are a concern and suggest systematic overfitting to local network topology in the TxGNN knowledge graph.

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Evidence Found | Assessment |
|------|---------|-------------|----------------|---------------|------------|
| 1 | Ureaplasma urethritis | 99.93% | L4 | 4 papers (indirect) | **False positive** — cell wall-deficient organism; intrinsically resistant to all beta-lactams |
| 2 | Gonococcal urethritis | 99.93% | L3 | 14 papers (inc. RCTs) | Historically valid; modern resistance limits current relevance |
| 3 | Uterine inflammatory disease | 99.92% | L3 | 7 papers + 1 guideline | Mechanistically sound; French 2019 guideline supports use |
| 4 | Xanthogranulomatous pyelonephritis | 99.90% | L4 | 2 case reports | Surgery is primary treatment; antibiotic role is adjunctive only |
| 5 | Urogenital tuberculosis | 99.89% | L5 | 1 case report (unrelated) | **False positive** — TB requires RIPE regimen; meropenem (not amoxicillin) needed for MDR-TB |
| 6 | Abdominal cystic lymphangioma | 99.80% | L5 | None | **False positive** — congenital lymphatic malformation; no infectious etiology |
| 7 | Celiac trunk compression syndrome | 99.80% | L5 | None | **False positive** — vascular mechanical disease; no infectious etiology |
| 8 | Abdominal ectopic pregnancy | 99.80% | L5 | 1 unrelated trial | **False positive** — surgical/methotrexate treatment; retrieved trial studies hysteroscopy technique |
| 9 | Lymph node palisaded myofibroblastoma | 99.80% | L5 | None | **False positive** — benign mesenchymal tumor; no infectious etiology |
| 10 | Disease of uterine broad ligament | 99.79% | L5 | None | Partial mechanistic rationale for infectious cases only; zero supporting evidence |

---

## Clinical Trial Evidence

No registered clinical trials (ClinicalTrials.gov or ICTRP) were identified for clavulanic acid in any of the 10 predicted indications.

> **Note on NCT04751500:** A clinical trial was retrieved under the "abdominal ectopic pregnancy" query but is entirely unrelated to clavulanic acid. The [HYMMN Trial (NCT04751500)](https://clinicaltrials.gov/study/NCT04751500) is a completed study (n=149) evaluating hysteroscopic surgical technique for management of retained products of conception following miscarriage. It was likely retrieved due to broad obstetric diagnosis code matching and carries no relevance to this drug repurposing analysis.

---

## Literature Evidence

### Gonococcal Urethritis (Rank 2 — Strongest Evidence: 14 publications)

| PMID | Year | Study Type | Journal | Key Findings |
|------|------|------------|---------|-------------|
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | RCT (dose comparison) | Genitourinary Medicine | Single oral dose amoxicillin 3g + clavulanic acid 125mg or 250mg cured 97/100 patients with anogenital gonorrhoea, including 85% of PPNG strains |
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Randomized Comparative Trial | Genitourinary Medicine | Amoxicillin 3g + clavulanic acid 0.25g vs cefuroxime axetil in 500 patients with urogenital/rectal gonorrhoea; both treatments combined with probenecid |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative Trial | British Journal of Venereal Diseases | Oral amoxicillin 3g + clavulanic acid 250mg achieved 90.6% cure vs 73.7% for IM procaine penicillin in 121 men with gonococcal urethritis |
| [3721514](https://pubmed.ncbi.nlm.nih.gov/3721514/) | 1986 | Three-Arm Clinical Trial | Genitourinary Medicine | Three penicillin regimens compared; Augmentin 3.25g + probenecid showed cure rates for both PPNG and non-PPNG strains |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical Trial | British Journal of Venereal Diseases | Two-dose Augmentin regimen achieved 95.9% cure rate vs 87.4% for kanamycin in 192 men with acute gonococcal urethritis; equally effective against PPNG |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Clinical Trial | African Journal of Medicine | Augmentin (amoxicillin 3g + clavulanic acid 125mg) studied in Nigeria where PPNG constitutes ~80% of strains |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Single-Arm Clinical Trial | Medical Journal of Malaysia | Single-dose oral amoxicillin + clavulanic acid for gonococcal urethritis in males; early clinical validation |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical Review | Sexually Transmitted Diseases | Comparative analysis of antibiotic options for PPNG-caused anogenital infections; clavulanic acid + amoxicillin listed alongside spectinomycin and ceftriaxone |
| [7958383](https://pubmed.ncbi.nlm.nih.gov/7958383/) | 1994 | Open Study | Journal of International Medical Research | Procaine penicillin G + clavulanate-potentiated amoxicillin + probenecid: near-complete symptom resolution in 55 acute gonorrhoea patients; 92.5% of isolates were penicillinase-producing |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Revista Española de Quimioterapia | Assessment of best empirical urethritis treatments; includes historical context of amoxicillin-clavulanate |

### Uterine Inflammatory Disease (Rank 3 — 7 publications; selected key items)

| PMID | Year | Study Type | Journal | Key Findings |
|------|------|------------|---------|-------------|
| [30890463](https://pubmed.ncbi.nlm.nih.gov/30890463/) | 2019 | Clinical Practice Guideline | Gynécologie Obstétrique Fertilité | **French CNGOF/SPILF guidelines**: amoxicillin-clavulanate listed as first-line antibiotic option for postpartum endometritis; cesarean delivery is primary risk factor |
| [7811001](https://pubmed.ncbi.nlm.nih.gov/7811001/) | 1994 | Animal Study (mouse) | Antimicrobial Agents and Chemotherapy | Murine model of *Chlamydia trachomatis* genital infection: amoxicillin-clavulanic acid tested but less effective than tetracyclines; upper tract infection (pyosalpinx, hydrosalpinx) observed at 28–70 days |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Narrative Review | European Journal of Translational Myology | Antibiotic use in pregnancy; amoxicillin-clavulanate discussed for odontogenic infections — provides context on safety considerations in pregnant patients |
| [7857230](https://pubmed.ncbi.nlm.nih.gov/7857230/) | 1995 | Case Report | Australian and New Zealand Journal of Surgery | Chest wall actinomycosis associated with IUD use; prolonged amoxicillin/clavulanic acid course used after surgical drainage and IUD removal |

---

## Taiwan Market Information

Clavulanic acid is **not independently registered in Taiwan** (0 product licenses, market status: not marketed). As a compound with no standalone antibacterial activity, clavulanic acid is commercially available only as a fixed-dose combination product — most commonly **amoxicillin/clavulanate potassium (Augmentin)**. Any repurposing feasibility assessment or clinical pathway planning should be conducted for the **combination product**, not clavulanic acid alone. The absence of standalone registration is expected and does not reflect a regulatory obstacle specific to clavulanic acid.

---

## Safety Considerations

No warnings, contraindications, or drug interaction data are available in the current evidence pack for clavulanic acid.

Based on established knowledge of amoxicillin-clavulanate combination products, the following consideration is particularly relevant to the predicted indications:

- **Neonatal necrotizing enterocolitis (NEC) risk**: The ORACLE trial demonstrated that amoxicillin-clavulanate use in preterm premature rupture of membranes is associated with a significantly increased risk of neonatal NEC. This is critically important when evaluating the uterine inflammatory disease prediction, where pregnant or peripartum patients may be involved.

Please refer to the complete package insert for Augmentin or equivalent amoxicillin-clavulanate products for full warnings, contraindications, and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The majority of TxGNN predictions for clavulanic acid are false positives rooted in knowledge graph topology rather than pharmacological reality (7 of 10 predictions involve either non-infectious diseases or organisms with intrinsic resistance to beta-lactams). The two predictions with meaningful evidence — gonococcal urethritis (historical RCTs, now superseded by ceftriaxone IM per WHO/CDC guidelines) and uterine inflammatory disease (French 2019 guideline support) — do not currently justify immediate repurposing investment without further evidence development.

**To proceed, the following is needed:**

- **Reframe the analysis unit**: All evidence and any future research should focus on the **amoxicillin-clavulanate combination product (Augmentin)**, not clavulanic acid as a standalone drug
- **Gonococcal urethritis pathway**: Conduct a systematic review of modern *N. gonorrhoeae* antimicrobial susceptibility data in Taiwan/Asia to determine whether amoxicillin-clavulanate retains any clinical activity given resistance evolution since the 1980s
- **Uterine inflammatory disease pathway**: Commission a systematic review comparing contemporary outcomes of amoxicillin-clavulanate vs. standard-of-care regimens (clindamycin + gentamicin) for postpartum endometritis and PID, with explicit evaluation of NEC risk in peripartum populations
- **Taiwan market assessment**: Identify all registered amoxicillin-clavulanate combination products (Augmentin and generics) in the Taiwan NHI formulary, including approved indications and reimbursement status
- **Safety data**: Obtain and parse Taiwan FDA package inserts for amoxicillin-clavulanate combination products for a complete contraindication/DDI profile
- **TxGNN model quality improvement**: Apply a pre-filter to exclude organisms with intrinsic beta-lactam resistance (Ureaplasma, Mycobacterium, etc.) before scoring to reduce false positive burden in future runs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

