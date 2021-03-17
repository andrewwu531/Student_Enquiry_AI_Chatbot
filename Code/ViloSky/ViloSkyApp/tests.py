from django.test import TestCase, Client
from django.urls import reverse
from ViloSkyApp import models

TEST_USER_PROFILE_PASSWORD = "MySecurePassword"
# Create your tests here.


def create_test_user_profile():
    u = models.CustomUser.objects.get_or_create(email="a@a.com")[0]
    u.set_password(TEST_USER_PROFILE_PASSWORD)
    u.save()
    user = models.UserProfile.objects.get_or_create(user=u)[0]
    user.save()
    return user


class ActionPlanTests(TestCase):
    def test_no_listed_plans_on_plain_user(self):
        client = Client()
        user_profile = create_test_user_profile()
        client.login(username=user_profile.user.email,
                     password=TEST_USER_PROFILE_PASSWORD)
        response = client.get(reverse('actions'))
        self.assertContains(response, "No action plans found")
