# Generated by Django 2.2.3 on 2019-07-29 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0032_user_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.TimeField()),
                ('date', models.DateField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.Employee')),
            ],
        ),
    ]
