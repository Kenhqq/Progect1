from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db, mail
from flask_mail import Message

main = Blueprint('main', __name__)



@main.route('/')
def start():
    return render_template('start.html', hasNav= False)


@main.route('/base')
def base():
    return render_template('base.html', hasNav= False)


@main.route('/forgot-password', methods=['GET'])
def forgot_pass():
    return render_template('forgotpass.html', hasNav= True)


@main.route('/forgot-password', methods=['POST'])
def forgot_pass_post():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        msg = Message('Забыли пароль?', 
                      sender='Watch2Gether',
                      recipients = [email])
    return email


@main.route('/index')
def index():
    return render_template('index.html', hasNav= True)
