from  flask import Blueprint, flash, render_template, request
from flask_login import login_required, current_user
from website.models import Note
from . import db
views = Blueprint('views',__name__)
@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get("note")
        if len(note) < 1:
            flash('La note est vide !', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note ajoutée avec succès !', category='success')

    return render_template('home.html', user= current_user)
    
