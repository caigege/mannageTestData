# Generated by Django 3.1.3 on 2021-01-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('L1_Task_create', '0002_task_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskCreater',
            field=models.CharField(max_length=50, null=True, verbose_name='任务创建者'),
        ),
    ]
