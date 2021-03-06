from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(
        DEBUG=True,
        # Настройки почты
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USERNAME='mvstrike17@gmail.com',
        MAIL_PASSWORD='',
        MAIL_USE_SSL=True
    )

    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
    return app


