from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from flask_login import login_user
from flask_mail import Mail, Message

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_handler():
    email = request.form.get('email')
    password = request.form.get('password')
    remember_me = request.form.get('remember_me')
    user = User.query.filter_by(email=email).first()

    if not user or password != user.password:
        user.authenticated = False
        return redirect(url_for('auth.login'))

    user.authenticated = True
    return redirect(url_for('main.base'))


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
    msg = Message('Подтвердите почту',
                  sender='Watch2Gether',
                  recipients=[email])
    msg.body = 'Привет ! \n Подтвердите почту.'
    mail.send(msg)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/mail-verification')
def mail_verification():
    try:
        msg = Message('Подтвердите почту',
                      sender = '',
                      recipients = [])
        msg.body = 'Привет ! \n Подтвердите почту.'
        mail.send(msg)
        return render_template('mail-sent.html')
    except Exception as e:
        return(str(e))


