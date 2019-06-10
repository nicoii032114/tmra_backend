# Generated by Django 2.2.1 on 2019-06-05 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0015_auto_20190602_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='budget',
            new_name='budget_id',
        ),
        migrations.AlterField(
            model_name='employmentdetails',
            name='flexi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rolesresponsibilities',
            name='position',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='rolesresponsibilities',
            name='responsibilities',
            field=models.CharField(max_length=5000),
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('training_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.Training')),
            ],
        ),
    ]
