'''定义learning_logs的URL模式'''

from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views # 导入当前目录的 views.py
from django.contrib import admin
app_name = 'learning_logs' # 定义命名空间（防止不同app的URL冲突）

# 为learning_logs定义URL模式
urlpatterns = [
    # 主页 （原书中使用url(), django 4.0+ 改用 path)
    path('', views.index, name='index'),
    # 显示所有主题（示例：/topics/)
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面（示例：/topics/1/)
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new/', views.new_topic, name='new_topic'), # 这个url模式将请求交给视图函数new_topic()
    # 19.1.2 添加新条目 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 19.1.3 编辑条目。用于编辑条目的页面  # 编辑条目（19.1.3节新增）
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # 19.2.1 应用程序 users. 为啥在这里看到admin和learning_logs。前面没看到
    path('admin/', admin.site.urls),
    # path('', include('learning_logs.urls', namespace='learning_logs')), 这不应该在这，而应该在learning_log/urls.py
    # 否则两处都有的话，会无限循环
    path('users/', include('users.urls', namespace='users')), # 新增users应用url
]
























