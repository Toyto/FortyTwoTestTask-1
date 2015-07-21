from django import forms
from .models import About_me, AllRequests


class AuthorForm(forms.ModelForm):

    class Meta:
        model = About_me
        widgets = {
            'bio': forms.Textarea(),
            'contacts': forms.Textarea()
        }


class RequestForm(forms.ModelForm):

    class Meta:
        model = AllRequests
