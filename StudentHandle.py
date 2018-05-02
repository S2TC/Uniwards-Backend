import ResponseHandle, SQLHandle
import jwt
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '*EtG*J 8);lJzP`HF}S5_v>aFLHX6D>qu)~&q5xF+rY{Fqixz,5A#h]M`Q%?+?gG'
def GetStudent(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'])
    temp_user = SQLHandle.student.query.filter_by(username=payload['username']).first()
    if(temp_user is not None):
        temp_user.password = ""
        response = ResponseHandle.GenerateStudentResponse("student_get_success", temp_user.todict())
    else:
        response = ResponseHandle.GenerateResponse("student_get_failed")
    return response