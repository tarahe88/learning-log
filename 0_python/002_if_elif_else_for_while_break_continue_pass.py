'''
控制流决定了程序的执行顺序和逻辑。
1.Python中的控制流。python中的控制流主要包括：
    1.条件语句： if, elif, else
    2.循环语句： for 循环，while 循环
    3.控制语句： break, continue, pass
'''
# 2.条件语句。 条件语句根据条件决定程序的执行路径。
# 2.1 if 语句。 如果条件为真，则执行if块中的代码。
# 示例： if 语句
x = 10
if x > 5:
    print("x 大于 5") # 输出： x 大于 5
# 2.2 if-else 语句： 如果if 条件为真，则执行if块中的代码；否则执行else块中的代码
# 示例： if-else 语句
x = 3
if x > 5:
    print("x 大于5")
else:
    print("x 小于等于 5 ") # 输出: x 小于等于 5
# 2.3 if-elif-else语句。用于检查多个条件，依次判断if和elif条件，如果都不满足则执行else块中的代码。
# 示例： if-elif-else语句
x = 7
if x > 10:
    print("x 大于 10")
elif x > 5:
    print("x 大于5 且小于或等于 10") # 输出： x 大于5 且小于或等于 10
else:
    print("x 小于或等于 5")
# 3 循环语句： 循环语句用于重复执行某段代码
# 3.1 for 循环： 用于遍历序列（如列表，元组，字符串等）中的每个元素。
# 示例： for 循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # 输出如下；
    '''
    apple
    banana
    cherry
    '''
# 使用 range()函数
for i in range(5): # 0 到 4
    print(i) # 输出如下：
'''
0
1
2
3
4
'''
# 3.2 while 循环： 只要条件为真，就会重复执行while块中的代码
# 示例： while 循环
count = 0
while count < 5:
    print(count)
    count += 1 # 这个是限制条件，就是执行1段后，count自动+1直到条件为假，就是直到count>=5. 不加的话就会一直无限循环下去
# 输出如下：
    '''
0
1
2
3
4
    '''
# 4. 控制语句： 控制语句用于改变循环的执行流程。break：立刻退出， continue：跳过当前，pass:什么都不做。
# 4.1 break 语句： 用于立刻退出循环
# 示例：break语句
for i in range(10):
    if i == 5:
        break
    print(i)   # 输出: 0 1 2 3 4
# 4.2 continue 语句： 用于跳过当前循环的剩余代码，直接进入下一次循环
# 示例： continue 语句
for i in range(5):
    if i == 2:
        continue # 就是跳过 i == 2时的代码进入3的循环
    print(i) # 输出: 0 1 3 4
# 4.3 pass 语句： 用于占位，表示什么都不做。
# 示例: pass 语句
for i in range(5):
    if i == 2:
        pass # 什么都不做
    print(i) # 输出: 0 1 2 3 4
# 5. 嵌套控制流：控制流可以嵌套使用，例如在循环中嵌套条件语句，或在条件语句中嵌套循环。
# 示例： 嵌套控制流
for i in range(3):
    if i == 1:
        print("i 等于 1")
    else:
        print("i 不等于 1") # 输出： i 不等于 1      i 等于 1       i 不等于 1
# 6 练习与巩固：
# 练习1: 条件语句：编写一个程序，判断用户输入的数是正数，负数还是零。 #参考代码
# num = float(input("请输入一个数："))
# if num >0:
#     print("正数")
# elif num < 0:
#     print("负数")
# else:
#     print("零")
# 练习2: for循环。编写一个程序，计算1到100的和。
## 这个不理解，为啥最后只出来一个总数。
total = 0
for i in range(1, 101):
    total += i
print("1 到 100 的和：", total) # 输出： 1 到 100 的和： 5050

# 练习3: while循环。 编写一个程序，让用户猜1到10之间的随机数，直到猜对为止。
# import random
# target = random.randint(1,10)
# while True:
#     guess = int(input("猜一个 1 到 10的数："))
#     if guess == target:
#         print("猜对了！")
#         break
#     else:
#         print("猜错了，再试一次！")
# 练习4: break 和 continue。 编写一个程序，输出1到10之间的奇数
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i) # 输出 1 3 5 7 9
'''
7. 总结：
条件语句： if, elif, else用于根据条件执行不同的代码块
循环语句： for 和 while 用于重复执行代码块
控制语句：break, continue, pass 用于改变循环的执行流程。 
通过以上内容的学习和练习，你将掌握 Python 控制流的核心知识，为编写更复杂的程序打下坚实的基础！
'''


