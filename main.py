import typer
from datetime import date
from beautiful_date import *
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from gcsa.recurrence import Recurrence

from gcsa.recurrence import SECONDLY, MINUTELY, HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY


app = typer.Typer()


@app.command()
def event(time:str, name:str, duration:int = 60):
    today = date.today()

    startHour,startMinute = time.split(':')

    start = (today.day/M[today.month]/today.year)[int(startHour):int(startMinute)]

    end = start + duration * minutes

    event = Event(name,start=start,end=end)

    gc.add_event(event)

@app.command()
def event(time:str, name:str,freq:str = 'd', duration:int = 60):
    today = date.today()

    startHour,startMinute = time.split(':')

    start = (today.day/M[today.month]/today.year)[int(startHour):int(startMinute)]

    end = start + duration * minutes

    if freq.lower() == 'd':
        event = Event(name,start=start,end=end, recurrence=Recurrence.rule(freq=DAILY))
    elif freq.lower() == 'w':
        event = Event(name,start=start,end=end, recurrence=Recurrence.rule(freq=WEEKLY))
    elif freq.lower() == 'm':
        event = Event(name,start=start,end=end, recurrence=Recurrence.rule(freq=MONTHLY))
    
    gc.add_event(event)

if __name__ == "__main__":
    gc = GoogleCalendar(credentials_path='./client_secret_176083467420-23cn6d5glp7cr1b4l3sj9t4e59s64hpu.apps.googleusercontent.com.json')
    app()
