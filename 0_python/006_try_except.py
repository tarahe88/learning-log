'''
在编写爬虫时，异常处理是非常重要的，因为网络请求、文件操作、数据处理等过程中可能会遇到各种不可预见的问题。
使用 try-except 语句可以帮助你捕获和处理这些异常，确保程序在出现错误时不会崩溃，并且能够优雅地处理错误情况
'''
# 1. 基本语法。 try-except语句的基本语法如下；
try:
    #可能会引发异常的代码
    risky_code()
except SomeException as e:
    #处理异常的代码
    handle_exception(e)
# try块中包含可能会引发异常的代码
# except块用于捕获并处理异常。 SomeException是你想要捕获的异常类型, as e 是将异常对象赋值给变量e，以便在except块中使用。
# 2. 捕获特定异常。你可以捕获特定的异常类型，并针对不同的异常类型进行不同的处理。
try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"Caught as exception:{e}")
# 3. 捕获多个异常。 你可以使用多个except块来捕获不同类型的异常
try:
    #可能会引发异常的代码
    risk_code()
except ZeroDivisionError as e:
    print(f"Caught as exception:{e}")
except FileNotFoundError as e:
    print(f"Caught a FileNotFoundError:{e}")
except Exception as e:
    print(f"Caught an unexpected exception:{e}")
# 4.捕获所有异常。使用呢Exception类，是所有内置异常的基类
try:
    # 可能会引发异常的代码
    risky_code()
except Exception as e:
    print(f"Caught an exception:{e}")
# 5. else 和 finally 块
# else 块：如果try块中的代码没有引发任何异常，else块中的代码将会执行。
# finally块：无论是否发生异常，finally块中的代码都会执行，通常用于释放资源或清理操作
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"Caught an exception:{e}")
else:
    print(f"Result is {result}")
finally:
    print("This will always execute")
# 6. 自定义异常。 你可以通过继承Exception类来创建自定义异常
class MyCustomError(Exception):
    pass
try:
    raise MyCustomError("Something went wrong")
except MyCustomError as e:
    print(f"Caught a custom exception:{e}")
# 7. 爬虫中的异常处理示例。在爬虫中，常见异常包括网络请求失败，解析错误，文件操作错误等。以下是简单的爬虫示例。
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
try:
    # 发送网络请求
    response = requests.get(url)
    response.raise_for_status() # 如果响应状态码不是200，抛出HTTPError
except requests.exceptions.RequestException as e:
    print(f"Network request failed:{e}")
else:
    try:
        # 解析  HTML 内容
        soup = BeautifulSoup(response.text,'html.parser')
        title = soup.title.string
    except AttributeError as e:
        print(f"Failed to parse HTML:{e}")
    else:
        try:
            # 将结果写入为难
            with open('output.txt','w') as file:
                file.write(title)
        except IOError as e:
            print(f"Failed to write to file:{e}")
        else:
            print("Sucessfully wrote the title to output.txt")
finally:
    print("Crawling process completed")
'''
8. 练习
编写一个简单的爬虫程序，尝试访问一个不存在的 URL，并使用 try-except 捕获和处理 requests.exceptions.RequestException。
修改程序，使其在解析 HTML 时捕获 AttributeError，并输出友好的错误信息。
添加 finally 块，确保在程序结束时输出“爬取过程结束”。'''