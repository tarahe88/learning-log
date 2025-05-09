# 学习 Python 基础语法是编程的第一步，而 变量与数据类型 是最基础也是最重要的部分
# 以下是新手学习 Python 变量与数据类型的详细指南，帮助你快速掌握这些概念。
'''
1.理解变量的定义与使用
1.1什么是变量？
    变量是用于存储数据的容器
    每个变量都有一个名称（标识符）和一个值
    变量的值可以在程序运行过程中改变
1.2 变量的命名规则
    变量名由字母，数字和下划线(_)组成
    变量名不能以数字开头
    变量名区分大小写（如name和Name是不同的变量）
    不能使用python的关键字（如if,for,while等）作为变量名
关键字有：False,None,True, and, as, assert, async, await, break, class, continue, def, del, elif, else
except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try
while, with,yield
'''
# 示例：定义变量
# 定义变量并赋值
name = "Alice"
age = 25
height = 1.68
is_student = True
# 打印变量
print(name) # 输出: Alice
print(age) # 输出: 25
print(height) # 输出: 1.68
print(is_student)# 输出: True
'''
2. 掌握常见数据类型: 
python中常见的数据类型包括：
整数(int)
浮点数（float)
字符串（str)
布尔值（bool) # 布尔值竟然是数据类型的一种。# 
列表(list)
元组(tuple)
集合(set)
字典(dict)
少一个空值类型 None 
整数、浮点数、字符串 和 布尔值 是 Python 的基础数据类型。
列表、元组、集合 和 字典 是 Python 的复合数据类型。
列表[]和元组()都是有序，元组不可变。集合{}和字典{}都是无序.集合{}无序不重复，字典{}是无序键值对
01-列表增、删、改、查。  02-元组只能查不能增删改。 03-集合：增、删和集合运算。04-字典：增、删、改、查
'''
# 2.1 整数（int）001-整数是不带小数部分的数字。 002-可以是正数，负数或零。
# 示例：整数
a = 10
b = -5
c = 0
print(type(a)) # 输出：<class 'int'>
# 2.2 浮点数(float) 001-浮点数是带小数部分的数字。 002-用于表示实数
# 示例： 浮点数
pi = 3.14159
temperature = -10.5
print(type(pi))  # 输出：<class 'float'>
# 2.3 字符串(str)  001-字符串是由字符组成的序列，用单引号(')或双引号("")包裹。002-字符串是不可变的（创建后不能修改）
name = "Alice"
greetings = "Hello,World!"
print(type(name)) # 输出： <class 'str'>
    # 字符串操作
# 字符串拼接
full_name = name + " Smith"
print(full_name) # 输出：Alice Smith
# 字符串长度
print(len(name)) # 输出: 5
# 字符串索引
print(name[0]) # 输出: A
# 字符串切片
print(name[1:4]) #输出: lic
# 2.4 布尔值(bool) 001-布尔值只有2个值： True 和 False. 002-用于表示逻辑值（真或假）
# 示例： 布尔值
is_student = True
is_adult = False
print(type(is_student)) # <class 'bool'>
    # 布尔运算
# 逻辑与
print(True and False) # 输出： False
# 逻辑或
print(True or False) # 输出： True
# 逻辑非
print(not True) # 输出: False
# 2.5 列表[list]. 001-列表是一个有序的可变序列，可以存储多个元素。 002-列表用方括号[]表示，元素之间用逗号分隔。
# 示例：列表
fruits = ["apple","banana", "cherry"]
numbers = [1,2,3,4,5]
print(type(fruits)) #<class 'list'>
    # 列表操作
# 访问元素
print(fruits[0]) # apple 索引[]只对有序序列有用，无序的没用。
# 修改元素
fruits[1] ="blueberry"
print(fruits) # 输出： ['apple', 'blueberry', 'cherry']
# 添加元素
fruits.append("orange")
print(fruits) # 输出：['apple', 'blueberry', 'cherry', 'orange']
# 删除元素
fruits.remove("cherry")
print(fruits) # 输出： ['apple', 'blueberry', 'orange']

#2.6元组(tuple) 001元组是一个有序的不可变序列，可以存储多个元素。 002元组用圆括号（）表示，元组之间用逗号分隔。
# 示例：元组
coordinates = (10.0,20.0)
colors =("red","green","blue")
print(type(coordinates)) # 输出： <class 'tuple'>
# 元组操作
# 访问元素
print(colors[1]) # 输出: green
# 元组不可修改。
## colors[1] = "yellow" # 会报错
# 2.7 集合{set} 001-集合是一个无序的不重复元素列表。 02-集合用花括号{}表示，元素之间用逗号分隔。
# 示例：集合
unique_numbers = {1,2,3,4,5}
fruits = {"apple", "banana", "cherry"}
print(type(unique_numbers)) # 输出: <class 'set'>
# 集合操作
# 添加元素
fruits.add("orange")
print(fruits) # {'banana', 'apple', 'orange', 'cherry'}
# 删除元素
fruits.remove("banana")
print(fruits) # 输出: {'apple', 'cherry', 'orange'}
# 集合运算
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2) # 并集: {1, 2, 3, 4, 5}
print(set1 & set2) # 交集: {3}

# 2.8 字典{dict}. 001-字典是一个无序的键值对集合。 002 字典用花括号{}表示，键值对用冒号:分隔
# 示例值；字典
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
print(type(person)) # <class 'dict'>
# 字典操作
# 访问值
print(person["name"]) # 输出： Alice
# 修改值
person["age"] = 26
print(person) # 输出： {'name': 'Alice', 'age': 26, 'is_student': True}
# 添加键值对
person["height"] = 1.68
print(person) # 输出： {'name': 'Alice', 'age': 26, 'is_student': True, 'height': 1.68}
# 删除键值对
del person["is_student"]
print(person)  # 输出: {'name': 'Alice', 'age': 26, 'height': 1.68}



'''
3. 数据类型转换。python提供了内置函数用于数据类型之间的转换：
int():将其他类型转换为整数。
float(): 将其他类型转换为浮点数。
str(): 将其他类型转换为字符串。
bool(): 将其他类型转换为布尔值。
'''
    # 示例： 数据类型转换
# 字符串转整数
num_str = "123"
num_int = int(num_str)
print(num_int) # 输出： 123
# 整数转字符串
num_int = 456
num_str = str(num_int)
print(num_str) # 输出： 456
# 整数转浮点数
num_int = 789
num_float = float(num_int)
print(num_float) # 输出： 789.0
# 布尔值转整数
is_true = True
num_int = int(is_true)
print(num_int) #输出 1. True是1 ， False是0
# 4.动态类型语言的特点：  001-python是动态类型语言，变量的类型由赋值决定，且可以随时改变 002-不需要显式声明变量类型。
# 示例： 动态类型
x = 10 # x 是整数
print(type(x)) # <class 'int'>
x="Hello" # x 变为字符串
print(type(x)) # <class 'int'>
'''
5. 练习与巩固。
练习1: 定义变量并输出。
定义一个字符串变量name,值为你的名字
定义一个整数变量age,值为你的年龄
定义一个浮点数变量height, 值为你的身高
定义一个布尔值变量is_student，表示你是否是学生
打印这些变量及其类型
'''
name = "Tara"
age = 28
height = 1.68
is_student = False
print(name, type(name)) # Tara <class 'str'>
print(age, type(age)) # 28 <class 'int'>
print(height,type(height)) # 1.68 <class 'float'>
print(is_student, type(is_student)) #False <class 'bool'>
'''
练习 2：数据类型转换
将字符串 "123" 转换为整数。
将整数 456 转换为字符串。
将浮点数 3.14 转换为整数。
将布尔值 True 转换为整数。
'''
num_str = "123"
num_int = int(num_str)
print(num_int,type(num_int)) # 123 <class 'int'>

num_int = 456
num_str = str(num_int)
print(num_str,type(num_str)) # 456 <class 'str'>

num_float = 3.14
num_int = int(num_float)
print(num_int,type(num_int)) # 3 <class 'int'>

is_true = True
num_int = int(is_true)
print(num_int,type(num_int)) # 1 <class 'int'>
'''
变量是存储数据的容器，通过赋值来使用。数据类型包括整数，浮点数，字符串，和布尔值。掌握数据类型转换的方法，可以灵活处理不同类型的数据
'''
# 延伸知识. 索引[]索引是编程中访问有序或映射数据结构的通用方式，理解不同数据结构中的索引操作对于高效编程非常重要。
# 索引的应用场景及代码示例：1 列表/数组索引。2.元组索引。 3.字典索引（通过键）4. NumPy数组索引。 5. Pandas DataFrame索引 6. 集合索引（Python集合不支持索引）7. 自定义对象索引
# 1. 列表/数组索引
# 列表索引
my_list = [10, 20, 30, 40, 50]
print(my_list[2])  # 输出：30 (访问第三个元素）
print(my_list[-1]) # 输出：50（访问最后一个元素）

#修改元素
my_list[1] = 25
print(my_list)  # 输出： [10, 25, 30, 40, 50]

# 2. 元组索引
my_tuple = ('a','b','c','d')
print(my_tuple[0]) # # 输出: 'a'
print(my_tuple[-2]) # 输出： 'c'

# 3. 字典索引（通过键）
my_dict = {'name':'Alice', 'age':25, 'city': 'New York'}
print(my_dict['name']) # 输出： Alice
print(my_dict.get('age')) # 输出： 25

# 修改值
my_dict['age'] = 26
print(my_dict) # 输出： {'name': 'Alice', 'age': 26, 'city': 'New York')

# 4. NumPy 数组索引 import numpy as np  5. Pandas DataFrame索引
# 6 集合索引（Python集合不支持索引） 注意：Python的集合(set)是无序的，不支持索引操作。如果需要索引，可以转换为列表。

# 7. 自定义对象索引。 可以通过实现__getitem__和__setitem__方法使自定义类支持索引操作：
class MyCollection:
    def __init__(self,items):
        self.items = items
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,value):
        self.items[index] = value
col = MyCollection(['a','b','c','d'])
print(col[1]) # 输出: 'b'
col[2] = 'x'
print(col.items) # 输出: ['a', 'b', 'x', 'd']






















