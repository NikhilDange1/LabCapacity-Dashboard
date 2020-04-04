from labcapacity import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model,UserMixin):
    UserID = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String(50),unique=True,nullable=False)
    Password= db.Column(db.String(50),unique=True,nullable=False)
    LabID  = db.Column(db.Integer,db.ForeignKey('labs.LabID'),nullable=False)
    lab = db.relationship('Labs',backref='name',lazy=True)

    def get_id(self):
           return (self.UserID)

    def __repr__(self):
        return f"User('{self.UserID}','{self.Email}','{self.LabID})"


class Labs(db.Model):
    LabID = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(50),nullable=False)
    Street= db.Column(db.String(50),nullable=False)
    City= db.Column(db.String(50),nullable=False)
    State= db.Column(db.String(50),nullable=False)
    Zip = db.Column(db.String(10),nullable=False)
    Lat  = db.Column(db.Float,nullable=False)
    Long = db.Column(db.Float,nullable=False)

    def __repr__(self):
        return f"Labs('{self.LabID}','{self.Name}','{self.Zip}')"


class Update(db.Model):
    UpdateId = db.Column(db.Integer,primary_key=True)
    LabID  = db.Column(db.Integer,db.ForeignKey('labs.LabID'),nullable=False)
    Timestamp = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    PatientToTest = db.Column(db.Integer,nullable=False)
    TotalTests = db.Column(db.Integer,nullable=False)
    Availability = db.Column(db.Integer,nullable=False)
    lab = db.relationship('Labs',backref='lname',lazy=True)

    def __repr__(self):
        return f"Labs('{self.LabID}','{self.Timestamp}','{self.PatientToTest}','{self.TotalTests}',''{self.Availability}')"
