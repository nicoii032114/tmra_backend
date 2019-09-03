# Generated by Django 2.2.3 on 2019-08-08 23:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0047_accountsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsettings',
            name='user_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
