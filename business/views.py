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
    ret = companyViews.checkFormat(fields)
    if (len(ret) == 0):
        ret = {"mgs": "未查询到"}
        # return JsonResponse(json.dumps(ret,ensure_ascii=False), safe=False)

    # print("getEmp ret :",ret)
    return JsonResponse(json.dumps(ret, ensure_ascii=False), safe=False)


@csrf_exempt
def toBusiness(request, businessName):
    # print("toBusiness:" + businessName)
    task1 = views.getVuale("project", "name", businessName)
    # task1 = project.objects.get("project", "name", "\'" + businessName+"\'" )
    # result = serializers.serialize("python", task1)

    # print("result:",task1["pk"])
    return render(request, "model/business_order.html", {"type": 1, "project": task1})


def createPro(request):
    return render(request, "model/business_order.html",{"type": 2})


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

    # data['strategy'] = "\'" + request.POST.get("strategy") + "\'"

    data['companyId'] = 'company'
    objs = {"company": company, "project": project}
    if (name.replace(' ', '') == ""):
        mgs = {"erro": "项目名不能为空"}
        return JsonResponse(mgs, charset='utf-8', safe=False, json_dumps_params={"ensure_ascii": False})
    #
    if (description.replace(' ', '') == ""):
        mgs = {"erro": "项目名简介 不能为空"}
        return JsonResponse(mgs, charset='utf-8', safe=False, json_dumps_params={"ensure_ascii": False})
    #
    projectJ = createData(data, "project", objs)
    if (type(projectJ) is project):
        mgs = {"success": "项目" + "添加成功"}
    else:
        mgs = {"erro": projectJ['mgs']}
    # print("create:", mgs)

    return JsonResponse(mgs, charset='utf-8', safe=False, json_dumps_params={"ensure_ascii": False})
    # return  HttpResponse({'alert(1)'})
    # return  HttpResponse({"script":"alert","mgs":"成功"})
    # return render(request,"model/business_order.html",{"script":"alert","mgs":"成功"})
