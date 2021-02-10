from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from plotly.offline import plot
import plotly.graph_objs as go
from random import randint
from random import uniform
from ViloSkyApp.models import AdminInput, CustomUser, UserProfile, Qualification
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from django.contrib.auth.decorators import login_required
#import ViloSkyApp.models
from ViloSkyApp.forms import UserForm, UserProfileForm, QualificationForm

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

@login_required
def baseuser(request):
   return render(request, 'baseuser.html', {})

@login_required(login_url='login')
def mydetails(request):
    p_form = UserProfileForm(instance = request.user.user_profile)
    q_form = QualificationForm(request.POST)

    if request.method == 'POST':
        if 'addquals' in request.POST: 
            #q_form = QualificationForm(request.POST, instance = request.user.user_profile)
            if q_form.is_valid():
                quals = q_form.save(commit=False)
                quals.user = request.user.user_profile
                quals.save()
                return redirect(reverse('mydetails'))
            else:
                q_form = QualificationForm(instance = request.user.user_profile)
        else:
            p_form = UserProfileForm(request.POST, instance = request.user.user_profile)
            if p_form.is_valid():
                profile = p_form.save()
                profile.save()
                return redirect(reverse('mydetails'))
            else:
                p_form = UserProfileForm(instance = request.user.user_profile)
           

    qualifications = Qualification.objects.filter(user=request.user.user_profile)
    context_dict = {'p_form':p_form, 'q_form':q_form, 'qualifications': qualifications}
    return render(request, 'myDetails.html', context= context_dict) 


@login_required(login_url='login')
def myactions(request):
    return render(request, 'myactions.html', {}) 

@login_required(login_url='login')
def report(request):
    return render(request, 'report.html', {}) 

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
