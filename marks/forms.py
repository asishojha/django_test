from django import forms
from django.contrib.auth import authenticate
from .models import Student , SchoolProfile
from django.contrib.auth.forms import PasswordChangeForm

class PasswordResetForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(PasswordChangeForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	
	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'class': 'form-control',
			"name":"username"})
		self.fields['password'].widget.attrs.update({
			'class': 'form-control',
			"name":"password"})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("Invalid Credentials! Please check username and password again.")
			if not user.is_active:
				raise forms.ValidationError("User is no longer active")
			
		return super(UsersLoginForm, self).clean(*args, **keyargs)

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

# ROLL-NUMBER
# Registration Number
# Father's Name
# Date of Birth
# Subject Combination

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['complete','ctg']

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control mb-3', 'required': ''})
			if self[field].value() is not None:
				self.fields[field].widget.attrs.update({'disabled': ''})
			self.fields['fl'].label = SUBJECT_CODE_DICT[f'{int(self['sub1'].value())}'].title() #'math' => 'fl'
			self.fields['sl'].label = SUBJECT_CODE_DICT[f'{int(self['sub2'].value())}'].title() #'english' => second field
			if len(self[field].errors) > 0:
				self.fields[field].widget.attrs.pop('disabled')
		
class SchoolProfileForm(forms.ModelForm):
	class Meta:
		model = SchoolProfile
		exclude = ['school']     
	def __init__(self, *args, **kwargs):
		super(SchoolProfileForm, self).__init__(*args, **kwargs)
		
		self.fields['name'].label = 'Name of H.M. / T.I.C'      
		self.fields['phone'].label = 'Mobile Number'

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})
	