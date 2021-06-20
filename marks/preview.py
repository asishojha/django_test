from django.shortcuts import redirect
from django import forms
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from formtools.preview import FormPreview
from .models import Student
from .decorators import has_update_permission

decorators = [login_required, has_update_permission]

@method_decorator(decorators, name='__call__')
class StudentFormPreview(FormPreview):
	student = None
	next_student = None
	form_template = 'student.html'
	preview_template = 'preview.html'

	def parse_params(self, request, *args, **kwargs):
		self.student = Student.objects.get(school=request.user, rollno=kwargs['rollno'])
		try:
			self.next_student = Student.objects.filter(school=request.user, complete=False).exclude(rollno=kwargs['rollno']).order_by('rollno')[0]
		except IndexError:
			self.next_student = None

	def get_initial(self, request):
		student_dict = model_to_dict(self.student, fields=[field.name for field in self.student._meta.fields])
		return student_dict

	def get_context(self, request, form):
		students = Student.objects.filter(school=request.user).order_by('rollno')
		return {
			'form': form,
			'stage_field': self.unused_name('stage'),
			'state': self.state,
			'students': students,
			'student': self.student,
		}

	def done(self, request, cleaned_data):
		self.student.fl = cleaned_data['fl']
		self.student.sl = cleaned_data['sl']
		self.student.math = cleaned_data['math']
		self.student.psc = cleaned_data['psc']
		self.student.lsc = cleaned_data['lsc']
		self.student.hist = cleaned_data['hist']
		self.student.geog = cleaned_data['geog']
		self.student.complete=True
		self.student.save()
		if self.next_student is not None:
			messages.success(request, f'Congratulations! Data for student {self.student.rollno} has been updated.')
			return redirect(self.next_student.get_absolute_url())
		else:
			messages.success(request, 'Congratulations! Data for all the students have been updated.')
			return redirect('marks:students')

	def __call__(self, request, *args, **kwargs):
		return super(StudentFormPreview, self).__call__(request, *args, **kwargs)