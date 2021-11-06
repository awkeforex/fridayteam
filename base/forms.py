from django.db.models.base import Model 
from django.forms import ModelForm, fields, models, widgets
from .models import  Room , Messages
from django import forms





class RoomForm(ModelForm):
  class Meta:
    model = Room
    fields = "__all__"
    exclude = ['host', 'participants']


class MessageForm(ModelForm):
  class Meta:
      model = Messages
      fields = "__all__"
      exclude = ['user']


      widgets = {
        "body"  : forms.TextInput(attrs={'class': 'form-control','id':'body' , 'name' : 'body' ,
                  'autocomplete': 'off' , 'placeholder': 'Write your message here...'}),
        "images" :forms.FileInput(attrs={'id':"image" , 'name':'image','is_hidden': True,}),
        "video" :forms.FileInput(attrs ={'id':"video" , 'name':'video' , 'is_hidden': True,}),
      }




    