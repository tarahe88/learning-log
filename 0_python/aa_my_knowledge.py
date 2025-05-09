from parsel.xpathfuncs import set_xpathfunc

print("字符串") # 字符串要加双引号
a = 3
print(a) # 变量 a 不加双引号
import math # math 是库
math.sin(1) # math. 表示是库里的， sin(1) 是 math 库里的函数 # 这个计算结果只会在内存里。

result = math.sin(1) # 可以将计算结果赋值到变量里，然后打印变量出来
print(result)
'''
input('请输入你多大：') # 函数名+() ()里面放参数，是标准调用函数的方式
user_age = input("请输入您的年龄：")  # input函数会返回一个值。用一个变量去获取input返回的值。 如果前面不加变量，这个值就不会被存储和被程序访问到
print(user_age)
mood_index = (input("今天对象的指数为："))
if mood_index is True:
    if mood_index >= 80:
        print("去吧，皮卡丘！")
        # 如何加一个值：如果不是数字，提示输入错误。
    else:
        print("为了小命，还是别去了 ")
else:
    print("输入错误，请输入一个数值")

.append() 是针对列表的方法。 方法和函数差不多, 只是位置不同。 对象.方法名().  函数名(对象)
shopping_list.append()    len(shopping_list)'''

# 逻辑运算符， not 优先级大于 and 优先级大于 or. not>and>or

'''
方法和函数都是可执行的代码块。 主要区别在于归属关系和调用方法以及饮食参数(self)
1.归属关系：
    函数(function）：独立存在，不依赖于任何对象或类class
    方法(method): 属于某个对象或类class的函数
2.调用方式：
    函数可以直接调用： len()
    方法需要对象或者类调用：my_list.append() 或 classname.methodname()
3.隐式参数
    方法通常有一个隐式参数（self)，可以访问对象实例的数据.有self(实例方法)和cls(类方法)。 函数没有这种隐式参数
其他区别：
命名：面向对象语言中，通常把类内部的函数称为方法，独立的成为函数
作用域： 方法可以访问类的属性和恰方法，函数通常只能访问自己的参数和全局变量
多态性：方法可以被子类重写，实现多态，函数通常不具备这种特性
'''
# 函数示例
def add(a, b): # 独立函数
    return a + b
# 调用函数
result = add(3, 5)

# 方法示例
class Math:
    def add(self, a, b):  # 类的方法
        return a + b
# 调用方法
math = Math()
result = math.add(3, 5)

# 函数和方法的代码实例
# (1) 函数 function
def greet(name): # 独立函数
    return f"Hello,{name}"
print(greet("Alice")) # 直接调用。 不依赖任何类或对象，直接调用。
# 输出：Hello,Alice

# (2) 方法 method。定义在内部。必须通过实例调用（自动传入self),可以访问实例属性(self.name)
# 2.1 实例方法 instance method
class Person:
    def greet(self,name): # 实例方法（第一个参数是'self')
        return f"Hello,{name}! I'm {self.name}."
p = Person()
p.name ="Bob"
print(p.greet("Alice"))  # 通过实例调用。
# 2.2 类方法 class method。 特点：使用@classmethod装饰器，可以访问类属性（如cls.some_class_var)。无序实例化即可调用。
class Math:
    @classmethod
    def add(cls,a,b): # 类方法（第一个参数是'cls')
        return a + b
print(Math.add(3,5)) # 通过类调用
# 2.3 静态方法(static method)。特点：使用@staticmethod装饰器。不绑定到实例或类（相当于放在类里的普通函数）。不能访问self或cls.
class Math:
    @staticmethod
    def multiply(a,b):  #静态方法（无'self'或'cls')
        return a * b
print(Math.multiply(3,5)) # 通过类调用

'''
# 3. 关键总结 函数和方法
类型。     定义方式           调用方式            自动传入参数         典型用途
函数      def 函数():        函数()             无                  独立功能
实例方法   def 方法(self):    对象.方法()        self(实例)           操作实例数据
类方法    
静态方法
什么时候用方法：如果逻辑和类/对象 相关（如修改实例属性，访问类变量）
什么时候用函数：如果逻辑是独立的（如数学计算，字符串处理）
'''
# 列表先空值，后慢慢添加，删除，修改等
shopping_list = [] # 先空值，后慢慢添加
shopping_list.append("键盘")
shopping_list.append("键帽")
print(shopping_list) # 输出： ['键盘', '键帽']

# 函数：最大函数max,最小函数min,排序函数sorted。 print括号里可以直接放变量。 变量可以直接等于一个函数的值
house_price = [10000, 8000, 15000,22000]
max_house_price = max(house_price)
min_house_price = min(house_price)
sorted_house_price = sorted(house_price)
print(max_house_price)      # 输出：22000
print(min_house_price)      # 输出：8000
print(sorted_house_price)   # 输出：[8000, 10000, 15000, 22000]

# 元组()的应用。元组()跟列表[]很像可以放很多类型数据。
# 但是跟列表不同的是，元组不可变。字典里的键值对，列表不可以作为键，但是元组可以作为键

# 例子；整个元组作为键。
contacts = {("张伟",23): "152298580",
                ("张伟",35):"1903849404",
                ("张伟",18): "189203495",
            ("李四",23): "149480204"}
zhangwei_23_contacts = contacts["张伟",23] # 注意这里的键值对里的键使用[]不是()表示。
print(zhangwei_23_contacts) # 输出：152298580
contacts.pop(("李四",23)) # 用pop方法就是用()，直接删除del contacts[("李四",23)]
print(contacts)

# 键 in 字典， 返回的是布尔值
print(("(张三)",18) in contacts) # 返回的是true
''' for 循环基本语法
# for 变量 in  可迭代对象：
    # 要重复执行的代码     # 提取每个变量，并对每个变量执行同样的代码
'''
# for 遍历 1 列表（最常用），2 字符串，3 数字范围range[5], 4 字典里的键值。遍历里面的每个元素，并对每个元素执行相同的操作。
# for 循环3个关键技巧。 1 break 提前退出， 2 continue跳过当前循环 3.使用enumerate获取索引
'''while循环基本语法
while 条件：
    # 条件为真时执行的代码
'''
# 简单示例：
count = 0
while count < 5:
    print(f"这是第{count +1}次循环")
    count += 1 # 不要忘记更新条件变量
# 2。 while 循环4种常见用法. 1.基础计数循环。 2.用户输入验证。 3.未知次数的循环（读取数据直到结束）4.循环+异常处理
# 3。 while 循环 3个关键控制语句。 1. break 立即退出循环 2.continue 跳过本次循环 3.else 循环正常结束执行
# 4。 while 循环常见错误及避免方法。 1.忘记更新条件变量（无限循环）。2.使用浮点数作为条件。3.复杂的退出条件
#二、while循环的4种常见用法
# 2.1 基础计数循环
# 打印1-10 的数字
num = 1
while num <= 10:
    print(num)
    num += 1
# 2.2 用户输入验证
password = ""
while password != "123456": # 当密码不正确时继续循环
    password = input("请输入密码：")
print("登录成功")
# 2.3 未知次数的循环（读取数据直到结束）
# 模拟读取数据直到遇到空行
data = []
while True:
    line = input("请输入数据（直接回车结束）：")
    if not line: # 如果输入空行
        break  # 退出循环
    data.append(line)
print("收集到的数据：", data)
# 2.4 循环+异常处理
while True:
    try:
        age = int(input("请输入您的年龄："))
        break  # 如果转换成功则退出循环
    except ValueError:
        print("输入无效，请输入数字！")
print(f"您的年龄是：{age}")
# 三、while循环的3个关键控制语句
# 3.1 break-立即退出循环
while True:
    answer = input("输入quit退出：")
    if answer == "quit":
        break # 立即退出循环
    print(f"你输入了：{answer}")
# 3.2 continue-跳过本次循环
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # 如果是偶数
        continue      # 跳过本次循环的剩余部分
    print(num)        # 只会打印奇数
# 3.3 else-循环正常结束执行
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("循环正常结束") # 如果循环没有被break中断，就会执行
    # 输出：
    # 0
    # 1
    # 2
    # 循环正常结束
# 四、while循环的常见错误及避免方法
# 4.1 忘记更新条件变量（无限循环）
# 错误示例：
#
# 正确写法：
count = 0
while count < 5:
    print(count)
    count += 1  # 必须更新条件变量
#错误2：使用浮点数做条件count = 0
# while count < 5:
#     print(count)     # 忘记写 count += 1, 导致无限循环
# 不推荐：
# x = 0.0
# while x != 1.0:  # 浮点数比较可能因精度问题导致意外结果
#     x += 0.1
#     print(x)

# 推荐：
x = 0.0
while x < 1.0:   # 使用小于比较更安全
    x += 0.1
    print(x)
# 错误3：复杂的退出条件
# 不清晰：
# while (not condition1) and (condition2 or condition3):
    # 代码

# 更清晰：
# while True:
#     if condition1:
#         break
#     if not condition2 and not condition3:
#         break
    # 代码
'''
引入模块 import...语句 和 from...import...语句
'''
# import 语句
import statistics
print(statistics.median([19, -5, 36]))   # 模块名.函数名/变量名（参数）
print(statistics.mean([19,-5,36]))       # 模块名.函数名/变量名（参数）

# from...import...语句
from statistics import median,mean
print(median([19, -5, 36]))  # 不需要带模块名字，直接用其函数/变量
print(mean([19,-5,36]))      # 不需要带模块名字，直接用其函数/变量

# from...import* 语句 引入模块里的全部函数/变量。不推荐使用，因为会产生命名冲突。A模块里的 a 与模块B 里的a 冲突
'''
面向对象编程
'''
# 所谓方法就是放在类里面的函数，所谓属性，就是放在类里面的变量
# 类是创建对象的模版，对象是类的实例
# 类定义对象有何种属性和方法，而对象拥有的属性不尽相同。
#  def __init__(self,cat_name,cat_age,cat_color): 类定义了对象有何种属性和方法
#  cat1 = CuteCat("JOJO", 2, '橙色')： 对象拥有的属性不尽相同
#  cat2 = CuteCat("Cash", 3, '黄色')： 对象拥有的属性不尽相同
#

'''
创建类. 类有属性-相当于变量 def __init__.  init构造方法定义对象有哪些属性。 
cat1 = CuteCat('1','白色','jojo')类括号创建对象，调用init属性，对属性进行赋值。 
类有方法-相当于函数.与函数不同的是。1.方法要写在class里面，2方法用self可以在方法里面去获取或修改和对象绑定的属性
'''
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):  # 括号里面是参数，相当于变量，可以赋值。
        # self帮你把属性的值绑定在实例对象上
        self.name = cat_name  # 前面的self.一定要加，相当于实例。 不加就以为是普通的变量name。
        # self.name是绑定到对象身上的属性。而cat_name是普通变量，是通过参数传入进来的
        self.age = cat_age    # 同上， self 相当于 CuteCat
        self.color = cat_color  # 同上。 实例.属性 = 参数（可传入的）

    def speak(self):  # 方法用self一个作用是可以在方法里面去获取或修改和对象绑定的属性
        print("喵" * self.age) # 年龄属性,n岁就叫n次喵

    def think(self, content): # 方法可以接收更多参数。思考的内容-参数值可以作为参数传入。
        # 如思考去抓什么，思考今天想干什么，思考穿什么，思考吃什么。这些都可以作为content的参数。
        print(f"小猫{self.name}在思考{content}...")

cat1 = CuteCat("JOJO", 2, '橙色')  # = 类名。 创建对象。 这样init属性就会被调用。
# 这是调用属性。 参数里面赋值给属性
cat1.speak()  # 这是调用方法。 和构造方法一样，不需要手动把self传入
# 输出：喵喵
cat1.think("现在去抓沙发还是去撕纸箱")
# 输出： 小猫JOJO在思考现在去抓沙发还是去撕纸箱...
# 例子 定义一个学生类。
# 要求：
# 1. 属性包括学生姓名，学号，以及语数英三科的成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印出该学生的所有科目成绩
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文":0, "数学":0, "英语":0} # 定义一个字典，让每个学生的每科成绩初始值都是0
        # 如果每个对象都拥有一样的初始值，就不需要从参数中获取。 就可以直接在下面self.grades中定义
        # 属性可以带初始值
        # self.grades 这是每个学生自带的“成绩单字典”(属性）初始状态:{"语文":0, "数学":0, "英语":0}
    def set_grade(self, course, grade): # 改哪个科目 course, 改什么样的成绩grade
        if course in self.grades: # 方法用self一个作用是可以在方法里面去获取或修改和对象绑定的属性
            self.grades[course] = grade # 如果这门课是self.grades里的键，那么把对应的值更新成传入的参数grade
            # 这是在更新字典里对应科目的值
            # 相当于把“数学”对应的0改成你传入的新分数。
            # self.grades[course]是字典的取值赋值操作
    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id}的成绩为：")
        # f 格式化字符串：就是加了f，后面的函数能在字符串里直接应用。
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")
            # f 格式化字符串：就是加了f，后面的函数能在字符串里直接应用。
chen=Student("小陈","200105")
chen.set_grade("语文",90)
chen.set_grade("数学", 98)
#输出：
'''学生小陈(学号：200105的成绩为：
语文:90分
数学:98分
英语:0分'''
chen.print_grades()
wang=Student("小王","200208")
print(chen.name) # 输出： 小陈
print(wang.grades) # 输出： {'语文': 0, '数学': 0, '英语': 0}
wang.set_grade("数学", 95)
print(wang.grades) # 输出： {'语文': 0, '数学': 95, '英语': 0}

'''#继承
面向对象有个重要特征叫继承。 可以创建有层次的类。 类也可以有子类和父类。 子类会继承父类的属性和方法'''
class Manmal: # 哺乳动物 包含人和猫
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2
    def breathe(self):
        print(self.name + "在呼吸...")
    def poop(self):
        print(self.name + "在拉屎...")

class Human(Manmal): # 子类人继承哺乳动物的属性（名字，性别，眼睛数量）。 和继承哺乳动物构造方法里的（在呼吸，在拉屎）
    def __init__(self,name,sex):
        super().__init__(name,sex) # 父类的属性继承
        # super()表示父类
        # 属性要调用父类的构造函数，用super().__init__不像方法一样直接写，属性要super
        # 子类也有父类的 眼睛，姓名，性别的属性了
        self.has_tail = False
    def read(self):
        print(self.name + "在阅读...") # 方法直接写。（子类方法优先父类）
class Cat(Manmal):
    def __init__(self,name,sex):
        super().__init__(name,sex) # 父类的属性继承
        # super()表示父类
        # 属性要调用父类的构造函数，用super().__init__不像方法一样直接写，属性要super
        # 子类也有父类的 眼睛，姓名，性别的属性了
        self.has_tail = True # 子类特有的属性
    def scratch_sofa(self):
        print(self.name + "在抓沙发...") # 方法直接写。（子类方法优先父类）
    def poop(self):
        print(self.name + "在猫砂上拉屎") # 方法优先看子类有没有方法，没有就调用父类的同名方法。此处有猫子类的拉屎方法，不用父类。
cat1 = Cat("Jojo","男")
print(cat1.name) # 输出： Jojo
cat1.poop() # 输出： Jojo在猫砂上拉屎
# 类继承练习：人力系统
# -员工分为两类：全职员工 FullTimeEmployee， 兼职员工PartTimeEmploeyee
# -都具备“打印信息 print_info" (打印姓名，工号）方法
# -全职有“月薪 monthly_salary" 属性
# -兼职有“日新 daily_salary'属性，“每月工作天数 work_days“的属性
# -全职和兼职都有“计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样
class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"员工名字：{self.name},工号：{self.id}")
class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary): # 父类里的姓名和编号属性，以及全职员工自己的属性月薪
        super().__init__(name,id) # 调用父类的构造函数 姓名和编号
        self.monthly_salary = monthly_salary # 全职员工自己的月薪属性

    def calculate_monthly_pay(self):  # 计算全职员工的工资
        return self.monthly_salary  # 这个就简单了，直接是属性里的员工月薪
        # 为什么是return 不是print. 因为返回值在类外有更好的操作空间
        # return是你还需要定义一个变量去接收它的返回值，，后面可以继续使用。而print是直接打印
        # 因为目的是计算而不是打印，计算的结果要用return来储存
class PartTimeEmployee(Employee):
    def __init__(self,name, id, daily_salary, work_days): # 兼职员工有两个自己的属性: 日薪和工作天数
        super().__init__(name,id) # 继承父类里的 name, id
        self.daily_salary = daily_salary # 兼职员工自己的属性日薪
        self.work_days = work_days # 兼职员工自己的属性工作天数

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days
        # 为什么是return 不是print. 因为返回值在类外有更好的操作空间
        # return是你还需要定义一个变量去接收它的返回值，后面可以继续使用。而print是直接打印
        # 因为目的是计算而不是打印，计算的结果要用return来储存
zhangsan = FullTimeEmployee("张三", "1001", 10000)
# 创造叫zhangsan的全职员工给姓名，编号，月薪 属性
lisi = PartTimeEmployee("李四", "2001", 500,15)
# 创造叫lisi的兼职员工给姓名，编号，日薪，工作天数 属性
zhangsan.print_info() # 输出： 员工名字：张三,工号：1001 # 调用的是父类的打印信息方法
lisi.print_info()  # 输出： 员工名字：李四,工号：2001 # 调用的是父类的打印信息方法
print(zhangsan.calculate_monthly_pay()) # 输出: 10000  # 调用的是子类-全职员工的各自计算员工工资的方法
print(lisi.calculate_monthly_pay())  # 输出： 7500。    # 调用的是子类-兼职员工的各自计算员工工资的方法

'''
文件操作：
1. 文件有绝对路径和相对路径
2. f = open("/usr/demo/data.txt", "r"， encoding="utf-8") 
第一个是路径(可以是相对也可以是绝对), r 是读取模式，w 是写入模式。不写的话默认读取。。
encoding 是可选参数。 utf-8是一般的编码方式是utf-8
print(f.read()) # 会读取全部的文件内容，并打印
print(f.read()) # 会读取空字符串，并打印。因为第一次（上面）已经读完了，所以会返回空值
print(f.read(10)) # 会读第1-10个字节的文件内容
print(f.read(10)) # 会读第11-20个字节的文件内容
print(f.readline()) # 会读取一行文件内容，并打印
# read()会有点大，尽量不要用read()而使用 readline或readlines

f = open("./data.txt","r", encoding="utf-8")
line = f.readline()         # 读取第一行
while line != "":           # 判断当前行是否为空
    print(line)             # 不为空则打印当前行
    line = f.readline()     # 读取下一行
更简洁的方法 readlines 读取全部文件内容
f = open("./data.txt","r", encoding="utf-8")
print(f.readlines())      # readlines会读取全部文件内容，并把每行作为列表元素返回。
# readlines返回的是列表，所以结合 for 循环使用
# readlines 会结合 for 循环使用
f = open("./data.txt","r", encoding="utf-8")
lines = f.readlines()   # 把每行内容储存到列表里
for line in lines:      # 遍历每行内容
    print(line)         # 打印当前行
# 总结： read() 返回全部文件内容。 readline()返回一行文件内容。 readlines()返回全部文件内容
# 关闭文件
f = open("./data.txt")
print(f.read())  # 对文件的操作
f.close()        # 关闭文件，释放资源

# 另外一种方法 with 关键字 跟上open 函数的调用，然后 as 跟上文件对象的命名
with open("./data.txt") as f:
    print(f.read())     # 对文件的操作。   
# with 自动打开关闭，缩进的代码块执行完毕后文件自动关闭
'''
f = open("./data.txt","r",encoding = "utf-8")  # ./ 表示当前文件夹
content = f.read() # 用变量储存内容
print(content)
f.close()

# 另外用with 自动关闭
with open("./data.txt","r", encoding = "utf-8") as f:
    content = f.read()
    print(content)
''''
"w" 写入模式和“r"只读模式的不同。 
如果文件不存在 with open("./data.txt","r") 就会报错，而"w"不会报错，会创建新文件
如果文件存在， "w" 写入模式将原文件清空，所以用"w"模式前要三思而后行
# "w" 是将原文件清空重写。  "a" 是增加不清空
f.write("Hello!")
f.write("Yoooo") 
# 如果不换行输出结果为: Hello!Yoooo
f.write("Hello!\n")
f.write("Yoooo")  # 输出:
Hello!
Yoooo
'''
#  "w" 是清空重写， “a"是附加，但要用到.write()函数
with open("./data.txt","a",encoding = "utf-8") as f:  # 同一文件夹下的话,./可以省略
    f.write("Hello!\n")
    f.write("Yoooo")

with open("./taoteching.txt","w",encoding = "utf-8") as f:  # 创建一个新文件道德经 Tao Te Ching 写入以下文字
    f.write("人法地，地法天，天法道，道法自然。\n上善若水，水善利万物而不争。\n有无相生，难易相成，长短相形。\n圣人之道，为而不争。治大国若烹小鲜。")
    f.write("\n天下莫柔弱于水，而攻坚强者莫之能胜。\n知足不辱，知止不殆。\n反者道之动，弱者道之用.\n")
with open("./taoteching.txt",'a', encoding = "utf-8") as f:
    f.write("\n道可道，非常道；名可名，非常名。（第一章）。\n天下皆知美之为美，斯恶已；皆知善之为善，斯不善已。（第二章）.\n上善若水，水善利万物而不争。（第八章）.\n功遂身退，天之道。（第九章）.\n有之以为利，无之以为用。（第十一章）")
    f.write("致虚极，守静笃。（第十六章）.\n大道废，有仁义；智慧出，有大伪。（第十八章）.\n绝圣弃智，民利百倍；绝仁弃义，民复孝慈。（第十九章）.\n人法地，地法天，天法道，道法自然。（第二十五章）.\n知人者智，自知者明。（第三十三章）")
    f.write("大方无隅，大器晚成，大音希声，大象无形。（第四十一章）.\n道生一，一生二，二生三，三生万物。（第四十二章）.\n祸兮福之所倚，福兮祸之所伏。（第五十八章）.\n治大国若烹小鲜。（第六十章）.\n天下难事必作于易，天下大事必作于细。（第六十三章）")
    f.write("合抱之木，生于毫末；九层之台，起于累土。（第六十四章）.\n江海所以能为百谷王者，以其善下之。（第六十六章）.\n天网恢恢，疏而不失。（第七十三章）.\n民之饥，以其上食税之多，是以饥。（第七十五章）.\n信言不美，美言不信；善者不辩，辩者不善。（第八十一章）")

'''捕捉异常 try except
报错类型
typeerror: 类型错误，zerodivisionerror除零错误，syntaxerror语法错误，indentationerror缩进错误，attributeerror属性错误
importerror导入模块错误，keyerror键错误，valueerror值错误
'''
try:  # try 放上你觉得可能会产生报错的代码
    user_weight = float(input("请输入您的体重（单位：kg):")) # 容易出现输入的不是数字错误
    user_height = float(input("请输入您的身高（单位：m:")) # 容易出现数字 0 错误
    user_BMI = user_weight / user_height ** 2  # 容易出现数字 0 错误
except ValueError: # 跟上你想捕捉的错误名字。比如客户没有输入数字，输入的是字符串
    print("输入的不是数字，请重新运行程序，并输入正确的数字") # 产生值错误时运行
except ZeroDivisionError:
    print("身高不能为零，请重新运行程序，并输入正确的数字")  # 产生除零错误时运行
except: # 这个会捕捉所有错误
    print("发生了未知错误，请重新运行")                   # 产生其他错误时运行
else:   # 当 try 里面的语句没有任何错误产生时要执行的语句
    print("您的BMI值为：" + str(user_BMI))             # 没有错误时运行
finally:  # 无论错误发生与否，最终都会被执行的语句
    print("程序结束运行")  # 不管发生错误与否，都会执行

'''assert 断言，后面为 True 或 False 的表达式
assertionerror 断言错误
unittest 测试库 测试代码放在独立文件里
'''
'''
# 实现代码
def my_adder(x,y):
    return x + y
# 测试代码 单独在另外一个文件里
import unittest
from my_caculator import my_adder 如果测试文件和被测试文件都在同一个文件夹下， 从文件名里引入函数名
class TestMyAdder(unittest.TestCase):创建一个类，可以以Test开头表示这是一个测试的类
# 这个类当unittest.TestCase的子类，这样就能继承unittest.TestCase的各种测试功能
# 在这个类下面，可以定义不同的测试用例，每个测试用例都是类下面的一个方法
    def test_positive_with_positive(self): # 命名很关键，必须以test_开头，因为unittest库只会搜索test_开头的方法
        self.assertEqual(my_adder(5,3),8) # 用assert的Equal方法。
        #如果第一个参数my_adder(5,3)和第二个参数8相等，显示通过。不想等显示不通过也不会炸。
    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5,3),-2)
# 运行 unittest. 在终端输入 python -m -unittest     
# 这库就会自动搜索所有继承了unittest库里TestCase类的子类，运行他们所有以test_开头的方法，然后展示测试结果  
..  2个点点表示2个测试通过
run 2 tests in 0.000s 运行了2个测试
OK 表示测试通过  
F.  表示有一个没通过，另外一个通过了
FAIL： test_negative_with_positive(test_my_calculator.TestMyAdder) 表示这个测试没通过
AssertionError:-2 != -1  表示没通过的原因
# unittest.TestCase类的常见测试方法
    方法                  类似于
assertEqual(A,B)        assert A == B 
assertTrue(A)           assert A is True
asserIn(A,B)            assert A in B   
assertNotEqual(A,B)     assert A !== B 
assertFalse(A)          assert A is False
asserNotIn(A,B)         assert A not in B 
# 例子 推荐用更针对性的方法。asserNotIn 专门针对元素和列表的方法而不是assertTrue这个万能方法
assertTrue(2 not in [1,3-1])  assertNotIn(2,[1,3-1]
# 例子，测试一个类 class Sentence
实现代码 sentence.py

class Sentence:
    def__init__(self.sentence):
        self.sentence = sentence
    
    # 返回句子字母数量
    def letter_count(self):
        return len(self.sentence)
    
    # 返回句子单词数量
    def word_count(self):
        return len(self.sentence.split(" "))
    
    # 返回所有字母大写后的句子
    def upper(self):
        return self.sentence.upper()
测试代码 test_sentence.py
import unittest
from sentence import Sentence

class TestSentence(unittest.TestCase):
    def test_str_count(self):
        sentence = Sentence("hello world!") # 重复代码 实例对象。正确应该在前面设置一个setUp方法。
        self.assertEqual(sentence.str_count(),12)
        
    def test_word_count(self):
        sentence = Sentence("hello world!") # 重复代码 实例对象。正确应该在前面设置一个setUp方法。 
        self.assertEqual(sentence.word_count(),2)
        
    def test_upper(self):
    sentence = Sentence("hello world!") # 重复代码 实例对象。正确应该在前面设置一个setUp方法。
    self.assertEqual(sentence.upper(),"HELLO WORLD!")     
# 上面的正确做法，设置set up 方法         
测试代码 test_sentence.py
import unittest
from sentence import Sentence

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence("hello world!")
        
    def test_str_count(self):
        self.assertEqual(sentence.str_count(),12)
        
    def test_word_count(self): 
        self.assertEqual(sentence.word_count(),2)
        
    def test_upper(self):
    self.assertEqual(sentence.upper(),"HELLO WORLD!")     
'''
# 实践时间
class ShoppingList:
    # 初始化购物清单，shopping_list是字典类型，包含商品名称和对应价格
    # 例子：（“牙刷”：5， “沐浴露”：15， “电池”：7}
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list

    # 返回购物清单上有多少项商品
    def get_item_count(self):
        return len(self.shopping_list)

    # 返回购物清单上商品价格总额数字
    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list:
            total_price += price
        return total_price
'''
高阶和匿名函数。函数作为参数的函数叫高阶函数。 函数可以传入函数。
注意作为参数的函数后面不要带括号，因为一旦有括号，这个函数就被调用，传入的就是函数的执行结果，而不是函数本身
calculate_and_print(3,calculate_square)
calculate_and_print(3,calculates-square()) # 这个函数作为参数不要带括号。
'''







