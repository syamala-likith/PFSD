from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.utils.translation import gettext,gettext_lazy as _
from .models import Employee
#from .views import insert_emp

class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = "__all__"
        #Set the fields attribute to the special value '__all__' to
        # indicate that all fields in the model should be used.
