import imp
from django.urls import path
from .views import ListPostsMixins,DetaledPostMixins,CustomCreate


urlpatterns = [
    path('',ListPostsMixins.as_view(),name='mp'),
    path('postud/<int:pk>',DetaledPostMixins.as_view(),name='mdp'),
    path('createpost',CustomCreate.as_view({'post':'create'}))


]