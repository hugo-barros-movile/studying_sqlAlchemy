from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, value):
        return self.password == value


    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def insert_user(self):
        try: 
            db.session.add(self)
            db.session.commit()
        except:
            return False

        return True


    def __repr__(self):
        return '<User %r>' % self.username
