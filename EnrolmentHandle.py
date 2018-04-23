import ResponseHandle, SQLHandle

def GetEnrolmentsByStudentID(student_id):
    temp_enrolments = SQLHandle.enrolled.query.filter_by(student_id=student_id)
    enrolment_list = SQLHandle.GetListOfRows(temp_enrolments)
    if (enrolment_list is not None):
        if(len(enrolment_list) > 0):
            response = ResponseHandle.GenerateEnrolmentsResponse(enrolment_list)
        else:
            response = ResponseHandle.GenerateResponse('enrolment_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('enrolment_get_failed')

    return response


def GetEnrolmentsByClassID(class_id):
    temp_enrolments = SQLHandle.enrolled.query.filter_by(class_id=class_id)
    enrolment_list = SQLHandle.GetListOfRows(temp_enrolments)
    if (enrolment_list is not None):
        if(len(enrolment_list) > 0):
            response = ResponseHandle.GenerateEnrolmentsResponse(enrolment_list)
        else:
            response = ResponseHandle.GenerateResponse('enrolment_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('enrolment_get_failed')

    return response


def GetEnrolments():
    temp_enrolments = SQLHandle.enrolled.query.all()
    enrolment_list = SQLHandle.GetListOfRows(temp_enrolments)
    if (enrolment_list is not None):
        if(len(enrolment_list) > 0):
            response = ResponseHandle.GenerateEnrolmentsResponse(enrolment_list)
        else:
            response = ResponseHandle.GenerateResponse('enrolment_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('enrolment_get_failed')

    return response


def RegisterEnrolment(req_data):
    temp_enrolment = SQLHandle.enrolled(class_id=req_data['class_id'], student_id=req_data['code'],
                                         date=req_data['date'])
    if(SQLHandle.InsertRowObject(temp_enrolment)):
        response = ResponseHandle.GenerateResponse('enrolment_register_success')
    else:
        response = ResponseHandle.GenerateResponse('enrolment_register_failed')
    return response


def UpdateEnrolment(req_data):
    pass


def DeleteEnrolment(req_data):
    pass


def __init__(self, class_id, student_id, date):
    self.class_id = class_id
    self.student_id = student_id
    self.date = date