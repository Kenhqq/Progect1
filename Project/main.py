from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db, mail
from flask_mail import Message

main = Blueprint('main', __name__)

# YouTube iFrame
"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/3yJTZottyjM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
https://www.youtube.com/watch?v=3yJTZottyjM
https://youtu.be/3yJTZottyjM
"""

@main.route('/')
def start():
    return render_template('start.html', hasNav= False)


@main.route('/base')
def base():
    return render_template('base.html', hasNav= False)


@main.route('/forgot-password', methods=['GET'])
def forgot_pass():
    return render_template('forgotpass.html', hasNav= True)


@main.route('/watch', methods=['GET'])
def watch_form():
    return render_template('watch.html')


@main.route('/yt_watch', methods=['POST'])
def yt_watch():
    link = 'https://www.youtube.com/embed/'+request.form.get('yt_link').split('/')[-1]
    return render_template('youtube_watch.html', link= link)



@main.route('/forgot-password', methods=['POST'])
def forgot_pass_post():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        msg = Message('Забыли логин или пароль?',
                      sender='Watch2Gether',
                      recipients = [email])
    return email

@main.route('/mail-sent')
def mail_sent():
    return render_template('mail-sent.html', hasNav=True)

@main.route('/index')
def index():
    return render_template('index.html', hasNav= True)


@main.route('/login', methods=['POST'])
def login_email():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        msg = Message('Забыли логин?',
                      sender='Watch2Gether',
                      recipients = [email])
    return email


def login_pass():
    password = request.form.get('password')
    user = User.query.filter_by(password=password).first()
    if user:
        msg = Message('Забыли пароль?',
                      sender='Watch2Gether',
                      recipients=[email])
    return email



