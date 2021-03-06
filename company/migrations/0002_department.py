# Generated by Django 3.1.3 on 2020-12-29 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='部门')),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company', verbose_name='公司id')),
            ],
        ),
    ]
