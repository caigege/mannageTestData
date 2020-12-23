from django.db import models
# 账号由后台添加
# 权限赋予

# Create your models here.
'''
0.id
id是唯一的 主键
 
1.昵称
2.账号
3.密码
4.头像
5.职位
6.权限（角色）

'''
# TODO 任务数据设计文档——用户
class User(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')