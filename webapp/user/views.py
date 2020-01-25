from .forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user
from flask import Blueprint, render_template, flash, redirect, url_for
from .models import User
from webapp.db import db

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route("/process-login", methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли в систему')
            return redirect(url_for('news.index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))
    flash('Вы вышли из системы')


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Регистрация"
    registration_form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=registration_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, mail=form.mail.data, role=form.role.data,
                        first_name=form.first_name.data, second_name=form.second_name.data,
                        father_name=form.father_name.data, phone_number=form.phone_number.data,
                        organisation=form.organisation.data)
        new_user.set_password(form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}:{}'.format(
                    getattr(form, field).label.text,
                    errors))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))
