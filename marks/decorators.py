  
from django.shortcuts import redirect

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
			return redirect('marks:change_password')
	return wrap