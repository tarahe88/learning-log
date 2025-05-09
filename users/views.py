# users/views.py
from django.shortcuts import render, redirect # deepseek新的
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect # 书里的
# from django.core.urresolvers import reverse # 书里已弃用。
from django.contrib.auth import logout # deepseek新的。 django内置的注销函数
from django.contrib.auth import login, logout, authenticate # 19.2.4 注册页面
from django.contrib.auth.forms import UserCreationForm # 19.2.4

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # 19.3.1 让用户拥有自己的数据
from django.http import HttpResponseRedirect, Http404     # 19.3.4 保护用户的主题。

def register(request): # 19.2.4
    # 注册新用户
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'users/register.html', context)

def logout_view(request):
    # 注销用户
    logout(request) # 调用Django的logout()函数清理会话
    return redirect('learning_logs:index') # 重定向到主页





