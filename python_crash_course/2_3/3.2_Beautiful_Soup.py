# #第2章讲了正则表达式，一旦正则写的有问题，得到的结果就不是想要的。 每个网页有一定的特殊结构和层级关系。很多节点都用id或class作区分。 借助结构属性来踢去
# #beautiful soup借助网页的结构和属性等特性来解析网页。不需要写复杂的正则表达式，只需要简单的几个语句，就可以完成某个元素的提取
# #beautiful soup是python的一个html 或 xml解析库。
# #支持第三方解析起入lxml. BeautifulSoup(markup, "html.parser"/"lxml"/"xml"/"html5lib")
# #使用LXML解析起，只需初始化beautiful soup时，把第二个参数改为lxml
# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>Hello</p>', "lxml")
# # print(soup.p.string) #Hello
# # 4 基本使用
# html = """
# <html><head><title> The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once Upon a time there were little sisters; and their names were
# <a href="https://example.com/elise" class="sister" id = "link1"><!--Elsie--></a>,
# <a href="https://example.com/lacie" class="sister" id = "link2"><!--Lacie--></a> and
# <a href="https://example.com/tillie" class="sister" id = "link3"><!--Tillie--></a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml") #第1个参数是html变量，第2个参数是解析起的类型lxml。beautifulsoup对象初始化。
# # print(soup.prettify()) #html文本 #prettify方法把要解析的字符串以标准的缩进格式输出。
# print(soup.title.string) # The Dormouse's story #输出html中title节点的文本内容。选出title节点，调用string属性得到title节点老爹文本内容
# print(soup.a.string) #Elsie
#
# #5 节点选择器。
# html = """
# <html><head><title> The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once Upon a time there were little sisters; and their names were
# <a href="https://example.com/elise" class="sister" id = "link1"><!--Elsie--></a>,
# <a href="https://example.com/lacie" class="sister" id = "link2"><!--Lacie--></a> and
# <a href="https://example.com/tillie" class="sister" id = "link3"><!--Tillie--></a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.title) #<title> The Dormouse's story</title>
# print(type(soup.title)) #<class 'bs4.element.Tag'> 这是bs的一种重要数据结构，tag具有一些属性，比如string属性调用
# #调用string属性可以得到节点的文本内容。
# print(soup.title.string) # The Dormouse's story
# print(soup.head) #<head><title> The Dormouse's story</title> </head>
# print(soup.p) #<p class="title" name="dromouse"><b>The Dormouse's story</b></p> #当有多个节点时，这种选择方式只会选择到第一个匹配的节点
#
# # 6 提取信息
# #获取名称
# print(soup.title.name) #title #选取title节点，调用name属性
#
# #获取属性 #一个节点多个属性比如id, class
# print(soup.p.attrs) #{'class': ['title'], 'name': 'dromouse'}
# print(soup.p.attrs["name"]) #dromouse #相当于从字典中获取某个键值，只需要中括号加属性名就可以
# #获取属性更简单的方法
# print(soup.p["name"]) # dromouse #属性是唯一，所以返回的是单个字符串
# print(soup.p["class"]) #['title']  # 一个节点包含多个class，所以返回的是列表
#
# #获取内容
# print(soup.p.string) #The Dormouse's story #注意这里选取的p节点是第一个p节点。获取的文本也是第一额p节点里的文本
# #嵌套选择
# html = """
# <html><head><title>The Dormouse's story</title></head>
#  <body>
#  """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.head.title) #<title>The Dormouse's story</title> #调用head后再调用title而选择的title节点
# print(type(soup.head.title)) #<class 'bs4.element.Tag'> #类型仍然是tag类型
# print(soup.head.title.string) #The Dormouse's story #title节点里的string属性，也就是节点里的文本内容

#7 关联选择。 有时不能一步就选到想要的节点，需要先选中某一个节点，以它为基准再选择子节点，父节点，兄弟节点。
#子节点和子孙节点
html = """
<html>
    <head>
        <title> The Dormouse's story</title>
    </head>
<body>
    <p class="story">
        Once Upon a time there were little sisters; and their names were
        <a href="https://example.com/elise" class="sister" id = "link1">
            <span>Elsie</span>,
        </a>
        <a href="https://example.com/lacie" class="sister" id = "link2">Lacie</a> 
        and 
        <a href="https://example.com/tillie" class="sister" id = "link3">Tillie</a>
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.p.contents) # ['\n Once upon a time there] 返回的是列表形式,p节点既包含文本，又包含节点，这些内容以列表形式一一返回。
# #同样，可以调用children属性得到相应的结果
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.p.children) #<list_iterator object at 0x103e65630> #调用children属性，返回生成器类型。
# for i, child in enumerate(soup.p.children):
#     print(i,child) # 0 Once Upon a time there were little sisters; and their names were
# #如果要得到所有的子孙节点，则可待用descendants属性
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.p.descendants) #<generator object Tag.descendants at 0x10790be00> #返回结果还是生成器
# for i, child in enumerate(soup.p.descendants):
#     print(i,child) #但是输出结果中就包含了span节点，因为descendants会递归查询所有的子节点，得到所有的子孙节点

#父节点和祖先节点。 父节点parent属性
html = """
<html>
    <head>
        <title> The Dormouse's story</title>
    </head>
<body>
    <p class="story">
        Once Upon a time there were little sisters; and their names were
        <a href="https://example.com/elise" class="sister" id = "link1">
            <span>Elsie</span>,
        </a>
    </p>
    <p class="story">...</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.a.parent) #<p class="story"> Once Upon <a class="sis" hr <span> </p> a节点的父节点是p节点，所以结果是p节点及其内容
#如果要获取所有祖先节点，可用parents属性
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(type(soup.a.parents)) #<class 'generator'>
# print(list(enumerate(soup.a.parents))) # 用列表输出了其索引和内容，列表中的元素就是a节点的所有祖先节点

#兄弟节点=同级节点
html = """
<html>
    <head>
        <title> The Dormouse's story</title>
    </head>
<body>
    <p class="story">
        Once Upon a time there were little sisters; and their names were
        <a href="https://example.com/elise" class="sister" id = "link1">
            <span>Elsie</span>,
        </a>
        Hello
        <a href="https://example.com/lacie" class="sister" id = "link2">Lacie</a> 
        and 
        <a href="https://example.com/tillie" class="sister" id = "link3">Tillie</a>
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print("Next Sibling", soup.a.next_sibling) #Next Sibling  Hello
# print("Prev Sibling", soup.a.previous_sibling) # Prev Sibling Once Upon a time there were little sisters; and their names were
# print("Next Siblings", list(enumerate(soup.a.next_siblings))) #Next Siblings [(0, '\n
# print("Prev Siblings", list(enumerate(soup.a.previous_siblings))) #Prev Siblings [(0, '\n

#提取信息 前面讲过关联元素节点的选择方法，如果想要获取它们的信息比如文本属性，也可以用同样的方法
html = """
<html>
    <body>
        <p class="story">
            Once Upon a time there were little sisters; and their names were
            <a href="https://example.com/elise" class="sister" id ="link1">Bob</a><a href=
                    "https://example.com/lacie" class="sister" id ="link2">Lacie</a> 
        </p>
"""
# #如果返回的是单个节点，可以直接调用string, attrs等属性获得文本和属性，
# # 如果返回包含多个节点的生成器，先将结果转为列表再从中取出某个原色，之后调用string, attrs等属性获得相应节点的文本和属性。
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print("Next Sibling:") #Next Sibling:
# print(type(soup.a.next_sibling)) #<class 'bs4.element.Tag'>
# print(soup.a.next_sibling) #<a class="sister" href="https://example.com/lacie" id="link2">Lacie</a>
# print("Parent:") #Parent:
# print(type(soup.a.parents)) #<class 'bs4.element.Tag'>
# print(list(soup.a.parents)[0]) #<p class="story"> Once Upon <a class="sister" </p>
# print(list(soup.a.parents)[0].attrs["class"]) #['story']

#8  方法选择器。 前面讲的都是基于属性选择的。bs提供了查询方法，find_all, find等。
#find_all(name, attrs, recursive, text, **kwargs)
#name
html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id = "list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"lxml")
# print(soup.find_all(name="ul")) #调用方法find_all,传入name参数，参数值为ul. 意思是查询素有ul节点。返回结果是列表类型。
"""
[<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>, <ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>]
"""
# print(type(soup.find_all(name="ul")[0])) #<class 'bs4.element.Tag'>
#因为都是tag类型，可以潜逃查询。 先查询所有ul节点，再继续查询其内部li节点
# for ul in soup.find_all(name="ul"):
#     print(ul.find_all(name="li"))
"""
[<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
[<li class="element">Foo</li>, <li class="element">Bar</li>]
"""
# # 接下来遍历每个li节点，并获取它的文本内容
# for ul in soup.find_all(name="ul"):
#     print(ul.find_all(name="li")) #同上
#     for li in ul.find_all(name="li"):
#         print(li.string) #Foo Bar Jay Foo Bar

# attrs 除了根据节点查询，也可以传入一些属性进行查询
html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.find_all(attrs={"id":"list-1"})) #传入attrs参数，属于字典类型。得到的符合id=list-1这一条件的所有节点。
# '''
# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]'''
# print(soup.find_all(attrs={"name":"elements"}))
# '''
# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]'''
# # 对于常用的属性比如id, class等。可以不用attrs传递。 可以直接传入id这个参数
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.find_all(id='list-1')) #直接传入id='list-1"就可以查询id为list-1的节点元素。
# print(soup.find_all(class_='element'))#由于class在python是一个关键字，所以后面需要加一个下划线。

#text text参数可以用来匹配节点的文本，其传入形式可以是字符串，也可以是正则表达式对象，
import re
html = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link too</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"lxml")
print(soup.find_all(string=re.compile('link'))) #书上是text,弃用警告，用string.2个a节点内部含文本信息。find_all方法传入text也就是string参数，为正则表达式。返回结果是由所有与正则表达式相匹配的节点文本组成的列表。
# '''['Hello, this is a link', 'Hello, this is a link too']'''

#find 除了find_all还有find也可以查询。只不过find返回的是单个元素，也就是第一个匹配的元素。find_all返回所有匹配的元素组成的列表
html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.find(name='ul')) #返回的结果不是列表形式，而是第一个匹配的节点元素
# '''<ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>'''
# print(type(soup.find(name='ul'))) #<class 'bs4.element.Tag'>
# print(soup.find(class_='list')) ##返回的结果不是列表形式，而是第一个匹配的节点元素
'''<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>'''
'''find_parents和 find_parent:前者返回所有祖先节点，后者返回直接父节点
find_next_siblings和 find_next_sibling: 前者返回素有兄弟节点，后者返回第一个兄弟节点
find_all_next和 find_next: 前者返回节点后面所有符合条件的节点，后者返回后面第一个符合条件的节点
find_all_previous和 find_previous: 前者返回节点前面所有符合条件的节点，后者返回前面第一个符合条件的节点
'''

## 9 CSS选择器。只需要调用select方法，传入相应的CSS选择器即可。
html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"lxml") #下面用了3次CSS选择器
print(soup.select('.panel .panel-heading')) #注意空格  #[<div class="panel-heading"> <h4>Hello</h4> </div>]
print(soup.select('ul li')) # 所有ul节点下面的所有li机诶单。结果是所有li节点组成的列表
## '''#[<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>, <li class="element">Foo</li>, <li class="element">Bar</li>]
print(soup.select('#list-2 .element')) #[<li class="element">Foo</li>, <li class="element">Bar</li>]
print(type(soup.select('ul')[0])) #<class 'bs4.element.Tag'>

#嵌套选择。 select方法也支持潜逃选择。比如先选择所有ul节点，再便利每个ul节点，选择其li节点
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"lxml")
for ul in soup.select('ul'):
    print(ul.select("li"))
    #[<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
    #[<li class="element">Foo</li>, <li class="element">Bar</li>]

#获取属性
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"lxml")
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])  #直接将属性名传入中括号和通过attrs属性获取属性值，可以成功获取属性
'''list-1
list-1
list-2
list-2'''

#获取文本。除了用前面的string属性，还有一个方法就是get_text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"lxml")
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print("String:", li.string)
''' Get Text: Foo
String: Foo
Get Text: Bar
String: Bar
Get Text: Jay
String: Jay
Get Text: Foo
String: Foo
Get Text: Bar
String: Bar'''

"""总结：
推荐使用LXML解析库，必要时使用html.parser. 
节点选择器筛选功能弱，但是速度快
建议使用find, find_all方法查询匹配的单个结果或者多个结果。
如果对CSS选择器熟悉，则可以使用select选择法"""