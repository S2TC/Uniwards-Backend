"""
*   Module Name: LoginHandle
*   Module Purpose: To handle all functions related to user login
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ConfigHandle import Config
from LogHandle import Logger, LogLevel
from passlib.hash import pbkdf2_sha256
import SQLHandle
import ResponseHandle
import datetime
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = '*EtG*J 8);lJzP`HF}S5_v>aFLHX6D>qu)~&q5xF+rY{Fqixz,5A#h]M`Q%?+?gG'
log_inst = Logger("LoginHandle.txt")

def TokenVerification(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        return payload['sub']
    except jwt.ExpiredSignature:
        return 'Expired'
    except jwt.InvalidTokenError:
        return 'Invalid'

def TokenCheckStub(token):
    token = TokenVerification(token)
    if (token == 1):
        response = 1
    elif (token == 'Invalid'):
        response = ResponseHandle.GenerateResponse('bad_token')
    elif (token == 'Expired'):
        response = ResponseHandle.GenerateResponse('expired_token')
    else:
        response = ResponseHandle.GenerateResponse('bad_token')

    return response
def StudentLogin(req_data):
    temp_student = SQLHandle.student.query.filter_by(username=req_data['username']).first()
    response = None
    token = None
    if(temp_student is not None):
        if(VerifyPassword(req_data['password'], temp_student.password)):
            response = ResponseHandle.GenerateResponse('login_success')
            token = GenerateToken(temp_student.username)
        else:
            response = ResponseHandle.GenerateResponse('login_incorrect_password')
    else:
        response = ResponseHandle.GenerateResponse('login_nonexistant_user')

    return response

def TutorLogin(req_data):
    pass

def VerifyPassword(password, hashed_pass):
    if(pbkdf2_sha256.verify(password, hashed_pass)):
        return True
    else:
        return False

def GenerateToken(username):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }

        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    except Exception as e:
        print(e)

