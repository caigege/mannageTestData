from django.db import models

# Create your models here.
class Company(models.Model):
    '''
    公司
    todo 公司名不能有 "-"
    '''
    name = models.CharField("公司名", max_length=100,null=True,unique=True)
    password = models.CharField("密码", max_length=20)
    IdNum = models.CharField("企业代码", max_length=200, null=True, blank=True)
    account = models.CharField("账号/电话", max_length=20, unique=True)
    description = models.TextField("公司简介", max_length=2000,null=True)
    business = models.TextField("公司业务范围", max_length=1000, null=True)
    trademark = models.ImageField("头像", null=True, width_field=50, height_field=60, blank=True)
    models.AutoField

class department(models.Model):
    '''
    部门
    部门名数据库中 公司名-部门名
    '''
    name = models.CharField("部门", max_length=100, null=True, unique=True)
    companyId = models.ForeignKey("company.Company", on_delete=models.DO_NOTHING, verbose_name="公司id")
    models.AutoField