from flask import Flask, request
from ConfigHandle import Config
import SQLHandle, RegistrationHandle, LoginHandle, ResponseHandle
app = Flask(__name__)
app.config['SECRET_KEY'] = '*EtG*J 8);lJzP`HF}S5_v>aFLHX6D>qu)~&q5xF+rY{Fqixz,5A#h]M`Q%?+?gG'
app.config['SECURITY_PASSWORD_SALT'] = 'Q?DLx(M-)8er&cbx*|ZJTNAjNt{rm69-g?yc%U=dNsho8QG6Z~twkM`^GU(]+EJA'

@app.route('/api')
def hello_world():
    return 'Hello World!'

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
    RegistrationHandle.SendAuthEmail(0,0)

if __name__ == '__main__':
    config = Config()
    ResponseHandle.PrintResponses()
    SQLHandle.CreateTables()
    app.run(host='0.0.0.0')
    AlwaysRun()
