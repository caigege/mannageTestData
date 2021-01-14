# Create your views here.
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from company import views as  companyView
from L1_Task_create.models import Task
from django.views.decorators.csrf import csrf_exempt

def getUser(request):
    user = request.session.get("user")
    print("getUser - user：", user)
    # res=getAllVuale("Task","selectEmp","\'"+user+"\'")
    res = Task.objects.filter(selectEmp=user).order_by("createTime")

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
            # print("this problem")
            # print("lv4",serializers.serialize("python", lv4[0]))

        elif num == 5:
            lv5.append(ret)
    resultdata = lv5 + lv4 + lv3 + lv2 + lv1
    result = serializers.serialize("python", resultdata)

    return render(request, 'model/personal_Center.html', {"list": result})

@csrf_exempt
def sureTask(request):
    data = request.POST.get("data")
    print(data)
    pk = data.split("*")[0]
    # taskCreate = data.split("*")[1]
    Task.objects.filter(id=pk).update(state=1)

    return HttpResponse("更新数据成功")




def getUserAjax(request):
    user = request.session.get("user")
    print("getUser - user：", user)
    # res=getAllVuale("Task","selectEmp","\'"+user+"\'")
    res = Task.objects.filter(selectEmp=user).order_by("createTime")
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