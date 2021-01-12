import re
import secrets
import time

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from company.models import Company,department,post

from login.models import User
from employee.models import emp
from business.models import project
@csrf_exempt
def exit(request):
    del request.session["user"]

    # klist=session.keys()
    # dataStr=""
    # for k in klist:
    #     dataStr+=k+"="+str(session.get(k))+","
    # print("dataStr exit:"+dataStr)

    # accout = request.session.get("user")
    # accout = request.session.get("user")
    # accout = request.session.get("user")
    print()
    msg = {"message": "success: 添加成功"}

    return JsonResponse(msg)

def  fristPage(request):
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
                    # request.session["key"]=

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
                    cookie = request.COOKIES.get("csrftoken")
                    print("cookie ：" + cookie)
                    # request.session['is_login'] = True
                    request.session['user'] = account
                    request.session['csrftoken'] = cookie
                    result=render(request, 'model/welcom.html', {'msg': '企业版'})
                    result.set_cookie('csrftoken',cookie)
                    return result
            return render(request, 'model/erro/loginErro.html', {'error_msg': '账号/或密码错误'})
        else:
            return render(request, 'model/erro/loginErro.html', {'error_msg': '类型异常'})
        # ----------------------------------
    return render(request, 'model/erro/loginErro.html', {'error_msg': 'get请求异常'})

def auth(func):
    # token验证
    def inner(request,*args,**kwargs):
        v=request.COOKIES.get('csrftoken')
        if not v:
            return  redirect('/sys/welcome/')
        return func(request,*args,**kwargs)
    return inner


def postCheck(func):
    # 请求验证
    def inner(request,*args,**kwargs):
        v=request.method=='POST'
        if not v:
            render(request, 'model/erro/loginErro.html', {'error_msg': '类型异常'})
        return func(request,*args,**kwargs)
    return inner







# def welcome(request):
#
#     cft=request.session.get("csrftoken")
#     print("ctf :" +cft )
#     return render(request, 'model/welcom.html')


def check(table, field, fieldObject):
    '''
    判断是否存在 相当于from * table where field=fieldObject
    :param table: 表名 string
    :param field: 字段名 string
    :param fieldObject: 字段值
    :return: Ture 存在 False 不存在
    '''
    print("fieldObject: "+fieldObject)
    checkObject = "judge=" + table + ".objects.get(" + field + "=\'" + fieldObject + "\')"
    print("checkObject :"+checkObject)
    try:
        exec(checkObject)
        return True
    except ObjectDoesNotExist:
        return False


def getVuale(table, field, fieldObject):
    '''
    获取单个对象
    :param table: String：  models. class 类名
    :param field: String 字段名
    :param fieldObject: 对象
    :return:
    '''
    # print("getVuale-fieldObject: " , fieldObject)
    checkObject = table + ".objects.get(" + field + "=\'" + str(fieldObject) + "\')"

    print("checkObject :" + checkObject)
    try:
        result = eval(checkObject)
    except:
        checkObject = table + ".objects.get(" + field + "=" + str(fieldObject) + ")"
        print("checkObject except :"+checkObject)
        result = eval(checkObject)
    # print("result:" + str(result))

    return result


def getVualeStr(table, field, fieldObject:str):
    '''
    获取单个对象
    :param table: String：  models. class 类名
    :param field: String 字段名
    :param fieldObject: 对象
    :return:
    '''
    # print("getVuale-fieldObject: " , fieldObject)
    checkObject = table + ".objects.get(" + field + "=\'" + str(fieldObject) + "\')"

    print("checkObject :" + checkObject)
    try:
        result = eval(checkObject)
    except:
        # checkObject = table + ".objects.get(" + field + "=" + str(fieldObject) + ")"
        # print("checkObject except :"+checkObject)
        result = {"msg":"未查询到"}
    # print("result:" + str(result))

    return result



def getVualeAllObj(table, field, fieldObject,objs):
    '''
    获取单个对象 传对象 外键
    :param table: String：  models. class 类名
    :param field: String 字段名
    :param fieldObject: 对象
    :return:
    '''
    # print("getVuale-fieldObject: " , fieldObject)
    checkObject = table + ".objects.filter(" + field + "=" + str(fieldObject) + ")"

    # print(checkObject)

    result = eval(checkObject,objs)
    # print("result:" + str(result))

    return result


def getAllVuale(table, field, fieldObject):
    '''
    获取单个对象或多个对象(数据库行）
    :param table: String：  models. class 类名
    :param field: String 字段名
    :param fieldObject: 对象
    :return:
    '''
    checkObject = table + ".objects.filter(" + field + "=" + fieldObject + ")"

    # print(checkObject)
    try:
        result = eval(checkObject)
    except:
        # checkObject = table + ".objects.get(" + field + "=" + str(fieldObject) + ")"
        # print("checkObject except :"+checkObject)
        result = {"msg": "查询异常"}
    # result = eval(checkObject)
    # print("result:" + str(result))

    return result


def register(request):
    print("register-----")
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
                User.objects.create(phone=account, password=password,creatTime=time.strftime('%Y-%m-%d %H:%M:%S'))
                return render(request, 'model/welcom.html', {'msg': '个人版'})

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
                        return render(request, 'model/welcom.html', {'msg': '企业版'})
                    return render(request, 'model/erro/loginErro.html', {'error_msg': '公司名重复'})

            return render(request, 'model/erro/loginErro.html', {'error_msg': '手机号已注册'})
        else:
            return render(request, 'model/erro/loginErro.html', {'error_msg': '类型异常'})
    return render(request, 'model/erro/loginErro.html', {'error_msg': 'get请求异常'})
