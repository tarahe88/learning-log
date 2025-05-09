"""用xpath代替正则表达式解析页面时，用xpath或者css选择器提取摸个节点，调用方法获取该节点的正文内容或者属性。xmlpath最初用来搜寻xml文档，同样适用于html文档
常用匹配规则：
//title[@lang='eng'] 代表选择所有名称为title,同时属性lang的值为eng的节点
"""
from lxml import etree #倒入etree模块。
text = '''
<div>
    <ul>
        <li class ="item-0"><a href="link1.html">first item</a></li>
        <li class ="item-1"><a href="link2.html">second item</a></li>
        <li class ="item-inactive"><a href="link3.html">third item</a></li>
        <li class ="item-1"><a href="link4.html">first item</a></li>
        <li class ="item-0"><a href="link5.html">fifth item</a> 
    </ul>
</div>
'''
#注意最后一个</li>没有闭合,etree可以自动修正html文本

# html = etree.HTML(text) #声明html文本，调用HTML类进行初始化。 这样构造了一个XPATH解析对象
# result = etree.tostring(html) #调用tostring方法输出修正后的html代码，输出bytes类型，需要decode人类能看懂的str类型
# print(result.decode('utf-8')) #跟原文本text一样，只是多加了<html><body>和</body></html>。decode就是将bytes转化成字符串

# #也可以不声明，直接读取文本文件进行解析。
# from lxml import etree
# import test.test_html
# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8')) # 多了DOCTYPE声明

#5 所有节点。 html.xpath('//*') 开头的xpath规则，选取所有符合要求的节点
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*') #使用*代表匹配所有节点，也就是获取整个html文本中的所有节点
print(result) # Element节点名称 [<Element html at 0x10af37f40>, <Element body at 0x10b50cb80>, <Element p at 0x10b50cbc0>
# 选取所有li节点 html.xpath('//li')
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result) #所有节点[<Element li at 0x10118c980>, <Element li at 0x10118ce40>, <Element li at 0x10118ce80>, <Element li at 0x10118cec0>
print(result[0]) #第1个li节点 <Element li at 0x10118c980>
print(result[1]) #第2个li节点 <Element li at 0x10118ce40>
print(result[2]) #第4个li节点 <Element li at 0x10118ce80>

#6 子节点或子孙节点 html.xpath('//li/a') /子节点，//子孙节点
#<li class ="item-1"><a href="link4.html">first item</a></li>
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a') #/a追加a节点
print(result) #[<Element a at 0x1098d4940>, <Element a at 0x1098d4980>, <Element a at 0x1098d49c0>, <Element a at 0x1098d4a40>, <Element a at 0x1098d4a80>]

#7 父节点。
#<li class ="item-1"><a href="link4.html">first item</a></li>
#选中href属性为link4.html的a节点，获取其父节点，获取父节点的class属性
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result) #['item-1']
#也可以通过parent:获取父节点
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result) #['item-1']

#8 属性匹配。
#选取节点的时候，还可以使用@符号实现属性过滤。如要选取CLass属性为item-0的li节点
#<li class ="item-0"><a href="link1.html">first item</a></li>
#<li class ="item-0"><a href="link5.html">fifth item</a>
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]') #如要选取CLass属性为item-0的li节点
print(result) #[<Element li at 0x10d22cc00>, <Element li at 0x10d22cc40>]
# 属性获取不同： result = html.xpath('//li/a/@href') #通过@href获取节点的href属性。

#9 文本获取
from lxml import etree
html= etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result) # [' #'] #正确应该为【'\n'] 正确的事没有获取任何文本，只获取了一个换行符。
#正确的是
from lxml import etree
html= etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()') #先选取li节点利用/选取子节点a节点再获取a的文本。
print(result) #['first item', 'fifth item']
#或者正确的是
from lxml import etree
html= etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()') #选取所有li子节点a内部文本和籽后一个li节点内部的文本=换行符
print(result) # ['first item', 'fifth item', ' #']

# 10 属性获取
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href') #通过@href获取节点的href属性。
print(result) #['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
#属性匹配是中括号加属性名和值限定某个属性。result = html.xpath('//li[@class="item-0"]') #如要选取CLass属性为item-0的li节点

#11 属性多值匹配
from lxml import etree
text = '''
<li class ="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result) #[] li节点的class属性有两个值：li 和 li-first。之前的方法不行，应该用contains方法
#用contains方法
from lxml import etree
text = '''
<li class ="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')#给第一个参数传入属性名，第二个参数传入属性值
print(result) #['first item']

#12 多属性匹配 根据多个属性确定一个节点
from lxml import etree
text = '''
<li class ="li li-first" name = "item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()') #用and运算符相连
print(result) #['first item']

#13 按序选择. 用到方法last, position等方法。
from lxml import etree
text = '''
<div>
    <ul>
        <li class ="item-0"><a href="link1.html">1st item</a></li>
        <li class ="item-1"><a href="link2.html">2nd item</a></li>
        <li class ="item-inactive"><a href="link3.html">3rd item</a></li>
        <li class ="item-1"><a href="link4.html">4th item</a></li>
        <li class ="item-0"><a href="link5.html">5th item</a> 
    </ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()') #第1个li节点，注意序号以1开头，跟写代码0开头不一样
print(result) #['1st item']
result = html.xpath('//li[last()]/a/text()') # 最后一个li节点
print(result) #['5th item']
result = html.xpath('//li[position()<3]/a/text()') #位置小雨3的li节点，也就是序号为1和2的节点
print(result) #['1st item', '2nd item']
result = html.xpath('//li[last()]/a/text()') #选取倒数第三个li节点 last方法-2因为last方法代表最后一个
print(result) #['5th item']

#14 节点轴选择
from lxml import etree
text = '''
<div>
    <ul>
        <li class ="item-0"><a href="link1.html">1st item</a></li>
        <li class ="item-1"><a href="link2.html">2nd item</a></li>
        <li class ="item-inactive"><a href="link3.html">3rd item</a></li>
        <li class ="item-1"><a href="link4.html">4th item</a></li>
        <li class ="item-0"><a href="link5.html">5th item</a> 
    </ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*') #所有祖先节点，包括html, body, div, ul
print(result) #[<Element html at 0x105b6c340>, <Element body at 0x105913d80>, <Element div at 0x105bbd280>, <Element ul at 0x105bbd140>]
result = html.xpath('//li[1]/ancestor::div') #只有div节点
print(result)  #[<Element div at 0x10e385600>]
result = html.xpath('//li[1]/attribute::*') #li节点的所有属性
print(result) #['item-0']
result = html.xpath('//li[1]/child::a[@href="link1.html"]') #获取直接子节点，限定条件属性为link1,html的a节点
print(result) #[<Element a at 0x10b4a7e00>]
result = html.xpath('//li[1]/descendant::span')#子孙节点，限定条件只包含span节点，不包含a节点
print(result) #[]?应该是其他的
result = html.xpath('//li[1]/following::*[2]') #获取当前节点之后的所有节点。加了索引2只获取了第2个后续节点
print(result) #[<Element a at 0x101ddfd80>]
result = html.xpath('//li[1]/following-sibling::*') #获取当前节点后的所有同级节点。*所有。
print(result) #[<Element li at 0x1020dd700>, <Element li at 0x1020dd5c0>, <Element li at 0x1020dd680>, <Element li at 0x1020dd600>]



