from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    content = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Post the pitch')