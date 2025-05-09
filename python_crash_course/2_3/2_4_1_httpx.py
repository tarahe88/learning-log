# #urllib 和 requests库不支持http/2.0
# #hyper 和 httpx 支持http2.0。
# import httpx
# response = httpx.get("https://www.httpbin.org/get")
# print(response.status_code)
# print(response.headers)
# print(response.text)

# #http2需要手动声明
# import httpx
# client = httpx.Client(http2=True) #默认使用的http/1.1，需要手动声明下才能使用http/2.0 也就是http2
# response = client.get("https://spa16.scrape.center/")
# print(response.text)

# #httpx和requests有很多相似的api，get, post, delete, put实现方法类似
# import httpx
# rg = httpx.get("https://www.httpbin.org/get") #书里有个参数params = "{"name": "germey"}" 应该是错误
# rp = httpx.post("https://www.httpbin.org/post", data={"name": "germey"})
# rpo = httpx.put("https://www.httpbin.org/put")
# rd = httpx.delete("https://www.httpbin.org/delete")
# rpa = httpx.patch("https://www.httpbin.or/patch")

# import httpx
# response = httpx.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.headers)
# print(response.text)

# #  4 client对象  可以和requests中的session类比学习。 httpx有一些基本的API和requests中的非常相似，也有一些不相似，比如client
# import httpx
# with httpx.Client() as client: #官方推荐使用方式是with as语句
#     response = client.get("https://www.httpbin.org/get")
#     print(response)
# #这个用法等价于：
# import httpx
# client = httpx.Client()
# try:
#     response = client.get("https://www.httpbin.org/get")
# finally:
#     client.close()
#
# #声明Client对象时可以制定一些参数，比如headers。 这样使用该对象发起的所有请求都会默认带上这些参数配置，比如
# import httpx
# url = "http://www.httpbin.org/headers"
# headers = {'User-Agent':'my-app/0.0.1'} #声明一个headers变量，
# with httpx.Client(headers=headers) as client: #将此变量传递给headers参数初始化一个client对象，并赋值为client变量
#     r = client.get(url) #用client变量请求了测试网站
#     print(r.json()['headers'] ['User-Agent']) #my-app/0.0.1

# # 5。支持http 2.0
# import httpx
# client = httpx.Client(http2=True)
# response = client.get("https://www.httpbin.org/get")
# print(response.text)
# print(response.http_version) #my-app/0.0.1 代表使用了http2协议。

# 6 支持异步 httpx支持async
import httpx
import asyncio
async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)
