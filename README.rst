===============================
Flask-Boilerplate
===============================

simple boilerplate for flask applications to get up and running real quick

based on the flask cookiecutter project:
https://github.com/sloria/cookiecutter-flask

Quickstart
----------

Assumes use of virtualenv / virtualenvwrapper / autoenv
http://docs.python-guide.org/en/latest/dev/virtualenvs/

::

    git clone https://github.com/isaacchansky/flask_boilerplate
    cd flask_boilerplate
    pip install -r requirements/dev.txt
    export FLASK_BOILERPLATE_ENV='dev'
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.

Development / Production Environments
-------------------------------------

Configuration environements are handled through the FLASK_BOILERPLATE_ENV system environment variable.

To switch to the development environment, set ::

    export FLASK_BOILERPLATE_ENV="dev"

To switch to the production environment, set ::

    export FLASK_BOILERPLATE_ENV="prod"
