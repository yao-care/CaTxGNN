---
layout: default
title: Alprostadil
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Alprostadil
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

# Alprostadil: From Patent Ductus Arteriosus Maintenance to Aortic Malformation

## One-Sentence Summary

Alprostadil (Prostaglandin E1, PGE1) is a synthetic prostaglandin analogue with well-established use in neonatal intensive care for maintaining patent ductus arteriosus (PDA) in ductus-dependent congenital heart disease — though no formal approved indication is currently on record in Canada.
The TxGNN model predicts it may be effective for **Aortic Malformation** (including conditions such as interrupted aortic arch and aortic coarctation),
with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in Canada (known clinical use: PDA maintenance in ductus-dependent neonatal CHD) |
| Predicted New Indication | Aortic Malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

While formal mechanism of action data is not available in this dataset, alprostadil is the synthetic form of prostaglandin E1 (PGE1). It acts on EP2 and EP4 prostaglandin receptors, activating adenylyl cyclase and raising intracellular cAMP levels in vascular smooth muscle. The resulting smooth muscle relaxation produces potent vasodilation — and most critically in the neonatal context, it prevents closure of the ductus arteriosus (PDA), the fetal vessel that connects the pulmonary artery to the descending aorta.

Aortic malformations such as interrupted aortic arch (IAA), critical aortic coarctation, and hypoplastic left heart syndrome are classic "ductus-dependent" lesions. In these conditions, systemic perfusion to the lower body depends entirely on right-to-left blood flow through the PDA. When the ductus spontaneously closes after birth — as it normally would — these infants deteriorate rapidly into cardiogenic shock. Alprostadil infusion maintains ductal patency, restoring systemic circulation and providing a critical window for preoperative stabilization before surgical repair.

The mechanistic link is therefore direct and exceptionally strong. As noted in landmark review literature, the introduction of PGE1 in the late 1970s *revolutionized* the management of interrupted aortic arch and similar lesions, enabling complete resuscitation over days prior to surgery and dramatically improving survival. The TxGNN model's near-perfect prediction score (99.98%) almost certainly reflects this well-established physiological relationship rather than a novel discovery.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Evaluated the acute effects of alprostadil on cerebral and pulmonary blood flow after bidirectional cavopulmonary connection (second-stage single-ventricle palliation). Study was terminated — possibly due to recruitment difficulties or safety findings — but provides direct Phase 1 evidence of alprostadil's hemodynamic role in complex aortic/cardiac malformations. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | A diagnostic cross-sectional comparison of Color Doppler Ultrasonography vs. MRI Angiography in systemic large vessel vasculitis involving supraaortic vessels (aorta, carotid, subclavian). Not a therapeutic trial for alprostadil; relevance to treatment of aortic malformation is low. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | RCT | Zhonghua Yi Xue Za Zhi | Alprostadil (Lipo-PGE1) combined with ulinastatin significantly attenuated inflammatory response and lung injury following cardiopulmonary bypass in pediatric patients with congenital heart disease. Provides direct RCT evidence of alprostadil's protective role in CHD surgery. |
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Review | Seminars in Thoracic & Cardiovascular Surgery | States that the introduction of prostaglandin E1 in the late 1970s "revolutionized" the management of interrupted aortic arch. Advocates for complete resuscitation over several days with PGE1 before surgery. One-stage primary neonatal repair is now the preferred approach. |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Review / Clinical Guideline | Cardiology in the Young | Outlines preoperative management of neonates with critical aortic valvar stenosis. Emphasizes PGE1 infusion as a key stabilizing measure prior to intervention; describes how maintaining ductal patency protects coronary perfusion in the critical period. |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Review | Journal of Neonatal-Perinatal Medicine | Reviews feeding strategies and outcomes in infants with duct-dependent congenital heart lesions treated with PGE1 infusion, including risks of necrotising enterocolitis during treatment. Supports the standard-of-care status of PGE1 in this population. |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Observational / Case Series | Pharmacotherapy | Foundational evaluation of alprostadil in the management of various forms of congenital heart disease. Demonstrates that PGE1 dilates the ductus, increases pulmonary blood flow, and improves systemic oxygenation in neonates with right ventricular outflow obstruction. |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Retrospective Cohort | Asian Journal of Surgery | Reports outcomes of staged surgical repair for interrupted aortic arch (IAA) at a single centre. PGE1 infusion was part of standard preoperative stabilization. Confirms the role of prostaglandin therapy as a bridge to definitive surgical correction. |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case Series | Pediatric Cardiology | PGE1 infusion in 7 infants with hypoplastic left ventricle and aortic atresia. Transient hemodynamic improvement was observed, though mortality remained high in this severe lesion group. Highlights both the utility and limitations of PGE1 in extreme ductus-dependent aortic malformations. |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Case Series | Journal of the American College of Cardiology | Long-term PGE1 infusion (average 39 days, up to 104 days) in 17 neonates with various congenital heart defects including aortic coarctation and transposition of the great arteries. Demonstrates feasibility and outcomes of extended bridging therapy. |
| [10771966](https://pubmed.ncbi.nlm.nih.gov/10771966/) | 1998 | Case Series | Indian Journal of Pediatrics | Describes the role of PGE1 as first-stage palliation in neonates with ductus-dependent CHD, including pulmonary atresia, aortic coarctation, and transposition of the great arteries. Emphasizes life-saving potential when initiated promptly. |
| [28508920](https://pubmed.ncbi.nlm.nih.gov/28508920/) | 2017 | Case Report | Pediatric Cardiology | Reports development of second- and third-degree atrioventricular block in a neonate with critical coarctation of the aorta during prolonged low-dose PGE1 infusion. The conduction disturbances resolved upon discontinuation. Highlights an important — and underrecognized — safety signal relevant to long-term use. |

---

## Canada Market Information

Alprostadil currently has **no active Drug Identification Numbers (DINs) in Canada** and is not commercially marketed. There are no approved product licenses on record in the Health Canada database for this drug.

> **Note:** Alprostadil (PGE1) is widely used as an essential medicine in neonatal intensive care units globally and is listed on the WHO Essential Medicines List for ductus-dependent congenital heart disease. Its absence from the Canadian market does not reflect a lack of clinical need; it may be obtained through special access or compounding pathways in practice.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug-drug interactions) were not available in this evidence pack for the Canadian context. Key safety signals identified in the literature include:

- **Apnoea:** Occurs in approximately 10–12% of neonates receiving PGE1 infusion, particularly at higher doses; requires respiratory monitoring and availability of ventilatory support.
- **Prolonged infusion complications:** Long-term PGE1 use (weeks to months) has been associated with cortical hyperostosis, hypertrophic pyloric stenosis/antral foveolar hyperplasia, and — as reported in recent literature — atrioventricular conduction blocks (see PMID 28508920).
- **Systemic hypotension and fever:** Common dose-dependent side effects requiring close haemodynamic monitoring.
- **Necrotising enterocolitis (NEC):** A risk associated with enteral feeding during PGE1 infusion in duct-dependent CHD (see PMID 30347623).

Please refer to the package insert and institutional neonatal cardiology protocols for complete safety prescribing information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between alprostadil and aortic malformation is direct, biologically sound, and well-supported by decades of neonatal cardiology practice. Multiple case series, retrospective cohort studies, one RCT in the CPB-CHD context, and multiple review-level publications (including clinical guidelines) substantiate PGE1's role as standard preoperative stabilization therapy for ductus-dependent aortic lesions. The TxGNN model's prediction at L3 evidence level is consistent with established clinical use, albeit not yet supported by large-scale Phase 3 randomized trials in the strict sense.

**To proceed, the following is needed:**

- **Formal MOA data:** Retrieve complete pharmacological profile from DrugBank (DB00770) to document EP2/EP4 receptor mechanism and cAMP pathway in the evidence record.
- **Canadian regulatory pathway:** Confirm availability mechanism in Canada (Special Access Programme, compounding, or importation) given no active DINs. Assess feasibility of formal Health Canada submission if a commercial indication is sought.
- **Full safety profile:** Obtain and review the current Canadian/US package insert for complete warnings, contraindications, dose-response safety data, and monitoring requirements specific to neonatal intravenous use.
- **Dose optimization data:** Identify optimal dosing protocols for aortic malformation subtypes (e.g., IAA Type A/B/C, critical coarctation) based on available literature and institutional guidelines.
- **Prospective trial consideration:** Given the ethical and logistical challenges of RCTs in critically ill neonates, consider a prospective registry or pragmatic adaptive trial design to generate higher-level evidence (L2/L1) for specific aortic malformation subtypes.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

