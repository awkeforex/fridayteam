from App.models import week , Attendence
from Members.models import User 

def week_check():
   if week.objects.all():
      last_week = week.objects.all().last()
      return last_week
   else:
      return 1

def attendence_register():
   users = User.objects.all()
   for user in users:
      Attendence.objects.create(week_match = week_check(),player = user , Attendence_option = 'Jooga')

def week_count():
   if week.objects.all():
      n = week.objects.all().count()
      n = n % 4 
      if n == 0:
         n = 4 
      return n 
   else:
      return 1


def  week_creation():
   week_id = week.objects.all()
   if week_id:
         week_cnt =  week_count()
         return week.objects.create(created = 'Admin' , week_count = week_cnt)
   else:
      return week.objects.create(created = 'Admin' , week_count = 1)


