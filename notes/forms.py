from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'text': 'Write your thoughts here:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accepts notes about Django!')

        elif 'Fuck' in title:
            raise ValidationError("The 'F' word is not allowed")
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if 'fuck' in text:
            raise ValidationError("The 'f' word is not allowed in your text field")
        return text