from django.conf.urls import url
from django.urls import path
from .views import home , logout_view , login_view, students, change_password, school_profile, activate, reset_password, instructions
from .preview import StudentFormPreview
from .forms import StudentForm

app_name = 'marks'

urlpatterns=[
    path('',home,name='home'),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('students/', students, name='students'),
    path('student/<slug:rollno>/', StudentFormPreview(StudentForm), name='student'),
    path('update-school-profile/', school_profile, name='school_profile'),
	path('change-password/', change_password, name='change_password'),
	path('reset-password/', reset_password, name='reset_password'),
    path('instructions/', instructions, name='instructions'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]