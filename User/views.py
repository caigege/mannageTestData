# Create your views here.
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from company import views as  companyView
from business.models import project
from L1_Task_create.models import Task
from django.views.decorators.csrf import csrf_exempt

def getUser(request):
    user = request.session.get("user")
    print("getUser - user：", user)
    # res=getAllVuale("Task","selectEmp","\'"+user+"\'")
    res = Task.objects.filter(selectEmp=user,state__in=[0,1,2,3,4,5,6]).order_by("createTime")

    lv1 = []
    lv2 = []
    lv3 = []
    lv4 = []
    lv5 = []

    for ret in res:
        num = ret.strategy
        # print(num, ret)
        if num == 1:
            lv1.append(ret)
        elif num == 2:
            lv2.append(ret)
        elif num == 3:
            lv3.append(ret)
        elif num == 4:
            lv4.append(ret)


        elif num == 5:
            lv5.append(ret)
    resultdata = lv5 + lv4 + lv3 + lv2 + lv1
    result = serializers.serialize("python", resultdata)

    return render(request, 'model/personal_Center.html', {"list": result})

@csrf_exempt
def sureTask(request):
    data = request.POST.get("data")
    print(data)
    # 任务id
    pk = data.split("*")[0]
    # taskCreate = data.split("*")[1]
    Task.objects.filter(id=pk).update(state=1)

    return HttpResponse("更新数据成功")




def getUserAjax(request):
    user = request.session.get("user")
    print("getUser - user：", user)
    # res=getAllVuale("Task","selectEmp","\'"+user+"\'")
    res = Task.objects.filter(selectEmp=user,state__in=[0,1,2,3,4,5,6]).order_by("createTime")
    result=serializers.serialize("python", res)
    lv1 = []
    lv2 = []
    lv3 = []
    lv4 = []
    lv5 = []

    for ret in result:
        num = ret['fields']['strategy']
        # print(num, ret)
        if num == 1:
            lv1.append(ret)
        elif num == 2:
            lv2.append(ret)
        elif num == 3:
            lv3.append(ret)
        elif num == 4:
            lv4.append(ret)
            # print("this problem")
            # print("lv4",serializers.serialize("python", lv4[0]))

        elif num == 5:
            lv5.append(ret)
    resultdata = lv5 + lv4 + lv3 + lv2 + lv1
    print("resultdata ----*****----:",type(resultdata),resultdata)
    return HttpResponse(json.dumps(companyView.checkFormat(resultdata), ensure_ascii=False))

@csrf_exempt
def refreshSchedule(request):
    '''
    查询项目进度
            0:任务确认(01超时未确认，02强制回收（未确认状态）,意外回收（
            1:执行中(确认后按开始时间判断）
            *2:执行完成 待验收
            *3:提前完成
            *4 顺利完成（未超期）
            *5 验收后,超时完成（按工作时间计算）
            6 超时未提交验收 自动提交
            *7:废弃
            *8:回收再发布，必须重新发布后才标示
            9:暂停
    :param request:
    :return:
    '''
    # 查询
    projectId=request.POST.get("data")
    print("projectId:",projectId)
    # 查询任务
    ress=Task.objects.filter(projectId=projectId)
    ressNum=len(ress)
    print("p:",ressNum)
    result_ress = serializers.serialize("python", ress)
    # print(result_ress)
    NumCode=0
    for res in result_ress :
        if res["fields"]["state"] in [2,3,4,5,7,8]:
            NumCode=NumCode+1
    numCode=str(NumCode)+"/"+ str(ressNum)
#             写入
#     返回数据

    project.objects.filter(id=projectId).update(schedule=numCode)
    return HttpResponse(numCode)

def secondTaskResolvej(request):
    '''
    继续分解，判断1 2级
    :param request:
    :return:
    '''
    data = request.POST.get("data")
    print(data)
    # 任务id
    pk = data.split("*")[0]
    # taskCreate = data.split("*")[1]
    # Task.objects.filter(id=pk).update(state=1)

    return None