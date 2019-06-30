from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class DiacForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired(), Length(max=500)])
    dialect = SelectField('Select version of Arabic', choices=[
        ('ca', 'Classical Arabic'),
        ('msa', 'Modern Standard Arabic'),
        ('tun', 'Tunisian Dialect'),
        ('mor', 'Moroccan Dialect')
    ])
    submit = SubmitField(' Restore Diacritics')
