from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime
import pytz
from ..forms import *


class test_register_view(TestCase):
    @classmethod
    def setUp(self):
        User = get_user_model()
        User.objects.create(email="apple@apple.com", first_name="App", last_name="Lee").set_password(
            'testPassword123')
        
    
    def test_register_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_register_registers_a_user(self):
        User = get_user_model()
        user = User.objects.get(id=1)
        user_details = {"email":"apple@apple.com", "password":"applepie"}
        response = self.client.post(reverse('register'), data=user_details)
        self.assertTrue(User.objects.filter(email= 'apple@apple.com').exists())
