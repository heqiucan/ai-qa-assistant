import streamlit as st
import os
from rag_keyword import split_paragraphs, extract_keywords, retrieve_paragraph, ask_llm

st.set_page_config(page_title="文档问答助手", page_icon="📚", layout="wide")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #2c3e50; text-align: center; margin-bottom: 1rem; }
    .sub-header { text-align: center; color: #7f8c8d; margin-bottom: 2rem; }
    .stButton > button { background-color: #4CAF50; color: white; border-radius: 8px; padding: 0.5rem 1rem; font-weight: bold; }
    .stButton > button:hover { background-color: #45a049; }
    .success-box { padding: 1rem; border-radius: 10px; background-color: #e8f5e9; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📚 文档问答助手</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">基于关键词检索 + 通义千问 | 上传你的知识库，立即提问</div>', unsafe_allow_html=True)


@st.cache_resource
def load_default_knowledge():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "knowledge.txt")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return split_paragraphs(content)
    except FileNotFoundError:
        return None


if "paragraphs" not in st.session_state:
    st.session_state.paragraphs = load_default_knowledge()
if "source_name" not in st.session_state:
    st.session_state.source_name = "默认知识库 (knowledge.txt)"
if "question" not in st.session_state:
    st.session_state.question = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.markdown("## 📂 知识库")
    uploaded_file = st.file_uploader("上传你的 .txt 文件", type=["txt"])
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        st.session_state.paragraphs = split_paragraphs(content)
        st.session_state.source_name = f"上传的文件: {uploaded_file.name}"
        st.success(f"✅ 已切换至 {uploaded_file.name}")
        st.rerun()
    else:
        if st.button("🔄 重置为默认知识库"):
            st.session_state.paragraphs = load_default_knowledge()
            st.session_state.source_name = "默认知识库 (knowledge.txt)"
            st.success("已恢复默认知识库")
            st.rerun()

    st.markdown("---")
    st.markdown("## 💡 示例问题")
    example_questions = [
        "什么是RAG？",
        "大语言模型的训练过程包括哪些步骤？",
        "Python有哪些应用？",
        "多模态融合是什么？"
    ]
    for q in example_questions:
        if st.button(q, key=q):
            st.session_state.question = q
            st.rerun()

    st.markdown("---")
    st.markdown("### 📌 当前知识库")
    st.info(st.session_state.source_name)

    if st.button("🗑️ 清空对话历史"):
        st.session_state.messages = []
        st.rerun()

if st.session_state.paragraphs is None:
    st.error("❌ 知识库加载失败，请检查默认文件或上传有效文件。")
    st.stop()

with st.container():
    st.markdown(f'<div class="success-box">✅ 知识库已加载，共 {len(st.session_state.paragraphs)} 个段落。</div>',
                unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("请输入你的问题"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("🔎 正在检索并生成答案..."):
            keywords = extract_keywords(prompt)
            best_para, score = retrieve_paragraph(st.session_state.paragraphs, keywords)
            if best_para:
                answer = ask_llm(prompt, best_para)
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                with st.expander("📖 查看相关段落"):
                    st.write(best_para)
            else:
                error_msg = "未找到相关段落，请尝试换个问法。"
                st.write(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

st.markdown("---")
st.markdown("💡 提示：你可以上传自己的txt文件作为临时知识库，或点击示例问题快速测试。")