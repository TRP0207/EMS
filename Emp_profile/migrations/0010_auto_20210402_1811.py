# Generated by Django 3.1.7 on 2021-04-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_profile', '0009_auto_20210331_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='is_denied',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
