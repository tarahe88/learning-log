from django.shortcuts import render, get_object_or_404, redirect # 函数render()根据视图提供的数据渲染响应。
from django.http import HttpResponseRedirect # 导入了HttpResponseRedirect类，
# 用户提交主题后我们将使用这类将用户重定向到网页topics。 函数reverse()根据指定的url模型确定url
# 这意味着django将在页面被请求时生成url。 我们还导入了刚才创建的表单TopicForm
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm
from .models import Topic
from django.urls import reverse
from django.contrib.auth.decorators import login_required # 19.3.1 让用户拥有自己的数据
from django.http import HttpResponseRedirect, Http404     # 19.3.4 保护用户的主题。


# Create your views here. 在这里创建视图
from .models import Topic, Entry
def index(request):
    # 学习笔记的主页
    return render(request, 'learning_logs/index.html')
@login_required    # 19.3.1 让用户拥有自己的数据，限制对topics页面的访问
def topics(request):
    # 显示所有主题
    # 这里假设你有一个Topic模型
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # 19.3.3 只允许用户访问自己的主题
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
@login_required    # 19.3.1 让用户拥有自己的数据，限制对topic页面的访问
def topic(request, topic_id):
    # 显示单个主题及其所有条目
    topic = get_object_or_404(Topic, id=topic_id)
    # 确认请求的主题属于当前用户    # 19.3.4 保护用户的主题
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
@login_required # 19.3.1 让用户拥有自己的数据，限制对new_topic页面的访问
def new_topic(request):
    # 添加新主题
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST 提交的数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
# 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
# 19.1.2 添加新条目
def new_entry(request, topic_id):
    # 在特定主题中添加新条目
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

# 19.1.3 编辑条目 页面edit_entry收到get请求，edit_entry()将返回一个表单，让用户能够对条目进行编辑。
# 该页面收到post请求，它将修改后的文本保存到数据库中
@login_required # 19.3.1 让用户拥有自己的数据，限制对edit_entry页面的访问
def edit_entry(request, entry_id):
    # 编辑既有条目
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404 # 19.3.5 保护页面edit_entry

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST 提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) # 19.3.6 将新主题关联到当前用户
            new_topic.owner = request.user   # 19.3.6 将新主题关联到当前用户
            new_topic.save()              # 19.3.6 将新主题关联到当前用户
            form.save()  # 直接保存表单，不需要处理 owner，因为 Entry 已经有 owner
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)









