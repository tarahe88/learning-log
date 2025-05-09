#requests库除了 get 和 post。 高级用法如下：

#文件上传
# import requests
# files = {"file": open("favicon.ico", "rb")} #前面我们保存了一个文件favicon.ico.逐一要和当前脚本保存在同一目录下。
# r = requests.post("https://www.httpbin.org/post", files=files)
# print(r.text)

# #设置cookie
# import requests
# r = requests.get("https://www.baidu.com")
# print(r.cookies) #调用cookie 手法娴熟于requescookiejar后调用items方法
# for key, value  in r.cookies.items(): # items方法转化为由元组组成的列表
#     print(key + "=" + value)

# #用cookie来维持登陆状态，以github为例
# import requests
# headers = {
#     "Cookie": "_gh_sess=2ZdWmRuhlTQZ3tjToYDlCi0XuUSG5FGPljmTjDOBrj0docnmacDIoOEofEJGQnpuKJ93LJo2BPZEDx9qy9BqjVcyflmaUwrkDRUIocq%2B9rBzk8%2FGjmg9To3hbs0JAKfGHFTMDWKO2RDdxBzwAqwNXpW%2F06VhIE9r5tGGNDXaLmwzbwF331%2BY%2B5OkPOD1F7Mmqy%2BBFwEjh0DtRUvKdaRAXeNTMB9PRvRILAN1CTXvIbLhHKMYesYopmZ7xNDsMhlCqAKinmAOC%2FdneBsdb7pIu1E8EuYxYw3H8gzZl7IEzlyrjT7ftInbiFq%2FRbHF8u1%2BMlAeVACI%2FPjVU8kMPB0OpjeA7w%2Bzvb1OSSv%2FaGrSfl3jiDeHo3xyjLnnRqZZL%2FGPHsrh%2Fw3F4IKiTjDlk1y7aAbun6Ks4MGXwHEZFdsR2PmwBM3nBI95VxWn2r%2FKvn%2FkCA4T%2BsXRqisYxpOYM9jevz7yHCaEjjjzgqwug5DJzHvAD3DK94bRWDCy7xDJyDnfJyqdTjvU2fBsEhY4nshqzJUIwxh4lJk3ZcNYtSK5Axhg%2B1MpxPhDtqLLYtErX8IY8Wa1rlQDadGxjzFigIdC9nsulM7NGF0s6KyA5uYJNs9DZ9DiPQfwI1fAmDUigwE3v98NyBwT6O0CLKy9zLHZww2DOMzwQwPjp0FUoIbxtM4DNsMPfxhoxQkqqL%2FVe8HUS1LQMrcJoFcGoeH%2BaSOY5ldiSy9W8bUkmwLxh7yNIm1zo6rN3Ib0awcCoJ6bWjQP6isXVrx9PTpyS0NcjUUNj6IdriocY7YxO3hxGgJJ5fvkgRn4nXFRbcXu4OnLuGNjJ9NctQzNnqt6pJfuAjDeRFWU8YGJl0nD--oYUKDYBy1HeqlrhN--pjsEDnRMmXWafPyoydMqKg%3D%3D; path=/; secure; HttpOnly; SameSite=Lax"
# } #我自己在github上的cookie
# r = requests.get("https://github.com/", headers=headers)
# print(r.text) #运行结果是包含了登陆后才能包含的结果 也就是能爬取登陆之后才能看到的页面

# # session. 维持同一个session。第二次请求打开的是浏览器选项卡而非新的浏览器。
# import requests
# s = requests.Session()
# s.get("https://www.httpbin.org/cookies/set/number/123456789") #请求测试网址，设置了cookie条目名称是number,内容是123456
# r = s.get("https://www.httpbin.org/cookies") #随后请求，以获取当前的cookie信息
# print(r.text) # "cookies": {"number": "123456789"}

# # ssl证书验证。如果有些网站的HTTPS没有验证，或者没有被CA认可。
# import requests
# import logging #忽视警告的话需要import logging
# logging.captureWarnings(True) #忽视警告的话需要用
# response = requests.get("https://ssr2.scrape.center/", verify=False) #用verify参数控制是否验证证书。False为不验证
# print(response.status_code) #200

# #超时设置，timeout
# import requests
# r = requests.get("https://www.httpbin.org/get", timeout=1) #超过设置的时间就会抛出异常
# print(r.status_code) #200
# r = requests.get("https://www.httpbin.org/get", timeout=None) #永久等待就设置None或者不写timeout
# # r = requests.get("https://www.httpbin.org/get") #永久等待不写timeout
# print(r.status_code) #200
#
# #身份认证 auth. requests自带基本身份认证.
# import requests
# from requests.auth import HTTPBasicAuth
# r = requests.get("https://ssr3.scrape.center/", auth=HTTPBasicAuth("admin", "admin")) #默认用户名密码都是admin
# print(r.status_code)

# #OAuth认证方式 需要安装oauth包
# import requests
# from requests_oauthlib import OAuth1
#
# url = "https://api.twitter.com/1.1/account/verify_credentials.json"
# auth = OAuth1("YOUR_APP_KEY", "YOUR_APP_SECRET"
#               "USER_OAUTH_TOKEN", "USER_OAUTH_TOKEN_SECRET")
# requests.get(url, auth=auth) #这个不成功，可能是因为是twitter

#代理设置 proxies
#http代理
import requests
proxies = {"https": "http://user:password@10.10.10.10:1080/"}
requests.get("https://www.httpbin.org/get",proxies=proxies)

#sockets协议代理。安装socks库
import requests
proxies = {
    "http" : "socks5://user:password@host:port",
    "https": "socks5://user:password@host:port"
}
requests.get("https://www.httpbin.org/get", proxies=proxies)