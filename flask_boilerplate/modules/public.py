'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)
from sqlalchemy.exc import IntegrityError

from flask_boilerplate.models import User
from flask_boilerplate.forms import RegisterForm, LoginForm
from flask_boilerplate.utils import flash_errors, bcrypt
from flask_boilerplate.models import db

blueprint = Blueprint('public', __name__,
                        static_folder="../static",
                        template_folder="../templates")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    if request.method == 'POST':

        u = User.query.filter_by(username=request.form['username']).first()
        passhash = u.passhash
        pass_is_valid = bcrypt.check_password_hash(passhash, request.form['password'])

        if pass_is_valid:
            session['logged_in'] = True
            session['username'] = u.username
            flash("You are logged in.", 'success')
            return redirect(url_for("member.members"))
        else:
            error = 'Invalid username or password.'
            flash(error, 'warning')

    return render_template("home.html", form=form)

@blueprint.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))

@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        passhash = bcrypt.generate_password_hash(form.password.data)
        new_user = User(form.username.data, form.email.data, passhash)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Thank you for registering. You can now log in.", 'success')
            return redirect(url_for('public.home'))
        except IntegrityError as err:
            print(err)
            flash("That username and/or email already exists. Try again.", 'warning')
    else:
        flash_errors(form)
    return render_template('register.html', form=form)

@blueprint.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("about.html", form=form)

@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
