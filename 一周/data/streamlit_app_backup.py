import streamlit as st

st.set_page_config(page_title="测试", layout="wide")

st.sidebar.title("侧边栏测试")
st.sidebar.write("如果你能看到这行字，说明侧边栏工作正常。")

st.title("文档问答助手（测试版）")
st.write("侧边栏已显示，新功能可用。")