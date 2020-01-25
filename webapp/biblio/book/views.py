from flask import render_template, Blueprint
from flask_login import login_required

blueprint = Blueprint('book', __name__, url_prefix='/')



@blueprint.route('/books')
@login_required
def book():
    title = 'Электронная библиотека'
    return render_template('biblio/books/index.html', page_title=title)

