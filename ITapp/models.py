from django.db import models

class ScheduleclassModel(models.Model):
    course_id=models.AutoField(default=None,primary_key=True)
    course_name=models.CharField(max_length=50,unique=True)
    faculty=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    fee=models.FloatField()
    duration=models.IntegerField()

class Student_register_Model(models.Model):
    name=models.CharField(max_length=50)
    contact_no=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
