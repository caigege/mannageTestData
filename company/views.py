# -*- coding: UTF-8 -*-
# Create your views here.
import json
import time
from datetime import datetime
from decimal import Decimal

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from company.models import Company, department, post
from employee.models import emp
from login import views
from login.models import User
from login.views import auth
from business import Test_Data

def getProject(request):
    company = companyGet(request)
    # obj = {"companyId": company}
    # res = views.getVualeAllObj("business", "companyId", "companyId", obj)
    # res
    # result=Test_Data.resultoK
    lists=Test_Data.resultoKstr
    # s=serializers.serialize()
    # result=json.dumps(s).encode("utf-8")
    # print("getProject result：",result)
    # return JsonResponse(lists,safe=False,json_dumps_params={'ensure_ascii':False})
    return JsonResponse(lists,safe=False)


def update(table, keyName, key, objs=None, **dicts):
    updata_str = table + ".objects.filter(" + keyName + "=" + key + ").update("

    if objs is None:
        keylist = dicts.keys()
        dataStr = ""
        for k in keylist:
            dataStr += k + "=" + str(dicts.get(k)) + ","
        dataStr = dataStr[0:len(dataStr) - 1]
        updata_str = updata_str + dataStr + ")"
        return eval(updata_str)

    else:

        return "待处理"


@csrf_exempt
def updatePost(request):
    phone = request.POST.get("phone")
    postnanme = request.POST.get("postnanme")
    print("phone", phone, postnanme)
    reslut = update("emp", "phone", str(phone), objs=None, post="\'" + postnanme + "\'")
    if reslut == 1:
        msg = {"message": "更新成功"}
    else:
        msg = {"message": "更新失败"}
    sm = json.dumps(msg)
    return HttpResponse(sm)


@csrf_exempt
def getPost(request):
    depName = request.GET.get("department")
    # depName = request.POST.get("depName")
    print("getPost depName:", depName)
    dep = views.getVuale("department", "name", depName)
    objs = {"post": post, "departmentId": dep}
    postObj = views.getVualeAllObj("post", "departmentId", "departmentId", objs)
    resultList = []
    if (postObj.count() == 0):
        # postName
        resultList.append({"postName": "暂无"})
    else:
        for dep in postObj:
            # depNm += str(dep.name) + ","
            resultList.append({"postName": dep.name})
        # depNm = depNm[0:len(depNm) - 1]
    resultOK = json.dumps(resultList)

    return HttpResponse(resultOK, charset='utf-8')


@csrf_exempt
def addPost(request):
    '''
    添加岗位
    :param request:
    :return:
    '''
    # company=companyGet(request)
    depName = request.POST.get("depName")
    postName = request.POST.get("postName")
    # print("addPost :",depName,postName)
    # print("addPost :",depName)
    # 获取外键
    depK = views.getVuale("department", "name", depName)
    postObj = {}
    postObj["name"] = "\'" + depName + "*" + postName + "\'"
    postObj["departmentId"] = "depK"

    objs = {"depK": depK, "post": post}
    result = createData(postObj, "post", objs)
    print("result", result)
    if (result is True):
        msg = {"message": "添加成功"}
    elif (result == "已存在"):
        msg = {"message": "已存在"}
    else:
        msg = {"message": "添加失败"}
    # return JsonResponse(json.dumps(resultOK),safe=False)
    return JsonResponse(msg, charset='utf-8')


def checkFormat(lists: list):
    '''
    检查Decimal datetime
    :param lists:
    :return:
    '''
    for liss in lists:
        for lissK in liss.keys():
            value = liss.get(lissK)
            # print("checkFormat: ",type(value))
            if isinstance(value, Decimal):
                liss[lissK] = str(value)

            elif isinstance(value, datetime):
                liss[lissK] = value.strftime("%Y-%m-%d %H:%M:%S")

    return lists


def getEmp(request):
    '''
    获取员工
    :param request:
    :return:
    '''
    company = companyGet(request)
    emps = views.getAllVuale("emp", "companyId", str(company.id))
    ret = serializers.serialize("python", emps)

    result = getArray(ret, "fields")
    # print("getEmp result:",result)
    # 获取部门名字
    for res in result:
        # print(res['department'])
        re = views.getVuale("department", "id", res['department'])
        res['department'] = re.name

    # print("getEmp - resutl： ", type(result))
    resultOK = json.dumps(checkFormat(result))
    # resultOK.encode('utf-8')
    # print("this getEmp")

    # return HttpResponse(resultOK,content_type="charset=utf-8")
    return JsonResponse(resultOK, safe=False)


def getDep(request):
    '''
    查询部门列表
    :param request:
    :return:
    '''
    # departmentsGetResultAll(request)
    result = departmentsGet(request)
    resultList = []
    for res in result:
        # print("getDep res:",res.id)
        # 部门
        resDict = {"post": post, "departmentId": res}
        # 岗位
        postObj = views.getVualeAllObj("post", "departmentId", "departmentId", resDict)
        # 获取岗位名字组成字符串
        # print("departmentObj type: ",type(departmentObj))
        # print("departmentObj type: ",departmentObj)
        depNm = ""
        if (postObj.count() == 0):
            # postName
            resultList.append({"name": res.name, "postName": "暂无"})
        else:
            for dep in postObj:
                depNm += str(dep.name) + ","
            depNm = depNm[0:len(depNm) - 1]
            resultList.append({"name": res.name, "postName": depNm})

    # print("getDep resultList: ",resultList)
    # 添加到结果中
    # print("departmentObj getDep",departmentObj)
    # result.id
    # ret = serializers.serialize("python", result)
    resultOK = json.dumps(resultList)
    # # print("getDep resutl： ", type(result))
    # print("getDep resultOK： ", result)

    return HttpResponse(resultOK)


def departmentsGetResultAll(request):
    '''
    :param request:
    :return:返回部门全部列表对象
    '''
    departments = departmentsGet(request)
    # 知识点 serialize json 参数 返回str  python 返回dict
    ret = serializers.serialize("python", departments)
    # print("departmentsGetResultAll ret :",ret)
    result = getArray(ret, "fields")
    return result


def departmentsGet(request):
    '''
    查询部门全部对象
    :param request:
    :return:
    '''
    company = companyGet(request)
    departments = views.getAllVuale("department", "companyId", str(company.id))
    return departments


def companyGet(request):
    '''
    获取公司登录对象
    :param request:
    :return:
    '''
    accout = request.session.get("user")
    company = views.getVuale("Company", "account", accout)
    return company


def getArray(checkResult, *fied: str):
    '''
    :param fied: 查询字段元组
    :param checkResult: 查询结果
    :return: 数组对象
    '''
    list = iter(checkResult)
    # print("getArray list",list)
    # todo 未考虑 list 为空的情况
    resultList = []
    for li in list:
        dic = li.get(fied[0])

        resultList.append(dic)
    return resultList


def traverse(list, *fied: str):
    pass
    '''
    遍历数据库查询结果列表 暂时不用 
    :return: 
    '''
    # print("fied, ", fied)

    dic = {}
    for fiedChild in fied[0]:
        # print("fiedChild, ", fiedChild)
        dic[fiedChild] = list.get(fiedChild)

    return dic  # fiedChild

    # return  next(list)


# @postCh
# # @auth todo 要验证不要报错eck
@csrf_exempt
def addDep(request):
    depname = request.POST.get("depName")

    # 验证是否为空
    depnum = len(depname.replace(" ", "")) != 0
    # print(depnum)
    # 验证是否包含"-"
    dep_ = "-" not in depname
    # print(depnum, dep_)
    if (not depnum or not dep_):
        # print(111111)
        #  知识点 跨模块用html  不适用于ajax de render ajax 接收到的是字符串
        # return redirect('/model/erro/loginErro.html', {'error_msg': '类型异常'})
        msg = {"message": "输入类型"}
        # ret = serializers.serialize("json", msg)
        return JsonResponse(msg)
        # return render(request, "model/success.html",context={"success_msg": "depname :" + depname})

    # 查询名字是否重复
    #   获取公司名字

    accout = request.session.get("user")
    company = views.getVuale("Company", "account", accout)
    # companyID=company.id
    # print("companyID ；",companyID)
    cpat = company.name + "-" + depname
    # print(cpat)

    departmentJp = views.check("department", "name", cpat)

    # print("departmentJp ：", departmentJp)
    if (departmentJp):
        msg = {"message": "Erro: depname 重复"}
        return JsonResponse(msg)

    # print("depname:" + depname)
    # 知识点 外键必须是 一个外键对应的对象这里是 company 而不是 companyID
    department.objects.create(name=cpat, companyId=company)
    # 提示添加成功
    msg = {"message": "success: 添加成功"}

    return JsonResponse(msg)


@auth
def addEmp(request, id):
    '''
    添加员工
    :param request:
    :param id:  员工id
    :return:
    '''
    accout = request.session.get("user")
    company = views.getVuale("Company", "account", accout)

    idsStrs = str(id).split("&")
    if (len(idsStrs) != 2):
        mgs = {"message": "非法请求"}
        return JsonResponse(mgs, charset='utf-8')

    # print("id:"+id);
    # print("dep:"+dep);
    # print()
    empId = idsStrs[0]
    dep = idsStrs[1]
    # 判断部门是否存在
    department
    depJ = views.check("department", "name", company.name + "-" + dep)
    # print("depJ :", depJ)
    if (not depJ):
        mgs = {"message": "部门不存在"}
        return JsonResponse(mgs, charset='utf-8')
    departmentObject = views.getVuale("department", "name", "\'" + company.name + "-" + dep + "\'")

    users = views.getVuale("User", "id", empId)
    # Todo 未考虑用户不存在情况
    # print("name： " + users.name)
    employee = {}
    employee['gender'] = users.gender
    if (users.name == "" or users.name is None):

        employee['name'] = str(users.phone)
    else:

        employee['name'] = users.name
    if (users.education == "" or users.education is None):
        employee['education'] = "\'大专\'"
    else:

        employee['education'] = users.education
    employee['phone'] = users.phone
    employee['companyId'] = 'company'
    employee['department'] = departmentObject.id

    employee['email'] = users.email
    # employee['headPortrait'] = users.headPortrait
    employee['identityCard'] = users.identityCard
    employee['birthday'] = users.birthday

    employee['entryTime'] = "\'" + time.strftime('%Y-%m-%d %H:%M:%S') + "\'"
    objs = {"company": company, "emp": emp}
    empJ = createData(employee, "emp", objs)

    if not empJ:
        mgs = {"message": str(empJ) + "添加失败"}
    else:
        if empJ == "员工已存在":
            mgs = {"message": str(empJ)}
        else:
            User.objects.filter(id=empId).update(postStatus=2)
            mgs = {"message": str(empJ) + "添加成功"}
    #     return JsonResponse(mgs)
    # print("empId :"+id)
    # mgs={"dep":id}
    return JsonResponse(mgs, charset='utf-8')


def createData(data: dict, table, objs: dict = None):
    '''
    添加单条数据
    :param data:
    :return:
    '''
    # 遍历字典
    keylist = data.keys()
    dataStr = ""
    for k in keylist:
        dataStr += k + "=" + str(data.get(k)) + ","
    dataStr = dataStr[0:len(dataStr) - 1]

    dataStr = table + ".objects.create(" + dataStr + ")"
    # print("dataStr: " + dataStr)
    try:
        if (objs is not None):
            try:
                exec(dataStr, objs)
            except IntegrityError:
                return "已存在"

        else:
            exec(dataStr)
        return True
    except ObjectDoesNotExist:
        print()
        return False
    # print(dataStr)


@auth
def companyC(request):
    user = request.session.get("user")
    companyHtml = Company.objects.filter(account=user).first()
    Users_Html = User.objects.filter(postStatus=1).order_by("creatTime")

    # 页码 / 总页码
    p_Html = int("2")
    page_size = 10
    pagtor = Paginator(Users_Html, per_page=page_size)

    pTotal_Html = pagtor.num_pages

    # 总数
    total_Html = pagtor.count

    # 当前页面对象数
    Page = pagtor.page(1)
    PageNum_Html = len(Page.object_list)
    # 对象
    page_User_Html = pagtor.page(p_Html).object_list  # 返回对应页码

    page_range_Html = pagtor.page_range
    # print(page_range_Html)
    types = "user"

    types_list = departmentsGetResultAll(request)
    j = 0
    for tl in types_list:
        types_list[j]['name'] = tl['name'].split("-")[1]
        j += 1
    return render(request, "model/company_Center.html", locals())


@auth
def newList(request, types, p):
    """
    :param request:
    :param types: 文章类型
    :param p: 页码
    :return:
    """
    # p = int(p)
    # page_size = 6
    # articles = ArticleType.objects.get(label=types).article_set.order_by("-public_time")
    #
    # article_list = Paginator(articles, page_size)  # 进行分页
    # page_article = article_list.page(p)  # 返回对应页码
    # page_range = set_page(article_list.page_range, p)
    # article_list.num_pages 总页码数，article_list.page_range 下标从 1 开始的页数范围迭代器，article_list.count表示所有页面的对象总数
    Users_Html = User.objects.filter(postStatus=1).order_by("creatTime")

    # 页码 / 总页码
    p_Html = int(p)
    page_size = 10
    pagtor = Paginator(Users_Html, per_page=page_size)

    pTotal_Html = pagtor.num_pages

    # 总数
    total_Html = pagtor.count

    # 当前页面对象数
    Page = pagtor.page(p_Html)
    PageNum_Html = len(Page.object_list)
    # 对象
    page_User_Html = pagtor.page(p_Html).object_list  # 返回对应页码

    # 知识点 处理不跳页面跟换数据
    return render(request, "newlist.html", locals())
