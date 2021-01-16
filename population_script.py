import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ViloSky.settings')

import django
django.setup()

from Code.ViloSkyApp.models.py import CustomUser, UserProfile, Qualifications, Link, Paragraph, Report, Action
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
        u = User.objects.get_or_create(email = user['email'], first_name = user['first_name'], last_name = user['last_name'])[0]
        u.set_password(user['password'])
        u.save()

    """ Declaring paragraphs prior to users as paragraphs is a member of the users dictionaries"""

    paragraphs = [
        {
           'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for 3-5 years now it is understandable that your confidence would be low, but you have all the skills and experience you need to re-establish your career.' ,
            'keywords': [
                {'key': '3-5 years', 'score': 5},
                {'key': 'confidence', 'score': 7},
            ],
            'links': []
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a Risk Management role in Banking & Finance, we think the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Risk Manegement', 'score': 10},
                {'key': 'Banking & Financy', 'score': 7},
            ],
            'links': [ 
                {'url': 'https://www.wibf.org.uk'},
                {'url': 'https://womenreturners.com '},
            ]
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'The following template might also help plan your childcare and carer responsibilities when you are back at work: ',
            'keywords': [
                {'key': 'childcare', 'score': 10},
                {'key': 'carer responsibilites', 'score': 8},
            ],
            'links':[
                {'url': 'Time planner.pdf/xls'},
            ]
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'As you are looking for flexibility and a shorter working week (20hrs), we suggest the following job search sites: ',
            'keywords': [
                {'key': 'flexibility', 'score': 10},
                {'key': 'work/life banace', 'score': 7},
                {'key': 'low stress', 'score': 5},
                {'key': 'ease', 'score': 7},
                {'key': '20', 'score': 10}
            ],
            'links':[
                {'url': 'https://timewise.co.uk/'},
                {'url': 'https://www.2to3days.com/'}
            ]
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'The following organisations are also well known for supporting flexible working and women returners so it is well worth checking their individual career pages too: ',
            'keywords':[
                {'key': 'flexibility', 'score' : 10},

                #triggered if someone has been out of work for any amount of time
                #score increases with time length
                {'key': '1-6 mnths', 'score': 4},
                {'key': '7-12 mnths', 'score': 5},
                {'key': '1-2 years', 'score': 6},
                {'key': '3-5 years', 'score':7},
                {'key': '5-10 years', 'score': 8},
                {'key': '10+ years', 'score': 9},
            ],
            'links':[]
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'To support ongoing career progression and to help with challenges such as learning new skills, regaining confidence and adapting to workplace cultures, we are strong advocates of creating a support network.',
            'keywords':[
                {'key': 'learn new skills', 'score': 8},
                {'key': 'develop confidence', 'score': 8},
                {'key': 're-establish career', 'score': 10},
                {'key': 'confidence', 'score': 9},
                {'key': 'workplace culture', 'score': 7}
            ],
            'links':[]
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'We would like to offer you a free coaching session or put you in touch with one of our associate coaches/mentors so please send us a note if you would like to discuss that further - info@vilosky.com.' ,
            'keywords':[],
            'links': []
        }
    ]

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
                ],
            'paragraphs': []
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
                ],
            'paragraphs': []
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
                ],
            'paragraphs': []
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
                ],
            'paragraphs': []
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
                ],
            'paragraphs': paragraphs
        }
    ]

    #initialise user profiles and qualifications
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
        )[0]

        p.save()

        #adding qualifications per profile
        for qualification in profile['qualifications']:
            q = Qualification.objects.get_or_create(user = profile['user'], level = qualification['level'], subject = qualification['subject'])[0]
            q.save()

        #if the user is an admin, create paragraphs with foreign key as this user
        if profile['is_vilo_sky_admin'] == True:
            for paragraph in paragraphs:
                admin = UserProfile.objects.get(profile['user'])
                pg = Paragraph.objects.get_or_create(created_by = admin, static_text = paragraph['text'])[0]
                pg.save()

            #each paragraoh has a series of key words
            for keyword in paragraph['keywords']:
                pg = Paragraph.objects.get(static_text = paragraph['text'])
                kw = Keyword.objects.get_or_create(paragraph = pg, key = keyword['key'], score = keyword['score'])[0]
                kw.save()
        
            #each paragraph has a series of links
            for link in paragraph['links']:
                pg = Paragraph.objects.get(static_text = paragraph['text'])
                l = Link.objects.get_or_create(paragraph = pg, url = link['url'])[0]
                l.save()
        
    reports = [
        {'user': 'greid@gmail.com'}
        ]

    for report in reports:
        r = Report.objects.get_or_create(paragraph = report['paragraph'], user = 'user')[0]
        r.save()

if __name__ == '__main__':
    print('Starting population script...')
    populate()

    