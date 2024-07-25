import functools

from argon2.exceptions import VerifyMismatchError
from flask import render_template, request, redirect, session, url_for
from sqlalchemy import Select

from pensieve_web import app, db, ph
from pensieve_web.models import User, Unit


def require_login(view):
    @functools.wraps(view)
    def decorated(*args, **kwargs):
        if session is None or "user_id" not in session:
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return decorated


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html", )


@app.route('/login', methods=['POST'])
def _login():
    user = db.session.get_one(User, request.form["userid"])

    try:
        ph.verify(user.password_hash, request.form["password"])
        session['user_id'] = user.user_id
    except VerifyMismatchError:
        return redirect('/login?error', code=303)

    return redirect('/dashboard')


@app.route('/dashboard')
@require_login
def dashboard():
    user = db.session.get_one(User, session["user_id"])
    return render_template("dashboard.html", user=user)

@app.route('/unit/<unit_id>')
@require_login
def unit_view_staff(unit_id):
    # TODO verify user permissions to view unit
    user = db.session.get_one(User, session["user_id"])
    unit = db.session.get_one(Unit, unit_id)
    unit_staff = [x for x in unit.user if x.role in ['owner', 'staff']]
    return render_template("unit.html", user=user, unit=unit, staff=unit_staff)

