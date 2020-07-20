"""IT_technology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ITapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('about_us/', views.about_us, name="about_us"),
    path('admin1/', views.admin1, name="admin1"),
    path('admin_login_check/', views.admin_login_check, name="admin_login_check"),
    path('schedule_newcls/', views.schedule_newcls, name="schedule_newcls"),
    path('save_classes/', views.save_classes, name="save_classes"),
    path('viewschedule_class/', views.viewschedule_class, name="viewschedule_class"),
    path('update_cls/',views.update_cls,name="update_cls"),
    path('upcls/',views.us_cls,name="upcls"),
    path('delete_course/',views.delete_course,name="delete_course"),
    path('student/', views.student, name="student"),
    path('student_register/', views.student_register, name="student_register"),
    path('save_student/', views.save_student, name="save_student"),
    path('student_login_check/', views.student_login_check, name="student_login_check"),
    path('enroll_course/',views.enroll_course,name="enroll_course"),
    path('add_enroll/',views.add_enroll,name="add_enroll"),
    path('view_enroll_courses/',views.view_enroll_courses,name="view_enroll_courses"),
    path('cancel_enroll_class/',views.cancel_enroll_class,name="cancel_enroll_class")


]
