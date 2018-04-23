"""
*   Module Name: SQLHandle
*   Module Purpose: To handle all functions related to the DB
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ConfigHandle import Config
from LogHandle import Logger, LogLevel


app = Flask(__name__)
log_inst = Logger("SQLHandle.txt")
db = SQLAlchemy(app)


def __init__(self):
    pass


#Create the tables specified in this file & commit
def CreateTables():
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.conf['DatabaseURI']
    db.drop_all()
    db.create_all()
    CommitSession()
    log_inst.Log("Created Tables!", LogLevel.DEBUG)

#Insert a single row obj into the DB & commit
def InsertRowObject(obj):
    try:
        db.session.add(obj)
        CommitSession()
        log_inst.Log("Inserted Row Obj: %s" % (obj), LogLevel.DEBUG)
        return True
    except error:
        log_inst.Log("Failed to insert Row Obj: %s" % (obj), LogLevel.ERROR)
        return False

#Delete a single row obj from the DB & commit
def DeleteRowObject(obj):
    try:
        db.session.delete(obj)
        CommitSession()
        log_inst.Log("Deleted Row Obj: %s" % (obj), LogLevel.DEBUG)
        return True
    except error:
        log_inst.Log("Failed to delete Row Obj: %s" % (obj), LogLevel.ERROR)
        return False

#Commit the current session to the DB
def CommitSession():
    db.session.commit()
    log_inst.Log("Committed to DB!", LogLevel.DEBUG)


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'))
    uni_id = db.Column(db.Integer, db.ForeignKey('university.id'))


    def __init__(self, name, tutor_id, uni_id):
        self.name = name
        self.tutor_id = tutor_id
        self.uni_id = uni_id


class tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    mobile = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text)
    uni_id = db.Column(db.Integer, db.ForeignKey('university.id'))


    def __init__(self, fname, lname, mobile, username, password, email, uni_id):
        self.fname = fname
        self.lname = lname
        self.mobile = mobile
        self.username = username
        self.password = password
        self.email = email
        self.uni_id = uni_id


class reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    value = db.Column(db.Integer)
    requirement = db.Column(db.Text)
    type = db.Column(db.Integer)
    tier = db.Column(db.Integer)
    desc = db.Column(db.Text)


    def __init__(self, name, value, requirement, type, tier, desc):
        self.name = name
        self.value = value
        self.requirement = requirement
        self.type = type
        self.tier = tier
        self.desc = desc


class coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    code = db.Column(db.Integer)
    expiry = db.Column(db.DateTime)
    desc = db.Column(db.Text)
    point_cost = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))


    def __init__(self, name, code, expiry, desc, point_cost, vendor_id):
        self.name = name
        self.code = code
        self.expiry = expiry
        self.desc = desc
        self.point_cost = point_cost
        self.vendor_id = vendor_id


class vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    mobile = db.Column(db.Text)
    website = db.Column(db.Text)
    type = db.Column(db.Integer)
    email = db.Column(db.Text)


    def __init__(self, name, mobile, website, type, email):
        self.name = name
        self.mobile = mobile
        self.website = website
        self.type = type
        self.email = email


class redemption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'))


    def __init__(self, date, student_id, coupon_id):
        self.date = date
        self.student_id = student_id
        self.coupon_id = coupon_id


class point(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    reward_id = db.Column(db.Integer, db.ForeignKey('reward.id'), primary_key=True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)


    def __init__(self, student_id, reward_id, tutor_id, date):
        self.student_id = student_id
        self.reward_id = reward_id
        self.tutor_id = tutor_id
        self.date = date


class university(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uni_code = db.Column(db.Text)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    mobile_no = db.Column(db.Text)


    def __init__(self, uni_code, name, address, mobile_no):
        self.uni_code = uni_code
        self.name = name
        self.address = address
        self.mobile_no = mobile_no


class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    mobile_no = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    birth = db.Column(db.DateTime)
    type = db.Column(db.Integer)
    email = db.Column(db.Text)
    auth_status = db.Column(db.Integer)
    uni_id = db.Column(db.Integer, db.ForeignKey('university.id'))

    def __init__(self, fname, lname, mobile_no, username, password, birth, type, email, auth_status, uni_id):
        self.fname = fname
        self.lname = lname
        self.mobile_no = mobile_no
        self.username = username
        self.password = password
        self.birth = birth
        self.type = type
        self.email = email
        self.auth_status = auth_status
        self.uni_id = uni_id


class enrolled(db.Model):
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    EN_DATE = db.Column(db.DateTime)


    def __init__(self, class_id, student_id, date):
        self.class_id = class_id
        self.student_id = student_id
        self.date = date


class beacon(db.Model):
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), primary_key=True)
    longitude = db.Column(db.Integer)
    latitude = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)


    def __init__(self, tutor_id, class_id, longitude, latitude, datetime):
        self.tutor_id = tutor_id
        self.class_id = class_id
        self.longitude = longitude
        self.latitude = latitude
        self.datetime = datetime