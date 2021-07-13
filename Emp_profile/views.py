from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ProfileForm, LeaveForm
from .models import Employee, Leave
from .decorators import manager_required
from EMS.settings import EMAIL_HOST_USER


@login_required
def base(request):
    user = request.user
    return render(request, 'Emp_profile/base.html', {'user': user})


@manager_required
def Emp_form(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/base/')

    else:
        form = ProfileForm()
    return render(request, "Emp_profile/Emp_Form.html", {'form': form})


@login_required
def Emp_list(request):
    emp = Employee.objects.filter(is_superuser=False)
    return render(request, "Emp_profile/Emp_list.html", {'employee': emp})


@login_required
def Emp_detail(request, employee_id):
    obj = get_object_or_404(Employee, employee_id=employee_id)
    return render(request, 'Emp_profile/Emp_detail.html', {'obj': obj})


@manager_required
def update(request, employee_id):
    emp = get_object_or_404(Employee, employee_id=employee_id)
    form = ProfileForm(request.POST or None, instance=emp)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('/base/Emp_list')
    else:
        pass
    return render(request, "Emp_profile/Emp_Form.html", {'form': form})


@manager_required
def delete(request, employee_id):
    emp = Employee.objects.get(employee_id=employee_id)
    emp.delete()
    return redirect("/base/")


@login_required
def Emp_leaveform(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/base/')
    else:
        form = LeaveForm()
    return render(request, "Emp_leaveform.html", {'form': form})


@manager_required
def Leave_list(request):
    leave = Leave.objects.filter(is_approved__isnull=True)
    return render(request, "Leave_list.html", {'leave': leave})


@manager_required
def approve_leave(request, employee_id):
    leave = get_object_or_404(Leave, employee_id=employee_id)
    leave.is_approved = True
    leave.save()
    print(leave)
    to = get_object_or_404(Leave, employee_id=employee_id)
    print(to.email)
    subject = 'Regarding to your leave application'
    message = 'Your Leave has been approved by the management...'
    recepient = to.email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    return render(request, "Emp_profile/base.html")


@manager_required
def deny_leave(request, employee_id):
    leave = get_object_or_404(Leave, employee_id=employee_id)
    leave.is_approved = False
    leave.save()
    print(leave)
    to = get_object_or_404(Leave, employee_id=employee_id)
    print(to.email)
    subject = 'Regarding to your leave application'
    message = 'Your Leave has been Denied by the management...'
    recepient = to.email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    return render(request, "Emp_profile/base.html")


@manager_required
def approved_leave_list(request):
    leave = Leave.objects.filter(is_approved=True)
    return render(request, "approved_leave_list.html", {'leave': leave})


@manager_required
def denied_leave_list(request):
    leave = Leave.objects.filter(is_approved=False)
    return render(request, "denied_leave_list.html", {'leave': leave})
