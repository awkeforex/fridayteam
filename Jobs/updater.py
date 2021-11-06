from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from  .jobs import attendence_register, week_creation
from datetime import date
 
start_date = date(2021 , 11, 4)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(week_creation , "interval" , days = 7)
    scheduler.add_job(attendence_register, "interval" ,days = 5 , seconds = 20)
    scheduler.start()