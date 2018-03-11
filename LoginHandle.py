"""
*   Module Name: LoginHandle
*   Module Purpose: To handle all functions related to user login
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ConfigHandle import Config
from LogHandle import Logger, LogLevel

app = Flask(__name__)
log_inst = Logger("LoginHandle.txt")

def TokenVerification(token):
    if(token == '123'):
        return True
    else:
        return False

def StudentLogin(req_data):
    pass

def TutorLogin(req_data):
    pass

def GenerateToken(entity):
    pass

