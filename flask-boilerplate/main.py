#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point for all things, to avoid circular imports.
"""
import os
from .app import create_app
from .models import User, db
import flask-boilerplate.modules as modules

if __name__ == '__main__':
    # Get the environment setting from the system environment variable
    env = os.environ.get("FLASK-BOILERPLATE_ENV", "prod")
    app = create_app("flask-boilerplate.settings.{env}Config"
                        .format(env=env.capitalize()), env)