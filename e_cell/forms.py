from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,IntegerField
from wtforms.validators import DataRequired,Length,Email,ValidationError,URL
from e_cell.models import StartUp

class Startup_Registration(FlaskForm):
    startup_name = StringField('Startup Name',validators=[DataRequired(),Length(min=4,max=30)])
    poc_name = StringField('Point of contact Name',validators=[DataRequired(),Length(min=4,max=30)])
    poc_email=StringField('Point of contact email',validators=[DataRequired(),Email()])
    poc_phone_no = IntegerField('Point of contact Phone no',validators=[DataRequired()])
    profile_doc = FileField('Profile_doc')
    incentive = StringField('Incentive',validators=[DataRequired(),Length(min=4,max=30)])
    duration= StringField('Duration',validators=[DataRequired(),Length(min=4,max=30)])
    website=StringField('Website',validators=[URL()])
    submit=SubmitField('Submit')

    #the following functions make sure that the startup name or startup website is not registered twice
    def validate_startup_name(self,startup_name):
            name=StartUp.query.filter_by(startup_name=startup_name.data).first()
            if name:
                raise ValidationError("The name of startup already choosen. Select different one!")
    
    def validate_website(self,website):
            name=StartUp.query.filter_by(website=website.data).first()
            if name:
                raise ValidationError("The website choosen by different startup. Select different one!")

        