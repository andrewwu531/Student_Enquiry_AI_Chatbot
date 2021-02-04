from django import forms
from django.contrib.auth.models import User
from ViloSkyApp.models import UserProfile
class UserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control txtbox'}))
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control txtbox'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')