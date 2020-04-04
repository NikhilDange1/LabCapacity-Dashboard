from flask import Flask, render_template, url_for,flash,redirect,request
from labcapacity.forms import RegistrationForm,LoginForm,DataEntryForm
from labcapacity.models import Users, Labs, Update
from labcapacity import app, db, bcrypt, geolocator
from flask_login import login_user, current_user, logout_user, login_required

def get_coord(street,city,state,zipcode):
    
    address =street+', '+city +', '+state+''+zipcode
    
    location = geolocator.geocode(address,exactly_one=True,country_codes='us')
    
    #IF address is not accurate geocode returns nearest accurate address without lat or lon. 
    # In that case query the lat and long again with accurate address
    if  not hasattr(location,'latitude'):
        location = geolocator.geocode(location,exactly_one=True,country_codes='us')

    return location.latitude , location.longitude

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

        street = form.lab_street.data
        city = form.lab_city.data
        state = form.lab_state.data
        zipcode = form.lab_zip.data

        lat,lon=get_coord(street,city,state,zipcode)
        
        lab = Labs(Name=form.labname.data,Street=street,City=city,Zip=zipcode,State=state,Lat=lat,Long=lon)

        user = Users(Email=form.email.data,Password=hashed,lab=lab)
        db.session.add(user)
        db.session.commit()
        

        flash(f'Account Created for {form.labname.data}!',category='success')
        return redirect(url_for('login'))
    return  render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
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