from django.db import models


# Create your models here.
class User(models.Model):
    gender = models.BooleanField("性别", default=1)
    name = models.CharField("姓名", max_length=20)
    education = models.CharField("学历", max_length=20)
    password = models.CharField("密码", max_length=20)
    email = models.CharField("邮件", max_length=200, null=True, blank=True)
    phone = models.CharField("电话", max_length=20, unique=True)
    headPortrait = models.ImageField("头像", null=True, width_field=50, height_field=60, blank=True)
    identityCard = models.CharField("身份证", max_length=18, null=True, unique=True, blank=True)
    birthday = models.DateField("生日", blank=True, null=True)
    type = models.IntegerField("账号类型", default=1)
    postStatus = models.IntegerField("职务状态", default=1)
    creatTime=models.DateTimeField("注册时间")
    models.AutoField

    # 1.upload_to 参数接收一个回调函数 user_directory_path，该函数返回具体的路径字符串，图片会自动上传到指定路径下，
    # 即 MEDIA_ROOT + upload_to
    # 2. user_directory_path 函数必须接收 instace 和 filename 两个参数。参数 instace 代表一个定义了 ImageField
    # 的模型的实例，说白了就是当前数据记录；filename 是原本的文件名
    # 3.null 是针对数据库而言，如果 null =   True, 表示数据库的该字段可以为空；blank 是针对表单的，如果 blank = True，
    # 表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    # photo = models.ImageField('照片', upload_to=user_directory_path, blank=True, null=True)

# # CharField类型不能为空,最少要指定一个长度
# user = models.CharField(max_length=32)

# '''
# DateTimeField、DateField、TimeFiel
# datetime()、date()、time()
# 1920-02-02 00:00:00 、1988-08-08、00:00:00
# '''
# + gender: int
# + name: String
# + email: String
# + phone: String
# + headPortrait: Image
# + identityCard: String
# + birthday: date
