from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail, Message


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'social_media.sqlite')
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

mail = Mail(app)
db = SQLAlchemy(app)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
