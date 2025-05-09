import socket        #timeout是服务器响应时间
import urllib.error
import urllib.request
try:
    response = urllib.request.urlopen("http://www.httpbin.org//get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):  #socket.timeout超时异常
        print("TIMEOUT")

print("时间间隔为1s，如果是0.1s就容易报错")
import urllib.request
response = urllib.request.urlopen("http://www.httpbin.org//get", timeout=1)
print(response.read())
