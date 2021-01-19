import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ViloSky.settings')

import django
django.setup()

from Code.ViloSky.ViloSkyApp.models import CustomUser, UserProfile, Qualification, Keyword, Link, Paragraph, Report, Action, AdminInput, AdminInputTypes, DropdownAdminInput, CheckboxAdminInput, TextAdminInput, TextareaAdminInput
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
            'links': [],
            'actions':[]
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
            ],
            'actions':[]
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
            ],
            'actions':[]
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
            ],
            'actions': []
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
            'links':[],
            'actions':[]
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
            'links':[],
            'actions':[]
        },
        {
            'admin': 'Suzie Mulligan',
            'text': 'We would like to offer you a free coaching session or put you in touch with one of our associate coaches/mentors so please send us a note if you would like to discuss that further - info@vilosky.com.' ,
            'keywords':[],
            'links': [],
            'actions':[]
        },

        #the following paragraphs have actions and form an action plan
        {
            'admin':'Suzie Mulligan',
            'text': 'Next few weeks:',
            'keywords':[
                {'key':'regaining confidence', 'score':4},
                {'key': 'Risk Management', 'score': 8},
                {'key': 'Finance', 'score':8},
            ],
            'links':[
                {'url':'https://www.udemy.com/topic/financial-risk-manager-frm/'}
            ],
            'actions':[
                {'title':'Decide what you want from your next role.', 'iscompleted': True},
                {'title': 'List your amazing skills and experience in the finance and risk management sector.', 'iscompleted':True},
                {'title': 'Start working on some Udemy finance courses to refresh your memory and gain confidence.', 'iscompleted':True},
            ],
        },
        {
            'admin': 'Suzie Mulligan',
            'text': '1+ months:',
            'keywords':[
                {'key':'regaining confidence', 'score':4},
                {'key': 'Risk Management', 'score': 8},
                {'key': 'Finance', 'score':8},
            ],
            'links':[
                {'url':'https://www.indeed.co.uk/Finance-Risk-jobs'},
                {'url':'https://www.facebook.com/Accounting-and-Finance-Webinar-Series-199716536749210/'}
            ],
            'actions':[
                {'title':'Complete the Udemy courses you started.', 'iscompleted':False},
                {'title':'Attend a webinar on Risk Management, or some networking events.', 'iscompleted':False},
                {'title': 'Start compiling a list of employers and vacances, look at companies such as RBS.', 'iscompleted': False},
                {'title': 'Update your CV - refer to Helen for CV advice', 'iscompleted': False},
                {'title': 'Start your search', 'iscompleted':False}
            ]
        },
        {
            'admin':'Suzie Mulligan',
            'text':'6 months:',
            'keywords':[],
            'links':[
                {'url':'https://jobs.theguardian.com/careers/job-hunting-advice/'},
                {'url':'https://www.careercast.com/job-hunting-advice'}
            ],
            'actions':[
                {'title':'If the ideal role has not yet appeared, give yourself a few week’s break. It’s hard work, full of ups and downs, but the right role will turn up. The following might help you at this point:', 'iscompleted':False}
            ]
        },
        {
            'admin':'Suzie Mulligan',
            'text':'7 months:',
            'keywords':[],
            'links':[],
            'actions':[
                {'title':'Back to it!', 'iscompleted':False}
            ]
        }
    ]

    #create data for admin inputs, if a user is an admin we associate the input with that admin
    admin_input = [
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Name',
            'input_type':AdminInputTypes.TEXT,
            'is_required':True,
            'maxlength':50,
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Gender (optional)',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':False,
            #what?
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Sexual Orientation (optional)',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':False,
            #what?
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Ethnicity (optional)',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':False,
            #what?
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Physical/Mental Abiltiy',
            'input_type':AdminInputTypes.TEXT,
            'is_required':False,
            #what?
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'What best describes current work situation (select one) ',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what?
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'What best describes current work barriers (select all that apply):',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what? 
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Time since last paid work:',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what?    
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Industry interested in (select all that apply):',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what?    
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Area of interest:',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what?    
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Do you have relevant formal qualifications in the area you are interested in:',
            'input_type':AdminInputTypes.CHECKBOX,
            'is_required':True,
            'default_value': True
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'How many year’s experience do you have in the area you are interested in:',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what?    
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Hours per week you want to work:',
            'input_type':AdminInputTypes.TEXT,
            'is_required':True,
            'maxlength':50,
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'What would you like to achieve from your next role? (select all that apply)', 
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            #what?
        },
    ]

    #create data for user profiles
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
            'paragraphs': [],
            'inputs':[],
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
            'paragraphs': [],
            'inputs':[],
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
            'paragraphs': [],
            'inputs':[],
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
            'paragraphs': [],
            'inputs':[],
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
            'paragraphs': paragraphs,
            'inputs': admin_input,
        }
    ]

    #Here user profiles are creates as well as their qualifciations
    #If the user is an admin then create paragraphs with theyr respetive links
    #keywords & actions

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

        for qualification in profile['qualifications']:
            q = Qualification.objects.get_or_create(user = profile['user'], level = qualification['level'], subject = qualification['subject'])[0]
            q.save()

        #if the user is an admin, create paragraphs with foreign key as this user
        if profile['is_vilo_sky_admin'] == True:
            for paragraph in paragraphs:

                admin = UserProfile.objects.get(profile['user'])
                pg = Paragraph.objects.get_or_create(created_by = admin, static_text = paragraph['text'])[0]
                pg.save()

                #pg_fk will be used as foreign key for following models
                pg_fk = Paragraph.objects.get(static_text = paragraph['text'])

                #each paragraph has a series of key words
                for keyword in paragraph['keywords']:
                    #pg = Paragraph.objects.get(static_text = paragraph['text'])
                    kw = Keyword.objects.get_or_create(paragraph = pg_fk, key = keyword['key'], score = keyword['score'])[0]
                    kw.save()
        
                #each paragraph has a series of links
                for link in paragraph['links']:
                    l = Link.objects.get_or_create(paragraph = pg_fk, url = link['url'])[0]
                    l.save()

                for action in paragraph['actions']:
                    a = Action.objects.get_or_create(paragraph = pg_fk, title = action['title'], completed = action['completed'])[0]
                    a.save()
                
                for inputs in admin_input:
                    admin = UserProfile.objects.get(profile['created_by'])
                    inp_type = inputs['input_type']
                    curr_input = AdminInput.objects.get(label = inputs['label'])

                    inp = AdminInput.objects.get_or_create(created_by = admin, label = inputs['label'], input_type = inputs['input_type'], is_required = inputs['is_required'])[0]
                    inp.save()

                    #depending on the input type of the input, create new object which as a one to one relationship with parent input
                    if inp_type == AdminInputTypes.TEXT:
                        user_input = TextAdminInput.objects.get_or_create(admin_input = curr_input, max_length = inputs['maxlength'])[0]
                    elif inp_type == AdminInputTypes.TEXTAREA:
                        user_input = TextareaAdminInput.objects.get_or_create(admin_input = curr_input, max_length = inputs['maxlength'])[0]
                    elif inp_type == AdminInputTypes.CHECKBOX:
                        user_input = CheckboxAdminInput.objects.get_or_create(admin_input = curr_input, default_value = False)[0]
                    elif inp_type == AdminInputTypes.DROPDOWN:
                        user_input = DropdownAdminInput.objects.get_or_create(admin_input = curr_input, max_length = inputs['maxlength'])[0]    
        
                    user_input.save()


    reports = [
        {'user': 'greid@gmail.com'}
        ]

    for report in reports:
        r = Report.objects.get_or_create(paragraph = report['paragraph'], user = 'user')[0]
        r.save()

if __name__ == '__main__':
    print('Starting population script...')
    populate()

    