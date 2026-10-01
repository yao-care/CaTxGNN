---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
---

# Imiquimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Imiquimod: From Approved Topical Use to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical immune-response modifier (a TLR7 agonist) marketed in Canada under four licences. The approved indication text was not included in the input data.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**, an umbrella term. The supporting evidence is lesion-specific: cervical, vulvar and anal intraepithelial neoplasia, actinic keratosis and related lesions.
**19 clinical trials** and **9 publications** are listed for this prediction, but most trials are small, early-phase or terminated, and only a few are directly relevant.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The pack's automated scoring assigns L1. Under the stated rules, L1 needs at least two completed Phase 3 RCTs. Only NCT01720407 (Phase 3, completed) may qualify, and its randomised design is not confirmed in the data. The other completed Phase 3 trial (NCT00175643) is open-label with 20 participants. The Phase 3 cervical trial (NCT02329171) was terminated after 9 participants. A completed randomised Phase 2 trial also exists (NCT03233412). L2 is therefore the more defensible level.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, imiquimod activates Toll-like receptor 7 and induces local innate and adaptive antitumour immunity (interferon-alpha, TNF-alpha, IL-12 and a Th1 response). This is a plausible way to clear dysplastic or pre-malignant epithelium, particularly HPV-associated or UV-associated lesions.

The evidence supports specific lesions rather than the umbrella category. The trials cover high-grade cervical intraepithelial neoplasia, vulvar intraepithelial neoplasia, actinic keratosis and actinic cheilitis. The literature includes Cochrane reviews of anal and vulvar intraepithelial neoplasia and reviews of topical therapy for actinic keratosis. Any recommendation should name the specific lesion.

The TxGNN score is consistent with the trial and literature signal but is not evidence in itself. Because the approved indications are not in the input, overlap between the original and new indications cannot be confirmed here.

## Clinical Trial Evidence

No trial results are included in the data; findings below reflect study design and stated purpose.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neo-adjuvant treatment before excision of facial lentigo maligna (intraepidermal melanocytic proliferation). Strongest direct Phase 3 signal. |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Randomised trial of topical imiquimod in high-grade cervical intraepithelial lesions. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomised trial of topical imiquimod versus loop excision for high-grade CIN. Only 9 participants, so underpowered and cannot support efficacy conclusions. |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream for actinic keratoses on the head; assesses duration of effect. |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands and forearms. |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Randomised comparison of 5% imiquimod, 0.05% imiquimod and 0.05% nanoencapsulated imiquimod gel in actinic cheilitis. |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explorative study of immune escape and imiquimod effects in vulvar intraepithelial neoplasia 2/3 and anogenital warts. |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot of neoadjuvant imiquimod (Aldara) in early-stage oral squamous cell carcinoma. Proof-of-concept and an established cancer, not a pre-malignant lesion. |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority trial of surgical excision versus curettage plus imiquimod for nodular basal cell carcinoma. Malignant rather than pre-malignant, so indirect. |

## Literature Evidence

The abstracts in the input are truncated, so the notes below describe scope rather than outcomes.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant HPV-associated condition. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, including topical field therapies. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies (fluorouracil, diclofenac, imiquimod, photodynamic therapy) for non-melanoma skin cancer and precursor lesions. |
| [37817570](https://pubmed.ncbi.nlm.nih.gov/37817570/) | 2024 | Scoping review | Br J Clin Pharmacol | Off-label imiquimod in oral mucosal diseases; reported effectiveness across several conditions, described as promising. |
| [38867102](https://pubmed.ncbi.nlm.nih.gov/38867102/) | 2024 | Review | Evid Based Dent | Scoping review of the safety of off-label imiquimod in oral lesions. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful imiquimod 5% treatment of high-grade vulval intra-epithelial neoplasia in a renal transplant recipient. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Bowenoid papulosis of the penis cleared with topical imiquimod 5%, well tolerated. |
| [12719972](https://pubmed.ncbi.nlm.nih.gov/12719972/) | 2003 | Case report (adverse event) | Med Microbiol Immunol | Malignant conversion of florid oral and labial papillomatosis during topical imiquimod. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2482983 | TARO-IMIQUIMOD PUMP |
| 2365561 | VYLOMA |
| 2340445 | ZYCLARA |
| 2239505 | ALDARA P |

Dosage form and approved indication text are not included in the input data.

## Safety Considerations

Please refer to the package insert for warnings, contraindications and drug interactions. Health Canada package insert data was not available, and no drug-interaction records were found.

Signals from the retrieved literature:
- **Malignant conversion:** One case report describes malignant conversion of florid oral papillomatosis during topical imiquimod (PMID 12719972).
- **Oral off-label use:** A 2024 review specifically examines the safety of off-label imiquimod in oral lesions (PMID 38867102).
- **Skin reactions:** Case reports describe lichen planopilaris and erythema multiforme after imiquimod in patients with Gorlin syndrome.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible, and trials and reviews exist for specific pre-malignant lesions (cervical, vulvar and anal intraepithelial neoplasia, actinic keratosis). The direct evidence is thin: the only large completed Phase 3 trial addresses lentigo maligna, the Phase 3 cervical trial was terminated at 9 participants, and the other trials are small or early-phase. Any use should be restricted to a named lesion type.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Approved indication text and dosage forms for the four DINs, to confirm overlap with existing labelling
- Confirmation of the design and exact lesion type of NCT01720407, and of the target conditions of NCT01229319 and NCT04883645
- A lesion-specific selection (for example high-grade CIN, VIN or actinic keratosis) before any development step
- Mechanism of action data from DrugBank
- Safety review for mucosal sites, given the oral malignant-conversion report

**Other predicted indications (ranks 2–10):** Only "benign neoplasm of buccal mucosa" has any literature (scoping review, animal models, case reports, and a safety signal), and it stays a research question. "Odontogenic cyst" and "cystic neoplasm" have only tangential literature. The other six have no trials or literature and should be held as prediction-only signals.

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

