from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login(): 
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('firstname')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not name or not password or not password2:
            flash('Veuillez remplir tous les champs.', category='error')
        elif len(name) < 2:
            flash('Le nom doit contenir au moins 2 caractères.', category='error')
        elif len(password) < 7:
            flash('Le mot de passe doit contenir au moins 7 caractères.', category='error')
        elif password != password2:
            flash('Les mots de passe ne correspondent pas.', category='error')
        else:
            # Ajouter l'utilisateur ici
            flash('Inscription réussie !', category='success')

    return render_template('sign_up.html')  # ou le nom de ton template

    

    