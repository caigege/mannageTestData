from django.db import models


# Create your models here.
class emp(models.Model):
    gender = models.BooleanField("性别", default=1)
    name = models.CharField("姓名", max_length=20)
    education = models.CharField("学历", max_length=20)
    phone = models.CharField("电话", max_length=20, unique=True)
    companyId = models.ForeignKey("company.Company", verbose_name="公司id", on_delete=models.DO_NOTHING)

    level = models.IntegerField("等级", default=1)
    department = models.IntegerField("部门", default=1)
    salary = models.DecimalField("工资", default=0.00, max_digits=7, decimal_places=2)

    email = models.CharField("邮件", max_length=200, null=True, blank=True)
    headPortrait = models.ImageField("头像", null=True, width_field=50, height_field=60, blank=True)
    identityCard = models.CharField("身份证", max_length=18, null=True, unique=True, blank=True)
    birthday = models.DateField("生日", blank=True, null=True)
    post = models.CharField("岗位", max_length=20, null=True, blank=True)
    entryTime = models.DateTimeField("入职时间", auto_now_add=True)
    models.AutoField
