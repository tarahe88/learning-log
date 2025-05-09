# 为应用程序users定义URL模式
from django.urls import path, re_path  # 替换原来的 from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views  # 确保这行没问题



# 使用path()代替url
app_name = 'users'
urlpatterns = [
    # 登陆页面.
    path('login/', LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('register/', views.register,name='register'),
    # 注销URL 19.2.3 注销
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logged_out.html'),name='logout'),
    # 注册页面url模式。19.2.4
    path('register/', views.register, name='register'),

]











