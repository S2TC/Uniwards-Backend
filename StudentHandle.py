import ResponseHandle, SQLHandle

def GetStudent(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'])
    temp_user = SQLHandle.student.query.filter_by(username=payload['username'])
    if(temp_user is not None):
        temp_user.password = ""
        response = ResponseHandle.GenerateStudentResponse("student_get_success", temp_user)
    else:
        response = ResponseHandle.GenerateResponse("student_get_failed")
    return response