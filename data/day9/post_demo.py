import requests
# 要发送的数据
data = {
    "message":"我是何秋灿，正在学习POST请求",
    "date": "2025-03-25",
    "hobby":"编程"
}
# 发送 POST 请求
response = requests.post("https://httpbin.org/post", json=data)
# 打印状态码
print("状态码:", response.status_code)
# 打印返回的原始文本（看看服务器回了什么）
print("返回原始文本:", response.text)
if response.status_code == 200:
    result = response.json()
    print("解析后的 json 字段:", result["json"])
    # httpbin 会把我们发送的 JSON 放在 'json' 字段里
    sent_back = result.get("json")
    print("服务器返回的数据:", sent_back)
    if sent_back == data:
        print("✅ 成功！服务器收到了我发送的数据")
    else:
        print("❌ 数据不一致")
else:
    print("请求失败")