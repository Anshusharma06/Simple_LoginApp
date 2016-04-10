#Simple Login App

A simple login application in flask.

##Setup:

To get the project's source code, clone the github repository:

    $ git clone https://github.com/satwik77/Simple_LoginApp.git

Install VirtualEnv using the following:

    $ sudo pip install virtualenv

Create your virtual environment in the root directory of the project:

    $ cd rumal
    $ virtualenv flask

Install the following packages:

    $ flask/bin/pip install flask
    $ flask/bin/pip install flask-login
    $ flask/bin/pip install flask-sqlalchemy
    $ flask/bin/pip install sqlalchemy-migrate
    $ flask/bin/pip install flask-wtf

Enter the following commands to create your database:

    $ chmod a+x db_create.py
    $ ./db_create.py

Enter the following command to for your first migration:

    $ chmod a+x db_migrate.py
    $ ./db_migrate.py

To run your server, enter the following commands:

    $ chmod a+x run.py
    $ ./run.py

The default port is 5000

To run unit tests, enter the following commands:

    $ chmod a+x test_login_app.py
    $ ./test_login_app.py


##Usage and Description

To get to the landing/index page, enter the url 'localhost:5000/' in your browser. Click on register button to register as a new user, then enter your new username or password. Entering an already existing username is not allowed and will respond with an error message. Once you register, you are logged in and redirected to the dashboard page. You will have to click on the logout button on the page to logout and register as a new user or login as an existing one. While you are logged in you cannot go to the login or index page, it will redirect you to the dashboard page.

    
