# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）。
本站照 UsTxGNN 的試做版建立，規則與程式都在本 repo，頁面文字用英文、依據是加拿大衛生部藥品資料庫（Health Canada Drug Product Database, DPD）。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁「## Review Log」表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/catxgnn/regulatory/page_format.py` | 頁首＝Quick Overview「Evidence Level」格的**第一個**等級（主預測）。2026-11-12 實測本站現有頁面全部是這個規則（第一個等級跟格內最高等級不同的頁也照第一個），照實寫成程式；Tw 是整格取最高，本站不同 |
| 撤回預測 | `src/catxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/ca_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/catxgnn/regulatory/licenses.py` | 快照存事實層與本藥號碼；gate 依快照驗市場段落的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包的許可證紀錄目前沒有適應症文字時，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 許可證修正時直接刪掉的矛盾子句（10-31 d8e822621、11-05 49c7cb708／dee6df88f／343992d0e（補回整句刪除時連帶刪掉的簡介）、11-06 5b78f0c9d／bfbb2d149），2026-11-12 由 scripts/reviews_from_edits.py 依 git 前後版本轉入。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 858 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Detailed mechanism of action data is not available in the data compiled for this report.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `ca-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：「According to the … section of the US FDA-approved prescribing information for <藥>: "…" ([DailyMed: …](…), label version …; accessed …)」。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 2026-11-19 結果：747 頁寫入紀錄（美國仿單 687、ChEMBL 60），111 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 8 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）35 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Approved use: Not recorded in the local data」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：DIN（marketed／dormant）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacept「Approved use: Not recorded in the local data」→「In Canada: 2 DINs (2 marketed)」；2026-11-19 改了 437 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site CaTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數由程式產生（2026-11-24）

用戶 2026-11-24 決定（各站「許可證張數與狀態不再每週過期」）：每週許可證排程只改概覽表狀態列／張數列，市場段落的 AI 自由格式許可證表（表頭多是「DIN | Product Name | Dosage Form | Approved Indication」、兩欄全是「Not specified」，只列前 5 筆）與正文寫死的張數會跟著 Health Canada DPD 過期、讓 checker 擋整頁；改成程式產生、每週自動同步。
- A. 程式許可證表：`scripts/sync_license_tables.py`。「## Canada Market Information」段落的第一張許可證表換成程式依證據包（tfda.records＝DPD 的 DIN）產生的表
  「| DIN | Product Name | Active Ingredients (DPD) | Status |」：列＝證據包全部紀錄（收集器最多 20 筆），排序 Marketed→Approved／Dormant→Cancelled、同狀態依 DIN；品名、成分照 DPD 原文；
  狀態照 DPD STATUS 原文寫法（MARKETED→Marketed、DORMANT→Dormant、CANCELLED POST MARKET→Cancelled post market…）。表後一句來源（SOURCE；不寫「marketed」字樣，免得 checker M3 當成正文上市說法——第一版寫了「not currently marketed」，checker 誤中 956 頁）；
  證據包只收到部分 DIN（total_matches 大於紀錄數或事實層 partial）時另一句 PART_NOTE；沒有紀錄時一句 NONE_LINE。前後 `<!-- licenses:begin -->`／`<!-- licenses:end -->`；段落沒有表時放在段落開頭，沒有市場段落的頁（公開頁 3 頁）不加。
  快照 `snapshots/ca_licenses.json.gz` 存 rows／show（build_license_snapshot.py 用 program_rows）；gate 第 18 項（src/catxgnn/regulatory/licenses.py）擋「市場段落沒有程式區塊」「程式區塊≠快照重算」。
  每週排程由 `scripts/license_adapter.py` 的 `sync_tables`（--bundles，所有頁比對、只寫有變的）重排，`PAGE_NOTE` 讓 3b 自我檢查放行程式區塊的非表格行；`apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 結尾（不給 --ws 時只跑這步與 B）也會跑。
  第一次換表（`--migrate`）一併拿掉市場段落裡只講舊表列了幾筆的整句與句尾子句（字詞白名單 CAP_WORDS 判斷，例「The first five are listed below.」「…; the five above are shown.」「These are 5 of 9 valid authorizations」），查核紀錄更正文字所在的句子不動。
- B. 正文張數程式改寫：`scripts/rewrite_license_counts.py`＋`src/catxgnn/regulatory/count_prose.py`（照 Kr／My／DE 移植，英文句型：「N valid licences」「N DINs」「N of M … are valid」「Eight licences are valid in Canada」「Of the N DINs, M are valid」）；
  有效數同時接受 MARKETED 與 MARKETED＋DORMANT（DORMANT 法律上仍有效，同 checker LEGAL_NM_VALID）。有保留、講查詢、相對數、劑型／品牌／複方子集、講表格顯示筆數、待辦條目、partial 頁不動；
  單方張數（single-ingredient）跟事實不符的不改（本站 11-06 慣例是刪「single-ingredient」字樣、checker 以總數比）、跨過 1（單複數）、both、全稱與「none cancelled」前提不符的不改，列待查。gate 第 22 項擋「再跑一次會變」。
- 2026-11-24 第一次套用（資料 data-20261112-154112）：程式表 970 頁（公開頁 929：AI 表 925 頁換掉、段落裡沒有表的 4 頁補上；noindex 41 頁）；拿掉舊表說明句／子句 224 處；正文張數改寫 0 句（頁面跟快照一致；試跑時唯一要改的 efavirenz「Eight valid single-entity」是單方張數，改成照上面規則不改、列待查）；
  被取代的表上沒有錨著的查核紀錄（superseded 0 筆）。待查清單加 28 項：舊表說明句 26 句（查核紀錄更正文字 18 句、句子同時講別的事 8 句，例 acebutolol「Only the first five are listed here; the sixth is APO-ACEBUTOLOL」）、B 判斷不了 2 句。
  另寫的寬偵測（正文 DIN 張數／狀態跟事實層不符或仍講表上筆數）139 句→71 句；剩下多是「另外還有某幾張」的補充句（Two further authorizations … are also valid）、部分紀錄頁的「at least 20 … may be partial」、以及上面列待查的說明句。
  checker 全量前後都是 0；gate exit 0。last_modified_at：程式表改到的 970 頁改 2026-11-24。
- 母目錄 `.claude/license_labels/CaTxGNN.json` 目前只有「Valid」：程式表寫的狀態字 Marketed（valid）、Dormant（not_marketed）、Cancelled post market（cancelled）沒有對應，排程 lts.apply 會略過這些格（由 sync_tables 重排），要在母目錄補上。

## 許可證張數與舊表說法的第二輪查核（2026-11-24）

用戶 2026-11-24 決定（第二輪，各站同日）：第一輪（市場段落換成程式許可證表、正文張數由程式改寫）列進待查的句子，以及查核紀錄更正文字裡寫死的張數，逐句寫查核紀錄處理；更正文字不寫死張數，改指向概覽表與程式表。資料：Release data-20261112-154112、快照 snapshots/ca_licenses.json.gz（2026-11-24）。
- 查核紀錄更正文字裡的張數／舊表筆數（「Twelve valid licenses exist in total; the five above are shown.」等）：99 筆同 id 重發，換成「The table above/below lists each DIN with its current status in the DPD.」或保留品名等非張數內容的寫法（例 insulin_aspart、serine、lactic_acid）；前版存 history（reason：程式許可證表／正文張數改由程式維護）。atropine 的紀錄更正文字裡「so those columns are left blank」一併拿掉（同 id 重發）。
- `scripts/reviews_from_edits.py` 的 `figures()` 說明樣板改成不寫數字（「The Quick Overview and the table under Canada Market Information show the current number and status of DINs.」）；說明裡寫死「The DPD lists N DINs for this drug, N marketed」的 31 筆另同 id 重發（只改說明）。
- 舊表（只列 5 筆）的相對說法：市場段落「A sixth authorization … is also valid」「The remaining N are …」「Only the first five are listed here」「(5 of 6 … shown)」等 81 句寫新紀錄（`ca-lic-20261124b-*`）：只列舉不在舊表上的 DIN 的句子刪除（52 句，程式表已列出證據包全部 DIN 與現行狀態），描述其餘產品類型的句子改成「The licences also include …」、拿掉數字（29 句）；第一輪拿掉舊表說明句前半後留下的半句「None is cancelled.」4 句刪除；描述舊表欄位（「so those columns are left blank」「the table shows only the DIN and product name」等）4 處刪除。
- 單方標籤錯誤（正文寫 single-ingredient／single-entity 而證據包成分欄為複方）：18 句以 `ca-lic-20261124b-*` 更正（efavirenz「Eight valid single-entity」→單方與 efavirenz/emtricitabine/tenofovir 複方並存；valine、alanine、histidine 等胺基酸與 clavulanic_acid、doxylamine、levodopa、polymyxin_b 全為複方；sacubitril 的 ENTRESTO 是與 valsartan 的複方等），部分收錄頁另以 data/raw 的 DPD 2026-03 全量檔確認沒有單方 DIN。
- 劑型說法（項目 2）：本站證據包沒有劑型欄，改用 DPD 全量檔（data/raw/form.txt、route.txt，2026-03）逐 DIN 對照全站公開頁的劑型／給藥途徑句；不成立的 3 句更正（cromoglicic_acid 的「eye drop and a nasal product」實為眼藥水與口服膠囊 NALCROM、ciclesonide「an inhaled product」另有鼻噴劑、potassium_chloride「all injectable or infusion products」另有血液透析用產品且含複方），其餘（「marketed in Canada as an injectable」「the only Canadian product is an injection」等）逐句對過成立、不改。
- 待查清單 11-24 新增的 28 項全部處理、標 resolved（附 record_ids）；剩 open 的 111 項都是作用機轉待查。
- 缺表的頁（項目 3）：公開頁裡市場段落沒有程式表的只有 almotriptan、carboplatin、anastrozole 3 頁，它們整頁沒有市場段落，照第一波站的做法不加。
- 驗證：checker 全量前後都是 0；gate exit 0；`rewrite_license_counts.py --check` 0 頁待改；另寫的寬偵測（舊表相對字樣、紀錄更正文字裡的張數）複查，剩下的是不含數字的「Other licences include …」、表外說明（例 latanoprost「listed in the data as single entries」）與 B 管得到的張數句。

## 整頁沒有市場段落的公開頁補程式表（2026-11-24 第三輪）

用戶 2026-11-24 第三輪決定（比照 JpTxGNN 第二輪的 `add_section`）：公開頁（非 noindex、非轉址）整頁沒有「## Canada Market Information」、但證據包有 DIN 紀錄的，補段落與程式表。
- `scripts/sync_license_tables.py` 的 `add_section`：放在「## Safety Considerations」之前（沒有就 Conclusion and Next Steps、再沒有就 Disclaimer）；表與表下說明照 program_block；noindex 頁、沒有紀錄的頁不補。
  apply_drug_reviews.py、build_license_snapshot.py 結尾與每週排程 sync_tables 都會跑；`PAGE_NOTE` 放行補的段落標題行。
- gate 第 18 項（`src/catxgnn/regulatory/licenses.py` 第 5 條）：公開頁快照有程式表列、卻整頁沒有市場段落就擋。
- 2026-11-24 全量量測 3 頁、補 3 頁：almotriptan（6 個 DIN）、carboplatin（3 個）、anastrozole（19 個，1 個 dormant）；三頁正文的市場說法（「currently marketed in Canada」等）跟事實層一致，沒有新紀錄。checker 全量前後都是 0；gate exit 0。

## 第五輪：收錯的藥排除表、adapter 存成分（2026-11-25）

用戶 2026-11-25 第五輪決定（本站做第 1、3 條）：
- 1. 收錯的藥排除並接進排程：`collectors/cafda.py` 依 drug_mapping.csv 的 DrugBank ID 收 DIN，drug_mapping 把 SODIUM LACTATE、SODIUM GLUCONATE 對到 DB09395（Sodium acetate）、把各種 ANTIHEMOPHILIC FACTOR 對到 DB09109（Turoctocog alfa），別的藥被收進本藥證據包。
  比照 CHTxGNN 第三輪：`config/bundle_record_exclusions.json`（每條附 reason、basis；成分欄＝DPD active ingredient、「;」分隔，有一段符合 family、沒有一段符合 keep 就排除）、`src/catxgnn/regulatory/record_exclusions.py`、`scripts/exclude_mismatched_records.py`
  （移到 tfda.excluded_records 附 excluded／excluded_reason／excluded_basis；total_matches 扣收集器全部比對結果裡被排除的 DIN、扣過的記在 tfda.excluded_ids；存下的不到 20 筆時照收集器同一規則與排序補回、記 source／added，狀態取 data/raw/dpd_current_status.json；可重複執行）。
  收集器 `search()` 照同一份表不收（新增 `matches()`、`excluded()`）；`.github/workflows/license-refresh.yml` 在 license_refresh 前跑，有移出或扣數就照常發新 Release。
  全量量測：DPD API（health-products.canada.ca/api/drug，58,480 個產品的成分）對全部證據包的收集器比對結果 18,404 筆（含沒存的）逐筆看本藥名在不在成分裡，對不到的 222 組逐組判讀；另列 drug_mapping 同一 DrugBank ID 底下不同成分名的 41 個 ID。
  確認收錯的只有上面兩個 DrugBank ID（4 條規則、5 個證據包）：turoctocog_alfa 移出 14 筆（KOVALTRY、OBIZUR、HUMATE-P、ELOCTATE、ADYNOVATE；total 34→6，剩 ZONOVATE 6 張 Dormant）、sodium_acetate 與 sodium_acetate_trihydrate 各移出 16 筆（乳酸林格氏液、DIANEAL／BALANCE、GLYCEROLYTE 57；total 53→23，各補回 16 筆含醋酸鈉產品）、sodium_gluconate 移出 19 筆（53→3）、sodium_lactate 移出 4 筆（醋酸鈉注射液、ISOLYTE S、TPN ELECTROLYTES；53→30）；合計移出 69 筆、扣 161 個 DIN、補回 38 筆。
  不收的（同分子的鹽、酯、前驅藥或 INN／USAN 寫法）：diclofenac sodium／potassium 對 diclofenac_diethylamine、norethindrone／acetate 對 norethindrone_enanthate、somatropin、ursodiol、rifampin、pramoxine、tetrahydrozoline、L-／DL- 胺基酸、維生素別名等；antihemophilic_factor（沒有頁）裡的 ZONOVATE 屬同一類別名稱，照收。
  公開頁 2 頁：turoctocog_alfa 概覽列（Marketed→Approved but not marketed、張數 6）、程式表由程式同步，正文 3 句以 `ca-lic-20261125-turoctocog_alfa-1`～`-3` 更正（「20 valid single-ingredient licences」、說表上有其他品牌的 Note、待辦只拿掉已解決的前提）；sodium_acetate 程式表重排，「20 張全部單方」以 `ca-lic-20261125-sodium_acetate-1` 更正（多為複方，不寫數字）。其他 3 個證據包沒有藥物頁；證據包 local_regulatory 重算 2 個。
- 3. adapter 存成分：`scripts/license_adapter.py` 的 fetch() 每筆另存 drug_code、class、brand、ingredients、forms、routes、company（萃取檔 drug／ingred／form／route／comp），Release 的 data/raw/dpd_current_status.json 帶著成分；
  萃取檔下載失敗時改用 DPD API（同一資料庫；狀態轉大寫寫法、set 依狀態歸類）。2026-11-25 從雲端用 requests 下載萃取檔成功（curl 走 HTTP/2 會被斷，requests 正常），58,216 筆、狀態跟上次 Release 一致，0 個 DIN 沒有成分；API 試抓 58,480 筆也通過 validate。
  漏收重量（照原收集規則：現行 allfiles 人用 DIN 的成分去括號後對 drug_mapping 標準化成分→DrugBank ID，跟證據包 DrugBank ID 相交、不在收集器比對結果裡）：477 個 DIN 不在 2026-03 的萃取檔，其中 412 個對得到 DrugBank ID，
  缺口 271 個證據包、707 次（有頁面 157 個，例 acetaminophen 16、guanfacine 12、metformin 11、aripiprazole 7、rivaroxaban 7）；超過 50 個證據包，照用戶規則先停下回報，沒有接補收。
- 驗證：exclude 第二次跑 0 筆；checker 全量前後 0；gate exit 0；apply --check、rewrite_license_counts --check、sync_license_tables --check 都 0。證據包與 data/raw 經 data-overlay 推進 Release。

## 第六輪：DPD 新上市 DIN 依原收集規則補收（2026-11-25）

用戶 2026-11-25 第六輪決定（第 1 條「新許可補收：全部照原規則補」）：第五輪量測 271 個證據包、707 次漏收（2026-03 萃取檔之後才上市的 DIN 不在 drug_mapping、也不在 data/raw 萃取檔，每週排程只更新既有 DIN 的狀態）。
- `scripts/add_current_dins.py [--download] [--dry-run] [--report out.tsv]`（比照 ES／CH 的 add_current_licenses.py）：
  收集規則逐包判定——照現行 drug_mapping.csv 與 drug_mapping.csv.bak_20261012（那一版 DIN 前導 0 被吃掉，補回 8 位數比對）分別在 2026-03 萃取檔重算 cafda.matches（扣排除表），
  張數等於 total_matches、現有紀錄都在裡面的那份就是它的規則（兩份都對用現行），記在 tfda.collection_rule；1,552 個證據包全部重算得出（現行 1,541、只有 bak 對得上 11），停損 0 包。
  當時算進 total_matches 卻因 20 筆上限沒存的 DIN 回填 tfda.records_not_stored（235 個證據包），避免重複計數。
  補收範圍照原收集器：現行清單（data/raw/dpd_current_status.json）set＝allfiles、class＝Human、不在 2026-03 萃取檔的 DIN（2026-11-25：477 個，全部 MARKETED）；
  成分照 loader 寫法（去重排序、「; 」連接），同一原始成分字串在該份 drug_mapping 見過就沿用其 DrugBank ID（當時 failed 的照舊不收），沒見過的照 map_fda_drugs_to_drugbank 逐成分對
  （成分名在該份 drug_mapping 的標準化成分見過就沿用，含 rescue 補救的對照，否則 drugbank_mapper），跟本藥 ID 相交才收；原收集器退回文字比對的證據包照 _text_match；排除表照舊不收。
  records 未滿 20 存進 records（單方在前），滿了只記 records_not_stored，都算進 total_matches；每筆記 source（萃取檔日期與規則）、added。只加不刪、可重複執行。
  `.github/workflows/license-refresh.yml` 在 Exclude mismatched records 之後、license_refresh 之前以 `--download` 跑（失敗只印出、不擋排程），有補收就照常發新 Release。
- 2026-11-25 套用（Release data-20261125-010637）：266 個證據包補 702 筆（不重複 DIN 407 個；477 個新 DIN 裡 70 個對不到任何證據包）；第二次跑 0 筆。
  補到的類別都是原規則本來就收的人用藥（DPD class Human）：多種維生素／礦物質複方逐成分歸屬（26 個證據包）、感冒藥複方、透析液／輸液、防曬成分（homosalate、octinoxate 等，DPD 列為人用藥）等；沒有獸用、消毒劑（DPD 另分 class），沒有判定為別的藥的。
  另有少數 DIN 號碼較舊、2026-03 時不在 allfiles（例 APO-BIMATOPROST RC 02403013），現在列為 MARKETED，照同一規則收。
  證據包 local_regulatory 重算 86 個；概覽狀態列／張數列 85 頁、程式表 84 頁、description 42 頁由程式同步，正文張數 B 改寫 10 頁；部分收錄頁 235→241（例 guanfacine 補收後超過 20 筆）。
- 正文跟新事實矛盾的 22 句以 22 筆 `ca-lic-20261125b-*` 更正（更正文字不寫張數，指向概覽表與程式表）：checker M3 12 句（B 不改的單方張數句，例 galantamine「12 valid single-ingredient」→新增 GALANTAMINE ER 3 張、
  aflibercept「Ten licences」→新增 EYDENZELT）、另寫的寬偵測（改到的 266 頁正文、數字只符合舊事實層而不符合新事實層的句子）再找到 bimatoprost「All four」、maraviroc「Both」、dexrazoxane「Both」、
  oxcarbazepine「All six」、ezetimibe、zolmitriptan、guanfacine 等 6 句，待辦條目 4 句（emicizumab、oxcarbazepine、ranolazine、sotalol 的「for the four DINs」等，只拿掉張數，ranolazine 一併拿掉「CORZYNA」前提）。
  寬偵測複查：舊事實層數字句剩 0（pembrolizumab 2 句是作用機轉節錄裡的數字，誤中）；其餘命中是試驗、文獻、交互作用與節錄裡的數字。正文有變的 85 頁 last_modified_at 改 2026-11-25。
- 驗證：checker 全量前後 0（中途 M3 12 → 0）、row-status 0；gate exit 0；apply --check、rewrite_license_counts --check、sync_license_tables --check 0；add_current_dins、exclude_mismatched_records 第二次跑 0 筆。證據包與 data/raw 經 data-overlay 推進 Release。
- 另：repo 根目錄未追蹤的 `._data`（macOS AppleDouble 殘留檔）已刪。
