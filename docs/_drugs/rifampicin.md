---
layout: default
title: Rifampicin
parent: Moderate Evidence (L3-L4)
nav_order: 799
evidence_level: L4
indication_count: 10
---

# Rifampicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Rifampicin: From Antibacterial Therapy to Conjunctivitis

## One-Sentence Summary

Rifampicin is an antibacterial drug (DrugBank DB01045) that is marketed in Canada, though the licence records supplied give no approved-indication text.
The TxGNN model predicts it may be effective for **conjunctivitis**.
**No clinical trials** are registered for this pairing, and the **20 publications** retrieved are mostly susceptibility surveys, case reports and one 1975 topical trachoma study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (rifampicin is an antibacterial agent) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on general pharmacology, rifampicin inhibits bacterial DNA-dependent RNA polymerase. It is active against organisms that can infect the conjunctiva, including *Staphylococcus aureus*, *Chlamydia trachomatis* and *Neisseria meningitidis*.

The link between the original and predicted uses is therefore antibacterial. Bacterial conjunctivitis and trachoma are eye infections caused by susceptible organisms, so a drug that kills these bacteria could plausibly help.

The supporting evidence is mostly indirect. It consists of microbiology and susceptibility surveys and a few case reports. The one possible interventional signal is a 1975 trachoma study in Tunisia that used topical rifampicin ointment, and its design and results cannot be verified from the supplied fields. The prediction also has a duplicate node, "conjunctivitis (disease)", with largely the same literature, so the two should be merged downstream to avoid double counting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | Clinical study (design unverified) | Am J Ophthalmol | Controlled trachoma trial in Tunisian schoolchildren comparing 1% rifampicin ointment (76 patients), 1% tetracycline ointment (79) and 5% boric acid ointment (79), applied twice daily for 10 weeks. Outcomes are not shown in the supplied abstract. |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | Case report | Clin Microbiol Infect | Primary meningococcal conjunctivitis in a healthy 6-year-old boy, treated with topical antibiotics and then systemic rifampin once the diagnosis was established. No ocular or systemic complications developed. |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | Surveillance (susceptibility) | Adv Biomed Res | Bacterial causes and antibiotic susceptibility of conjunctivitis isolates in Kashan, Iran. |
| [8363150](https://pubmed.ncbi.nlm.nih.gov/8363150/) | 1993 | Surveillance (susceptibility) | An Esp Pediatr | Fifty neonatal conjunctival samples; 84% were culture-positive, mainly staphylococci and *S. pneumoniae*. Isolates were highly sensitive to most drugs tested, except penicillin. |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | Surveillance | An Pediatr (Barc) | Most prevalent pathogens in bacterial conjunctivitis and their antibiotic sensitivity. |
| [21191558](https://pubmed.ncbi.nlm.nih.gov/21191558/) | 2010 | Surveillance (susceptibility) | Rev Esp Quimioter | Antibiotic susceptibility of *Corynebacterium macginleyi* strains causing conjunctivitis. |
| [30347565](https://pubmed.ncbi.nlm.nih.gov/30347565/) | 2018 | Experimental (lab) | Zhonghua Yan Ke Za Zhi | Genetic typing and susceptibility of 34 *S. aureus* strains from keratitis or conjunctivitis patients. |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | Surveillance | J Ophthalmic Inflamm Infect | Bacterial agents of conjunctivitis in Lagos, Nigeria, with resistance and plasmid profiles. |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | Preclinical (title only) | Nature | Anti-trachoma activity of rifampicin and rifamycin SV derivatives. No abstract available. |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Overview (title only) | Ann Ophthalmol | Short ophthalmology article titled "Rifampicin". No abstract available. |

---

## Canada Market Information

| DIN / Licence No. | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 343617 | ROFACT | — | — |
| 393444 | ROFACT | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

One interaction concern appears in the literature retrieved for other predicted indications. Rifampicin is a strong CYP3A4 and UGT1A1 inducer and lowers exposure to several co-administered drugs, such as efavirenz, dolutegravir and atazanavir. Systemic use would need a full interaction review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.95% score is supported only by indirect evidence: susceptibility surveys, case reports and a single 1975 topical trachoma study with unverified design and results. There are no registered trials for conjunctivitis, and the Canadian licence records give no indication or dosage-form details.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, and the approved indications for both ROFACT licences
- Mechanism of action data from DrugBank
- Full text and outcomes of the 1975 Tunisian trachoma study (PMID 1096630)
- Confirmation of whether any ocular or topical rifampicin formulation is available in Canada, since route compatibility has not been assessed
- Merging the "conjunctivitis" and "conjunctivitis (disease)" nodes

**Other predicted indications (for reference):**
- **Rheumatoid arthritis** is the most advanced candidate (L2). It has several small 1988–1993 rifampicin studies and a Phase 3 antibiotic-combination trial in reactive arthritis (n=42), which are inconclusive on efficacy.
- **Acne:** the literature actually concerns hidradenitis suppurativa (clindamycin plus rifampicin), so this node should be remapped.
- **HIV and related nodes:** the trials are TB/HIV drug-interaction studies and do not support repurposing.
- **Remaining nodes:** these rest on the model score alone, with no supporting evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

