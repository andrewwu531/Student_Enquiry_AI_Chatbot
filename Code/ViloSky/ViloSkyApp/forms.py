from django import forms
from .models import UserProfile, Paragraph, Report, Link, Keyword, Action
import datetime
from datetime import date

class ReportForm(forms.ModelForm):
    datetime_created = forms.DateField(initial=datetime.date.today, widget=forms.HiddenInput())
    class Meta:
        model = Report
        fields = [
            'datetime_created',
        ]