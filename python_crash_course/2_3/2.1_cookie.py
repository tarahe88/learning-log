#获取网站cookie
#先声明一个cookiejar对象，后利用httpcookieprocessor构建一个handler,后利用build_opener方法构建opener，执行open函数
# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://wwww.baidu.com")
# for item in cookie:
#     print(item.name+"=" +item.value)

#生成cookie.txt文件 见左侧栏并保存为Mozilla型浏览器的格式
# import urllib.request, http.cookiejar
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# """MozillaCookieJar是CookieJar的子类，生成文件时用到。可以读取和保存Cookie.
# 可以将Cookie保存成Mozilla型浏览器的Cookie格式"""
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True) #Netscape HTTP Cookie File

#LWPCookieJar将Cookie文件格式保存为LWP(libwww-perl)格式
# import urllib.request, http.cookiejar
# filename = "cookie.txt"
# cookie = http.cookiejar.LWPCookieJar(filename) #将cookie保存为LWPCookie格式了
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True) #LWP-Cookies-2.0

#生成cookie后，读取内容加以利用.以LWPCookieJar格式为例看下
import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar() #首先生成了LWPCookie格式的Cookie并保存文件
cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True) #调用load方法读取本地Cookie文件，获取cookie内容
handler = urllib.request.HTTPCookieProcessor(cookie) #读取之后，使用同样的方法构建handler类opener类
opener = urllib.request.build_opener(handler) #读取之后，使用同样的方法构建opener类
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8")) #运行成功后，输出百度网页的源代码
