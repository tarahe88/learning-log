from django.contrib import admin

# 在这里注册你的明星
# 为向管理网站注册Topic，请输入下面的代码
from learning_logs.models import Topic, Entry  # 18.2.6 修改加了 Entry

admin.site.register(Topic)
admin.site.register(Entry) # 18.2.6 修改加了 Entry
