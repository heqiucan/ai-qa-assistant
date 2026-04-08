import streamlit as st
from rag_core import load_document, split_paragraphs, extract_keywords, retrieve_paragraph, ask_llm

# 缓存加载知识库的结果
@st.cache_resource
def load_knowledge_base():
    content = load_document("knowledge.txt")
    if content:
        paragraphs = split_paragraphs(content)
        return paragraphs
    return None

st.set_page_config(page_title="文档问答助手", page_icon="📚")
st.title("📚 文档问答助手")
st.markdown("基于 `knowledge.txt` 回答问题")

paragraphs = load_knowledge_base()
if paragraphs is None:
    st.error("知识库文件 'knowledge.txt' 加载失败，请检查文件是否存在。")
    st.stop()

st.success(f"知识库加载成功，共 {len(paragraphs)} 个段落。")

question = st.text_input("请输入你的问题：")
if st.button("查询"):
    if not question:
        st.warning("请输入问题")
    else:
        with st.spinner("正在检索并生成答案..."):
            keywords = extract_keywords(question)
            best_para, score = retrieve_paragraph(paragraphs, keywords)
            if best_para:
                answer = ask_llm(question, best_para)
                st.success("答案：")
                st.write(answer)
                with st.expander("查看相关段落"):
                    st.write(best_para)
            else:
                st.error("未找到相关段落，请尝试换个问法。")