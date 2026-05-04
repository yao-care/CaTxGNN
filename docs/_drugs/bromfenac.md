---
layout: default
title: Bromfenac
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Bromfenac
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

# Bromfenac: From Post-Cataract Ocular Inflammation to Broader Eye Disease

## One-Sentence Summary

Bromfenac is a topical ophthalmic non-steroidal anti-inflammatory drug (NSAID) globally established for treating post-operative ocular inflammation and pain after cataract surgery, though it currently holds no Canadian market authorization.
The TxGNN model predicts it may be effective across a broader spectrum of **Eye Disease** — encompassing conditions such as macular edema, age-related macular degeneration, dry eye disease, and pterygium,
with **6+ completed Phase 3 RCTs**, additional Phase 4 post-marketing studies, and **20 publications** currently supporting this expanded direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Post-operative ocular inflammation and pain following cataract surgery (inferred from global clinical context; no Canadian DIN on file) |
| Predicted New Indication | Eye Disease (broader ocular indications including macular edema, AMD, dry eye, pterygium) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known published pharmacology, bromfenac is a topical ophthalmic NSAID of the aminonicotinic acid class that inhibits both cyclooxygenase-1 (COX-1) and cyclooxygenase-2 (COX-2), thereby blocking prostaglandin synthesis (primarily PGE₂ and PGI₂) in ocular tissues. This mechanism directly suppresses the post-operative inflammatory cascade, which underpins its established use after cataract surgery in jurisdictions such as the United States (FDA-approved as Xibrom, Bromday, and Prolensa), Japan, and the European Union.

The TxGNN prediction for "eye disease" as a broader category is mechanistically well-grounded because COX-mediated prostaglandin overproduction is a shared pathological thread across many ophthalmic conditions — including cystoid macular edema, diabetic macular edema, age-related macular degeneration, allergic conjunctivitis, pterygium, and dry eye disease. Beyond prostaglandin suppression, bromfenac has demonstrated additional biological activities that extend its clinical rationale: it directly inhibits TGF-β1-induced fibrotic effects in primary human pterygium and conjunctival fibroblasts (PMID 30908581), and reduces retinal gliosis and PGE₂ levels following optic nerve injury in animal models (PMID 27832276). A 2024 meta-analysis further confirms its adjunctive potential in VEGF-driven maculopathies such as neovascular AMD and diabetic macular edema (PMID 39180057).

Taken together, the convergence of direct clinical trial evidence, mechanistic plausibility across multiple ocular disease subtypes, and the TxGNN knowledge graph signal strongly supports pursuing bromfenac's application beyond its original post-cataract niche into the broader "eye disease" landscape — particularly for macular edema prevention and anti-VEGF adjunctive therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00198445](https://clinicaltrials.gov/study/NCT00198445) | Phase 3 | Completed | 527 | Large RCT demonstrating bromfenac ophthalmic solution 0.09% is efficacious and safe for post-operative ocular inflammation following cataract extraction and IOL implantation — highest-grade direct evidence |
| [NCT01367249](https://clinicaltrials.gov/study/NCT01367249) | Phase 3 | Completed | 440 | Efficacy of bromfenac ophthalmic solution vs. placebo for ocular inflammation and pain associated with cataract surgery |
| [NCT01774474](https://clinicaltrials.gov/study/NCT01774474) | Phase 3 | Completed | 1,127 | Large RCT evaluating prevention of cystoid macular edema after cataract surgery in both diabetic and non-diabetic patients; designed to generate evidence-based guidelines |
| [NCT01212471](https://clinicaltrials.gov/study/NCT01212471) | Phase 3 | Completed | 840 | Dose-ranging study evaluating safety and efficacy of bromfenac ophthalmic solution across formulations in dry eye disease |
| [NCT00703781](https://clinicaltrials.gov/study/NCT00703781) | Phase 3 | Completed | 126 | Phase 3 assessment of bromfenac efficacy and safety in the cataract surgery setting |
| [NCT00704418](https://clinicaltrials.gov/study/NCT00704418) | Phase 3 | Completed | 156 | Additional Phase 3 confirmation of bromfenac efficacy and safety in cataract surgery |
| [NCT07090044](https://clinicaltrials.gov/study/NCT07090044) | Phase 4 | Completed | 77 | Post-marketing study directly comparing bromfenac sodium, loteprednol, and artificial tears for alleviating pain after intravitreal injection over a 24-hour period |
| [NCT03317847](https://clinicaltrials.gov/study/NCT03317847) | Phase 4 | Completed | 92 | Head-to-head comparison of bromfenac vs. dexamethasone eye drops for controlling anterior chamber inflammation after cataract surgery, measured by Laser Flare Photometry |
| [NCT04022811](https://clinicaltrials.gov/study/NCT04022811) | Phase 4 | Completed | 60 | Bromfenac 0.1% twice daily evaluated for ocular inflammation and pain after pterygium excision with amniotic membrane transplantation |
| [NCT00805233](https://clinicaltrials.gov/study/NCT00805233) | Phase 2 | Completed | 30 | Exploratory trial investigating bromfenac ophthalmic drops combined with ranibizumab intravitreal injection vs. ranibizumab alone for neovascular age-related macular degeneration |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31343372](https://pubmed.ncbi.nlm.nih.gov/31343372/) | 2019 | RCT/Expert Review | Expert Opinion on Pharmacotherapy | Bromfenac 0.075% in DuraSite vehicle is efficacious and safe for cataract surgery pain/inflammation; slightly superior posterior segment bioavailability compared to other topical NSAIDs |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | RCT/Comparative | International Journal of Ophthalmology | Three-arm comparative study of bromfenac 0.09% vs. nepafenac 0.1% vs. diclofenac 0.1% for CME prophylaxis after phacoemulsification — bromfenac demonstrated competitive efficacy |
| [39180057](https://pubmed.ncbi.nlm.nih.gov/39180057/) | 2024 | Meta-analysis | BMC Ophthalmology | Topical bromfenac reduces treatment burden and improves outcomes of anti-VEGF therapy in neovascular AMD, diabetic macular edema, and retinal vein occlusions — supports expanded indications |
| [17445902](https://pubmed.ncbi.nlm.nih.gov/17445902/) | 2007 | RCT | Ophthalmology | Pivotal Phase 3 trial (Xibrom) establishing bromfenac 0.09% efficacy and safety for post-cataract ocular inflammation and pain reduction |
| [21762992](https://pubmed.ncbi.nlm.nih.gov/21762992/) | 2011 | RCT | Ophthalmology | Bromfenac 0.09% dosed once daily (Bromday) is safe and effective for post-cataract ocular inflammation, supporting simplified dosing regimen |
| [19735215](https://pubmed.ncbi.nlm.nih.gov/19735215/) | 2009 | Review | Expert Opinion on Pharmacotherapy | Comprehensive review of ophthalmic utility; twice-daily bromfenac clearly superior to placebo for post-cataract outcomes with favorable COX-1/COX-2 inhibition profile |
| [26068607](https://pubmed.ncbi.nlm.nih.gov/26068607/) | 2015 | Clinical Study | Asia-Pacific Journal of Ophthalmology | Bromfenac sodium ophthalmic solution effective in dry eye disease patients with inadequate response to artificial tears alone |
| [30009640](https://pubmed.ncbi.nlm.nih.gov/30009640/) | 2018 | Comparative Study | Current Eye Research | Bromfenac 0.09% vs. diclofenac 0.1% as adjunctive therapy after cataract surgery — comparable anti-inflammatory efficacy with good tolerability profile |
| [30908581](https://pubmed.ncbi.nlm.nih.gov/30908581/) | 2019 | In Vitro | Investigative Ophthalmology & Visual Science | Bromfenac directly inhibits TGF-β1-induced fibrotic effects in primary human pterygium and conjunctival fibroblasts — provides mechanistic rationale for anti-fibrotic applications |
| [27832276](https://pubmed.ncbi.nlm.nih.gov/27832276/) | 2016 | Animal Study | Investigative Ophthalmology & Visual Science | Topical bromfenac reduces retinal gliosis, suppresses PGE₂ levels, and attenuates inflammation after complete optic nerve crush — extends mechanistic rationale to retinal disease |

---

## Canada Market Information

Bromfenac currently has no Drug Identification Numbers (DINs) registered with Health Canada and is not marketed in Canada. There are no approved indications, licensed products, or dosage forms on file in the Canadian regulatory system.

For reference, bromfenac ophthalmic solutions are approved in other major jurisdictions: in the United States (Xibrom 0.09%, Bromday 0.09%, Prolensa 0.07%) for post-cataract surgery ocular inflammation and pain; and in Japan (Bronuck 0.1%) with additional approved indications. Any Canadian commercialization pathway would require a new drug submission to Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Notable safety signals from included literature evidence:** Post-marketing case reports document rare but serious adverse events with topical bromfenac, including a case of toxic epidermal necrolysis (PMID 38734855) and bilateral corneal melting/perforation in a patient with pre-existing tear deficiency secondary to Stevens-Johnson syndrome (PMID 17720085). These events highlight that compromised ocular surface integrity represents a significant risk factor. Additionally, the oral formulation of bromfenac was withdrawn from the US market in 1998 due to severe hepatotoxicity (PMID 17023947); however, the ophthalmic formulation has minimal systemic absorption and this risk does not apply to topical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for bromfenac in eye disease meets Level 1 criteria, with at least 6 completed Phase 3 RCTs directly evaluating its ophthalmic efficacy, a 2024 meta-analysis supporting its use as adjunct to anti-VEGF therapy in VEGF-driven maculopathies, and mechanistic evidence extending beyond COX inhibition to include anti-fibrotic and neuroprotective pathways. The primary barrier to Canadian use is regulatory — no DIN exists — rather than a lack of clinical evidence.

**To proceed, the following is needed:**
- **Regulatory pathway:** Submit a New Drug Submission (NDS) to Health Canada to obtain DIN registration; reference US FDA approvals and Phase 3 data packages as the primary regulatory basis
- **MOA documentation:** Retrieve full mechanism of action data from DrugBank API (DG002, currently High-severity data gap)
- **Canadian prescribing information:** Obtain TFDA/Health Canada-equivalent package insert including complete contraindications, warnings, and drug-drug interaction profile (DG001, currently Blocking data gap)
- **Risk management plan:** Develop a formal monitoring strategy for high-risk populations — particularly patients with dry eye disease, autoimmune ocular surface conditions (Sjögren syndrome, SJS), or prior corneal compromise — given rare but serious adverse events documented in post-marketing surveillance
- **Indication prioritization:** Given the breadth of the "eye disease" prediction, prioritize the most commercially and clinically actionable sub-indications: (1) CME prevention post-cataract surgery, (2) diabetic macular edema as anti-VEGF adjunct, and (3) allergic conjunctivitis — all supported by Phase 2–4 data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

