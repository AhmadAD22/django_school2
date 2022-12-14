from rest_framework import mixins
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet, ModelViewSet,GenericViewSet
from .models import Student,Teacher,Rate,Subject,Learn
from rest_framework import authentication, generics
from .serializers import StudentSerializer,TeacherSerializer,RateSerializer,StudentExistsSerializer
from .serializers import SubjectSerializer

class SubjectViewset(mixins.CreateModelMixin,GenericViewSet):
   # authentication_classes = [authentication.TokenAuthentication]
    queryset =Subject.objects.all()
    serializer_class= SubjectSerializer
    def list(self,request):
        queryset =Subject.objects.all()
        serializer=SubjectSerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DetaledSubjectMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

        queryset=Subject.objects.all()
        serializer_class=SubjectSerializer

        def get (self,request,*args,**kwargs):
             return self.retrieve(request,*args,**kwargs)
        def put (self,request,*args,**kwargs):
             return self.update(request,*args,**kwargs)
        def delete (self,request,*args,**kwargs):
             return self.destroy(request,*args,**kwargs)

class StudentExists(GenericViewSet):
      queryset =Subject.objects.all()
      serializer_class= StudentExistsSerializer

      def post(self, request, format=None):
          s_id=request.data.get("student_id")
          student=Student.objects.filter(pk=s_id)
          if (student):
               serializer= StudentSerializer(student,many=True)
               return Response(serializer.data)
          else:
                 return Response(0)


#All student information
class StudentViewset(mixins.CreateModelMixin,GenericViewSet):
   # authentication_classes = [authentication.TokenAuthentication]
    queryset =Student.objects.all()
    serializer_class= StudentSerializer

    def list(self,request):
        queryset =Student.objects.all()
        serializer= StudentSerializer(queryset,many=True)
        return Response(serializer.data)

    def listbyclass(self,request,class_number):
        queryset =Student.objects.filter(class_num=class_number)
        serializer= StudentSerializer(queryset,many=True)
        return Response(serializer.data)

    def listforrating(self,request):
        rating=Rate.objects.filter(presence=True)
        studentforrating=[]
        students=Student.objects.all()
        for student in students :
            for rate in rating:
                if (student.id ==rate.student):
                    studentforrating.append(student)

        serializer= StudentSerializer(studentforrating,many=True)
        return Response(serializer.data)

    def create(self, request):


        new_student = Student.objects.create(
                                       first_name=self.request.data.get("first_name"),
                                       mid_name=self.request.data.get("mid_name"),
                                       last_name=self.request.data.get("last_name"),
                                       address=self.request.data.get("address"),
                                       birth_date=self.request.data.get("birth_date"),
                                       phone=self.request.data.get("phone"),
                                       class_num=self.request.data.get("class_num"),
                                       )
        subjects=Subject.objects.filter(class_num=request.data.get("class_num"))

        for  subject in subjects:
             new_student.Subjects.add(subject.id)
        new_student.save()

        serializer= StudentSerializer(new_student)


        return Response(serializer.data,status=status.HTTP_201_CREATED)

class DetaledStudentMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

        queryset=Student.objects.all()
        serializer_class=StudentSerializer

        def get (self,request,*args,**kwargs):
             return self.retrieve(request,*args,**kwargs)
        def put (self,request,*args,**kwargs):
             return self.update(request,*args,**kwargs)
        def delete (self,request,*args,**kwargs):
             return self.destroy(request,*args,**kwargs)



# All TEACHER INFORMATION
class TeachertViewset(mixins.CreateModelMixin,GenericViewSet):

    queryset =Teacher.objects.all()
    serializer_class=TeacherSerializer
    def list(self,request):
        # queryset =Teacher.objects.all()

        teachers=[{
                   'id':teacher.id,
                   'first_name':teacher.teacher_user.first_name,
                   'last_name':teacher.teacher_user.last_name,
                   'certification ':teacher.certification ,
                   }
                  for teacher in Teacher.objects.all()]
        # serializer= TeacherSerializer (teachers,many=True)
        return Response(teachers)
    def list1(self,request):
        queryset =Teacher.objects.all()
        serializer=TeacherSerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DetaledTeacherMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

        queryset=Teacher.objects.all()
        serializer_class=TeacherSerializer

        def get (self,request,*args,**kwargs):
             return self.retrieve(request,*args,**kwargs)
        def put (self,request,*args,**kwargs):
             return self.update(request,*args,**kwargs)
        def delete (self,request,*args,**kwargs):
             return self.destroy(request,*args,**kwargs)

#Rate Information
class RateViewset(mixins.CreateModelMixin,GenericViewSet):
   # authentication_classes = [authentication.TokenAuthentication]
    queryset =Rate.objects.all()
    serializer_class= RateSerializer
    def list(self,request):
        queryset =Rate.objects.all()
        serializer= RateSerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)