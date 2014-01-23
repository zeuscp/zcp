from flask.ext.wtf import Form
from wtforms import TextAreaField, TextField, BooleanField, validators, ValidationError, SelectMultipleField, widgets
from wtforms.validators import Required

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class LAMP(Form):
    lamp = {"basic_lamp": [('httpd', 'httpd'),
                           ('mysql-server', 'mysql-server'),
                           ('mysql-client', 'mysql-client'),
                           ('php', 'php')
                           ]
            }

    for l in lamp:
        l = MultiCheckboxField(l, choices=lamp[l])
