from flask import Flask, request
from ConfigHandle import Config
import SQLHandle, RegistrationHandle, LoginHandle, ResponseHandle
from LogHandle import Logger, LogLevel

app = Flask(__name__)
log_inst = Logger("Uniwards-Backend.txt")

@app.route('/api')
def hello_world():
    #AlwaysRun()
    return 'Hello World!'

#Authenticate email token to complete user registration
@app.route('/api/auth_user/<auth_token>')
def AuthUser(auth_token):
    if(RegistrationHandle.VerifyStudentEmailAuth(auth_token)):
        log_inst.Log("Verified email for: %s" % (RegistrationHandle.DecryptEmailAuth(auth_token)), LogLevel.DEBUG)
        response = ResponseHandle.GenerateResponse('email_auth_verified')
    else:
        log_inst.Log("Failed to verify email for: %s" % (RegistrationHandle.DecryptEmailAuth(auth_token)), LogLevel.DEBUG)
        response = ResponseHandle.GenerateResponse('email_auth_failed')

    return response[0], response[1]

@app.route('/api/validate_token/<token>/<username>')
def ValidateToken(token, username):
    response = LoginHandle.ValidateToken(token, username)
    print response
    return response[0], response[1]

#User Registration endpoint
@app.route('/api/registeruser', methods = ['POST'])
def RegisterUser():
    response = LoginHandle.TokenVerification(request.headers['Token'])
    print response
    if(response is not 'Valid' and response is not 'Expired'):
        log_inst.Log("Registering student: %s" % (request.form['username']), LogLevel.DEBUG)
        response = RegistrationHandle.RegisterStudent(request.form)
    else:
        log_inst.Log("Student already registered: %s" % (request.form['username']), LogLevel.DEBUG)
        response = ResponseHandle.GenerateResponse('registration_already_registered')

    return response[0], response[1]

#Student Login endpoint
@app.route('/api/studentlogin', methods = ['POST'])
def StudentLogin():
    log_inst.Log("Student attempting to login: %s" % (request.form['username']), LogLevel.DEBUG)
    response = LoginHandle.StudentLogin(request.form)
    if(response[0] == 'login_success'):
        log_inst.Log("Student login success: %s" % (request.form['username']), LogLevel.DEBUG)
    return response[0], response[1]

def TestFunc():
    uni = SQLHandle.university(1, "test", "test", "1234")
    SQLHandle.InsertRowObject(uni)
    uni2 = SQLHandle.university.query.all()
    print(uni2[0].mobile_no)
    pass

def AlwaysRun():
    RegistrationHandle.SendAuthEmail('test@uniwards.xyz', '123')

if __name__ == '__main__':
    config = Config()
    SQLHandle.CreateTables()
    #AlwaysRun()
    app.run(host='0.0.0.0')
