'''
python中，函数是组织代码的基本单元，它可以将一段代码封装起来，方便重复使用。掌握函数的核心知识和技巧
1. 函数的定义与调用
1.1什么是函数？
    函数是一段可重复使用的代码块，用于完成特定任务。
    函数可以接收输入参数，并返回输出结果
'''
# 1.2 定义函数。
    # 使用def 关键字定义函数
    # 函数名后跟括号（），括号内可以定义参数
    # 函数体需要缩进
#示例：定义一个简单的函数
def greet():
    print("Hello,world!")
# 1.3 调用函数：通过函数名加括号（）调用函数
# 示例：调用函数
greet() # 输出： Hello,world!
# 2. 函数的参数与返回值
# 2.1 参数
    # 参数是传递给函数的值，用于函数内部处理
    # 参数分为位置参数和关键字参数
# 示例： 带参数的函数
def greet(name):
    print(f"Hello,{name}!")
greet("Alice") # 输出: Hello, Alice!

# 2.2 默认参数。可以为参数指定默认值，调用时如果不传递该参数，则使用默认值。
def greet(name="World"):
    print(f"Hello,{name}!")
greet()       # 输出: Hello, World!
greet("Alice") # 输出: Hello, Alice!
# 2.3 返回值
# 使用return 语句返回函数的结果
# 如果没有return语句，函数默认返回None
# 示例： 带回返回值的函数
def add(a,b):
    return a + b
result = add(3,5)
print(result)  # 输出: 8
# 3. 函数的类型
# 3.1 无参数无返回值。 # 函数不需要参数，也不返回任何值
# 示例： 无参数无返回值
def say_hello():
    print("Hello")
# 3.2 有参数，无返回值. # 函数需要参数，但不返回任何值
# 示例：有参数无返回值
def greet(name):
    print(f"Hello,{name}!")
# 3.3 无参数有返回值。 函数不需要参数，但返回一个值。
# 示例： 无参数有返回值
def get_pi():
    return 3.14159
# 3.4 有参数有返回值。 函数需要参数，并返回一个值。
# 示例： 有参数有返回值。
def add(a, b):
    return a + b
# 4. 函数的高级用法。
# 4.1 可变参数
    # 使用*args接收任意数量的位置参数。# 通过位置参数调用时，必须按照括号里面的顺序传递参数。
    # 使用**kwargs接收任意数量的关键字参数。#通过关键字参数调用，可以指定参数名来传递值，不受顺序限制。
    # ？关键字参数是必须有值的么？
# 示例：可变参数
def print_args(*args, **kwargs):
    print("位置参数：", args)
    print("关键字参数：", kwargs)
print_args(1,2,3, name="Alice", age =25)
'''
输出：
位置参数： (1, 2, 3)
关键字参数： {'name': 'Alice', 'age': 25}
'''
# 4.2 匿名函数（lambda函数）001-使用lambda关键字定义匿名函数 002-适合定义简单的函数
# 示例： lambda函数
add = lambda a,b: a+b
print(add(3,5))   # 输出: 8

# 4.3 函数作为参数。 函数可以作为参数传递给其他函数。
# 示例： 函数作为参数
def apply_func(func,a,b):
    return func(a,b)
result = apply_func(lambda x, y: x*y, 3, 4)
print(result) # 输出: 12

# 5. 函数的作用域。
# 5.1 局部变量。 在函数内部定义的变量是局部变量，只能在函数内部访问
# 示例： 局部变量
def my_func():
    x = 10
    print(x) # 这里为啥是空的，不显示.因为它在下面一行的调用函数里显示了。
my_func() # 输出: 10
# print(x) # 报错：NameError: name 'x' is not defined

# 5.2 全局变量。
    # 在函数外部定义的变量是全局变量，可以在整个程序中访问。
    # 如果需要在函数内部修改全局变量，需要使用global关键字。
# 示例： 全局变量
x = 10
def my_func():
    global x
    x = 20
    print(x)
my_func()  # 输出: 20
print(x)  # 输出: 20

# 6. 递归函数
    # 递归函数是调用自身的函数
    # 递归函数必须有一个终止条件，否则会无限递归。
# 示例: 递归函数
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # 输出: 120. 5*4*3*2？

# 7. 练习与巩固。
# 练习1:定义一个函数，定义一个函数 is_even, 判断一个数是否是偶数
def is_even(num):
    return num % 2 ==0
print(is_even(4)) # 输出: True
print(is_even(5)) # 输出: False
# 练习2: 带默认参数的函数。 定义一个函数greet, 接收一个名字参数，默认值为"World".
def greet(name="World"):
    print(f"Hello,{name}!")
greet()        # 输出: Hello, World!
greet("Alice") # 输出: Hello, Alice!

# 练习 3：递归函数. 定义一个递归函数fibonacci,计算斐波那契数列的第n项
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))  # 输出: 8
# 8 总结
#函数是组织代码的基本单元，可以提高代码的复用性和可读性。
# 掌握参数，返回值，作用域和递归等核心概念。











