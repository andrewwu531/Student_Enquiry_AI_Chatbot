from django import forms
from ViloSkyApp.models import UserProfile, Qualification

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
       
        fields = [
                  'is_vilosky_admin',
                  'is_hr_representative',
                  'date_of_birth',
                  'company',
                  'employment_sector',
                  'employment_status',
                  'time_worked_in_industry'
                  ]
    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit  = False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['user', 'level', 'subjects']