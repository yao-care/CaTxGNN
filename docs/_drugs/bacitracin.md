---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

# Bacitracin: From Bacterial Skin Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic traditionally used as a topical agent against gram-positive bacterial skin and wound infections. The TxGNN model ranks **Punctate Epithelial Keratoconjunctivitis** as its top repurposing candidate (Score: ~100%), yet **no supporting clinical trials or publications** were identified for this indication. Notably, **Otitis Externa** (Rank 4) emerges as the most evidence-supported prediction among the 10 analyzed, backed by 6 publications including one double-blind comparative clinical study.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical antibacterial use for minor bacterial skin and wound infections |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | ~99.9999% (Score: 0.9999919) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Bacitracin is a cyclic polypeptide antibiotic produced by *Bacillus subtilis* that inhibits bacterial cell wall synthesis. It does so by blocking the dephosphorylation of undecaprenyl pyrophosphate, a lipid carrier required to shuttle peptidoglycan precursors across the bacterial membrane. This mechanism confers activity predominantly against gram-positive organisms — particularly *Staphylococcus aureus* and *Streptococcus* species — which are common pathogens in superficial infections of skin, wounds, and mucosal surfaces.

The prediction for punctate epithelial keratoconjunctivitis (PEK) appears to leverage bacitracin's established ophthalmic use: in several markets outside Canada, bacitracin ophthalmic ointments are approved for bacterial conjunctivitis. The ocular surface is accessible to topical application, and high local concentrations can be achieved without meaningful systemic absorption, thereby circumventing the nephrotoxicity that makes systemic bacitracin use prohibitive.

However, the mechanistic match for PEK is indirect at best. Punctate epithelial keratoconjunctivitis is most commonly driven by adenoviral infection or severe dry eye disease — neither of which is a bacterial target. Bacitracin's mode of action does not address viral replication or tear film dysfunction. The high TxGNN score likely reflects graph-topology proximity (ocular surface disease → ophthalmic antibiotic agent) rather than a direct pathophysiological connection, and no clinical or preclinical studies were found to substantiate this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Notable Alternative Prediction: Otitis Externa (Rank 4)

Among all 10 predicted indications, **Otitis Externa** carries the highest evidence density and the most coherent mechanistic rationale. Bacitracin-containing combination ointments (most notably **Nebacetin** = bacitracin + neomycin) have a long history of clinical use in external ear canal infections. Otitis externa is frequently caused by *Staphylococcus aureus* (gram-positive, bacitracin-sensitive) and *Pseudomonas aeruginosa* (gram-negative, covered by the neomycin component), making combination formulations mechanistically well-matched. Topical delivery achieves high local concentrations in the ear canal while avoiding systemic nephrotoxicity.

**Evidence Level for Otitis Externa: L4 | Recommendation: Research Question**

### Literature Evidence for Otitis Externa

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Clinical Comparative Study | Eur Arch Otorhinolaryngol | Double-blind RCT (n=151): polymyxin-B/bacitracin ointment vs. same plus hydrocortisone acetate in acute otitis externa; evaluates contribution of steroid component |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Case Series / Historical Report | Z Laryngol Rhinol Otol | Local treatment of inflammatory and secretory ear conditions with Nebacetin (bacitracin + neomycin) styli |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Clinical Review | Maryland State Med J | Practical treatment of otitis externa including antibiotic ointment use |
| [4306877](https://pubmed.ncbi.nlm.nih.gov/4306877/) | 1969 | Expert Review | Z Arztl Fortbild | Antibiotic use in otologic practice, including bacitracin-containing formulations |
| [165871](https://pubmed.ncbi.nlm.nih.gov/165871/) | 1975 | Clinical Study | Can Med Assoc J | Antibiotic selection for external otitis in Canadian clinical context |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | In Vitro / Veterinary | J Vet Med Ser B | Antibiotic susceptibility testing of 46 bacterial strains from chronic otitis externa; documents resistance trends relevant to antibiotic selection |

---

## Canada Market Information

Bacitracin currently has **no DIN-registered products in Canada** (0 active licenses). No standalone or combination products (e.g., bacitracin + polymyxin B; bacitracin + neomycin) were identified in the Canadian regulatory database. Combination topical antibiotics containing bacitracin are available in other markets (US, Europe, Japan) as OTC preparations, ophthalmic ointments, and otic formulations, but none appear to hold a Canadian DIN at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Systemic administration of bacitracin carries significant nephrotoxicity risk and is generally avoided. Topical and ophthalmic formulations are considered safer due to minimal systemic absorption. Contact sensitization has been reported with repeated topical use, a factor relevant to long-term or prophylactic applications.

---

## Conclusion and Next Steps

### Primary Prediction (Punctate Epithelial Keratoconjunctivitis)

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction scores exceptionally high but is unsupported by any clinical trial or published literature. Punctate epithelial keratoconjunctivitis is predominantly viral or dry-eye in origin, making bacitracin's antibacterial mechanism only tangentially relevant. There is insufficient scientific basis to advance this indication.

---

### Most Promising Alternative (Otitis Externa — Rank 4)

**Decision: Research Question**

**Rationale:**
Otitis externa has a plausible mechanistic foundation and historical clinical use for bacitracin-containing formulations, anchored by at least one double-blind comparative clinical study. However, the existing evidence is largely dated (1960s–2007) and does not meet modern Phase 2/3 RCT standards. The absence of a currently marketed Canadian product also means a regulatory development pathway would need to be defined.

**To advance the otitis externa evaluation, the following is needed:**

- **Full-text review** of PMID 17503066 (the most contemporary clinical comparative study) to assess efficacy endpoints and safety profile
- **Guideline benchmarking**: Compare bacitracin/neomycin combinations against current first-line agents for otitis externa (e.g., ciprofloxacin/dexamethasone otic drops) to assess competitive positioning
- **Formulation assessment**: Determine whether an existing otic formulation can be adapted for Canadian registration or whether novel development is required
- **MOA data completion**: Retrieve full mechanism-of-action and pharmacokinetic data from DrugBank (DB00626) to strengthen the mechanistic narrative
- **Safety package**: Obtain TFDA/Health Canada package insert warnings and contraindications to complete the safety evaluation and enable S1 safety screening
- **Regulatory pathway consultation**: Explore whether the combination product (bacitracin + neomycin/polymyxin B) qualifies for an abbreviated NDS pathway given existing approvals in comparable jurisdictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

