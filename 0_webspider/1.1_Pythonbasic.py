#Python 是学习爬虫的利器，掌握基础语法和常用库是关键。
#作为新手学习爬虫，掌握Python基础语法是第一步。以下是需要掌握的关键内容：
## 1 变量与数据类型。 001 理解变量的定义与使用。 002掌握常见类型如整数，浮点数，字符串，布尔值
x = 10
name = "Alice"
is_student = True
## 2 控制结构 001 条件语句：if, elif, else 循环语句：for 和 while循环
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
for i in range(5):
    print(i)
## 3 函数 001定义与调用：使用def定义函数。 002参数与返回值： 理解如何传递参数和返回值
def greet(name):
    return f"Hello, {name}"
print(greet("Alice"))
## 4 列表与字典 001列表：掌握列表的创建访问修改和常用操作。 002字典：理解字典的键值对结构及其基本操作。
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

person = {"name": "Alice", "age": 25}
print(person["name"])
## 5 文件操作。读写操作：掌握文件的打开，读取，写入和关闭
with open ("file.text","r") as file:
    content = file.read()
    print(content)
## 6 异常处理 try-except:捕获和处理异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
## 7 模块与库 001 导入模块：使用import 导入标准库或第三方库 002 常用库：如requests.BeautifulSoup. os等。
import requests
response = requests.get("https://www.example.com")
print(response.text)
## 8 面向对象编程（OOP) 001 类与对象：理解类的定义与对象的创建。002属性与方法：掌握类的属性和方法
class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return f"{self.name} says woof!"
my_dog = Dog("Bob")
print(my_dog.bark())
## 9正则表达式 re模块： 掌握正则表达式的基本用法，用于文本匹配。
import re
pattern = r"\d+"
text = "There are 3 apples and 5 oranges."
matches = re.findall(pattern, text)
print(matches)
## 10 网络请求. requests库： 掌握发送HTTP请求和处理响应。
import requests
response = requests.get("https://www.example.com")
print(response.status_code)
print(response.text)
## 11 数据处理 001 字符串操作：掌握字符串的常见操作，如分割，替换等. 002JSON处理：掌握JSON数据的解析与生成
import json
data = '{"name":"Alice", "age":25}'
parsed_data = json.loads(data)
print(parsed_data["name"])
## 12 虚拟环境 venv:掌握虚拟环境的创建与管理，隔离项目依赖。
# python -m venv myenv
# source myenv/bin/activate #On Windows:myenv\Scripts\activate





