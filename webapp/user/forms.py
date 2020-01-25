from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, RadioField
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


class RegistrationForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], render_kw={'class': 'form-control',
                                                                       'placeholder': 'Имя пользователя'})
    mail = StringField('', validators=[DataRequired(), Email()], render_kw={'class': 'form-control',
                                                                   'placeholder': 'email'})

    first_name = StringField('', validators=[], render_kw={'class': 'form-control',
                                                           'placeholder': 'Имя'})
    second_name = StringField('', validators=[], render_kw={'class': 'form-control',
                                                            'placeholder': 'Фамилия'})
    father_name = StringField('', validators=[], render_kw={'class': 'form-control',
                                                            'placeholder': 'Отчество'})
    phone_number = StringField('', validators=[], render_kw={'class': 'form-control',
                                                                           'placeholder': 'Номер телефона'})
    organisation = StringField('', validators=[], render_kw={'class': 'form-control',
                                                             'placeholder': 'Организация'})
    password1 = PasswordField('', validators=[DataRequired(), EqualTo('password2', message='Passwords not match')],
                              render_kw={'class': 'form-control', 'placeholder': 'Пароль'})
    password2 = PasswordField('', validators=[DataRequired()],
                              render_kw={'class': 'form-control', 'placeholder': 'Повторите пароль'})
    role = RadioField('Читатель', choices=["Читатель", "Расчетчик", "Эксперт"], render_kw={'type': 'form-radio',
                                                                                           'class': 'custom-control-input'})
    submit = SubmitField('Отправить', render_kw={'type': 'submit', 'class': 'btn btn-secondary'})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с таким именем уже существует')

    def validate_mail(self, mail):
        mail_count = User.query.filter_by(mail=mail.data).count()
        if mail_count > 0:
            raise ValidationError('Пользователь с таким email уже существует')