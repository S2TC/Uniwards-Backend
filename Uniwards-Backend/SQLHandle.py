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


def CreateTables():
    #app.config["SQLALCHEMY_DATABASE_URI"] = Config.conf[
        #"DatabaseURI"]  # 'mysql+mysqlconnector://root:ThreeCupsOfCoffee123!@@localhost/Uniwards'
    db.create_all()
    log_inst.Log("Created Tables!", LogLevel.DEBUG)


def InsertRowObject(obj):
    db.session.add(obj)
    CommitSession()
    log_inst.Log("Inserted Row Obj", LogLevel.DEBUG)


def DeleteRowObject(obj):
    db.session.delete(obj)
    CommitSession()
    log_inst.Log("Deleted Row Obj", LogLevel.DEBUG)


def CommitSession():
    db.session.commit()
    log_inst.Log("Committed to DB!", LogLevel.DEBUG)


class Class(db.Model):
    CL_ID = db.Column(db.Integer, primary_key=True)
    CL_NAME = db.Column(db.String(20))
    T_ID = db.Column(db.Integer, db.ForeignKey('tutor.T_ID'))
    UNI_ID = db.Column(db.Integer, db.ForeignKey('university.UNI_ID'))


    def __init__(self, id, name, tutor_id, uni_id):
        self.id = id
        self.name = name
        self.tutor_id = tutor_id
        self.uni_id = uni_id


class Tutor(db.Model):
    T_ID = db.Column(db.Integer, primary_key=True)
    T_FNAME = db.Column(db.String(50))
    T_LNAME = db.Column(db.String(50))
    T_MOBILE = db.Column(db.String(50))
    T_USERNAME = db.Column(db.String(12))
    T_PASSWORD = db.Column(db.String(12))
    T_EMAIL = db.Column(db.String(50))
    UNI_ID = db.Column(db.Integer, db.ForeignKey('university.UNI_ID'))


    def __init__(self, id, fname, lname, mobile, username, password, email, uni_id):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.mobile = mobile
        self.username = username
        self.password = password
        self.email = email
        self.uni_id = uni_id


class Reward(db.Model):
    R_ID = db.Column(db.Integer, primary_key=True)
    R_NAME = db.Column(db.Integer)
    R_VALUE = db.Column(db.Integer)
    R_REQUIREMENT = db.Column(db.String(50))
    R_TYPE = db.Column(db.Integer)
    R_TIER = db.Column(db.Integer)
    R_DESC = db.Column(db.String(200))


    def __init__(self, id, name, value, requirement, type, tier, desc):
        self.id = id
        self.name = name
        self.value = value
        self.requirement = requirement
        self.type = type
        self.tier = tier
        self.desc = desc


class Coupon(db.Model):
    C_ID = db.Column(db.Integer, primary_key=True)
    C_NAME = db.Column(db.String(50))
    C_CODE = db.Column(db.Integer)
    C_EXPIRY = db.Column(db.DateTime)
    C_DESC = db.Column(db.String(50))
    C_POINTCOST = db.Column(db.Integer)
    V_ID = db.Column(db.Integer, db.ForeignKey('vendor.V_ID'))


    def __init__(self, id, name, code, expiry, desc, point_cost, vendor_id):
        self.id = id
        self.name = name
        self.code = code
        self.expiry = expiry
        self.desc = desc
        self.point_cost = point_cost
        self.vendor_id = vendor_id


class Vendor(db.Model):
    V_ID = db.Column(db.Integer, primary_key=True)
    V_NAME = db.Column(db.String(50))
    V_MOBILE = db.Column(db.String(50))
    V_WEBSITE = db.Column(db.String(50))
    V_TYPE = db.Column(db.Integer)
    V_EMAIL = db.Column(db.String(50))


    def __init__(self, id, name, mobile, website, type, email):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.website = website
        self.type = type
        self.email = email


class Redemption(db.Model):
    RDM_ID = db.Column(db.Integer, primary_key=True)
    RDM_DATE = db.Column(db.DateTime)
    ST_ID = db.Column(db.Integer, db.ForeignKey('student.ST_ID'))
    C_ID = db.Column(db.Integer, db.ForeignKey('coupon.C_ID'))


    def __init__(self, id, date, student_id, coupon_id):
        self.id = id
        self.date = date
        self.student_id = student_id
        self.coupon_id = coupon_id


class Point(db.Model):
    ST_ID = db.Column(db.Integer, db.ForeignKey('student.ST_ID'), primary_key=True)
    R_ID = db.Column(db.Integer, db.ForeignKey('reward.R_ID'), primary_key=True)
    T_ID = db.Column(db.Integer, db.ForeignKey('tutor.T_ID'), primary_key=True)
    P_DATE = db.Column(db.DateTime, primary_key=True)


    def __init__(self, student_id, reward_id, tutor_id, date):
        self.student_id = student_id
        self.reward_id = reward_id
        self.tutor_id = tutor_id
        self.date = date


class University(db.Model):
    UNI_ID = db.Column(db.Integer, primary_key=True)
    UNI_NAME = db.Column(db.String(50))
    UNI_ADDRESS = db.Column(db.String(50))
    UNI_MOBILE = db.Column(db.String(50))


    def __init__(self, id, name, address, mobile_no):
        self.id = id
        self.name = name
        self.address = address
        self.mobile_no = mobile_no


class Student(db.Model):
    ST_ID = db.Column(db.Integer, primary_key=True)
    ST_FNAME = db.Column(db.String(50))
    ST_LNAME = db.Column(db.String(50))
    ST_MOBILE = db.Column(db.String(50))
    ST_USERNAME = db.Column(db.String(12))
    ST_PASSWORD = db.Column(db.String(12))
    ST_BIRTH = db.Column(db.DateTime)
    ST_TYPE = db.Column(db.Integer)
    ST_EMAIL = db.Column(db.String(50))
    UNI_ID = db.Column(db.Integer, db.ForeignKey('university.UNI_ID'))


    def __init__(self, id, fname, lname, mobile_no, username, password, birth, type, email, uni_id):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.mobile_no = mobile_no
        self.username = username
        self.password = password
        self.birth = birth
        self.type = type
        self.email = email
        self.uni_id = uni_id


class Enrolled(db.Model):
    CL_ID = db.Column(db.Integer, db.ForeignKey('class.CL_ID'), primary_key=True)
    ST_ID = db.Column(db.Integer, db.ForeignKey('student.ST_ID'), primary_key=True)
    EN_DATE = db.Column(db.DateTime)


    def __init__(self, cl_id, st_id, date):
        self.cl_id = cl_id
        self.st_id = st_id
        self.date = date


class Beacon(db.Model):
    T_ID = db.Column(db.Integer, db.ForeignKey('tutor.T_ID'), primary_key=True)
    CL_ID = db.Column(db.Integer, db.ForeignKey('class.CL_ID'), primary_key=True)
    B_LONGITUDE = db.Column(db.Integer)
    B_LATITUDE = db.Column(db.Integer)
    B_DATETIME = db.Column(db.DateTime)


    def __init__(self, t_id, cl_id, longitude, latitude, datetime):
        self.t_id = t_id
        self.cl_id = cl_id
        self.longitude = longitude
        self.latitude = latitude
        self.datetime = datetime