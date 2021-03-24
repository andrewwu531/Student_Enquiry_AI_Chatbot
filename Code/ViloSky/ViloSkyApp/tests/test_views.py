from django.test import TestCase
from django.test import Client
from django.urls import reverse
from ViloSkyApp import models

TEST_USER_PROFILE_PASSWORD = "MySecurePassword"
# Create your tests here.


def create_test_user_profile():
    u = models.CustomUser.objects.get_or_create(email="a@a.com")[0]
    u.set_password(TEST_USER_PROFILE_PASSWORD)
    u.save()
    user = models.UserProfile.objects.get_or_create(user=u, company="aa")[0]
    user.save()
    return user

def create_test_qualification():
    ql = models.Qualification.objects.get_or_create(user=create_test_user_profile(),
                                                    level='ajbsncoqenfounsdfnw', subjects='jknqnefnojdnaxcnwenfi')[0]
    ql.save()
    return ql

class Profile_page_testing(TestCase):

    def test_qualification_displayed(self):
        client = Client()
        ql = create_test_qualification()
        user_profile = create_test_user_profile()
        client.login(username=user_profile.user.email,
                     password=TEST_USER_PROFILE_PASSWORD) 
        response = client.get(reverse('mydetails'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, ql.level)
        self.assertContains(response, ql.subjects) 

    #test qualification can be deleted
    def test_delete_qualification(self):
        client = Client()
        ql = create_test_qualification()
        user_profile = ql.user
        client.login(username=user_profile.user.email,
                     password=TEST_USER_PROFILE_PASSWORD)
        response = client.post(reverse('mydetails'), {'delete_list' : '1', 'delete_qualifications' : ''})
        self.assertIsNone(response.context)

    # test new qualification added successfully
    def test_add_qual(self):
        client = Client()
        user_profile = create_test_user_profile()
        client.login(username=user_profile.user.email,
                     password=TEST_USER_PROFILE_PASSWORD) 
        client.post(reverse('mydetails'), {'level' : 'QWERTYUI', 'subjects' : 'Law', 'addquals' : ''})
        ql_added = models.Qualification.objects.get(user = user_profile)
        self.assertEqual(ql_added.user, user_profile)
        self.assertEqual(ql_added.level, 'QWERTYUI')
        self.assertEqual(ql_added.subjects, 'Law')

    #test invalid qualification form posted
    def test_add_qual_failed(self):
        client = Client()
        user_profile = create_test_user_profile()
        client.login(username=user_profile.user.email,
                     password=TEST_USER_PROFILE_PASSWORD) 
        response = client.post(reverse('mydetails'), {'level' : 'ajbsncoqenfounsdfnw', 'subjects' : '', 'addquals' : ''})
        qls_length = len(models.Qualification.objects.all())
        self.assertEqual(qls_length, 0)


    def test_edit_profile(self):
        client = Client()
        user_profile = create_test_user_profile()
        client.login(username=user_profile.user.email,
                     password=TEST_USER_PROFILE_PASSWORD) 
        response = client.post(reverse('mydetails'), {'date_of_birth_month': ['10'], 'date_of_birth_day': ['5'], 
                                                        'date_of_birth_year': ['1980'], 'company': ['haha'], 
                                                        'employment_status': [''], 'employment_sector': [''],
                                                        'time_worked_in_industry': ['']})
        profile = models.UserProfile.objects.get(company="haha")
        self.assertEqual(profile, user_profile)

    
