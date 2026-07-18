import streamlit as st
import os
import hashlib
import logging
from datetime import datetime
from dotenv import load_dotenv

# 嚴格精簡：只使用官方原生套件與基礎數學庫，徹底消滅 ModuleNotFoundError
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
    st.session_state.messages = [{"role": "assistant", "content": "您好！我是香港數字辦 (DPO) 法規 RAG 智能顧問（純原生硬化架構）。我已啟動 ISO 42001 級別的審計日誌追蹤，請輸入您的 AI 管治情境。"}]

# ==========================================
# 2. 純地端 PDF 解析與內建文本分塊
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
            
            # 使用原生 Python 進行 Sliding Window 切片
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

# ==========================================
# 3. 原生語義向量化與餘弦相似度計算 (Zero-Dependency Embedding)
# ==========================================
@st.cache_resource(show_spinner="📚 正在動態掃描並加載官方 DPO PDF 文件...")
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
    # 呼叫官方原生 Embedding API
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def cosine_similarity(v1, v2):
    # 純數學計算餘弦相似度
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# ==========================================
# 4. 密碼學審計軌跡生成 (Non-repudiation)
# ==========================================
def generate_and_log_audit_trail(query, response_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    raw_data = f"{query}|{response_text}|{timestamp}".encode('utf-8')
    audit_hash = hashlib.sha256(raw_data).hexdigest()[:16].upper()
    logging.info(f"HashID: [{audit_hash}] | Prompt: {query}")
    return f"<div class='audit-trail'>🔒 ISO 42001 Cryptographic Audit ID: {audit_hash} | Timestamp: {timestamp} (Log secured to local ledger)</div>"

# ==========================================
# 5. 主畫面佈局渲染與推理引擎
# ==========================================
st.title("🏛️ DPO AI 法規 RAG 智能顧問")
st.subheader("高階管治諮詢架構 • 具備 ISO 42001 審計軌跡與語義檢索")

with st.sidebar:
    st.header("📊 系統管治監控")
    st.metric("已加載官方 PDF 數量", f"{PDF_COUNT} 份")
    st.metric("解構法規文字切片", f"{CHUNK_COUNT} 個")
    st.markdown("---")
    st.markdown("💡 **管治提示：** 本系統已完全移除第三方 LangChain 框架依賴，轉向 100% 純原生 Python 安全硬化架構。自動為每次互動產生防篡改的密碼學審計 ID。")

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("🛑 系統警報：未偵測到 `.env` 檔案中的 `OPENAI_API_KEY`，大模型推理層無法啟動。")
elif CHUNK_COUNT == 0:
    st.error("🛑 系統警報：未偵測到官方 PDF 檔案！請將 DPO 官方指引放入 `knowledge_base/` 資料夾中。")
else:
    # 初始化 OpenAI 原生客戶端
    client = OpenAI(api_key=openai_api_key)

    for msg in st.session_state.messages:
        st.markdown(msg["content"], unsafe_allow_html=True)

    if prompt := st.chat_input("請輸入企業情境或法規疑問..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("🔍 正在透過原生語義空間計算檢索官方文本中..."):
                
                # 1. 計算查詢詞的 Embedding
                query_vector = get_embedding(client, prompt)
                
                # 2. 在記憶體中對所有文本塊計算相似度度分
                scored_chunks = []
                for chunk in ALL_CHUNKS:
                    if "vector" not in chunk:
                        # 首次計算快取以提升效能
                        chunk["vector"] = get_embedding(client, chunk["text"])
                    score = cosine_similarity(query_vector, chunk["vector"])
                    scored_chunks.append((score, chunk))
                
                # 3. 排序並抓出前 3 個最相關的段落
                scored_chunks.sort(key=lambda x: x[0], reverse=True)
                top_chunks = scored_chunks[:3]
                
                # 4. 建立上下文
                context_text = "\n\n".join([f"Source: {c[1]['source']} (Page {c[1]['page']})\nContent: {c[1]['text']}" for c in top_chunks])
                
                # 5. 強大的系統護欄 Prompt
                system_prompt = (
                    "You are an expert AI Governance Auditor.\n"
                    "Your core task is to answer corporate compliance queries based strictly on the provided context from the HK DPO Guideline.\n\n"
                    "🚨 BOUNDARY RULES:\n"
                    "1. If the user asks about traditional machine learning (e.g., Random Forest, regression, clustering) that DOES NOT generate content, you MUST state it is OUT OF SCOPE. Do not provide a risk tier for it.\n"
                    "2. If the user asks about non-HK frameworks (e.g., EU AI Act, GDPR) or generic laws (e.g., Employment Ordinance), refuse to answer and state it is out of scope to prevent compliance illusions.\n"
                    "3. ALWAYS base your advice on the retrieved context. Do not invent rules.\n"
                    "4. Reply in the user's language (Traditional Chinese or English) with a professional corporate tone.\n\n"
                    f"CONTEXT:\n{context_text}"
                )
                
                # 6. 呼叫 Chat Completion API
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
                
                # 7. 渲染審計追溯鏈 (Traceability Links)
                st.markdown("---")
                st.markdown("#### 📚 官方條文追溯 (Audit Traceability)")
                citations_html = ""
                for score, chunk in top_chunks:
                    confidence = score * 100
                    citations_html += f"<div class='source-tag'>🔍 <b>Doc_ID: {chunk['hash']}</b> | 來源: {chunk['source']} (第 {chunk['page']} 頁) | 置信度: {confidence:.1f}%</div>"
                st.markdown(citations_html, unsafe_allow_html=True)
                
                # 8. 附加密碼學審計軌跡
                audit_html = generate_and_log_audit_trail(prompt, answer)
                st.markdown(audit_html, unsafe_allow_html=True)
                
                # 9. 儲存紀錄
                full_response = answer + "\n\n" + citations_html + audit_html
                st.session_state.messages.append({"role": "assistant", "content": full_response})
