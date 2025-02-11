from django import forms
from django.shortcuts import render
from . import models
from .models import Post, Poste, Postw, People, News
from django.conf import settings
from .models import Comment, Commente, Commentw

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
image: forms.ImageField(
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

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['password']  # Указываем поле для редактирования
        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Введите пароль',
                'maxlength': 4,
            }),  # Отображаем поле как "пароль" (звёздочки вместо текста)
        }
        labels = {
            'password': 'Пароль',  # Название поля в форме
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Проверка, что ключ существует в базе данных
        if People.objects.filter(password=password, used=False).exists():
            return password
        raise forms.ValidationError("Неверный или уже использованный ключ.")


class NewsForm(forms.ModelForm):
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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CommenteForm(forms.ModelForm):
    class Meta:
        model = Commente
        fields = ['text']

class CommentwForm(forms.ModelForm):
    class Meta:
        model = Commentw
        fields = ['text']