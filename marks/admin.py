from django.contrib import admin
from django.contrib.auth import models
from marks.models import Student , SchoolProfile

class StudentAdmin(admin.ModelAdmin):
    list_display = ['school', 'ctg','rollno','regno','name','fname','dob','sub1','sub2','sub2']


admin.site.register(Student,StudentAdmin)
admin.site.register(SchoolProfile)