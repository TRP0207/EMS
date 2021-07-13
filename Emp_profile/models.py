from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class Employee(AbstractUser):
    is_manager = models.BooleanField(default=False,blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    employee_id = models.CharField(unique=True,max_length=6,null=False)
    department = models.CharField(max_length=25, null=False)
    job_title = models.CharField(max_length=25, null=False)
    doj = models.DateField(null=True)
    TYPE_CHOICES = (
        ('part-time', 'Part-time'),
        ('full-time', 'Full-time'),
    )
    employment_type = models.CharField(max_length=10,
                                         choices=TYPE_CHOICES,
                                         default='full-time')
    salary = models.CharField(max_length=10)
    address = models.TextField(max_length=100, default="")
    mobile_number = models.CharField(max_length=10)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=25, null=True)
    pin_code = models.CharField(max_length=25, null=True)
    state = models.CharField(max_length=25, null=True)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES,
                              default='male')
    MS_CHOICES = (
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
    )
    marrital_status = models.CharField(max_length=10,
                                       choices=MS_CHOICES,
                                       default='married')
    hobbies = models.CharField(max_length=25, null=True)

    def get_absolute_url(self):
        return reverse("Emp_profile:Emp_detail", args=[self.employee_id])

    def __str__(self):
        return self.first_name

class Leave(models.Model):
    TYPE_CHOISE = (
        ('Casual Leave(CL)','Casual Leave(CL)'),
        ('Sick Leave (SL)','Sick Leave (SL)'),
        ('Maternity Leave (ML)','Maternity Leave (ML)'),
        ('Paternity Leave','Paternity Leave'),
        ('Marriage Leave','Marriage Leave'),
    )

    email = models.EmailField(max_length=30,default="")
    employee_id = models.CharField(unique=True,max_length=6,default="")
    type_of_leave = models.CharField(choices=TYPE_CHOISE,default="", max_length=20)
    days_of_leave = models.PositiveIntegerField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_approved = models.BooleanField(default="", blank= True, null=True)
