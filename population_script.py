import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ViloSky.settings')

import django
django.setup()

from ViloSkyApp.models import User, UserProfile, Qualifications
from django.contrib.auth import get_user_model

User = get_user_model()

def populate():

    users = [
    {
        'first_name': 'Catherine',
        'last_name': 'Peirs',
        'email': 'cathpeirs@gmail.com',
        'password': 'zXyz+S3_1qQ'
    },
    {
        'first_name': 'Muhammad',
        'last_name': 'Abbar',
        'email': 'muhammadA123@gmail.com',
        'password': '_ak_LF4Fghc'
    },
    {
        'first_name': 'Stevie',
        'last_name': 'Ovens',
        'email': 'ovensS99@yahoo.co.uk',
        'password': 'bosLeDs3_*'
    },
    {
        'first_name': 'Pietro',
        'last_name': 'Marinelli',
        'email': 'marinelli76@hotmail.com',
        'password': 'zXyzS31qQ'
    },
    {
        'first_name': 'Suzie',
        'last_name': 'Mulligan',
        'email': 'suzieMul23@gmail.com',
        'password': 'zXyzS31qQ'
    }
    ]

    #initialise users
    for user in users:
        u = User.objects.get_or_create(email = user['email'], first_name = user['first_name'], last_name = user['last_name'])
        u.set_password(user['password'])
        u.save()

    profiles = [
        {
            'user_id': 'cathpeirs@gmail.com',
            'd.o.b.': datetime.date(1980, 10, 5),
            'user_type': 'standard',
            'company': 'Tesco Bank',
            'sector': 'Financial Services',
            'status': 'employed',
            'time_in_sector': '10 years'
        },
        {
            'user_id': 'muhammadA123@gmail.com',
            'd.o.b.': datetime.date(1989, 6, 11),
            'user_type': 'standard',
            'company': 'n/a',
            'sector': 'Hospitality',
            'status': 'unemployed',
            'time_in_sector': '5 years'  
        },
        {
            'user_id': 'ovensS99@yahoo.co.uk',
            'd.o.b.': datetime.date(1976, 7, 21),
            'user_type': 'hr',
            'company': 'JP Morgan',
            'sector': 'Investment Banking',
            'status': 'employed',
            'time_in_sector': '20 years'
        },
        {
           'user_id': 'marinelli76@hotmail.com',
            'd.o.b.': datetime.date(1992, 12, 6),
            'user_type': 'standard',
            'company': 'Barrhead Travel',
            'sector': 'Travel',
            'status': 'full time',
            'time_in_sector': '6 months' 
        },
        {
           'user_id': 'suzieMul23@gmail.com',
            'd.o.b.': datetime.date(1995, 11, 2),
            'user_type': 'admin',
            'company': 'ViloSky',
            'sector': 'Consulting',
            'status': 'employed',
            'time_in_sector': '4 years' 
        }
    ]

    #initialise user profiles
    for profile in profiles:
        p = UserProfile.pobjects.get_or_create(
            user_id = profile['user_id'],
            dob = profile['d.o.b'],
            user_type = profile['user_type'],
            company = profile['company'],
            sector = profile['sector'],
            status = profile['status'],
            time_in_sector = profile['time_in_sector']
        )
        p.save()