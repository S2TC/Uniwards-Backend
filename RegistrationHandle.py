"""
*   Module Name: LogHandle
*   Module Purpose: To handle all functions related to user registration
"""

from flask_sqlalchemy import SQLAlchemy
from ConfigHandle import Config
from LogHandle import Logger, LogLevel
import ResponseHandle, SQLHandle
from dateutil import parser
from itsdangerous import URLSafeSerializer
from flask import Flask
from flask_mail import Mail, Message
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'root'
app.config['MAIL_USERNAME'] = 'Un1w4r65321!&'
app.config['SECRET_KEY'] = '*EtG*J 8);lJzP`HF}S5_v>aFLHX6D>qu)~&q5xF+rY{Fqixz,5A#h]M`Q%?+?gG'
app.config['SECURITY_PASSWORD_SALT'] = 'Q?DLx(M-)8er&cbx*|ZJTNAjNt{rm69-g?yc%U=dNsho8QG6Z~twkM`^GU(]+EJA'
log_inst = Logger("RegistrationHandle.txt")


def RegisterStudent(req_data):
    #try:
        temp_student_username = SQLHandle.student.query.filter_by(username=req_data['username']).first()
        temp_student_email = SQLHandle.student.query.filter_by(email=req_data['email']).first()
        response = None
        if(temp_student_email is not None):
            response = ResponseHandle.GenerateResponse('registration_email_already_registered')
        elif(temp_student_username is not None):
            response = ResponseHandle.GenerateResponse('registration_username_already_registered')
        else:
            parsed_bd = parser.parse(req_data['birth'])
            uni_id = (int)(req_data['uni_id'])
            st_type = (int)(req_data['type'])
            hashed_password = HashPass(req_data['password'])
            print hashed_password
            new_student = SQLHandle.student(fname=req_data['fname'], lname=req_data['lname'], mobile_no=req_data['mobile_no'],
                                            username=req_data['username'], password=hashed_password, birth=parsed_bd, type=st_type,
                                            email=req_data['email'], auth_status=0, uni_id=uni_id)

            if(SQLHandle.InsertRowObject(new_student)):
                response = ResponseHandle.GenerateResponse('registration_successful')
                log_inst.Log("Registered new student: %s" % (req_data['username']), LogLevel.DEBUG)
                st_test = SQLHandle.student.query.filter_by(username=req_data['username']).first()
                print(st_test.__dict__)
                auth_token = GenerateEmailAuth(req_data['email'])
                SendAuthEmail(req_data['email'], auth_token)
            else:
                response = ResponseHandle.GenerateResponse('registration_failed')

        return response
    #except Exception as error:
        log_inst.Log(error, LogLevel.ERROR)
        return ResponseHandle.GenerateResponse('registration_failed')

def HashPass(password):
    return pbkdf2_sha256.hash(password)


def GenerateEmailAuth(email):
    serializer = URLSafeSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def DecryptEmailAuth(token):
    serializer = URLSafeSerializer(app.config['SECRET_KEY'])
    return serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'])

def VerifyStudentEmailAuth(token):
    email = DecryptEmailAuth(token)
    temp_student = SQLHandle.student.query.filter_by(email=email).first()
    if(temp_student is not None):
        if(temp_student.auth_status is 0):
            temp_student.auth_status = 1
            SQLHandle.CommitSession()
            return True
        else:
            return False
    else:
        return False

def SendAuthEmail(email, auth_token):
    url_str = "uniwards.xyz/api/auth_user/%s" % (auth_token)
    msg = Message("Confirmation", sender=("Uniwards", "confirmation@uniwards.xyz"), recipients=[email])
    msg.html = """<h1>Thank you for registering with Uniwards!</h1>
                  <p>Below is your confirmation link, please click it to finalize the registration process!</p>
                  <a href="%s"> Click to Confirm</a>
                  <br>
                  <p>Good Luck!</p>""" % (url_str)
    mail.send(msg)

def CheckRegistrationStatus():
    pass
