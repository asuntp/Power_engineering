import os
from flask import flash, redirect, url_for, request, send_from_directory, Blueprint
from werkzeug.utils import secure_filename
from flask_login import login_required

blueprint = Blueprint('upload', __name__, url_prefix='/')



basedir_downloads = os.path.abspath(os.path.dirname(__name__))
ALLOWED_EXTENSIONS = set(['djvu', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('biblio.book.book'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('biblio.book.book'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir_downloads, filename))

            return redirect(url_for('upload.uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@blueprint.route('/uploaded/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory(os.path.join(basedir_downloads), filename)
