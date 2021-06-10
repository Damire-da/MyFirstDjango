from django import forms
from .models import Draft

class FormPage(forms.ModelForm):
    class Meta:
        model = Draft
        fields = ['title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Просто текст'
            })
        }

