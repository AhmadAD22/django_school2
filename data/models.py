from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from xml.dom.minidom import CharacterData
from django.db import models
from django.contrib.auth.models import User

class Student (models.Model):
     first_name=models.CharField(max_length=50)
     mid_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     login_id=models.CharField(max_length=50,default="a")
     address=models.CharField(max_length=250)
     birth_date=models.DateField()
     phone=models.IntegerField()
     class_num=models.IntegerField()
     
     def __str__(self):
         return self.first_name


class Subject(models.Model):
     sub_name= models.CharField(max_length=50)
     class_num= models.IntegerField()
     learning=models.ManyToManyField(Student,through='Learn')
     
     def __str__(self):
         return self.sub_name
     
     
class Teacher(models.Model):
     teacher_user=models.OneToOneField(User,on_delete=models.CASCADE)
     certification =models.CharField(max_length=30)
     birth_date=models.DateField()
     address=models.CharField(max_length=250)
     phone=models.PositiveIntegerField(default=0,blank=True)
     rate_students=models.ManyToManyField(Student,through='Rate')
     teaching=models.ManyToManyField(Subject,through='Teach')
     def __str__(self):
         return self.teacher_user.first_name
class Declirations(models.Model):
     teacher_publish_it=models.ForeignKey(Teacher,on_delete=models.CASCADE)
     title=models.CharField(max_length=5000)
     body_text=models.TextField()   
     body_img=models.ImageField()
     date=models.DateField()

     
     
      
      
      
class Documintation(models.Model):
     teacher_publish_it=models.ForeignKey(Teacher,on_delete=models.CASCADE)
     title= models.CharField(max_length=50)
     body_text=models.CharField(max_length=255)
     file_body=models.FileField(upload_to='files')
     date= models.DateField()
    
    
# relation between Student and Subject for Marks in the next version 
class Learn (models.Model):
     student=models.ForeignKey(Student, on_delete=models.CASCADE)
     subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
     fainal_mark=models.IntegerField()
     
     
#Rate table for evry day we will take data from it to monthly rate
class Rate (models.Model):
     rate_value=(
          (1,'Bad'),
          (2,'Medieum'),
          (3,'Good'),
          (4,'Very Good'),
          (5,'Excellent'),       
     )
  
     teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
     student=models.ForeignKey(Student,on_delete=models.CASCADE)
     subject=models.ForeignKey(Subject,on_delete=models.CASCADE,default=1)
     #presence
     presence=models.BooleanField()
     date=models.DateField( null=True, blank=True, default='2020-10-10')
     #basic rate
     attention=models.IntegerField(choices=rate_value,blank=True)
     behavior=models.IntegerField(choices=rate_value,blank=True)
     interaction=models.IntegerField(choices=rate_value,blank=True)
     #skills
     communiction_skills=models.IntegerField(choices=rate_value,blank=True)
     leadership_skills=models.IntegerField(choices=rate_value,blank=True)
     team_skills=models.IntegerField(choices=rate_value,blank=True)
     #thinking
     logical_thinking=models.IntegerField(choices=rate_value,blank=True)
     critical_thinking=models.IntegerField(choices=rate_value,blank=True)
     creative_thinking=models.IntegerField(choices=rate_value,blank=True)
     proplem_solving=models.IntegerField(choices=rate_value,blank=True)
     #Nots to teacher
     nots=models.TextField()
     
     
class Teach(models.Model):
     teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
     subject=models.ForeignKey(Subject, on_delete=models.CASCADE)