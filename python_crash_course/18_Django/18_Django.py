'''
操作：
确保文件里的代码正确后
1-  source 11_env/bin/activate    --激活虚拟环境source 11_env/bin/activate    --激活虚拟环境
2-  启动服务器：python manage.py runserver
python manage.py runserver
出现 Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
代表正常。

# 优先使用 manage.py：这是 Django 项目的标准入口。
'''
'''
2. 使用 Python 3 创建虚拟环境
bash
# 明确使用 python3 创建虚拟环境
python3 -m venv 11_env
3. 激活虚拟环境
bash
source 11_env/bin/activatepip install django-bootstrap3
'''
# 当今网站实际上都是富应用程序 rich application. 就像成熟的桌面应用程序一样。 python提供了一组开发web应用程序的卓越工具
# 学习用django(https://djangoproject.com/)开发一个名为学习笔记（learning log)的项目。 在线日志项目。
# django是一个web框架，一套用于帮助开发交互式网站的工具。
# django响应网页请求，还能让你更轻松的读写数据库，管理用户等。

# 18.1.1 制定规范。
# 完整的规范详细说明了项目的目标，阐述了项目的功能，并讨论了项目的外观和用户界面。
'''
我们要编写一个名为‘学习笔记的’的web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条目。
‘学习笔记‘的主页对这个网站进行描述，并邀请用户注册或登录。 用户登录后，就可以创建主题，添加新条目以及阅读既有的条目
'''

# 18.1.2 建立虚拟环境
# 虚拟环境是系统的一个位置，可以在其中安装包，并将其与其他python包隔离。
# 命令 python -m venv 11_env 运行了模块 venv，并使用它来创建一个名为11_env的虚拟环境
# 不知道为啥，我的电脑要用python3 -m venv 11_env .python后面要跟3才行

# 18.1.3 安装 virtualenv 如果系统不能使用模块venv python3 -m venv 11_env  source 11_env/bin/activate

# 18.1.4 激活虚拟环境。 建立虚拟环境后，需要使用下面的命令激活它：

# source 11_env/bin/activate     激活之后显示 (11_env)leaning_log$
# 这个命令运行11_env/bin中的脚本activate。环境处于活动状态时，环境名将包含在括号内，如(11_env)learning_log$.
# 你在11_env中安装的包仅在该环境处于活动状态时可用。

# 18.1.5 安装 django pip install django
# 环境处于激活后，就可以安装Django了: pip install Django
# 因为我们在虚拟环境中工作，因此在所有的系统中，安装Django的命令都相同：不需要指定标志--user，
# 也无需使用python -m pip install package_name这样较长的命令

# 18.1.6 在django中创建项目
# 在依然处于活动的虚拟环境的情况下(11_env包含在括号内)，
# /// 执行如下命令来新建一个项目:django-admin startproject learning_log
# 该命令让Django新建一个名为learning_log的项目
# 运行命令 ls ，结果表明Django新建了一个名为learning_log的目录，还创建了一个名为manage.py的文件。
# manage.py是一个简单的程序，接受命令，并将其交给Django的相关部分去运行。我们将使用这些命令来管理注入使用数据库和运行服务器等任务
# 运行命令 ls learning_log 结果表明learning_log包含4个文件 __init__.py, setting.py, urls.py, wsgi.py

# learning_log 中最重要的.settings.py, urls.py和wsgi.py
# settings.py 指定django如何与你的系统交互以及如何管理项目.开发中我们会修改一些设置，添加一些设置。
# urls.py 告诉django 应创建哪些网页来响应浏览器请求
# wsgi.py 帮助django提供它创建的文件。这个文件名是 web server gateway interface(web服务器网关接口）的首字母缩写

# 18.1.7 创建数据库 python manage.py migrate
# Django将大部分与项目相关的信息都存储在数据库中，因此我们需要创建一个供Django使用的数据库。
# 为项目“学习笔记‘创建数据库，请在处于活动虚拟环境中的情况下执行下面的命令：python manage.py migrate
#我们将修改数据库称为前一数据库。首次执行命令migrate时，将让Django确保数据库与项目的当前状态匹配。
# 在使用SQLite（后面将更详细介绍）的新项目首次执行这命令时，Django
# 输出结果 Django指出它将创建必要的数据库表，用于存储我们将在这个项目中使用的信息，。。。。。
# 运行命令ls， 输出表明Django又创建了一个文件 db.sqlite3
# db.sqlite3  是一种使用单个文件的数据库，是编写简单应用程序的理想选择，因为它让你不用太关注数据库管理的问题。

# 18.1.8 核实django是否正确的创建了项目
# /// 执行命令  python manage.py runserver
# Django启动一个服务器，让你能够查看系统中的项目，了解它们的工作情况。
# 当你在浏览器输入URL以请求网页时，该Django服务器将进行响应：生成合适的网页，并将其发送给浏览器。
# Django 项目必须通过 manage.py 或设置环境变量来加载配置：
# 优先使用 manage.py：这是 Django 项目的标准入口。
'''
System check identified no issues (0 silenced).             # django通过检查确认正确的创建了项目
April 11, 2025 - 01:05:08
Django version 5.2, using settings 'learning_log.settings'  # 使用的django版本以及当前使用的设置文件名称
Starting development server at http://127.0.0.1:8000/       # 指出项目url。
#表明项目将在你的计算机localhost的端口8000上侦听请求。localhost是一种只处理当前系统发出的请求，而不允许其他任何人查看你正在开发的网页服务器
Quit the server with CONTROL-C.
'''
# http://127.0.0.1:8000/            # 这个页mmk面是 Django创建的，让你知道到目前为止一切正常。

# 退出上一个虚拟环境deactivate
'''练习：18-1 新项目：
创建两个空项目，看看Django创建了什么
新建一个文件夹，名称：InstaBook 或 FaceGram(不要在learning_log中新建），
在终端中切换到该文件夹，并创建一个虚拟环境。
在这个虚拟环境中安装Django，并执行命令 django-admin.py startproject instabook.(不要忘了这命令末尾的句点）

1.创建第一个项目FaceGram
# 创建项目文件夹
mkdir FaceGram
cd FaceGram
# 创建虚拟环境
python -m venv fg_venv
# 激活虚拟环境
source venv/bin/activate

# 创建项目文件夹
mkdir FaceGram
cd FaceGram

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装Django
pip install django

# 创建项目(注意末尾的句点)
django-admin startproject facegram .

2 创建第二个项目Instagram
# 返回上级目录
cd ..

# 创建第二个项目文件夹
mkdir InstaBook
cd InstaBook

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装Django
pip install django

# 创建项目(注意末尾的句点)
django-admin startproject instabook .

'''

# 18.2 创建应用程序 # learning_logs
# django项目由一系列应用程序组成，他们协同工作，让项目成为一个整体。
# 在前面打开的终端窗口应该还运行着runserver.
# 请再打开一个终端窗口（或标签页），并切换到mange.py所在的目录。激活该虚拟环境，再执行命令startapp
'''source 11_env/bin/activate    --激活虚拟环境
python manage.py startapp learning_logs ---新增一个文件夹叫learning_logs
ls ---查看项目目录，就会发现里面有4个 db.sqlite3 learning_log learning_logs, 11_env manage.py
ls learning_logs/ ----看看 learning log下有啥 '__init__.py     __pycache__     admin.py        apps.py         migrations      models.py       settings.py     tests.py        views.py'
'''
# 18.2.1 定义模型 models.py -learning_logs 模型Topic
'''
我们来想想涉及的数据。每位用户都需要在学习笔记中创建很多主题。用户输入的每个条目都与特定主题相关联
条目以文本方式显示。 存储每个条目的时间戳，以便告诉用户各个条目都是什么时候创建的

'''
# 18.2.2 激活模型 settings.py
'''
要使用模型，必须让Django将应用程序包含到项目中。 所以要打开settings.py(在项目learning_log/learning_log中）
01. ///将learning_logs应用程序添加到settings.py中的元组去INSTALLED_APPS = [ ]
通过将应用程序编组，在项目不断扩大，包含更多的应用程序时，有助于对应用程序进行跟踪。
这里新建了一个My apps的片段，当前它只包含应用程序learning_logs
接下来， 需要django修改数据库，使其能够存储于模型Topic相关的信息。
02. ///终端执行命令 manage.py makemigrations learning_logs
命令makeemigrations让django确定如何修改数据库，使其能够存储于我们定义的新模型相关联的数据。。
输出表明django创建了一个名为/0001_initial.py的迁移文件，这个文件将在数据库中为模型Topic创建一个表。
我复习的时候好像创建了一个新的 0002_entry.py
接下来应用这种迁移，让django替我们修改数据库
03. ///终端执行命令 python manage.py migrate
我们需要检查的是输出行：Applying learning_logs.0001_initial... OK。在这里django确认为learning_logs应用迁移时一切正常(OK)
每当需要修改“学习笔记“管理的数据时，都采取如下三个步骤： 修改models.py; 对learning_logs调用makemigrations; 让django迁移项目
'''
# 每当需要修改“学习笔记”管理的数据时，都采取以下三个步骤：修改models.py; 对learning_logs调用makeemigrations; 让Django迁移项目

# 18.2.3 Django 管理网站
# django提供的管理网站（admin site)让你能够轻松的处理模型。 网站的管理员可以使用管理网站，普通用户不行。
# 我们建立管理网站，并通过它使用模型Topic来添加一些主题
    # 1.创建超级用户
# 创建具备所有权限的用户=超级用户。 优秀的管理员会小心对待用户的敏感信息，因为用户对其访问的应用程序有极大信任
# django中创建超级用户，终端执行命令按提示做。
#  python manage.py createsuperuser 有提示后输入用户名 密码 kim h**y*8*! 邮箱可以是空
    # 2. 向管理网站注册模型。 django自动在管理网站中添加了一些模型，如user和group，但对我们创建的模型比如Topic，必须手工注册
# 我们创建应用程序learning_log时，Django在models.py所在的目录中创建了一个名为admin.py的文件

# learning_logs中 admin.py 输入: # 为向管理网站注册Topic，请输入下面的代码(导入Topic类)
'''
from django.contrib import admin
from learning_logs.models import Topic # 导入我们要注册的模型Topic
admin.site.register(Topic) # 再使用admin.site.register()让Django通过管理网站管理我们的模型'''

# 这些代码到五我们要注册的模型，再使用admin.site.register()让Django通过管理网站管理我们的模型
# 使用超级用户账户访问管理网很赞：localhost.8000/admin/，输入用户名kim 密码h***8*!
# 如果不能访问服务器你可能没有运行 python manage.py runserver，或者服务器意外关闭了。
# 成功后，这个网站可以让你能够添加和修改用户和用户组，还可以管理与刚才定义的模型Topic相关的数据
    # 3. 添加主题。 向管理网站注册Topic后，添加第一个主题。 单击Topics进入主题网页，是空的，单击add，输入Chess， 单击Save
    #再次点击Add，并创建另一个主题Rock Climbing。 save后返回主题管理页面，包含主题chess和rock climbing
# 如果localhost访问的页面不可用，请确认你在终端窗口中运行着django服务器，如果没有，请激活虚拟环境，并执行命令python.manage.py runserver

# 18.2.4 定义模型 Entry
# 要记录学到的国际象棋和攀岩知识，需要用户可在学习笔记中添加的条目定义模型。每个条目都与特定主题相关联。
# 每个条目都与特定主题相关联，这种关系被称为多对一关系，即多个条目可关联到同一个主题
# 下面是模型Entry的代码， 在models.py里

# 18.2.5 迁移模型Entry
# 由于我们添加了一个新模型，因此需要在此迁移数据库。 ：
# 修改models.py执行命令 python manage.py makemigrations app_name 也就是learning_logs，
# 再执行命令 python manage.py migrate

# 生成了一个新的迁移文件 0002_entry.py 他告诉django如何修改数据库，使其能够存储与模型Entry相关的信息。
# 执行命令migrate,我们发现Django应用了这种迁移且一切顺利

# 18.2.6 向管理网站注册Entry
# 修改admin.py修改成类似于: import Topic, Entry, admin.site.register(Entry)
# 返回到localhost:8000/admin/ 将看到learning_logs下列出了Entries. 单击Entries的Add链接，
# 然后在 chess和rock climber下面输入一些文本

# 18.2.7 Django shell

# 输入一些数据后，就可以通过交互式终端会话以编程方式查看这些数据了。 交互式环境称为Django shell。
# 示例 python manage.py shell 在活动的虚拟环境中，命令python manage.py shell启动一个python 解释器，来探索存在项目数据库中的数据
# from learning_logs.models import Topic   Topic.objects.all() 导入模型中的模型Topic，然后使用方法all()来获取模型Topic的所有实例。 返回的是一个列表
# 这个列表称为查询集（queryset). 我们可以像遍历列表一样遍历查询集。 查看每个主题对象的ID: topics = Topic.objects.all() for topic in topics: print(topic.id, topic)
# 知道对象的ID后，就可以获取该对象并查看其任何属性。 下面看主题chess的属性text和date_added的值：
'''
t = Topic.objects.get(id=1)
t.text
t.date_added
'''
# 每次修改模型后，都需要重启shell,这样才能看到修改的效果。要退出shell对话，可按ctr+D


# 18.3 创建网页： 学习笔记主页
# 使用Django创建网页的过程分3个阶段：定义URL， 编写试图和编写模版。
# URL 模式描述了URL是如何设计的，让Django知道如何将浏览器请求与网站URL匹配，以确定返回哪个网页。
# 每个URL都映射到特定的视图，视图函数获取并处理网页所需要的数据，视图函数通常调用一个模版，后者生成浏览器能够理解的网页。
# 我们来创建学习笔记的主页。 将定义该主页的URL，编写视图函数并创建一个简单的模版

# 18.2.1 映射URL
# 用户通过浏览器输入URL以及单击链接来请求网页。我们需要确定项目需要哪些URL. 主页的URL最重要。 它是用户用来访问项目的基础URL.
# 基础URL( http://localhost:8000/) 返回默认的django网站。让我们转掉正确地建立了项目。我们家给你这个基础url映射到‘学习笔记’的主页。
# 项目主文件夹learning_log 中的文件 urls.py url(r'', include('learning_logs.urls', namespace='learning_logs')), # 添加了包含模块learning_logs的URL
# 在learning_logs中的URL创建另一个urls.py

# 错误原因：Django 4.0+ 移除了 django.conf.urls.url()，改用 path() 或 re_path()。
'''
1. 主项目 urls.py（项目根目录) 设置django后台管理，包含learning_logs的URL
2. 应用 learning_logs/urls.py  导入当前目录views.py. 定义命名空间，设置主页，设置显示所有主题/topics/，设置特定主题的详细页面/topics/1
3. 对应的view.py代码.def index-学习笔记的主页, def topics-显示所有主题， def topic-显示单个主题及所有条目

'''
# 18.3.2 编写视图
# 视图函数接受请求中的信息，准备好生成网页所需要的数据，再将这些数据发送给浏览器--这通常是使用定义了网页是什么样的模版实现的
# learning_logs中的文件views.py是你执行命令python manage.py startapp时自动生成的。
'''url请求与刚才定义的模式匹配时，django将在文件view.py中查找函数index()，再将请求对象传递给这个视图函数。
这里不需要处理任何数据，因此这个函数值包含调用render()的代码。 向函数render()提供了2个实参：原始请求对象以及一个可用于创建网页的模版
'''
# 18.3.3 编写模版
'''
模版定义了网页的结构。模版指定了网页是什么样的，而每当网页被请求时，django将填入相关的数据。 模版让你能够访问视图提供的任何数据。 
我们的主页视图没有提供任何数据，因此相应的模版非常简单。 
在文件夹learning_logs中新建一个文件夹，命名为templates. 在templates新建一个文件夹learning_logs(看着好像多余）,
但建立了django能够明确解读的结构，即便项目很大，包含很多应用程序也如此。 在最里面的learning_logs中，新建一个文件 index.html

'''

# 18.4 创建其他网页。
'''
制定创建网页的流程后，可以开始扩充‘学习笔记’项目了。 我们将创建两个现实数据的网页，其中一个列出所有的主题，另一个显示特定主题的所有条目。
对于每个网页，我们都将制定URL模式，编写一个视图函数，并编写一个模版。 这样之前，我们先创建一个父模版，项目中的其他模版都将继承它
'''
# 18.4.1 模版继承
'''
创建网站时，几乎都有一些所有网页都将包含的元素。在这情况下，可编写一个包含通用元素的父模版，
并让每个网页都继承这个模版，而不必在每个网页中重复定义这些通用元素
'''
# 1. 父模版
'''首先创建一个名为base.html的模版，并将其存储在index.html所在的目录中。 这个文件包含所有页面都有的元素。其他的模版都继承base.html
当前，所有的页面都包含的元素只有顶端的标题。我们将在每个页面中包含这个模版，因为我们将这个标题设置为到主页的链接
父模版
<p>
    <a href="{% url'learning_logs:index'%}" >Learning Log</a>
    段落含项目名，一个到主页的链接。模版标签，用大括号和百分号{% %}表示。
    模版标签{% url'learning_logs:index'%}生成一个URL,该URL与learning_logs/urls.py中定义的名为index的URL模式匹配.
    在这个示例中，learning_logs是一个命名空间，而index是该命名空间中一个名称独特的URL模式
</p>
{% block content %}{% endblock content %}  # 插入了一对块标签。这个块名为content, 是一个占位符，其中包含的信息都将由子模版指定
'''
# 让模版标签来生成URL,可让链接保持最新容易得多。 要修改项目中的URL,只需要修改urls.py中的URL模式，这样网页被请求时，django将自动插入修改后的URL
# 在我们的项目中，每个网页都将继承base.html. 因此从现在开始，每个网页都包含到主页的链接

# 2. 子模版
'''
现在需要重新编写index.html，使其继承base.html,
{% extends "learning_logs/base.html" %} # 子模版第一行必须包含标签{% extends %} 让django知道它继承了哪个父模版。
文件base.html位于文件夹learning_logs中，因此父模版路径中包含learning_logs.

{% black content %} # 插入了一个名为content的{%block%}标签，以定义content块。 不是从父模版继承的内容都包含在content块中
    <p> learning log helps you keep track of your learning, for any topic you're learning about.</p>
    # 这里是一个描述项目“学习笔记”的段落。
{% endblock content %} # 使用标签{% %} 指出了内容定义的结束位置。

模版继承的优点：在子模版中，只需包含当前网页特有的内容，不仅简化了每个模版，还是的网站修改起来容易得多。 
要修改很多网页都包含的元素，只需在父模版中修改该元素，你所做的修改将传导到继承该父模版的每个页面。 
'''
# 在大型网站中，通常有一个用于整个网站的父模版---base.html，而且网站的每个主要部分都有一个父模版。

# 18.4.2 显示所有主题的页面。
'''
有了高效的网页创建方法，就能专注另外两个网页了：显示全部主题的网页一集显示特定主题中条目的网页。 
所有主题页面显示用户创建的所有主题，它是第一个需要使用数据的网页
1.URL模式
learning_logs/urls.py
首先，定义显示所有主题的页面的URL.通常，使用一个简单的URL片段来指出网页显示的信息。 我们将使用单词topics，
因此URL http://localhost:8000/topics/将返回显示所有主题的页面。
修改learning_logs/urls.py
2.视图

learning_logs/views.py
3.模版 显示所有主题的页面模版接受字典context, 创建一个topics.html并存储到index.html所在的目录
topics.html继承base.html. 
修改父模版base.html,使其包含到显示所有主题的页面的链接

'''
# 18.4.3 显示特定主题的页面
'''
1.URL模式, learning_logs/urls.py
2. 视图
 添加新的视图函数 (learning_logs/views.py)
3. 创建特定主题的模板 (learning_logs/templates/learning_logs/topic.html)
4. 更新主题列表模板添加链接 (learning_logs/templates/learning_logs/topics.html)
'''

#





