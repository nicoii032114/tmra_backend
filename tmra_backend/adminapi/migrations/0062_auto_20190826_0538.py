# Generated by Django 2.2.3 on 2019-08-26 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0061_auto_20190819_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountsettings',
            name='employeeForm',
        ),
        migrations.RemoveField(
            model_name='accountsettings',
            name='employeeList',
        ),
        migrations.RemoveField(
            model_name='accountsettings',
            name='employmentHistory',
        ),
        migrations.RemoveField(
            model_name='accountsettings',
            name='employmentInfo',
        ),
        migrations.RemoveField(
            model_name='accountsettings',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='accountsettings',
            name='trainingEmployee',
        ),
    ]