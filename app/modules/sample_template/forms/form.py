from flask.ext.wtf import Form
from wtforms import TextAreaField, TextField, BooleanField, validators, ValidationError
from wtforms.validators import Required


class FormDatas(Form):
    field1 = TextField('field1', [validators.Required('Please enter the required data')])
    field2 = TextAreaField('field2', default='danger zone')
    field3 = TextAreaField('field3', default='yuuuuuuuuup')
