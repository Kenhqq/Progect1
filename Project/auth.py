from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from flask_login import login_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_handler():

    return 'Здесь будет происходить обработка формы логина'


@auth.route('/register', methods=['GET'])
def reg():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def reg_handler():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    rep_pass = request.form.get('repeat_password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash("Пользователь с такой почтой уже существует")
        return redirect(url_for('auth.reg'))
    new_user = User(email = email, password=password, username=username)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
