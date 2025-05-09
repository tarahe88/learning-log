'''
XPath（XML Path Language） 是一种用于在 XML 和 HTML 文档中定位节点的语言。
在爬虫中，XPath 常用于解析和提取网页数据，尤其是在处理复杂的 HTML 结构时非常高效
以下是新手学习 XPath 需要掌握的核心知识和技巧。
8. XPath 与正则表达式的对比
XPath：适合处理结构化数据（如 HTML/XML），语法直观，支持层级定位。
正则表达式：适合处理非结构化文本，灵活性高，但语法复杂。
'''
# 1. XPath 的作用
            # 定位节点：通过路径表达式定位 HTML/XML 文档中的元素。
            # 提取数据：从定位的节点中提取文本、属性等数据。
            # 过滤数据：通过条件筛选出符合条件的节点。
# 2. XPath 的基本语法
# 2.1 节点类型
            # 元素节点：HTML 标签，如 <div>、<p>。
            # 属性节点：标签的属性，如 href、class。
            # 文本节点：标签内的文本内容。
# 2.2 路径表达式
'''
/:从根节点开始定位
//：从当前节点开始，递归查找所有符合条件的节点
.: 当前节点
..:父节点
*: 匹配任意节点
@：选择属性
'''
# 2.3 示例
'''
<html>
    <body>
        <div id = "content">
            <p class = "title">Hello, World!</p>
            <a href = "https://example.com">Visit Example</a>
        </div>
    </body>
</html>
————————————————————————————————————————————————————————————————————————————————————————————————————
XPath表达式	                          说明	                              匹配结果
/html/body/div	               从根节点开始查找 <div>	                 <div id="content">...</div>
//div	                       查找文档中所有的 <div>	                 <div id="content">...</div>
//p[@class="title"]	           查找 class 为 title 的 <p>	         <p class="title">Hello, World!</p>
//a/@href	                   查找所有 <a> 的 href 属性	             https://example.com
//div/p/text()	               查找 <div> 下 <p> 的文本内容	         Hello, World!
'''
# 3. XPath的常用函数
            # text(): 获取节点的文本内容
            # contains(): 判断节点是否包含某字符串
            # starts-with(): 判断节点的属性火文本是否以某字符串开头。
            # last() : 选择最后一个节点
            # position(): 选择特定位置的节点
'''
示例：
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

——————————————————————————————————————————————————————————————————————————————————————————————————
XPath表达式	                          说明	                 匹配结果
//li[1]	                        选择第一个 <li>	           <li>Item 1</li>
//li[last()]	                选择最后一个 <li>	           <li>Item 3</li>
//li[contains(text(), "2")]	    选择文本包含 "2" 的 <li>	   <li>Item 2</li>
//li[position() < 3]	        选择前两个 <li>	           <li>Item 1</li>, <li>Item 2</li>
'''
# 4. Python 中使用 XPath。 Python 中常用 lxml 库或 scrapy 框架来解析 HTML 并使用 XPath。
# 4.1 安装 lxml pip install lxml
# 4.2 使用lxml解析html
from lxml import etree # etree是一个解析xml文档的一个python库
html = '''
<html>
    <body>
        <div id="content">
            <p class="title">Hello, World!</p>
            <a href="https://example.com">Visit Example</a>
        </div>
    </body>
</html>
'''
# 解析 HTML
tree = etree.HTML(html)
# 使用xpath提取数据
title = tree.xpath('//p[@class="title"]/text()')[0]
link = tree.xpath('//a/@href')[0]

print("标题:",title) # 输出：标题: Hello, World!
print("链接:",link)  #输出：链接 https://example.com

## 5. XPath在爬虫中的应用。
# 5.1 提取文本
text = tree.xpath('//p/text()')
print(text) # 输出：['Hello, World!']
# 5.2 提取属性
href = tree.xpath('//a/@href')
print(href)  # 输出：['https://example.com']
# 5.3 提取多个元素
items = tree.xpath('//li/text()')
print(items) # 输出: ['Item 1', 'Item 2', 'Item 3']
# 5.4 条件过滤
# 提取 class包含 "active"的<li>
active_items = tree.xpath('//li[contains(@class,"active")]/text()')
print(active_items)

# 7 示例：爬虫 + XPath 以下是一个简单的爬虫示例，使用 XPath 提取网页中的标题和链接。
import requests
from lxml import etree
url = "https://example.com"
response = requests.get(url)
html = response.text
# 解析HTML
tree = etree.HTML(html)
# 提取标题
title = tree.xpath('//title/text()')[0]
print("标题：", title)
# 提取所有链接
links = tree.xpath('//a/@href')
print("链接：", links)







'''
6. XPath 学习建议
掌握基础语法：先熟悉路径表达式和常用函数。

使用开发者工具：在浏览器中右键点击元素，选择“检查”，然后复制 XPath。

多练习：通过实际爬虫项目练习 XPath。

结合工具：使用在线 XPath 测试工具（如 XPath Tester）调试和验证 XPath。'''














