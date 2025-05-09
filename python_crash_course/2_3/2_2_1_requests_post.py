# post 请求
# import requests
# data = {
#     "name": "pony",
#     "age" : "30"
# }
# r = requests.post("https://www.httpbin.org/post", data = data) #httpbin网站可以判断请求是否为post方式，如果是，则返回相应请求信息
# print(r.text)

#响应。 上面的实例，使用text和content获取了响应的内容给。
#此外，还有很多属性和方法来获取其他信息。 例如状态码，响应头，cookie等
import requests
r = requests.get("https://ssr1.scrape.center/")
print(type(r.status_code), r.status_code) #<class 'int'> 200 状态码
print(type(r.headers), r.headers) #<class 'requests.structures.CaseInsensitiveDict'> 响应头
print(type(r.cookies), r.cookies) #<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[]>
print(type(r.url),r.url) #<class 'str'> https://ssr1.scrape.center/ #url链接
print(type(r.history), r.history) #<class 'list'> [] #请求历史

# requests.codes 内置状态码查询对象
import requests
r = requests.get("https://ssr1.scrape.center/")
exit() if not r.status_code == requests.codes.ok else print("Requests Successfully") #Requests Successfully