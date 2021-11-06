from django.contrib import admin
from .models import  Matches , Attendence , week , Month


class attendenceDisplay(admin.ModelAdmin):
    list_display = ('week_match', 'player','Attendence_option')
class MonthDisplay(admin.ModelAdmin):
    list_display = ('id','winner')

class MatchDisplay(admin.ModelAdmin):
    list_display = ('week_id', 'yellow_team','red_team')


admin.site.register(Matches , MatchDisplay)
admin.site.register(Attendence , attendenceDisplay)
admin.site.register(week)
admin.site.register(Month , MonthDisplay)
