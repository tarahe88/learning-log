import urllib.request
response = urllib.request.urlopen("http://www.baidu.com/") #这里是http不是https
print(response.status)
print(response.getheaders())
print(response.getheader("Server"))
print(response.getheader("date")) #我自己。p
print(response.getheader("Content-Type"))
print(response.getheader("Set-Cookie"))
print(response.msg)
print(response.version)