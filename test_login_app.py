#!flask/bin/python

# Author: Satwik Bhattamishra <ronu66@gmail.com>
# Task for Honeynet Organization


import os
import unittest

from config import basedir
from login_app import login_app, db
from login_app.models import User
from flask import url_for
from login_app.views import *

class TestCase(unittest.TestCase):

    def setUp(self):
        login_app.config['TESTING'] = True
        login_app.config['WTF_CSRF_ENABLED'] = False
        login_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.login_app = login_app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()




    def register(self, username, password):
        return self.login_app.post('/register/', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)


    def logout(self):
        return self.login_app.get('/logout/', follow_redirects=True)        


    def login(self, username, password):
        return self.login_app.post('/login/', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)




    def test_index(self):
        result= self.login_app.get('/')
        assert result.status_code == 200


    def test_register_logout(self):
        test_data = self.register('test_username', 'test_password')
        assert 'test_username' in test_data.data

        result = self.logout()
        assert result.status_code == 200


    def test_login_logout(self):
        test_data = self.login('test_username', 'test_password')
        assert 'test_username' in test_data.data

        result = self.logout()
        assert result.status_code == 200

        test_data = self.login('test', 'test_password')
        assert 'Invalid Username or Password' in test_data.data

        test_data = self.login('test_username', 'test')
        assert 'Invalid Username or Password' in test_data.data



if __name__ == '__main__':
    unittest.main()