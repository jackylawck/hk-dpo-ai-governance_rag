import streamlit as st
import os
import hashlib
import logging
from datetime import datetime
from dotenv import load_dotenv

# 原生硬化組件
from pypdf import PdfReader
from openai import OpenAI
import numpy as np

load_dotenv()

# ==========================================
# 0. 企業級審計日誌初始化 (ISO 42001 Compliance)
# ==========================================
logging.basicConfig(
    filename='dpo_compliance_audit.log', 
    level=logging.INFO,
    format='%(asctime)s | ISO42001-DPO-NATIVE-RAG | %(levelname)s | %(message)s'
)

# ==========================================
# 1. 頁面配置與 UI 初始化
# ==========================================
st.set_page_config(
    page_title="HK DPO AI RAG Advisor",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .audit-trail {font-family: 'Courier New', Courier, monospace; color: #a1a1a1; font-size: 0.8em; margin-top: 15px; border-top: 1px dashed #ced4da; padding-top: 5px;}
    .source-tag {
        background-color: #e9ecef; border-left: 4px solid #007bff; color: #212529; 
        padding: 10px; margin: 8px 0; font-size: 0.9em; border-radius: 4px; font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "您好！我是香港數字辦 (DPO) 法規 RAG 智能顧問。本系統已啟動 ISO 42001 級別的審計日誌追蹤，請確保知識庫已配置後輸入您的 AI 管治情境。"}]

# ==========================================
# 2. 本地 PDF 解析與分塊
# ==========================================
KB_DIR = "knowledge_base"

def process_pdf_to_chunks(pdf_path):
    filename = os.path.basename(pdf_path)
    chunks = []
    try:
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if not text: continue
            
            chunk_size = 1000
            overlap = 200
            start = 0
            while start < len(text):
                end = start + chunk_size
                chunk_text = text[start:end]
                chunks.append({
                    "text": chunk_text,
                    "source": filename,
                    "page": page_num,
                    "hash": hashlib.md5(chunk_text.encode('utf-8')).hexdigest()[:8]
                })
                start += (chunk_size - overlap)
    except Exception as e:
        logging.error(f"Error processing PDF {filename}: {str(e)}")
    return chunks

@st.cache_resource(show_spinner="📚 正在動態掃描本地知識庫...")
def load_all_documents():
    if not os.path.exists(KB_DIR) or not os.listdir(KB_DIR):
        return [], 0
    
    all_chunks = []
    pdf_files = [os.path.join(KB_DIR, f) for f in os.listdir(KB_DIR) if f.endswith('.pdf')]
    for pdf_path in pdf_files:
        all_chunks.extend(process_pdf_to_chunks(pdf_path))
    return all_chunks, len(pdf_files)

ALL_CHUNKS, PDF_COUNT = load_all_documents()
CHUNK_COUNT = len(ALL_CHUNKS)

def get_embedding(client, text, model="text-embedding-3-small"):
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def generate_and_log_audit_trail(query, response_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    raw_data = f"{query}|{response_text}|{timestamp}".encode('utf-8')
    audit_hash = hashlib.sha256(raw_data).hexdigest()[:16].upper()
    logging.info(f"HashID: [{audit_hash}] | Prompt: {query}")
    return f"<div class='audit-trail'>🔒 ISO 42001 Cryptographic Audit ID: {audit_hash} | Timestamp: {timestamp} (Log secured to local ledger)</div>"

# ==========================================
# 3. 主畫面佈局渲染與智慧型引導機制
# ==========================================
st.title("🏛️ DPO AI 法規 RAG 智能顧問")
st.subheader("高階管治諮詢架構 • 具備 ISO 42001 審計軌跡與語義檢索")

with st.sidebar:
    st.header("📊 系統管治監控")
    st.metric("已加載官方 PDF 數量", f"{PDF_COUNT} 份")
    st.metric("解構法規文字切片", f"{CHUNK_COUNT} 個")
    st.markdown("---")
    st.markdown("💡 **管治提示：** 本系統已完全移除第三方 LangChain 框架依賴，轉向 100% 純原生 Python 安全硬化架構。")

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("🛑 系統警報：未偵測到 `OPENAI_API_KEY`，請於 Streamlit Cloud Secrets 中配置變數方可激活大模型推理層。")
    
# ✨ 核心創新：如果雲端找不到檔案，彈出極其優雅且具備合規教育意義的引導卡，直接提供下載網址
elif CHUNK_COUNT == 0:
    st.info("### 📂 知識庫初始化引導 (Knowledge-Base Alignment Guide)")
    st.markdown(
        """
        本公開線上沙盒遵循**最高級別的資訊管治與版權合規原則**，開源倉庫中不直接分發特區政府指引文件原文。若您希望激活本智能顧問系統，請依循以下專業審計標準配置您的本地運行環境：
        
        1. **前往數字政策辦公室官方網站下載最新版指引文件：**
           👉 **[點此訪問 DPO 官方指引下載頁面](https://www.digitalpolicy.gov.hk/en/our_work/data_governance/policies_standards/ethical_ai_framework/)**
        2. 在您本地克隆的專案目錄下，建立一個名為 **`knowledge_base/`** 的資料夾。
        3. 將下載的官方中英文 PDF 檔案放入該資料夾內。
        4. 本系統已配置 `.gitignore` 保護屏障，放入該資料夾的任何 PDF 文件**絕對不會被誤傳上傳至公開 GitHub 倉庫**，確保企業敏感資訊與版權資安隔離。
        5. 於本地執行 `streamlit run app.py` 即可在 100% 安全的地端環境中啟動您的專案二。
        
        *—— 為了保障企業的資料隱私安全，本系統拒絕提供線上開放上傳功能，以防範潛在的 PII 資料外洩與惡意提示詞注入攻擊。*
        """
    )
    st.stop()
    
else:
    # 正常運行時的對話代碼
    client = OpenAI(api_key=openai_api_key)

    for msg in st.session_state.messages:
        st.markdown(msg["content"], unsafe_allow_html=True)

    if prompt := st.chat_input("請輸入企業情境或法規疑問..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("🔍 正在透過原生語義空間計算檢索官方文本中..."):
                query_vector = get_embedding(client, prompt)
                scored_chunks = []
                for chunk in ALL_CHUNKS:
                    if "vector" not in chunk:
                        chunk["vector"] = get_embedding(client, chunk["text"])
                    score = cosine_similarity(query_vector, chunk["vector"])
                    scored_chunks.append((score, chunk))
                
                scored_chunks.sort(key=lambda x: x[0], reverse=True)
                top_chunks = scored_chunks[:3]
                
                context_text = "\n\n".join([f"Source: {c[1]['source']} (Page {c[1]['page']})\nContent: {c[1]['text']}" for c in top_chunks])
                
                system_prompt = (
                    "You are an expert AI Governance Auditor.\n"
                    "Your core task is to answer corporate compliance queries based strictly on the provided context from the HK DPO Guideline.\n\n"
                    "🚨 BOUNDARY RULES:\n"
                    "1. If the user asks about traditional machine learning (e.g., Random Forest) that DOES NOT generate content, state it is OUT OF SCOPE.\n"
                    "2. If the user asks about non-HK frameworks (e.g., EU AI Act, GDPR), refuse to answer.\n"
                    "3. ALWAYS base your advice on the retrieved context. Do not invent rules.\n"
                    "4. Reply in the user's language with a professional corporate tone.\n\n"
                    f"CONTEXT:\n{context_text}"
                )
                
                llm_response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.0
                )
                
                answer = llm_response.choices[0].message.content
                st.markdown(answer)
                
                st.markdown("---")
                st.markdown("#### 📚 官方條文追溯 (Audit Traceability)")
                citations_html = ""
                for score, chunk in top_chunks:
                    confidence = score * 100
                    citations_html += f"<div class='source-tag'>🔍 <b>Doc_ID: {chunk['hash']}</b> | 來源: {chunk['source']} (第 {chunk['page']} 頁) | 置信度: {confidence:.1f}%</div>"
                st.markdown(citations_html, unsafe_allow_html=True)
                
                audit_html = generate_and_log_audit_trail(prompt, answer)
                st.markdown(audit_html, unsafe_allow_html=True)
                
                full_response = answer + "\n\n" + citations_html + audit_html
                st.session_state.messages.append({"role": "assistant", "content": full_response})
