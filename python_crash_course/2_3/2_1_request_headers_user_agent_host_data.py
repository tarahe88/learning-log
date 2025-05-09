from urllib import request, parse
url = "http://www.httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "host": "www.httpbin.org"
}
dict={"name": "germey"}
data = bytes(parse.urlencode(dict),encoding = "utf-8")
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))