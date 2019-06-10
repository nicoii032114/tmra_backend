# Generated by Django 2.2.1 on 2019-05-30 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0007_auto_20190530_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('certified_by', models.CharField(max_length=50)),
                ('performance_rating', models.DecimalField(decimal_places=2, max_digits=16)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.Employee')),
            ],
        ),
    ]