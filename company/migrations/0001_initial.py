# Generated by Django 3.1.3 on 2020-12-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='公司名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('IdNum', models.CharField(blank=True, max_length=200, null=True, verbose_name='企业代码')),
                ('account', models.CharField(max_length=20, unique=True, verbose_name='账号/电话')),
                ('description', models.TextField(max_length=2000, null=True, verbose_name='公司简介')),
                ('business', models.TextField(max_length=1000, null=True, verbose_name='公司业务范围')),
                ('trademark', models.ImageField(blank=True, height_field=60, null=True, upload_to='', verbose_name='头像', width_field=50)),
            ],
        ),
    ]
