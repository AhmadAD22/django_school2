from ast import Sub
from django.contrib import admin
from data.models import Student,Teacher ,Rate,Teach,Learn,Subject
from data.models import Declirations

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Rate)
admin.site.register(Teach)
admin.site.register(Learn)
admin.site.register(Subject)
admin.site.register(Declirations)