import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({"name": "pony"}),encoding="utf-8") #data数据必须是bytes类型
response = urllib.request.urlopen("http://www.httpbin.org/post", data = data) #https不行，要http
print(response.read().decode("utf-8"))