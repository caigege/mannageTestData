# Generated by Django 3.1.3 on 2020-12-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField(default=1, verbose_name='性别')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('education', models.CharField(max_length=20, verbose_name='学历')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='邮件')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='电话')),
                ('headPortrait', models.ImageField(blank=True, height_field=60, null=True, upload_to='', verbose_name='头像', width_field=50)),
                ('identityCard', models.CharField(blank=True, max_length=18, null=True, unique=True, verbose_name='身份证')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('level', models.IntegerField(default=1, verbose_name='等级')),
                ('post', models.CharField(blank=True, max_length=20, null=True, verbose_name='岗位')),
                ('department', models.IntegerField(default=1, verbose_name='部门')),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='工资')),
                ('entryTime', models.DateTimeField(auto_now_add=True, verbose_name='入职时间')),
            ],
        ),
    ]
