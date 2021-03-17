""" Views for the ViloSky app"""
import json
from random import uniform, randint
from plotly.offline import plot
import plotly.graph_objs as go
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from django.contrib.auth.decorators import login_required
from django.utils.formats import localize
from ViloSkyApp import models
from ViloSkyApp.forms import (UserForm, QualificationForm, UserProfileForm, DropdownAdminInputForm,
                              CheckboxAdminInputForm, TextAdminInputForm, TextareaAdminInputForm)
from ViloSkyApp.models import Qualification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


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
            # q_form = QualificationForm(request.POST, instance = request.user.user_profile)
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


class AdminInputDetail(LoginRequiredMixin, DetailView):
    model = models.AdminInput
    template_name = 'admin_input_detail.html'
    # By default django looks for "pk" in the url
    # By changing this it will now look for admin_input_id instead, as is already written in urls.py
    pk_url_kwarg = 'admin_input_id'


class DropdownAdminInput(LoginRequiredMixin, CreateView):
    form_class = DropdownAdminInputForm
    template_name = 'admin_input_form.html'

    def form_valid(self, form):
        form.instance.created_by = get_object_or_404(models.UserProfile, user=self.request.user)
        form.instance.input_type = "DROPDOWN"

        for ch in [' ', '[', ']', '\\', '\"']:
            if ch in form.instance.choices:
                form.instance.choices = form.instance.choices.replace(ch, '')
        form.instance.choices = json.dumps(form.instance.choices.split(','))

        return super().form_valid(form)


class DropdownAdminInputUpdate(LoginRequiredMixin, UpdateView):
    form_class = DropdownAdminInputForm
    model = models.DropdownAdminInput
    template_name = 'admin_input_form.html'
    pk_url_kwarg = 'admin_input_id'

    def form_valid(self, form):
        for ch in [' ', '[', ']', '\\', '\"']:
            if ch in form.instance.choices:
                form.instance.choices = form.instance.choices.replace(ch, '')
        form.instance.choices = json.dumps(form.instance.choices.split(','))
        return super().form_valid(form)


class CheckboxAdminInput(LoginRequiredMixin, CreateView):
    form_class = CheckboxAdminInputForm
    template_name = 'admin_input_form.html'

    def form_valid(self, form):
        form.instance.created_by = get_object_or_404(models.UserProfile, user=self.request.user)
        form.instance.input_type = "CHECKBOX"
        return super().form_valid(form)


class CheckboxAdminInputUpdate(LoginRequiredMixin, UpdateView):
    form_class = CheckboxAdminInputForm
    model = models.CheckboxAdminInput
    template_name = 'admin_input_form.html'
    pk_url_kwarg = 'admin_input_id'


class TextAdminInput(LoginRequiredMixin, CreateView):
    form_class = TextAdminInputForm
    template_name = 'admin_input_form.html'

    def form_valid(self, form):
        form.instance.created_by = get_object_or_404(models.UserProfile, user=self.request.user)
        form.instance.input_type = "TEXT"
        return super().form_valid(form)


class TextAdminInputUpdate(LoginRequiredMixin, UpdateView):
    form_class = TextAdminInputForm
    model = models.TextAdminInput
    template_name = 'admin_input_form.html'
    pk_url_kwarg = 'admin_input_id'


class TextAreaAdminInput(LoginRequiredMixin, CreateView):
    form_class = TextareaAdminInputForm
    template_name = 'admin_input_form.html'

    def form_valid(self, form):
        form.instance.created_by = get_object_or_404(models.UserProfile, user=self.request.user)
        form.instance.input_type = "TEXTAREA"
        return super().form_valid(form)


class TextareaAdminInputUpdate(LoginRequiredMixin, UpdateView):
    form_class = TextareaAdminInputForm
    model = models.TextareaAdminInput
    template_name = 'admin_input_form.html'
    pk_url_kwarg = 'admin_input_id'


class AdminInputDelete(LoginRequiredMixin, DeleteView):
    model = models.AdminInput
    template_name = 'admin_input_delete.html'
    pk_url_kwarg = 'admin_input_id'

    def get_success_url(self):
        return reverse('admin_inputs')


@ login_required(login_url='login')
def admin_inputs(request):
    # Get User
    user = models.UserProfile.objects.filter(user=request.user).first()

    # If no user logged in then show error.html
    if user is None:
        return render(request, "error.html")

    # List Item to store admin input details to be rendered
    inputs_to_render = list(
        models.AdminInput.objects.all().values('id', 'created_by__user__first_name', 'label', 'input_type',
                                               'is_required'))
    template_headings = ["#", "Created By", "Label", "Type", "Required"]
    model_keys = ["id", "created_by__user__first_name",
                  "label", "input_type", "is_required"]

    return render(request, 'admin_inputs.html', {
        "headings": template_headings, "model_keys": model_keys,
        "entries": inputs_to_render, "row_link_to": "/admin_input/"
    })


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
