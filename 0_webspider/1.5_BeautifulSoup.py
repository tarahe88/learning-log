##Python 的第三方库，用于解析 HTML 和 XML 文档。BeautifulSoup 是 Python 爬虫的利器，掌握其使用方法至关重要。
## 1 安装beautifulsoup, 2 创建beautifulsoup对象， 3 查找元素 ， 4提取数据
### 1 创建beautifulsoup对象
from bs4 import BeautifulSoup
html = '''
<html>
    <head><title>网页标题</title></head>
    <body>
        <h1>这是一个标题<h1>
        <p class="content">真丝一个i额段落。</p>
        <a href = 'https://www.example.com">这是一个链接</a>
    </body>
</html>
'''
import requests
#发送请求，获取网页内容
url = "https://www.example.com"
response = requests.get(url)
html = response.text #此处与前面html重复，所以黄色波浪线
# 1 创建beautifulsoup对象
soup = BeautifulSoup(html, "html.parser")
#提取标题
title = soup.title.string
print(title)
#提取所有链接
links = soup.find_all("a")
for link in links:
    print(link["href"])
#提取所有图片
images = soup.find_all("img")
for image in images:
    print(image("src"))
#以下是beautifulsoup常用的查找和提取数据的方法。
'''
1. 查找元素：
标签名:soup.find("h1"), soup.find_all("p")
属性:soup.find("p", class="content"),soup.find_all("a",href=True)
CSS选择器: soup.select("h1"), soup.select("p.content"),soup.select("a[href]")
'''
#查找第一个<h1>标签 find(): 查找第一个匹配的元素。 语法：find(name, attrs, recursive, string, **kwargs)
import bs4
h1 = soup.find("h1")
#查找第一个class为“content“的<p>标签
p = soup.find("p", class_="content")
#查找第一个包含"Python"文本的<a>标签
a = soup.find("a", string="Python")
'''
find_all(): 查找所有匹配的元素。
语法：find_all(name, attrs, recursive, string, limit, **kwargs)
'''
#查找所有<a>标签
links = soup.find_all("a")
#查找所有class为"content“的<p>标签
paragraphs = soup.find_all("p", class_="content")
#查找所有包含"Python“文本的<a>标签
python_links = soup.find_all("p", string="Python")
'''
select(): 使用 CSS 选择器查找元素。
语法：select(selector)
'''
#查找所有<h1>标签
h1_list = soup.select("h1")
#查找所有class为"content"的<p>标签
p_list = soup.select("p.content")
#查找所有包含href属性的<a>标签
a_list = soup.select("a[href]")
'''
2. 提取数据：
标签文本element.text， 
属性值:element["href"], 
标签名:element.name
标签文本: element.text
'''
#提取<h1>标签的文本
title = h1.text
'''
属性值：element["attribute_name"]
'''
#提取<a>标签的href属性值
link = a['href']
#提取<img>标签的src属性值
img_url=img["src"]
'''
标签名element.name
'''
# 获取标签名
tag_name = element.name
'''
3.遍历元素：for循环遍历find_all()或slecet()返回的列表
'''
#遍历所有<a>标签，提取链接
for a in soup.find_all("a"):
    print(a["href"])
#或者
for p in soup.find_all("p"):
    print(p.text)
'''
4.处理嵌套结构：
链式调用：在找到的元素上继续调用find()或find_all()
'''
#查找<div>标签下的第一个<h1>标签
h1 = soup.find("div").find("h1")
#查找<ul>标签下的所有<li>标签
li_list = soup.find("ul").find_all("li")
#处理嵌套也可以这样
for div in soup.find_all("div"):
    h1 = div.find("h1")
    if h1:
        print(h1.text)
'''
其他常用方法：
get_text()：获取元素及其子元素的文本内容
prettify():格式化输出html文档
parent:获取父元素
children:获取子元素
'''
