import urllib.request
request = urllib.request.Request("http://www.httpbin.org") #为什么书上能成功的https://python.org，我这不行
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))
#Request后面的参数 Request(URL, data=None, headers={},origin_req_host=None, unverifiable=False, method=None)URL是必传参数