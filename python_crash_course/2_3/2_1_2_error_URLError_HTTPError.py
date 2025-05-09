#处理异常。如果网络不好，出现异常。urllib库中的error模块集成自OSError类。 由request模块产生异常的都可以通过捕获这个类处理
#具有属性reason，返回错误的原因。
#URLError
# from urllib import request, error
# try:
#     response = request.urlopen("https://cuiqingcai.com/404") #打开一个不存在的页面，按理应该报错，但是捕获了URLError这个异常
#     #运行结果如下：程序没有直接报错，而是输出了错误原因，这样可以避免程序异常终止，同时异常得到了有效处理
# except error.URLError as e:
#     print(e.reason)

#HTTPError是URLError子类
# from urllib import request, error
#
# try:
#     response = request.urlopen("https://cuiqingcai.com/404")
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep="\n")

#上述代码更好的写法：先捕获子类即HTTP的错误，再捕获父类即URL的错误。
from urllib import request, error
# try:
#     response = request.urlopen("https://cuiqingcai.com/404")
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep="\n") #先捕获HTTPError，获取错误原因，状态吗，请求头等信息。
# except error.URLError as e: #如果不是HTTP异常，就会补货URL异常，输出错误原因。
#     print(e.reason)
# else: #最后用else语句来处理正常的逻辑。
#     print("Request Successfully")

#有时候reason 属性 返回的不一定是字符串，也可能是一个对象。再看下面的实例
from urllib import request, error
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen("https://www.baidu.com", timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout): #reason属性返回的不一定是字符串，也可能是一个对象
        print("TIME OUT")
