from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from company.models import Company
from login.models import User
from login.views import auth
from login import views
from django.core.paginator import Paginator


@auth
def addEmp(request,id):
    accout = request.session.get("user")
    company =views.getVuale("Company","account",accout)

    empId= id
    users = views.getVuale("User","id",empId)
    # Todo 未考虑用户不存在情况
    print("name： "+users.name)
    employee={}
    employee['gender']=users.gender
    employee['name']=users.name
    employee['education']=users.education
    employee['email']=users.email
    employee['phone']=users.phone
    employee['headPortrait']=users.headPortrait
    employee['identityCard']=users.identityCard
    employee['birthday']=users.birthday

    employee['post']=users.post

    employee['companyId ']=company.id
    # employee['']=users.
    # employee['']=users.

    # print("empId :"+id)

    return










@auth
def companyC(request):
    user = request.session.get("user")
    companyHtml=Company.objects.filter(account=user).first()
    Users_Html = User.objects.filter(postStatus=1).order_by("creatTime")

    # 页码 / 总页码
    p_Html = int("2")
    page_size=1
    pagtor = Paginator(Users_Html, per_page=page_size)

    pTotal_Html=pagtor.num_pages

    # 总数
    total_Html=pagtor.count

    # 当前页面对象数
    Page=pagtor.page(1)
    PageNum_Html=len(Page.object_list)
    # 对象
    page_User_Html = pagtor.page(p_Html).object_list  # 返回对应页码

    page_range_Html=pagtor.page_range
    print(page_range_Html)
    types="user"
    return render(request,"model/company_Center.html",locals())


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