from django.shortcuts import redirect
from .models import Student

def has_update_permission(func):
	def wrap(request, *args, **kwargs):
		if request.user.has_perm('marks.can_update'): #data => app_name
			return func(request, *args, **kwargs)
		else:
			return redirect('marks:change_password')
	return wrap

def has_password_change_permission(func):
	def wrap(request, *args, **kwargs):
		if request.user.has_perm('marks.can_change_password'):
			return func(request, *args, **kwargs)
		else:
			marks_filled_students_count = Student.objects.filter(school=request.user, complete=True).count()
			if marks_filled_students_count > 0:
				return redirect('marks:students')
			return redirect('marks:change_password')
	return wrap