"""
*   Module Name: LogHandle
*   Module Purpose: To handle all functions related to user registration
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ConfigHandle import Config
from LogHandle import Logger, LogLevel

app = Flask(__name__)
log_inst = Logger("RegistrationHandle.txt")

def RegisterUser(email, username, password):
    pass