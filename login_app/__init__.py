# Author: Satwik Bhattamishra <ronu66@gmail.com>
# Task for Honeynet Organization


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

login_app= Flask(__name__)
login_app.config.from_object('config')
db = SQLAlchemy(login_app)

from login_app import views, models
