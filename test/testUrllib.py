import urllib.request

#获取一个get请求 -不需要登录验证的
# response = urllib.request.urlopen("http://www.baidu.com") #这里是http不是https
# print(response.read().decode("utf-8")) #对获取到的网页源码进行utf-8解码

#获取一个post请求 --错误示例，没有封装
# response = urllib.request.urlopen("http://httpbin.org/post")
# print(response.read()) #错误要封装 urllib.error.HTTPError: HTTP Error 405: METHOD NOT ALLOWED

#获取一个post请求--需要登录验证的要用post，往服务器发送一个请求
import urllib.parse #解析器
data = bytes(urllib.parse.urlencode({"username": "password"}),"utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data = data) #用post访问人家必须用人家的post封装方式，
# #封装方式就是用data传参数
# print(response.read()) #b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "hello": "world"\n  }, \n  "headers
print(response.read().decode("utf-8"))


