from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo
from labcapacity.models import Users

class RegistrationForm(FlaskForm):
    #email field
    email =StringField('Email',validators=[DataRequired(),Email()])

    #lab association
    lablist = ['Lab A', 'Lab B', 'Lab C'] #replace with call to db for active list
    lablist.append('Lab Not Listed') #add value for new fields to be queued
    labs = []
    for ea in lablist:
        labs.append((ea, ea))
    labname = SelectField('Lab you represent:', choices =  labs)

    #password
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self,email):

        user = Users.query.filter_by(Email=email.data).first()

        if user:
            raise ValidationError('Email already exits!')

class LabRegistration(FlaskForm):
    #lab detials
    labname = StringField('Lab Name',validators=[DataRequired(),Length(min=2,max=15)])
    lab_street = StringField('Street',validators=[DataRequired()])
    lab_city = StringField('City',validators=[DataRequired()])
    lab_zip = StringField('Zip',validators=[DataRequired()])
    lab_state = StringField('State',validators=[DataRequired()])
    submit = SubmitField('Register Lab')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField()
    submit = SubmitField('Login')


class DataEntryForm(FlaskForm):
    lab_capacity = IntegerField('Lab Capacity For today')
    current = IntegerField('Current Tests Being Processed',validators=[DataRequired()])
    submit  = SubmitField('Update')
