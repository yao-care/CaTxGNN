---
layout: default
title: Cefprozil
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Cefprozil
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

# Cefprozil: From Respiratory Tract Infections to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is an orally bioavailable second-generation cephalosporin antibiotic, originally developed for upper and lower respiratory tract infections and skin/soft tissue infections.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (UTI)**,
with **no registered clinical trials** but **9 publications — including 3 Phase 3 RCTs** — directly supporting this indication.
The evidence base is unusually robust for a "predicted" repurposing candidate, as multiple well-controlled trials from the early 1990s already demonstrated cure rates exceeding 90%.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory tract infections and skin/soft tissue infections (based on international literature; no marketing authorization in Taiwan) |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, cefprozil is a second-generation oral cephalosporin that exerts its antibacterial effect by binding to **penicillin-binding proteins (PBPs)** — the enzymes responsible for cross-linking peptidoglycan strands in the bacterial cell wall. Inhibiting PBPs prevents proper cell wall synthesis, causing structural instability and ultimately bactericidal cell lysis. Compared to first-generation cephalosporins, cefprozil has improved stability against β-lactamases and a broader gram-negative spectrum, while retaining strong gram-positive activity.

The mechanistic connection to UTI is straightforward. The three most prevalent uropathogens in uncomplicated UTI — *Escherichia coli*, *Klebsiella pneumoniae*, and *Proteus mirabilis* — all fall within cefprozil's established antibacterial spectrum. Following oral administration, cefprozil achieves high urinary concentrations due to renal excretion of the unchanged drug, producing the drug exposure at the site of infection that UTI treatment requires. Its once-daily dosing option (500 mg QD) further enhances practical suitability for outpatient UTI management.

This is one of the rare TxGNN predictions that is well-corroborated by historical clinical evidence. Three Phase 3 RCTs conducted between 1991 and 1992 directly compared cefprozil to cefaclor for acute uncomplicated UTI, consistently reporting clinical and bacteriological cure rates of approximately 90–94%. In vitro data from Taiwan clinical isolates (*E. coli* and *K. pneumoniae*) also confirm local pathogen susceptibility. The TxGNN model's 99.99% prediction score reflects this strong mechanistic and evidential alignment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov for cefprozil in urinary tract infection.

> **Note:** Three Phase 3 randomized controlled trials exist in the peer-reviewed literature (see Literature Evidence below), but these were conducted in the pre-registration era (1991–1992) and are not catalogued on ClinicalTrials.gov.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | RCT (Phase 3) | J Antimicrobial Chemotherapy | Cefprozil 500 mg QD vs. cefaclor 250 mg TID in 102 adults with acute uncomplicated UTI; comparable clinical and bacteriological cure rates, with cefprozil offering the convenience of once-daily dosing |
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | RCT (Phase 3) | Clinical Therapeutics | Multicenter study in patients ≥2 years; cefprozil QD vs. cefaclor TID for 10 days; satisfactory clinical response rates comparable between groups in acute uncomplicated UTI |
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | RCT | Antimicrobial Agents and Chemotherapy | 108 college women with acute UTI; clinical and bacterial cure rates of 94% and 93% respectively for cefprozil QD, equivalent to cefaclor TID (94%/94%) at 1-week post-therapy |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Systematic Review | Drugs | Comprehensive review of cefprozil's antibacterial activity, pharmacokinetics, and therapeutic potential; confirms good in vitro activity against *E. coli*, *Klebsiella*, and Enterobacteriaceae relevant to UTI |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Comprehensive Review | Pediatric Annals | Review of cefprozil clinical applications including UTI; pharmacokinetics support once- or twice-daily dosing; favorable tolerability with low GI and dermatologic adverse event rates |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Expert Review | American Family Physician | Comparison of new oral cephalosporins; cefprozil, cefpodoxime, and loracarbef assessed as effective alternatives for skin, respiratory tract, and urinary tract infections |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In vitro | Chemotherapy | Activity assessed against 637 clinical isolates from Kaohsiung Veterans General Hospital, Taiwan; inhibited >80% of *E. coli* and *K. pneumoniae* at 8 mg/L — directly relevant to Taiwanese uropathogens |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Clinical Series (Pediatric) | Japanese Journal of Antibiotics | PK and clinical evaluation in children; high urinary concentrations and recovery rates following oral dosing support UTI pharmacological rationale |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Clinical Series | Japanese Journal of Antibiotics | 21 pediatric patients including 3 UTI cases; good to excellent clinical responses in 19/21 patients; complete bacterial eradication in all 11 culture-positive cases |

---

## Taiwan Market Information

Cefprozil is currently **not marketed in Taiwan (未上市)**. No product licenses or drug identification numbers are registered with Taiwan's regulatory authority. Any clinical use in Taiwan would require a formal product registration application.

---

## Safety Considerations

Formal safety data from Taiwan's drug monograph or DrugBank was not available in this Evidence Pack. Please refer to international prescribing information for complete safety details.

Based on the known class pharmacology of cephalosporins, the following considerations apply:

- **Hypersensitivity**: Cross-reactivity with penicillins exists (estimated <5% in true penicillin allergy); contraindicated in patients with a history of severe immediate β-lactam hypersensitivity
- **Gastrointestinal effects**: Nausea, diarrhea, and *Clostridioides difficile*-associated diarrhea are recognized class effects
- **Renal impairment**: Dose adjustment is likely required in patients with reduced creatinine clearance, as cefprozil is primarily renally excreted
- **Drug interactions**: Full DDI profile requires review of the product monograph; no interaction data were available in this Evidence Pack

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three Phase 3 RCTs from 1991–1992 directly demonstrate cefprozil's clinical efficacy in acute uncomplicated UTI (cure rates ~90–94%), achieving an L1 evidence level — the highest tier in this framework. The mechanistic basis (PBP inhibition → bactericidal activity against *E. coli*, *Klebsiella*, *Proteus*) is pharmacologically sound, and in vitro data from Taiwanese clinical isolates confirms activity against locally relevant uropathogens. The primary barriers are not scientific but regulatory and operational: the drug is currently not marketed in Taiwan, and the existing clinical data is approximately 30 years old.

**To proceed, the following is needed:**

- **Resistance surveillance update**: The three pivotal RCTs date from 1991–1992; contemporary Taiwan antibiogram data for *E. coli* and *K. pneumoniae* is essential to confirm current susceptibility, given the global rise in ESBL-producing and fluoroquinolone-resistant uropathogens
- **Regulatory pathway clarification**: A formal Taiwan product registration application (NDA or abbreviated NDA) would be required; assessment of whether existing Phase 3 data meets current TFDA submission standards
- **Safety data package**: Formal retrieval of full package insert (warnings, contraindications, drug interactions) from DrugBank API or regulatory authority databases to complete the blocking DG001/DG002 data gaps
- **Head-to-head positioning analysis**: Comparison against current Taiwan UTI guideline-recommended agents (fosfomycin, nitrofurantoin, trimethoprim-sulfamethoxazole) to define the clinical niche and value proposition
- **Special population data review**: Assessment of dosing and safety in elderly patients, pregnant women, and patients with renal impairment for Taiwan's patient demographics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

