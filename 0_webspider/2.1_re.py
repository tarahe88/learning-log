#正则表达式（Regular Expression，简称 regex 或 re）处理文本强大工具，用于提取和匹配目标数据
# 1 re作用：
            #匹配文本：从网页源码，api响应等文本提取目标数据
            #替换文本：将匹配的文本替换为指定内容。
            #验证文本：检查字符串是否符合特定格式（如邮箱，电话号码）
# 2 Python中的正则表达式模块
#Python通过re模块支持正则表达式
import re

# 3 正则表达式基础语法
# 3.1 普通字符 普通字符（如字母，数字）直接匹配自身。例如python撇普字符串中过的"python"
# 3.2 元字符。元字符是正则表达式的核心，具有特殊含义：
'''
#  . 匹配任意字符（除换行符\n)  例 a.b匹配aab, acb
#  ^ 匹配字符串的开头          例 ^abc匹配以abc开头的字符串
#  $ 匹配字符串的结尾          例 abc$匹配以abc结尾的字符串
#  * 匹配前一个字符0次或多次    例 abc*匹配 a、ab、abb
#  + 匹配前一个字符1次或多次    例 abc+匹配 ab、abb
#  ？匹配前一个字符0次或1次     例 abc？匹配 a、ab
# {n}匹配前一个字符恰好n次     例 a{2}匹配 aa
# {n,}匹配前一个字符至少n次     例 a{2,}匹配 aa、aaa
# {n,m}匹配前一个字符n到m次     例 a{2,4}匹配 aa、aaa、aaaa
# \d 匹配数字（等价于 [0-9]）	例 \d+ 匹配 123
# \D 匹配非数字	            例 \D+ 匹配 abc
# \w 匹配字母、数字、下划线（等价于 [a-zA-Z0-9_]）	 例\w+ 匹配 abc_123
# \W 匹配非字母、数字、下划线	                      例 \W+ 匹配 !@#
# \s 匹配空白字符（空格、制表符等）	             例 \s+ 匹配
# \S 匹配非空白字符	                            例 \S+ 匹配 abc
# [] 匹配括号内的任意一个字符	                    例 [abc] 匹配 a、b、c
# `	` 或操作，匹配左边或右边的表达式	                   例 `a	b匹配a或b`
# () 分组，将多个字符作为一个整体	                    例 (abc)+ 匹配 abc、abcabc

'''
# 3.3 转义字符，如果要匹配元字符本身，需要使用反斜杠\转义。例如匹配.需要用\.

# 4 Python中的正则表达式操作。
# 4.1  re.match() 从字符串开头匹配正则表达式。如果匹配成功，返回匹配对象，否则返回None.
import re
result = re.match(r"\d+", "123abc") # \d 匹配数字（等价于 [0-9]）
if result:
    print("匹配成功：", result.group()) #输出：匹配成功：123
else:
    print("匹配失败")

# 4.2 re.search() #在整个字符串中搜索匹配正则表达式的第一个位置。匹配成功返回匹配对象，否则返回None.
result = re.search(r"\d+", "abc123def")
if result:
    print("匹配成功:", result.group()) # 输出 匹配成功：123
else:
    print("匹配失败")
# 4.3 re.findall() 返回字符串中所有匹配正则表达式的子串，以列表形式返回。
result = re.findall(r"\d+", "abc123def456")
print(result) #输出 【‘123’，‘456’】
# 4.4 re.sub() 替换字符串中匹配正则表达式的部分。
result = re.sub(r"\d+", "NUM", "abc123def456")
print(result) #输出: abcNUMdefNUM .
# 4.5 re.compile() 将正则表达式编译成一个对象，便于重复使用。
pattern = re.compile(r"\d+")
result = pattern.findall("abc123def456")
print(result) #输出 [‘123’， ‘456’]

# 5 爬虫中常用的正则表达式示例
# 5.1 提取URL
text = "Visit my website at https://www.example.com."
url_pattern = r"https?://[^\s]+"
urls = re.findall(url_pattern, text)
print(urls) #输出：['https://www.example.com']
# 5.2 提取邮箱地址
text = 'Contact me at alice@example.com or bob@example.com.'
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)
print(emails) #输出： ['alice@example.com', 'bob@example.com']
# 5.3 提取HTML标签中的内容
html = '<div class="title">Hello,World!</div>' # = 前后不要有空格，不然76行报错
title_pattern = r"<div class=\"title\">(.*?)</div>"
title = re.search(title_pattern, html).group(1) #76行
print(title) # 输出： Hello,World!
# 5.4 提取数字
text = 'The price is $123.45'
number_pattern = r"\d+\.\d+"
numbers = re.findall(number_pattern, text)
print(numbers) #输出 ['123.45']
'''
6. 学习建议
从简单到复杂：先掌握基础语法，再逐步学习高级用法。
多练习：通过实际爬虫项目练习正则表达式。
使用工具：借助在线正则表达式测试工具（如 regex101）调试和验证正则表达式。
结合爬虫库：在爬虫中结合 BeautifulSoup 或 lxml 使用正则表达式提取数据。

'''
# 7. 示例：爬虫 + 正则表达式
# 以下是一个简单的爬虫示例，使用正则表达式提取网页中的标题和链接。
import requests
import re

url = "https://www.example.com"
response = requests.get(url)
html = response.text

#提取标题
title_pattern = r"<title>(.*?)</title>"
title = re.search(title_pattern, html).group(1)
print("标题：",title)
#提取所有链接
link_pattern = r"<a href=\"(.*?)\">"
links = re.findall(link_pattern,html)
print("链接：",links)


