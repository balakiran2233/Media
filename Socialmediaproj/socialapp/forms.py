from django import forms
from .models import Article,Comment
from django.contrib.auth.models import User
from django.forms import fields

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )
    confirm_password=forms.CharField(
    label='Confirm Password',
    widget=forms.PasswordInput(
        attrs={
            'placeholder':'Confirm password',
            'class':'form-control'
                }
         )
    )
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']

class UserLoginForm(forms.Form):
    username=forms.CharField(
        label='UserName',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control'
            }
        )

    )
    password=forms.CharField(
    label='password:',
    widget=forms.PasswordInput(
        attrs={
        'placeholder':'Password',
        'class':'form-control'
            }
        )
    )

class ArticleCreateForm(forms.Form):
    title=forms.CharField(
        label='Enter Title',
        widget=forms.TextInput(
            attrs={
                'placeholder':'title',
                'class':'form-control'
            }
        )
    )

    body=forms.CharField(
        label='Enter Body',
        widget=forms.Textarea(
            attrs={
                'placeholder':'body',
                'class':'form-control',
                'rows':10,
                'columns':50
            }
        )
    )


class ArticleEditForm(forms.Form):
    title=forms.CharField(
        label='Enter Title',
        widget=forms.TextInput(
            attrs={
                'placeholder':'title',
                'class':'form-control'
            }
        )
    )

    body=forms.CharField(
        label='Enter Body',
        widget=forms.Textarea(
            attrs={
                'placeholder':'body',
                'class':'form-control',
                'rows':10,
                'columns':50
            }
        )
    )

class CommentForm(forms.ModelForm):
    content= forms.CharField(
        label="",
        widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'text goes here..',
            'rows':'5',
            'columns':'40'        
            }
        )
    )
    class Meta:
        model=Comment
        fields=('content',)
