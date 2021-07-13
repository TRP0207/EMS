from django.urls import path
from . import views 

app_name = 'Emp_profile'

urlpatterns=[
    path('',views.base, name='base'),
    path('Emp_list/',views.Emp_list,name='Emp_list'),
    path('Emp_list/detail/<int:employee_id>/',views.Emp_detail,name='Emp_detail'),
    path('update/<int:employee_id>', views.update, name="update"),  
    path('delete/<int:employee_id>', views.delete, name="delete"),
    path('Emp_form/',views.Emp_form, name='Emp_Form'),
    path('apply_for_leave/',views.Emp_leaveform, name='apply_for_leave'),
    path('leave_list/', views.Leave_list, name='leave_list'),
    path('approve_leave/<int:employee_id>', views.approve_leave, name='approve_leave'),
    path('deny_leave/<int:employee_id>', views.deny_leave, name='deny_leave'),
    path('approved_leave_list/',views.approved_leave_list, name='approved_leave_list'),
    path('denied_leave_list/', views.denied_leave_list, name='dined_leave_list'),

]
