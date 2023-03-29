from flask_wtf import FlaskForm             
from wtforms import StringField, BooleanField, TextAreaField, IntegerField  
from wtforms.validators import DataRequired 



class HomelibraryForm(FlaskForm):  
    done = BooleanField('Прочитаєш?', validators=[DataRequired()])
    title    = StringField('Напиши назву', validators=[DataRequired()])
    description = TextAreaField('Стерти', validators=[DataRequired()])
    
