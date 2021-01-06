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
        'first_name': 'Gemma',
        'last_name': 'Reid',
        'email': 'greid@gmail.com',
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
            'user': 'greid@gmail.com',
            'date_of_birth': datetime.date(1980, 10, 5),
            'is_vilo_sky_admin': False,
            'is_hr_rep':False,
            'company': 'Tesco Bank',
            'employment_sector': 'Banking&Finance',
            'employment_status': 'unemployed/volounteer',
            'time_worked_in_industry': '3-5 years',
            'qualifications': [
                {'level': 'MS', 'subject':'Mathematics & Finance'},
                {'level' : 'HighSchool', 'subject': 'Mathematics'},
                {'level' : 'HighSchool', 'subject': 'Physics'},
                {'level' : 'HighSchool', 'subject': 'Chemistry'}
                ]
        },
        {
            'user': 'muhammadA123@gmail.com',
            'date_of_birth': datetime.date(1989, 6, 11),
            'is_vilosky_admin': False,
            'is_hr_rep':False,
            'company': 'Urban Outfitters',
            'employment_sector': 'Retail',
            'emploment_status': 'unemployed',
            'time_worked_in_industry': '12 months',
            'qualifications': [
                {'level': 'Modern Apprentice', 'subject':'Retail Skills'},
                {'level' : 'HighSchool', 'subject': 'English'},
                {'level' : 'HighSchool', 'subject': 'Drama'},
                {'level' : 'HighSchool', 'subject': 'Musics'}
                ]  
        },
        {
            'user': 'ovensS99@yahoo.co.uk',
            'date_of_birth': datetime.date(1976, 7, 21),
            'is_viloky_admin':False,
            'is_hr_rep':True,
            'company': 'JP Morgan',
            'employment_sector': 'IT',
            'employment_status': 'employed',
            'time_worked_in_industry': '5-10 years',
            'qualifications': [
                {'level': 'UD', 'subject':'Computer Science'},
                {'level' : 'HighSchool', 'subject': 'Mathematics'},
                {'level' : 'HighSchool', 'subject': 'Physics'},
                {'level' : 'HighSchool', 'subject': 'Computer Science'}
                ]
        },
        {
           'user': 'marinelli76@hotmail.com',
            'date_of_birth': datetime.date(1992, 12, 6),
            'is_vilosky_admin': False,
            'is_hr_rep':False,
            'company': None,
            'employment_sector': 'Construction',
            'employment_status': 'unemployed',
            'time_worked_in_industry': '0',
            'qualifications': [
                {'level' : 'HighSchool', 'subject': 'Woodwork'},
                {'level' : 'HighSchool', 'subject': 'Physics'},
                {'level' : 'HighSchool', 'subject': 'Spanish'},
                {'level' : 'HighSchool', 'subject': 'Physical Education'}
                ]
        },
        {
           'user': 'suzieMul23@gmail.com',
            'date_of_birth': datetime.date(1995, 11, 2),
            'is_vilosky_admin' : True,
            'is_hr_rep': False,
            'company': 'ViloSky',
            'employment_sector': 'Consulting',
            'employment_status': 'employed',
            'time_worked_in_sector': '1-2 years',
            'qualifications': [
                {'level' : 'MS', 'subject': 'Law'},
                {'level' : 'HighSchool', 'subject': 'English'},
                {'level' : 'HighSchool', 'subject': 'Spanish'},
                {'level' : 'HighSchool', 'subject': 'Biology'}
                ]
        }
    ]

    #initialise user profiles and qualidications
    for profile in profiles:
        p = UserProfile.objects.get_or_create(
            user = profile['user'],
            date_of_birth = profile['date_of_birth'],
            is_vilo_sky_admin = profile['is_vilosky_admin'],
            is_hr_rep = profile['is_hr_rep'],
            company = profile['company'],
            employment_sector = profile['employment_sector'],
            employment_status = profile['employment_status'],
            time_worked_in_industry = profile['time_worked_in_industry']
        )

        p.save()

        #adding qualifications per profile
        for qualification in profile['qualifications']:
            q = Qualification.objects.get_or_create(
                user = profile['user'],
                level = qualification['level'],
                subject = qualification['subject']
            )
            q.save()

    

    