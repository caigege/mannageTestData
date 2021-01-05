# Generated by Django 3.1.3 on 2021-01-05 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='部门')),
                ('departmentId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.department', verbose_name='公司部门id')),
            ],
        ),
    ]
