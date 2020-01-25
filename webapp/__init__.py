from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate
from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.upload.views import blueprint as upload_blueprint
from webapp.biblio.book.views import blueprint as book_blueprint
from webapp.download.views import blueprint as download_blueprint

# set FLASK_APP=webapp&&set FLASK_env=development&&set FLASK_DEBUG=1&&FLASK run

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate (app, db)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(upload_blueprint)
    app.register_blueprint(book_blueprint)
    app.register_blueprint(download_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
