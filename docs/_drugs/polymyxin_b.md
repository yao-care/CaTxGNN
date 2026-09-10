---
layout: default
title: Polymyxin B
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 3
---

# Polymyxin B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Polymyxin B: From Antibacterial Agent to Three Candidate Indications — Conjunctivitis, Bronchitis, and Laryngotracheitis

## One-Sentence Summary

Polymyxin B is a polymyxin-class antibacterial agent; TFDA records show it currently holds **no marketing authorization in Taiwan** (未上市), so no approved local indication is on file. TxGNN predicts three new indications — **Conjunctivitis**, **Bronchitis**, and **Laryngotracheitis** — but the evidence backing them differs sharply: conjunctivitis is supported by **3 clinical trials and 20 publications (including 4 Tier-1 RCTs)**, bronchitis by **14 publications and no trials**, and laryngotracheitis by **no trials or literature at all** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not marketed in Taiwan) |
| Taiwan (TFDA) Market Status | ✗ Not Marketed (未上市) |
| Number of Marketing Authorizations | 0 |
| Candidate 1 — Conjunctivitis | TxGNN 99.06% · Evidence Level **L1** · Decision Stage S3 · **Proceed with Guardrails** |
| Candidate 2 — Bronchitis | TxGNN 99.87% · Evidence Level **L4** · Decision Stage S1 · **Hold** |
| Candidate 3 — Laryngotracheitis | TxGNN 99.62% · Evidence Level **L5** · Decision Stage S0 · **Hold** |
| Overall Recommended Decision | Proceed with Guardrails (conjunctivitis only); Hold on bronchitis and laryngotracheitis |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record (flagged as a High-severity data gap, DG002). Based on well-established pharmacology captured in the evidence base itself: Polymyxin B is a cyclic lipopeptide antibiotic that binds lipopolysaccharide (LPS/Lipid A) in the outer membrane of Gram-negative bacteria, disrupting membrane integrity and causing bactericidal cell death. This activity is the common thread linking the drug to all three candidate indications below, though the strength of supporting evidence — and even the direction of the safety signal — differs considerably between them.

**Conjunctivitis** — This is mechanistically the most mature candidate. Topical (ophthalmic) Polymyxin B, typically combined with Trimethoprim (e.g., Polytrim) or Neomycin/Gramicidin, is already an established treatment for bacterial conjunctivitis worldwide, targeting the Gram-negative and mixed flora (*H. influenzae*, *S. pneumoniae*) that commonly cause the disease. In Taiwan this would represent a "locally not yet marketed but internationally well-precedented" use rather than a genuinely novel mechanism.

**Bronchitis** — The rationale is more conflicted. Some literature supports inhaled/systemic Polymyxin B as salvage therapy for tracheobronchitis and ventilator-associated pneumonia caused by *Pseudomonas aeruginosa* or *Acinetobacter baumannii*. However, a separate and substantial body of literature shows that inhaled Polymyxin B itself provokes bronchoconstriction and is used experimentally as a bronchial-hyperresponsiveness challenge agent — including an explicit case report titled "Danger of polymyxin B inhalation." The therapeutic rationale and the irritant/spasmogenic risk profile point in opposite directions, so the safety window needs clarification before this indication can advance.

**Laryngotracheitis** — No clinical trials or literature evidence exist for this indication; the prediction rests entirely on TxGNN's knowledge-graph score. It is a plausible mechanistic extrapolation (if the causative organism is Gram-negative) but currently has no epidemiological or clinical corroboration.

## Clinical Trial Evidence

### Conjunctivitis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Completed | 124 | Head-to-head comparison of Polytrim (Polymyxin B/Trimethoprim) vs. Moxifloxacin ophthalmic solution for pediatric conjunctivitis; direct efficacy evidence |
| [NCT01227863](https://clinicaltrials.gov/study/NCT01227863) | Phase 3 | Unknown | 70 | Compared two dexamethasone+neomycin+polymyxin B combination products for acute bacterial conjunctivitis; effect attributable to Polymyxin B alone is unclear |
| [NCT01809483](https://clinicaltrials.gov/study/NCT01809483) | Phase 3 | Completed | 32 | Bandage contact lens vs. pressure patching for corneal erosion; indirect relevance, does not directly test Polymyxin B |

### Bronchitis

Currently no related clinical trials registered

### Laryngotracheitis

Currently no related clinical trials registered

## Literature Evidence

### Conjunctivitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043943](https://pubmed.ncbi.nlm.nih.gov/19043943/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Moxifloxacin vs. Polymyxin B/Trimethoprim in pediatric bacterial conjunctivitis |
| [23092529](https://pubmed.ncbi.nlm.nih.gov/23092529/) | 2013 | RCT | J Pediatr | Single-blind RCT comparing Polymyxin B-Trimethoprim vs. Moxifloxacin for acute conjunctivitis in children |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Multicenter comparison of speed of clinical efficacy: Polymyxin B/Trimethoprim vs. Moxifloxacin |
| [2540136](https://pubmed.ncbi.nlm.nih.gov/2540136/) | 1989 | RCT | J Antimicrob Chemother | Pooled review of 4 RCTs (528 patients): Trimethoprim-Polymyxin B vs. Chloramphenicol ophthalmic ointment |
| [2370842](https://pubmed.ncbi.nlm.nih.gov/2370842/) | 1990 | Review | Med Lett Drugs Ther | Review of Trimethoprim-Polymyxin B for bacterial conjunctivitis |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Cohort | Clin Ther | Survey of children with acute bacterial conjunctivitis treated with Trimethoprim-Polymyxin B |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | Cohort | J Antimicrob Chemother | 230-patient multicentre trial: Trimethoprim-Polymyxin B vs. Neomycin-Polymyxin B-Gramicidin vs. Chloramphenicol |
| [2850891](https://pubmed.ncbi.nlm.nih.gov/2850891/) | 1988 | Cohort | Curr Med Res Opin | Double-blind study: Trimethoprim-Polymyxin B ointment vs. Chloramphenicol ointment, 42 patients |
| [31535057](https://pubmed.ncbi.nlm.nih.gov/31535057/) | 2019 | Case Report | Am J Ophthalmol Case Rep | Case of dupilumab-associated blepharoconjunctivitis (background/differential relevance) |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | Case Report | Clin Microbiol Infect | Case of primary meningococcal conjunctivitis treated with topical polymyxin B/neomycin/gramicidin |

### Bronchitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Review | Infection | Compares Polymyxin B with other antimicrobials for VAP/tracheobronchitis caused by *P. aeruginosa* or *A. baumannii* |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Cohort | Diagn Microbiol Infect Dis | Inhaled polymyxin B as salvage therapy for pneumonia/tracheobronchitis from multidrug-resistant Gram-negative bacilli (19 patients) |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Cohort | Lung | Bronchial reactivity to inhaled polymyxin B in asthma and chronic obstructive bronchitis (used as a bronchoprovocation agent) |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Case Report | Chest | Endobronchial Polymyxin B experimental observations in chronic bronchitis |
| [8054833](https://pubmed.ncbi.nlm.nih.gov/8054833/) | 1994 | Cohort | Clin Auton Res | Guinea-pig eosinophilic bronchitis model induced by intranasal polymyxin B; used to study cough mechanisms |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Case Report | J Kansas Med Soc | Pseudomonas tracheobronchitis treated with systemic gentamicin and polymyxin B aerosol |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Cohort | Orvosi Hetilap | Polymyxin B sulfate-induced non-specific bronchial provocation in asthma and chronic bronchitis |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Case Report | Ann Intern Med | "Danger of polymyxin B inhalation" — adverse respiratory reaction case report |
| [28441858](https://pubmed.ncbi.nlm.nih.gov/28441858/) | 2017 | Review | Zhonghua Yi Xue Za Zhi | Eosinophilic bronchitis mouse model; effects of eosinophil activation on airway hyperresponsiveness |
| [7402949](https://pubmed.ncbi.nlm.nih.gov/7402949/) | 1980 | Cohort | Pneumonol Pol | Exercise-induced bronchospasm vs. histamine/polymyxin B provocation test in asthma and chronic obstructive bronchitis |

### Laryngotracheitis

Currently no related literature available

## Taiwan Market Information

Polymyxin B currently holds **zero marketing authorizations** in Taiwan (market status: 未上市 / Not Marketed). No license records, product names, dosage forms, or approved-indication text are available.

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is currently available for this record — this is flagged as a **Blocking** data gap (DG001) that prevents the compound from advancing past initial safety screening (S1).

**Literature-derived caution (not from official labeling):** Several publications indicate that inhaled/intranasal Polymyxin B can itself provoke bronchoconstriction and non-specific bronchial hyperreactivity, and it has been used experimentally as a bronchoprovocation challenge agent. One case report is titled "Danger of polymyxin B inhalation." This is directly relevant to the bronchitis candidate and should be weighed against any therapeutic use by the inhaled/endobronchial route.

Please refer to the official product label/monograph once available for comprehensive safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Conjunctivitis) / Hold (Bronchitis, Laryngotracheitis)**

**Rationale:**
- **Conjunctivitis** has L1-level evidence (multiple completed trials, 4 Tier-1 RCTs, and decades of real-world precedent for topical Polymyxin B/Trimethoprim), so it can advance under guardrails.
- **Bronchitis** has only preclinical/mechanistic evidence (L4) and a direct safety contradiction (therapeutic use vs. documented bronchospasm/irritant risk from inhalation), so it should be held pending safety clarification.
- **Laryngotracheitis** has no clinical or literature support (L5, model prediction only) and cannot proceed past initial screening.

**To proceed, the following is needed:**
- TFDA product label / package insert data (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- For bronchitis: dedicated evaluation of inhalation-route safety (bronchospasm/irritant risk) before any therapeutic use is considered
- For laryngotracheitis: primary literature or trial data to move beyond a pure model prediction
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

