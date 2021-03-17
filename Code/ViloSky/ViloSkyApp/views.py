''' Views for the ViloSky app'''
from random import uniform, randint
from datetime import datetime
from difflib import SequenceMatcher
from plotly.offline import plot
import plotly.graph_objs as go
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.utils.formats import localize
from ViloSkyApp import models
from ViloSkyApp.forms import UserForm, InputForm
from ViloSkyApp.models import Qualification, Paragraph, Link, Action, Keyword
from ViloSkyApp.forms import QualificationForm, ParagraphForm, LinksForm, ActionForm, KeyWordForm
from .forms import UserProfileForm


def index(request):
    return redirect(reverse('login'))


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
def action(request, report_id):
    # Pass required info and update template
    actions_list = models.UserAction.objects.all().filter(report=report_id)

    if request.method == "GET":
        context_dict = {
            'actions': actions_list,
            'action_id': report_id,
        }
        return render(request, 'action_plan.html', context_dict)

    elif request.method == 'POST':
        is_success = False
        try:
            if 'completed' in request.POST:
                completed_actions_ids = request.POST.getlist(
                    'completed')
                completed_actions = actions_list.filter(
                    pk__in=completed_actions_ids)
                incomplete_actions = actions_list.exclude(
                    id__in=completed_actions_ids)
                completed_actions.update(is_completed=True)
                incomplete_actions.update(is_completed=False)
                is_success = True

            context_dict = {
                'actions': actions_list,
                'action_id': report_id,
                'success': is_success,
            }
            return render(request, 'action_plan.html', context_dict)
        except Exception as _:
            context_dict = {
                'actions': actions_list,
                'action_id': report_id,
                'success': False,
            }
            return render(request, 'action_plan.html', context_dict)


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
    created_by = models.UserProfile.objects.filter(user=request.user).first()
    page = 'paragraph/' + paragraph_id + '/'
    # Pass required info and update template
    para = Paragraph.objects.filter(id = paragraph_id)[0]
    links = Link.objects.filter(paragraph = paragraph_id)
    actions = Action.objects.filter(paragraph = paragraph_id)
    keywords = Keyword.objects.filter(paragraph = paragraph_id)

    paragraph = Paragraph.objects.get(id=paragraph_id)

    #all these forms are to edit paragraphs
    p_form = ParagraphForm(request.POST, instance = paragraph)
    link_form = LinksForm(request.POST)
    action_form = ActionForm(request.POST)
    keywords_form = KeyWordForm(request.POST)

    if request.method == 'POST':
        if 'editText' in request.POST:
            if p_form.is_valid():
                p = p_form.save(commit=False)
                p.created_by = created_by
                p.save()
                return redirect(reverse('paragraphs'))
        elif 'editLinks' in request.POST:
            if link_form.is_valid():
                l = link_form.save(commit=False)
                l.paragraph = Paragraph.objects.get(id = paragraph_id)
                l.save()
                return redirect(reverse('paragraphs'))
        elif 'editActions' in request.POST:
            if action_form.is_valid():
                a = action_form.save(commit=False)
                a.paragraph = Paragraph.objects.get(id = paragraph_id)
                a.save()
                return redirect(reverse('paragraphs'))
        elif 'editKeys' in request.POST:
            if keywords_form.is_valid():
                k = keywords_form.save(commit=False)
                k.paragraph = Paragraph.objects.get(id = paragraph_id)
                k.save()
                return redirect('paragraphs')
        elif 'delete_actions' in request.POST:
            Action.objects.filter(
                pk__in=request.POST.getlist('delete_list')).delete()
            return redirect(reverse('paragraphs'))
        elif 'delete_links' in request.POST:
            Link.objects.filter(
                pk__in=request.POST.getlist('delete_list')).delete()
            return redirect(reverse('paragraphs'))
        elif 'delete_keywords' in request.POST:
            Keyword.objects.filter(
                pk__in=request.POST.getlist('delete_list')).delete()
            return redirect(reverse('paragraphs'))
        else:
            Paragraph.objects.filter(id = paragraph_id).delete()
            return redirect(reverse('paragraphs'))

    return render(request, 'paragraph.html', {'paragraph_id': paragraph_id, 'created_by':created_by, 'para':para, 'links':links,
    'keywords':keywords, 'actions':actions, 'p_form':p_form, 'l_form': link_form, 'a_form': action_form,
    'k_form': keywords_form})


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


def report_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and fill it with the request data
        input_form = InputForm(request.POST)

        if input_form.is_valid():
            # data from the form is stored in a dictionary, 'cd'
            cd = input_form.cleaned_data
            request.session['saved'] = cd
            # Create report
            report_id = create_report(request,
                                      cd, request.user.is_authenticated)
            if report_id is not None:
                return redirect(reverse('report_view', kwargs={'report_id': report_id}))
            else:
                return redirect(reverse('report_view_public'))

    # if we arrive here from a GET method, i.e. via inputting a url.
    else:
        # Create a new instance of the form
        input_form = InputForm()

        # Check if can populate the database from partial_inputs. i.e. if the user left without completing the form
        if request.user.is_authenticated:
            user = models.UserProfile.objects.get(user=request.user)
            partials = models.PartialInput.objects.filter(created_by=user)
            if partials:
                # Dictionary to store partials, to be passed in to instantiated input_form
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
                input_form = InputForm(initial=partials_dict)
    context = {'inputForm': input_form, }
    return render(request, 'report_create.html', context)


@login_required(login_url='login')
def report_view(request, report_id):
    # Pass required info and update template
    report = models.Report.objects.filter(id=int(report_id)).first()

    if report is not None:
        paras = report.paragraphs.all()
        link_list = models.Link.objects.filter(paragraph__in=paras)
        actions_list = models.Action.objects.filter(paragraph__in=paras)

        links_dict = {}

        # get the associated links and actions for each paragraph
        for par in paras:
            temp = []
            t = []
            big_l = []
            for link in link_list:
                if par == link.paragraph:
                    temp.append(link)
            for act in actions_list:
                if par == act.paragraph:
                    t.append(act)
            if temp:
                big_l.append(temp)
            if t:
                big_l.append(t)
            # list of the lists for links and actions added to dictionary
            links_dict[par] = big_l

        return render(request, 'report.html', {'data': links_dict})

    return render(request, "error.html")


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

    for _ in range(num_paras):
        highest_score = max(scores_dict, key=scores_dict.get)
        paragraphs_list.append(highest_score)
        del scores_dict[highest_score]
    return paragraphs_list


def report_view_public(request):
    # Get the dictionary of inputs. Gathered in InputForm, saved to django session.
    inputs = request.session.get('saved')
    # Get a list of paragraphs based on the inputs
    paras = get_paragraphs(inputs)
    # Get all the relevant context for the paragraphs
    links_dict = get_context_from_paragraphs(paras)

    context = {'data': links_dict}
    return render(request, 'report_public.html', context)


def create_report(request, inputs, is_authenticated=False):
    # Get a list of paragraphs based on the inputs
    paras = get_paragraphs(inputs)
    report_id = None

    # If a user is logged in then create and save a report instance linked to their profile
    if is_authenticated:
        current_user_profile = models.UserProfile.objects.filter(
            user=request.user).first()
        # Create a report instance and add paragraphs to it
        rep = models.Report(user=current_user_profile,
                            datetime_created=datetime.now())
        rep.save()
        report_id = rep.id
        for p in paras:
            rep.paragraphs.add(p)

    # if a user is not logged in
    else:
        # serialize the paragraphs and save them to the session
        request.session["temp_saved"] = serialize('json', paras)

    return report_id


def get_context_from_paragraphs(paras):
    ''' Helper method retrieving all required data from paragraphs
    that is needed for rendering a report.
    '''
    link_list = models.Link.objects.all()
    actions_list = models.Action.objects.all()
    links_dict = {}

    # get the associated links and actions for each paragraph
    for par in paras:
        temp = []
        t = []
        big_l = []
        for link in link_list:
            if par == link.paragraph:
                temp.append(link)
        for action in actions_list:
            if par == action.paragraph:
                t.append(action)
        if temp:
            big_l.append(temp)
        if t:
            big_l.append(t)
        # list of the lists for links and actions added to dictionary
        links_dict[par] = big_l
    return links_dict
