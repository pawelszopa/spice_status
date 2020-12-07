from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from ..models.user_models import User


class LoginForm(FlaskForm):
    username = StringField('Your username:', validators=[DataRequired()])
    password = PasswordField('Your password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    username = StringField('Your username:', validators=[DataRequired(), Length(3, 80)])
    email = StringField('Your email:', validators=[DataRequired(), Length(5, 120), Email()])
    password = PasswordField('Your password:',
                             validators=[DataRequired(), EqualTo('password_2', message='Password mast much.')])
    password_2 = PasswordField('Repeat your password', validators=[])
    submit = SubmitField('SignUp')

    @staticmethod
    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('User already exist.')

    @staticmethod
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError("email already taken")