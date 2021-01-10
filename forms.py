from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Password, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField(
        'Username', 
        validators=[DataRequired(), Length(min=5, max=20)],
        )

    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=5, max=20)]
    )

    confirm_password = PasswordField(
        'Confirm password',
        validators=[DataRequired(), Length(min=5, max=20), EqualTo('password')]
    )

    submit = SubmitField('Sign Up')

