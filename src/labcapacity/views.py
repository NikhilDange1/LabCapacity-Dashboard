from flask import Flask, render_template, url_for,flash,redirect
from labcapacity.forms import RegistrationForm,LoginForm
from labcapacity import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.labname.data}!',category='success')
        return redirect(url_for('home'))
    return  render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html",title='Login',form=form)