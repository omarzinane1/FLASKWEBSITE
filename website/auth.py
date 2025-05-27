from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>page login</p>'

@auth.route('/logout')
def logout():
    return '<p>logout page</p>'

@auth.route('/sign-up')
def  sign_up():
    return '<p>sign up page</p>'

    

    