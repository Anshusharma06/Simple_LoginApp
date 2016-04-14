"""
    Honeynet Task: Simple Login Application
                ~~~~~~~~~

    Author: Satwik Bhattamishra <ronu66@gmail.com>
    Task for Honeynet Organization
"""

from login_app import login_app
from flask import render_template, redirect, request, flash, session, url_for
from forms import *
from models import db, User


@login_app.route('/dashboard/')
def dashboard():
    """
    Checks if user is authenticated by looking
    for the key named 'username'. If it does not
    exist, redirect to login page.

    If it exists, then query the database for the
    user with this username.

    """
    if 'username' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(username= session['username']).first()

    if user is None:
        return redirect(url_for('login'))
    else:
        return render_template('dashboard.html', user=user)


@login_app.route('/')
def index():
    """
    The landing page of the website,
    with a login and register button.

    If a user is authenticated, he/she
    will be redirected to the dashboard
    page.

    """

    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@login_app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Opens the page with a form for user login.

    In case of a POST request it validates the form
    and redirects to the dashboard page after setting
    a cookie in the user's browser, if the form is
    valid, else it displays an error message.

    If user is authenticated, he/she is redirected
    to the dashboard page.
    """
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate() == False:
            return render_template('login.html', form=form)
        else:
            session['username'] = form.username.data
            flash('Logged In')
            return redirect(url_for('dashboard'))

    elif request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('dashboard'))
        return render_template('login.html', form=form)


@login_app.route('/logout/')
def logout():
    """
    Clears the cookie in the browser.

    Redirects to the landing(index)
    page.

    """

    if 'username' not in session:
        return redirect(url_for('login'))

    session.pop('username', None)
    flash('logged out')
    return redirect(url_for('index'))


@login_app.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Takes the data in the form of a POST request from
    the user, validates the form, creates a new User
    object if the form is valid.

    Adds the new objects in the database object's
    session and updates the database by committing
    the changes.

    """
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.form)

        if form.validate() == False:
            return render_template('register.html', form=form)

        else:
            new_user = User(username=form.username.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()

            session['username'] = new_user.username

            return redirect(url_for('dashboard'))

    elif request.method == 'GET':
        return render_template('register.html', form=form)
