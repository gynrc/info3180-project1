from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import NumberRange, InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    num_bedrooms = IntegerField('No. of bedrooms', validators=[InputRequired(), NumberRange(min=1)])
    num_bathrooms = IntegerField('No. of bathrooms', validators=[InputRequired(), NumberRange(min=1)])
    location = StringField('Location', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired(), NumberRange(min=1)])
    type = SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])