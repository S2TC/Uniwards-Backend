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

def TokenValidation(token, username):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        if(username is payload['sub']):
            return ResponseHandle.GenerateResponse('token_valid')
        else:
            return ResponseHandle.GenerateResponse('token_bad')
    except jwt.ExpiredSignature:
        return ResponseHandle.GenerateResponse('token_expired')
    except jwt.InvalidTokenError:
        return ResponseHandle.GenerateResponse('token_bad')

#Decode token & check if expired/invalid
def TokenVerification(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        return payload['sub']
    except jwt.ExpiredSignature:
        return 'Expired'
    except jwt.InvalidTokenError:
        return 'Invalid'

def TokenCheckStub(raw_token):
    token = TokenVerification(raw_token)
    if (token is not 'Expired' or token is not 'Invalid'):
        response = ResponseHandle.GenerateResponse('token_verified')
    elif (token == 'Invalid'):
        response = ResponseHandle.GenerateResponse('token_bad')
    elif (token == 'Expired'):
        response = ResponseHandle.GenerateResponse('token_expired')
    else:
        response = ResponseHandle.GenerateResponse('token_bad')

    return response

#Check if a student with the username exists, and if the passwords match
def StudentLogin(req_data):
    temp_student = SQLHandle.student.query.filter_by(username=req_data['username']).first()
    response = None
    token = None
    if(temp_student is not None):
        if(VerifyPassword(req_data['password'], temp_student.password)):
            token = GenerateToken(temp_student.username)
            response = ResponseHandle.GenerateTokenResponse('login_success', token)
        else:
            response = ResponseHandle.GenerateTokenResponse('login_incorrect_password', "")
    else:
        response = ResponseHandle.GenerateTokenResponse('login_nonexistant_user', "")

    return response

def TutorLogin(req_data):
    pass

#Compare plaintext password to hashed password
def VerifyPassword(password, hashed_pass):
    if(pbkdf2_sha256.verify(password, hashed_pass)):
        return True
    else:
        return False

#Generate the JWT based on username, expires in 7 days
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

