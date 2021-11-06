from Members.models import Team
from App.models import Month
from .jobs import week_creation
from datetime import date
from datetime import timedelta





def winner_In_week_3():
    yellow  = Team.objects.get(name = 'Yellow Team')
    red = Team.objects.get(name = 'Red Team')
    if yellow.points == 7:
        Month.object.create(winner = "Yellow Team")
        week_creation()
        return Team.objects.update(points = 0)
    elif red.points == 7:
        Team.object.create(winner = "Red Team")
        week_creation()
        return Team.objects.update(points= 0)
    else:
        pass

def winner_game_4():
    yellow  = Team.objects.get(name = 'Yellow Team')
    red = Team.objects.get(name = 'Red Team')
    if yellow.points > red.points :
        Month.objects.create(winner = 'Yellow Team')
        Team.objects.update(points = 0)
    elif red.points > yellow.points:
        Month.objects.create(winner = 'Red Team')
        Team.objects.update(points = 0)
    else:
        Month.objects.create(winner = 'No winner')
        Team.objects.update(points = 0)



matchday = date(2021 , 11, 4)
def matchweekday():
    global matchday
    if matchday == date.today():
        new  = matchday + timedelta(days = 7)
        matchday = new
        return matchday
    else:
        return matchday