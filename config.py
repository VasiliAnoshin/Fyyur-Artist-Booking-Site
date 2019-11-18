import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://USER@localhost:5432/fyyurdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
#if SQLALCHEMY_DATABASE_URI is None:
#    raise Exception('Please, set the DATABASE_URL environment variable to be postgresql://postgres@localhost/jane')
