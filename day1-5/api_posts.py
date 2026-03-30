import requests
url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
print("状态码：",response.status_code)
if response.status_code==200:
    data=response.json()
    print("总获取到",len(data),"篇文章")
    first_post_title=data[0]["title"]
    print("第一篇文章的标题：",first_post_title)
else:
    print("请求失败")