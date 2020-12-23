from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
'''选择日期创建任务'''
# from django.shortcuts import render
def create_Task(request):
    return render("创建任务")

# date=time(),who="小米",taskName="任务名",taskContent="任务内容"

# def create_Task(request):
#
#     return HttpResponse("创建任务")

