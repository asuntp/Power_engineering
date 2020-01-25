from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], render_kw={'class': 'form-control',
                                                                       'placeholder': 'Имя пользователя, номер '
                                                                                      'телефона или mail'})
    password = PasswordField('', validators=[DataRequired()],
                             render_kw={'class': 'form-control', 'placeholder': 'Пароль'})
    submit = SubmitField('Войти', render_kw={'type': 'submit', 'class': 'btn btn-secondary'})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
