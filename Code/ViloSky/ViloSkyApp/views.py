from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from plotly.offline import plot
import plotly.graph_objs as go
from random import randint
from random import uniform
# Create your views here.
def index(request):
    return render(request, 'index.html', {}) 

def login(request):
    return render(request, 'login.html', {}) 

def register(request):
    return render(request, 'register.html', {}) 

def dashboard(request):
    return render(request, 'dashboard.html', {}) 
    
def mydetails(request):
    return render(request, 'mydetails.html', {}) 

def myactions(request):
    return render(request, 'myactions.html', {}) 

def report(request):
    return render(request, 'report.html', {}) 

def roles(request):
    return render(request, 'roles.html', {}) 

def input(request):
    return render(request, 'input.html', {}) 

def output(request):
    return render(request, 'output.html', {}) 

def editquestion(request):
    return render(request, 'editquestion.html', {}) 

def outputdetails(request):
    return render(request, 'outputdetails.html', {}) 

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