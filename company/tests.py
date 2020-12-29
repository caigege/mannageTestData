from django.test import TestCase

# Create your tests here.
# 知识点 添加
dic={}
dic['feq']=1
import  inspect
# 知识点 遍历字典
print(dic['feq'])

def n(r=1):
    a=1
    v=locals()
    # print(v.fromkeys())
    print(len(v))
n()