---
layout: default
title: Hexaminolevulinate
parent: 中證據等級 (L3-L4)
nav_order: 380
evidence_level: L3
indication_count: 10
---

# Hexaminolevulinate
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Hexaminolevulinate：從膀胱癌螢光診斷到大腸贅生病灶偵測

> **候選篩選說明**：本 Evidence Pack 提供 TxGNN 對 Hexaminolevulinate（HAL）的 10 項預測適應症，但僅有 **Colonic Neoplasm（大腸贅生病灶）** 具備實質臨床試驗證據（Decision Stage S1）。排名第一的 bronchitis（支氣管炎，分數 0.9906）雖分數最高，但模型自身的機轉推論已明確標註為「TxGNN 圖譜雜訊或間接節點連結造成之偽陽性」且無任何臨床或文獻證據，不建議進一步調查。因此本報告以 Colonic Neoplasm 作為主要評估標的，其餘 8 項低證據候選整理於文末附表供參考。

## 一句話總結

> Hexaminolevulinate（HAL）為一種螢光顯影劑，其核准用途為透過膀胱鏡進行光動力診斷（PDD）以偵測膀胱癌病灶。
> TxGNN 模型預測其可能適用於 **大腸贅生病灶（Colonic Neoplasm）** 之螢光內視鏡偵測，
> 目前有 **3 件相關臨床試驗**（其中 1 件已完成，收案 38 人）支持此方向，惟尚無支持性文獻報告。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 膀胱癌螢光顯影診斷（來自證據中之機轉描述；正式仿單/適應症紀錄尚缺，見 DG002） |
| 預測新適應症 | Colonic Neoplasm（大腸贅生病灶） |
| TxGNN 預測分數 | 98.64% |
| 證據等級 | L3 |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 DrugBank 尚未提供完整的作用機轉（MOA）資料（資料缺口 DG002，嚴重度 High）。根據證據包中 repurposing_rationale 提供的機轉描述：HAL 為原紫質 IX（PpIX）之前驅物，投予後會在快速增生/贅生組織中選擇性蓄積，經藍光激發後產生紅色螢光，藉此輔助內視鏡下病灶偵測——此即其核准之膀胱鏡光動力診斷（PDD）機轉原理。

大腸贅生病灶與膀胱癌雖屬不同器官系統，但兩者在病理生理上有共通點：皆屬上皮性快速增生/贅生組織，理論上同樣具備 PpIX 選擇性蓄積的螢光顯影特性。因此，將 HAL 由「膀胱鏡螢光診斷」延伸至「大腸內視鏡螢光診斷」，在機轉上屬於「同一診斷平台、不同偵測部位」的合理外推，而非全新藥理機轉的假設，機轉關聯性相對強。

值得注意的是，這是一個**診斷用途的擴展**，而非治療用途的老藥新用——HAL 本身並非抗腫瘤治療藥物，其潛在新適應症價值在於「輔助偵測」而非「治療」大腸贅生病灶，這點在後續安全性與臨床定位評估時需特別區分。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00285701](https://clinicaltrials.gov/study/NCT00285701) | Phase 1/2 | 已完成 | 38 | 局部/口服給予 HAL 於大腸鏡檢查前致敏，藍光激發可使息肉與腫瘤產生紅色螢光，提升病灶偵測率；並測試不同劑量以找出最佳顯影條件與耐受性 |
| [NCT01344902](https://clinicaltrials.gov/study/NCT01344902) | Phase 1/2 | 已終止 | 13 | 開放式劑量摸索研究，評估口服 HAL 螢光技術於疑似/高風險大腸贅生病人之偵測效果；因收案僅 13 人即終止，結果解讀有限 |
| [NCT03272659](https://clinicaltrials.gov/study/NCT03272659) | Phase 2 | 已撤回（招募失敗，收案 0 人） | 0 | 原規劃評估術前化放療後大腸直腸癌手術檢體病理與光動力螢光相關性（HAL 灌腸致敏），因招募失敗撤回，無實質數據產出 |

---

## 文獻證據

目前無相關文獻可供參考。

---

## 台灣市場資訊

Hexaminolevulinate 目前**未於台灣上市**，無許可證核發紀錄（total_licenses = 0）。

---

## 安全性考量

請參閱藥品仿單以獲取安全性資訊。

*（資料缺口 DG001：TFDA 仿單警語/禁忌尚未取得，嚴重度為 Blocking，此為進入 S1 安全性初評前必須補齊的項目。）*

---

## 結論與下一步

**決策建議：Hold**

**理由：**
現有證據僅為 Phase 1/2 早期概念驗證等級（1 件完成、1 件因收案不足終止、1 件招募失敗撤回），尚無 Phase 3 隨機對照試驗或已發表文獻佐證；同時關鍵的安全性仿單資料（DG001，Blocking）與正式作用機轉紀錄（DG002，High）皆為缺口，尚不足以支持進入下一階段評估。

**若要繼續推進，需要補齊：**
- TFDA 仿單警語/禁忌資料（DG001，Blocking，須下載並解析官方仿單 PDF）
- 經 DrugBank API 查證之正式作用機轉（MOA）紀錄（DG002）
- 針對大腸贅生病灶偵測之更大規模、完整收案的 Phase 2/3 臨床試驗
- 獨立同儕審查文獻以佐證現有臨床試驗發現
- 內視鏡給藥途徑（灌腸/口服）與現行大腸鏡設備相容性評估

---

## 附表：其他 TxGNN 預測候選（暫不推進）

以下 8 項候選皆缺乏臨床試驗或文獻證據支持（Decision Stage S0），模型機轉推論亦判定關聯性薄弱或屬圖譜雜訊，暫不建議進一步調查：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 主要判斷理由 |
|------|------|-----------|---------|------|-------------|
| 1 | Bronchitis | 99.06% | L5 | Hold | 與 HAL 螢光顯影機轉完全無關，極可能為偽陽性 |
| 3 | Severe nonproliferative diabetic retinopathy | 98.60% | L5 | Hold | 病理機轉（微血管病變）與贅生組織螢光偵測無直接關聯 |
| 4 | Cecum villous adenoma | 98.43% | L4 | Hold | 與大腸贅生病灶同光譜，僅能間接類推，無直接證據 |
| 5 | Rectosigmoid junction neoplasm | 98.43% | L4 | Hold | 同上，僅能類推，無直接試驗或文獻 |
| 6 | Cecum neuroendocrine tumor G1 | 98.43% | L5 | Hold | 神經內分泌腫瘤增生特性不同，機轉延伸屬推測 |
| 7 | Colonic lymphangioma | 98.43% | L5 | Hold | 非上皮性贅生病灶，機轉相關性薄弱 |
| 8 | Lipoma of colon | 98.43% | L5 | Hold | 間葉組織來源良性腫瘤，機轉不匹配 |
| 9 | Cecal disease | 98.42% | L5 | Hold | 疾病定義過於籠統，無法建立明確機轉關聯 |
| 10 | Cavernous hemangioma of colon | 98.42% | L5 | Hold | 血管畸形病灶，非增生性組織，機轉不匹配 |

---

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

