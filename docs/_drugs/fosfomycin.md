---
layout: default
title: Fosfomycin
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
---

# Fosfomycin
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

# Fosfomycin: From Uncomplicated Urinary Tract Infection to Pyelitis

## One-Sentence Summary

Fosfomycin is a broad-spectrum bactericidal antibiotic with a well-established role in treating uncomplicated lower urinary tract infections, acting through irreversible inhibition of the MurA enzyme to block bacterial cell wall synthesis. Among 10 TxGNN-predicted new indications, **pyelitis (upper urinary tract infection / acute pyelonephritis)** is the most clinically actionable candidate, supported by a **completed Phase 3 RCT (ZEUS trial)** and **a 2025 systematic review with network meta-analysis**. The drug is currently not marketed in Canada, meaning any clinical access requires the Health Canada Special Access Programme.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uncomplicated urinary tract infection (cystitis) |
| Featured Predicted Indication | Pyelitis / Acute Pyelonephritis |
| TxGNN Prediction Score | 99.37% (Rank #10 among 10 predictions) |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN Ranking:** The highest-scored TxGNN prediction (Ureaplasma urethritis, Rank #1, 99.99%) has a fundamental mechanistic barrier — *Ureaplasma urealyticum* is a cell wall-deficient organism, making fosfomycin's MurA-targeting mechanism entirely ineffective. Similarly, Rank #6 (urogenital tuberculosis) has no biological plausibility — *Mycobacterium tuberculosis* is intrinsically resistant to fosfomycin. The most clinically actionable prediction is pyelitis (Rank #10), which carries the highest evidence level (L1).

---

## Why is This Prediction Reasonable?

Fosfomycin is an epoxide antibiotic that irreversibly inactivates MurA (UDP-N-acetylglucosamine-3-enolpyruvyltransferase), the enzyme catalyzing the first committed step of bacterial peptidoglycan biosynthesis. This mechanism is entirely distinct from β-lactams, fluoroquinolones, and aminoglycosides, which explains its retained potency against multidrug-resistant organisms including ESBL-producing *E. coli*, carbapenem-resistant *Enterobacteriaceae*, and vancomycin-resistant *Enterococcus*. Against the major uropathogens — *E. coli*, *Klebsiella pneumoniae*, *Proteus mirabilis*, and *Enterococcus faecalis* — fosfomycin maintains favorable MIC distributions with low cross-resistance rates.

Pyelitis and acute pyelonephritis are upper urinary tract infections sharing the same causative pathogens as uncomplicated cystitis, predominantly *E. coli* (60–80% of cases). The step from lower to upper tract treatment is pharmacokinetically well-supported: approximately 90% of absorbed fosfomycin is excreted unchanged in urine, achieving concentrations exceeding 1,000 μg/mL — far above the MIC₉₀ for common uropathogens. Intravenous fosfomycin disodium additionally achieves therapeutic concentrations in renal parenchymal tissue, which is essential for upper tract infections. These pharmacokinetic properties create a direct mechanistic bridge from uncomplicated cystitis to pyelitis.

The Phase 3 ZEUS trial directly compared IV fosfomycin (ZTI-01) with piperacillin-tazobactam in patients with complicated UTI including acute pyelonephritis and demonstrated non-inferiority in clinical cure rates. A 2025 systematic review and network meta-analysis further confirmed this efficacy across comparators. The clinical significance of fosfomycin's preserved activity against ESBL-producing organisms — increasingly responsible for hospital-acquired and community-onset pyelonephritis — makes this prediction particularly timely in the context of antimicrobial stewardship.

---

## Clinical Trial Evidence

No clinical trials specifically targeting pyelitis are registered in ClinicalTrials.gov in the current evidence pack. The pivotal Phase 3 RCT evidence (ZEUS trial) exists as published literature — see the Literature Evidence section below for full details.

The only ClinicalTrials.gov entries retrieved across all 10 predicted indications were two broad pediatric PK/PD safety studies (NCT04278404, NCT01431326) identified under "uterine inflammatory disease." Both studies enrolled thousands of children to characterize general pharmacokinetics of understudied drugs — neither was designed to evaluate fosfomycin efficacy for any specific indication in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | Phase 3 RCT | Clin Infect Dis | ZEUS trial: IV fosfomycin (ZTI-01) non-inferior to piperacillin-tazobactam for complicated UTI including acute pyelonephritis |
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT | Clin Microbiol Infect | Fosfomycin trometamol (3g × 3 doses) effective for uncomplicated gonococcal urethritis in men (N=126); directly validates Rank #2 prediction |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic Review / NMA | J Comp Effectiveness Research | Fosfomycin confirmed efficacious for cUTI/acute pyelonephritis vs. carbapenems and other agents in network meta-analysis |
| [33819054](https://pubmed.ncbi.nlm.nih.gov/33819054/) | 2021 | Clinical Guidelines | Ann Intern Med | ACP best practices recommend short-course antibiotics for UTIs; fosfomycin endorsed as first-line for uncomplicated cystitis |
| [36031053](https://pubmed.ncbi.nlm.nih.gov/36031053/) | 2023 | Review | Clin Microbiol Infect | Fosfomycin recommended for UTI in pregnancy including upper tract infections; international guideline summary |
| [32303061](https://pubmed.ncbi.nlm.nih.gov/32303061/) | 2020 | Retrospective Cohort | J Antimicrob Chemother | Real-world oral fosfomycin use for pyelonephritis and cUTI over 1 year in a large municipal system; limited data but used clinically |
| [35141335](https://pubmed.ncbi.nlm.nih.gov/35141335/) | 2022 | Cohort Study | BioMed Res Int | Fosfomycin therapeutic efficacy validated in ESBL-producing E. coli acute pyelonephritis mouse model |
| [31494827](https://pubmed.ncbi.nlm.nih.gov/31494827/) | 2019 | Systematic Review (PK/PD) | Eur J Clin Microbiol Infect Dis | PK/PD target attainment analysis for oral antibiotics in pyelonephritis; fosfomycin assessed for resistant E. coli |
| [31160291](https://pubmed.ncbi.nlm.nih.gov/31160291/) | 2019 | Preclinical Study | Antimicrob Agents Chemother | Oral fosfomycin shows unexpected activity against resistant E. coli strains (MIC up to 256 μg/mL) in murine pyelonephritis model |
| [31608743](https://pubmed.ncbi.nlm.nih.gov/31608743/) | 2020 | Narrative Review | Postgraduate Medicine | Fosfomycin 3g single dose listed as first-line for uncomplicated cystitis; discussed as rescue option for MDR uropathogens |

---

## Canada Market Information

Fosfomycin is not currently marketed in Canada and holds no approved Drug Identification Numbers (DINs) with Health Canada.

> Fosfomycin is commercially available in other jurisdictions: IV formulation (fosfomycin disodium/ZTI-01, marketed as **CONTEPO®**) is approved in the United States for cUTI; oral formulation (fosfomycin trometamol 3g sachets) is widely available in Europe, Japan, and Latin America. Canadian healthcare facilities seeking access would need to apply through **Health Canada's Special Access Programme (SAP)**.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data — including key warnings, contraindications, and drug-drug interactions — was not available in this evidence pack. A formal review of the complete SmPC or package insert is a prerequisite before any clinical application and is listed as a required action in the Next Steps below.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ZEUS Phase 3 RCT demonstrated non-inferiority of IV fosfomycin versus piperacillin-tazobactam for complicated UTI including acute pyelonephritis, and a 2025 systematic review with network meta-analysis independently confirms this efficacy. Fosfomycin's unique mechanism of action, favorable pharmacokinetics (>90% renal excretion, urine concentrations >1,000 μg/mL), and preserved activity against ESBL-producing and MDR uropathogens create a compelling clinical case — especially where standard first-line agents have failed due to resistance. The drug is not marketed in Canada, which is the principal guardrail governing access.

**To proceed, the following is needed:**

- **Regulatory access:** File a Health Canada Special Access Programme (SAP) application specifying the target formulation (IV fosfomycin disodium for hospitalized pyelonephritis, or oral fosfomycin trometamol for outpatient use)
- **Safety review:** Obtain and formally evaluate the complete package insert for contraindications, warnings, and drug interactions — this data is entirely absent from the current evidence pack and is classified as a blocking gap
- **Local susceptibility data:** Confirm fosfomycin MIC distributions and resistance rates for local *E. coli*, *Klebsiella*, and *Proteus* isolates before considering empiric use
- **Formulation and route decision:** Define whether IV (for hospitalized acute pyelonephritis) or oral (for selected outpatient complicated UTI) formulation is the intended use case, as clinical evidence and dosing regimens differ substantially between routes
- **Secondary research question — Gonococcal urethritis:** Rank #2 prediction has RCT-level evidence (PMID 27064136) supporting fosfomycin trometamol for uncomplicated gonococcal urethritis in men — rated **Research Question**. This warrants active monitoring given escalating *N. gonorrhoeae* resistance to fluoroquinolones and extended-spectrum cephalosporins; fosfomycin may represent a viable salvage option if resistance to current first-line agents continues to rise
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

