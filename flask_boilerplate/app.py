import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader

from flask_boilerplate import assets
from flask_boilerplate.models import db
from flask_boilerplate.utils import bcrypt

assets_env = Environment()

def create_app(config_object, env):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    :param env: A string, the current environment. Either "dev" or "prod"
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['ENV'] = env
    # Initialize SQLAlchemy
    db.init_app(app)
    # Register bcrypt
    bcrypt.init_app(app)
    # Register asset bundles
    assets_env.init_app(app)
    assets_loader = PythonLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)
    # Register blueprints
    from flask_boilerplate.modules import public, member
    app.register_blueprint(public.blueprint)
    app.register_blueprint(member.blueprint)

    return app
