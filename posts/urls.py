import imp
from django.urls import path
from .views import ListPostsMixins,DetaledPostMixins


urlpatterns = [
    path('mixinpath',ListPostsMixins.as_view(),name='mp'),
    path('postmixin/<int:pk>',DetaledPostMixins.as_view(),name='mdp')
    
]