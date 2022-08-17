
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
from data.models import Student,Teacher,Teach,Subject
from rest_framework.viewsets import ViewSet, ModelViewSet,GenericViewSet
from .serializers import CraeteUserSerializer, UserSerializer



class CreateUser(mixins.CreateModelMixin,GenericViewSet):

    queryset =User.objects.all()
    serializer_class=CraeteUserSerializer
    def create(self, serializer):
        if (self.request.data.get("is_superuser")):
            is_admin=True
        else:
            is_admin=False
        test_user=User.objects.filter(username=self.request.data.get("username"))
        if (test_user):
            return Response(0)
        else:
            new_user = User.objects.create(username=self.request.data.get("username"),
                                       first_name=self.request.data.get("first_name"),
                                       last_name=self.request.data.get("last_name"),
                                       email=self.request.data.get("email"),
                                        is_superuser=is_admin,
                                       )
            new_user.set_password(self.request.data.get("password"))
            new_user.save()

            new_teacer=Teacher.objects.create(teacher_user=new_user)
            new_teacer.certification=self.request.data.get("b")
            a=self.request.data.get("a")
            for i in a:
                new_teacer.teaching.add(i)
            new_teacer.save()

            return Response(new_user.pk)


class DetaledUserMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

        queryset=User.objects.all()
        serializer_class=UserSerializer

        def get (self,request,*args,**kwargs):
             return self.retrieve(request,*args,**kwargs)
        def put (self,request,*args,**kwargs):
             return self.update(request,*args,**kwargs)
        def delete (self,request,*args,**kwargs):
             return self.destroy(request,*args,**kwargs)


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):

        # Return a list of all users.
        usernames = [{"username":user.username,"id":user.id,"first_name":user.first_name,"last_name":user.last_name} for user in User.objects.all()]
        return Response(usernames)




class GetPermission(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request, format=None):
         if request.user.is_superuser:
            return Response(1)

         else:
            return Response(2)

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
            'username': user.username
        })
