from django.contrib import admin
from django.contrib.auth import models
from marks.models import Student , SchoolProfile
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    # Add a few display fields here
    list_display = ['school', 'ctg','rollno','regno','name','fname','dob','sub1','sub2','sub2']


admin.site.register(Student,StudentAdmin)
# Register your models here.

admin.site.register(SchoolProfile)