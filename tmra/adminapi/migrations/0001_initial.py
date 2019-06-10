# Generated by Django 2.2.1 on 2019-05-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.IntegerField()),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('birthday', models.DateField()),
                ('citizenship', models.CharField(max_length=20)),
                ('height', models.DecimalField(decimal_places=2, max_digits=16)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=16)),
                ('blood_type', models.IntegerField()),
            ],
        ),
    ]