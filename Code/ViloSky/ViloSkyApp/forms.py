'''Forms for the ViloSky app'''
import datetime
from django import forms
from django.contrib.auth import get_user_model
from ViloSkyApp.models import (UserProfile, Qualification, AdminInput, DropdownAdminInput,
                               TextAdminInput, TextareaAdminInput, CheckboxAdminInput,
                               RadioButtonsAdminInput, Paragraph, Link, Keyword, Action)


class UserForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'id': 'inputEmail3', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'id': 'inputPassword4', 'placeholder': 'Enter password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'id': 'inputPassword5', 'placeholder': 'Confirm password'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'confirm_password')


class InputForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(AdminInput.objects.all()):

            # dropdowns
            if q.input_type == 'DROPDOWN':
                d_q = DropdownAdminInput.objects.get(label=q.label)
                # Need to set the choices as a tuple of (choice, choice)
                # That way filling in the form with partial_inputs is possible
                choices = [(c, c) for c in d_q.choices]
                # Set the default value of dropdowns to N/A
                choices.insert(0, ('', "N/A"))
                if q.is_required == 'True':
                    self.fields[d_q.label] = forms.ChoiceField(
                        label=d_q.label, choices=choices)
                else:
                    self.fields[d_q.label] = forms.ChoiceField(
                        label=d_q.label, choices=choices, required=False)

            # RadioButtons
            elif q.input_type == 'RADIOBUTTONS':
                r_q = RadioButtonsAdminInput.objects.get(label=q.label)
                # Need to set the choices as a tuple of (choice, choice)
                # That way filling in the form with partial_inputs is possible
                choices = [(c, c) for c in r_q.choices]
                if q.is_required == 'True':
                    self.fields[r_q.label] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                                       label=r_q.label, choices=choices)
                else:
                    self.fields[r_q.label] = forms.MultipleChoiceField(
                        widget=forms.CheckboxSelectMultiple, label=r_q.label, choices=choices, required=False)
            # Checkboxes
            elif q.input_type == 'CHECKBOX':
                check_q = CheckboxAdminInput.objects.get(label=q.label)
                if q.is_required == 'True':
                    self.fields['%s_field' %
                                i] = forms.BooleanField(label=check_q.label)
                else:
                    self.fields['%s_field' % i] = forms.BooleanField(
                        label=check_q.label, required=False)
            elif q.input_type == 'TEXT':
                text_q = TextAdminInput.objects.get(label=q.label)
                if q.is_required:
                    self.fields['%s_field' % i] = forms.CharField(
                        max_length=text_q.max_length, label=q.label)
                else:
                    self.fields['%s_field' % i] = forms.CharField(
                        max_length=text_q.max_length, label=q.label, required=False)
            else:
                textarea_q = TextareaAdminInput.objects.get(label=q.label)
                if q.is_required:
                    self.fields['%s_field' % i] = forms.CharField(
                        max_length=textarea_q.max_length, label=q.label)
                else:
                    self.fields['%s_field' % i] = forms.CharField(
                        max_length=textarea_q.max_length, label=q.label, required=False)


class UserProfileForm(forms.ModelForm):
    cur_year = datetime.datetime.today().year
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(
        years=tuple([i for i in range(cur_year - 80, cur_year - 16)])))

    class Meta:
        model = UserProfile
        fields = (
            'date_of_birth',
            'company',
            'employment_sector',
            'employment_status',
            'time_worked_in_industry'
        )


class QualificationForm(forms.ModelForm):
    level = forms.CharField(max_length=160, widget=forms.TextInput(attrs={
        'placeholder': 'Level e.g. High School ',
    }),
        required=True)
    subjects = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
    }),
        required=True)

    class Meta:
        model = Qualification
        fields = (
            'level',
            'subjects'
        )
# QualificationFormSet = modelformset_factory(QualificationForm, fields = ('user','level', 'subjects'), extra = 1)


class DropdownAdminInputForm(forms.ModelForm):
    choices = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = DropdownAdminInput
        fields = [
            'label',
            'is_required',
            'choices',
        ]


class CheckboxAdminInputForm(forms.ModelForm):

    class Meta:
        model = CheckboxAdminInput
        fields = [
            'label',
            'is_required',
            'default_value',
        ]


class TextAdminInputForm(forms.ModelForm):

    class Meta:
        model = TextAdminInput
        fields = [
            'label',
            'is_required',
            'max_length',
        ]


class TextareaAdminInputForm(forms.ModelForm):

    class Meta:
        model = TextareaAdminInput
        fields = [
            'label',
            'is_required',
            'max_length',
        ]


class NewParaForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ('static_text',)
        widgets = {
            'static_text':  forms.Textarea(attrs={'placeholder': 'Having been out of work for over a year...'})}


class NewLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'https://womenreturners.com'})}

    def __init__(self, *args, **kwargs):
        super(NewLinkForm, self).__init__(*args, **kwargs)
        self.fields['url'].required = False


class NewActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'List your skills...'})}

    def __init__(self, *args, **kwargs):
        super(NewActionForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False


class NewKeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ('key', 'score')
        widgets = {
            'key': forms.TextInput(attrs={'placeholder': 'Risk Management'}),
            'score': forms.TextInput(attrs={'placeholder': '10'})
        }

    def __init__(self, *args, **kwargs):
        super(NewKeywordForm, self).__init__(*args, **kwargs)
        self.fields['key'].required = False
        self.fields['score'].required = False
