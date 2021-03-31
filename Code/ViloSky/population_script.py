import os
import datetime
import json
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ViloSky.settings')

import django
from django.contrib.auth import get_user_model
from django.utils import timezone
django.setup()

from ViloSkyApp.models import CustomUser, UserProfile, Qualification, Keyword, Link, Paragraph, Report, Action, AdminInput, \
    DropdownAdminInput, CheckboxAdminInput, TextAdminInput, TextareaAdminInput, MultiselectAdminInput, Session, PartialInput, UserAction
timezone.now()

from pathway_1 import paragraphs as pathway_1
from pathway_2 import paragraphs as pathway_2

pathways = [pathway_1,pathway_2]

User = get_user_model()


def load_pathway(paragraphs):
    for paragraph in paragraphs:
        admin = UserProfile.objects.get(
            user=CustomUser.objects.get(email=paragraph['created_by']))

        created_paragraph = Paragraph.objects.get_or_create(
            created_by=admin, static_text=paragraph['text'])[0]
        created_paragraph.save()

        create_and_add_keywords_to_paragraph(
            paragraph['keywords'], created_paragraph)
        create_and_add_links_to_paragraph(
            paragraph['links'], created_paragraph)
        create_and_add_actions_to_paragraph(
            paragraph['actions'], created_paragraph)


def create_and_add_keywords_to_paragraph(keywords, paragraph):
    for keyword in keywords:
        created_keyword = Keyword.objects.get_or_create(
            paragraph=paragraph, key=keyword['key'],
            score=keyword['score'])[0]
        created_keyword.save()


def create_and_add_links_to_paragraph(links, paragraph):
    for link in links:
        created_link = Link.objects.get_or_create(
            paragraph=paragraph, url=link['url'])[0]
        created_link.save()


def create_and_add_actions_to_paragraph(actions, paragraph):
    for action in actions:
        created_action = Action.objects.get_or_create(
            paragraph=paragraph, title=action['title'])[0]
        created_action.save()


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

    # initialise users
    for user in users:
        u = User.objects.get_or_create(
            email=user['email'], first_name=user['first_name'], last_name=user['last_name'])[0]
        u.set_password(user['password'])
        u.save()

    """ Declaring paragraphs prior to users as paragraphs is a member of the users dictionaries"""

    paragraphs = [
        # gender related paragraphs
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'The following guide may be some use to you, as a Transgender individual. It also include tips for employers, so you may wish to share this guide with your workplace to help promote an inclusive environment. ',
            'keywords': [
                {'key': 'Transgender', 'score': 10},
            ],
            'links': [
                {'url': 'http://www.lgbthealth.org.uk/wp-content/uploads/2016/07/TWSP-Info-Guide-Final.pdf'}
            ],
            'actions': []
        },


        # paragraphs for time out of work
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for a few months now your confidence may be low, but you have the skills and experience you need to re-establish your career.',
            'keywords': [
                {'key': '1-6 Months since last work', 'score': 5},
            ],
            'links': [
                {'url': 'https://www.gov.uk/government/publications/help-and-support-for-returning-to-work'}
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for a almost a year now, your confidence may be low, but you have the skills and experience you need to re-establish your career. The following website may have some good tips in aiding your return to work. ',
            'keywords': [
                {'key': '1-2 Years since last work', 'score': 5},
            ],
            'links': [
                {'url': 'https://www.gov.uk/government/publications/help-and-support-for-returning-to-work'}
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for 3-5 years now it is understandable that your confidence may be low, but you have the skills and experience you need to re-establish your career. The following website may have some good tips in aiding your return to work',
            'keywords': [
                {'key': '3-5 Years since last work', 'score': 5},
            ],
            'links': [
                {'url': 'https://www.gov.uk/government/publications/help-and-support-for-returning-to-work'}
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for 3-5 years now it is understandable that your confidence may be low, but you have the skills and experience you need to re-establish your career. The following website may have some good tips in aiding your return to work.',
            'keywords': [
                {'key': '5-10 Years since last work', 'score': 5},
            ],
            'links': [
                {'url': 'https://www.gov.uk/government/publications/help-and-support-for-returning-to-work'}
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'Having been out of work for 10+ years now it is understandable that your confidence may be low, but you have the skills and experience you need to re-establish your career. The following website may have some good tips in aiding your return to work',
            'keywords': [
                {'key': '10+ Years since last work', 'score': 5},
            ],
            'links': [
                {'url': 'https://www.gov.uk/government/publications/help-and-support-for-returning-to-work'}
            ],
            'actions': []
        },
        # industry related paragraphs
        # 'Retail', 'Fashion', 'Media', 'Banking&Finance', 'Construction',
        #' Manufacturing', 'Law', 'Medical', 'Education', 'IT'
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in Retail, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Retail', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in Fashion, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Fashion', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in Media, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Media', 'score': 7},
            ],
            'links': [
                {'url': 'https://www.wibf.org.uk'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in banking and finance, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Banking&Finance', 'score': 7},
            ],
            'links': [
                {'url': 'https://www.wibf.org.uk'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in the Construction industry, we think the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Construction', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in the Manufacturing industry, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Manufacturing', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role concerning Law, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Law', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in the medical profession, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Medical', 'score': 7},
            ],
            'links': [
                {'url': 'https://jobs.scot.nhs.uk/'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in the education sector, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Education', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        # paras regarding work barriers
        # 'Childcare', 'Carer Responsibilities', 'Technical Skills',
        # 'Leadership Skills', 'Flexibility', 'Workplace Culture', 'Confidence'
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'The following template might also help plan your childcare responsibilities when you are at work: ',
            'keywords': [
                {'key': 'Childcare', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.employersforchildcare.org/app/uploads/2016/10/Employment-Rights-For-Working-Parents.pdf'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'The following template might also help plan your carer responsibilities when you are at work: ',
            'keywords': [
                {'key': 'Carer Responsibilities', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.skillsforcare.org.uk/Careers-in-care/Job-roles/Roles/Care-worker.aspx'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you feel you are lacking in technical skills, improving them would be very useful. Visit the follwoing website for help in doing this.',
            'keywords': [
                {'key': 'Technical Skills', 'score': 10},
            ],
            'links': [
                {"url":"https://www.indeed.com/career-advice/resumes-cover-letters/technical-skills"},
                {"url":"https://www.udemy.com/course/python-class/"},
            ],
            'actions': [
                {"title":"Try analyze your previous interests to narrow down the field you may be interested in."},
                {"title":"Engage in basic programming courses to establish initial understanding of the matter."},
                {"title":"Make sure this is for you, go on with courses when you feel confident!"},
            ]
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you feel you are lacking in Leadership skills, it may be useful to try and improve these. Try to take on more leadership roles in order to improve, and you may find the follwoing sites of use.',
            'keywords': [
                {'key': 'Leadership Skills', 'score': 10},
            ],
            'links': [],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'If you are struggling with workplace culture it may be worth speaking to your colleagues or HR to try improve the situation. Workplace culture varies greatly between different companies, and even different departments or locations. Seeking a job with a workplace culture you fit in with ay be a good idea, wether that be working at a different store, a different department or a new job entirely.',
            'keywords': [
                {'key': 'Workplace culture', 'score': 10},
            ],
            'links': [
                {'url': 'https://innovationmanagement.se/2017/05/04/struggling-with-company-culture-here-are-3-ways-to-improve-your-work-environment/'},
            ],
            'actions': []
        },
        # parars for area of interest
        # 'HR', 'Risk Management', 'Accountancy', 'Law', 'Marketing',
        # 'Coaching', 'IT', 'Nursing', 'Medicine'
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a HR role, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'HR', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.cipd.co.uk/careers/career-options?gclid=Cj0KCQjwmIuDBhDXARIsAFITC_6uKMpU0ovLi8LhOG1tuJdnR7Z01uSmniXehsX-9z1_YV5sUNFFqKIaArGbEALw_wcB'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a risk managment role, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Risk Management', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.reed.co.uk/jobs/risk-management-jobs'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in an accountancy role, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'HR', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.reed.co.uk/jobs/accountancy-jobs-in-edinburgh'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a marketing job, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Marketing', 'score': 10},
            ],
            'links': [
                {'url': 'https://uk.indeed.com/Marketing-jobs-in-Edinburgh'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a coaching role for your next job, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Coaching', 'score': 10},
            ],
            'links': [
                {'url': 'https://uk.indeed.com/Coach-jobs-in-Edinburgh'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in an IT role, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'IT', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.reed.co.uk/jobs/it-jobs-in-edinburgh'},
                {'url': 'https://www.newhorizons.com/article/7-it-roles-every-modern-company-needs-to-stay-competitive'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role practicing law, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Law', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.prospects.ac.uk/jobs-and-work-experience/job-sectors/law-sector/law-careers'},
            ],
            'actions': []
        },
        {
            'users': ['greid@gmail.com', ],
            'admin': 'Suzie Mulligan',
            'text': 'As you are interested in a role in the nursing profession, the following networks would be very useful for you: ',
            'keywords': [
                {'key': 'Nursing', 'score': 10},
            ],
            'links': [
                {'url': 'https://www.healthcareers.nhs.uk/we-are-the-nhs/nursing-careers'},
            ],
            'actions': []
        }
    ]

    # create data for admin inputs, if a user is an admin we associate the input with that admin
    admin_input = [
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Name',
            'input_type': AdminInput.AdminInputTypes.TEXT,
            'is_required': True,
            'max_length': 50,
            'partial_inputs': [
                {'created_by': 'greid@gmail.com', 'value': 'Gemma Reid'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Gender (optional)',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': False,
            'choices': json.dumps(['Male', 'Female', 'Non-Binary', 'Transgender Male', 'Other', 'Transgender Female']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Female'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Sexual Orientation (optional)',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': False,
            'choices': json.dumps(['Heterosexual', 'Homosexual', 'Bisexual', 'Pansexual', 'Asexual', 'Queer']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': ''},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Ethnicity (optional)',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': False,
            'choices': json.dumps(['White', 'Black', 'Asian', 'Mixed Race', 'South Asian']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'White'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Do you have any physical or mental disabilities (optional)?',
            'input_type': AdminInput.AdminInputTypes.TEXT,
            'is_required': False,
            'choices': [],
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': ''},
            ],
            'max_length': None,
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'What best describes current work situation (select one)',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': True,
            'choices': json.dumps(['Employed', 'Self-Employed', 'Unpaid Work (e.g. Volunteering)', 'Retired', 'Career Break']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Career Break'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'What best describes current work barriers (select all that apply)',
            'input_type': AdminInput.AdminInputTypes.MULTISELECT,
            'is_required': False,
            'choices': json.dumps(['Childcare', 'Carer Responsibilities', 'Technical Skills',
                                   'Leadership Skills', 'Flexibility', 'Workplace Culture', 'Confidence']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': ''},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Time since last paid work:',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': True,
            'choices': json.dumps(['0 (Currently Working)', '1-6 Months since last work', '7-12 Months since last work', '1-2 Years since last work',
                                   '3-5 Years since last work', '5-10 Years since last work', '10+ Years since last work']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com',
                    'value': '10+ Years since last work'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Industry interested in (select all that apply)',
            'input_type': AdminInput.AdminInputTypes.MULTISELECT,
            'is_required': False,
            'choices': json.dumps(['Retail', 'Fashion', 'Media', 'Banking&Finance', 'Construction',
                                   'Manufacturing', 'Law', 'Medical', 'Education', 'IT']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Banking&Finance'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Area of interest',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': True,
            'choices': json.dumps(['HR', 'Risk Management', 'Accountancy', 'Law', 'Marketing',
                                   'Coaching', 'IT', 'Nursing', 'Medicine']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': 'Risk Management'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Do you have relevant formal qualifications in the area you are interested in',
            'input_type': AdminInput.AdminInputTypes.CHECKBOX,
            'is_required': False,
            'default_value': True,
            'partial_inputs': [
                {'created_by': 'greid@gmail.com', 'value': True},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'How many year’s experience do you have in the area you are interested in',
            'input_type': AdminInput.AdminInputTypes.DROPDOWN,
            'is_required': True,
            'choices': json.dumps(['0', '1-6 Months', '7-12 Months', '1-2 Years', '3-5 Years', '5-10 Years', '10+ Years']),
            'partial_inputs':[
                {'created_by': 'greid@gmail.com', 'value': '3-5 Years'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'Hours per week you want to work',
            'input_type': AdminInput.AdminInputTypes.TEXT,
            'is_required': True,
            'max_length': 50,
            'partial_inputs': [
                {'created_by': 'greid@gmail.com', 'value': '20'},
            ]
        },
        {
            'created_by': 'suzieMul23@gmail.com',
            'label': 'What would you like to achieve from your next role? (select all that apply)',
            'input_type': AdminInput.AdminInputTypes.MULTISELECT,
            'is_required': False,
            'choices': json.dumps(['Re-establish career', 'Learn New Skills', 'Give Something Back', 'Confidence',
                                   'Realise Full Potential', 'Promotion', 'Work/Life Balance', 'Ease', 'Good Salary',
                                   'Working From Home', 'Low Stress', 'Flexibility', 'Greater Autonomy', 'More Responsibility',
                                   'Less Responsibility']),
            'partial_inputs':[
                {
                    'created_by': 'greid@gmail.com',
                    'value': ['Re-establish career', 'Learn New Skills', 'Give Something Back', 'Confidence',
                              'Promotion', 'Work/Life Balance', 'Ease', 'Good Salary', 'Working From Home', 'Low Stress', 'Flexibility']
                },
            ]
        },
    ]

    # create data for user profiles
    profiles = [
        {
            'user': 'greid@gmail.com',
            'date_of_birth': datetime.datetime(1980, 10, 5, tzinfo=pytz.UTC),
            'is_vilosky_admin': False,
            'is_hr_representative': False,
            'company': 'Tesco Bank',
            'employment_sector': 'Banking&Finance',
            'employment_status': UserProfile.EmploymentStatusTypes.CAREER_BREAK,
            'time_worked_in_industry': UserProfile.TimeWorkedTypes.THREE_TO_FIVE_YEARS,
            'qualifications': [
                {'level': 'MS', 'subjects': 'Mathematics & Finance'},
                {'level': 'HighSchool', 'subjects': 'Mathematics'},
                {'level': 'HighSchool', 'subjects': 'Physics'},
                {'level': 'HighSchool', 'subjects': 'Chemistry'}
            ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page': 'Home', 'time': datetime.timedelta(
                    minutes=5, seconds=10), 'clicks': 20},
                {'page': 'Register', 'time': datetime.timedelta(
                    minutes=3, seconds=15), 'clicks': 13},
                {'page': 'Input Page', 'time': datetime.timedelta(
                    minutes=15), 'clicks': 40},
                {'page': 'Dashboard', 'time': datetime.timedelta(
                    minutes=25, seconds=30), 'clicks': 20},
            ]
        },
        {
            'user': 'muhammadA123@gmail.com',
            'date_of_birth': datetime.datetime(1989, 6, 11, tzinfo=pytz.UTC),
            'is_vilosky_admin': False,
            'is_hr_representative': False,
            'company': 'Urban Outfitters',
            'employment_sector': 'Retail',
            'employment_status': UserProfile.EmploymentStatusTypes.UNEMPLOYED_OR_VOLUNTEER,
            'time_worked_in_industry': UserProfile.TimeWorkedTypes.SEVEN_TO_TWELVE_MONTHS,
            'qualifications': [
                {'level': 'Modern Apprentice', 'subjects': 'Retail Skills'},
                {'level': 'HighSchool', 'subjects': 'English'},
                {'level': 'HighSchool', 'subjects': 'Drama'},
                {'level': 'HighSchool', 'subjects': 'Musics'}
            ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page': 'Home Page', 'time': datetime.timedelta(
                    minutes=5, seconds=10), 'clicks': 5},
                {'page': 'Login', 'time': datetime.timedelta(
                    minutes=2, seconds=5), 'clicks': 10},
                {'page': 'Dashboard', 'time': datetime.timedelta(
                    minutes=20, seconds=15), 'clicks': 30}
            ]
        },
        {
            'user': 'ovensS99@yahoo.co.uk',
            'date_of_birth': datetime.datetime(1976, 7, 21, tzinfo=pytz.UTC),
            'is_vilosky_admin': False,
            'is_hr_representative': True,
            'company': 'JP Morgan',
            'employment_sector': 'IT',
            'employment_status': UserProfile.EmploymentStatusTypes.EMPLOYED,
            'time_worked_in_industry': UserProfile.TimeWorkedTypes.FIVE_TO_TEN_YEARS,
            'qualifications': [
                {'level': 'UD', 'subjects': 'Computer Science'},
                {'level': 'HighSchool', 'subjects': 'Mathematics'},
                {'level': 'HighSchool', 'subjects': 'Physics'},
                {'level': 'HighSchool', 'subjects': 'Computer Science'}
            ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page': 'Home Page', 'time': datetime.timedelta(
                    minutes=12, seconds=10), 'clicks': 10},
                {'page': 'Register', 'time': datetime.timedelta(
                    minutes=7, seconds=10), 'clicks': 15},
                {'page': 'My Account', 'time': datetime.timedelta(
                    minutes=10, seconds=10), 'clicks': 30},
                {'page': 'Dashboard', 'time': datetime.timedelta(
                    minutes=13, seconds=13), 'clicks': 100},
            ],
        },
        {
            'user': 'marinelli76@hotmail.com',
            'date_of_birth': datetime.datetime(1992, 12, 6, tzinfo=pytz.UTC),
            'is_vilosky_admin': False,
            'is_hr_representative': False,
            'company': "",
            'employment_sector': 'Construction',
            'employment_status': UserProfile.EmploymentStatusTypes.UNEMPLOYED_OR_VOLUNTEER,
            'time_worked_in_industry': UserProfile.TimeWorkedTypes.NO_EXPERIENCE,
            'qualifications': [
                {'level': 'HighSchool', 'subjects': 'Woodwork'},
                {'level': 'HighSchool', 'subjects': 'Physics'},
                {'level': 'HighSchool', 'subjects': 'Spanish'},
                {'level': 'HighSchool', 'subjects': 'Physical Education'}
            ],
            'paragraphs': [],
            'inputs':[],
            'sessions':[
                {'page': 'Login', 'time': datetime.timedelta(
                    minutes=1, seconds=15), 'clicks': 7},
                {'page': 'Home Page', 'time': datetime.timedelta(
                    minutes=12, seconds=25), 'clicks': 17},
                {'page': 'Dashboard', 'time': datetime.timedelta(
                    minutes=15, seconds=30), 'clicks': 18},
                {'page': 'My Account', 'time': datetime.timedelta(
                    minutes=3, seconds=25), 'clicks': 7},
            ]
        },
        {
            'user': 'suzieMul23@gmail.com',
            'date_of_birth': datetime.datetime(1995, 11, 2, tzinfo=pytz.UTC),
            'is_vilosky_admin': True,
            'is_hr_representative': False,
            'company': 'ViloSky',
            'employment_sector': 'Consulting',
            'employment_status': UserProfile.EmploymentStatusTypes.SELFEMPLOYED,
            'time_worked_in_industry': UserProfile.TimeWorkedTypes.ONE_TO_TWO_YEARS,
            'qualifications': [
                {'level': 'MS', 'subjects': 'Law'},
                {'level': 'HighSchool', 'subjects': 'English'},
                {'level': 'HighSchool', 'subjects': 'Spanish'},
                {'level': 'HighSchool', 'subjects': 'Biology'}
            ],
            'paragraphs': paragraphs,
            'inputs': admin_input,
            'sessions': [
                {'page': 'Login', 'time': datetime.timedelta(
                    minutes=3, seconds=45), 'clicks': 10},
                {'page': 'Admin Input', 'time': datetime.timedelta(
                    minutes=45), 'clicks': 50},
                {'page': 'Home Page', 'time': datetime.timedelta(
                    minutes=1, seconds=25), 'clicks': 13},
                {'page': 'My Account', 'time': datetime.timedelta(
                    minutes=4), 'clicks': 23},
            ]
        }
    ]

    # Here user profiles are creates as well as their qualifciations
    # If the user is an admin then create paragraphs with theyr respetive links
    # keywords & actions, as well as admin input

    # initialise user profiles and qualifications
    for profile in profiles:
        p = UserProfile.objects.get_or_create(
            user=User.objects.filter(email=profile['user']).first(),
            date_of_birth=profile['date_of_birth'],
            is_vilosky_admin=profile['is_vilosky_admin'],
            is_hr_representative=profile['is_hr_representative'],
            company=profile['company'],
            employment_sector=profile['employment_sector'],
            employment_status=profile['employment_status'],
            time_worked_in_industry=profile['time_worked_in_industry']
        )[0]

        p.save()

        # get the user object we just saved for foregin keys for qualifications and sessions
        user_p = UserProfile.objects.get(
            user=User.objects.get(email=profile['user']))

        for qualification in profile['qualifications']:
            qual = Qualification.objects.get_or_create(
                user=user_p, level=qualification['level'], subjects=qualification['subjects'])[0]
            qual.save()

        for session in profile['sessions']:
            ses = Session.objects.get_or_create(
                user=user_p, page=session['page'], time_spent_on_page=session['time'], clicks_on_page=session['clicks'])[0]
            ses.save()

        # if the user is an admin, create paragraphs with foreign key as this user
        # and create admin inputs.
        is_admin = profile['is_vilosky_admin']
        if is_admin:
            for paragraph in paragraphs:

                admin = UserProfile.objects.get(
                    user=User.objects.get(email=profile['user']))
                pgph = Paragraph.objects.get_or_create(
                    created_by=admin, static_text=paragraph['text'])[0]
                pgph.save()

                # pg_fk will be used as foreign key for following models
                pg_fk = Paragraph.objects.get(static_text=paragraph['text'])

                # each paragraph has a series of key words
                for keyword in paragraph['keywords']:
                    #pg = Paragraph.objects.get(static_text = paragraph['text'])
                    keyw = Keyword.objects.get_or_create(
                        paragraph=pg_fk, key=keyword['key'], score=keyword['score'])[0]
                    keyw.save()

                # each paragraph has a series of links
                for link in paragraph['links']:
                    lnk = Link.objects.get_or_create(
                        paragraph=pg_fk, url=link['url'])[0]
                    lnk.save()

                for action in paragraph['actions']:
                    act = Action.objects.get_or_create(
                        paragraph=pg_fk, title=action['title'])[0]
                    act.save()

            # each input has corresponding partial inputs, each partial
            # input has a corresponding user.
            for inputs in profile['inputs']:
                admin = user_p
                inp_type = inputs['input_type']

                inp = AdminInput.objects.get_or_create(
                    created_by=admin, label=inputs['label'], input_type=inputs['input_type'], is_required=inputs['is_required'])[0]
                inp.save()

                curr_input = inp

                # depending on the input type of the input, create new object which as a one to one relationship with parent input
                if inp_type == AdminInput.AdminInputTypes.TEXT:
                    user_input = TextAdminInput.objects.get_or_create(
                        admin_input=curr_input,
                        is_required=inputs['is_required'],
                        label=inputs['label'],
                        input_type=inputs['input_type'],
                        created_by=admin, max_length=inputs['max_length'])[0]
                elif inp_type == AdminInput.AdminInputTypes.TEXTAREA:
                    user_input = TextareaAdminInput.objects.get_or_create(
                        admin_input=curr_input,
                        is_required=inputs['is_required'],
                        label=inputs['label'],
                        input_type=inputs['input_type'],
                        created_by=admin, max_length=inputs['max_length'])[0]
                elif inp_type == AdminInput.AdminInputTypes.CHECKBOX:
                    user_input = CheckboxAdminInput.objects.get_or_create(
                        admin_input=curr_input,
                        is_required=inputs['is_required'],
                        label=inputs['label'],
                        input_type=inputs['input_type'],
                        created_by=admin, default_value=False)[0]
                elif inp_type == AdminInput.AdminInputTypes.DROPDOWN:
                    user_input = DropdownAdminInput.objects.get_or_create(
                        admin_input=curr_input,
                        is_required=inputs['is_required'],
                        label=inputs['label'],
                        input_type=inputs['input_type'],
                        created_by=admin, choices=inputs['choices'])[0]
                elif inp_type == AdminInput.AdminInputTypes.MULTISELECT:
                    user_input = MultiselectAdminInput.objects.get_or_create(
                        admin_input=curr_input,
                        is_required=inputs['is_required'],
                        label=inputs['label'],
                        input_type=inputs['input_type'],
                        created_by=admin, choices=inputs['choices'])[0]

                user_input.save()

                # create partial inputs
                # use curr_input as the input that each partial input is for
                # created_by_user is a foreign key which uses the given email in 'created_by' key of dict
                for partial_input in inputs['partial_inputs']:
                    created_by_user = UserProfile.objects.get(
                        user=User.objects.get(email=partial_input['created_by']))
                    partial_inp = PartialInput.objects.get_or_create(
                        created_by=created_by_user, admin_input=curr_input, value=partial_input['value'])[0]
                    partial_inp.save()

    # creating reports

    reports = [
        {
            'user': 'greid@gmail.com',
            'datetime_created': datetime.datetime(2021, 3, 1, tzinfo=pytz.UTC),
        },
    ]

    for report in reports:

        # create report object with user and datetime
        rep = Report.objects.get_or_create(
            user=UserProfile.objects.get(user=User.objects.get(email=report['user'])), datetime_created=report['datetime_created'])[0]
        rep.save()

        # now we have saved the report, we can add paragraphs to it
        for text in paragraphs:

            # added users to the paragraph dict for ease of populating database
            if 'greid@gmail.com' in text['users']:
                # wherever a paragphs user contains gemmas email, add the paragraoh to her report
                user_paragraph = Paragraph.objects.get(
                    static_text=text['text'])
                rep.paragraphs.add(user_paragraph)

                # each action in this paragaph will then become a user action, linked to this report
                for actions in text['actions']:
                    user_action = UserAction.objects.get_or_create(
                        report=rep, title=actions['title'], is_completed=False)[0]
                    user_action.save()


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Populating modular pathways...')
    for i, pathway in enumerate(pathways):
        load_pathway(pathway)
        print(f"Loaded pathway module {i+1}")
