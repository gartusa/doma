from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class EditChoreForm(forms.Form):
    deadline = forms.DateField(help_text = 'When is this chore due?')

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        # Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - deadline cannot be in the past'))
        return data

class CreateChoreForm(forms.Form):
    title = forms.CharField(help_text = 'Enter a chore name')
    description = forms.CharField(help_text = 'Enter a description')
    created_on = forms.DateField()
    deadline = forms.DateField(help_text = 'When is this chore due?')

    def clean_title(self):
        data = self.cleaned_data['title']
        # Check title is not longer than 200 characters
        if len(data) > 200:
            raise ValidationError(_('Invalid title - cannot be longer than 200 characters'))
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        # Check description is not longer than 500
        if len(data) > 500:
            raise ValidationError(_('Invalid description - cannot be longer than 500 characters'))
        return data
    
    def clean_created_on(self):
        data = self.cleaned_data['created_on']
        # Check date is not in future. 
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - created_on cannot be in the future'))
        return data

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        # Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - deadline cannot be in the past'))
        return data
