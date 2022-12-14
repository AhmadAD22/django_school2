from email.utils import parseaddr
from re import sub
from urllib import response
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from data import models as datamodel, serializers
from rest_framework.viewsets import ViewSet, ModelViewSet,GenericViewSet
from rest_framework import mixins
from data.models import Rate, Student, Subject,Teacher,Teach,Learn
from .serializers import RateSerializer,AddRateSerializer
import datetime as DT
from .average import avg


class Rating (GenericViewSet):
# Show All Subject for teacher
    queryset=Teach.objects.all()
    def SubjectsTeacher(self,request,pk):
        teachers=[{
                   'teacher_id':teacher.teacher.id,
                   'id':teacher.subject.id,
                   'subjects':teacher.subject.sub_name,
                   'class':teacher.subject.class_num,
                   }
                  for teacher in Teach.objects.filter(teacher=pk)]
        return Response(teachers)

#Show all students studying the subject by its number
    def liststudent(self,request,pk,pk1,mydate):
        #get All stutents id have rates in this day
        rates=Rate.objects.filter(subject=pk1,date=mydate)
        student_id_has_rate=[
                   rate.student.id 
                  for rate in rates]
        students=[
                   {
                   'sutdent_id':subject.student.id,
                    'sutdent_name':{'first':subject.student.first_name,
                                   'mid':subject.student.mid_name,
                                   'last':subject.student.last_name,
                                   },
                   }
                  for subject in Learn.objects.filter(subject=pk1).exclude(student__in=student_id_has_rate)
                  ]
        return Response(students)

        

#Get rate by student_id
    def getratebyid(self,request,pk):
        rates=Rate.objects.filter(student=pk)
        serializer=RateSerializer(rates,many=True)
        return Response(serializer.data)


class AddRate (GenericViewSet,mixins.CreateModelMixin):
    queryset =Rate.objects.all()
    serializer_class= AddRateSerializer
    def addrate(self,request,pk,pk1,pk2):
         teacher1=Teacher.objects.filter(pk=pk).first()
         subject1=Subject.objects.filter(pk=pk1).first()
         student1=Student.objects.filter(pk=pk2).first()

         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save(presence=True,teacher=teacher1,student=student1,subject=subject1)
         return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetRate (GenericViewSet):
     queryset=Rate.objects.all()

     def getsubjects(self,request,pk):
           subjects=[{
                   'subject_id':student.subject.id,
                    'subject_name':student.subject.sub_name,
                   }
                  for student in Learn.objects.filter(student=pk)]
           return Response(subjects)

     def getrate(self,request,pk,pk1):
        rates=Rate.objects.filter(student=pk,subject=pk1)
        serializer=RateSerializer(rates,many=True)
        return Response(serializer.data)
     def getrate2(self,request,pk,pk1,mydate):

        rates=Rate.objects.filter(student=pk,subject=pk1,date=mydate)
        serializer=RateSerializer(rates,many=True)
        return Response(serializer.data)


     def getweeklyrate(self,request,pk,pk1,mydate):

        week_ago = mydate - DT.timedelta(days=7)
        avg_rates=avg(week_ago,mydate,pk,pk1)
        return Response(avg_rates)

     def getmonthlyrate(self,request,pk,pk1,mydate):

        week_ago = mydate - DT.timedelta(days=7)
        avg_rates=avg(week_ago,mydate)
        return Response(avg_rates)