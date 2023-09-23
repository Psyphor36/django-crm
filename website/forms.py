from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    f_name = forms.CharField(label="",max_length="30", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname'}))
    l_name = forms.CharField(label="",max_length="30",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}))

    class Meta:
        model = User
        fields = ('username','fname','lname','email','password1','password2')