import typer

app = typer.Typer()

@app.command()
def hello():
    print("hello World!")

if __name__ == "__main__":
    app()
