from django import forms
from django.forms import ModelForm ,  widgets
from .models import Matches , Attendence
from Members.models import User 





class MatchesRegister(ModelForm):
    class Meta:
        model = Matches
        fields = "__all__"
    

    widgets = {
            "yellow_team":forms.Select(attrs={'class':"form-select" , "name": "yellow"}),
            "red_team" : forms.Select(attrs={'class':"form-select" , "name": "red"}),
    }


class AttendenceRegister(ModelForm):
    class Meta:
        model = Attendence
        fields = ['Attendence_option']
        

class team(ModelForm):
     class Meta:
        model = User
        fields = ['currentTeam' , 'username']