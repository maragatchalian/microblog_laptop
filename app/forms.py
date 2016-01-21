from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


# Web forms are represented in Flast-WTF as classes, subclassed from base class Form
# A form subclass simply defines the fields of the form as class variables.
# L02
#   |--StringField: For the email/openID
#   |--BooleanField: For the 'Remember Me' (Yes or no)
#L03 DataRequired
#   |-- a validator, "This field should not remain empty!"