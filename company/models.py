from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField("公司名", max_length=100,null=True,unique=True)
    password = models.CharField("密码", max_length=20)
    IdNum = models.CharField("企业代码", max_length=200, null=True, blank=True)
    account = models.CharField("账号/电话", max_length=20, unique=True)
    description = models.TextField("公司简介", max_length=2000,null=True)
    business = models.TextField("公司业务范围", max_length=1000, null=True)
    trademark = models.ImageField("头像", null=True, width_field=50, height_field=60, blank=True)
    models.AutoField











