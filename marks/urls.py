from django.conf.urls import url
from django.urls import path , reverse , include
from marks import views
from .views import home , logout_view , login_view, students , student, change_password, school_profile, activate, reset_password
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .preview import StudentFormPreview
from .forms import StudentForm
# SET THE NAMESPACE!
app_name = 'marks'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',home,name='home'),
    url(r"^login/$", login_view, name = "login"),
    # path('login/', LoginView.as_view(),name='login'),
    url(r'^logout/$', logout_view, name = "logout"),
    path('students/', students, name='students'),
    path('student/<slug:rollno>/', StudentFormPreview(StudentForm), name='student'),
    path('update-school-profile/', school_profile, name='school_profile'),
	path('change-password/', change_password, name='change_password'),
	path('reset-password/', reset_password, name='reset_password'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_DIR)