# 20.1 设置‘学习笔记’的样式
'''
我们一直专注于项目学习笔记的功能，而没有考虑样式设置的问题，这是有意为之的。 这时一种不错的开发方法。
因为能正确运行的应用程序才是有用的。当然应用程序呢个能够正确运行后，外观就显得很重要了。
因为漂亮的应用程序才能吸引用户使用它。
本节中，简要介绍应用程序django-bootstrap3，并演示如何将其继承到项目中，为部署项目做好准备。
'''
# 20.1.1 应用车给女婿 django-bootstrap3
'''
安装django-bootstrap3,在活动的虚拟环境中执行如下命令： 
pip install django-bootstrap3 
出现错误了，解决方案
"kim@TaradeMacBook-Air webspider % python3 -m venv 11_env
kim@TaradeMacBook-Air webspider % source 11_env/bin/activate
(11_env) kim@TaradeMacBook-Air webspider % pip install django-bootstrap3
"
在setting.py末尾添加代码。 learning_logs/settings.py?? 
'''

# 20.1.2 使用Bootstrap来设置项目‘学习笔记’的样式。
'''
bootstrap基本上就是一个大型的样式设置工具集，提供了大量的模版，可以将他们应用于项目以创建独特的总体风格。 
对于bootstrap初学者来说，这些模版比各个样式设置工具使用起来要容易得多。 
查看bootstrap模版，可以访问http://getbootstrap.com/ getting strarted, examples, navbars in action.
我们将使用模版static top navbar. 提供了简单的顶部导航，页面标题和用于放置页面内容的容器。 
'''

# 20.1.3 修改 base.html。
'''
我们需要修改模版base.html以使用前述bootstrap模版。 我们把新的base.html分成几个部分进行介绍
1. 定义html头部。 修改base.html使显示学习笔记的每个页面时，浏览器标题栏都显示这个网站的名称。
删除base.html的全部代码，并输入下面的代码：
2. 定义导航栏。 定义页面顶部的导航栏。 继续修改base.html.
3. 定义页面的主要部分。 继续修改base.html
base.html的剩余部分包含页面的主要部分。 
'''

# 20.1.4 使用jumbotron 设置主页的样式
'''
使用新定义的header块以及另一个名为jumbotron的bootstrap 元素修改主页。 index.html代码
'''
# 20.1.5 设置登陆页面的样式
'''
改进登陆表单。login.html。这个好像只有在user里有login.html
'''

# 20.1.6 设置new_topic页面的样式.     learning_logs/new_topic.html
'''
修改new_topic页面，修改类似于login.html。 
'''
# 20.1.7 设置topics页面的样式。 topics.html

# 20.1.8 设置topic页面中条目的样式 topic.html
'''topic页面包含的内容比其他大部分页面都多，因此需要做的样式设置工作要多些。我们将使用bootstrap面板(panel)来突出每个条目'''

# 20.2 部署“学习笔记”
'''至此，项目‘学习笔记’的外观显得很专业了，下面将其部署到一台服务器，让任何有网络连接的人都能够使用它。为此，我们将使用Heroku
这是一个基于web的平台，让你能够管理web应用程序的部署，我们将让‘学习笔记’在heroku上运行。

# 20.2.1 建立Heroku账户。source 11_env/bin/activate
 20.2.2 安装heroku toolbelt ?
 20.2.3 安装必要的包。 dj-database-url, dj-static, static3, gunicorn
 20.2.4 创建包含列表的文件requirements.txt
 20.2.5 指定python版本. 在manage.py所在的文件夹中新建一个名为runtime.txt的文件
 20.2.6 为部署到heroku而修改settings.py
 20.2.7 创建启动进程的Procifile,不指定文件扩展名，并保存到manage.py所在的目录
 20.2.8 为部署到heroku而修改wsgi.py
 20.2.9 创建用于存储静态文件的目录
 learning_log/learning_log/static/placeholder.txt
 20.2.10在本地使用gunicorn服务器
 /// heroku local
 20.2.11 使用git跟踪项目文件
 1.安装git git --version
 2. 配置git. git跟踪睡修改了项目，即便项目由一个人开发时亦如此。为进行跟踪，git需要知道你的用户名和email. 因此你必须提供用户名。
 联系县古，可以随便伪造一个email.
 3.忽略文件
 我们无需让git跟踪项目的每个文件，因此将让git忽略一些文件，为此在manage.py所在的文件夹中创建一个名为.gitignore的文件。这个文件名以句点
 打头，且不包括扩展名。
 4.提交项目
我们需要为学习笔记初始化一个git仓库，将所有必要的文件都加入到这个仓库中，并提交项目的初始状态。
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'''
