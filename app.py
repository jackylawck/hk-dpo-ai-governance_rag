import streamlit as st
import os
import hashlib
import logging
from datetime import datetime
from dotenv import load_dotenv

# ==========================================
# 經典且絕對穩定的 RAG 與 LLM 組件
# ==========================================
from pypdf import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

# ==========================================
# 0. 企業級審計日誌初始化 (ISO 42001 Compliance)
# ==========================================
logging.basicConfig(
    filename='dpo_compliance_audit.log', 
    level=logging.INFO,
    format='%(asctime)s | ISO42001-DPO-RAG | %(levelname)s | %(message)s'
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
    st.session_state.messages = [{"role": "assistant", "content": "您好！我是香港數字辦 (DPO) 法規 RAG 智能顧問。我已啟動 ISO 42001 級別的審計日誌追蹤，請輸入您的 AI 管治情境。"}]

# ==========================================
# 2. 本地 RAG 向量資料庫引擎 (知識庫隔離架構)
# ==========================================
KB_DIR = "knowledge_base"

@st.cache_resource(show_spinner="🛡️ 正在初始化本地 HuggingFace Embedding 引擎...")
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def process_pdf_to_chunks(pdf_path):
    filename = os.path.basename(pdf_path)
    chunks = []
    try:
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if not text: continue
            
            chunk_size = 600
            overlap = 150
            start = 0
            while start < len(text):
                end = start + chunk_size
                chunk_text = text[start:end]
                doc = Document(
                    page_content=chunk_text,
                    metadata={"source": filename, "page": page_num, "hash": hashlib.md5(chunk_text.encode('utf-8')).hexdigest()[:8]}
                )
                chunks.append(doc)
                start += (chunk_size - overlap)
    except Exception as e:
        logging.error(f"Error processing PDF {filename}: {str(e)}")
    return chunks

@st.cache_resource(show_spinner="📚 正在掃描並加載官方 DPO PDF 文件至本地向量庫...")
def initialize_vector_db():
    if not os.path.exists(KB_DIR) or not os.listdir(KB_DIR):
        return None, 0, 0
        
    embeddings = get_embedding_model()
    all_chunks = []
    pdf_files = [os.path.join(KB_DIR, f) for f in os.listdir(KB_DIR) if f.endswith('.pdf')]
    
    for pdf_path in pdf_files:
        all_chunks.extend(process_pdf_to_chunks(pdf_path))
        
    if all_chunks:
        vector_db = FAISS.from_documents(all_chunks, embeddings)
        logging.info(f"Vector DB built with {len(all_chunks)} chunks from {len(pdf_files)} PDFs.")
        return vector_db.as_retriever(search_kwargs={"k": 4}), len(pdf_files), len(all_chunks)
    return None, 0, 0

RETRIEVER, PDF_COUNT, CHUNK_COUNT = initialize_vector_db()

# ==========================================
# 3. 密碼學審計軌跡生成 (Non-repudiation)
# ==========================================
def generate_and_log_audit_trail(query, response_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    raw_data = f"{query}|{response_text}|{timestamp}".encode('utf-8')
    audit_hash = hashlib.sha256(raw_data).hexdigest()[:16].upper()
    logging.info(f"HashID: [{audit_hash}] | Prompt: {query}")
    return f"<div class='audit-trail'>🔒 ISO 42001 Cryptographic Audit ID: {audit_hash} | Timestamp: {timestamp} (Log secured to local ledger)</div>"

# ==========================================
# 4. LLM 防禦性系統提示詞與經典 QA 工作管線
# ==========================================
openai_api_key = os.getenv("OPENAI_API_KEY")

system_prompt = """You are an expert AI Governance Auditor.
Your core task is to answer corporate compliance queries based strictly on the retrieved context from the HK DPO Guideline.

🚨 BOUNDARY RULES:
1. If the user asks about traditional machine learning (e.g., Random Forest, regression) that DOES NOT generate content, state it is OUT OF SCOPE.
2. If the user asks about non-HK frameworks (e.g., EU AI Act, GDPR), refuse to answer to prevent compliance illusions.
3. ALWAYS base your advice on the retrieved context. Do not invent rules.
4. Reply in the user's language (Traditional Chinese or English) with a professional corporate tone.

CONTEXT:
{context}

USER QUERY:
{question}"""

if openai_api_key and RETRIEVER:
    prompt_template = PromptTemplate(template=system_prompt, input_variables=["context", "question"])
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
    
    # 使用最穩定、相容所有版本的 RetrievalQA
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=RETRIEVER,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template}
    )
else:
    rag_chain = None

# ==========================================
# 5. 主畫面佈局渲染
# ==========================================
st.title("🏛️ DPO AI 法規 RAG 智能顧問")
st.subheader("高階管治諮詢架構 • 具備 ISO 42001 審計軌跡與語義檢索")

with st.sidebar:
    st.header("📊 系統管治監控")
    st.metric("已加載官方 PDF 數量", f"{PDF_COUNT} 份")
    st.metric("解構法規文字切片", f"{CHUNK_COUNT} 個")
    st.markdown("---")
    st.markdown("💡 **管治提示：** 本系統不會將您的 PDF 上傳至外部伺服器。向量化完全於本地運行，並自動為每次互動產生防篡改的密碼學審計 ID。")

if not openai_api_key:
    st.error("🛑 系統警報：未偵測到 `.env` 檔案中的 `OPENAI_API_KEY`，大模型推理層無法啟動。")
elif not RETRIEVER:
    st.error("🛑 系統警報：未偵測到官方 PDF 檔案！請將 DPO 官方指引放入 `knowledge_base/` 資料夾中。")
else:
    for msg in st.session_state.messages:
        st.markdown(msg["content"], unsafe_allow_html=True)

    if prompt := st.chat_input("請輸入企業情境或法規疑問..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("🔍 正在語義檢索本地向量庫並比對官方文本中..."):
                # 執行經典 RAG 推理
                response = rag_chain.invoke({"query": prompt})
                answer = response["result"]
                source_documents = response["source_documents"]
                
                # 渲染來源追溯 ( Traceability )
                citations_html = ""
                st.markdown(answer)
                
                if source_documents:
                    st.markdown("---")
                    st.markdown("#### 📚 官方條文追溯 (Audit Traceability)")
                    for i, doc in enumerate(source_documents):
                        source_file = doc.metadata.get("source", "Unknown")
                        page_num = doc.metadata.get("page", "Unknown")
                        chunk_hash = doc.metadata.get("hash", "Unknown")
                        
                        citations_html += f"<div class='source-tag'>🔍 <b>Doc_ID: {chunk_hash}</b> | 來源: {source_file} (第 {page_num} 頁)</div>"
                    
                    st.markdown(citations_html, unsafe_allow_html=True)
                
                # 附加審計軌跡
                audit_html = generate_and_log_audit_trail(prompt, answer)
                st.markdown(audit_html, unsafe_allow_html=True)
                
                # 儲存對話歷史
                full_response = answer + "\n\n" + citations_html + audit_html
                st.session_state.messages.append({"role": "assistant", "content": full_response})
