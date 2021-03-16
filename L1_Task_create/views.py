import datetime
import json
import time

from django.core import serializers
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import L1_Task_create
from L1_Task_create.models import Task
from company import views as companyView
from login import views
# from test.testTime import planTime
# from test.testTime import workDay
# from test import testTime.workDay
from tools import tool_time
from tools.tool_time import getDayStr, strToDateTime

from L1_Task_create.testTime import workDay,dic

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
    3 延期执行 作为新的任务发布（任务状态改为0)
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
    # 工作时长
    workTime = requset.POST.get("workTime")
    # empId
    empId = requset.POST.get("empId")
    # todo 测试
    empId = '13838682632'
    # startTimeWO
    startTimeWO = requset.POST.get("startTimeWO")
    # request.POST.get("phone")
    # todo 要记录任务过程1

    print("selec", type(selec), selec)
    print("finshiTime", type(finshiTime), finshiTime)
    print("taskId", type(taskId), taskId)
    print("workTime", type(workTime), workTime)
    print("startTimeWO", type(startTimeWO), startTimeWO)
    print("empId", type(empId), empId)
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
            if finshiTimeWF_long - 1 < time.time():
                #     提前完成
                Task.objects.filter(id=taskId).update(state=3)
            else:
                # 顺利完成
                Task.objects.filter(id=taskId).update(state=4)
        rert = {"result": "success", "content": "更新成功"}
        return HttpResponse(json.dumps(rert, ensure_ascii=False))
    elif (selec == "2"):
        # todo 记录任务时间 和状态
        # 设置更新工作时长,工作开始时间，任务状态为确认状态
        # 'test'

        Task.objects.filter(id=taskId).update(state=0,
                                              startTime=tool_time.getDBtime(time.time() + int(workTime) * 60 * 60),
                                              taskTime=workTime)

    elif (selec == "3"):
        # 延期
        res = Task.objects.get(id=taskId)

        print("res.priorityLevel:", type(res.priorityLevel), res.priorityLevel)
        print("res.projectId:", type(res.projectId), res.projectId)
        print("res.strategy:", type(res.strategy), res.strategy)
        # 优先级别
        priorityLevel = res.priorityLevel
        # 项目id
        projectId = res.projectId
        # 权重
        strategy = res.strategy
        startTime = Task.objects.filter(strategy=strategy, projectId=projectId).all().aggregate(Max("startTime"))
        print("startTime：", startTime)

        workTime = Task.objects.filter(startTime=startTime["startTime__max"], projectId=projectId).all().aggregate(
            Max("taskTime"))
        # print("workTime：", workTime)

        sTime = tool_time.getTimeStamp(startTime["startTime__max"]) + workTime["taskTime__max"] * 60 * 60
        print("sTime：", sTime)
        if time.time() > sTime:
            sDBTime = tool_time.getDBtime(time.time())
        else:
            # 如果时间超过当前，则用计算时间
            sDBTime = tool_time.getDBtime(sTime)
        print("sDBTime：", sDBTime)
        # 查询项目中 同级（权重）中人物开始时间最大的 和工作时间后的时间作为开始时间 同项目

        Task.objects.filter(id=taskId).update(state=0, priorityLevel=priorityLevel + 1, startTime=sDBTime)
        rert = {"result": "success", "content": "更新成功"}
        return HttpResponse(json.dumps(rert, ensure_ascii=False))
    elif (selec == "4"):
        #
        # todo 测试
        startTimeWO = "2021-01-12 18:00:00"
        nextDay(strToDateTime(startTimeWO), empId)
        # startTimeWO = "2021-01-12 18:00:00"
        # day = getDayStr(strToDateTime(startTimeWO))
        # print("day:", day)
        # # st_amStart = day + " " + dic["workTime14"]["am"]["starTime"]
        # # st_amEnd = day + " " + dic["workTime14"]["am"]["endTime"]
        # st_amStart = day + " " + dic["workTime14"]["pm"]["starTime"]
        # st_amEnd = day + " " + dic["workTime14"]["pm"]["endTime"]
        # print("st_amStart:", st_amStart)
        # print("st_amEnd:", st_amEnd)
        # stTime = strToDateTime(st_amStart)
        # endTime = strToDateTime(st_amEnd)
        # am9_12(empId, endTime, stTime, "pm")

        pass
    elif (selec == "5"):
        pass
    elif (selec == "6"):
        pass
    # todo 20210115

    return HttpResponse("处理成功")


'''选择日期创建任务'''


def nextDay(guestStartTime, empId):
    '''
    :param guestStartTime:任务设置开始日期
    :return: 任务开始时间
    '''
    day = getDayStr(guestStartTime)
    # while True:
    # 判断是否是假日
    # 判断周几
    # 是否调休
    # 判断上午
    # if planTime():

    sWorkTime = whoSelect(guestStartTime)


    # 判断 judgeStata=1,
    st_amStart = day + " " + dic[sWorkTime]["am"]["starTime"]
    st_amEnd = day + " " + dic[sWorkTime]["am"]["endTime"]
    # 转化为 时间
    stTime = strToDateTime(st_amStart)
    endTime = strToDateTime(st_amEnd)

    print("stTime:", stTime)
    startTime = Task.objects.filter(selectEmp=empId, startTime__lt=stTime).aggregate(Max('startTime'))
    # Task.objects.filter()
    if startTime["startTime__max"] is None:
        # 没有 比安排时间更短的时间
        # 判断在时间内的

        print("endTime:", endTime)
        return am9_12(empId, endTime, stTime)

    else:
        # 获取最大值得关闭时间
        endTimeGlTask = Task.objects.filter(startTime=startTime["startTime__max"], selectEmp=empId)[0].endTime
        print("获取最大值得关闭时间endTime:", endTimeGlTask, type(endTimeGlTask))
        if endTimeGlTask <= stTime:
            # 9:00前开始的任务的结束时间 小于9:00
            #     判断在时间9-12内的

            am9_12(empId, endTime, stTime)

        elif endTimeGlTask < endTime:

            print(endTime - endTimeGlTask)
            am9_12(empId, endTime, stTime)
        else:
            # 下午时间

            pass

        # .aggregate(startTime=Max("startTime"))


def whoSelect(guestStartTime):
    weekDay = guestStartTime.weekday()
    print("weekDay", weekDay)
    if weekDay <= 4:
        sWorkTime = "workTime14"
    elif weekDay == 5:
        #     todo
        sWorkTime = "workTime5"
    else:
        sWorkTime = "workTime67"
    return sWorkTime


def am9_12(empId, endTime, stTime, upDown):
    '''

    :param empId:
    :param endTime:
    :param stTime:
    :param upDown:am pm
    :return:
    '''

    mid = Task.objects.filter(selectEmp=empId, startTime__lt=endTime, startTime__gt=stTime).aggregate(Max('endTime'))
    print("mid:", mid)
    judgeTime = (endTime - mid['endTime__max']).seconds


    if judgeTime < 30 * 60:
        #     下午 加一工作日
        if upDown == "pm":
            # 获取假日天数

            num = workDay(getDayStr(endTime))
            endTime = endTime + datetime.timedelta(days=num).strftime("%Y-%m-%d %H:%M:%S")
            stTime = stTime + datetime.timedelta(days=num).strftime("%Y-%m-%d %H:%M:%S")
            return am9_12(empId, endTime, stTime, "am")
        else:
            #         "am"
            wT=whoSelect(endTime) # todo 处理workTime14
            day = getDayStr(strToDateTime(endTime))

            endTime = day + " " + dic[wT]["pm"]["endTime"]
            stTime = day + " " + dic[wT]["pm"]["starTime"]
            return am9_12(empId, endTime, stTime, "pm")


    else:
        # 返回 开始时间
        return mid['endTime__max'] + datetime.timedelta(seconds=1).strftime("%Y-%m-%d %H:%M:%S")



def taskVerify(request):
    user = request.session.get("user")
    # user = "13200000001"  # todo 测试处理
    user = "13312345678"  # todo 测试处理 g
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


def checkEmpDayWorkPlan():
    # 员工id
    empId = ""
    # 时间


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
    # todo 查询员工当天 是否有工作安排已满

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
    endTime = startTime + datetime.timedelta(minutes=int(taskTime) * 60)
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
    task['endTime'] = "\'" + str(endTime) + "\'"
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
