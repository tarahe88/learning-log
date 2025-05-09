# 1 requests库比urllib更强大方便。
#urllib.urlopen = requests.get。
# import requests
# r = requests.get("https://www.baidu.com/")
# print(type(r)) #<class 'requests.models.Response'>
# print(r.status_code) #200
# print(type(r.text)) #<class 'str'>
# print(r.text[:100])  #虽然是str类型，但是是json格式的。 解析返回结果，得到json格式的数据，调用json方法
# print(r.cookies)

# # 2 requests库方便之处在于其他请求类型依然可以用一句话完成。
# import requests
# r = requests.get("https://www.baidu.com/")
# r = requests.post("https://www.baidu.com/post")
# r = requests.put("https://www.baidu.com/put")
# r = requests.delete("https://www.baidu.com/delete")
# r = requests.patch("https://www.baidu.com/patch")

# ##3.Get请求
# import requests
# r = requests.get("https://www.httpbin.org/get") #httpbin网站判断客户端发起的是否是get请求，是返回相应的请求信息
# print(r.text)

# #get请求增加额外的信息
# import requests
# data = {
#     "name": "pony",
#     "age": "30"
# }
# r = requests.get("https://www.httpbin.org/get", params = data) #将信息以字典形式传给get方法的params参数
# print(r.text)

# #调用json方法将get获取的json格式的i富川转化为字典
# import requests
# r = requests.get("https://www.httpbin.org/get")
# print(type(r.text)) #<class 'str'>
# print(r.json()) #用json方法将json格式变成字典形式
# print(type(r.json())) #<class 'dict'>

# # 抓取网页，实际返回的是html文件。加点提取信息的逻辑。
# import requests
# import re
# r = requests.get("https://ssr1.scrape.center/")
# pattern = re.compile("<h2.*?>(.*?)</h2>",re.S) #用最基本的正则表达式匹配所有的标题
# titles = re.findall(pattern,r.text)
# print(titles)
#
# # 抓取二进制数据比如图片，音频，视频。
# import requests
# r = requests.get("https://scrape.center/favicon.ico")
# print(r.text) #出现了乱码，因为图片是二进制转为str字符串会出现乱码
# print(r.content) #bytes类型的数据

# 将刚才提取到的信息保存下来。
import requests
r = requests.get("https://scrape.center/favicon.ico")
with open("../../other/favicon.ico", "wb") as f: #open方法，第一个是文件名称，第2个参数代表以二进制写的形式打开文件
    f.write(r.content) #向上述文件写入二进制 #这个小图片就被我们保存下来了，左侧有个“favicon.ico"的文件

# 添加请求头
import requests
headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
r = requests.get("https://scrape.center", headers = headers)
print(r.text)