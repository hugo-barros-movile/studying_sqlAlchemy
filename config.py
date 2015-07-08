import os

# default to dev config because no one should use this in
# production anyway
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                         'sqlite:///database.db')

DEBUG = True
