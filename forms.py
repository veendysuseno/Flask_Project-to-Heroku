from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('Whats is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class PuppiesForm(FlaskForm):
    name = StringField('Puppies name?', validators=[Required()])
    age = IntegerField('age?', validators=[Required()])
    breed = StringField('Breed?', validators=[Required()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    submit = SubmitField('Submit')