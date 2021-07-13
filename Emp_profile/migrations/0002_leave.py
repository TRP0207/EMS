# Generated by Django 3.1.7 on 2021-03-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_leave', models.CharField(choices=[('Casual Leave(CL)', 'Casual Leave(CL)'), ('Sick Leave (SL)', 'Sick Leave (SL)'), ('Maternity Leave (ML)', 'Maternity Leave (ML)'), ('Paternity Leave', 'Paternity Leave'), ('Marriage Leave', 'Marriage Leave')], default='', max_length=20)),
                ('days_of_leave', models.PositiveIntegerField()),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
    ]
