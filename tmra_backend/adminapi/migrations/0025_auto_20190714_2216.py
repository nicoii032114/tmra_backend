# Generated by Django 2.2.1 on 2019-07-14 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0024_auto_20190714_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individualpoints',
            old_name='extra_wordload',
            new_name='extra_workload',
        ),
    ]
