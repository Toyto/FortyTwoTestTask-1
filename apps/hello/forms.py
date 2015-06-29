from django import forms
from .models import About_me

class AuthorForm(forms.ModelForm):
    class Meta:
        model = About_me
        widgets = {
            'bio': forms.Textarea(),
            'contacts': forms.Textarea()
        }