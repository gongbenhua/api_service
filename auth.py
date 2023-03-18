import functools
from utils.MysqlDb import db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

auth = Blueprint('auth', __name__)


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@auth.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        sql = 'SELECT * FROM student_system.user WHERE id = %s'
        g.user = db.select_one_value(sql,user_id)


@auth.route('/register', methods=('GET', 'POST'))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        sql0 = 'SELECT id FROM student_system.user WHERE username = %s'

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.select_one_value(sql0, username) is not None:
            error = 'User {0} is already registered.'.format(username)

        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            sql1 = 'INSERT INTO student_system.user (username, password) values(%s,%s)'
            value = (username,password)
            db.execute_value(sql1,value)
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        sql = 'SELECT * FROM student_system.user WHERE username = %s'
        user = db.select_one_value(sql,username)

        if user is None:
            error = 'Incorrect username.'

        elif user['password'] != password :
            error = 'Incorrect password.'

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for('index'))
