# Generated by Django 2.2.1 on 2019-07-14 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0026_auto_20190714_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individualpoints',
            old_name='nonpaid_billiable',
            new_name='notpaid_billiable',
        ),
    ]
