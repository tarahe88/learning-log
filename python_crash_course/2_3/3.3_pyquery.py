# bs的css选择器功能没那么强大。乳沟你对web编程了解，比较喜欢用css选择器，对jQuery了解，那么更适合你的解析库pyquery
#2 初始化-解析HTML文本的时候，先将其初始化为一个pyquery对象。 （直接传入字符串，传入url,传入文件名等）
html = '''
<div>
    <ul>
        <li class='item-0'>first item</li>
        <li class='item-1'><a href='link2.html'>second item</a></li>
        <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
        <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
        <li class='item-0'><a href='link5.html'>fifth item</a></li>
    </ul>
</div>
'''
from pyquery import PyQuery as pq, PyQuery  # 引入PyQuer 取别名为pq.
doc = pq(html) #声明一个长html字符串，当作参数传递给Pyquery类。这样就完成了初始化。
print(doc('li')) # 将初始化对象传入CSS选择器。这个实例中，传入li节点，这样可以选择所有的li节点
"""
<li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
"""
#URL初始化。 初始化的参数除了字符串，还能是网页的URL. 只需要制定Pyquery对象的参数为url
from pyquery import PyQuery as pq
doc = pq(url='https://cuiqingcai.com') #pq对象首先请求这个url，然后用得到的Html内容完成初始化
print(doc('title')) #<title>静觅丨崔庆才的个人站点 - Python爬虫教程</title> #相当于把网页的源代码以字符串形式传给pq完成初始化

#文件初始化 除了html文本， url初始化，还可以传递本地的文件名。此时将参数指定为filename即可。
##from pyquery import PyQuery as pq
##doc = pq(filename='demo.html') #这里需要一个本地html文件demo.html.
##print(doc('li'))

#3 基本CSS选择器 pyquery库的css选择器用法
html = '''
<div id='container'>
    <ul class='list'>'
        <li class='item-0'>first item</li>
        <li class='item-1'><a href='link2.html'>second item</a></li>
        <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
        <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
        <li class='item-0'><a href='link5.html'>fifth item</a></li>
    </ul>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li')) #初始化pyquery对象后，传入了一个css选择器#container .list li,意思是先选取id为container的鸡诶单，再选取内部class为
#list的节点内部的所有li节点，然后打印输出。 这里没有写正则表达式，直接通过选择器和text方法，得到了想要提取的文本信息。方便多了。
'''
<li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
'''
# 4 查找节点
# 子节点 需要用到find方法，参数是css选择器。还是以上面html为例。
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
print(type(items)) #<class 'pyquery.pyquery.PyQuery'>
print(items)
lis = items.find('li') #find查找范围是节点的所有子孙节点。如果只想查找子节点，用children lis = items.children()
print(type(lis)) #<class 'pyquery.pyquery.PyQuery'>
print(lis)
'''
<ul class="list">'
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
'''
"""
<li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
"""
## children()子节点"
print("# children()子节点")
lis = items.children()
print(type(lis))
print(lis)
# 筛选出字节点中class为active的节点，向children方法传入css选择器.active"
print("# 筛选出字节点中class为active的节点，向children方法传入css选择器.active")
lis = items.children(".active")
print(lis)

##父节点  parent方法
print("父节点 parent方法")
html = '''
<div class="wrap">
    <div id="container">
        <ul class ="list">
            <li class='item-0'>first item</li>
            <li class='item-1'><a href='link2.html'>second item</a></li>
            <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
            <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
            <li class='item-0'><a href='link5.html'>fifth item</a></li>
        </ul>
    </div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
items = doc(".list") #先用.list选取class为list的节点，然后调用parent方法得到父节点，类型依然为PyQuery
container = items.parent()
print(type(container))
print(container)

##祖先节点  parents方法 父节点的父节点
print("祖先节点  parents方法")
from pyquery import PyQuery as pq
doc = pq(html)
items = doc(".list") #先用.list选取class为list的节点，然后调用parent方法得到父节点，类型依然为PyQuery
parents = items.parents()
print(type(parents))
print(parents) #返回结果2个，1个是class为wrap的节点，一个是id为container的节点。也就是说parents方法返回所有祖先节点

##筛选某个祖先节点，可以向parents方法传入css选择器，会返回祖先节点中符合css选择器的节点
print("#筛选某个祖先节点，可以向parents方法传入css选择器，会返回祖先节点中符合css选择器的节点")
parent = items.parents('.wrap')
print(parent) #只保留了class为wrap的节点。

##兄弟节点siblings
print("##兄弟节点siblings")
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active') #中间空格，不然运行是空白
print(li.siblings('.active')) #class为active的兄弟节点，只有第四个li节点满足。

## 5 遍历节点 pq库选择结果可能是多个节点也可以是单个节点，类型都是pq，没有bs那样返回列表
print("# 5 遍历节点 ##如果结果是单个节点，既可以直接打印输出，也可以直接转成字符串")
##如果结果是单个节点，既可以直接打印输出，也可以直接转成字符串
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active') #多个节点遍历 li = doc('li').items()
print(li)
print(str(li))
print("# 如果结果是多个节点，需要遍历获取，需要调用items方法")
from pyquery import PyQuery as pq
doc = pq(html)
lis = doc('li').items() #单个节点li = doc('.item-0.active')
print(type(lis)) #调用items方法后，得到一个生成器，对其进行遍历，就可以卓哥得到li节点对象。
for li in lis:
    print(li,type(li))
##获取信息  提取到节点后，最终目的是提取节点包含的信息。比较重要的信息2类，1类属性，2是文本
## 获取属性：提取到pq类型的节点后，调用attr方法获取属性
print("#获取信息中的属性")
html = '''
<div class="wrap">
    <div id="container">
        <ul class ="list">
            <li class='item-0'>first item</li>
            <li class='item-1'><a href='link2.html'>second item</a></li>
            <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
            <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
            <li class='item-0'><a href='link5.html'>fifth item</a></li>
        </ul>
    </div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a') #选中class为item-0和active的li节点内的a节点，类型是pq类型
print(a, type(a))
print(a.attr('href')) #调用attr方法，传入属性名称，得到对应的属性值。 #也可以调用attr属性获取属性之。 print(a.attr.href) 结果一样。
##注意当返回结果包含多个节点时，调用attr方法时，返回结果只会得到第一个节点的属性。
print("##注意当返回结果包含多个节点时，调用attr方法时，返回结果只会得到第一个节点的属性。想要获取所有属性，用遍历")
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('a')
for item in a.items(): #用遍历获取所有属性
    print(item.attr('href'))

## 获取文本 用text方法实现
print("## 获取文本用text方法实现")
html = '''
<div class="wrap">
    <div id="container">
        <ul class ="list">
            <li class='item-0'>first item</li>
            <li class='item-1'><a href='link2.html'>second item</a></li>
            <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
            <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
            <li class='item-0'><a href='link5.html'>fifth item</a></li>
        </ul>
    </div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a') #首先选中a节点，
print(a)
print(a.text()) #然后调用text方法。 此时text方法会忽略节点内部包含的所有html,只返回纯文字内容
##获取节点内部的html文本，需要用html方法
print("##获取节点内部的html文本，需要用html方法")
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active') #这里选中了第三个li节点，调用html方法，返回解雇应该是li节点内的所有html文本
print(li)
print(li.html())
## 选中多个节点， html方法返回第1个节点内部的html文本-需要遍历，text返回所有li节点内部的纯文本-不需要遍历。
print("## 选中多个节点， html方法返回第1个节点内部的html文本-需要遍历，text返回所有li节点内部的纯文本-不需要遍历。")
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li') #选中多个节点，
print(li.html) #html方法只返回第一个，想要返回所有需要遍历
print(li.text()) #返回所有，text方法不需要遍历
print(type(li.text()))
