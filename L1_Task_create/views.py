import datetime
import json
import time

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import L1_Task_create
from L1_Task_create.models import Task
from company import views as companyView
from login import views
'''
任务状态    ---- 1:待分解（级别为1、2级 默认状态）----
            0:任务确认(01超时未确认，02强制回收（未确认状态）,意外回收（
            1:执行中(确认后按开始时间判断）
            2:执行完成 待验收
            3:提前完成 
            4 顺利完成（未超期）
            5 验收后,超时完成（按工作时间计算）
            6 超时未提交验收 自动提交
            6 延迟（执行中超时未完成）
            # 7 时间计划提前执行 （不考虑）
'''

@csrf_exempt
def taskVerifyResult(requset):
    '''
    处理审核结果
    0 通过
    1 继续
    2 加急
    3 延期执行 作为新的任务发布
    4 废除终止 不在换方案属于不相干或是错误任务
    5 回收再发布，换个方案在执行的
    6 暂停，项目封闭(包括其子任务
    :param requset:
    :return:
    '''
    # 方案
    selec = requset.POST.get("selec")
    # 显示完成时间 30分内
    finshiTime = requset.POST.get("finshiTime")
    # 任务id
    taskId = requset.POST.get("taskId")
    # 标准完成时间
    finshiTimeWF = requset.POST.get("finshiTimeWF")
    # request.POST.get("phone")
    # todo 要记录任务过程1

    print("selec", type(selec), selec)
    print("finshiTime", type(finshiTime), finshiTime)
    print("taskId", type(taskId), taskId)
    finshiTime_long = int(finshiTime) / 1000
    finshiTimeWF_long = int(finshiTimeWF) / 1000
    # time.time()
    # time
    print(finshiTime_long - 1 < time.time(), "过期")

    if (selec == "1"):
        # 前端已经判断时间 还是要判断，不然系统时间会出问题，而且延迟2秒缓冲 保证计算时间在分钟内精确
        # todo 记录继续过程
        if (finshiTime_long - 1 < time.time()):
            rert = {"result": "erro", "content": "任务已超时，其选择其他验收方案"}
            return HttpResponse(json.dumps(rert, ensure_ascii=False))
        else:
        #     可以继续,修改任务状态 为通知状态,需要再次确认 todo 记录任务未完成类型

            Task.objects.filter(id=taskId).update(state=0)
            rert = {"result": "success", "content": "更新成功"}
            return HttpResponse(json.dumps(rert, ensure_ascii=False))
    elif (selec == "0"):
        # 通过状态 todo 记录完成过程
        if (finshiTime_long - 1 < time.time()):
            # 超时完成
            Task.objects.filter(id=taskId).update(state=5)

        else:
            if finshiTimeWF_long-1<time.time():
            #     提前完成
                Task.objects.filter(id=taskId).update(state=3)
            else:
                # 顺利完成
                Task.objects.filter(id=taskId).update(state=4)
        rert = {"result": "success", "content": "更新成功"}
        return HttpResponse(json.dumps(rert, ensure_ascii=False))
    elif (selec == "2"):
        # todo 记录任务时间 和状态
        # 设置更新工作时长,工作开始时间
        'test'
        Task.objects.filter(id=taskId).update(state=0,)
        pass
    elif (selec == "3"):
        pass
    elif (selec == "4"):
        pass
    elif (selec == "5"):
        pass
    elif (selec == "6"):
        pass
    # todo 20210115

    return HttpResponse("处理成功")


'''选择日期创建任务'''


def taskVerify(request):
    user = request.session.get("user")
    user = "13312345678"  # todo 测试处理
    task = Task.objects.filter(taskCreater=user, state=2)
    # task=Task.objects.filter(taskCreater="\'"+user+"\'",state=2)
    result = serializers.serialize("python", task)
    # print(locals())
    if (result == []):
        result = ""
    return render(request, 'model/taskVerify.html', {"list": result})


# from django.shortcuts import render
def judgeTaskselect(request, obj):
    if (obj == "-1"):
        return True
    return False


def taskFinshiSubmit(request):
    # todo 提交记录未处理 重复提交未提示
    # 更新任务状态未待验收状态
    data = request.GET.get("data")
    print(data)
    pk = data.split("*")[0]
    # taskCreate=data.split("*")[1]
    Task.objects.filter(id=pk).update(state=2)

    return HttpResponse("更新数据成功")


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
    user = request.session.get("user")
    projectName = request.POST.get("projectName")
    taskName = request.POST.get("taskName")
    content = request.POST.get("content")
    taskTime = request.POST.get("taskTime")
    strategy = request.POST.get("strategy")  # 策略 处理任务处理顺序
    taskLevel = request.POST.get("taskLevel")  # 任务级别 是否需分解 1再次分解 2执行
    selectDep = request.POST.get("selectDep")  # 部门
    selectPost = request.POST.get("selectPost")  # 岗位
    selectEmp = request.POST.get("selectEmp")  # 员工phone
    startTime = request.POST.get("startTime")  # 开始时间
    nowOrNot = request.POST.get("nowOrNot")  # 时间策略，任务是否马上开始
    task = {}
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
            startTime = startTime + ":00"
            print(str(startTime) + "--", type(startTime))
            dd = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
            startTime = dd + datetime.timedelta(minutes=10)
        except:
            startTime = startTime[0:len(startTime) - 3]
            print(str(startTime) + "--", type(startTime))
            dd = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
            startTime = dd + datetime.timedelta(minutes=10)
    else:
        # 选“马上开始"
        startTime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    print("create_Task: ", locals())

    # 部门前端判断
    if (judgeTaskselect(request, selectDep)):
        result = {"erro": "异常:部门未选择"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    # 查询部门是否存在
    checkDep = views.check("department", "name", selectDep)
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
    projectId = views.getVuale("project", "name", projectName)
    print("projectId: ", projectId)

    task['projectId'] = 'projectId'
    task['taskName'] = "\'" + taskName + "\'"
    task['content'] = "\'" + content + "\'"
    task['createTime'] = "\'" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\'"
    task['startTime'] = "\'" + str(startTime) + "\'"
    task['taskTime'] = "\'" + taskTime + "\'"
    task['strategy'] = strategy
    task['taskLevel'] = taskLevel
    task['selectDep'] = "\'" + selectDep + "\'"
    task['selectPost'] = "\'" + selectPost + "\'"
    # task['selectPost']="\'"+selectPost+"\'"
    task['selectEmp'] = selectEmp
    task['taskCreater'] = "\'" + user + "\'"
    objs = {"projectId": projectId, "Task": Task}
    # print(locals())
    # Task.objects.create(projectId=projectId,taskName=taskName,content=content,
    #                     createTime=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
    #                     startTime=startTime,taskTime=taskTime,strategy=strategy,taskLevel=taskLevel,
    #                     selectDep=selectDep,selectPost=selectPost,selectEmp=str(selectEmp))

    rert = companyView.createData(task, "Task", objs)
    print("rert", type(rert) is L1_Task_create.models.Task)
    if (type(rert) is L1_Task_create.models.Task):
        rert = {"success": "添加成功"}
    else:
        rert = {"erro": "任务名" + rert['mgs']}
    # res=serializers.serialize("python",rert)
    # print(locals())
    # if()
    return HttpResponse(json.dumps(rert, ensure_ascii=False))
    # render("创建任务")

# date=time(),who="小米",taskName="任务名",taskContent="任务内容"

# def create_Task(request):
#
#     return HttpResponse("创建任务")
