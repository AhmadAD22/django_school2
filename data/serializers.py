from rest_framework import serializers
from .models import Student,Teacher, Rate,Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Subject
        fields ='__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teacher
        fields ='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = ['id','first_name', 'mid_name', 'last_name','address','phone','birth_date','class_num']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Rate
        fields ='__all__'