import imp
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from data.models import Declirations,Teacher
from .serializers import PostsSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

# Create your views here.
class ListPostsMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Declirations.objects.order_by('-date')
    serializer_class=PostsSerializer
    def get (self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class CustomCreate(GenericViewSet):
     queryset=Declirations.objects.all()
     serializer_class=PostsSerializer
     def create(self, request):

        new_post =Declirations.objects.create(
                                       title=self.request.data.get("title"),
                                       body_text=self.request.data.get("body_text"),
                                       date=self.request.data.get("date"),
                                       teacher_publish_it=Teacher.objects.filter(pk=self.request.data.get("teacher_publish_it")).first()
                                       )
        new_post.save()
        serializer= PostsSerializer(new_post)

        return Response(serializer.data)

class DetaledPostMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

    queryset=Declirations.objects.all()
    serializer_class=PostsSerializer

    def get (self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put (self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete (self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)