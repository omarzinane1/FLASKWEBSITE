from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login(): 
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET','POST'])
def  sign_up():
    if request.method == 'POST':
        name = request.form.get('firstname')
        email = request.form.get('email')
        password = request.form.get('password')
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        elif len(password)<7:
            pass
        else:
            #user add
            pass

    return render_template('sign_up.html')

    

    