from django.shortcuts import redirect
from django.contrib.auth.models import Permission
from .models import Student, SchoolProfile

def has_update_permission(func):
	def wrap(request, *args, **kwargs):
		if request.user.has_perm('marks.can_update'):
			return func(request, *args, **kwargs)
		else:
			return redirect('marks:school_profile')
	return wrap

def has_password_change_permission(func):
	def wrap(request, *args, **kwargs):
		if request.user.has_perm('marks.can_change_password'):
			return func(request, *args, **kwargs)
		else:
			return redirect('marks:school_profile')
	return wrap

def has_schoolprofile(func):
	def wrap(request, *args, **kwargs):
		try:
			profile = request.user.schoolprofile
			return func(request, *args, **kwargs)
		except SchoolProfile.DoesNotExist:
			return redirect('marks:school_profile')
	return wrap

def no_update_pemission(func):
	def wrap(request, *args, **kwargs):
		if not request.user.has_perm('marks.can_update'):
			return func(request, *args, **kwargs)
		else:
			return redirect('marks:students')
	return wrap