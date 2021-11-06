from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, models
from .models import User, ProfileUser
from django.contrib.auth.forms import UserCreationForm


class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'position']








class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'currentTeam', 'position']


class createProfileUser(ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['fullName', 'age',  'phoneNumber', 'profile_pic']
