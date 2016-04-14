# Author: Satwik Bhattamishra <ronu66@gmail.com>
# Task for Honeynet Organization


import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'gauss'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'login_app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
