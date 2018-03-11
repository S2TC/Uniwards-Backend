from flask import Flask, request
from ConfigHandle import Config
import SQLHandle
import RegistrationHandle
app = Flask(__name__)


@app.route('/api/')
def hello_world():
    return 'Hello World!'

@app.route('/api/registeruser', methods = ['POST'])
def RegisterUser():
    RegistrationHandle.RegisterUser(email, "test", 1)
    return '', 201

if __name__ == '__main__':
    config = Config()
    SQLHandle.CreateTables()
    SQLHandle.CommitSession()
    uni = SQLHandle.University(1, "test", "test", "1234")
    SQLHandle.InsertRowObject(uni)
    SQLHandle.CommitSession()
    uni2 = SQLHandle.University.query.all()
    print(uni2[0].mobile_no)
    app.run()
