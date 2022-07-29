from django.contrib.auth.models import User
from data.models import Teacher
from rest_framework import serializers
from  data.models import Teacher

class CraeteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ['id', 'username','password','first_name','last_name','email','is_superuser',]
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups','first_name','last_name',]


