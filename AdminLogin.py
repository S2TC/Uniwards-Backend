from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '*EtG*J 8);lJzP`HF}S5_v>aFLHX6D>qu)~&q5xF+rY{Fqixz,5A#h]M`Q%?+?gG'

class LoginForm(Form):
    username = TextField('Name:', validators=[validators.required()])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

def hello(request):
    form = LoginForm(request.form)

    print form.errors
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

    return render_template('AdminLogin.html', form=form)
