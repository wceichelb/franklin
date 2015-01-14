from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class ENEditForm(Form):
    content = TextField('New Task')
