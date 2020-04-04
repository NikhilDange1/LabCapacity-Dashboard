from flask import Flask, render_template, url_for,flash,redirect,request
from labcapacity.forms import RegistrationForm,LoginForm,DataEntryForm
from labcapacity.models import Users, Labs, Update
from labcapacity import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

>>>>>>> Add user registration , user authentication and database


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')#hash password
        lab = Labs(Name=form.labname.data,Street=form.lab_street.data,City=form.lab_city.data,Zip=form.lab_zip.data,State=form.lab_state.data,Lat=41.40,Long=-75.66)

        user = Users(Email=form.email.data,Password=hashed,lab=lab)
        db.session.add(user)
        db.session.commit()
        

        flash(f'Account Created for {form.labname.data}!',category='success')
        return redirect(url_for('login'))
    return  render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
<<<<<<< 4cf5e4da5d12a417e749abc85fe6a032effc8ec7
    return render_template("login.html",title='Login',form=form)
=======
    if form.validate_on_submit():

        user = Users.query.filter_by(Email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.Password,form.password.data):
            login_user(user,form.remember_me.data)
            flash(f'Logged in as {form.email.data}!',category='success')
            next_page = request.args.get('next')

            return redirect(next_page) if not None else redirect(url_for('home'))

        else:
            flash(f'Invalid email or password',category='danger')
    return render_template("login.html",title='Login',form=form)


@app.route('/update',methods=['GET','POST'])
@login_required
def DataEntry():
    form  = DataEntryForm()
    if form.validate_on_submit():
        

        #get data from forms
        current = form.current.data
        total = form.lab_capacity.data
        ava = total-current #availability

        #get labid for current user
        lid = current_user.LabID
        
        #create update entity
        update  = Update(LabID=lid,PatientToTest=current,TotalTests=total,Availability=ava)
        
        #Add entity to db
        db.session.add(update)
        db.session.commit()

        return redirect(url_for('home'))
    
    
    return render_template("Update.html",title='Update data',form=form)
    
    #else:
    #    flash(f'Login to continue',category='info')
    #return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
>>>>>>> Add user registration , user authentication and database
