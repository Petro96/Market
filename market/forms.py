
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    # check if theres user already exist

    def validate_username(self,username_to_check):

        #username_to_check -> <User> / user_to_check.data <User.userName>
        user = User.query.filter_by(userName=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Please try different username!")

    # validate email address
        
    def validate_email(self,email_to_check):

        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError("Email address already exists! Please try a different email address!")



    username = StringField(label='User Name:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = EmailField(label='Email Address:', validators=[Email(),DataRequired()], granular_message=True)

    password = PasswordField(label='Password:', validators=[Length(min=6),DataRequired()])
    password_confirmation = PasswordField(label='Confirm Password:', validators=[EqualTo('password'),DataRequired()])

    submit = SubmitField(label='Create Account')