
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from plotly.offline import plot
import plotly.graph_objs as go
from random import randint
from random import uniform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from django.contrib.auth.decorators import login_required
import ViloSkyApp.models
from .forms import UserForm, InputForm
from .models import AdminInput, Keyword, Paragraph, Report, CreateReport, UserProfile, PartialInput, Link, Action
from difflib import SequenceMatcher
from datetime import datetime
from django.core.serializers import serialize, deserialize
# Create your views here.
def index(request):
    return render(request, 'index.html', {}) 

def login(request):
    context_dict = {}
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username = email, password = password)
            if user:
                ulogin(request, user)
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, "Email or password is incorrect")
                return redirect(reverse('login'))
        else:
            return render(request, 'login.html', context_dict)
    else:
        return redirect(reverse('dashboard'))
    return render(request, 'login.html', {}) 

def register(request):
    if not request.user.is_authenticated:
        registered = False
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                if request.POST.get('tos') != "on":
                    user.delete()
                    messages.error(request, "You must accept the TOS and Privacy Policy in order to register.")
                elif request.POST.get('password') != request.POST.get('confirm_password'):
                    user.delete()
                    messages.error(request, "The passwords provided do not match.")
                else:
                    registered = True
        else:
            user_form = UserForm()
        context_dict = {
            'user_form' : user_form,
            'registered' : registered,
        }
        return render(request, 'register.html', context_dict)
    else:
        return redirect(reverse('dashboard'))

@login_required(login_url='login')
def user_logout(request):
    ulogout(request)
    return redirect(reverse('index'))

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html', {}) 

@login_required(login_url='login')    
def mydetails(request):
    return render(request, 'mydetails.html', {}) 

@login_required(login_url='login')
def myactions(request):
    return render(request, 'myactions.html', {}) 


def report(request):
    # Get the dictionary of inputs. Gathered in InputForm, saved to django session.
    inputs = request.session.get('saved')
    # Get a list of paragraphs based on the inputs
    paras = get_paragraphs(inputs)
    link_list = Link.objects.all()
    actions_list = Action.objects.all()
    links_dict = {}

    #get the associated links and actions for each paragraph
    for paragraph in paras:
        temp = []
        t = []
        big_l = []
        for link in link_list:
            if paragraph == link.paragraph:
                temp.append(link)
        for action in actions_list:
            if paragraph == action.paragraph:
                t.append(action)
        if temp:
            big_l.append(temp)
        if t:
            big_l.append(t)
        #list of the lists for links and actions added to dictionary
        links_dict[paragraph] = big_l
    #If a user is logged in then create and save a report instance linked to their profile
    if request.user.is_authenticated:
        current_user_profile = UserProfile.objects.filter(user=request.user).first()
        # Create a report instance and add paragraphs to it
        rep = Report(user=current_user_profile, datetime_created=datetime.now())
        rep.save()
        for p in paras:
            rep.paragraphs.add(p)
    # if a user is not logged in
    else:
        #serialize the paragraphs and save them to the session
        request.session["temp_saved"] = serialize('json', paras)

    context = {'data':links_dict}
    return render(request, 'report.html', context)

@login_required(login_url='login')
def roles(request):
    return render(request, 'roles.html', {}) 

@login_required(login_url='login')
def input(request):
    return render(request, 'input.html', {}) 

@login_required(login_url='login')
def output(request):
    return render(request, 'output.html', {}) 

@login_required(login_url='login')
def editquestion(request):
    return render(request, 'editquestion.html', {}) 

@login_required(login_url='login')
def outputdetails(request):
    return render(request, 'outputdetails.html', {}) 

@login_required(login_url='login')
def data(request):
    visitors = []
    registered_users = []
    inputs = []
    outputs = []
    days = []
    for i in range(31):
        days.append(i)
        cur_visitors = randint(0,12000)
        visitors.append(cur_visitors)
        registered_users.append(int(cur_visitors*uniform(0,0.4)))
        inputs.append(randint(100,2900))
        outputs.append(randint(200,8000))
    vis_fig = go.Figure(data=[go.Scatter(x=days,y=visitors, name="visitors"),
                        go.Scatter(x=days,y=registered_users, name="registered users")]
    )
    vis_div = plot(vis_fig, output_type='div')
    inp_fig = go.Figure(data=go.Scatter(x=days,y=inputs, name="inputs"))
    inp_div = plot(inp_fig, output_type='div')
    out_fig = go.Figure(data=go.Scatter(x=days,y=outputs, name="outputs"))
    out_div = plot(out_fig, output_type='div')
    content_dict ={"vis_div":vis_div,"inp_div":inp_div,"out_div":out_div}
    return render(request, 'data.html', content_dict)

def inputform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and fill it with the request data
        inputForm = InputForm(request.POST)

        if inputForm.is_valid():
            #data from the form is stored in a dictionary, 'cd'
            cd = inputForm.cleaned_data
            request.session['saved'] = cd
            return redirect('/report/')

    # else if we arrive here from a GET method, i.e. via inputting a url.
    else:
        # Create a new instance of the form
        inputForm = InputForm()

        # Check if can populate the database from partial_inputs. i.e. if the user left without completing the form
        if request.user.is_authenticated:
            user = UserProfile.objects.get(user=request.user)
            partials = PartialInput.objects.filter(created_by=user)
            if partials:
                # Dictionary to store partials, to be passed in to instantiated inputForm
                partials_dict = {}
                for p in partials:
                    if p.admin_input.input_type == "DROPDOWN":
                        partials_dict[p.admin_input.label] = (p.value, p.value)
                    elif p.admin_input.input_type == "RADIOBUTTONS":
                        partials_dict[p.admin_input.label] = p.value.strip("[]").replace("\'", "").split(", ")
                        print(p.value)
                    else:
                        partials_dict[p.admin_input.label] = p.value
                inputForm = InputForm(initial=partials_dict)
    context = {'inputForm': inputForm,}
    return render(request, 'input_form.html',context)


def similarity(a,b):
    return SequenceMatcher(None, a,b).ratio()


def get_paragraphs(inputs_dictionary):
    # Get all keywords, questions and list of answers
    keywords = Keyword.objects.all()
    question_list = AdminInput.objects.all()
    answers = [value for value in inputs_dictionary.values()]

    # create dictionary of paragraph score(how relevant paragraphs are to user input)
    paragraphs_list = []
    scores_dict = {}
    counter = 0

    for question in question_list:
        if question.input_type == 'CHECKBOX':
            if answers[counter] == 'True':
                 counter+=1
        elif question.input_type == 'DROPDOWN':
            for keyword in keywords:
                if keyword == answers[counter]:
                    paragraphs_list.append(keyword.paragraph)
            counter+=1
        elif question.input_type == 'RADIOBUTTONS':
            for keyword in keywords:
                if keyword.key in answers[counter]:
                    paragraphs_list.append(keyword.paragraph)
            counter+=1
        else:
            for keyword in keywords:
                score = similarity(answers[counter], keyword.key)
                para = keyword.paragraph
                if para not in scores_dict.keys():
                    scores_dict[para] = score
                else:
                    scores_dict[para] += score
            counter+=1

    num_paras = 5

    for k in range(num_paras):
        highest_score = max(scores_dict, key=scores_dict.get)
        paragraphs_list.append(highest_score)
        del scores_dict[highest_score]
    return paragraphs_list
