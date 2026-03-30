import requests
url="https://httpbin.org/get"
response=requests.get(url)
print("状态码：",response.status_code)
print("原始文本：",response.text)
if response.status_code==200:
    data=response.json()
    print("解析后的字典",data)
    print("请求的URL是：",data["url"])
else:
    print("请求失败")