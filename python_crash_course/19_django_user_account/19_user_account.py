# 19.1 让用户能够输入数据
'''
建立用于创建用户账户的身份验证系统之前，先添加几个页面，让用户能能够输入数据。
用户添加新主题，新条目，编辑既有条目。不想用户与管理网站交互就用django表单
使用django表单创建工具创建让用户能够输入数据的页面
'''
# 19.1.1 添加新主题
'''
 创建表单与创建网页一样：定义一个URL, 编写一个视图函数并编写一个模版。 主要差别：需要导入包含表单的模块forms.py
 1. 用于添加主题的表单。 
 让用户输入并提交信息的页面都是表单，哪怕它看起来不像表单。 用户输入信息时，我们需要验证，确认提供的信息是正确的数据类型，
 而不是恶意的信息，如中断服务器的代码。然后我们再对这些有效信息进行处理，并将其保存到数据库的合适的地方。 这些工作由django自动完成的。 
 django中，创建表单的最简单方式是使用ModelForm，它根据我们在18章定义的模型中的信息自动创建表单。 
 创建一个forms.py文件，将其储存到models.py所在的目录中，并编写你的第一个表单。
 
 2. URL模式new_topic
 这个新网页的url应简短而有描述性，因此当用户要添加新主题时，我们将切换到http://localhost:8000/new_topic的URL模式，
 我们将其添加到learning_logs/urls.py中。这个url模式将请求交给视图函数new_topic(),接下来编写视图函数
 
 3. 视图函new_topic()
 learning_logs/views.py
函数new_topic()需要处理2种情形：刚进入new_topic网页（这时应显示一个空表单）；对提交的表单数据进行处理，并将用户重定向到网页topics

4.get请求和post请求
创建web应用程序时，我们将用到的两种主要请求类型是get请求和post请求。 
get请求：只是从服务器读取数据的页面，使用get请求。
post请求：用户需要通过表单提交信息时，通常使用post请求。 处理所有表单时，都将指定使用post方法。
函数new_topic()将请求对象作为参数。 用户初次请求该网页时，其浏览器将发送get请求：用户填写并提交表单时，其浏览器发送post请求。
根据请求类型，我们可以确定用户请求的是空表单（get请求）还是要求对填写好的表单进行处理（post请求）

5. 模版 new_topic()
创建新模版 new_topic.html，显示我们刚创建的表单 learning_logs/templates/learning_logs
这个模版继承了base.html，因此基本结构与项目“学习笔记”的其他页面相同

6.连接到页面new_topic
接下来，我们在页面topics中添加一饿到页面new_topic的链接：templates/topics.html

现在用户可以添加新主题了
'''

# 19.1.2 添加新条目
'''
用户还想添加新条目。 将再次定义URL，编写视图函数和模版，并连接到添加新条目的网页。 forms.py中再添加一个类
1. 用于添加新条目的表单 forms.py

2. URL模式new_entry
learning_logs/urls.py
path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry') 
这个URL模式与形式为http://localhost:8000/new_entry/id/的URL匹配，其中id是一个与主题ID匹配的数字
代码int:topic_id捕获一个数字值，并将其存储在变量topic_id中。请求的URL与这个模式匹配时，django将请求和主题ID发送给函数new_entry()

3.视图函数new_entry() 
视图函数new_entry与函数new_topic()很像
修改import语句，其中包含刚创建的EntryForm

4.模版new_entry。 类似于模版new_topic
new_entry.html

5.链接到页面new_entry
topic.html 添加到页面new_entry的链接
'''

# 19.1.3 编辑条目
'''
创建一个页面，让用户能编辑条目
1. URL模式edit_entry learning_logs/urls.py
2. 视图函数edit_entry()
页面edit_entry收到get请求，edit_entry()将返回一个表单，让用户能够对条目进行编辑。 该页面收到post请求，它将修改后的文本保存到数据库中
3. 模版 edit_entry     edit_entry.html， 与模版new_entry.html类似
4. 连接到页面edit_entry  在topic.html 添加到页面edit_entry的链接
'''
# 19.2 创建用户账户
'''
我们将建立一个用户注册和身份验证系统，让用户能够注册账户，进而登陆和注销。 将创建一个新的应用程序，包含于处理用户账户相关的所有功能
还将对模型topic稍作修改，让每个主题都归属于特定用户
'''
# 19.2.1 应用程序users
'''
///命令： python manage.py startapp users
ls
ls users
1. 将应用程序users添加到settings.py中
2. 包含应用程序users的URL。  在根目录中的urls.py # learning_log/urls.py (项目根目录)
'''
# 19.2.2 登陆页面
'''
learning_log/users/中，users文件夹新建？ 新建一个一个名为urls.py的文件
1. 模版 login.html 
在目录learning_log/users中，创建一个名为templates目录，再创建一个名为users的目录，新建login.html
这一步存疑，因为我自己创建了之后，发现还有一个自动创建的users文件夹，下面由login.html, logout.html等
learning_log/users/templates/users
模版继承base.html. 登陆页面的外观与网站的外观相同。

2. 链接到登陆页面。
在base.html中添加到登陆页面的链接，让所有页面都包含它。用户已登录时，不想显示这个链接，将它嵌套在一个{% if %}标签中。

3. 使用登陆页面
发现打不开localhost， 然后在根urls.py里添加path('users/')

登陆下登陆页面： http://localhost:8000/users/login/
'''
# 19.2.3 注销
'''
我们现在需要提供一个让用户注销的途径。不创建用于注销的页面，让用户只需单击一个链接就能注销并放回到主页。
为注销链接定义一个URL模式，编写视图函数，并在base.html中添加一个注销链接。
1. 注销URL. users/urls.py 而不是learning_log/urls.py
2. 视图函数 logout_view()    users.views.py
3. 链接到注销视图。 
添加一个注销链接，在base.html中添加。 
'''
# 19.2.4 注册页面
'''
创建一个新用户能够注册的页面
1. 注册页面的url模式 users/urls.py.
模式与url http://localhost:8000/users/register/匹配，并将请求发送给我们即将编写的函数register()
2. 视图函数register()
users/views.py
3. 注册新模版。 register.html保存到login.html所在的目录中
4. 链接到注册页面
在base.html中添加代码
'''

# 19.3 让用户拥有自己的数据
'''
用户应该能够输入其专有的数据，因此创建一个系统，确定各项数据所属的用户，再限制对页面的访问，让用户只能使用自己的数据
修改模型Topic，让每个主题都归属于特定用户。 这也将影响条目，因为每个条目都属于特定的主题。
# 19.3.1 使用@login_required限制访问 
django装饰器@logoin_required，让你实现：对于某些页面，只允许已登陆的用户访问他们。 装饰器(decorator)是放在函数定义前面的指令
1. 限制对topics页面的访问
每个主题都归特定用户所有，因此应只允许已登陆的用户请求topics页面。
learning_logs/views.py 添加代码
导入函数@login_required()。 检查用户是否已登陆，仅当用户登录时，django才运行topics()的代码。 未登陆，就重定向到登陆页面
重定向需要修改：
settings.py。 learning_log/settings.py? 

注意这里： 打开网页无法注销，注销显示该网页无法正常运作。如果问题仍然存在，请与网站所有者联系。

2. 全面限制对项目“学习笔记”的访问
django让你鞥能够轻松的限制对页面的访问，但你必须针对要保护那些页面做决定。最好先确定项目的哪些页面不需要保护，再限制对其他所有页面的访问
在项目“学习笔记”中，我们将不限制对主页，注册页面和注销页面的访问，并限制对其他所有页面的访问
learning_logs/views.py
'''
# 19.3.2 将数据关联到用户
'''
现在，需要将数据关联到提交它们的用户。 只需将最高层的数据关联到用户，这样更低层的数据讲自动关联到用户。 例如学习笔记中，最高层数据是主题
所有条目都与特定主题相关联，只要每个主题都归属特定用户，我们就能确定数据库中每个条目的所有者。 
修改模型Topic，添加一个关联到用户的外键。 这样做后，我们必须对数据库进行迁移。 最后必须对有些视图进行修改，使其志显示与当前登陆用户相关联的数据

1. 修改模型Topic  models.py。 导入django.contrib.auth中的模型user, 然后在topic中添加字段owenr。建立到模型user外键关系
2. 确定当前有哪些用户。启动一个django shell会话，执行如下命令? 这步卡住，不能在终端运行，要在解释器里运行？
/// python manage.py shell
3. 迁移数据。 知道用户ID后，就可以迁移数据哭。 
'''
# 19.3.3 只允许用户访问自己的主题
'''
当前，不管你以哪个用户的身份登陆，都能看到所有的主题。我们来改变这种情况，只向用户显示属于自己的主题。 
views.py
'''

# 19.3.4 保护用户的主题。
'''
我们还没有限制对单个主题的页面的访问，因此任何已登陆的用户都可输入类似于http://localhost:8000/topics/1/的URL,来访问显示相应主题的页面
views.py
'''

# 19.3.5 保护页面edit_entry
'''
页面edit_entry的URL为http://localhost:8000/edit_entry/entry_id/,其中entry_id是一个数字，下面来保护这个页面
禁止用户通过输入类似前面的URL来访问其他用户的条目：
views.py
'''
# 19.3.6 将新主题关联到当前用户
'''
当前，用于添加新主题的页面存在问题，因此它没有将新主题关联到特定用户。如果你尝试添加新主题，将看到错误消息IntegrityError,指出leanring_logs_topic.user_id不能为Null
django的意思是说，创建新主题时，你必须制定其owner字段的值。 
views.py
'''