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