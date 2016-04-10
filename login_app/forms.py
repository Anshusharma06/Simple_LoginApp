# Author: Satwik Bhattamishra <ronu66@gmail.com>
# Task for Honeynet Organization


from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms.validators import DataRequired
from models import db, User



class LoginForm(Form):
  username = TextField("Username",  [validators.Required("Please enter your Username.")])
  password = PasswordField("Password", [validators.Required("Please enter a password.")])
  submit = SubmitField("Log in")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(username = self.username.data).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.username.errors.append("Invalid Username or Password")
      return False



class RegisterForm(Form):
  username = TextField("Username",  [validators.Required("Please enter your Username.")])
  password = PasswordField("Password", [validators.Required("Please enter your password")])
  submit = SubmitField("Submit")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(username = self.username.data).first()
    if user:
      self.username.errors.append("That username is already taken")
      return False
    else:
      return True
