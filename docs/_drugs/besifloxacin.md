---
layout: default
title: Besifloxacin
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 8
---

# Besifloxacin
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

# Besifloxacin: From Bacterial Conjunctivitis to Bronchitis

## One-Sentence Summary

Besifloxacin (Besivance®) is a fourth-generation fluoroquinolone antibiotic developed exclusively as a topical ophthalmic suspension, used globally for the treatment of bacterial conjunctivitis.
The TxGNN model predicts it may be effective for **Bronchitis** with a prediction score of **99.84%**; however, **no clinical trials or published literature** currently support this specific repurposing direction, and a fundamental formulation barrier — the absence of any systemic or inhalation dosage form — limits clinical translatability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canada/Taiwan authorization; globally indicated for bacterial conjunctivitis (ophthalmic topical use) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Besifloxacin is a fluoroquinolone antibiotic that works by simultaneously inhibiting two bacterial enzymes — DNA gyrase (topoisomerase II) and topoisomerase IV — thereby disrupting DNA replication and causing bacterial cell death. This dual-target mechanism is shared by all fluoroquinolones and is the basis for the class's broad-spectrum antibacterial activity. Systemic fluoroquinolones such as levofloxacin and moxifloxacin are in fact first-line treatments for community-acquired pneumonia and acute exacerbations of chronic bronchitis, and they achieve this by targeting the very same respiratory pathogens — *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — for which besifloxacin also demonstrates strong in vitro susceptibility.

The TxGNN prediction is therefore mechanistically coherent at the class level: the knowledge graph recognizes that besifloxacin shares the fluoroquinolone pharmacophore with established respiratory antibiotics and infers a potential role in bronchitis treatment. The high prediction score (99.84%) reflects this class-effect extrapolation, not drug-specific clinical evidence for besifloxacin in bronchitis.

However, there is a critical and currently insurmountable translational barrier. Besifloxacin exists exclusively as a 0.6% ophthalmic suspension. Pharmacokinetic data from NCT00407589 confirms that systemic plasma exposure following topical ocular instillation is negligible. Treating bronchitis requires drug concentrations at the bronchial mucosa that can only be achieved through systemic (oral/IV) or inhalation administration — neither of which currently exists for besifloxacin. The prediction should therefore be read as a signal about the fluoroquinolone class rather than a clinical action item for this specific molecule.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for besifloxacin in bronchitis.

> **Context note:** Six completed clinical trials exist for besifloxacin in the adjacent category of **post-bacterial disorder** (all in the ophthalmic domain — bacterial conjunctivitis and pre-surgical prophylaxis). These trials confirm the drug's antibacterial efficacy and safety on mucosal surfaces but do not translate to respiratory applications. Details are available in the rank-3 indication analysis below.

---

## Literature Evidence

Currently no related literature available for besifloxacin in bronchitis.

---

## Canada Market Information

Besifloxacin is **not currently authorized or marketed in Canada**. No Drug Identification Numbers (DINs) are registered with Health Canada, and no approved indications exist in the Canadian drug registry.

For international reference: besifloxacin is marketed in the United States as **Besivance® 0.6% Ophthalmic Suspension** (Bausch & Lomb/Bausch Health), approved by the FDA for treatment of bacterial conjunctivitis caused by susceptible bacteria including *CDC coryneform group G*, *Corynebacterium pseudodiphtheriticum*, *Haemophilus influenzae*, *Moraxella lacunata*, *Staphylococcus aureus*, *Staphylococcus epidermidis*, *Staphylococcus hominis*, *Staphylococcus lugdunensis*, *Streptococcus mitis group*, *Streptococcus oralis*, *Streptococcus pneumoniae*, and *Streptococcus salivarius*.

---

## Additional Indication Analysis: Post-Bacterial Disorder (Rank #3)

Although the top TxGNN prediction is bronchitis (L5, Hold), the **third-ranked prediction — post-bacterial disorder** — carries meaningfully stronger evidence (L4, Research Question) and warrants separate discussion given the six available clinical trials.

### Clinical Trial Evidence for Post-Bacterial Disorder

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01175590](https://clinicaltrials.gov/study/NCT01175590) | Phase 3 | Completed | 518 | Largest besifloxacin safety trial (n=518); established the drug's safety profile and antibacterial efficacy as Besivance vs. vehicle over 7 days TID dosing — the highest-quality evidence base for the drug |
| [NCT04542759](https://clinicaltrials.gov/study/NCT04542759) | Phase 1 | Completed | 60 | Demonstrated topical besifloxacin effectively reduces conjunctival microbiota prior to cataract surgery; directly supports bacterial clearance as a strategy to prevent post-bacterial ocular sequelae |
| [NCT00407589](https://clinicaltrials.gov/study/NCT00407589) | Phase 1 | Completed | 24 | PK study confirming negligible systemic absorption after topical instillation in patients with bacterial conjunctivitis; critical finding that both establishes ocular safety and limits systemic repurposing potential |
| [NCT01296542](https://clinicaltrials.gov/study/NCT01296542) | Phase 4 | Completed | 60 | Head-to-head comparison of Besivance vs. VIGAMOX (moxifloxacin) for conjunctival bacterial load reduction prior to phacoemulsification; supports prophylactic use to prevent post-surgical infection |
| [NCT01478256](https://clinicaltrials.gov/study/NCT01478256) | Phase 4 | Completed | 30 | Besifloxacin vs. erythromycin for acute blepharitis; demonstrates microbiological efficacy in lid surface infections, relevant to preventing chronic post-infectious lid disease |
| [NCT01740388](https://clinicaltrials.gov/study/NCT01740388) | Phase 3 | Terminated | 136 | BID dosing regimen trial for bacterial conjunctivitis — terminated early (reason undisclosed); termination rationale requires investigation before relying on this dataset |

**Interpretation:** All six trials are in the **ophthalmic domain**, addressing bacterial conjunctivitis and peri-surgical prophylaxis. The mechanistic link to "post-bacterial disorder" is indirect: by eradicating conjunctival bacteria effectively, besifloxacin theoretically reduces the incidence of post-infectious ocular sequelae (e.g., chronic conjunctival scarring, corneal opacity, endophthalmitis after surgery). This is a biologically coherent but indirect inference rather than a designed study of post-bacterial disorder as a primary endpoint.

---

## Otitis Externa: A Mechanistically Compelling Secondary Signal (Rank #8)

Among all non-ophthalmic predictions, **otitis externa** (rank 8, score 99.03%) deserves special mention as the most mechanistically plausible candidate for formulation-adjacent repurposing.

The common causative organisms of otitis externa — *Pseudomonas aeruginosa* and *Staphylococcus aureus* (including MRSA) — overlap directly with besifloxacin's documented antibacterial spectrum. Fluoroquinolone-based ear drops (e.g., ciprofloxacin/dexamethasone) are already the standard of care for otitis externa. Besifloxacin's ophthalmic suspension is chemically compatible with topical otic application, and its superior MRSA coverage compared to existing otic fluoroquinolones represents a potential differentiated value proposition. No clinical trials or literature currently support this use, but the feasibility of an off-label or repurposing trial is higher here than for any systemic indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

As a topically applied fluoroquinolone, the systemic class-level risks (tendinopathy, peripheral neuropathy, QT interval prolongation, dysglycemia) are **not clinically relevant** at besifloxacin's negligible systemic exposure levels following ophthalmic instillation. Local ocular tolerability has been well-characterized across the Phase 3 trial program (n=518, NCT01175590) with an acceptable safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for bronchitis is high (99.84%), reflecting a mechanistically coherent fluoroquinolone class-effect inference, but zero drug-specific clinical or preclinical evidence supports this indication. More importantly, besifloxacin's exclusive availability as a topical ophthalmic suspension represents a **fundamental formulation barrier** that cannot be overcome without new drug development efforts; no route of administration capable of achieving therapeutic bronchial drug concentrations currently exists.

**To proceed with any repurposing pathway, the following is needed:**

- **For bronchitis or any systemic indication:** Development of an oral or inhalation formulation is a prerequisite; this constitutes new drug development, not simple repurposing
- **For post-bacterial disorder (ophthalmic scope):** A prospective study measuring post-infectious ocular sequelae rates (e.g., corneal scarring, endophthalmitis) as primary endpoints using the existing ophthalmic formulation could validate this signal with reasonable feasibility
- **For otitis externa (highest near-term opportunity):** A pilot Phase 2 trial evaluating off-label otic application of the existing 0.6% suspension vs. standard-of-care ciprofloxacin/dexamethasone drops, particularly in MRSA-implicated cases, would represent the most actionable and lowest-barrier repurposing study
- **For all indications:** Retrieval of detailed MOA data from DrugBank (Data Gap DG002) and full package insert warnings/contraindications (Data Gap DG001) are required before any formal safety pre-screening (Stage S1) can be completed
- **Resistance surveillance:** Given global fluoroquinolone resistance trends, a feasibility assessment of the target pathogen's resistance landscape is warranted prior to any respiratory or urogenital indication pursuit

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

