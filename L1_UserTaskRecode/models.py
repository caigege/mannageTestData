from django.db import models
# TODO 任务记录，主要目的是通过数据分析，项目进度、参与人员能力评估，任务难度评估 任务分解合理度进行评估
# Create your models here.
# 指标1.响应时间 ，超时次数
# 2.提前次数 和超时次数对应
class TaskCode(models.Model):
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    taskId = models.IntegerField('任务id', default=0)
    departmentId = models.IntegerField('部门id', default=0)
    empId = models.IntegerField('执行人员id', default=0)
    state = models.IntegerField("任务状态", null=True, default=0)
    upstate = models.IntegerField("任务状态", null=True, default=0)
    taskName = models.CharField('任务名', max_length=100, unique=True)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    models.AutoField


class Statistics(models.Model):
    '''
    统计：项目id  任务部门id 员工id	  任务id 任务状态state 状态次数num
    '''
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    empId = models.IntegerField('执行人员id', default=0)
    taskId = models.IntegerField('任务id', default=0)
    departmentId = models.IntegerField('部门id', default=0)
    state = models.IntegerField("任务状态", null=True, default=0)
    stateNum = models.IntegerField('状态次数', default=0)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    # answer

    models.AutoField

class StatisticsProject(models.Model):
    # 统计项目概况
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    # empId = models.IntegerField('执行人员id', default=0)
    # taskId = models.IntegerField('任务id', default=0)
    # departmentId = models.IntegerField('部门id', default=0)
    state = models.IntegerField("任务状态", null=True, default=0)
    overtimeNum = models.IntegerField("超时次数", null=True, default=0)
    advanceTimeNum = models.IntegerField("提前次数", null=True, default=0)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    models.AutoField

class StatisticsDepartment(models.Model):
    # 统计部门概况
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    # empId = models.IntegerField('执行人员id', default=0)
    # taskId = models.IntegerField('任务id', default=0)
    # departmentId = models.IntegerField('部门id', default=0)
    state = models.IntegerField("任务状态", null=True, default=0)
    overtimeNum = models.IntegerField("超时次数", null=True, default=0)
    advanceTimeNum = models.IntegerField("提前次数", null=True, default=0)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    models.AutoField

class StatisticsEmp(models.Model):
    # 统计员工概况
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    # empId = models.IntegerField('执行人员id', default=0)
    # taskId = models.IntegerField('任务id', default=0)
    # departmentId = models.IntegerField('部门id', default=0)
    state = models.IntegerField("任务状态", null=True, default=0)
    overtimeNum = models.IntegerField("超时次数", null=True, default=0)
    advanceTimeNum = models.IntegerField("提前次数", null=True, default=0)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    models.AutoField


class StatisticsCompany(models.Model):
    # 统计公司概况
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    # empId = models.IntegerField('执行人员id', default=0)
    # taskId = models.IntegerField('任务id', default=0)
    # departmentId = models.IntegerField('部门id', default=0)
    state = models.IntegerField("任务状态", null=True, default=0)
    overtimeNum = models.IntegerField("超时次数", null=True, default=0)
    advanceTimeNum = models.IntegerField("提前次数", null=True, default=0)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    models.AutoField