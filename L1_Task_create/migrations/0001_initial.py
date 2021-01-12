# Generated by Django 3.1.3 on 2021-01-12 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=100, unique=True, verbose_name='任务名')),
                ('content', models.CharField(max_length=1000, verbose_name='任务内容')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='任务创建时间')),
                ('startTime', models.DateTimeField(blank=True, null=True, verbose_name='任务开始时间')),
                ('taskTime', models.IntegerField(default=0, verbose_name='工作时间长')),
                ('strategy', models.IntegerField(default=1, verbose_name='任务策略')),
                ('taskLevel', models.IntegerField(default=1, verbose_name='任务级别')),
                ('selectDep', models.CharField(max_length=100, verbose_name='部门')),
                ('selectPost', models.CharField(max_length=100, verbose_name='岗位')),
                ('selectEmp', models.CharField(max_length=100, verbose_name='任务指派')),
                ('upTaskId', models.IntegerField(default=0, verbose_name='上级任务')),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='business.project', verbose_name='项目id')),
            ],
        ),
    ]
