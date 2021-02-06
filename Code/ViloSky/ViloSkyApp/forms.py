from django import forms
from ViloSkyApp.models import CustomUser, UserProfile, Qualification

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
                  'is_vilosky_admin',
                  'is_hr_representative',
                  'date_of_birth',
                  'company',
                  'employment_sector',
                  'employment_status',
                  'time_worked_in_industry'
                  ]


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['user', 'level', 'subjects']