
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

from website.models import User, Note

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login(): 
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged seuccessfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password ! try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('firstname')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exist',category='error')
        elif not name or not password or not password2:
            flash('Veuillez remplir tous les champs.', category='error')
        elif len(name) < 2:
            flash('Le nom doit contenir au moins 2 caractères.', category='error')
        elif len(password) < 7:
            flash('Le mot de passe doit contenir au moins 7 caractères.', category='error')
        elif password != password2:
            flash('Les mots de passe ne correspondent pas.', category='error')
        else:
            # Ajouter l'utilisateur
            new_user = User(email = email, name = name, password = generate_password_hash(password, method='pbkdf2:sha256')
)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Inscription réussie !', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)  # ou le nom de ton template

    

    