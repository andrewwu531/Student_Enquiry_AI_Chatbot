import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ViloSky.settings')

import django
django.setup()

from Code.ViloSky.ViloSkyApp.models import CustomUser, UserProfile, Qualification, Keyword, Link, Paragraph, Report, Action, AdminInput, AdminInputTypes, DropdownAdminInput, CheckboxAdminInput, TextAdminInput, TextareaAdminInput, Session, PartialInput, UserAction
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
            'users':['greid@gmail.com',],
            'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for 3-5 years now it is understandable that your confidence would be low, but you have all the skills and experience you need to re-establish your career.' ,
            'keywords': [
                {'key': '3-5 Years', 'score': 5},
                {'key': 'Confidence', 'score': 7},
            ],
            'links': [],
            'actions':[]
        },
        {
            'users':['greid@gmail.com',],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a Risk Management role in Banking & Finance, we think the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Risk Manegement', 'score': 10},
                {'key': 'Banking&Finance', 'score': 7},
            ],
            'links': [ 
                {'url': 'https://www.wibf.org.uk'},
                {'url': 'https://womenreturners.com '},
            ],
            'actions':[]
        },
        {
            'users':['greid@gmail.com',],
            'admin': 'Suzie Mulligan',
            'text': 'The following template might also help plan your childcare and carer responsibilities when you are back at work: ',
            'keywords': [
                {'key': 'Childcare', 'score': 10},
                {'key': 'Carer Responsibilites', 'score': 8},
            ],
            'links':[
                {'url': 'Time planner.pdf/xls'},
            ],
            'actions':[]
        },
        {
            'users':['greid@gmail.com',],
            'admin': 'Suzie Mulligan',
            'text': 'As you are looking for flexibility and a shorter working week (20hrs), we suggest the following job search sites: ',
            'keywords': [
                {'key': 'Flexibility', 'score': 10},
                {'key': 'Work/Life Balance', 'score': 7},
                {'key': 'Low Stress', 'score': 5},
                {'key': 'Ease', 'score': 7},
                {'key': '20', 'score': 10}
            ],
            'links':[
                {'url': 'https://timewise.co.uk/'},
                {'url': 'https://www.2to3days.com/'}
            ],
            'actions': []
        },
        {
            'users':['greid@gmail.com',],
            'admin': 'Suzie Mulligan',
            'text': 'The following organisations are also well known for supporting flexible working and women returners so it is well worth checking their individual career pages too: ',
            'keywords':[
                {'key': 'flexibility', 'score' : 10},

                #triggered if someone has been out of work for any amount of time
                #score increases with time length
                {'key': '1-6 Months', 'score': 4},
                {'key': '7-12 Months', 'score': 5},
                {'key': '1-2 Years', 'score': 6},
                {'key': '3-5 Years', 'score':7},
                {'key': '5-10 Years', 'score': 8},
                {'key': '10+ Years', 'score': 9},
            ],
            'links':[],
            'actions':[]
        },
        {
            'users':['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'To support ongoing career progression and to help with challenges such as learning new skills, regaining confidence and adapting to workplace cultures, we are strong advocates of creating a support network.',
            'keywords':[
                {'key': 'Learn New Skills', 'score': 8},
                {'key': 'Develop Confidence', 'score': 8},
                {'key': 'Re-establish Career', 'score': 10},
                {'key': 'Confidence', 'score': 9},
                {'key': 'Workplace Culture', 'score': 7}
            ],
            'links':[],
            'actions':[]
        },
        {
            'users':['greid@gmail.com',],
            'admin': 'Suzie Mulligan',
            'text': 'We would like to offer you a free coaching session or put you in touch with one of our associate coaches/mentors so please send us a note if you would like to discuss that further - info@vilosky.com.' ,
            'keywords':[],
            'links': [],
            'actions':[]
        },

        #the following paragraphs have actions and form an action plan
        {
            'users':['greid@gmail.com',],
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
                {'title':'Decide what you want from your next role.'},
                {'title': 'List your amazing skills and experience in the finance and risk management sector.'},
                {'title': 'Start working on some Udemy finance courses to refresh your memory and gain confidence.'},
            ],
        },
        {
            'users':['greid@gmail.com',],
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
                {'title':'Complete the Udemy courses you started.'},
                {'title':'Attend a webinar on Risk Management, or some networking events.'},
                {'title': 'Start compiling a list of employers and vacances, look at companies such as RBS.'},
                {'title': 'Update your CV - refer to Helen for CV advice'},
                {'title': 'Start your search'}
            ]
        },
        {
            'users':['greid@gmail.com',],
            'admin':'Suzie Mulligan',
            'text':'6 months:',
            'keywords':[],
            'links':[
                {'url':'https://jobs.theguardian.com/careers/job-hunting-advice/'},
                {'url':'https://www.careercast.com/job-hunting-advice'}
            ],
            'actions':[
                {'title':'If the ideal role has not yet appeared, give yourself a few week’s break. It’s hard work, full of ups and downs, but the right role will turn up. The following might help you at this point:'}
            ]
        },
        {
            'users':['greid@gmail.com',],
            'admin':'Suzie Mulligan',
            'text':'7 months:',
            'keywords':[],
            'links':[],
            'actions':[
                {'title':'Back to it!'}
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
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Gemma Reid'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Gender (optional)',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':False,
            'choices': ['Male', 'Female', 'Non-Binary', 'Transgender Male', 'Other', 'Transgender Female'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Female'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Sexual Orientation (optional)',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':False,
            'choices': ['Heterosexual', 'Homosexual', 'Bisexual', 'Pansexual', 'Asexual', 'Queer'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': ''},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Ethnicity (optional)',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':False,
            'choices': ['White', 'Black', 'Asian', 'Mixed Race', 'South Asian'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'White'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Physical/Mental Abiltiy (optional)',
            'input_type':AdminInputTypes.TEXT,
            'is_required':False,
            'choices': [],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': ''},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'What best describes current work situation (select one) ',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices': ['Employed', 'Self-Employed', 'Unpaid Work (e.g. Volunteering)', 'Retired', 'Career Break'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Career Break'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'What best describes current work barriers (select all that apply):',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices': ['Childcare', 'Carer Responsibilities', 'Technical Skills', 
            'Leadership Skills', 'Flexibility', 'Workplace Culture', 'Confidence'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': ''},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Time since last paid work:',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices': ['0 (Currently Working)', '1-6 Months', '7-12 Months', '1-2 Years', 
            '3-5 Years', '5-10 Years', '10+ Years'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com','value': '10+ Years'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Industry interested in (select all that apply):',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices':['Retail', 'Fashion', 'Media', 'Banking&Finance', 'Construction', 
            'Manuacturing', 'Law', 'Medical', 'Education', 'IT'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Banking&Finance'},
            ]  
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Area of interest:',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices': ['HR', 'Risk Management', 'Accountancy', 'Law', 'Marketing',
            'Coaching', 'IT', 'Nursing', 'Medicine'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Risk Management'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Do you have relevant formal qualifications in the area you are interested in:',
            'input_type':AdminInputTypes.CHECKBOX,
            'is_required':True,
            'default_value': True,
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': True},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'How many year’s experience do you have in the area you are interested in:',
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices': ['0', '1-6 Months', '7-12 Months', '1-2 Years', '3-5 Years', '5-10 Years', '10+ Years'],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': '3-5 Years'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'Hours per week you want to work:',
            'input_type':AdminInputTypes.TEXT,
            'is_required':True,
            'maxlength':50,
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': '20'},
            ]
        },
        {
            'created_by':'suzieMul23@gmail.com',
            'label':'What would you like to achieve from your next role? (select all that apply)', 
            'input_type':AdminInputTypes.DROPDOWN,
            'is_required':True,
            'choices': ['Re-establish career', 'Learn New Skills', 'Give Something Back', 'Confidence',
            'Realise Full Potential', 'Promotion', 'Work/Life Balance','Ease', 'Good Salary',
            'Working From Home', 'Low Stress', 'Flexibility', 'Greater Autonomy', 'More Responsibility', 
            'Less Responsibility'],
            'partial_inputs':[
                {
                'created_by': 'greid@gmail.com', 
                'value': ['Re-establish career', 'Learn New Skills', 'Give Something Back', 'Confidence',
                'Promotion', 'Work/Life Balance','Ease', 'Good Salary','Working From Home', 'Low Stress', 'Flexibility']
                },
            ]
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
            'sessions':[
                {'page':'Home', 'time': datetime.time(0,5,10), 'clicks':20},
                {'page':'Register', 'time':datetime.time(0,3,15) , 'clicks':13},
                {'page':'Input Page', 'time':datetime.time(0,15,0) , 'clicks':40},
                {'page':'Dashboard', 'time': datetime.time(0,25,30), 'clicks':20},
            ]
        },
        {
            'user': 'muhammadA123@gmail.com',
            'date_of_birth': datetime.date(1989, 6, 11),
            'is_vilosky_admin': False,
            'is_hr_rep':False,
            'company': 'Urban Outfitters',
            'employment_sector': 'Retail',
            'emploment_status': 'Unemployed',
            'time_worked_in_industry': '7-12 Months',
            'qualifications': [
                {'level': 'Modern Apprentice', 'subject':'Retail Skills'},
                {'level' : 'HighSchool', 'subject': 'English'},
                {'level' : 'HighSchool', 'subject': 'Drama'},
                {'level' : 'HighSchool', 'subject': 'Musics'}
                ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page':'Home Page', 'time': datetime.time(0,5,10), 'clicks':5},
                {'page':'Login', 'time': datetime.time(0,2,5), 'clicks':10},
                {'page':'Dashboard', 'time': datetime.time(0,20,10), 'clicks':30}
            ]
        },
        {
            'user': 'ovensS99@yahoo.co.uk',
            'date_of_birth': datetime.date(1976, 7, 21),
            'is_viloky_admin':False,
            'is_hr_rep':True,
            'company': 'JP Morgan',
            'employment_sector': 'IT',
            'employment_status': 'Employed',
            'time_worked_in_industry': '5-10 Years',
            'qualifications': [
                {'level': 'UD', 'subject':'Computer Science'},
                {'level' : 'HighSchool', 'subject': 'Mathematics'},
                {'level' : 'HighSchool', 'subject': 'Physics'},
                {'level' : 'HighSchool', 'subject': 'Computer Science'}
                ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page':'Home Page', 'time': datetime.time(0,12,10), 'clicks': 10},
                {'page':'Register', 'time': datetime.time(0,7,10), 'clicks': 15},
                {'page':'My Account', 'time': datetime.time(0,10,10), 'clicks': 30},
                {'page':'Dashboard', 'time': datetime.time(0,30,30), 'clicks':100},
            ],
        },
        {
            'user': 'marinelli76@hotmail.com',
            'date_of_birth': datetime.date(1992, 12, 6),
            'is_vilosky_admin': False,
            'is_hr_rep':False,
            'company': None,
            'employment_sector': 'Construction',
            'employment_status': 'Unemployed',
            'time_worked_in_industry': '0',
            'qualifications': [
                {'level' : 'HighSchool', 'subject': 'Woodwork'},
                {'level' : 'HighSchool', 'subject': 'Physics'},
                {'level' : 'HighSchool', 'subject': 'Spanish'},
                {'level' : 'HighSchool', 'subject': 'Physical Education'}
                ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page':'Login', 'time': datetime.time(0,1,15), 'clicks':7},
                {'page':'Home Page', 'time': datetime.time(0,12,25), 'clicks':17},
                {'page':'Dashboard', 'time': datetime.time(0,15,30), 'clicks':18},
                {'page':'My Account', 'time': datetime.time(0,3,25), 'clicks':7},
            ]
        },
        {
            'user': 'suzieMul23@gmail.com',
            'date_of_birth': datetime.date(1995, 11, 2),
            'is_vilosky_admin' : True,
            'is_hr_rep': False,
            'company': 'ViloSky',
            'employment_sector': 'Consulting',
            'employment_status': 'Employed',
            'time_worked_in_sector': '1-2 Years',
            'qualifications': [
                {'level' : 'MS', 'subject': 'Law'},
                {'level' : 'HighSchool', 'subject': 'English'},
                {'level' : 'HighSchool', 'subject': 'Spanish'},
                {'level' : 'HighSchool', 'subject': 'Biology'}
                ],
            'paragraphs': paragraphs,
            'inputs': admin_input,
            'sessions':[
                {'page':'Login', 'time': datetime.time(0,3,45), 'clicks':10},
                {'page':'Admin Input', 'time': datetime.time(0,45,0), 'clicks':50},
                {'page':'Home Page', 'time': datetime.time(0,1,25), 'clicks':13},
                {'page':'My Account', 'time': datetime.time(0,4,0), 'clicks':23},
            ]
        }
    ]

    #Here user profiles are creates as well as their qualifciations
    #If the user is an admin then create paragraphs with theyr respetive links
    #keywords & actions, as well as admin input

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

        #get the user object we just saved for foregin keys for qualifications and sessions
        user_p = UserProfile.objects.get(profile['user'])

        for qualification in profile['qualifications']:
            qual = Qualification.objects.get_or_create(user = user_p, level = qualification['level'], subject = qualification['subject'])[0]
            qual.save()

        for session in profile['sessions']:
            ses = Session.objects.get_orCreate(user = user_p, page = session['page'], time_spent_on_page = session['time'], clicks_on_page = session['clicks'])
            ses.save()

        #if the user is an admin, create paragraphs with foreign key as this user
        #and create admin inputs.
        is_admin =  profile['is_vilo_sky_admin']
        if is_admin:
            for paragraph in paragraphs:

                admin = UserProfile.objects.get(profile[user_p])
                pgph = Paragraph.objects.get_or_create(created_by = admin, static_text = paragraph['text'])[0]
                pgph.save()

                #pg_fk will be used as foreign key for following models
                pg_fk = Paragraph.objects.get(static_text = paragraph['text'])

                #each paragraph has a series of key words
                for keyword in paragraph['keywords']:
                    #pg = Paragraph.objects.get(static_text = paragraph['text'])
                    keyw = Keyword.objects.get_or_create(paragraph = pg_fk, key = keyword['key'], score = keyword['score'])[0]
                    keyw.save()
        
                #each paragraph has a series of links
                for link in paragraph['links']:
                    lnk = Link.objects.get_or_create(paragraph = pg_fk, url = link['url'])[0]
                    lnk.save()

                for action in paragraph['actions']:
                    act = Action.objects.get_or_create(paragraph = pg_fk, title = action['title'])[0]
                    act.save()
                
            #each input has corresponding partial inputs, each partial
            #input has a corresponding user.
            for inputs in profile['inputs']:
                admin = user_p
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
                    user_input = DropdownAdminInput.objects.get_or_create(admin_input = curr_input, choices = inputs['choices'])[0]
                
                user_input.save()

                #create partial inputs
                #use curr_input as the input that each partial input is for
                #created_by_user is a foreign key which uses the given email in 'created_by' key of dict
                for partial_input in inputs['partial_inputs']:
                    created_by_user = UserProfile.objects.get(user = partial_input['created_by'])
                    partial_inp = PartialInput.objects.get_or_create(created_by = created_by_user, admin_input = curr_input, value = partial_input['value'])[0]
                    partial_inp.save()



    #creating reports

    reports = [
        {
            'user': 'greid@gmail.com',
            'datetime_created': datetime.date(2021, 11, 1),
        },
        ]

    for report in reports:

        #create report object with user and datetime
        rep = Report.objects.get_or_create(user = report['user'], datetime_created = report['datetime_created'])[0]
        rep.save()

        #now we have saved the report, we can add paragraphs to it
        for text in paragraphs:

            #added users to the paragraph dict for ease of populating database
            if 'greid@gmail.com' in text['users']:
                #wherever a paragphs user contains gemmas email, add the paragraoh to her report
                user_paragraph = Paragraph.objects.get(static_text = text['text'])
                rep.paragraphs.add(user_paragraph)

                #each action in this paragaph will then become a user action, linked to this report
                for actions in text['actions']:
                    user_action = UserAction.objects.get_or_create(report = rep, title = actions['title'], is_completed = False)[0]
                    user_action.save()

if __name__ == '__main__':
    print('Starting population script...')
    populate()

    