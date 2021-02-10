from django import forms
from .models import UserProfile, Paragraph, Report, Link, Keyword, Action
from django.contrib.auth import get_user_model
from ViloSkyApp.models import UserProfile
import datetime
from datetime import date
from ViloSkyApp.models import UserProfile

class UserForm(forms.ModelForm):
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control txtbox'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))

    class Meta:
        model = get_user_model()
        fields = ( 'email', 'password', 'confirm_password')


class ReportForm(forms.ModelForm):
    datetime_created = forms.DateField(initial=datetime.date.today, widget=forms.HiddenInput())
    class Meta:
        model = Report
        fields = [
            'paragraphs', 'user', 'datetime_created'
        ]