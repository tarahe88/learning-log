#1 正则表达式用来处理字符串。实现字符串的检索，替换，匹配验证。
#https://tool.oschina.net/regex# 开源中国提供的正则表达式测试工具。

# #2  match  第一个比较常用的匹配方法。 match方法从字符串的开头开始匹配。
# #传入要匹配的字符串和正则表达式，检测正则表达式是否和字符串相匹配
# import re
# content = "Hello 123 4567 World_This is a Regex Demo"
# print(len(content)) #41
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content) #正则表达式+要匹配的字符串
# #^开头， \s空白字符串 \d数字， \d\d\d三个数字，d{4}表示4个数字 w{10} 10个字母及下划线
# print(result) #SRE_Match证明匹配成功。
# print(result.group()) #goupr方法可以输出匹配到的内容Hello 123 4567 World_This
# print(result.span()) #span方法输出匹配的范围。 匹配结果在字符串中的位置范围
#
# #匹配目标
# #从字符串中提取email地址电话。用()将想提取的字符串扩起来。
# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('Hello\s(\d+)\sWorld', content) #提取数字1234567. 表达式扩起来。
# print(result)
# print(result.group()) #Hello 1234567 World 输出第一个被()包围的匹配结果
# print(result.group(1))#1234567 输出完整的匹配结果
# print(result.span())

# #通用匹配.*-也叫贪婪匹配，用*代表匹配前面的字符无限次
# import re
# content = "Hello 123 4567 World_This is a Regex Demo"
# result = re.match('^Hello.*Demo$', content) #直接省略中间部分用.*代替，并在最后加一个结尾字符串
# print (result) #<re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
# print(result.group()) #Hello 123 4567 World_This is a Regex Demo
# print(result.span())
#
# # 非贪婪匹配 .*? 贪婪匹配是匹配尽可能多的数字，非贪婪匹配是尽可能少的字符。
# import re
# content = "Hello 1234567 World_This is a Regex Demo"
# result = re.match('^Hello.*?(\d+).*Demo$', content)
# print (result)
# print(result.group(1)) #1234567 非贪婪是尽可能少的字符

# #.*?如果在字符串结尾就匹配不到任何内容
# import re
# content = "http:/weibo.com/comment/kEraCN"
# result1 = re.match('http.*?comment/(.*?)',content) #.*?
# result2 = re.match('http.*comment/(.*)',content)  #.*
# print('result1', result1.group(1)) #result1 .*?在末尾没有匹配到任何结果
# print('result2', result2.group(1)) #result2 kEraCN .*尽量多匹配内容

# #修饰符re.S 作用是使匹配内容包括换行符在内的所有字符。
# #re.I 常用。使匹配对大小写不敏感。 re.L本地化识别。 re.M多行匹配影响^和$. re.S换行符。re.U unicode解析，影响\w,\b。 re.X
# import re
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^Hello.*?(\d+).*Demo$', content, re.S) #re.S修饰符 使之匹配包括换行符在内的所有字符。
# print(result.group(1))
#
# #转义匹配 \. 如果原文里有.了在前面加\.就可以转义
# import re
# content = '(百度)www.baidu.com'
# result = re.match('\(百度 \)www\.baidu\.com', content) #百度后面要加空格 不然报错
# print(result) #None 为啥这里不成功，但是书里成功了。
#
# #3 search. 正则表达式可以是字符串的一部分。 为了匹配方便，尽量使用search而非match
# import re
# content = "Extra stings Hello 1234567 World_This is a Regex Demo Extra stings"
# result = re.match('Hello.*?(\d+).*?Demo', content)
# print(result) #None 因为match里的正则表达式是从头开始匹配的
# #re.match改成re.search后就可以运行。 为了匹配方便，尽量使用search而非match
# import re
# content = "Extra stings Hello 1234567 World_This is a Regex Demo Extra stings"
# result = re.search('Hello.*?(\d+).*?Demo', content) #改成search后就可以正常运心g 。
# print(result) #<re.Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# import re
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# #提取singer属性值，需要的歌手和歌手名已经用小括号包围，所以可以用group方法获取
# if result:
#     print(result.group(1),result.group(2))   #齐秦 往事随风
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S) #不加Active
# if result:
#     print(result.group(1),result.group(2)) #任贤齐 沧海一声笑
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)  #去掉re.S
# if result:
#     print(result.group(1),result.group(2)) #beyond 光辉岁月

# # 4 findall 获取与正则表达式相匹配的所有字符串。 而search是返回与正则表达式相匹配的第一个字符串
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)>(.*?)</a>',html, re.S)
# print(results) #[('/2.mp3', '任贤齐"', '沧海一声笑'), ('/3.mp3', '齐秦"', '往事随风'), ('/4.mp3', 'beyond"', '光辉岁月'), ('/5.mp3', '陈慧琳"', '记事本'), ('/6.mp3', '邓丽君"', '但愿
# print(type(results))  # <class 'list'>
# for result in results:
#     print(result)  #列表的每个原色都是元组类型
#     print(result[0],result[1],result[2])    #用索引依次取出每个条目即可。

#5 sub 修改文本。 search 和 findall找到文本后，sub修改文本
import re
content = "9kahg80a8gag88780gfg"
content = re.sub('\d+'," ",content)  # 找到数字，替换成空格，在所有内容里
print(content)  #kahg a gag gfg

# import re
# html=re.sub('<a.*?>|</a>',"", html)  #将a节点去掉，只留下文本
# print(html)
# results = re.findall('<li.*?>(.*?)</li>',html,re.S)  #通过findall方法直接提取。
# for result in results:
#     print(result.strip())

# 6 compile 将字符串变异成正则表达式对象，以便在后面的匹配中复用。
import re
content1 = "2019-12-15 12:00"
content2 = "2019-12-17 12:55"
content3 = "2019-12-22 13:21"
pattern =  re.compile('\d{2}:\d{2}') #
result1 = re.sub(pattern, "", content1)  #去掉3个日期中的时间
result2 = re.sub(pattern, "", content2)
result3 = re.sub(pattern, "", content3)
print(result1, result2, result3)





















