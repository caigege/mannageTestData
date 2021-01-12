import datetime
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import L1_Task_create
from login import views
from employee.models import emp
from company import views as companyView
from L1_Task_create.models import Task
from django.utils import timezone
from django.core import serializers
# Create your views here.
'''选择日期创建任务'''


# from django.shortcuts import render
def judgeTaskselect(request, obj):
    if (obj == "-1"):
        return True
    return False


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
    projectName = request.POST.get("projectName")
    taskName = request.POST.get("taskName")
    content = request.POST.get("content")
    taskTime = request.POST.get("taskTime")
    strategy = request.POST.get("strategy")  # 策略
    taskLevel = request.POST.get("taskLevel")  # 任务级别
    selectDep = request.POST.get("selectDep")  # 部门
    selectPost = request.POST.get("selectPost")  # 岗位
    selectEmp = request.POST.get("selectEmp")  # 员工phone
    startTime = request.POST.get("startTime")  # 开始时间
    nowOrNot = request.POST.get("nowOrNot")  # 时间策略，任务是否马上开始
    task={}
    if (taskName == ''):
        result = {"erro": "异常:任务名为空"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    if (content == ''):
        result = {"erro": "异常:内容为空"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))

    if (nowOrNot is None):
        #      没选中“马上开始" 10分钟后开始,todo 获取任务排班表后得出结论 未对时间做严禁判断
        startTime = startTime.split("T")[0] + " " + startTime.split("T")[1]
        try:
            startTime=startTime+":00"
            print(str(startTime) + "--", type(startTime))
            dd = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
            startTime=dd+datetime.timedelta(minutes=10)
        except:
            startTime=startTime[0:len(startTime)-3]
            print(str(startTime) + "--", type(startTime))
            dd = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
            startTime = dd + datetime.timedelta(minutes=10)
    else:
        # 选“马上开始"
        startTime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    print("create_Task: ", locals())

    #部门前端判断
    if (judgeTaskselect(request, selectDep)):
        result = {"erro": "异常:部门未选择"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    # 查询部门是否存在
    checkDep=views.check("department", "name", selectDep)
    if (not checkDep):
        mgs = {"message": "部门不存在"}
        return HttpResponse(json.dumps(mgs, ensure_ascii=False))


    if (judgeTaskselect(request, selectPost)):
        result = {"erro": "异常:岗位未选择"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
        # 岗位部门是否存在
    checkPost = views.check("post", "name", selectPost)
    if (not checkPost):
        mgs = {"message": "岗位不存在"}
        return HttpResponse(json.dumps(mgs, ensure_ascii=False))



    if (judgeTaskselect(request, selectEmp)):
        result = {"erro": "异常:任务指派未选择"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    checkEmp = views.check("emp", "phone", selectEmp)
    if (not checkEmp):
        mgs = {"message": "员工不存在"}
        return HttpResponse(json.dumps(mgs, ensure_ascii=False))
    projectId=views.getVuale("project","name",projectName)
    print("projectId: ",projectId)

    task['projectId']='projectId'
    task['taskName']="\'"+taskName+"\'"
    task['content']="\'"+content+"\'"
    task['createTime']="\'"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\'"
    task['startTime']="\'"+str(startTime)+"\'"
    task['taskTime']="\'"+taskTime+"\'"
    task['strategy']=strategy
    task['taskLevel']=taskLevel
    task['selectDep']="\'"+selectDep+"\'"
    task['selectPost']="\'"+selectPost+"\'"
    # task['selectPost']="\'"+selectPost+"\'"
    task['selectEmp']=selectEmp
    objs = {"projectId": projectId, "Task": Task}
    # print(locals())
    # Task.objects.create(projectId=projectId,taskName=taskName,content=content,
    #                     createTime=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
    #                     startTime=startTime,taskTime=taskTime,strategy=strategy,taskLevel=taskLevel,
    #                     selectDep=selectDep,selectPost=selectPost,selectEmp=str(selectEmp))

    rert=companyView.createData(task,"Task",objs)
    print("rert",type(rert) is L1_Task_create.models.Task)
    if(type(rert) is L1_Task_create.models.Task):
        rert={"success":"添加成功"}
    rert={"erro":"任务名"+rert['mgs']}
    # res=serializers.serialize("python",rert)
    # print(locals())
    # if()
    return HttpResponse(json.dumps(rert, ensure_ascii=False))
    # render("创建任务")

# date=time(),who="小米",taskName="任务名",taskContent="任务内容"

# def create_Task(request):
#
#     return HttpResponse("创建任务")
