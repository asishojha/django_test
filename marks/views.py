from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import update_session_auth_hash
from .forms import StudentForm , UsersLoginForm , SchoolProfileForm, PasswordResetForm
from .decorators import has_update_permission, has_password_change_permission
from .tokens import account_activation_token
from .models import Student , SchoolProfile
import csv

def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		try:
			profile = request.user.schoolprofile
			return redirect('marks:students')
		except:
			return redirect("marks:school_profile")
	return render(request, "accounts/form.html", {
		"form" : form,
		"title" : "Login",
	})

def logout_view(request):
	logout(request)
	return redirect("/")

@login_required
def school_profile(request):
	try:
		profile = request.user.schoolprofile
		return redirect('marks:change_password')
	except:
		pass
	user = request.user
	form = SchoolProfileForm()
	if request.method == 'POST':
		form = SchoolProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.school = user
			profile.save()
			user.email = profile.email
			user.save()
			return redirect('marks:change_password')
	context = {
		'form': form
	}
	return render(request, 'school-profile.html', context)
@login_required
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid) 
		print(user)
	except:
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		if request.user == user:
			permission = Permission.objects.get(codename='can_change_password')
			request.user.user_permissions.add(permission)
			return redirect('marks:reset_password')
	return HttpResponse('Activation Link Invalid')

@login_required
@has_password_change_permission
def reset_password(request):
	form = PasswordResetForm(request.user)
	# for field in form.fields:
	# 	form.fields[field].widget.attrs.update({'class': 'form-control'})
	update_permission = Permission.objects.get(codename='can_update')
	password_change_permission = Permission.objects.get(codename='can_change_password')
	if request.method == 'POST':
		form = PasswordResetForm(request.user, request.POST)
		if form.is_valid():
			password = form.save()
			update_session_auth_hash(request, password)
			if not request.user.has_perm('data.can_update'):
				request.user.user_permissions.add(update_permission)
			request.user.user_permissions.remove(password_change_permission)
			return redirect('marks:students')
	context = {
		'form': form
	}
	return render(request, 'accounts/reset-password.html', context)


@login_required
def change_password(request):
	try:
		profile = request.user.schoolprofile
		pass
	except SchoolProfile.DoesNotExist:
		return redirect('marks:school_profile')
	current_site = get_current_site(request)
	mail_subject = "Activate your account"
	message = render_to_string('accounts/account_activation_email.html', {
		'user': request.user,
		'domain': current_site.domain,
		'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
		'token': account_activation_token.make_token(request.user),
	})
	send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [request.user.email])
	context = {
		'user': request.user
	}
	return render(request, 'accounts/change-password.html', context)

def home(request):
	return render(request, 'home.html')

@login_required
@has_update_permission
def students(request):
	students = Student.objects.filter(school=request.user).order_by('rollno')
	paginator = Paginator(students,15)
	page = request.GET.get('page',1)
	
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	try:
		first_student = students.filter(complete=False)[0]
	except:
		first_student = None
	context = {
		'students': students,
		'first_student': first_student,
		'userx' : request.user,
		'regm' : Student.objects.filter(school=request.user , ctg='1N').count(),
		'regf' : Student.objects.filter(school=request.user , ctg='2N').count(),
		'tot' : Student.objects.filter(school=request.user).count(),
		'left' : Student.objects.filter(school=request.user, complete=False).count(),
		'done' : Student.objects.filter(school=request.user, complete=True).count(),
		'users' : users
		
		#'usery' : students.username
	}
	return render(request, 'student_list.html', context)

@login_required
@has_update_permission
def student(request, rollno):
	last_elements_list = ['6', '5', '4', '3', '2', '1']
	students = Student.objects.filter(school=request.user).order_by('rollno')
	student = Student.objects.get(rollno=rollno, school=request.user)
	form = StudentForm(instance=student)

	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.complete = True
			obj.save()
			pass

			try:
				next_student = students.filter(rollno__gt=rollno, complete=False)[0]
				messages.success(request, f'Congratulations! Data for student {obj.rollno} have been updated.')
				return redirect(next_student.get_absolute_url())
			except IndexError:
				messages.success(request, 'Congratulations! Data for all the students have been updated.')
				return redirect('marks:students')

	context = {
		'student': student,
		'students': students,
		'form': form,
		'last_elements_list': 'last_elements_list'
	}
	return render(request, 'student.html', context)

@login_required
def instructions(request):
	return render(request, 'instructions.html')