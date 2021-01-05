list=[]

if(list==[]):
    print(1)

# lis = [{"gender":  True, "name": "13557376460", "education": "we", "phone": "13557376460", "companyId": 1, "level": 1,
#         "department": 2, "salary": "0.00", "email": None, "headPortrait": "", "identityCard": None, "birthday": None,
#         "post": None, "entryTime": "2021-01-04 01:48:54"},
#        {"gender": True, "name": "15583436117", "education": "eee", "phone": "15583436117", "companyId": 1, "level": 1,
#         "department": 3, "salary": "0.00", "email": None, "headPortrait": "", "identityCard": None, "birthday": None,
#         "post": None, "entryTime": "2021-01-04 01:57:31"}]
#
# for i in lis:
#     print(i["name"])

# from decimal import Decimal


# a=1
# b=2.2
# c=float(2.2)
# print(a,b,c)
# print(type(a),type(b),type(c))
# bb=Decimal(b)
# cc=Decimal(c)
#
# print(type(type(bb)),type(cc))
# bbb=str(bb)
#
# print(type(bbb))
#
# if str(type(bb))=="<class 'decimal.Decimal'>":
#     print("this is Decimal")
# print(type(bb))
# from django.test import TestCase
#
# # Create your tests here.
# import time
#
# employee = {}
# employee['gender'] = 1
# employee['name'] = "张三"
# employee['education'] = "本科"
# employee['phone'] = 13200000001
# employee['companyId'] = 1
#
# employee['email'] = "35644648@163.com"
# # employee['headPortrait'] = users.headPortrait
# employee['identityCard'] = "511231199908014661"
# employee['birthday'] = "1984-04-14 13:00:00"
#
# # employee['post'] = users.postStatus
#
# # employee['companyId '] = company
# #
# employee['entryTime'] = time.strftime('%Y-%m-%d %H:%M:%S')
#
# # s="suan;l".split(";")[1]
# # print(s)
#
# def createData(data:dict,table):
#     '''
#     添加单条数据
#     :param data:
#     :return:
#     '''
#     # 遍历字典
#     keylist=data.keys()
#     dataStr=""
#     for k in keylist:
#         dataStr+=k+"="+str(data.get(k))+","
#     dataStr=dataStr[1:len(dataStr)-1]
#     dataStr=table+".objects.create("+dataStr+")"
#     try:
#         exec(dataStr)
#         return True
#     except ObjectDoesNotExist:
#         return False
#     print(dataStr)
#
#
# createData(employee,"emp")
#
#
#
#
#
#
# # import json
# # import chardet
# #
# # #json字符串，json类型根字符串有关系，平时最多是字典
# # mydict={"name":"yincheng","QQ":["77025077","12345"]}
# # # mydict=[1,2,3,4,5,6]
# # print( json.dumps(mydict) )
# # print( type( json.dumps(mydict) ) )
# #查看编码
# # print( chardet.detect( json.dumps(mydict) ) )
# # 知识点 添加
# # dic={}
# # dic['feq']=1
# # import  inspect
# # # 知识点 遍历字典
# # print(dic['feq'])
# #
# # def n(r=1):
# #     a=1
# #     v=locals()
# #     # print(v.fromkeys())
# #     print(len(v))
# # n()
# # ase=(1,2,3)
# # for asedown in ase:
# #     print(asedown)
