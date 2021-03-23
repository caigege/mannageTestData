from django.db import models

# 【任务发布】需求：
# 1、任务适用于项目开发
# 2、任务必须分三级，3级是可执行的，1、2级只能分解任务
# 3、任务分发后，要求马上确认，若没有确认，任务会自动确认
# 4、任务开始时间默认当前时间的10分钟后
# 5、计算出当前人员的工作状态
# Create your models here.
'''
0.id
id是唯一的 主键

1.*时间*
任务创建时间：系统时间  时分秒
任务开始时间：上传 时间 精确到时>当前时间最低10分钟后，手动设置为1小时
任务执行时长：上传（小时，不满一小时1小时计算，一天按8小时计算) 前端展示为总时间（小时），天数重新计算展示,数据库记时长Int
任务结束时间: 计算得出
执行时间：执行时创建时间


2.*对象*
任务创建者  id 外键
任务创建者 名字
任务id
任务名称
任务指派者 id 外键
任务指派 名字 

3.*内容*
任务内容
备注

4.*状态*

任务状态    ---- 1:待分解（级别为1、2级 默认状态）----
            0:任务确认(01超时未确认，02强制回收（未确认状态）,意外回收（
            1:执行中(确认后按开始时间判断）
            2:执行完成 待验收
            3:提前完成 
            4 顺利完成（未超期）
            5 验收后,超时完成（按工作时间计算）
            6 超时未提交验收 自动提交
            7:废弃
            8:回收再发布
            9:暂停
            
任务级别  1:方向级 2:分解任务级 3：任务可执行级
任务策略 1 2 3 4 5
优先级别 默认为1 级别越高优先等级越低

date=time(),who="小米",taskName="任务名",taskContent="任务内容",starTime 
'''


# TODO 任务数据设计文档——任务
class Task(models.Model):
    # projectKey = models.ForeignKey(max_length=200) 外键
    # 项目id
    projectId = models.ForeignKey("business.project", on_delete=models.DO_NOTHING, verbose_name="项目id")
    taskName = models.CharField('任务名', max_length=100, unique=True)
    content = models.CharField('任务内容', max_length=1000)

    # createTime = models.DateTimeField('任务创建时间',)
    createTime = models.DateTimeField("任务创建时间", auto_now_add=True)
    startTime = models.DateTimeField("任务开始时间", blank=True, null=True)
    startPlanTime = models.DateTimeField("计划开始时间", blank=True, null=True)
    taskTime = models.IntegerField('工作时间长', default=0)
    endTime = models.DateTimeField("任务计划结束时间", blank=True, null=True)
    state = models.IntegerField('任务状态', default=0)

    strategy = models.IntegerField('任务策略', default=1)
    taskLevel = models.IntegerField('任务级别', default=1)
    priorityLevel = models.IntegerField('优先级别', default=1)

    selectDep = models.CharField('部门', max_length=100)
    selectPost = models.CharField('岗位', max_length=100)
    selectEmp = models.CharField('任务指派', max_length=100)
    upTaskId = models.IntegerField('上级任务', default=0)
    taskCreater = models.CharField('任务创建者', max_length=50, null=True)
    models.AutoField
