# LINE Bot + Gemini API 整合

這是一個使用 FastAPI 建立的 LINE Bot,整合了 Google Gemini API 來回應使用者訊息。

## 功能特色

- ✅ 接收 LINE 使用者的訊息
- ✅ 使用 Gemini AI 生成智慧回應
- ✅ 自動回覆給 LINE 使用者
- ✅ 完整的錯誤處理和日誌記錄

## 安裝步驟

### 1. 安裝必要套件

```bash
uv pip install fastapi uvicorn python-dotenv line-bot-sdk google-genai
```

### 2. 設定環境變數

在專案根目錄的 `.env` 檔案中設定以下變數:

```
GEMINI_API_KEY=你的_GEMINI_API_KEY
LINE_CHANNEL_ACCESS_TOKEN=你的_LINE_CHANNEL_ACCESS_TOKEN
LINE_CHANNEL_SECRET=你的_LINE_CHANNEL_SECRET
```

### 3. 取得 LINE Bot 憑證

1. 前往 [LINE Developers Console](https://developers.line.biz/)
2. 建立新的 Provider (如果還沒有)
3. 建立新的 Messaging API Channel
4. 在 Channel 設定中找到:
   - **Channel Access Token** (長期)
   - **Channel Secret**
5. 將這些資訊填入 `.env` 檔案

### 4. 設定 Webhook URL

在 LINE Developers Console 中:
1. 進入你的 Messaging API Channel
2. 找到 "Webhook settings"
3. 設定 Webhook URL: `https://你的網域/webhook`
4. 啟用 "Use webhook"
5. 關閉 "Auto-reply messages" (如果不需要)

## 執行程式

```bash
python pratice1.py
```

或使用 uv:

```bash
uv run python pratice1.py
```

程式會在 `http://0.0.0.0:8000` 啟動

## 測試

1. 開啟瀏覽器訪問 `http://localhost:8000` 查看首頁
2. 在 LINE 中加入你的 Bot 為好友
3. 傳送訊息給 Bot
4. Bot 會使用 Gemini AI 生成回應並回覆給你

## 程式架構

```
pratice1.py
├── 載入環境變數和初始化
├── FastAPI 應用程式
├── chat_with_gemini() - Gemini API 呼叫
├── handle_text_message() - LINE 訊息處理
├── line_webhook() - Webhook 端點
└── 主程式啟動
```

## Gemini 模型設定

目前使用的模型: `gemini-2.0-flash-exp`
- Temperature: 0.7 (可調整創意程度)

你可以修改 `chat_with_gemini()` 函式中的參數來調整 AI 的行為。

## 日誌記錄

程式會記錄:
- 收到的使用者訊息
- Gemini 的回覆內容
- 錯誤訊息

## 注意事項

⚠️ **重要**: 
- 確保你的伺服器有公開的 HTTPS URL (LINE 要求使用 HTTPS)
- 建議使用 ngrok 或其他服務來建立 HTTPS 通道進行測試
- 不要將 `.env` 檔案提交到版本控制系統

## ngrok 測試範例

```bash
# 啟動 ngrok
ngrok http 8000

# 將 ngrok 提供的 HTTPS URL 設定到 LINE Webhook
# 例如: https://abc123.ngrok.io/webhook
```

## 故障排除

### 問題: Webhook 收不到訊息
- 檢查 LINE Webhook URL 是否正確設定
- 確認 Webhook 已啟用
- 查看日誌確認是否有錯誤訊息

### 問題: 簽章驗證失敗
- 確認 `LINE_CHANNEL_SECRET` 設定正確
- 檢查是否有多餘的空格或換行

### 問題: Gemini API 錯誤
- 確認 `GEMINI_API_KEY` 有效
- 檢查 API 配額是否已用完
- 查看錯誤日誌獲取詳細資訊

## 參考資料

- [LINE Messaging API 文件](https://developers.line.biz/en/docs/messaging-api/)
- [Google Gemini API 文件](https://ai.google.dev/docs)
- [FastAPI 文件](https://fastapi.tiangolo.com/)
