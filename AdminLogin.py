from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

def hello(request):
    form = ReusableForm(request.form)

    print form.errors
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        print name, " ", email, " ", password

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

    return render_template('AdminLogin.html', form=form)
