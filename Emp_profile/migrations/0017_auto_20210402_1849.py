# Generated by Django 3.1.7 on 2021-04-02 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_profile', '0016_auto_20210402_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='Approve_or_Deny',
            new_name='is_approved',
        ),
    ]
