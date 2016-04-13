# Author: Satwik Bhattamishra <ronu66@gmail.com>
# Task for Honeynet Organization


from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from login_app import db

 
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(30))

    def __init__(self, username, password):
        """
        Constructor(function) instantiates the 
        User objects used to store user data
        in the database through the ORM 

        """
        self.username= username
        self.set_password(password)
     
    def set_password(self, password):
        """
        Hashes the password entered by the
        user and stores it in the database
        """
        self.password_hash = generate_password_hash(password)
 
    def check_password(self, password):
        """
        Used to check whether the password entered
        by the user and the hased password stored
        in the database
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)
