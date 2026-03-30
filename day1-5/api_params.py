import requests

# 基础 URL
base_url = "https://jsonplaceholder.typicode.com/posts"

# 参数：只获取 userId = 1 的文章
params = {
    "userId": 1
}

response = requests.get(base_url, params=params)

print("状态码:", response.status_code)
print("请求的完整 URL:", response.url)  # 可以看到参数自动拼接到 URL 后

if response.status_code == 200:
    data = response.json()
    print(f"获取到 {len(data)} 篇文章（userId=1）")
    if data:
        print("第一篇文章标题:", data[0]['title'])
else:
    print("请求失败")