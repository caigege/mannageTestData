from django.db import models


# Create your models here.
class project(models.Model):
    '''
    项目
    '''
    name = models.CharField("项目名", max_length=100, null=True, unique=True)
    description = models.TextField("项目简介", max_length=5000, null=True)
    note = models.TextField("备注", max_length=5000)
    schedule = models.TextField("项目进度", max_length=100, default='0/0')
    source = models.TextField("来源", null=True, max_length=200)
    state = models.IntegerField("状态：0:计划(创建未启动）1:启动(进行中),2:完成，3：暂停，4：废除(终止）", null=True, default=0)
    companyId = models.ForeignKey("company.Company", on_delete=models.DO_NOTHING, verbose_name="公司id")
    models.AutoField
