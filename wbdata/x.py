import csv, sys, os, django
from django.conf import settings

project_dir = "/wbdata/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'wbdata.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()


from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from marks.models import Student
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

#file = f"{settings.BASE_DIR}\\schools.csv"

date_time = datetime.datetime.now()

data = csv.reader(open(f"{settings.BASE_DIR}\\y1.csv"), delimiter=",")
for row in data:
    if row[0] != "Number":
        # Post.id = row[0]
        Post=Student()
        #Post.password = make_password('password')
        # Post.last_login = "2011-05-27 05:51:42.521991"
        #   Post.is_superuser = "0"
        # Post.username = row[0]
        # Post.is_staff = True
        # Post.is_active = True
        # Post.date_joined = date_time
        # Post.first_name=row[1]
        Post.school=User.objects.get(pk = (row[0]))
        Post.ctg=row[2],
        Post.rollno=row[3],
        Post.regno=row[4],
        Post.name=row[5],
        Post.fname=row[6],
        Post.dob=row[7],
        Post.sub1=row[8],
        Post.sub2=row[9],
        Post.sub3=row[10],
        Post.save()
        