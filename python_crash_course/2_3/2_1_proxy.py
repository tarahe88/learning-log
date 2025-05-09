#事先在本地搭建一个代理，让其运行在8080端口上
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({ #参数是字典，键名是协议名，值是代理连接，可以添加多个代理
    "http":"http://127.0.0.1:8080",
    "https" : "https://127.0.0.1:8080"
})
opener=build_opener(proxy_handler)
try:
    response = opener.open("https:www.baidu.com")
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)

