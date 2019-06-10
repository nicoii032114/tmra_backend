# Generated by Django 2.2.1 on 2019-05-30 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0005_auto_20190530_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('points', models.IntegerField()),
                ('hours_classification', models.CharField(max_length=50)),
                ('hours_duration', models.DateField()),
                ('actual_hours', models.DateField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.Employee')),
            ],
        ),
    ]