---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a broad-spectrum aminopenicillin antibiotic with a long-established history of treating a wide range of bacterial infections, including respiratory, urinary tract, gastrointestinal, and skin infections.
The TxGNN model predicts it may be effective for **Laryngitis**, with **1 clinical trial** and **20 publications** currently supporting this direction.
The available evidence is largely indirect — largely drawn from related ENT infections and broad penicillin-class literature — and key safety data was not retrieved in this Evidence Pack, warranting a Hold decision pending data completion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (respiratory, urinary tract, meningitis, skin infections) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed (per current dataset) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank in this Evidence Pack. Based on established pharmacological knowledge, Ampicillin is an aminopenicillin (broad-spectrum beta-lactam) that inhibits bacterial cell wall synthesis by irreversibly binding to penicillin-binding proteins (PBPs). This disrupts peptidoglycan cross-linking, leading to osmotic instability and bacterial cell death. Its spectrum covers key Gram-positive organisms (including Streptococcus pyogenes, Streptococcus pneumoniae) and select Gram-negative organisms (including Haemophilus influenzae) — all recognised pathogens in upper respiratory tract infections.

Laryngitis — inflammation of the larynx — is predominantly viral, but bacterial laryngitis does occur, most commonly caused by S. pneumoniae, H. influenzae, and Moraxella catarrhalis. Ampicillin's in vitro and clinical activity against these organisms provides a mechanistic basis for the TxGNN model's prediction. The drug has historically been included in empirical treatment regimens for acute upper respiratory infections, including pharyngitis, tonsillitis, and epiglottitis, which share overlapping pathogen profiles with bacterial laryngitis.

That said, the evidence retrieved in this pack is almost entirely indirect: the single registered clinical trial examined amoxicillin/clavulanate (not ampicillin alone) across a mixed paediatric respiratory cohort that included laryngitis as one of several indications, and the literature largely consists of case reports, case series, and observational studies describing laryngeal infections where beta-lactams were employed. No dedicated RCT evaluating ampicillin specifically for laryngitis was identified.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing surveillance of CLAVAMOX® (amoxicillin/clavulanate) in Japanese paediatric patients; covered multiple indications including laryngitis, pharyngitis, tonsillitis, skin infections, and urinary tract infections — not specific to ampicillin alone or to laryngitis as a primary endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline Review | CoDAS | AGREE II quality assessment of clinical guidelines for laryngitis and pharyngitis management; highlights current evidence base and gaps |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case Report + Review | Ann Otol Rhinol Laryngol | Historical and modern review of spontaneous laryngeal abscess; antibiotics (including beta-lactams) remain the cornerstone treatment; modern cases associated with immunosuppression and diabetes |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case Report | Auris Nasus Larynx | COVID-19 presenting as acute epiglottitis with necrotic laryngeal lesions; illustrates the need for antibiotic cover in severe laryngeal infections |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Observational | Eur Arch Otorhinolaryngol | Microbiological analysis and antibiotic selection in neck abscesses among diabetic patients; supports broad-spectrum penicillin-class antibiotics in deep ENT infections |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case Report | Auris Nasus Larynx | Post-transplant laryngeal actinomycosis in a 14-year-old; treated with prolonged penicillin course — demonstrates beta-lactam efficacy in laryngeal infections |
| [24930374](https://pubmed.ncbi.nlm.nih.gov/24930374/) | 2014 | Case Report | J Voice | Laryngeal actinomycosis in a 74-year-old immunocompromised patient; penicillin (beta-lactam class) resolved infection after laryngeal biopsy-guided diagnosis |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | Case Series | Acta Otorrinolaringol Esp | Two cases of paraglottic laryngeal abscess — a rare, life-threatening condition requiring urgent diagnosis and antibiotic therapy |
| [7487676](https://pubmed.ncbi.nlm.nih.gov/7487676/) | 1995 | Animal Study | Auris Nasus Larynx | Ampicillin ± ibuprofen in experimental acute otitis media (chinchilla model); demonstrates ampicillin's antibacterial efficacy in upper respiratory tract bacterial infections |
| [41536375](https://pubmed.ncbi.nlm.nih.gov/41536375/) | 2025 | Case Report | Cureus | Croup differential diagnosis in a 3-year-old; case highlights when bacterial aetiology should be reconsidered and antibiotic therapy escalated |
| [1712371](https://pubmed.ncbi.nlm.nih.gov/1712371/) | 1991 | Case Series | J Clin Gastroenterol | Short-term antibiotic treatment in Whipple's disease; one patient treated with ampicillin 2 g/day with clinical response — documents ampicillin's clinical use |

---

## Canada Market Information

No approved products (DINs) for Ampicillin were found in the Health Canada regulatory dataset included in this Evidence Pack.

> **Note:** The absence of DINs in this dataset may reflect a data retrieval gap rather than a true absence from the Canadian market. Ampicillin and its prodrug forms (e.g., pivampicillin, bacampicillin) have been widely used internationally. A direct search of the Health Canada Drug Product Database (DPD) is recommended to confirm current market status.

---

## Safety Considerations

Key warnings, contraindications, and drug interaction data were not retrieved in this Evidence Pack. Before proceeding with any clinical evaluation:

> Please refer to the ampicillin product monograph and Health Canada package insert for complete safety information. Clinically important considerations include: hypersensitivity reactions and cross-reactivity in penicillin-allergic patients (including risk of anaphylaxis), antibiotic-associated diarrhoea and *Clostridioides difficile* infection, ampicillin-associated maculopapular rash in patients with infectious mononucleosis (EBV), and interactions with oral anticoagulants and probenecid.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is missing critical safety data (warnings, contraindications, drug interactions), and the Canada regulatory data shows no DINs currently on record — both represent blocking gaps that prevent a complete first-stage safety screening. While ampicillin's mechanistic rationale for bacterial laryngitis is sound and its broad antimicrobial use is well established, the evidence in this pack is entirely indirect with no dedicated trial specifically evaluating ampicillin for laryngitis, and no comparative efficacy data in this indication.

**To proceed, the following is needed:**
- Retrieve the Health Canada product monograph / package insert for ampicillin to complete safety pre-screening (warnings, contraindications, DDI)
- Confirm Canadian market availability via direct Health Canada DPD query
- Determine whether any dedicated clinical trials for aminopenicillins (ampicillin or amoxicillin) in bacterial laryngitis have been conducted or are ongoing
- Clarify target clinical context: bacterial vs. viral laryngitis, acute vs. chronic, severity spectrum, and intended patient population (paediatric vs. adult)
- Review current Canadian antibiotic resistance surveillance data for common laryngitis pathogens (particularly *Streptococcus pyogenes* and *H. influenzae*) to confirm that ampicillin retains adequate in vitro activity in the Canadian context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

