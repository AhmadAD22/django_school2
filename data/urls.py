from data.views import StudentViewset,TeachertViewset,\
    RateViewset,SubjectViewset,\
    DetaledStudentMixins,DetaledTeacherMixins,\
    DetaledSubjectMixins,StudentExists
from django.urls import path
urlpatterns = [

    #Student urls
    path('api/studentlogin', StudentExists.as_view({'post':'post'})),
    path('api/student1', StudentViewset.as_view({'get':'list'})),
    path('api/student', StudentViewset.as_view({'get':'listforrating'})),
    path('api/student/<int:class_number>', StudentViewset.as_view({'get':'listbyclass'})),
    path('studentmixin/<int:pk>',DetaledStudentMixins.as_view(),name='RUD'),
    path('api/student/add', StudentViewset.as_view({'post':'create'})),
    #subjects urls
    path('api/subject',SubjectViewset.as_view({'get':'list'})),
    path('api/subject/add', SubjectViewset.as_view({'post':'create'})),
    path('subjectmixin/<int:pk>',DetaledSubjectMixins.as_view(),name='RUD'),
   #tracher urls
    path('api/teacher', TeachertViewset.as_view({'get':'list'})),
    path('api/teacher1', TeachertViewset.as_view({'get':'list1'})),
    path('api/teacher/add', TeachertViewset.as_view({'post':'create'})),
    path('teachermixin/<int:pk>',DetaledTeacherMixins.as_view(),name='RUD'),

    path('api/rate', RateViewset.as_view({'get':'list'})),
    path('api/rate/add', RateViewset.as_view({'post':'create'})),

]