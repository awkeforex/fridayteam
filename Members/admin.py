from django.contrib import admin
from django.contrib import admin
from .models import  User , ProfileUser , Team
# Register your models here.

class TeamDisplay(admin.ModelAdmin):
    list_display = ('id', 'name' , 'logo' , 'points')

admin.site.register(Team, TeamDisplay)
admin.site.register(ProfileUser)
admin.site.register(User)