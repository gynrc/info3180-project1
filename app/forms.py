from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import NumberRange, InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    num_bedrooms = IntegerField('Number of bedrooms', validators=[InputRequired(), NumberRange(min=1)])
    num_bathrooms = IntegerField('Number of bathrooms', validators=[InputRequired(), NumberRange(min=1)])
    location = StringField('Location', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired(), NumberRange(min=1)])
    type = SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[InputRequired()])