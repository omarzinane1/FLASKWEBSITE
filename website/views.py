from datetime import date
from  flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from website.models import Note
from . import db
import json

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

@views.route('/delete-note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        flash("Note supprimée avec succès.", category='success')
    else:
        flash("Suppression non autorisée.", category='error')
    return redirect(url_for('views.home'))



    
    
