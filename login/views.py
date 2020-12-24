import re

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from company.models import Company
from login.models import User


def fristPage(request):
    '''
    :param request: 首頁
    :return:
   '''
    types = [{"typeName": "个人", "typeNum": 1}, {"typeName": "企业", "typeNum": 2}]
    context = {"types_list": types}
    return render(request, 'model/login.html', context)


def login(request):
    if request.method == 'POST':
        typeL = request.POST.get("type")
        account = request.POST.get("account")
        password = request.POST.get("password")
        # print("---- :" + account)

        # ----------------------------------
        if (typeL == "个人"):
            print("个人账号登录")
            phoneJp = check("User", "phone", account)

            if (phoneJp == True):

                # 知识点：获取某条记录字段的值

                print(password)
                user = getVuale("User", "phone", account)
                passwordDB = user.password

                print("passwordDB: " + passwordDB)
                if (password == passwordDB):

                    return render(request, 'model/welcom.html', {'msg': '个人版'})

            return render(request, 'model/erro/loginErro.html', {'error_msg': '账号/或密码错误'})

        elif (typeL == "企业"):
            print("企业账号登录")
            accountJp = check("Company", "account", account)

            if (accountJp == True):

                # 知识点：获取某条记录字段的值

                print(password)
                user = getVuale("Company", "account", account)
                passwordDB = user.password

                print("passwordDB: " + passwordDB)
                if (password == passwordDB):
                    # return redirect('/login/')
                    return render(request, 'model/welcom.html', {'msg': '企业版'})
            return render(request, 'model/erro/loginErro.html', {'error_msg': '账号/或密码错误'})
        else:
            return render(request, 'model/erro/loginErro.html', {'error_msg': '类型异常'})
        # ----------------------------------
    return render(request, 'model/erro/loginErro.html', {'error_msg': 'get请求异常'})


def welcome(request):

    return render(request, 'model/welcom.html')


def check(table, field, fieldObject):
    checkObject = "judge=" + table + ".objects.get(" + field + "=\'" + fieldObject + "\')"
    print("checkObject :"+checkObject)
    try:
        exec(checkObject)
        return True
    except ObjectDoesNotExist:
        return False


def getVuale(table, field, fieldObject):
    checkObject = table + ".objects.get(" + field + "=" + fieldObject + ")"

    # checkObject=checkObject+"return judge"
    print(checkObject)
    result = eval(checkObject)
    print("result:" + str(result))
    # print("result:"+type(result))

    return result
    # return result


def register(request):
    print("register-----")
    # todo 输入判断未处理
    if request.method == 'POST':
        account = request.POST.get("account")
        password = request.POST.get("password")
        typeL = request.POST.get("type")
        companyName = request.POST.get("companyName")


        if (re.match("^1[3456789]\d{9}$", account) == None):
            return render(request, 'model/erro/loginErro.html', {'error_msg': '输入正确手机号' + account})

        if (len(password) > 10 or len(password) < 3):
            return render(request, 'model/erro/loginErro.html', {'error_msg': '密码长度3-10'})

        if (typeL == "个人"):
            phoneJp = check("User", "phone", account)

            if (phoneJp == False):
                User.objects.create(phone=account, password=password)
                return redirect('/login/')

            return render(request, 'model/erro/loginErro.html', {'error_msg': '手机号已注册'})

        elif (typeL == "企业"):
            companyNameJp = check("Company", "account", account)
            if (companyNameJp == False):
                if (len(companyName) == 0):
                    return render(request, 'model/erro/loginErro.html', {'error_msg': '公司名为空'})
                else:
                    companyNameJp = check("Company", "name", companyName)
                    if (companyNameJp == False):

                        Company.objects.create(account=account, password=password, name=companyName)
                        return redirect('/login/')
                    return render(request, 'model/erro/loginErro.html', {'error_msg': '公司名重复'})

            return render(request, 'model/erro/loginErro.html', {'error_msg': '手机号已注册'})
        else:
            return render(request, 'model/erro/loginErro.html', {'error_msg': '类型异常'})
    return render(request, 'model/erro/loginErro.html', {'error_msg': 'get请求异常'})
