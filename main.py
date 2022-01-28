import typer
from gcsa.google_calendar import GoogleCalendar

app = typer.Typer()

global gc

@app.command()
def login():
    gc = GoogleCalendar(credentials_path='./client_secret_176083467420-23cn6d5glp7cr1b4l3sj9t4e59s64hpu.apps.googleusercontent.com.json')

if __name__ == "__main__":
    app()
