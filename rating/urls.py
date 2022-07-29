from django.urls import path,include
from .views import Rating,AddRate,GetRate

urlpatterns = [
    #Show all subjects for spicefic teacher
    #when press (reate) in teacher's form we will recive teacher_id
     path('add/<int:pk>',Rating.as_view({'get':'SubjectsTeacher'})),
     path('add/<int:pk>/<int:pk1>',Rating.as_view({'get':'liststudent'})),
     path('add/<int:pk>/<int:pk1>/<int:pk2>',AddRate.as_view({'post':'addrate'})),
    #get rating
     #get student's subjects by id
      path('get/<int:pk>',GetRate.as_view({'get':'getsubjects'})),
     
     #default get
    path('api/listsubjectsteacher/<int:pk>',Rating.as_view({'get':'SubjectsTeacher'})),
    path('api/liststudentssubject/<int:pk>',Rating.as_view({'get':'liststudent'})),
    path('api/getstudentrates/<int:pk>',Rating.as_view({'get':'getratebyid'})),
]