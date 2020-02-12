from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import EqualTo, Email, DataRequired


class UserRegistrationForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField("Confirm Password:", validators=[DataRequired()])
    submit = SubmitField("SignUp")


class UserLoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Login")


class TheaterCreationForm(FlaskForm):
    # Theater Name
    # No Of Screens
    # Screen Capacity
    # No Of shows
    # When The Theater Is Created movies Will Be Null[]
    theatername = StringField("Theater Name:", validators=[DataRequired()])
    noofscreens = IntegerField("No Of Screens:", validators=[DataRequired()])
    screencapacity = IntegerField("Screen Capacity:", validators=[DataRequired()])
    noofshows = IntegerField("No Of Shows:", validators=[DataRequired()])
    submit = SubmitField("Submit")


class MovieForm(FlaskForm):
    theatername = StringField("Theater Name:", validators=[DataRequired()])
    moviename = StringField("Movie Name:", validators=[DataRequired()])
    submit = SubmitField("Submit")


