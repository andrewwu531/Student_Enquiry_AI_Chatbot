from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile, AdminInput, DropdownAdminInput, CheckboxAdminInput, TextareaAdminInput, TextAdminInput, RadioButtonsAdminInput

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

            # Dropdowns
            if q.input_type == 'DROPDOWN':
                d_q = DropdownAdminInput.objects.get(label=q.label)
                # Need to set the choices as a tuple of (choice, choice)
                # That way filling in the form with partial_inputs is possible
                choices = [(c,c) for c in d_q.choices]
                # Set the default value of dropdowns to N/A
                choices.insert(0, ('',"N/A"))
                if q.is_required == 'True':
                    self.fields[d_q.label] = forms.ChoiceField(label=d_q.label, choices=choices)
                else:
                    self.fields[d_q.label] = forms.ChoiceField(label=d_q.label, choices=choices, required=False)

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
                    self.fields[r_q.label] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                                       label=r_q.label, choices=choices, required=False)
            # Checkboxes
            elif q.input_type == 'CHECKBOX':
                check_q = CheckboxAdminInput.objects.get(label=q.label)
                if q.is_required == 'True':
                    self.fields[check_q.label] = forms.BooleanField(label=check_q.label)
                else:
                    self.fields[check_q.label] = forms.BooleanField(label=check_q.label, required=False)
            elif q.input_type  == 'TEXT':
                text_q = TextAdminInput.objects.get(label=q.label)
                if q.is_required:
                    self.fields[text_q.label] = forms.CharField(max_length=text_q.max_length, label=q.label)
                else:
                    self.fields[text_q.label] = forms.CharField(max_length=text_q.max_length, label=q.label, required=False)
            else:
                textarea_q = TextareaAdminInput.objects.get(label=q.label)
                if q.is_required:
                    self.fields[textarea_q.label] = forms.CharField(max_length=textarea_q.max_length, label=q.label)
                else:
                    self.fields[textarea_q.label] = forms.CharField(max_length=textarea_q.max_length, label=q.label, required=False)
