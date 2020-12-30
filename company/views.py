# Create your views here.
from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from company.models import Company, department
from login import views
from login.models import User
from login.views import auth
import json

def getDep(request):
    '''
    查询部门列表
    :param request:
    :return:
    '''
    result = departmentsGetResultAll(request)

    resultOK=json.dumps(result)
    print("resutl： ",type(result))
    print("resutl： ",result)

    return HttpResponse(resultOK)
    # return JsonResponse(msg)


def departmentsGetResultAll(request):
    '''
    返回部门全部列表对象
    :param request:
    :return:
    '''
    departments = departmentsGet(request)
    # 知识点 serialize json 参数 返回str  python 返回dict
    ret = serializers.serialize("python", departments)
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
        # print("li: ",li)
        # ls = next(list)
        # print("ls :", ls)
        # dic = traverse(li, fied)
        dic = li.get(fied[0])

        resultList.append(dic)
    return resultList


def traverse(list, *fied: str):
    pass
    '''
    遍历数据库查询结果列表 暂时不用 
    :return: 
    '''
    print("fied, ",fied)

    dic = {}
    for fiedChild in fied[0]:
        print("fiedChild, ", fiedChild)
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
    print(depnum)
    # 验证是否包含"-"
    dep_ = "-" not in depname
    print(depnum, dep_)
    if (not depnum or not dep_):
        print(111111)
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
    print(cpat)

    departmentJp = views.check("department", "name", cpat)

    # try:
    #     judge = department.objects.get(name='算力科技-123')
    #
    #     departmentJp=True
    # except:
    #     departmentJp = False

    print("departmentJp ：", departmentJp)
    if (departmentJp):
        msg = {"message": "Erro: depname 重复"}
        return JsonResponse(msg)

    # print("depname:" + depname)
    # 知识点 外键必须是 一个外键对应的对象这里是 company 而不是 companyID
    department.objects.create(name=cpat, companyId=company)
    # 提示添加成功
    msg = {"message": "success: 添加成功"}

    return JsonResponse(msg)
    # return render(request, "model/success.html", {"success_msg": "depname :" + depname})


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
    print("id:"+id);
    empId = id
    users = views.getVuale("User", "id", empId)
    # Todo 未考虑用户不存在情况
    print("name： " + users.name)
    employee = {}
    employee['gender'] = users.gender
    employee['name'] = users.name
    employee['education'] = users.education
    employee['email'] = users.email
    employee['phone'] = users.phone
    employee['headPortrait'] = users.headPortrait
    employee['identityCard'] = users.identityCard
    employee['birthday'] = users.birthday

    # employee['post'] = users.postStatus

    employee['companyId '] = company
    # employee['']=users.
    # employee['']=users.

    # print("empId :"+id)

    return JsonResponse(employee)


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
    print(page_range_Html)
    types = "user"

    types_list = departmentsGetResultAll(request)
    j=0
    for tl in types_list:
        types_list[j]['name']=tl['name'].split("-")[1]
        j+=1





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
