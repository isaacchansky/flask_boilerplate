#!/usr/bin/env python
import os
import sys
import subprocess
from flask.ext.script import Manager, Shell, Server
from flask_boilerplate import models
from flask_boilerplate.app import create_app
from flask_boilerplate.models import db

env = os.environ.get("FLASK_BOILERPLATE_ENV", 'prod')
app = create_app("flask_boilerplate.settings.{0}Config"
                    .format(env.capitalize()), env)

manager = Manager(app)
TEST_CMD = "nosetests"

def _make_context():
    '''Return context dict for a shell session so you can access
    app, db, and models by default.
    '''
    return {'app': app, 'db': db, 'models': models}

@manager.command
def test():
    '''Run the tests.'''
    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)

@manager.command
def createdb():
    '''Create a database from the tables defined in models.py.'''
    db.create_all()

manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
