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

任务状态  1:待分解（级别为1、2级 默认状态） 2:确认 3:执行中(时间计划内开始） 4 执行完成（未超期） 5 延迟（执行中超时未完成）6超时（按工作时间计算）7 时间计划提前执行
任务级别  1:方向级 2:分解任务级 3：任务可执行级



date=time(),who="小米",taskName="任务名",taskContent="任务内容",starTime 
'''
# TODO 任务数据设计文档——任务
class Task(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')