from django import forms
from ViloSkyApp.models import CustomUser, UserProfile, Qualification
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from ViloSkyApp.models import UserProfile


class UserForm(forms.ModelForm):
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control txtbox'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))

    class Meta:
        model = get_user_model()
        fields = ( 'email', 'password', 'confirm_password')

class UserProfileForm(forms.ModelForm):

    is_vilosky_admin = forms.BooleanField(required = False)
    is_hr_representative = forms.BooleanField(required = False)
    date_of_birth = forms.DateField(widget = forms.DateInput(format=('%m/%d/%Y')))
    company = forms.CharField()
    employment_status = forms.CharField()
    employment_sector = forms.CharField()
    time_worked_in_industry = forms.CharField()

    class Meta:
        model = UserProfile
        fields = (
                  'is_vilosky_admin',
                  'is_hr_representative',
                  'date_of_birth',
                  'company',
                  'employment_sector',
                  'employment_status',
                  'time_worked_in_industry'
        )


class QualificationForm(forms.ModelForm):
    level = forms.CharField(max_length=160, widget=forms.TextInput(attrs={
        'placeholder': 'Qualification Level (e.g.BSc'
    }),
    required = True)
    subject = forms.CharField(max_length=160, widget=forms.TextInput(attrs={
        'placeholder': 'Subject'
    }),
    required = True)

#QualificationFormSet = modelformset_factory(QualificationForm, fields = ('user','level', 'subjects'), extra = 1)



