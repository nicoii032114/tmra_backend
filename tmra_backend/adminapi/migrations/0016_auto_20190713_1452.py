# Generated by Django 2.2.1 on 2019-07-13 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0015_auto_20190713_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.Training'),
        ),
    ]
