from flask_uploads import IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import BooleanField, PasswordField, StringField, TextAreaField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    name = StringField('Full name', validators=[
        InputRequired('A full name is required.'),
        Length(max=100, message='Your name can\'t be more than 100 characters.')])
    username = StringField('Username', validators=[
        InputRequired('Username is required.'),
        Length(max=30, message='Your username has too many characters.')])
    password = PasswordField('Password', validators=[
                             InputRequired('A password is required.')])
    image = FileField(validators=[FileAllowed(
        IMAGES, 'Only images are accepted.')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired('Username is required.'),
        Length(max=30, message='Your username is too many characters.')])
    password = PasswordField('Password', validators=[
                             InputRequired('A password is required.')])
    remember = BooleanField('Remember me')


class TweetForm(FlaskForm):
    text = TextAreaField('Message', validators=[
                         InputRequired('Message is required.')])
