# Generated by Django 2.2.3 on 2019-08-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0060_accountsettings_positionresponsibilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettings',
            name='positionResponsibilities',
            field=models.BooleanField(),
        ),
    ]
