"""mannageTestData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
route	route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。	必须

view	当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。	必须

kwargs	任意个关键字参数可以作为一个字典传递给目标视图函数。	可选

name	为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。


"""
from django.contrib import admin
from django.urls import path
from  model import views
from L1_Task_create import views as L1_Task_createView
from login import views as loginView
from company import views as companyView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from  login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.model_resp),
    path('', views.detail, name='detail'),
    # path('detailChild/', views.detailChild, name='detailChild'),
    path('detailChild/', views.detailChild, name='detailChild'),
    path('task/', L1_Task_createView.create_Task, name='task'),
    path('sys/login/', loginView.login, name='login'),
    path('sys/welcome/', loginView.fristPage, name='welcome'),
    # path('login/', loginView.welcome, name='hadLogin'),
    path('sys/register/', loginView.register, name='register'),
    path('company/', companyView.companyC, name='company'),
    path('newList/user/', companyView.newList),
    path('addEmp/<id>', companyView.addEmp),
    path('company/addDep/', companyView.addDep),
    path('company/getDep/', companyView.getDep),
    path('company/empGet/', companyView.getEmp),
    path('company/addPost/', companyView.addPost),
    path('company/getPost/', companyView.getPost),


    # path('sys/login/', loginView.fristPage, name='login'),
]
urlpatterns += staticfiles_urlpatterns()
