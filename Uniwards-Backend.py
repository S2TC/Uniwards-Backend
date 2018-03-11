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
    if(LoginHandle.TokenVerification(request.headers['Token'])):
        response = RegistrationHandle.RegisterStudent(request.form)
    else:
        response = ResponseHandle.GenerateResponse('bad_token')

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
