import ResponseHandle, SQLHandle
import jwt
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '*EtG*J 8);lJzP`HF}S5_v>aFLHX6D>qu)~&q5xF+rY{Fqixz,5A#h]M`Q%?+?gG'
def GetStudent(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'])
    temp_user = SQLHandle.student.query.filter_by(username=payload['username']).first()
    if(temp_user is not None):
        response = ResponseHandle.GenerateStudentResponse("student_get_success", temp_user.todict())
    else:
        response = ResponseHandle.GenerateResponse("student_get_failed")
    return response

def SetTotalPoints(student):
    total_points = 0
    if(student is not None):
        points = SQLHandle.point.query.filter_by(student_id=student.id)
        point_list = SQLHandle.GetListOfRows(points)
        if (point_list is not None):
            if(len(point_list) > 0):
                for point in point_list:
                    reward = SQLHandle.reward.query.filter_by(id=point['reward_id']).first()
                    if (reward is not None):
                        total_points = total_points + reward.value
                student.total_points = total_points
                SQLHandle.CommitSession()

def SubtractPoints(student, value):
    total_points = 0
    if(student is not None):
        student.total_points = student.total_points - value
        SQLHandle.CommitSession()

def ValidateStudentPasscode(token, passcode):
    payload = jwt.decode(token, app.config['SECRET_KEY'])
    student = SQLHandle.student.query.filter_by(username=payload['username']).first()
    if(student is not None):
        str_passcode = str(student.passcode)
        if(passcode == str_passcode):
            print "SUCCESS"
            response = ResponseHandle.GenerateResponse('passcode_success')
        else:
            response = ResponseHandle.GenerateResponse('passcode_incorrect')
    else:
        response = ResponseHandle.GenerateResponse('passcode_incorrect')

    return response

def ValidateTutorPasscode(passcode, tutor_id):
    print passcode
    print tutor_id
    tutor = SQLHandle.student.query.filter_by(id=tutor_id).first()
    if(tutor is not None):
        str_passcode = str(tutor.passcode)
        if(passcode == str_passcode):
            print "SUCCESS"
            response = True
        else:
            print "Failed because not match"
            response = False
    else:
        print "not found"
        response = False

    return response