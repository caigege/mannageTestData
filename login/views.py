from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from login.models import User

def fristPage(request):
    '''
    :param request: 首頁
    :return:
   '''
    return render(request, 'model/login.html')


def login(request):
    if request.method == 'POST':

        account = request.POST.get("account")
        print("---- :"+account)

        phoneJp = check("User", "phone", account)
        print(phoneJp)

        if (phoneJp == False):
            # 账号不存在
            return render(request, 'model/erro/loginErro.html', {'error_msg': '账号/或密码错误'})
        else:
            # 知识点：获取某条记录字段的值
            password = request.POST.get("password")
            print(password)
            getVuale("User", "phone", account)
            return redirect('/login/')



#     *
#         if len(account) < 3 or len(account) > 12:
#             return render(request, 'model/erro/loginErro.html', {'error_msg': '用户名长度最小3位，最大12位'})
#         password = request.POST.get('password')
#         # User.objects.create(name=username, pwd=pwd)
#         print(password)
#         return
#     return render(request, '不用Django中form表单模块.html')
# *
def welcome(request):
    return render(request, 'model/welcom.html')
def check(table,field,fieldObject):
    checkObject="judge="+table+".objects.get("+field+"="+fieldObject+")"
    try:
        exec(checkObject)

        return True
    except ObjectDoesNotExist:
        return False

def getVuale(table,field,fieldObject):
    checkObject="judge="+table+".objects.get("+field+"="+fieldObject+")"

    # checkObject=checkObject+"return judge"
    print(checkObject)
    result=exec(checkObject)
    # print("result:"+result)
    print("result:"+type(result))
    return result


def register(request):
    print("register-----")
    if request.method == 'POST':
        account = request.POST.get("account")
        print("---- :" + account)
        phoneJp = check("User","phone",account)
        print(phoneJp)
        if(phoneJp==False):
            password = request.POST.get("password")
            print(password)
            User.objects.create(phone=account,password=password)
            return redirect('/login/')
        else:
            return render(request, 'model/erro/loginErro.html', {'error_msg': '手机号已注册'})

    return render(request, 'model/erro/loginErro.html', {'error_msg': 'get请求异常'})

