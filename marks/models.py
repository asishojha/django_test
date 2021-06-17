from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_marks

SUBJECT_CODE_DICT = {
    '2':'BENGALI',
    '3':'ENGLISH',
    '4':'GUJRATI',
    '5':'HINDI',
    '9':'MODERN TIBETAN',
    '10':'NEPALI',
    '11':'ODIA',
    '12':'GURUMUKHI(PUNJABI)',
    '13':'SANTALI',
    '15':'TELEGU',
    '16':'TAMIL',
    '17':'URDU',
    '21':'ENGLISH',
    '22':'BENGALI',
    '23':'NEPALI'
}

class Student(models.Model):
    school = models.ForeignKey(User,on_delete=models.CASCADE)
    ctg = models.CharField(max_length=2)
    rollno = models.CharField(max_length=11, verbose_name='Roll-Number')
    regno = models.CharField(max_length=11, verbose_name='Registration Number')
    name = models.CharField(max_length=40)
    fname = models.CharField(max_length=40, verbose_name='First Name')
    dob = models.CharField(max_length=30, verbose_name='Date of Birth')
    subj = models.CharField(max_length=40, verbose_name='Subject Combination')
    sub1 = models.CharField(max_length=2)
    sub2 = models.CharField(max_length=2)
    fl = models.CharField(max_length=3 , null=True, blank=True, validators=[validate_marks])
    sl = models.CharField(max_length=3, null=True, blank=True, validators=[validate_marks])
    math = models.CharField(max_length=3, null=True, blank=True, validators=[validate_marks], verbose_name='Mathematics')
    psc = models.CharField(max_length=3, null=True, blank=True, validators=[validate_marks], verbose_name='Physical Science')
    lsc = models.CharField(max_length=3, null=True, blank=True, validators=[validate_marks], verbose_name='Life Science')
    hist = models.CharField(max_length=3, null=True, blank=True, validators=[validate_marks], verbose_name='History')
    geog = models.CharField(max_length=3, null=True, blank=True, validators=[validate_marks], verbose_name='Geography')
    complete = models.BooleanField(default=False)
    
    def __str__(self):
    		return f'{self.school.username} - {self.rollno}'

    def get_absolute_url(self):
        return reverse('marks:student' , kwargs={
            'rollno' : self.rollno
        })

    def get_fl_name(self):
        return SUBJECT_CODE_DICT[self.sub1]

    def get_sl_name(self):
        return SUBJECT_CODE_DICT[self.sub2]
        
    class Meta:
        permissions = [
			("can_update", "Can update the data of students"),
			("can_change_password", "Can change the password of school user"),
		]

class SchoolProfile(models.Model):
	school = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=70)
	phone = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.school.username