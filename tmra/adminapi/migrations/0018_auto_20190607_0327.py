# Generated by Django 2.2.1 on 2019-06-07 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0017_trainees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='budget_id',
        ),
        migrations.AddField(
            model_name='training',
            name='training_duration',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
