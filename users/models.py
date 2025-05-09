from django.db import models
from django.contrib.auth.models import User

#
# class Topic(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 添加这行 #
#
#     def __str__(self):
#         return self.text
# # Create your models here.
