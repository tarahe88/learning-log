from django import forms      # 导入模块 froms
from .models import Topic, Entry   # 导入模型 Topic. 19.1.2 导入Entry

class TopicForm(forms.ModelForm):      # 定义TopicForm类，继承forms.ModelForm
    class Meta:       # 最简单的ModelForm版本值包含一个内嵌的Meta类，告诉django根据哪个模型创建表单，以及包含哪些字段
        model = Topic  # 根据模型Topic创建一个表单
        fields = ['text']    # 表单只包含字段text
        labels = {'text': ''}  # 让django不要为字段text生成标签。

class EntryForm(forms.ModelForm): # 19.1.2 添加新条目。继承了forms.ModelForm
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})} # 小部件widget是一个HTML表单元素。