from django.urls import path
from . import views


urlpatterns = [
    path('match-register/', views.matches , name='matches'),
    path('attendence/', views.Attendence_register , name='attendence'),
    path('attendenceUpdate/', views.AttendenceUpdate , name='attendenceUpdate'),
    path('team-view/' , views.team_changer , name='team-view'),
    path('team-edit/<str:pk>' , views.edit_team , name='team-edit'),
    
    path('table/', views.Table, name='table'),
    path('attendecetable/', views.AttendenceTable, name='attendencetable'),   
]

