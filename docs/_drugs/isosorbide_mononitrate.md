---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate：原始適應症資料缺口 → Hypertrichosis（多毛症）

## 一句話摘要

Isosorbide mononitrate 為 NO 供體/血管擴張劑（依證據包中各候選項之機轉敘述推得），但本證據包未提供其正式核准適應症與加拿大上市資訊（藥品目前**未在加拿大上市**，0 筆 DIN）。TxGNN 模型將 **Hypertrichosis（多毛症）** 列為預測分數最高的候選適應症（99.99%），但**目前無任何臨床試驗或文獻支持**，證據包本身亦註記此分數僅反映知識圖譜嵌入的統計相似性，非藥理學推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（本證據包未提供；加拿大無上市紀錄可佐證） |
| 預測新適應症 | Hypertrichosis（多毛症） |
| TxGNN 預測分數 | 99.995%（排名 194） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 加拿大市場狀態 | 未上市 |
| DIN 數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

本證據包未收錄 Isosorbide mononitrate 的正式作用機轉描述（DG002，High severity）。但由候選項的機轉敘述可還原其藥理學背景：Isosorbide mononitrate 屬硝酸鹽類 NO 供體，經 NO-sGC-cGMP 路徑造成血管平滑肌鬆弛，臨床上此類藥物多用於心絞痛、肝門靜脈高壓等血管相關適應症（見證據包中對其他候選項的敘述，如肝硬化門脈壓力研究 PMID 3384359、2759546）。

至於 Hypertrichosis（多毛症），證據包的 `repurposing_rationale` 明確指出：「無已知機轉：Isosorbide mononitrate 為 NO 供體/血管擴張劑，與毛髮過度生長之病理機轉無已知關聯；此分數僅為 TxGNN 圖譜嵌入的統計相似性，非藥理學推論」。換句話說，這是知識圖譜排名前列，但**藥理學上缺乏合理連結**的候選項，應視為需要人工排除的雜訊候選，而非優先開發方向。

值得注意的是，同一批候選項中排名第 10 的 **Pulmonary arterial hypertension（肺動脈高壓）** 具有遠高於本候選項的證據強度（L4／S1／Research Question），因其 NO-sGC-cGMP 路徑與 PAH 病理生理直接相關，並有 6 篇相關文獻支持（含動物模式與機轉研究）。若要在本藥物的預測候選中挑選後續研究方向，PAH 會是比 Hypertrichosis 更值得推進的標的，但仍需注意其與 PDE5 抑制劑併用之嚴重低血壓禁忌。

---

## 臨床試驗證據

目前無相關已註冊之臨床試驗（Hypertrichosis 相關檢索結果為 0 筆，含 ClinicalTrials.gov 與 ICTRP）。

---

## 文獻證據

目前無相關文獻（PubMed 檢索 Isosorbide mononitrate + hypertrichosis 結果為 0 筆）。

---

## 加拿大市場資訊

Isosorbide mononitrate 目前未在加拿大上市，無 DIN 授權紀錄可列。

---

## 安全性考量

請參閱藥品仿單以取得安全性資訊（本證據包之警語、禁忌與藥物交互作用查詢皆為資料缺口，DG001 屬 Blocking 等級，將阻擋進入 S1 安全性初評）。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
TxGNN 分數雖高（99.995%），但證據包本身已明確標註此為圖譜統計相似性雜訊，缺乏任何臨床試驗、文獻或機轉合理性支持（L5／S0）；加上藥品未在加拿大上市、安全性資料存在阻斷型缺口，現階段不具備推進條件。

**若要推進，需補充：**
- TFDA／Health Canada 仿單警語與禁忌資料（DG001，Blocking，阻擋 S1 安全性初評）
- Isosorbide mononitrate 完整作用機轉（MOA）資料（DG002）
- 若欲驗證 Hypertrichosis 方向：需先取得任何體外/動物層級的機轉合理性資料，目前完全缺乏
- 建議另案評估同批次中證據等級較高的候選項（Pulmonary arterial hypertension，L4／S1），該方向機轉關聯性明確，且已有初步文獻基礎
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

