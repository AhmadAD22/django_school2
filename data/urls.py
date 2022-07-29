from data.views import StudentViewset,TeachertViewset,RateViewset,SubjectViewset
from django.urls import path
urlpatterns = [

    path('api/student1', StudentViewset.as_view({'get':'list'})),
     path('api/subject',SubjectViewset.as_view({'get':'list'})),
     path('api/subject/add', SubjectViewset.as_view({'post':'create'})),
    path('api/student/add', StudentViewset.as_view({'post':'create'})),
    path('api/teacher', TeachertViewset.as_view({'get':'list'})),
    path('api/teacher1', TeachertViewset.as_view({'get':'list1'})),
    path('api/teacher/add', TeachertViewset.as_view({'post':'create'})),
    path('api/rate', RateViewset.as_view({'get':'list'})),
    path('api/rate/add', RateViewset.as_view({'post':'create'})),
]