from django.db import models # 这里为我们导入了模块models，还让我们创建自己的模型。
# 模型告诉django如何处理应用程序中存储的数据

# 在这里创建模型.
# 在代码层面，模型就是一个类，包含属性和方法。 下面表示用户将要存储的主题的模型
from django.db import models
from django.contrib.auth.models import User # 19.3.2 将数据关联到用户
class Topic(models.Model): # 创建了一个名为topic的类，它继承了Model-Django中一个定义了模型基本功能的类
    # Topic类只有2个属性， text和date_added
    # 用户学习的主题
    text = models.CharField(max_length=200)
    # 属性text是一个CharField-由字符和文本组成的数据。需要存储少量的文本，如名称标题城市时可以使用CharField
    # 定义CharField属性时，必须告诉Django改在数据库中预留多少空间。比如200个字符
    # 这里将max_length设置成了200（即200个字符），这对存储大多数主题名来说够了
    date_added = models.DateTimeField(auto_now_add=True)
    # date_added是一个DateTimeField-记录日期和时间的数据。传递了实参auto_now_add=True.
    # 每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间

    # 我们需要告诉Django，默认应使用哪个属性来显示有关主题的信息。
    # 编写了方法__str__，返回存储在属性text中的字符串
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 新增 owner 字段 根据deepseek
    def __str__(self):
        # 返回模型的字符串表示
        return self.text
class Entry(models.Model): # Entry跟Topic一样，也继承了Django基类Model。
    # 学到的有关某个主题的具体知识
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) # 第一个属性topic是一个ForeignKey实例
    #外键是一个数据库属于，引用了数据库中另一条记录。将每个条目关联到特定的主题。每个主题都有一个键(或ID)。
    text = models.TextField() # 属性text是一个TextField实例。不需要长度限制
    date_added = models.DateTimeField(auto_now_add=True) #属性date_added让我们能够按创建顺序呈现条目
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # 19.3.2 将数据关联到用户. 这个书本上有错误。
    # 这个应该在users/models.py上添加吗？

    class Meta: # Meta类存储用于管理模型的额外信息。使用Entrys表示多个条目。
        verbose_name_plural = 'entries'

        def __str__(self):
            # 返回模型的字符串表示
            return self.text[:50] + "..." # 呈现条目时显示哪些信息（如只显示前50个字符）。“。。。”表示现实的并非整个条目
