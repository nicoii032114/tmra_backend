# Generated by Django 2.2.1 on 2019-06-02 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0013_auto_20190530_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
