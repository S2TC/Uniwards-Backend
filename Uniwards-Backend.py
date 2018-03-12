from flask import Flask, request
from ConfigHandle import Config
import SQLHandle, RegistrationHandle, LoginHandle, ResponseHandle
app = Flask(__name__)

@app.route('/api')
def hello_world():
    AlwaysRun()
    return 'Hello World!'

@app.route('/api/auth_user/<int:auth_token>')
def AuthUser(auth_token):
    if(RegistrationHandle.VerifyStudentEmailAuth(auth_token)):
        return 'Confirmed'
    else:
        return 'Shit hit the fan'

@app.route('/api/registeruser', methods = ['POST'])
def RegisterUser():
    response = LoginHandle.TokenCheckStub(request.headers['Token'])
    if(response is not 1 and response is not 'Expired'):
        response = RegistrationHandle.RegisterStudent(request.form)
    else:
        response = ResponseHandle.GenerateResponse('registration_already_registered')

    return response[0], response[1]

@app.route('/api/studentlogin', methods = ['POST'])
def StudentLogin():
    response = LoginHandle.TokenCheckStub(request.headers['Token'])
    if(response == 1):
        response = LoginHandle.StudentLogin(request.form)

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
    ResponseHandle.PrintResponses()
    SQLHandle.CreateTables()
    #AlwaysRun()
    app.run(host='0.0.0.0')
