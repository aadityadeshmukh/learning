from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'note')
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control my-5'}),
            'note': forms.Textarea(attrs={'class' : 'form-control mb5'})
        }
        labels = {
            'note': "What's on your mind?"
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Not a django related note')
        return title