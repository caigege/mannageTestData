from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from business.models import project
from company.views import companyGet, createData
from login import views


# Create your views here.

@csrf_exempt
def toBusiness(request, businessName):
    print("toBusiness:" + businessName)
    result = views.getVuale("project", "name", businessName)

    return render(request, "model/business_order.html", {"project": result})


@csrf_exempt
def create(request):
    company = companyGet(request)

    data = {}
    data['name'] = "\'" + request.POST.get("name") + "\'"
    data['description'] = "\'" + request.POST.get("description") + "\'"
    data['source'] = "\'" + request.POST.get("source") + "\'"
    data['note'] = "\'" + request.POST.get("note") + "\'"
    data['companyId'] = 'company'
    objs = {"company": company, "project": project}

    # print("create:",locals())
    projectJ = createData(data, "project", objs)
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
