from django import forms

from . import models
from .models import Post, Poste, Postw
from django.conf import settings
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'text', 'image']
        widgets = {
            "name": forms.TextInput(attrs={
                'autocomplete' : 'off',
             'class':'form-control',
            'placeholder': "вводи тему епта"
        }),
            "text": forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder':'Вводи текст сюда епта'
        }),
        }
image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': '',
            'required' : True,
            'type':'file',
            'id':'files',
            'name':'files[]',
            'multiple': False


        })
    )


class AccessKeyForm(forms.Form):
    access_key = forms.CharField(max_length=50, label="Ну вводи товарищ курсант")

class PosteForm(forms.ModelForm):
        class Meta:
            model = Poste
            fields = ['name', 'text', 'image']
            widgets = {
                "name": forms.TextInput(attrs={
                    'autocomplete': 'off',
                    'class': 'form-control',
                    'placeholder': "вводи тему епта"
                }),
                "text": forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Вводи текст сюда епта'
                }),
            }
            image = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={
            'class': '',
            'required': True,
            'type': 'file',
            'id': 'files',
            'name': 'files[]',
            'multiple': False

        })
    )


class PostwForm(forms.ModelForm):
    class Meta:
        model = Postw
        fields = ['name', 'text', 'image']
        widgets = {
            "name": forms.TextInput(attrs={
                'autocomplete': 'off',
                'class': 'form-control',
                'placeholder': "вводи тему епта"
            }),
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вводи текст сюда епта'
            }),
        }
        image = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={
                'class': '',
                'required': True,
                'type': 'file',
                'id': 'files',
                'name': 'files[]',
                'multiple': False

            })
        )

        class AccessKeyForm(forms.Form):
            access_key = forms.CharField(max_length=50, label="Ну вводи товарищ курсант")