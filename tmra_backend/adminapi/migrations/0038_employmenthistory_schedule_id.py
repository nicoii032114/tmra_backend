# Generated by Django 2.2.3 on 2019-08-05 00:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0037_auto_20190805_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmenthistory',
            name='schedule_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
