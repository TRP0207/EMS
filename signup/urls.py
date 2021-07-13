from django.urls import path
from .views import home,login_request,logout_request

app_name='signup'

urlpatterns=[
    path('',home,name='home'),
    path('login/',login_request, name='login'),
    path('base/logout/',logout_request,name='logout'),
    path('accounts/login/',login_request, name='login'),

    ]