# Create your views here.
from django.core import serializers
from django.shortcuts import render

from L1_Task_create.models import Task


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
