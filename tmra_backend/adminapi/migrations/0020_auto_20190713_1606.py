# Generated by Django 2.2.1 on 2019-07-13 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0019_auto_20190713_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainees',
            old_name='training_name',
            new_name='training',
        ),
    ]