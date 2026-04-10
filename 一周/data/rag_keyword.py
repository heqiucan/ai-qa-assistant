import re
import os
import dashscope
from dashscope import Generation


dashscope.api_key = os.getenv("DASHSCOPE_API_KEY", "YOUR_API_KEY")


# 请替换成你的真实Key

def load_document(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def split_paragraphs(text):
    return [p.strip() for p in text.split('\n\n') if p.strip()]

def extract_keywords(question):
    words = re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]+', question)
    return [w for w in words if len(w) > 1]

def retrieve_paragraph(paragraphs, keywords):
    best_para = None
    best_score = -1
    for para in paragraphs:
        score = sum(para.count(kw) for kw in keywords)
        if score > best_score and score > 0:
            best_score = score
            best_para = para
    return best_para, best_score

def ask_llm(question, context):
    if not context:
        return "未找到相关信息。"
    prompt = f"根据以下内容回答问题：\n\n{context}\n\n问题：{question}\n\n答案："
    messages = [{'role': 'user', 'content': prompt}]
    try:
        response = Generation.call(
            model='qwen-turbo',
            messages=messages,
            result_format='message'
        )
        if response.status_code == 200:
            return response.output.choices[0].message.content
        else:
            return f"API错误: {response.message}"
    except Exception as e:
        return f"调用失败: {e}"