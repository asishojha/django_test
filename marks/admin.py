from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import path
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from marks.models import Student, SchoolProfile

class StudentAdmin(admin.ModelAdmin):
    list_display = ['school', 'ctg','rollno','regno','name','fname','dob','sub1','sub2','sub2']

class SchoolProfileAdmin(admin.ModelAdmin):
    
    @method_decorator(staff_member_required)
    def reset_password(self, request, pk):
        profile = SchoolProfile.objects.get(pk=pk)
        user = profile.school
        user.password = make_password('password')
        user.save()

        update_permission = Permission.objects.get(codename='can_update')
        password_change_permission = Permission.objects.get(codename='can_change_password')
        user.user_permissions.remove(update_permission)
        user.user_permissions.add(password_change_permission)

        mail_subject = "Reset your Account's Password"
        message = f"Hi {user.username}, as per your request, your password has been reset.\nPlease login to the site again and reset your password once again.\nTo Login into the website, please use following credentials:\nUsername: {user.username}\nPassword: password"
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])

        messages.success(request, f"Password of the school with index {user.username} has been reset to 'password'.")
        return redirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(pk,)))

    def get_urls(self):
        super_urls = super().get_urls()
        urls = [
            path('<int:pk>/reset-password/', self.admin_site.admin_view(self.reset_password), name='reset_password')
        ]
        return urls + super_urls

admin.site.register(Student,StudentAdmin)
admin.site.register(SchoolProfile, SchoolProfileAdmin)