---
layout: default
title: Alprostadil
parent: Moderate Evidence (L3-L4)
nav_order: 41
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Alprostadil: predicted new indication Aortic malformation (evidence level L4). Approved use: Erectile dysfunction, psychologic dyspareunia, premature ejaculation…"
monitor_inn: "Alprostadil"
predicted_indications: ["congenital tricuspid stenosis", "congenital valvular dysplasia", "tricuspid valve agenesis", "straddling or overriding tricuspid valve", "tricuspid valve prolapse (disease)", "anomaly of the tricuspid subvalvular apparatus", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "heart septal defect", "endemic goiter"]
---

# Alprostadil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Alprostadil: From Erectile Dysfunction and Ductal-Dependent Congenital Heart Disease to Aortic Malformation

## One-Sentence Summary

Alprostadil (prostaglandin E1) is originally used for erectile dysfunction and for keeping the ductus arteriosus open in newborns with ductal-dependent congenital heart disease (such as tricuspid atresia, aortic coarctation and tetralogy of Fallot).
The TxGNN model predicts it may be effective for **aortic malformation**, with **no registered clinical trials** and **8 publications** (mostly case reports and observational studies) currently related to this direction.
This is largely an extension within its existing approved indication class rather than a wholly new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction, psychologic dyspareunia, premature ejaculation, tricuspid atresia, aortic coarctation, tetralogy of Fallot, and related congenital heart defects (Health Canada licence text is not available) |
| Predicted New Indication | Aortic malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, alprostadil is a prostaglandin E1 that relaxes the smooth muscle of the ductus arteriosus. This keeps the duct open, which increases pulmonary or systemic blood flow in newborns whose circulation depends on it.

Aortic coarctation is already among the original indications. Other aortic malformations, such as interrupted aortic arch, also depend on ductal patency to supply the body's circulation before surgery. Because the mechanism is shared, the high prediction score is biologically plausible.

Several other lesions in the model's top-ten list are weaker. Predictions for tricuspid valve prolapse, endemic goiter and isolated septal defects have little or no mechanistic basis. These are not the focus of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Clinical evaluation / case series | Pharmacotherapy | Alprostadil infusion dilates the ductus, increases pulmonary blood flow and supports newborns with congenital malformations that depend on ductal patency |
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | Clinical study | Zhonghua Yi Xue Za Zhi | Alprostadil with ulinastatin studied for inflammatory response and lung injury after cardiopulmonary bypass in children with congenital heart disease (not ductal patency) |
| [19068708](https://pubmed.ncbi.nlm.nih.gov/19068708/) | 2008 | Case report | Kyobu Geka | Neonate with interrupted aortic arch type B kept ductus open with alprostadil, then had single-stage repair and survived |
| [30184041](https://pubmed.ncbi.nlm.nih.gov/30184041/) | 2018 | Case report | Braz J Cardiovasc Surg | Alprostadil and milrinone used before surgery to counter high lung pressure in a child with aortopulmonary window |
| [15362549](https://pubmed.ncbi.nlm.nih.gov/15362549/) | 2004 | Review | Kyobu Geka | Alprostadil keeps the ductus patent in transposition of the great arteries before arterial switch surgery |
| [41167776](https://pubmed.ncbi.nlm.nih.gov/41167776/) | 2025 | Observational study | Zhonghua Fu Chan Ke Za Zhi | Retrospective study of delivery mode and timing in 123 fetuses with complex congenital heart disease |
| [42469655](https://pubmed.ncbi.nlm.nih.gov/42469655/) | 2026 | Observational study | BMC Pregnancy Childbirth | Preliminary retrospective study of perinatal management of complex fetal congenital heart disease |
| [20029353](https://pubmed.ncbi.nlm.nih.gov/20029353/) | 2009 | Preclinical animal study | Minerva Chirurgica | Alprostadil in rat skeletal muscle ischaemia-reperfusion injury (not relevant to this indication) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02215756 | CAVERJECT STERILE POWDER | Not stated | Not stated |
| 00559253 | PROSTIN VR STERILE SOLUTION | Not stated | Not stated |
| 02215187 | CAVERJECT STERILE POWDER - PWS 23.2MCG/VIAL | Not stated | Not stated |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The model's drug-disease contraindication links include newborn and acute respiratory distress syndrome, hypotensive disorder, blood coagulation disease, sickle cell disease and other haemoglobinopathies, lung disease, plasma cell myeloma, leukaemias, polycythaemia, thrombocytosis, priapism, Peyronie disease, urethral stricture, urethritis, balanitis and pyloric stenosis. These must be confirmed against the Canadian product labels.
- **Adverse effect signals from the literature**: Prolonged prostaglandin E1 infusion in neonates has been associated with gastric outlet obstruction (antral foveolar hyperplasia, hypertrophic pyloric stenosis) and with pseudo-Bartter syndrome. Other known side effects include fever, rash, apnoea, diarrhoea, jitteriness and flushing.
- **Drug Interactions**: 59 interactions were recorded. Those rated Moderate are canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, lorcaserin and sapropterin. Others, such as pantoprazole, morphine, metformin, omeprazole, vancomycin, atropine, prednisone, simvastatin, amphotericin B, potassium chloride, prednisolone and ranitidine, have no severity rating.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For aortic malformations that depend on ductal patency, the mechanism matches the established use in aortic coarctation, and published case reports and reviews support it. However, there are no registered trials and no controlled evidence. The package insert warnings and contraindications are also missing from the compiled data, which currently blocks safety screening. The other nine predictions have little or no supporting evidence and should remain on Hold.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text for all three DINs
- Detailed mechanism of action data (MOA)
- Review of the literature to confirm relevance of each publication, and a search for controlled studies in interrupted aortic arch and similar lesions
- A safety monitoring plan for neonates, covering apnoea, gastric outlet obstruction and electrolyte disturbance during prolonged infusion
- Clarification of which formulation applies: the Prostin VR product is the likely one for neonatal ductal use, while Caverject is an erectile dysfunction product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

