===============================
Flask-Boilerplate
===============================

simple boilerplate for flask applications to get up and running real quick

based on the flask cookiecutter project:
https://github.com/sloria/cookiecutter-flask

Quickstart
----------

::

    git clone https://github.com/isaacchansky/flask-boilerplate
    cd flask-boilerplate
    pip install -r requirements/dev.txt
    export FLASK-BOILERPLATE_ENV='dev'
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.

Development / Production Environments
-------------------------------------

Configuration environements are handled through the FLASK-BOILERPLATE_ENV system environment variable.

To switch to the development environment, set ::

    export FLASK-BOILERPLATE_ENV="dev"

To switch to the production environment, set ::

    export FLASK-BOILERPLATE_ENV="prod"
