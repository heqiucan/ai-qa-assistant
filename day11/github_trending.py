import requests
import pandas as pd   # 建议把导入放最前面

url = "https://api.github.com/search/repositories"
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 30
}
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, params=params, headers=headers)
print("状态码:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("成功获取数据！共", data["total_count"], "个仓库")

    items = data["items"]
    repos = []
    for item in items:
        repos.append({
            "name": item["name"],
            "stars": item["stargazers_count"]   # 注意字段名
        })

    print("前3个仓库：", repos[:3])

    df = pd.DataFrame(repos)
    print(df.head())

    df_sorted = df.sort_values("stars", ascending=False)
    print("\nTop 10 仓库（star数）:")
    print(df_sorted.head(10))

    df_sorted.to_csv("github_python_trending.csv", index=False, encoding="utf-8")
    print("已保存到 github_python_trending.csv")

else:
    print("请求失败:", response.text)