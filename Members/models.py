from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(null = True , blank= True)
    points = models.IntegerField(default=0,  blank=True , null=True)

    def __str__(self):
        return  self.name




teams = (
    ('RED','RED'),
    ('YELLOW','YELLOW')
)

positions = (
    ('FW', 'Forward'),
    ('MD', 'Midfielder'),
    ('DF', 'Defender'),
)


class User(AbstractUser):
   
    email = models.EmailField(unique=True , null=True)
    currentTeam = models.ForeignKey(Team , on_delete=models.CASCADE , null=True)
    position = models.CharField(max_length= 64 , choices= positions , null = True )
    wins = models.IntegerField(null =True ,default=0, blank=True)
    loss = models.IntegerField(null =True ,default=0 , blank=True)
    draw = models.IntegerField(null =True ,default=0, blank=True)
    Total_games = models.IntegerField(null=True , default=0 , blank=True)
    points = models.IntegerField(null=True , default=0 , blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return  self.username
        
class ProfileUser(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    fullName = models.CharField(null=True , max_length=200)
    phoneNumber = models.CharField(null=True , max_length=50)
    profile_pic = models.ImageField(null= True , default='avatar.svg' , blank=True)
    age = models.IntegerField(null=True)
    


    def __str__(self):
        return   self.fullName

