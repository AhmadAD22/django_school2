
from urllib import response
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions,generics
from django.contrib.auth.models import User
from data.models import Student,Teacher
from rest_framework.viewsets import ViewSet, ModelViewSet,GenericViewSet
from .serializers import CraeteUserSerializer



class CreateUser(mixins.CreateModelMixin,GenericViewSet):
    
    queryset =User.objects.all()
    serializer_class=CraeteUserSerializer
    def create(self, serializer):
        if (self.request.data.get("is_superuser")):
            is_admin=True
        else:
            is_admin=False
        new_user = User.objects.create(username=self.request.data.get("username"),
                                       first_name=self.request.data.get("first_name"),
                                       last_name=self.request.data.get("last_name"),
                                       email=self.request.data.get("email"),
                                        is_superuser=is_admin,
                                       )
        new_user.set_password(self.request.data.get("password"))
        new_teacer=Teacher.objects.create()
        new_teacer.teacher_user=new_user
        new_teacer.certification=self.request.data.get("certification")
        new_teacer.save()
        new_user.save()
        return Response(new_user.pk)
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        if request.user.is_superuser:
        #     usernames = [user.username for user in User.objects.all()]
            return Response('1')
    
        else:
            # students=[student.last_name for student in Student.objects.all()]
            return Response('2')
            
        
class GetPermission(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request, format=None):
         if request.user.is_superuser:
            return Response('1')
    
         else:
            return Response('2')
    
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        