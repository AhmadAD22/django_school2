import imp
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from data.models import Declirations
from .serializers import PostsSerializer

# Create your views here.
class ListPostsMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Declirations.objects.all()
    serializer_class=PostsSerializer
    def get (self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

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