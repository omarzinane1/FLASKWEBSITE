from website import create_app,  create_database, db
from flask_login import LoginManager

from website.models import User


app = create_app()
create_database(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    user = User.query.get(int(id))
    print(f'Chargement de l\'utilisateur : {user}')
    return user

if __name__ == '__main__':
    app.run(debug = True)
