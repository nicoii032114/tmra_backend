# Generated by Django 2.2.3 on 2019-08-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0035_auto_20190805_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmenthistory',
            name='schedule_id',
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='basic_rate',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='challenge_quota',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='date_effective',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='date_employed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='employee_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='employment_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='end_of_contract',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='flexi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='incentive',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='quota',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='resignation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='salary_base',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
    ]
