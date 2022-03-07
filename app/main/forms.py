from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):

    search = StringField('Search', validators=[Required()])
    # submit = SubmitField('Submit')