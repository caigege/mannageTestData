#! /usr/bin/env python

'''
# @Create   :2021/3/12 16:35
# @Author   : Admin
# @Description  :   说明文件功能
@Modify Time        @Version    @Description
------------        --------    ------------
2021/3/12 16:35     1.0          '你好'   
'''
# from L1_Task_create.models import Task

# Task.objects.filter(id=8).update(state=0)
import time
import datetime
print(type(time.time()))
# 1615777594
# 1610445300
# 1610446920
def getDBtime(timeStamp):
    '''
    时间戳转 dateTime
    :param timeStamp:
    :return:
    '''
    dateArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime
print(time.time())

print(getDBtime(time.time()))
print(type(getDBtime(86400)))