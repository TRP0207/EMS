# Generated by Django 3.1.7 on 2021-03-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_profile', '0003_auto_20210312_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
    ]