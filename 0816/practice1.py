# 匯入 Google Gemini AI 套件
from google import genai
# 匯入 dotenv 套件，用來讀取 .env 檔案中的環境變數
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數（例如 API 金鑰）
load_dotenv()

# 建立 Gemini AI 客戶端，會自動從環境變數讀取 API 金鑰
client = genai.Client()

# 建立一次對話互動，指定模型與輸入問題
interaction = client.interactions.create(
    model="gemini-3.5-flash",  # 使用 gemini-3.5-flash 模型
    input="天空為什麼是藍的"   # 輸入的問題
)

# 輸出 AI 回覆的文字內容
print(interaction.output_text)
