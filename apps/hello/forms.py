from django import forms
from .models import About_me, AllRequests
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from datetime import date
current_year = date.today().year


class AuthorForm(forms.ModelForm):

    class Meta:
        model = About_me
        widgets = {
            'bio': forms.Textarea(),
            'contacts': forms.Textarea()
        }

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        year = data.year
        time_delta = (date.today() - data).total_seconds()
        if time_delta < 0 or year < 1900:
            raise ValidationError("- Your birth date is unreal.")
        return data

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('Email uncorrect')
        return email

    def clean_jabber(self):
        jabber = self.cleaned_data['jabber']
        try:
            validate_email(jabber)
        except ValidationError:
            raise ValidationError("- Jabber uncorrect.")
        return jabber


class RequestForm(forms.ModelForm):

    class Meta:
        model = AllRequests
