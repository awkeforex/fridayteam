from django.db import models
from django.db.models.base import Model
from Members.models import User
from django.db.models.fields import CharField , IntegerField


# Create your models here.
class week(models.Model):
    week_count = models.IntegerField(null=True , default=1 ,blank= True)
    date =  models.DateTimeField(auto_now_add=True , blank=True , null=True)
    created = models.CharField(max_length=64 , null=True)


    def __str__(self):
        return f" Week{self.id} "



class Month(models.Model):
    winner = models.CharField(null=True , blank= True ,  max_length=50)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" Month{self.id}   {self.winner}" 




class Matches(models.Model):
    results = (
    ("win" , "win"),
    ("loss" , "loss"),
    ("draw" , "draw")
    )
    
    week_id = models.ForeignKey(week , on_delete=models.CASCADE , null=True , blank=True) 
    date = models.DateTimeField(auto_now=True , blank=True)
    yellow_team = models.CharField(max_length= 64 , choices= results  , null= True)
    red_team = models.CharField(max_length= 64 , choices= results , null= True)


    def __str__(self):
        return f" Week{self.week_id}"



class Attendence(models.Model):
    
    options = (
        ( "Jooga" , "Jooga"),
        ( "Maqan", "Maqan"),
    )
    
    week_match= models.ForeignKey(week , on_delete=models.CASCADE  , blank=True , null=True) 
    player= models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True , blank=True)
    Attendence_option =  models.CharField(max_length= 64 , choices= options , null= True)
    status = models.BooleanField(null=True ,  blank=True)


    def __str__(self):
        return f" Week{self.week_match} {self.player.username}  {self.Attendence_option}" 