
from flask import send_file, Blueprint
from flask_login import login_required

blueprint = Blueprint('download', __name__, url_prefix='/download')





@blueprint.route('/Bootstrap4')
@login_required
def bootstrap4():
    return send_file('C:/Users/asunt/PycharmProjects/untitled2/Luba_project/webapp/static/bootstrap4.pdf', attachment_filename='Bootstrap4.pdf')


@blueprint.route('/Flask_web_eng')
@login_required
def flask_eng():
    return send_file('C:/Users/asunt/PycharmProjects/untitled2/Luba_project/webapp/static/Flask_web_eng.pdf', attachment_filename='Flask_web_eng.pdf')


@blueprint.route('/A_Byte_of_Python')
@login_required
def a_byte_of_python():
    return send_file('C:/Users/asunt/PycharmProjects/untitled2/Luba_project/webapp/static/AByteofPython.pdf', attachment_filename='AByteofPython.pdf')
