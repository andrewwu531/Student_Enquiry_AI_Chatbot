from django import forms
from django.contrib.auth import get_user_model
from ViloSkyApp.models import UserProfile
class UserForm(forms.ModelForm):
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control txtbox'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))

    class Meta:
        model = get_user_model()
        fields = ( 'email', 'password', 'confirm_password')
