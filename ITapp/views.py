from django.contrib import messages
from django.shortcuts import render, redirect

from ITapp.models import ScheduleclassModel,Student_register_Model


def index(request):
    return render(request,"index.html")


def about_us(request):
    return render(request,"about_us.html")


def admin1(request):
    return render(request,"admin1.html")

def admin_login_check(request):
    un = request.POST.get("t1")
    ps = request.POST.get("t2")

    if un == "yash" and ps == "kumar2280":
        return render(request, "admin_home_page.html")
    else:
        messages.error(request, "INVALID USER")
        return redirect("admin1")

def schedule_newcls(request):
    return render(request,"schedule_newcls.html")


def save_classes(request):
   c_name =request.POST.get("s1")
   faculty=request.POST.get("s2")
   date=request.POST.get("s3")
   time=request.POST.get("s4")
   fees=request.POST.get("s5")
   durations=request.POST.get("s6")
   ScheduleclassModel(course_name=c_name,faculty=faculty,date=date,time=time,fee=fees,duration=durations).save()
   messages.success(request,"COURSE SAVED")
   return redirect('schedule_newcls')


def viewschedule_class(request):
    result=ScheduleclassModel.objects.all()
    return render(request,"viewschedule_class.html",{"data":result})



def student(request):
    return render(request,"student.html")


def student_register(request):
    return render(request,"student_register.html")

def save_student(request):
    sname = request.POST.get("r1")
    scno = request.POST.get("r2")
    sem = request.POST.get("r3")
    spass = request.POST.get("r4")
    Student_register_Model(name=sname,contact_no=scno,email=sem,password=spass).save()
    messages.success(request,"Successfully Registered")
    return redirect('student_register')



def student_login_check(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")
    try:
        Student_register_Model.objects.get(email=uname,password=upass)
        return render(request,"student_view.html")
    except Student_register_Model.DoesNotExist:
        messages.error(request,"invalid user")
        return redirect('student')


def enroll_course(request):
    res=ScheduleclassModel.objects.all()
    return render(request,"enroll_course.html",{"data":res})


def add_enroll(request):
    course_id=request.GET.get("t1")
    course_name=request.GET.get("t2")
    response=redirect('enroll_course')
    if len(request.COOKIES) !=10:
        response.set_cookie(course_id,course_name)
        return response
    else:
        messages.error(request,"CAN'T ENROLL ")
        return redirect("enroll_course")


def view_enroll_courses(request):

    return render(request,"view_enroll_courses.html",{"env_data":request.COOKIES})


def cancel_enroll_class(request):
    courseid=request.GET.get("cid")
    response=redirect('view_enroll_courses')
    response.delete_cookie(courseid)
    return response


    return None