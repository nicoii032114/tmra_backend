# Generated by Django 2.2.3 on 2019-08-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0040_auto_20190805_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentdetails',
            name='end_of_contract',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employmentdetails',
            name='resignation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
