from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 1、models.AutoField　　自增列 = int(11)
    # 　　如果没有的话，默认会生成一个名称为id的列，如果要显示的自定义一个自增列，必须将给列设置为主键
    # primary_key = True。
    # 2、models.CharField　　字符串字段 必须 max_length参数
    # 3、models.BooleanField　　布尔类型 = tinyint(1) 不能为空，Blank = True
    # 4、models.ComaSeparatedIntegerField　　用逗号分割的数字 = varchar　继承CharField，所以必须 max_length参数
    # 5、models.DateField　　日期类型    date    　　对于参数，auto_now = True    则每次更新都会更新这个时间；auto_now_add
    #     则只是第一次创建添加，之后的更新不再改变。
    # 6、models.DateTimeField　　日期类型    datetime    　　同DateField的参数
    # 7、models.Decimal　　十进制小数类型 = decimal    　　必须指定整数位max_digits和小数位decimal_places
    # 8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar    　　对字符串进行正则表达式
    # ^[a-z0-9A-Z]+[-|a-z0-9A-Z._]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$
    # 9、models.FloatField　　浮点类型 = double
    # 10、models.IntegerField　　整形
    # 11、models.BigIntegerField　　长整形
    # 　　integer_field_ranges = {
    # 　　　　'SmallIntegerField': (-32768, 32767),
    # 　　　　'IntegerField': (-2147483648, 2147483647),
    # 　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
    # 　　　　'PositiveSmallIntegerField': (0, 32767),
    # 　　　　'PositiveIntegerField': (0, 2147483647),
    # 　　}
    # 12、models.IPAddressField　　字符串类型（ip4正则表达式）
    # 13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
    # 　参数protocol可以是：both、ipv4、ipv6　验证时，会根据设置报错
    # 14、models.NullBooleanField　　允许为空的布尔类型
    # 15、models.PositiveIntegerFiel　　正Integer
    # 16、models.PositiveSmallIntegerField　　正smallInteger
    # 17、models.SlugField　　减号、下划线、字母、数字
    # 18、models.SmallIntegerField　　数字    　　数据库中的字段有：tinyint、smallint、int、bigint
    # 19、models.TextField　　字符串 = longtext
    # 20、models.TimeField　　时间    HH: MM[:ss[.uuuuuu]]
    # 21、models.URLField　　字符串，地址正则表达式
    # 22、models.BinaryField　　二进制
    # 23、models.ImageField    图片
    # 24、models.FilePathField    文件
