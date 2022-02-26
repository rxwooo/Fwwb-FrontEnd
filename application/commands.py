import click
from application import db, app
from application.models import Class

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
