# Generated by Django 3.1.7 on 2021-03-26 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_profile', '0005_auto_20210326_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='approve',
            new_name='is_approved',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='deny',
            new_name='is_denied',
        ),
    ]
