from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('accounts/signup/',views.signupView,name='signup'),
    path('accounts/login/',views.loginView,name='login'),
    path('accounts/logout/',views.logoutView,name='logout'),
    path('accounts/forgotpassword/',views.forgotPassword,name='forgotpassword'),
    path('adminDashboard/',views.adminDashboard,name='adminDashboard'),
]