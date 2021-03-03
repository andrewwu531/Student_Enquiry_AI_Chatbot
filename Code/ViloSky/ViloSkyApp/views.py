''' Views for the ViloSky app'''
from random import uniform, randint
from plotly.offline import plot
import plotly.graph_objs as go
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from django.contrib.auth.decorators import login_required
from django.utils.formats import localize
from ViloSkyApp import models
from ViloSkyApp.forms import UserForm, InputForm
from ViloSkyApp.models import Qualification
from ViloSkyApp.forms import QualificationForm
from difflib import SequenceMatcher
from datetime import datetime
from .forms import UserProfileForm
from django.core.serializers import serialize, deserialize


def index(request):
    return render(request, 'index.html', {})


def login(request):
    context_dict = {}
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
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
                    messages.error(
                        request, "You must accept the TOS and Privacy Policy in order to register.")
                elif request.POST.get('password') != request.POST.get('confirm_password'):
                    user.delete()
                    messages.error(
                        request, "The passwords provided do not match.")
                else:
                    registered = True
        else:
            user_form = UserForm()
        context_dict = {
            'user_form': user_form,
            'registered': registered,
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
    p_form = UserProfileForm(instance=request.user.user_profile)
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
                q_form = QualificationForm(instance=request.user.user_profile)
        elif 'delete_qualifications' in request.POST:
            Qualification.objects.filter(
                pk__in=request.POST.getlist('delete_list')).delete()
            return redirect(reverse('mydetails'))
        else:
            p_form = UserProfileForm(
                request.POST, instance=request.user.user_profile)
            if p_form.is_valid():
                profile = p_form.save()
                profile.save()
                return redirect(reverse('mydetails'))
            else:
                p_form = UserProfileForm(instance=request.user.user_profile)
    qualifications = Qualification.objects.filter(
        user=request.user.user_profile)
    context_dict = {'p_form': p_form, 'q_form': q_form,
                    'qualifications': qualifications}
    return render(request, 'myDetails.html', context=context_dict)


@login_required(login_url='login')
def action(request, action_id):
    # Pass required info and update template
    return render(request, 'action_plan.html', {'action_id': action_id})


@login_required(login_url='login')
def actions(request):
    user = models.UserProfile.objects.filter(user=request.user).first()

    if user is None:
        return render(request, "error.html")

    user_reports = user.reports_assigned.all().order_by('-datetime_created')
    entries = [{"id": report.id, "title": f"Action plan from {localize(report.datetime_created)}"}
               for report in user_reports]
    template_headings = ["#", "Title"]
    model_keys = ["id", "title"]

    return render(request, 'action_plans.html', {
        "headings": template_headings, "model_keys": model_keys,
        "entries": entries, "row_link_to": "/action/"
    })


@login_required(login_url='login')
def report(request, report_id):
    # Pass required info and update template
    return render(request, 'report.html', {'report_id': report_id})


@login_required
def baseuser(request):
    return render(request, 'baseuser.html', {})


@login_required(login_url='login')
def reports(request):
    user = models.UserProfile.objects.filter(user=request.user).first()

    if user is None:
        return render(request, "error.html")

    reports_to_render = list(
        user.reports_assigned.all().values().order_by('-datetime_created'))
    for report in reports_to_render:
        report['datetime_created'] = localize(report['datetime_created'])
    template_headings = ["#", "Date Created"]
    model_keys = ["id", "datetime_created"]

    return render(request, 'reports.html', {
        "headings": template_headings, "model_keys": model_keys,
        "entries": reports_to_render, "row_link_to": "/report/"
    })


@ login_required(login_url='login')
def roles(request):
    return render(request, 'roles.html', {})


@ login_required(login_url='login')
def admin_input(request, admin_input_id):
    # Pass required info and update template
    return render(request, 'admin_input.html', {'admin_input_id': admin_input_id})


@ login_required(login_url='login')
def admin_inputs(request):
    user = models.UserProfile.objects.filter(user=request.user).first()

    if user is None:
        return render(request, "error.html")

    inputs_to_render = list(
        models.AdminInput.objects.all().values('id', 'created_by__user__first_name', 'label', 'input_type', 'is_required'))
    template_headings = ["#", "Created By", "Label", "Type", "Required"]
    model_keys = ["id", "created_by__user__first_name",
                  "label", "input_type", "is_required"]

    return render(request, 'admin_inputs.html', {
        "headings": template_headings, "model_keys": model_keys,
        "entries": inputs_to_render, "row_link_to": "/admin_input/"
    })

    return render(request, 'admin_inputs.html', {})


@ login_required(login_url='login')
def paragraph(request, paragraph_id):
    # Pass required info and update template
    return render(request, 'paragraph.html', {'paragraph_id': paragraph_id})


@ login_required(login_url='login')
def paragraphs(request):
    user = models.UserProfile.objects.filter(user=request.user).first()

    if user is None:
        return render(request, "error.html")

    pars_to_render = list(
        models.Paragraph.objects.all().values('id', 'created_by__user__first_name', 'static_text'))
    template_headings = ["#", "Created By", "Text"]
    model_keys = ["id", "created_by__user__first_name", "static_text"]

    return render(request, 'paragraphs.html', {
        "headings": template_headings, "model_keys": model_keys,
        "entries": pars_to_render, "row_link_to": "/paragraph/"
    })


@ login_required(login_url='login')
def data(request):
    visitors = []
    registered_users = []
    inputs = []
    outputs = []
    days = []
    for i in range(31):
        days.append(i)
        cur_visitors = randint(0, 12000)
        visitors.append(cur_visitors)
        registered_users.append(int(cur_visitors*uniform(0, 0.4)))
        inputs.append(randint(100, 2900))
        outputs.append(randint(200, 8000))
    vis_fig = go.Figure(data=[go.Scatter(x=days, y=visitors, name="visitors"),
                              go.Scatter(x=days, y=registered_users, name="registered users")]
                        )
    vis_div = plot(vis_fig, output_type='div')
    inp_fig = go.Figure(data=go.Scatter(x=days, y=inputs, name="inputs"))
    inp_div = plot(inp_fig, output_type='div')
    out_fig = go.Figure(data=go.Scatter(x=days, y=outputs, name="outputs"))
    out_div = plot(out_fig, output_type='div')
    content_dict = {"vis_div": vis_div, "inp_div": inp_div, "out_div": out_div}
    return render(request, 'data.html', content_dict)


def inputform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and fill it with the request data
        inputForm = InputForm(request.POST)

        if inputForm.is_valid():
            # data from the form is stored in a dictionary, 'cd'
            cd = inputForm.cleaned_data
            request.session['saved'] = cd
            return redirect('/report/')

    # else if we arrive here from a GET method, i.e. via inputting a url.
    else:
        # Create a new instance of the form
        inputForm = InputForm()

        # Check if can populate the database from partial_inputs. i.e. if the user left without completing the form
        if request.user.is_authenticated:
            user = models.UserProfile.objects.get(user=request.user)
            partials = models.PartialInput.objects.filter(created_by=user)
            if partials:
                # Dictionary to store partials, to be passed in to instantiated inputForm
                partials_dict = {}
                for p in partials:
                    if p.admin_input.input_type == "DROPDOWN":
                        partials_dict[p.admin_input.label] = (p.value, p.value)
                    elif p.admin_input.input_type == "RADIOBUTTONS":
                        partials_dict[p.admin_input.label] = p.value.strip(
                            "[]").replace("\'", "").split(", ")
                        print(p.value)
                    else:
                        partials_dict[p.admin_input.label] = p.value
                inputForm = InputForm(initial=partials_dict)
    context = {'inputForm': inputForm, }
    return render(request, 'input_form.html', context)


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def get_paragraphs(inputs_dictionary):
    # Get all keywords, questions and list of answers
    keywords = models.Keyword.objects.all()
    question_list = models.AdminInput.objects.all()
    answers = [value for value in inputs_dictionary.values()]

    # create dictionary of paragraph score(how relevant paragraphs are to user input)
    paragraphs_list = []
    scores_dict = {}
    counter = 0

    for question in question_list:
        if question.input_type == 'CHECKBOX':
            if answers[counter] == 'True':
                counter += 1
        elif question.input_type == 'DROPDOWN':
            for keyword in keywords:
                if keyword == answers[counter]:
                    paragraphs_list.append(keyword.paragraph)
            counter += 1
        elif question.input_type == 'RADIOBUTTONS':
            for keyword in keywords:
                if keyword.key in answers[counter]:
                    paragraphs_list.append(keyword.paragraph)
            counter += 1
        else:
            for keyword in keywords:
                score = similarity(answers[counter], keyword.key)
                para = keyword.paragraph
                if para not in scores_dict.keys():
                    scores_dict[para] = score
                else:
                    scores_dict[para] += score
            counter += 1

    num_paras = 5

    for k in range(num_paras):
        highest_score = max(scores_dict, key=scores_dict.get)
        paragraphs_list.append(highest_score)
        del scores_dict[highest_score]
    return paragraphs_list


def report(request):
    # Get the dictionary of inputs. Gathered in InputForm, saved to django session.
    inputs = request.session.get('saved')
    # Get a list of paragraphs based on the inputs
    paras = get_paragraphs(inputs)
    link_list = models.Link.objects.all()
    actions_list = models.Action.objects.all()
    links_dict = {}

    # get the associated links and actions for each paragraph
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
        # list of the lists for links and actions added to dictionary
        links_dict[paragraph] = big_l
    # If a user is logged in then create and save a report instance linked to their profile
    if request.user.is_authenticated:
        current_user_profile = models.UserProfile.objects.filter(
            user=request.user).first()
        # Create a report instance and add paragraphs to it
        rep = models.Report(user=current_user_profile,
                            datetime_created=datetime.now())
        rep.save()
        for p in paras:
            rep.paragraphs.add(p)
    # if a user is not logged in
    else:
        # serialize the paragraphs and save them to the session
        request.session["temp_saved"] = serialize('json', paras)

    context = {'data': links_dict}
    return render(request, 'report.html', context)
