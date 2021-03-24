# Create your views here.
from django.core import serializers

from L1_UserTaskRecode.models import TaskCode
from business.models import project
from company.models import department
from company.views import createData
from employee.models import emp
from login import views

def codeTask(obj, upstate):
    '''
    状态变化
    :param obj:可以是对象，也可以是字典
    :return:
    '''


    s_obj = serializers.serialize('python', obj)
    objK=s_obj[0]
    objC=objK['fields']
    data = {}
    # 查询pk
    depObj=department.objects.filter(name=objC["selectDep"])
    depObj_obj=serializers.serialize('python',depObj)
    depObj_objK=depObj_obj[0]
    # depObj_objC=depObj_objK['fields']

    empObj = emp.objects.filter(phone=objC["selectEmp"])
    empObj_obj = serializers.serialize('python', empObj)
    empObj_objK = empObj_obj[0]


    data["upstate"]=upstate
    data["projectId"]='projectId'
    data["taskId"]=objK["pk"]
    data["departmentId"]="\'" +str(depObj_objK['pk'])+"\'"
    data["empId"]="\'" +str(empObj_objK["pk"])+"\'"
    data["state"]=objC["state"]
    data["taskName"]="\'" +objC["taskName"]+"\'"


    proId = views.getVuale("project", "id", objC["projectId"])
    objs = {"projectId": proId, "TaskCode": TaskCode}
    createData(data,"TaskCode",objs)

    print("obj:", s_obj,type(s_obj))
