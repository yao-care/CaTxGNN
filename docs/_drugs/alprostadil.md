---
layout: default
title: Alprostadil
parent: Moderate Evidence (L3-L4)
nav_order: 41
evidence_level: L3
indication_count: 10
---

# Alprostadil
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

# Alprostadil: From Marketed Use to Aortic Malformation

## One-Sentence Summary

Alprostadil (prostaglandin E1) is marketed in Canada under three DINs (Caverject and Prostin VR), but the source data lists no approved indication text.
The TxGNN model predicts it may be effective for **aortic malformation**, supported by **2 registered clinical trials** (neither an efficacy trial for this condition) and **20 publications**, mostly small neonatal series and case reports.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Aortic malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on the retrieved literature, alprostadil is a synthetic form of prostaglandin E1. It relaxes the smooth muscle of the ductus arteriosus and keeps it open.

In duct-dependent aortic lesions, an open ductus keeps blood flowing to the body until surgery or intervention. Examples are interrupted aortic arch, aortic atresia or critical stenosis, hypoplastic left heart, and critical coarctation. The literature describes prostaglandin E1 as having "revolutionized" the management of interrupted aortic arch. Neonatal series spanning several decades show consistent findings.

The source data lists no original indication, so this may be established neonatal practice rather than a true repurposing signal. This should be checked against the Canadian label (Prostin VR) before it is treated as a new indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Acute effects of alprostadil on cerebral and pulmonary flow after bidirectional cavopulmonary connection (single-ventricle palliation). Right drug and congenital heart population, but not aortic malformation. Early termination and small sample limit its weight. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | Cross-sectional comparison of color Doppler ultrasonography and MRA in large-vessel vasculitis. A diagnostic imaging study with no evident alprostadil intervention, so likely matched on the condition only. |

## Literature Evidence

Listed by priority: reviews first, then cohorts and case series, then case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Review | Semin Thorac Cardiovasc Surg | Prostaglandin E1 transformed interrupted aortic arch management. Stabilization over days precedes one-stage neonatal repair. |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Review | Cardiol Young | Preoperative management of neonates with critical aortic valvar stenosis, a rare condition often presenting with cardiogenic shock. |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Review | J Neonatal Perinat Med | Enteral feeding and necrotising enterocolitis risk in duct-dependent heart disease infants on prostaglandin E1. |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Cohort | Pharmacotherapy | Alprostadil dilates the ductus and increases pulmonary blood flow in infants with congenital heart malformations. |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Case series | J Am Coll Cardiol | 17 neonates received prostaglandin E1 for an average of 39 days (range 8–104). Included two with aortic coarctation. |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case series | Pediatr Cardiol | Prostaglandin E1 in 7 infants with hypoplastic left ventricle and aortic atresia. Six showed transient improvement, but most non-operated patients died. |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Cohort | Asian J Surg | Surgical results of a staged-repair policy for infants with interrupted aortic arch. |
| [10771966](https://pubmed.ncbi.nlm.nih.gov/10771966/) | 1998 | Cohort | Indian J Pediatr | Prostaglandin E1 as first-stage palliation across ductus-dependent congenital cardiac defects. |
| [28508920](https://pubmed.ncbi.nlm.nih.gov/28508920/) | 2017 | Case report | Pediatr Cardiol | Neonate with critical coarctation developed second- and third-degree AV block on prolonged low-dose infusion. It resolved after discontinuation. |
| [1926911](https://pubmed.ncbi.nlm.nih.gov/1926911/) | 1991 | Not classified | DICP Ann Pharmacother | Starting prostaglandin E1 before neonatal transport when a ductus-dependent defect is suspected. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2215756 | CAVERJECT STERILE POWDER |
| 559253 | PROSTIN VR STERILE SOLUTION |
| 2215187 | CAVERJECT STERILE POWDER - PWS 23.2MCG/VIAL |

## Safety Considerations

Package insert warnings, contraindications, and drug interaction data are not available in the source record. Please refer to the package insert for authoritative safety information.

The retrieved literature reports these signals with prostaglandin E1 infusion in neonates:
- **Prolonged infusion:** transient hypertrophic pyloric stenosis or antral foveolar hyperplasia (PMIDs 25263728, 23521358). Prolonged therapy needs specific monitoring.
- **Cardiac conduction:** second- and third-degree AV block with chronic low-dose infusion (PMID 28508920).
- **Other effects:** apnea, fever, hypotension, flushing, rash, and a harlequin skin colour change (PMIDs 23521358, 15461766). Necrotising enterocolitis risk is a concern with enteral feeding (PMID 30347623).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is biologically coherent and consistent across decades of neonatal series and reviews. There is no Phase 2/3 RCT for this condition, so the evidence stays at L3. Lower-ranked predictions (congenital tricuspid stenosis, tricuspid valve agenesis, heart septal defect) rest on indirect evidence, and the rest have no supporting studies.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Confirmation against the Prostin VR label of whether ductus-dependent aortic lesions are already an approved use
- Mechanism of action data from DrugBank
- Guardrails: neonatal ICU setting only, monitoring for apnea, hypotension, fever and AV block, and the lowest effective dose and duration
- Controlled or larger comparative data for aortic lesions specifically

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

