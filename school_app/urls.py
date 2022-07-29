from django.urls import path,include
from school_app.views import ListUsers,CustomAuthToken,CreateUser

urlpatterns = [
    path('api/users/',ListUsers.as_view()),
    path('api/auth1/',ListUsers.as_view()),
    path('api/signup/',CreateUser.as_view({'post':'create'})),
     path('api/auth/', CustomAuthToken.as_view()),
    
]