import click
from application import db, app
from application.models import Class, User

@app.cli.command()
@click.option('--drop', is_flag=True, help="Create after drop")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized database.")

@app.cli.command()
def addclass():
    classes = [
        {"classname": "zhen_kong"},
        {"classname": "hua_heng"},
        {"classname": "zang_wu"},
        {"classname": "zhe_zhou"}
    ]
    for c in classes:
        cl = Class(classname=c["classname"])
        db.session.add(cl)
    db.session.commit()
    click.echo("classes added done.")
    
@app.cli.command()
@click.option('--username', prompt = True, help = "username to login")
@click.option('--password', prompt = True, confirmation_prompt=True, help = "password to login")
def userset(username, password):
    db.create_all()
    user = User.query.filter(User.name == username).first()
    if user is not None:
        click.echo("User already exists, now reset password")
        user.set_password(password)
    else:
        click.echo("creating user......")
        user = User(name=username)
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo("done.")
        