
from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from Members.models import User , Team
from  .models import week , Attendence
from .forms import MatchesRegister , AttendenceRegister, Matches , team
from django.db.models import F
from  Jobs.helpers import winner_In_week_3 , winner_game_4
from  Jobs.jobs import attendence_register, week_count
from  base.decorators import allowed_users , IsMatchDay , Line_up_avialable
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['Guddi'])
def matches(request):
   week_day = week.objects.all().last() 
   form = MatchesRegister()
   if request.method == 'POST':
      yellow_team = request.POST['yellow_team']
      red_team = request.POST['red_team']
      print(yellow_team , red_team)
      form = MatchesRegister(request.POST)
      if form.is_valid():
         match = form.save(commit=False)
         match.week_id = week_day
         match.week_count = week_count()
         match.save()
         request.session['match_week'] = True
         if yellow_team == 'win':
            Team.objects.filter(name = 'Yellow Team').update(points = F('points') + 3)
            User.objects.filter(currentTeam_id = 2).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day).update(loss= F("loss") + 1 , points = F("points") + 0 , Total_games = F('Total_games') + 1)
            User.objects.filter(currentTeam_id = 1).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day).update(wins= F("wins") + 1 , points = F("points") + 3, Total_games = F('Total_games') + 1)
         elif yellow_team == 'loss':
            Team.objects.filter(name = 'Red Team').update(points = F('points') + 3)
            User.objects.filter(currentTeam_id = 1).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day).update(loss= F("loss") + 1 , points = F("points") + 0, Total_games = F('Total_games') + 1)
            User.objects.filter(currentTeam_id = 2).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day).update(wins= F("wins") + 1 , points = F("points") + 3, Total_games = F('Total_games') + 1)
         else:
            Team.objects.all().update(points = F('points') + 1)
            User.objects.filter(currentTeam_id = 1).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day).update(draw= F("loss") + 1 , points = F("points") + 1, Total_games = F('Total_games') + 1)
            User.objects.filter(currentTeam_id = 2).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day).update(draw= F("wins") + 1 , points = F("points") + 1, Total_games = F('Total_games') + 1)
         
         if week_day.week_count == 3:
            winner_In_week_3()
         
         elif week_day.week_count == 4:
            winner_game_4()

         else:
            pass   
         return redirect('home')
         
      else:
         return redirect('matches')
         
   
   context = {'week_id' : week_day , 'form':form }
   return render (request , 'app/match_register.html' , context)



@IsMatchDay
def Attendence_register(request):
   week_day = week.objects.all().last() 
   week_number = week_day.id
 
   form = AttendenceRegister()
   if request.method == 'POST':
         form = AttendenceRegister(request.POST)
         if form.is_valid():
            attend  = form.save(commit=False)
            attend.week_match = week_day
            attend.player = request.user
            attend.status = True
            attend.save()
            request.session['username'] = request.user.username
            request.session['week'] = week_number
            return redirect('attendencetable')
         else:
            return redirect('attendence')

   context = {'week_id' : week_number , 'form':form}
   return render(request , 'app/attend.html' , context)



@login_required(login_url='login')
def  Table(request):
   users = User.objects.all().order_by('-points')
   context={'users':users}
   return render(request, 'app/table.html' , context)

@login_required(login_url='login')
@Line_up_avialable
def  AttendenceTable(request):
   users = User.objects.all()
   week_day = week.objects.all().last() 
   ready_yellow = User.objects.filter(currentTeam_id = 2).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day)
   Absent_yellow = User.objects.filter(currentTeam_id = 2).filter(attendence__Attendence_option="Maqan" , attendence__week_match = week_day)
   ready_Red = User.objects.filter(currentTeam_id = 1).filter(attendence__Attendence_option="Jooga" , attendence__week_match = week_day)
   Absent_Red = User.objects.filter(currentTeam_id = 1).filter(attendence__Attendence_option="Maqan" , attendence__week_match = week_day)
  


   context={'users':users , 'week_day':week_day, 'ready_yellow': ready_yellow , 'ready_red':ready_Red , 'absent_yellow':Absent_yellow , 'absent_red':Absent_Red }
   return render(request, 'app/players.html' , context)


@IsMatchDay
def AttendenceUpdate(request):
   week_day = week.objects.all().last() 
   week_number = week_day.id
   player = Attendence.objects.filter(week_match = week_day , player = request.user)[0]
   form = AttendenceRegister(instance=player)
   if request.method == 'POST':
         form = AttendenceRegister(request.POST , instance=player)
         if form.is_valid():
            attend  = form.save(commit=False)
            attend.week_match = week_day
            attend.player = request.user
            attend.status = True
            attend.save()
            return redirect('attendencetable')
         else:
            return redirect('attendence')
  
   context = {'week_id' : week_number , 'form':form}
   return render(request , 'app/attend.html' , context)


login_required(login_url='login')
@allowed_users(allowed_roles=['Guddi'])
def team_changer(request):
   yellowUsers =  User.objects.filter(currentTeam=1).all()
   redUsers = User.objects.filter(currentTeam=2).all()
   context = {'yellowUsers':yellowUsers , 'redUsers':redUsers}
   return render(request , 'app/team.html', context)

login_required(login_url='login')
@allowed_users(allowed_roles=['Guddi'])
def edit_team(request, pk):
   user = User.objects.get(id=pk)
   form = team(instance=user)
   if request.method == 'POST':
      form = team(request.POST ,instance=user)
      if form.is_valid():
         form.save()
         return redirect('home')
      else:
         return redirect('team-view')
         
   context = {'form':form}
   return render(request , 'app/edit-team.html', context)