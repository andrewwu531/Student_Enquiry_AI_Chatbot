import datetime
from django.test import TestCase
from django.utils import timezone
from ViloSkyApp.forms import UserProfileForm

class UserProfileFormTest(TestCase):
    def test_date_of_birth_field_label(self):
        form = UserProfileForm()
        self.assertTrue(form.fields['date_of_birth'].label == None or form.fields['date_of_birth'].label == 'date_of_birth')

    