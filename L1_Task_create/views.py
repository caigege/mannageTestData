import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import datetime
# Create your views here.
'''选择日期创建任务'''
# from django.shortcuts import render


@csrf_exempt
def create_Task(request):
    '''
      strategy

    4.任务策略：
     a.加急（必须完成）
     b.顺延(先处理其他，增加优先等级，默认为1，优先等级每高一级，优先顺序增加）优先推荐
    1级：无色，普通，创建时间排列
    2级：白色，执行者自行创建
    3级：蓝色，1级上级安排顺
    4级：紫色，管理级
    5级：红色，紧急任务，一般不用
    :param request:
    :return:
    '''
    projectName=request.POST.get("projectName")
    taskName=request.POST.get("taskName")
    content=request.POST.get("content")
    taskTime=request.POST.get("taskTime")
    strategy=request.POST.get("strategy")#策略
    taskLevel=request.POST.get("taskLevel")#任务级别
    selectDep=request.POST.get("selectDep")#部门
    selectPost=request.POST.get("selectPost")#岗位
    selectEmp=request.POST.get("selectEmp")#员工
    startTime=request.POST.get("startTime")#开始时间
    nowOrNot=request.POST.get("nowOrNot")#时间策略，任务是否马上开始

    if(taskName==''):
        result = {"erro": "异常:任务名为空"}
        return HttpResponse(json.dumps(result,ensure_ascii=False))
    if(content==''):
        result = {"erro": "异常:内容为空"}
        return HttpResponse(json.dumps(result,ensure_ascii=False))

    if(nowOrNot is None):
    #      没选中“马上开始" 10分钟后开始,todo 获取任务排班表后得出结论
        startTime=startTime.split("T")[0]+ " "+startTime.split("T")[1]
        dd = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
        startTime=dd+datetime.timedelta(minutes=10)
        # print(str(startTime)+"--"+type(startTime))
        # pass
    else:
        # 没选“马上开始"
        startTime = startTime.split("T")[0] + " " + startTime.split("T")[1]
    print("create_Task: ", locals())

    # todo 20210111 创建任务的sql内容





    resultOK={"mgs":"111eeee"}
    return HttpResponse(locals())
    # render("创建任务")

# date=time(),who="小米",taskName="任务名",taskContent="任务内容"

# def create_Task(request):
#
#     return HttpResponse("创建任务")

