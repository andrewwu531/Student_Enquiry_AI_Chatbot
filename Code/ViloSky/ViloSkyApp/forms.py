from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile, AdminInput, DropdownAdminInput, CheckboxAdminInput, TextareaAdminInput, TextAdminInput

class UserForm(forms.ModelForm):
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control txtbox'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control txtbox'}))

    class Meta:
        model = get_user_model()
        fields = ( 'email', 'password', 'confirm_password')

class InputForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(AdminInput.objects.all()):

            #dropdowns
            if q.input_type == 'DROPDOWN':
                d_q = DropdownAdminInput.objects.get(label=q.label)
                choices = d_q.choices
                choice_list = []
                counter = 1
                for i in choices:
                    choice_list.append((counter, i))
                if q.is_required == 'True':
                    self.fields['%s_field' % i] = forms.ChoiceField(label=d_q.label, choices =choice_list)
                else:
                    self.fields['%s_field' % i] = forms.ChoiceField(label=d_q.label, choices=choice_list, required=False)

            #Checkboxes
            elif q.input_type == 'CHECKBOX':
                check_q = CheckboxAdminInput.objects.get(label=q.label)
                if q.is_required == 'True':
                    self.fields['%s_field' % i] = forms.BooleanField(label=check_q.label)
                else:
                    self.fields['%s_field' % i] = forms.BooleanField(label=check_q.label, required=False)
            elif q.input_type  == 'TEXT':
                text_q = TextAdminInput.objects.get(label=q.label)
                if q.is_required:
                    self.fields['%s_field' % i] = forms.CharField(max_length=text_q.max_length, label=q.label)
                else:
                    self.fields['%s_field' % i] = forms.CharField(max_length=text_q.max_length, label=q.label, required=False)
            else:
                textarea_q = TextareaAdminInput.objects.get(label=q.label)
                if q.is_required:
                    self.fields['%s_field' % i] = forms.CharField(max_length=textarea_q.max_length, label=q.label)
                else:
                    self.fields['%s_field' % i] = forms.CharField(max_length=textarea_q.max_length, label=q.label, required=False)