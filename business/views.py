import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from business.models import project
from company import views as companyViews
from company.views import companyGet, createData
from login import views


def getmU(dataList, objs: dict):
    '''

    :param dataList:
    :param objs:
    :return:
    '''

    pass


# Create your views here.
@csrf_exempt
def getEmp(request):
    postName = request.GET.get("postName")
    res = views.getAllVuale("emp", "post", "\'" + postName + "\'")
    ret = serializers.serialize("python", res)
    fields = companyViews.getArray(ret, "fields")
    ret=companyViews.checkFormat(fields)
    if (len(ret) == 0):
        ret = {"mgs": "未查询到"}
        # return JsonResponse(json.dumps(ret,ensure_ascii=False), safe=False)

    # print("getEmp ret :",ret)
    return JsonResponse(json.dumps(ret,ensure_ascii=False), safe=False)


@csrf_exempt
def toBusiness(request, businessName):
    print("toBusiness:" + businessName)
    result = views.getVuale("project", "name", businessName)

    return render(request, "model/business_order.html", {"project": result})


@csrf_exempt
def create(request):
    '''

    :param request:
    :return:
    '''
    company = companyGet(request)
    data = {}
    name = request.POST.get("name")
    description = request.POST.get("description")
    source = request.POST.get("source")
    note = request.POST.get("note")
    if name is not None:
        data['name'] = "\'" + name + "\'"
    if description is not None:
        data['description'] = "\'" + description + "\'"
    if description is not None:
        data['source'] = "\'" + source + "\'"
    if description is not None:
        data['note'] = "\'" + note + "\'"

    data['strategy'] = "\'" + request.POST.get("strategy") + "\'"

    data['companyId'] = 'company'
    objs = {"company": company, "project": project}

    print("create:", locals())
    projectJ = createData(data, "project", objs)
    # projectJ = True
    if not projectJ:
        mgs = {"message": str(projectJ) + "添加失败"}
    else:
        if projectJ == "已存在":
            mgs = {"message": str(projectJ)}
        else:
            # User.objects.filter(id=projectJ).update(postStatus=2)
            mgs = {"message": str(projectJ) + "添加成功"}
    return JsonResponse(mgs, charset='utf-8', safe=False, json_dumps_params={"ensure_ascii": False})
    # return  HttpResponse({'alert(1)'})
    # return  HttpResponse({"script":"alert","mgs":"成功"})
    # return render(request,"model/business_order.html",{"script":"alert","mgs":"成功"})
